This page presents the basic components required to simulate a single object.

The animation loop
------------------

Any simulation in SOFA is ruled by an animation loop. This component manages the different steps of the simulation, i.e. the animation loop makes the simulation run from one time step to the next, and at each time step, it triggers the solving of the system and the associated constraints. If no animation loop is defined in the scene, a "DefaultAnimationLoop" is automatically created.

In an XML format, this would be written as follows:
```xml
<Node name="root" dt="0.01" gravity="0 -9.81 0">
    <DefaultAnimationLoop />
</Node>
```

State vectors (DOFs)
--------------------

As described in [the introduction to state vectors](https://www.sofa-framework.org/community/doc/simulation-principles/mechanicalobject/#state-vectors), the degrees of freedom (DOFs) of your simulation are stored in state vectors. These vectors are managed by the main component of a simulation: the MechanicalObject. The SOFA framework was historically focused on soft tissue mechanics. Therefore, the semantic is strongly related to mechanics.

Depending on the physics (DOFs) you want to compute, you will have to choose the template of the MechanicalObject among: 1, 2, 3 or 6 reals per node, 1 rigid per node.

In an XML format, this would be written as follows:
```xml
<Node name="root" dt="0.01" gravity="0 -9.81 0">
    <DefaultAnimationLoop />
    <MechanicalObject template="Vec3f" name="myDOFs" />
</Node>
```

Solvers
-------

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

Physics
-------

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
