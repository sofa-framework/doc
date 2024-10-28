<!-- generate_doc -->
# DampVelocitySolver

Reduce the velocities.


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
		<td>rate</td>
		<td>
Factor used to reduce the velocities. Typically between 0 and 1.
		</td>
		<td>0.99</td>
	</tr>
	<tr>
		<td>threshold</td>
		<td>
Threshold under which the velocities are canceled.
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

DampVelocitySolver.scn

=== "XML"

    ```xml
    <Node name="root" gravity="0 0 0" dt="0.05">
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Forward"/> <!-- Needed to use components [DampVelocitySolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangleFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <DefaultAnimationLoop/>
    
        <Node name="M0">
            <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" tolerance="1e-5" threshold="1e-10"/>
            <DampVelocitySolver rate="0.9" threshold="0.01" printLog="0" name="damp" />
            <MechanicalObject position="0 0 0  1 0 0  1 1 0  0 1 0" velocity="1 0 0  1 0 0  1 0 0  1 0 0" />
            <UniformMass vertexMass="0.1" />
            <MeshTopology triangles="0 1 2  0 2 3" />
            <TriangleFEMForceField name="FEM0" youngModulus="100" poissonRatio="0.3" method="large" />
            <Node name="Visu">
                <OglModel name="Visual" color="red" />
                <IdentityMapping input="@.." output="@Visual" />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 0 0", dt="0.05")

       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Forward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
       root.addObject('DefaultAnimationLoop', )

       m0 = root.addChild('M0')

       m0.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
       m0.addObject('CGLinearSolver', iterations="25", tolerance="1e-5", threshold="1e-10")
       m0.addObject('DampVelocitySolver', rate="0.9", threshold="0.01", printLog="0", name="damp")
       m0.addObject('MechanicalObject', position="0 0 0  1 0 0  1 1 0  0 1 0", velocity="1 0 0  1 0 0  1 0 0  1 0 0")
       m0.addObject('UniformMass', vertexMass="0.1")
       m0.addObject('MeshTopology', triangles="0 1 2  0 2 3")
       m0.addObject('TriangleFEMForceField', name="FEM0", youngModulus="100", poissonRatio="0.3", method="large")

       visu = M0.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="red")
       visu.addObject('IdentityMapping', input="@..", output="@Visual")
    ```

