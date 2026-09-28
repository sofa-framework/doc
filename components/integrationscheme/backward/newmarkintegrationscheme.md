<!-- generate_doc -->
# NewmarkIntegrationScheme

Time integrator using Newmark-beta implicit scheme.


__Target__: Sofa.Component.IntegrationScheme.Backward

__namespace__: sofa::component::integrationscheme::backward

__parents__:

- AccelerationBasedImplicitIntegrationScheme

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
	<tr>
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping coefficient related to stiffness, > 0
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>rayleighMass</td>
		<td>
Rayleigh damping coefficient related to mass, > 0
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>beta</td>
		<td>
Factor controlling the 'implicitness' of the position computation with respect to the acceleration. 0.0 means explicit central difference, 1.0/0.6 means linear accelerations scheme
		</td>
		<td>0.25</td>
	</tr>
	<tr>
		<td>gamma</td>
		<td>
Factor controlling the 'implicitness' of the velocity computation with respect to the acceleration. To insure unconditional stability, gamma must belong to [2*beta, 1/2]. 
		</td>
		<td>0.5</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseComponent|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseComponent|
|linearSolver|Linear solver used by this component|LinearSolver|

## Examples 

NewmarkIntegrationScheme.scn

=== "XML"

    ```xml
    <Node name="root" gravity="-1.8 0 100" dt="0.02">
        <RequiredPlugin pluginName="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin pluginName="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader MeshOBJLoader] -->
        <RequiredPlugin pluginName="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [SparseLDLSolver] -->
        <RequiredPlugin pluginName="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin pluginName="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin pluginName="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin pluginName="Sofa.Component.IntegrationScheme.Backward"/> <!-- Needed to use components [NewmarkIntegrationScheme] -->
        <RequiredPlugin pluginName="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin pluginName="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [MeshSpringForceField] -->
        <RequiredPlugin pluginName="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin pluginName="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <DefaultAnimationLoop/>
        
        <Node name="Reference">
            <MeshOBJLoader name="meshLoader_0" filename="mesh/truthcylinder1-bent.obj" scale="0.95" handleSeams="1" />
            <OglModel src="@meshLoader_0" dx="0" dy="-1" dz="0" color="green" />
        </Node>
        <Node name="Springs">
            <NewmarkIntegrationScheme rayleighMass="0" rayleighStiffness="0.1" />
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
            <NewmarkIntegrationScheme rayleighMass="0" rayleighStiffness="0.1" />
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
            <NewmarkIntegrationScheme rayleighMass="0" rayleighStiffness="0.1" />
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
    def createScene(root_node):

       root = root_node.addChild('root', gravity="-1.8 0 100", dt="0.02")

       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSolver.Direct")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.IntegrationScheme.Backward")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', pluginName="Sofa.GL.Component.Rendering3D")
       root.addObject('DefaultAnimationLoop', )

       reference = root.addChild('Reference')

       reference.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/truthcylinder1-bent.obj", scale="0.95", handleSeams="1")
       reference.addObject('OglModel', src="@meshLoader_0", dx="0", dy="-1", dz="0", color="green")

       springs = root.addChild('Springs')

       springs.addObject('NewmarkIntegrationScheme', rayleighMass="0", rayleighStiffness="0.1")
       springs.addObject('SparseLDLSolver', )
       springs.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
       springs.addObject('MeshTopology', src="@loader")
       springs.addObject('MechanicalObject', src="@loader", dx="15")
       springs.addObject('UniformMass', totalMass="15")
       springs.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345")
       springs.addObject('MeshSpringForceField', name="Spring", tetrasStiffness="1870", tetrasDamping="0")

       node = Springs.addChild('node')

       node.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/truthcylinder1.obj", handleSeams="1")
       node.addObject('OglModel', name="Visual", src="@meshLoader_3", color="yellow", dx="15")
       node.addObject('BarycentricMapping', input="@..", output="@Visual")

       co_fem = root.addChild('CoFEM')

       co_fem.addObject('NewmarkIntegrationScheme', rayleighMass="0", rayleighStiffness="0.1")
       co_fem.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")
       co_fem.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
       co_fem.addObject('MeshTopology', src="@loader")
       co_fem.addObject('MechanicalObject', src="@loader", dx="30")
       co_fem.addObject('UniformMass', totalMass="15")
       co_fem.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345")
       co_fem.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1116", poissonRatio="0.49", method="polar")

       node = CoFEM.addChild('node')

       node.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/truthcylinder1.obj", handleSeams="1")
       node.addObject('OglModel', name="Visual", src="@meshLoader_2", color="cyan", dx="30")
       node.addObject('BarycentricMapping', input="@..", output="@Visual")

       linear_fem = root.addChild('LinearFEM')

       linear_fem.addObject('NewmarkIntegrationScheme', rayleighMass="0", rayleighStiffness="0.1")
       linear_fem.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")
       linear_fem.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
       linear_fem.addObject('MeshTopology', src="@loader")
       linear_fem.addObject('MechanicalObject', src="@loader", dx="45")
       linear_fem.addObject('UniformMass', totalMass="15")
       linear_fem.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345")
       linear_fem.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1116", poissonRatio="0.49", method="small")

       node = LinearFEM.addChild('node')

       node.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/truthcylinder1.obj", handleSeams="1")
       node.addObject('OglModel', name="Visual", src="@meshLoader_1", color="red", dx="45")
       node.addObject('BarycentricMapping', input="@..", output="@Visual")
    ```

