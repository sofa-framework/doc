The main component of a simulation in SOFA is the _MechanicalObject_. It inherits from _MechanicalState_, which saves all the state vectors, namely the degrees of freedom (DOFs), their associated velocity, acceleration and the forces applied on the simulated body. By gathering all state vectors, the _MechanicalObject_ avoids multiple calls of virtual functions. The vector size is the number of nodes, and the size of each vector entry depends on the template (see below).

The SOFA framework was historically focused on soft tissue mechanics. Therefore, the semantic is strongly related to mechanics. The component saving the DOFs is called _MechanicalObject_. In this class, the state vectors (DOFs) are stored in the _position_ field, their first derivatives in the _velocity_ field and their second derivatives in the _acceleration_ field. These state vectors 

Templates
---------

In this _MechanicalObject_, we need to specify the type of DOFs. It supports several templates depending on these DOFs:

*   _Vec1f_ or _Vec1d_: 1 DOF per node is used. For instance, this can be used for thermodynamics (temperature field). Vec1f denotes vectors of float and Vec1d denotes the use of doubles.
*   _Vec2f_ or _Vec2d_: 2 DOFs per node are used. For instance, this can be used for cardiac electrophysiology.
*   _Vec3f_ or _Vec3d_: 3 DOFs per node are used. For instance, this can be used for mechanics.
*   _Vec6f_ or _Vec6d_: 6 DOFs per node are used. For instance, this can be used for beam simulations (3 translations and 3 rotations).
*   _Rigid_: this DataType corresponds to 7 DOFs per node, this can be used to simulate rigid bodies (3 positions and 1 quaternion).

In an XML format, this would be written as follows:
```xml
<Node name="root" dt="0.01" gravity="0 -9.81 0">
    <DefaultAnimationLoop />
    <MechanicalObject template="Vec3f" name="myDOFs" />
</Node>
```

The C++ templates avoid code redundancy between scalar types and DOFs types. All nodes in a vector have the same type, known at compilation time to allow agressive compiler optimizations. Nodes with different DOFs must be stored in two different _MechanicalObjects_.