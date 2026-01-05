---
title: StaticSolver
---

StaticSolver  
============  

This component belongs to the category of [integration schemes or ODE Solver](../../../../simulation-principles/system-resolution/integration-scheme/).  

In the field of mechanics, statics consists in finding the equilibrium taking into account the loads (internal forces, external forces and torques) acting on the physical system, that do not experience an acceleration ( $a=0$ ). Finding a static equilibrium means finding a solution to: $\textstyle \sum F=0$ where $F$ is the sum of all loads, one of which might be unknown.  

In a static analysis, the inertia and damping effects are ignored, i.e. the dynamic effect of the mass is ignored. It can thus be written: $M=I \alpha=0$. In the same way, when running a static simulation, time is not elapsing and time steps should rather be considered as convergence steps.  

In a static simulation involving elasticity, the linear system that we solve corresponds to $K \Delta u=f$ where $K$ is the stiffness matrix (derivative of elastic forces), $\Delta u$ is a vector describing the total increment of displacement and $f$ are all explicit forces. We realize here that the static solver is in fact an implicit scheme, since the $K$ matrix is present in the left-hand side of the equation. The solution $\Delta u$ is obtained iteratively. At each iteration _i_, the displacement is incremented $\Delta u_{i+1}=\Delta u_{i}+\delta u_i$, thus resulting in the following system to solve: $K_i \delta u_i=f$.  

In case of non-linear elasticity, $K_i$ is a linearization which must be updated with regards to the increment of displacement $\delta u_i$. In such cases, several iterations of Newton Raphson are required to find an appropriate approximate solution. In one step of the StaticSolver, the number of Newton Raphson iterations is ruled by the data field **newton_iterations**.

_Reminder_: the [Newton Raphson method](https://en.wikipedia.org/wiki/Newton%27s_method) is an iterative algorithm aiming at finding the solution of the system $f(x)=0$ where $f(x)$ is non-linear. At each iteration of Newton Raphson algorithm, we find a new approximate solution:

$x^{n+1}=x^n-\frac{f(x^n)}{f'(x^n)}$ where $f'(x^n) = \frac{df}{dx}(x^n)$

In our elasticity case, the system to solve is $K_i \delta u_i-f=0$. At each iteration of Newton Raphson algorithm $n$ at simulation step $i$, we therefore find:

$$
\delta u_i^{n+1}=\delta u_i^{n}-\frac{(K_i^n \delta u_i^n-f)}{K_i^n}
$$


Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/StaticSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/StaticSolver.png?raw=true" title="Flow diagram for the StaticSolver"/></a>

 
Usage  
-----  

At each simulation step and each Newton Raphson iteration, the StaticSolver **requires**:

- a [LinearSolver](../../../../simulation-principles/system-resolution/linear-solver/) to solve the linear system
- and a MechanicalObject to store the state vectors.

A StaticSolver must be used in simulations where the dynamics has no or a negligible effect on the system. A StaticSolver would also be relevant for systems with low mass. In such case, we fall into the quasi-static analysis.

In some loading configuration, applying the full forces and torques might not lead to any converging simulation. It is then relevant to go for an incremental loading, i.e. loads are applied incrementally at each simulation step  $i$. This incremental loading has to be done in the associated ForceField. If you want to use this solver with Newton Raphson iterations, it is in the user's hand to make sure the external forces used in the scene (pressure, traction, etc.) only get incremented at each time step, and not at each calls to addForce (which is currently the case for most force fields).
<!-- automatically generated doc START -->
<!-- generate_doc -->

Static ODE Solver


__Target__: Sofa.Component.ODESolver.Backward

__namespace__: sofa::component::odesolver::backward

__parents__:

- OdeSolver
- LinearSolverAccessor

### Data

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Default value</th>
        </tr>
    </thead>
    <tbody>
	<tr>
		<td>name</td>
		<td>
object name
		</td>
		<td>unnamed</td>
	</tr>
	<tr>
		<td>printLog</td>
		<td>
if true, emits extra messages at runtime.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>tags</td>
		<td>
list of the subsets the object belongs to
		</td>
		<td></td>
	</tr>
	<tr>
		<td>bbox</td>
		<td>
this object bounding box
		</td>
		<td></td>
	</tr>
	<tr>
		<td>componentState</td>
		<td>
The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
		</td>
		<td>Undefined</td>
	</tr>
	<tr>
		<td>listening</td>
		<td>
if true, handle the events, otherwise ignore the events
		</td>
		<td>0</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|linearSolver|Linear solver used by this component|LinearSolver|
|newtonSolver|Link to a NewtonRaphsonSolver|NewtonRaphsonSolver|

## Examples 

StaticSolver.scn

=== "XML"

    ```xml
    <Node name="root" gravity="-1.8 0 100"  dt="1">
        <Node name="plugins">
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader MeshOBJLoader] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [EigenSimplicialLDLT] -->
            <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [NewtonRaphsonSolver StaticSolver] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [MeshSpringForceField] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
            <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
            <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        </Node>
        <DefaultAnimationLoop parallelODESolving="true"/>
    
        <VisualStyle displayFlags="hideBehaviorModels hideCollisionModels hideMappings hideForceFields" />
    
        <Node name="Reference">
            <MeshOBJLoader name="meshLoader_1" filename="mesh/truthcylinder1-bent.obj" scale="0.95" handleSeams="1" />
            <OglModel src="@meshLoader_1" dx="0" dy="-1" dz="0" color="green" />
        </Node>
    
        <MeshGmshLoader name="loader" filename="mesh/truthcylinder1.msh" />
    
        <Node name="Springs">
            <NewtonRaphsonSolver name="newtonSolver_springs" maxNbIterationsNewton="100"
                                 maxNbIterationsLineSearch="1" warnWhenLineSearchFails="false"/>
            <StaticSolver newtonSolver="@newtonSolver_springs"/>
            <EigenSimplicialLDLT template="CompressedRowSparseMatrixMat3x3"/>
    
            <MeshTopology src="@../loader" />
            <MechanicalObject src="@../loader" dx="15" />
            <UniformMass totalMass="15" />
            <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345" />
            <MeshSpringForceField name="Spring" tetrasStiffness="1870" tetrasDamping="0" />
            <Node>
                <MeshOBJLoader name="meshLoader_0" filename="mesh/truthcylinder1.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_0" color="yellow" dx="15" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
        </Node>
        <Node name="CoFEM">
            <NewtonRaphsonSolver name="newtonSolver_corot" maxNbIterationsNewton="100"
                                 maxNbIterationsLineSearch="1" warnWhenLineSearchFails="false"/>
            <StaticSolver newtonSolver="@newtonSolver_corot"/>
            <EigenSimplicialLDLT template="CompressedRowSparseMatrixMat3x3"/>
    
            <MeshTopology src="@../loader" />
            <MechanicalObject src="@../loader" dx="30" />
            <UniformMass totalMass="15" />
            <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1116" poissonRatio="0.49" method="large" />
            <Node>
                <MeshOBJLoader name="meshLoader_3" filename="mesh/truthcylinder1.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_3" color="cyan" dx="30" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
        </Node>
        <Node name="LinearFEM">
            <NewtonRaphsonSolver name="newtonSolver_lin" maxNbIterationsNewton="100"
                                 maxNbIterationsLineSearch="1" warnWhenLineSearchFails="false"/>
            <StaticSolver newtonSolver="@newtonSolver_lin"/>
            <EigenSimplicialLDLT template="CompressedRowSparseMatrixMat3x3"/>
    
            <MeshTopology src="@../loader" />
            <MechanicalObject src="@../loader" dx="45" />
            <UniformMass totalMass="15" />
            <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1116" poissonRatio="0.49" method="small" />
            <Node>
                <MeshOBJLoader name="meshLoader_2" filename="mesh/truthcylinder1.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_2" color="red" dx="45" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="-1.8 0 100", dt="1")

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       plugins.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")

       root.addObject('DefaultAnimationLoop', parallelODESolving="true")
       root.addObject('VisualStyle', displayFlags="hideBehaviorModels hideCollisionModels hideMappings hideForceFields")

       reference = root.addChild('Reference')

       reference.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/truthcylinder1-bent.obj", scale="0.95", handleSeams="1")
       reference.addObject('OglModel', src="@meshLoader_1", dx="0", dy="-1", dz="0", color="green")

       root.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")

       springs = root.addChild('Springs')

       springs.addObject('NewtonRaphsonSolver', name="newtonSolver_springs", maxNbIterationsNewton="100", maxNbIterationsLineSearch="1", warnWhenLineSearchFails="false")
       springs.addObject('StaticSolver', newtonSolver="@newtonSolver_springs")
       springs.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrixMat3x3")
       springs.addObject('MeshTopology', src="@../loader")
       springs.addObject('MechanicalObject', src="@../loader", dx="15")
       springs.addObject('UniformMass', totalMass="15")
       springs.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345")
       springs.addObject('MeshSpringForceField', name="Spring", tetrasStiffness="1870", tetrasDamping="0")

       node = Springs.addChild('node')

       node.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/truthcylinder1.obj", handleSeams="1")
       node.addObject('OglModel', name="Visual", src="@meshLoader_0", color="yellow", dx="15")
       node.addObject('BarycentricMapping', input="@..", output="@Visual")

       co_fem = root.addChild('CoFEM')

       co_fem.addObject('NewtonRaphsonSolver', name="newtonSolver_corot", maxNbIterationsNewton="100", maxNbIterationsLineSearch="1", warnWhenLineSearchFails="false")
       co_fem.addObject('StaticSolver', newtonSolver="@newtonSolver_corot")
       co_fem.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrixMat3x3")
       co_fem.addObject('MeshTopology', src="@../loader")
       co_fem.addObject('MechanicalObject', src="@../loader", dx="30")
       co_fem.addObject('UniformMass', totalMass="15")
       co_fem.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345")
       co_fem.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1116", poissonRatio="0.49", method="large")

       node = CoFEM.addChild('node')

       node.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/truthcylinder1.obj", handleSeams="1")
       node.addObject('OglModel', name="Visual", src="@meshLoader_3", color="cyan", dx="30")
       node.addObject('BarycentricMapping', input="@..", output="@Visual")

       linear_fem = root.addChild('LinearFEM')

       linear_fem.addObject('NewtonRaphsonSolver', name="newtonSolver_lin", maxNbIterationsNewton="100", maxNbIterationsLineSearch="1", warnWhenLineSearchFails="false")
       linear_fem.addObject('StaticSolver', newtonSolver="@newtonSolver_lin")
       linear_fem.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrixMat3x3")
       linear_fem.addObject('MeshTopology', src="@../loader")
       linear_fem.addObject('MechanicalObject', src="@../loader", dx="45")
       linear_fem.addObject('UniformMass', totalMass="15")
       linear_fem.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345")
       linear_fem.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1116", poissonRatio="0.49", method="small")

       node = LinearFEM.addChild('node')

       node.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/truthcylinder1.obj", handleSeams="1")
       node.addObject('OglModel', name="Visual", src="@meshLoader_2", color="red", dx="45")
       node.addObject('BarycentricMapping', input="@..", output="@Visual")
    ```


<!-- automatically generated doc END -->
