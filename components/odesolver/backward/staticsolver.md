<!-- generate_doc -->
# StaticSolver

Static ODE Solver.


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
		<td>newton_iterations</td>
		<td>
Number of Netwon iterations between each load increments (normally, one load increment per simulation time-step.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>absolute_correction_tolerance_threshold</td>
		<td>
Convergence criterion of the norm |du| under which the Netwon iterations stop
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>relative_correction_tolerance_threshold</td>
		<td>
Convergence criterion regarding the ratio |du| / |U| under which the Netwon iterations stop
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>absolute_residual_tolerance_threshold</td>
		<td>
Convergence criterion of the norm |R| under which the Netwon iterations stop.Use a negative value to disable this criterion
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>relative_residual_tolerance_threshold</td>
		<td>
Convergence criterion regarding the ratio |R|/|R0| under which the Netwon iterations stop.Use a negative value to disable this criterion
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>should_diverge_when_residual_is_growing</td>
		<td>
Boolean stopping Netwon iterations when the residual is greater than the one from the previous iteration
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

## Examples 

StaticSolver.scn

=== "XML"

    ```xml
    <Node name="root" gravity="-1.8 0 100"  dt="1">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [StaticSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [MeshSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <DefaultAnimationLoop/>
    
        <VisualStyle displayFlags="hideBehaviorModels hideCollisionModels hideMappings hideForceFields" />
    	<Node name="Reference">
    		<MeshOBJLoader name="meshLoader_1" filename="mesh/truthcylinder1-bent.obj" scale="0.95" handleSeams="1" />
    		<OglModel src="@meshLoader_1" dx="0" dy="-1" dz="0" color="green" />
    	</Node>
    	<Node name="Springs">
    
    		<StaticSolver  />
    		<CGLinearSolver iterations="100" tolerance="1e-5" threshold="1e-5"/>
    		<MeshGmshLoader name="loader" filename="mesh/truthcylinder1.msh" />
    		<MeshTopology src="@loader" />
    		<MechanicalObject src="@loader" dx="15" />
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
    		<StaticSolver  />
    		<CGLinearSolver iterations="100" tolerance="1e-5" threshold="1e-5"/>
    		<MeshGmshLoader name="loader" filename="mesh/truthcylinder1.msh"/>
    		<MeshTopology src="@loader" />
    		<MechanicalObject src="@loader" dx="30" />
    		<UniformMass totalMass="15" />
    		<FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345" />
    		<TetrahedronFEMForceField name="FEM" youngModulus="1116" poissonRatio="0.49" method="polar" />
    		<Node>
    			<MeshOBJLoader name="meshLoader_3" filename="mesh/truthcylinder1.obj" handleSeams="1" />
    			<OglModel name="Visual" src="@meshLoader_3" color="cyan" dx="30" />
    			<BarycentricMapping input="@.." output="@Visual" />
    		</Node>
    	</Node>
    	<Node name="LinearFEM">
    		<StaticSolver  />
    		<CGLinearSolver iterations="100" tolerance="1e-5" threshold="1e-5"/>
    		<MeshGmshLoader name="loader" filename="mesh/truthcylinder1.msh"/>
    		<MeshTopology src="@loader" />
    		<MechanicalObject src="@loader" dx="45" />
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

       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="hideBehaviorModels hideCollisionModels hideMappings hideForceFields")

       reference = root.addChild('Reference')

       reference.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/truthcylinder1-bent.obj", scale="0.95", handleSeams="1")
       reference.addObject('OglModel', src="@meshLoader_1", dx="0", dy="-1", dz="0", color="green")

       springs = root.addChild('Springs')

       springs.addObject('StaticSolver', )
       springs.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")
       springs.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
       springs.addObject('MeshTopology', src="@loader")
       springs.addObject('MechanicalObject', src="@loader", dx="15")
       springs.addObject('UniformMass', totalMass="15")
       springs.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345")
       springs.addObject('MeshSpringForceField', name="Spring", tetrasStiffness="1870", tetrasDamping="0")

       node = Springs.addChild('node')

       node.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/truthcylinder1.obj", handleSeams="1")
       node.addObject('OglModel', name="Visual", src="@meshLoader_0", color="yellow", dx="15")
       node.addObject('BarycentricMapping', input="@..", output="@Visual")

       co_fem = root.addChild('CoFEM')

       co_fem.addObject('StaticSolver', )
       co_fem.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")
       co_fem.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
       co_fem.addObject('MeshTopology', src="@loader")
       co_fem.addObject('MechanicalObject', src="@loader", dx="30")
       co_fem.addObject('UniformMass', totalMass="15")
       co_fem.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345")
       co_fem.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1116", poissonRatio="0.49", method="polar")

       node = CoFEM.addChild('node')

       node.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/truthcylinder1.obj", handleSeams="1")
       node.addObject('OglModel', name="Visual", src="@meshLoader_3", color="cyan", dx="30")
       node.addObject('BarycentricMapping', input="@..", output="@Visual")

       linear_fem = root.addChild('LinearFEM')

       linear_fem.addObject('StaticSolver', )
       linear_fem.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")
       linear_fem.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
       linear_fem.addObject('MeshTopology', src="@loader")
       linear_fem.addObject('MechanicalObject', src="@loader", dx="45")
       linear_fem.addObject('UniformMass', totalMass="15")
       linear_fem.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345")
       linear_fem.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1116", poissonRatio="0.49", method="small")

       node = LinearFEM.addChild('node')

       node.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/truthcylinder1.obj", handleSeams="1")
       node.addObject('OglModel', name="Visual", src="@meshLoader_2", color="red", dx="45")
       node.addObject('BarycentricMapping', input="@..", output="@Visual")
    ```

