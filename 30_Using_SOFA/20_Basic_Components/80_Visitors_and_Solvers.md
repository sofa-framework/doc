We implement the simulation using visitors which traverse the scene
top-down and bottom-up, and call the corresponding virtual functions at
each graph node traversal. Algorithmic operations on the simulated
objects are implemented by deriving the Visitor class and overloading
its virtual functions processNodeTopDown( ) and processNodeBottomUp( ).
Time stepping is implemented using the AnimateVisitor, which passes the
control to an AnimationLoop, which schedules collision detection and ODE
solution. ODE solvers control an arbitrary number of simulated objects
through abstract methods implemented by specialized visitors, and
symbolic vector identificators. The symbolic vector ids allow to
represent global state vectors, such as positions, while leaving all the
actual state vectors in the local MechanicalState of the simulated
objects.

More on Solvers
---------------

There are two categories of solvers. ODE solvers (derived from
core::behavior::OdeSolver), which goal is to advance the objects in
time, may use auxiliary linear solvers (derived from
core::behavior::BaseLinearSolver) to solve linear equations. In the
following, we focus on ode solvers, though some info also applies to
linear solvers. The goal of ode solvers is to advance objects in time.
Most of them used to do it by solving an Ordinary Differential Equation,
hence the name of the namespace odesolver. However, other animation
algorithms, from simple keyframe interpolation to complex Differential
Algebraic Equation (DAE) solvers may fit in this category. The solver
does not access the state vectors directly. It accesses the state
vectors remotely using visitors, which traverse the graph starting from
the node which contains the solver. This keeps the implementation of the
solver independent from the simulated objects and their types. The set
of components reachable by the visitors sent by the solver is called the
scope of the solver. The solver animates only the objects within its
scope. The scope contains an arbitray number of simulated objects, of
arbitrary types. The solver drives a dynamical system represented by the
state vectors of the simulated objects. The state vectors are contained
in the different component::container::MechanicalOblect components (or,
more generally, core::State components). The solver remotely address
abstract (scattered) state vectors, called multi-vectors or MultiVec.
For instance, the position vector is the union of all the position
vectors of the objects. The multivec entries are not directly accessible
by the solvers. The multivec are represented by identificators. The
operations on the vectors are implemented using visitors which contain
the identificators of the relevant vectors. The multivec identificators
(MultiVecId) have different types, depending on the data they contain
(positions or their derivatives) and the access mode, e.g.:

``` cpp
typedef TMultiVecId<V_COORD, V_READ> ConstMultiVecCoordId;
typedef TMultiVecId<V_COORD, V_WRITE>     MultiVecCoordId;
typedef TMultiVecId<V_DERIV, V_READ> ConstMultiVecDerivId;
typedef TMultiVecId<V_DERIV, V_WRITE>     MultiVecDerivId;
```

For simplicity, some standard state vectors are represented using
constant ids:

``` cpp
template
class TStandardVec
{
public:
    typedef TVecId MyVecId;
    static MyVecId position()      { return MyVecId(1);}
    static MyVecId restPosition()  { return MyVecId(2);}
    static MyVecId freePosition()  { return MyVecId(3);}
    static MyVecId resetPosition() { return MyVecId(4);}
    enum { V_FIRST_DYNAMIC_INDEX = 5 }; ///< This is the first index used for dynamically allocated vectors
…
};
template
class TStandardVec
{
public:
    typedef TVecId MyVecId;
    static MyVecId velocity()       { return MyVecId(1); }
    static MyVecId resetVelocity()  { return MyVecId(2); }
    static MyVecId freeVelocity()   { return MyVecId(3); }
    static MyVecId normal()         { return MyVecId(4); }
    static MyVecId force()          { return MyVecId(5); }
    static MyVecId externalForce()  { return MyVecId(6); }
    static MyVecId dx()             { return MyVecId(7); }
    static MyVecId dforce()         { return MyVecId(8); }
    static MyVecId accFromFrame()   { return MyVecId(9); }
    enum { V_FIRST_DYNAMIC_INDEX = 11 }; ///< This is the first index used for dynamically allocated vectors
...
};
```

Each type of solver may use different auxiliary state vectors to
implement their simulation method. State vectors are allocated and
processed in the scope of the solver in a thread-safe way using an
instance of simulation::common::VectorOperations. For example:

``` cpp
MultiVecCoord pos(&vop, core::VecCoordId::position() ); // standard position vector, write access
MultiVecDeriv acc(&vop);   // auxiliary vector
```

Each object is composed of a set of particles of the same type
(typically 3d particles or 6d rigid bodies). These types and their
containers are represented in DataTypes (such as StdVectorTypes,
RigidTypes). The state vectors are stored in a dedicated component,
typically MechanicalObject derived from State. The visitors which
implement mechanical operations derive from MechanicalVisitor. They
contain a MultVecId which represent the result state vector of the
operation (such as force or acceleration), as well as a MechanicalParams
which contains the MultiVecIds of the vectors the component may have to
read, such as position or velocity. The component functions called by
MechanicalVisitor get the MechanicalParams and the result MultiVecId as
parameters. They use this information to access the state vectors stored
in the local State component. The state vectors, like other component
data, are stored in Data containers which control their access,
connections and serialization. The vector Data containers provide
different ways of accessing their vectors, see the wiki page.

From symbolic Ids to concrete state vectors
-------------------------------------------

The translation from the symbolic ids to the actual DOF is performed
using two levels of abstraction above the concrete class:

-   the most abstract level represents concepts, such as force function,
    or mass, independently of the actual DOF types. Example:
    core::behavior::BaseForceField
-   the second level, deriving from the first, represents the concept
    applied to a given type of DOF.
    Example: core::behavior::ForceField&lt;&gt;. This template class is
    instanciated on various concrete DOF types such as 1d, 2d and 3d
    particles, 2d and 3d rigid bodies.
-   the concrete classes derive from the second abstract level.
    Example: TetrahedralFEMForceField&lt;&gt;.

During the traversal, - the visitor passes the symbolic vector ids to
the virtual method of a pointer to the highest abstract level. - the
actual implementation is in the second level, which knows the actual DOF
types, queries the corresponding vector(s) from the local
MechanicalState, and passes them to an abstract method with vector
parameters. - the concrete class implements the method. For example, let
us consider the accumulation of force in a given state vector by the
EulerSolver:

-   a vector identificator is created in method solve(const
    core::ExecParams\* params, double dt, sofa::core::MultiVecCoordId
    xResult, sofa::core::MultiVecDerivId vResult)

    ``` cpp
    MultiVecDeriv fId  (&vop, core::VecDerivId::force() );
    ```

-   then method computeForce(core::MultiVecDerivId fId, bool clear,
    bool accumulate) is called, which creates and launches an
    appropriate visitor parameterized using the vector id:

    ``` cpp
    executeVisitor( MechanicalComputeForceVisitor(&mparams, fId, accumulate) )
    ```

    (the parameter is actually a pointer to the visitor)

-   the visitor traverses the scene and applies its
    fwdForceField(simulation::Node\*,
    core::behavior::BaseForceField\* ff) to each (top-level) abstract
    force function

    ``` cpp
    ff->addForce(this->mparams, fId)
    ```

-   Virtual method addForce(const MechanicalParams\*, MultiVecDerivId)
    is actually implemented by ForceField&lt;&gt;, which queries the
    vectors and passes them to a virtual method with actual parameters

    ``` cpp
    addForce(mparams, *fId[mstate.get(mparams)].write() , *mparams->readX(mstate), *mparams->readV(mstate));
    ```

    The pointer mstate to the local MechanicalState was queried
    at initialization. Note that the Id of the force vector is
    explicitly passed as parameter to the abstract functions, while the
    Ids of the position and velocity vectors are stored in mparams. More
    generally, the output vector ids are passed explicitly, while the
    input vector Ids are stored in the MechanicalParameters, because not
    all components use the same input vectors to compute a given output
    vector. Finally, the concrete implementation of the method is
    provided by the concrete class

 
