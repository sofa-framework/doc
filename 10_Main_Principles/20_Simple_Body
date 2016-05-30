This page presents the basic components required to simulate a single object.

#### The animation loop

Any simulation in SOFA is ruled by an animation loop. This component manages the different steps of the simulation, i.e. the animation loop makes the simulation run from one time step to the next, and at each time step, it triggers the solving of the system and the associated constraints. If no animation loop is defined in the scene, a "DefaultAnimationLoop" is automatically created.

In an XML format, this would be written as follows:
```xml
<Node name="root" dt="0.01" gravity="0 -9.81 0">
    <DefaultAnimationLoop />
</Node>
```

#### State vectors (DOFs)

The main component of a simulation in SOFA is the MechanicalObject. This component saves all the state vectors, namely the degrees of freedom (DOFs), their associated velocity, acceleration and the forces applied on the simulated body.

The SOFA framework was historically focused on soft tissue mechanics. Therefore, the semantic is strongly related to mechanics. The component saving the degrees of freedom is called "MechanicalObject", and the degrees of freedom are stored in the "position" field.

#### Templates

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

#### Solvers

To solve the mathematical system at each time step, solvers have to be defined. For dynamic simulations, you need to choose:

*   an integration scheme, or ODE solver: Euler explicit, implicit, Runge Kutta, etc. This schemes describes how to compute the next state based on the current one.
*   a linear solver: iterative (conjugate gradient) or direct (LU, LDL, etc.) to solve the linear system assembled by the previous integration scheme.

Discover more about how the mathematical system is solved in SOFA in the [associated page](https://www.sofa-framework.org/support/doc/).

In an XML format, this would be written as follows:
```xml
<Node name="root" dt="0.01" gravity="0 -9.81 0">
    <DefaultAnimationLoop />
    <EulerImplicitSolver rayleighStiffness="0.01"/>
    <CGLinearSolver iterations="100" tolerance="1e-06" threshold="1e-06"/>
    <MechanicalObject name="myRigidDOF" template="Rigid" position="0 0 0 0 0 0 0" />
</Node>
```

#### Physics

There is many different kind of physics available in SOFA, namely soft body mechanics but also thermodynamics and fluid dynamics. To run a physics simulation, all you need is to add the associated component in your scene.

If we consider an object with a mass under gravity, you will have to:

*   load your object (ex: a torus),
*   add the mass component (ex: DiagonalMass if you want to consider your mass matrix as diagonal)

In an XML format, this would be written as follows:
```xml
<Node name="root" dt="0.01" gravity="0 -9.81 0">
    <DefaultAnimationLoop />
    <EulerImplicitSolver rayleighStiffness="0.01"/>
    <CGLinearSolver iterations="100" tolerance="1e-06" threshold="1e-06"/>
    <MeshGmshLoader name="meshLoader" filename="torus.msh"/>

    <MechanicalObject name="myRigidDOF" template="Vec3d" src="@meshLoader" />
    <DiagonalMass densitymass="1.0"/>
</Node>
```

The gravity is defined in the root node, whereas the mass properties (density) are defined directly in the component.

Adding a deformable model (ex: linear elasticity for tetrahedral topology), this would be written:
```xml
<Node name="root" dt="0.01" gravity="0 -9.81 0">
    <DefaultAnimationLoop />
    <EulerImplicitSolver rayleighStiffness="0.01"/>
    <CGLinearSolver iterations="100" tolerance="1e-06" threshold="1e-06"/>
    <MeshGmshLoader name="meshLoader" filename="torus.msh"/>

    <MechanicalObject name="myRigidDOF" template="Vec3d" src="@meshLoader" />
    <DiagonalMass densitymass="1.0"/>
    <TetrahedronFEMForceField name="FEM" youngModulus="5000" poissonRatio="0.45"/>
</Node>
```

Now, you have your first physics simulation! To discover more about the simulation and the mechanisms of SOFA, you can visit:

*   the topology,
*   the system resolution,
*   the physics models (forcefields),
*   the mappings,
*   the constraints,
*   and the detection collision and response.
