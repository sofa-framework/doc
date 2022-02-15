MechanicalObject
================

The main component of a simulation in SOFA is the _MechanicalObject_. It inherits from _MechanicalState_, itself inheriting from _State_.


State vectors
-------------

The _MechanicalState_ saves all the state vectors, namely the degrees of freedom (DOFs), their associated velocity, acceleration and the forces applied on the simulated body. By gathering all state vectors, the _MechanicalObject_ avoids multiple calls of virtual functions. The vector size is the number of nodes, and the size of each vector entry depends on the template (see below).

**Note**: the SOFA framework was historically focused on soft tissue mechanics. Therefore, the semantic is strongly related to mechanics. In the _MechanicalObject_, the state vectors (DOFs) are stored in the field named _position_, their first derivatives in the _velocity_ field and their second derivatives in the _acceleration_ field.



Templates
---------

The state vectors can contain different type of data depending on the degrees of freedom (DOFs). In order to provide generic implementation, components (C++ classes) in SOFA will be templated on **DataTypes**.

SOFA supports several DataTypes corresponding to the DOFs:

*   _Vec1f_ or _Vec1d_: 1 DOF per node is used. For instance, this can be used for thermodynamics (temperature field). Vec1f denotes vectors of float and Vec1d denotes the use of doubles.
*   _Vec2f_ or _Vec2d_: 2 DOFs per node are used. For instance, this can be used for cardiac electrophysiology.
*   _Vec3f_ or _Vec3d_: 3 DOFs per node are used. For instance, this can be used for mechanics.
*   _Vec6f_ or _Vec6d_: 6 DOFs per node are used. For instance, this can be used for beam simulations (3 translations and 3 rotations).
*   _Rigid3d_: this DataType corresponds to 7 DOFs per node, this can be used to simulate rigid bodies (3 positions and 1 quaternion).



In the _MechanicalObject_, each of these state vectors can be accessed using (scattered) state vectors, called multi-vectors or MultiVec. 


Symbolic ids
------------

The MultiVec entries are not directly accessible by the solvers. The MultiVec are represented by identificators. The operations on the vectors are implemented using visitors which contain the identificators of the relevant vectors. The MultiVec identificators (MultiVecId) have different types, depending on the data they contain
(positions or their derivatives) and the access mode, e.g.:

The use of symbolic identificators (MultiVecId) prevent other components (like solvers) from handling state vectors directly and allow to easily work with abstract MultiVec by using their ids. These symbolic ids are widely used by specialized visitors, like the ones used in [ODESolver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/integration-schemes/).

``` cpp
typedef TMultiVecId<V_COORD, V_READ>  ConstMultiVecCoordId;
typedef TMultiVecId<V_COORD, V_WRITE>      MultiVecCoordId;
typedef TMultiVecId<V_DERIV, V_READ>  ConstMultiVecDerivId;
typedef TMultiVecId<V_DERIV, V_WRITE>      MultiVecDerivId;
```


For simplicity, standard state vectors are represented using constant identificators:

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



Example
-------

In an XML format, this would be written as follows:
```xml
<Node name="root" dt="0.01" gravity="0 -9.81 0">
    <DefaultAnimationLoop />
    <MechanicalObject template="Vec3f" name="myDOFs" />
</Node>
```

The C++ templates avoid code redundancy between scalar types and DOFs types. All nodes in a vector have the same type, known at compilation time to allow aggressive compiler optimizations. Nodes with different DOFs must be stored in two different _MechanicalObjects_.

