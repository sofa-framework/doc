MechanicalObject
================

The main component of a simulation in SOFA is the _MechanicalObject_. It inherits from _MechanicalState_, itself inheriting from _State_.


State vectors
-------------

The _MechanicalObject_ (MechanicalState) saves all the state vectors. These state vectors correspond to the degrees of freedom (DOFs) and their first time derivative. The vector size is the number of nodes, and the size of each vector entry depends on the template (see below).

**Note**: the SOFA framework being historically focused on soft tissue mechanics, the semantic is strongly related to mechanics. The state vectors (DOFs) are stored in the field named _position_, their first derivatives in the _velocity_ field and their second derivatives in the _acceleration_ field.


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



List of state vectors (MultiVec)
--------------------------------

<table>
<tbody>
  <tr>
    <td></td>
    <td>Vector name<br></td>
    <td>Vector type</td>
    <td>Description</td>
  </tr>
  <tr>
    <td rowspan="5">State</td>
    <td>position</td>
    <td>VecCoord</td>
    <td>current coordinates of the degrees of freedom</td>
  </tr>
  <tr>
    <td>velocity</td>
    <td>VecDeriv</td>
    <td>current first derivative in time of the coordinates of the degrees of freedom</td>
  </tr>
  <tr>
    <td>derivX</td>
    <td>VecDeriv</td>
    <td>x vector of the linear system Ax=b (therefore depends on the integration scheme)</td>
  </tr>
  <tr>
    <td>reset_position</td>
    <td>VecCoord</td>
    <td>coordinates of the degrees of freedom used for reset</td>
  </tr>
  <tr>
    <td>reset_velocity</td>
    <td>VecDeriv</td>
    <td>first derivative in time of the coordinates of the degrees of freedom used for reset</td>
  </tr>
  <tr>
    <td rowspan="3">Force</td>
    <td>force</td>
    <td>VecDeriv</td>
    <td>b vector of the linear system Ax=b (therefore depends on the integration scheme)</td>
  </tr>
  <tr>
    <td>externalForce</td>
    <td>VecDeriv</td>
    <td>vector containing only forces resulting from InteractionForceFields and some constraint forces</td>
  </tr>
  <tr>
    <td>dforce</td>
    <td>VecDeriv</td>
    <td>vector corresponding to the derivative of the forces (<em>no much use in the code base</em>)</td>
  </tr>
  <tr>
    <td>Rest State</td>
    <td>rest_position</td>
    <td>VecCoord</td>
    <td>coordinates of the degrees of freedom when the object is at rest (no force acting)</td>
  </tr>
  <tr>
    <td rowspan="2">FreeMotion</td>
    <td>free_position</td>
    <td>VecCoord</td>
    <td>in the FreeMotionAnimationLoop, coordinates of the degrees of freedom as if no collision would be taken into account (free motion)</td>
  </tr>
  <tr>
    <td>free_velocity</td>
    <td>VecDeriv</td>
    <td>in the FreeMotionAnimationLoop, first derivative in time of the coordinates of the degrees of freedom as if no collision would be taken into account (free motion)</td>
  </tr>
  <tr>
    <td rowspan="2">Jacobian</td>
    <td>constraint</td>
    <td>MatrixDeriv</td>
    <td>matrix containing the constraint directions, i.e. derivative of the constraint laws</td>
  </tr>
  <tr>
    <td>mappingJacobian</td>
    <td>MatrixDeriv</td>
    <td>matrix accumulating the Jacobian matrices of mappings, used only in the MechanicalMatrixMapper</td>
  </tr>
</tbody>
</table>



Symbolic ids
------------

The MultiVec entries are not directly accessible by the solvers. The MultiVec are represented by identificators. The operations on the vectors are implemented using visitors which contain the identificators of the relevant vectors. The MultiVec identificators (MultiVecId) have different types, depending on the data they contain
(positions or their derivatives) and the access mode.

The use of symbolic identificators (MultiVecId) prevent other components (like solvers) from handling state vectors directly and allow to easily work with abstract MultiVec by using their ids. These symbolic ids are widely used by specialized visitors, like the ones used in [ODESolver](./system-resolution/integration-scheme/).

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
<Node name="root" dt="0.01" >
    <DefaultAnimationLoop />
    <MechanicalObject template="Vec3d" name="myDOFs" position="0 0 0"/>
</Node>
```

The C++ templates avoid code redundancy between scalar types and DOFs types. All nodes in a vector have the same type, known at compilation time to allow aggressive compiler optimizations. Nodes with different DOFs must be stored in two different _MechanicalObjects_.

