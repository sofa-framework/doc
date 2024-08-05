# LinearForceField

Linearly interpolated force applied to given degrees of freedom
Supports GPU-side computation using CUDA


__Templates__:

- `#!c++ Rigid3d`
- `#!c++ Vec1d`
- `#!c++ Vec2d`
- `#!c++ Vec3d`
- `#!c++ Vec6d`

__Target__: `Sofa.Component.MechanicalLoad`

__namespace__: `#!c++ sofa::component::mechanicalload`

__parents__: 

- `#!c++ ForceField`

__categories__: 

- ForceField

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
Rayleigh damping - stiffness matrix coefficient
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>points</td>
		<td>
points where the force is applied
</td>
		<td></td>
	</tr>
	<tr>
		<td>force</td>
		<td>
applied force to all points
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>times</td>
		<td>
key times for the interpolation
</td>
		<td></td>
	</tr>
	<tr>
		<td>forces</td>
		<td>
forces corresponding to the key times
</td>
		<td></td>
	</tr>
	<tr>
		<td>arrowSizeCoef</td>
		<td>
Size of the drawn arrows (0-&gt;no arrows, sign-&gt;direction of drawing
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
|mechanicalStates|List of mechanical states to which this component is associated|
|mstate|MechanicalState used by this component|
|topology|link to the topology container|



## Examples

Component/MechanicalLoad/LinearForceField.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.005" gravity="0 0 0">
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [LinearForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Forward"/> <!-- Needed to use components [EulerExplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <DefaultAnimationLoop/>
        
        <Node name="TorusRigidX">
            <EulerExplicitSolver />
            <CGLinearSolver iterations="25" threshold="0.00000001" tolerance="1e-5"/>
            <MechanicalObject template="Rigid3" dx="2" dy="0" dz="0" rx="0" ry="0" rz="0" scale="1.0" />
            <UniformMass />
            <!-- forces for a rigid is composed of two parts translation of the rigid dof [x y z] and a quaternion for the rotation [x y z w] -->
            <LinearForceField points="0" forces="0 0 0 0 0 0  1 0 0 0 0 0  -1 0 0 0 0 0  -1 0 0 0 0 0  0 0 0 0 0 0" force="2.0" times="0 4 8 10 12" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/torus.obj" scale="0.3" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_0" color="gray" />
                <RigidMapping input="@.." output="@Visual" />
            </Node>
        </Node>
        <Node name="TorusRigidY">
            <EulerExplicitSolver />
            <CGLinearSolver iterations="25" threshold="0.00000001" tolerance="1e-5"/>
            <MechanicalObject template="Rigid3" dx="2" dy="2" dz="0" rx="0" ry="0" rz="0" scale="1.0" />
            <UniformMass />
            <!-- forces for a rigid is composed of two parts translation of the rigid dof [x y z] and a quaternion for the rotation [x y z w] -->
            <LinearForceField points="0" forces="0 0 0 0 0 0  0 1 0 0 0 0  0 -1 0 0 0 0  0 -1 0 0 0 0  0 0 0 0 0 0" force="2.0" times="0 4 8 10 12" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_1" filename="mesh/torus.obj" scale="0.3" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_1" color="gray" />
                <RigidMapping input="@.." output="@Visual" />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.005", gravity="0 0 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Forward")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
        root.addObject('DefaultAnimationLoop')

        TorusRigidX = root.addChild('TorusRigidX')
        TorusRigidX.addObject('EulerExplicitSolver')
        TorusRigidX.addObject('CGLinearSolver', iterations="25", threshold="0.00000001", tolerance="1e-5")
        TorusRigidX.addObject('MechanicalObject', template="Rigid3", dx="2", dy="0", dz="0", rx="0", ry="0", rz="0", scale="1.0")
        TorusRigidX.addObject('UniformMass')
        TorusRigidX.addObject('LinearForceField', points="0", forces="0 0 0 0 0 0  1 0 0 0 0 0  -1 0 0 0 0 0  -1 0 0 0 0 0  0 0 0 0 0 0", force="2.0", times="0 4 8 10 12")

        Visu = TorusRigidX.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", scale="0.3", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="gray")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        TorusRigidY = root.addChild('TorusRigidY')
        TorusRigidY.addObject('EulerExplicitSolver')
        TorusRigidY.addObject('CGLinearSolver', iterations="25", threshold="0.00000001", tolerance="1e-5")
        TorusRigidY.addObject('MechanicalObject', template="Rigid3", dx="2", dy="2", dz="0", rx="0", ry="0", rz="0", scale="1.0")
        TorusRigidY.addObject('UniformMass')
        TorusRigidY.addObject('LinearForceField', points="0", forces="0 0 0 0 0 0  0 1 0 0 0 0  0 -1 0 0 0 0  0 -1 0 0 0 0  0 0 0 0 0 0", force="2.0", times="0 4 8 10 12")

        Visu = TorusRigidY.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/torus.obj", scale="0.3", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="gray")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")
    ```

