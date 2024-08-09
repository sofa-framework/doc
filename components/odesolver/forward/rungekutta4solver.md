<!-- generate_doc -->
# RungeKutta4Solver

A popular explicit time integrator


__Target__: Sofa.Component.ODESolver.Forward

__namespace__: sofa::component::odesolver::forward

__parents__:

- OdeSolver

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

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|

## Examples 

RungeKutta4Solver.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="-1.8 0 100" dt="0.001">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Forward"/> <!-- Needed to use components [RungeKutta4Solver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <DefaultAnimationLoop/>
        
        <Node name="DeformableObject">
            <RungeKutta4Solver name="odeExplicitSolver" />
            <CGLinearSolver iterations="100" tolerance="1e-5" threshold="1e-5"/>
            <MeshGmshLoader name="loader" filename="mesh/truthcylinder1.msh" />
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader" />
            <UniformMass totalMass="15" />
            <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 &#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;11 12 13 14 15 16 17 18 19 20 &#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 &#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;41 42 43 44 45 46 47 268 269 270 271 343 345" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.45" method="large" />
            <Node>
                <MeshOBJLoader name="meshLoader_0" filename="mesh/truthcylinder1.obj" handleSeams="1" />
                <OglModel name="m_Visual" src="@meshLoader_0" color="red" />
                <BarycentricMapping input="@.." output="@m_Visual" />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="-1.8 0 100", dt="0.001")

       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Forward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('DefaultAnimationLoop', )

       deformable_object = root.addChild('DeformableObject')

       deformable_object.addObject('RungeKutta4Solver', name="odeExplicitSolver")
       deformable_object.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")
       deformable_object.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
       deformable_object.addObject('MeshTopology', src="@loader")
       deformable_object.addObject('MechanicalObject', src="@loader")
       deformable_object.addObject('UniformMass', totalMass="15")
       deformable_object.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 
							11 12 13 14 15 16 17 18 19 20 
							21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 
							41 42 43 44 45 46 47 268 269 270 271 343 345")
       deformable_object.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.45", method="large")

       node = DeformableObject.addChild('node')

       node.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/truthcylinder1.obj", handleSeams="1")
       node.addObject('OglModel', name="m_Visual", src="@meshLoader_0", color="red")
       node.addObject('BarycentricMapping', input="@..", output="@m_Visual")
    ```

