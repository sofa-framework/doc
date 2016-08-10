The main component of a simulation in SOFA is the MechanicalObject. This component saves all the state vectors, namely the degrees of freedom (DOFs), their associated velocity, acceleration and the forces applied on the simulated body.

The SOFA framework was historically focused on soft tissue mechanics. Therefore, the semantic is strongly related to mechanics. The component saving the degrees of freedom is called "MechanicalObject", and the degrees of freedom are stored in the "position" field.

Templates
---------

In this MechanicalObject, we need to specify the type of degrees of freedom. The MechanicalObject can thus save either:

*   Vec1f or Vec1d: 1 DOF per node is used. For instance, this can be used for thermodynamics (temperature field). Vec1f denotes vectors of float and Vec1d denotes the use of doubles.
*   Vec2f or Vec2d: 2 DOFs per node are used. For instance, this can be used for cardiac electrophysiology.
*   Vec3f or Vec3d: 3 DOFs per node are used. For instance, this can be used for mechanics.
*   Vec6f or Vec6d: 6 DOFs per node are used. For instance, this can be used for beam simulations (3 translations and 3 rotations).
*   Rigid: this DataType corresponds to 7 DOFs per node, this can be used to simulate rigid bodies (3 positions and 1 quaternion).

In an XML format, this would be written as follows:
```xml
<Node name="root" dt="0.01" gravity="0 -9.81 0">
    <DefaultAnimationLoop />
    <MechanicalObject template="Vec3f" name="myDOFs" />
</Node>
```