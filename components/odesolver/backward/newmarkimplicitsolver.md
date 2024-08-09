---
title: NewmarkImplicitSolver
---

NewmarkImplicitSolver  
=====================

This component belongs to the category of [integration schemes or ODE Solver](../../../simulation-principles/system-resolution/integration-scheme/).  

This scheme is an implicit time integrator for dynamic system using the Newmark scheme. To compute the new position or new velocity, the NewmarkImplicitSolver is based on the following equations:

$$x_{t+h}=x_t+h v_t+\frac{h^2}{2}((1-2\beta)a_t+2\beta a_{t+h})$$

$$v_{t+h}=v_t+h((1-\gamma)a_t+\gamma a_{t+h})$$


Applied to a mechanical system where $$\small Ma_t+(r_MM+r_KK)v_t+Kx_t=f_{ext}$$, we need to solve the following system:


$$\tiny Ma_{t+h}+(r_MM+r_KK)v_{t+h}+Kx_{t+h}=f_{ext}$$

$$\tiny Ma_{t+h}+(r_MM+r_KK)(v_t+h((1-\gamma)a_t+\gamma a_{t+h}))+K(x_t+hv_t+\frac{h^2}{2}((1-2\beta)a_t+2\beta a_{t+h}))=f_{ext}$$

$$\tiny (M+h\gamma(r_MM+r_KK)+h^2\beta K)a_{t+h}=f_{ext}-(r_MM+r_KK)(v_t+h(1-\gamma)a_t)-K(x_t+hv_t+\frac{h^2(1-2\beta)}{2}a_t)$$

$$\tiny ((1+h\gamma r_M)M+(h^2\beta +h\gamma r_K)K)a_{t+h}=f_{ext}-(r_MM+r_KK)v_t-Kx_t-(r_MM+r_KK)(h(1-\gamma)a_t)-K(hv_t+\frac{h^2(1-2\beta)}{2}a_t)$$

$$\tiny ((1+h\gamma r_M)M+(h^2\beta+h\gamma r_K)K)a_{t+h}=a_t-(r_MM+r_KK)(h(1-\gamma)a_t)-K(hv_t+\frac{h^2(1-2\beta)}{2}a_t)$$



Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/NewmarkImplicitSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/NewmarkImplicitSolver.png?raw=true" title="Flow diagram for the NewmarkImplicitSolver"/></a>
 

Usage  
-----  

At each simulation step and each Newton Raphson iteration, the NewmarkImplicitSolver **requires**:

- a [LinearSolver](../../../simulation-principles/system-resolution/linear-solver/) to solve the linear system
- and a MechanicalObject to store the state vectors.
<!-- automatically generated doc START -->
__Target__: `Sofa.Component.ODESolver.Backward`

__namespace__: `#!c++ sofa::component::odesolver::backward`

__parents__: 

- `#!c++ OdeSolver`
- `#!c++ LinearSolverAccessor`

__categories__: 

- OdeSolver

Data: 

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
list of the subsets the objet belongs to
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
	<tr>
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping coefficient related to stiffness
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>rayleighMass</td>
		<td>
Rayleigh damping coefficient related to mass
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>vdamping</td>
		<td>
Velocity decay coefficient (no decay if null)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>gamma</td>
		<td>
Newmark scheme gamma coefficient
</td>
		<td>0.5</td>
	</tr>
	<tr>
		<td>beta</td>
		<td>
Newmark scheme beta coefficient
</td>
		<td>0.25</td>
	</tr>
	<tr>
		<td>threadSafeVisitor</td>
		<td>
If true, do not use realloc and free visitors in fwdInteractionForceField.
</td>
		<td>0</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|linearSolver|Linear solver used by this component|



## Examples

Component/ODESolver/Backward/NewmarkImplicitSolver.scn

=== "XML"

    ```xml
    <Node name="root" gravity="-1.8 0 100" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [SparseLDLSolver] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [NewmarkImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [MeshSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <DefaultAnimationLoop/>
        
        <Node name="Reference">
            <MeshOBJLoader name="meshLoader_0" filename="mesh/truthcylinder1-bent.obj" scale="0.95" handleSeams="1" />
            <OglModel src="@meshLoader_0" dx="0" dy="-1" dz="0" color="green" />
        </Node>
        <Node name="Springs">
            <NewmarkImplicitSolver rayleighMass="0" rayleighStiffness="0.1" />
            <SparseLDLSolver/>
            <MeshGmshLoader name="loader" filename="mesh/truthcylinder1.msh" />
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader" dx="15" />
            <UniformMass totalMass="15" />
            <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345" />
            <MeshSpringForceField name="Spring" tetrasStiffness="1870" tetrasDamping="0" />
    
            <Node>
                <MeshOBJLoader name="meshLoader_3" filename="mesh/truthcylinder1.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_3" color="yellow" dx="15" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
        </Node>
        
        <Node name="CoFEM">
            <NewmarkImplicitSolver rayleighMass="0" rayleighStiffness="0.1" />
            <CGLinearSolver iterations="100" tolerance="1e-5" threshold="1e-5"/>
            <MeshGmshLoader name="loader" filename="mesh/truthcylinder1.msh"/>
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader" dx="30" />
            <UniformMass totalMass="15" />
            <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1116" poissonRatio="0.49" method="polar" />
    
            <Node>
                <MeshOBJLoader name="meshLoader_2" filename="mesh/truthcylinder1.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_2" color="cyan" dx="30" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
        </Node>
        <Node name="LinearFEM">
            <NewmarkImplicitSolver rayleighMass="0" rayleighStiffness="0.1" />
            <CGLinearSolver iterations="100" tolerance="1e-5" threshold="1e-5"/>
            <MeshGmshLoader name="loader" filename="mesh/truthcylinder1.msh"/>
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader" dx="45" />
            <UniformMass totalMass="15" />
            <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1116" poissonRatio="0.49" method="small" />
    
            <Node>
                <MeshOBJLoader name="meshLoader_1" filename="mesh/truthcylinder1.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_1" color="red" dx="45" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="-1.8 0 100", dt="0.02")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')

        Reference = root.addChild('Reference')
        Reference.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/truthcylinder1-bent.obj", scale="0.95", handleSeams="1")
        Reference.addObject('OglModel', src="@meshLoader_0", dx="0", dy="-1", dz="0", color="green")

        Springs = root.addChild('Springs')
        Springs.addObject('NewmarkImplicitSolver', rayleighMass="0", rayleighStiffness="0.1")
        Springs.addObject('SparseLDLSolver')
        Springs.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
        Springs.addObject('MeshTopology', src="@loader")
        Springs.addObject('MechanicalObject', src="@loader", dx="15")
        Springs.addObject('UniformMass', totalMass="15")
        Springs.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345")
        Springs.addObject('MeshSpringForceField', name="Spring", tetrasStiffness="1870", tetrasDamping="0")

        Springs = Springs.addChild('Springs')
        Springs.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/truthcylinder1.obj", handleSeams="1")
        Springs.addObject('OglModel', name="Visual", src="@meshLoader_3", color="yellow", dx="15")
        Springs.addObject('BarycentricMapping', input="@..", output="@Visual")

        CoFEM = root.addChild('CoFEM')
        CoFEM.addObject('NewmarkImplicitSolver', rayleighMass="0", rayleighStiffness="0.1")
        CoFEM.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")
        CoFEM.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
        CoFEM.addObject('MeshTopology', src="@loader")
        CoFEM.addObject('MechanicalObject', src="@loader", dx="30")
        CoFEM.addObject('UniformMass', totalMass="15")
        CoFEM.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345")
        CoFEM.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1116", poissonRatio="0.49", method="polar")

        CoFEM = CoFEM.addChild('CoFEM')
        CoFEM.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/truthcylinder1.obj", handleSeams="1")
        CoFEM.addObject('OglModel', name="Visual", src="@meshLoader_2", color="cyan", dx="30")
        CoFEM.addObject('BarycentricMapping', input="@..", output="@Visual")

        LinearFEM = root.addChild('LinearFEM')
        LinearFEM.addObject('NewmarkImplicitSolver', rayleighMass="0", rayleighStiffness="0.1")
        LinearFEM.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")
        LinearFEM.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
        LinearFEM.addObject('MeshTopology', src="@loader")
        LinearFEM.addObject('MechanicalObject', src="@loader", dx="45")
        LinearFEM.addObject('UniformMass', totalMass="15")
        LinearFEM.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345")
        LinearFEM.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1116", poissonRatio="0.49", method="small")

        LinearFEM = LinearFEM.addChild('LinearFEM')
        LinearFEM.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/truthcylinder1.obj", handleSeams="1")
        LinearFEM.addObject('OglModel', name="Visual", src="@meshLoader_1", color="red", dx="45")
        LinearFEM.addObject('BarycentricMapping', input="@..", output="@Visual")
    ```


<!-- automatically generated doc END -->
