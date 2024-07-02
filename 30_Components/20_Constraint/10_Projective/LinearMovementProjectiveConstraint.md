# LinearMovementProjectiveConstraint

translate given particles
Supports GPU-side computations using CUDA


__Templates__:

- `#!c++ Rigid3d`
- `#!c++ Vec1d`
- `#!c++ Vec2d`
- `#!c++ Vec3d`
- `#!c++ Vec6d`

__Target__: `Sofa.Component.Constraint.Projective`

__namespace__: `#!c++ sofa::component::constraint::projective`

__parents__: 

- `#!c++ ProjectiveConstraintSet`

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
		<td>group</td>
		<td>
ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>endTime</td>
		<td>
The constraint stops acting after the given value.
Use a negative value for infinite constraints
</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
Indices of the constrained points
</td>
		<td></td>
	</tr>
	<tr>
		<td>keyTimes</td>
		<td>
key times for the movements
</td>
		<td></td>
	</tr>
	<tr>
		<td>movements</td>
		<td>
movements corresponding to the key times
</td>
		<td></td>
	</tr>
	<tr>
		<td>relativeMovements</td>
		<td>
If true, movements are relative to first position, absolute otherwise
</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showMovement</td>
		<td>
Visualization of the movement to be applied to constrained dofs.
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

Component/Constraint/Projective/LinearMovementProjectiveConstraint.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="Root"  dt="0.1" >
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [LinearMovementProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <DefaultAnimationLoop/>
    
        <Node name="Spoon1">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject template="Rigid3" dx="0" dy="0" dz="0" name="default118" position="0 1.41421 0 0 0 0.382683 0.92388" rest_position="0 1.41421 0 0 0 0.382683 0.92388" />
            <LinearMovementProjectiveConstraint template="Rigid3" keyTimes="0 2 10 40 50" movements="0 0 0   0 0 0
    										      0 0 0   0 0 0
    										      0 0 -1  0 0 0
    										      0 0 -1  0 0 6.3
    										      0 0 -1   0 0 6.3" />
            <Node name="coli">
                <MeshOBJLoader name="loader" filename="mesh/liver.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" template="Vec3" name="dofs" />
                <TriangleCollisionModel moving="1" simulated="1" contactStiffness="100000000"/>
                <RigidMapping template="Rigid3,Vec3" />
            </Node>
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_1" filename="mesh/liver.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_1" color="red" />
                <RigidMapping template="Rigid3,Vec3" name="default161" input="@.." output="@Visual" />
            </Node>
        </Node>
        <Node name="Spoon2">
            <EulerImplicitSolver name="cg_odesolver" printLog="false" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject template="Rigid3" dx="10" dy="0" dz="0" name="default118" position="0 1.41421 0 0 0 0.382683 0.92388" rest_position="0 1.41421 0 0 0 0.382683 0.92388"/>
            <LinearMovementProjectiveConstraint template="Rigid3" keyTimes="0 2 10 40 50" movements="0 0 0   0 0 0
    										      0 0 0   0 0 0
    										      0 0 -1  0 0 0
    										      0 0 -1  0 0 6.3
    										      0 0 0   0 0 6.3" />
            <Node name="coli">
                <MeshOBJLoader name="loader" filename="mesh/liver.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" template="Vec3" name="dofs" />
                <TriangleCollisionModel moving="1" simulated="1" contactStiffness="100000000" />
                <RigidMapping template="Rigid3,Vec3" />
            </Node>
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/liver.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_0" color="green" />
                <RigidMapping template="Rigid3,Vec3" name="default161" input="@.." output="@Visual"/>
            </Node>
        </Node>
        <Node name="Spoon3">
            <EulerImplicitSolver name="cg_odesolver" printLog="false" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject template="Rigid3" dx="20" dy="0" dz="0" name="default118" position="0 1.41421 0 0 0 0.382683 0.92388" rest_position="0 1.41421 0 0 0 0.382683 0.92388" />
            <LinearMovementProjectiveConstraint template="Rigid3" keyTimes="0 2 10 40 50" movements="0 0 0   0 0 0
    										      0 0 0   0 0 0
    										      0 0 -1  0 0 0
    										      0 0 -1  0 0 6.3
    										      0 0 -1   0 0 0" />
            <Node name="coli">
                <MeshOBJLoader name="loader" filename="mesh/liver.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" template="Vec3" name="dofs" />
                <TriangleCollisionModel moving="1" simulated="1" contactStiffness="100000000" />
                <RigidMapping template="Rigid3,Vec3" />
            </Node>
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_2" filename="mesh/liver.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_2" color="blue" />
                <RigidMapping template="Rigid3,Vec3" name="default161" input="@.." output="@Visual" />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        Root = rootNode.addChild('Root', dt="0.1")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        Root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        Root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        Root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        Root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        Root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        Root.addObject('DefaultAnimationLoop')

        Spoon1 = Root.addChild('Spoon1')
        Spoon1.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        Spoon1.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        Spoon1.addObject('MechanicalObject', template="Rigid3", dx="0", dy="0", dz="0", name="default118", position="0 1.41421 0 0 0 0.382683 0.92388", rest_position="0 1.41421 0 0 0 0.382683 0.92388")
        Spoon1.addObject('LinearMovementProjectiveConstraint', template="Rigid3", keyTimes="0 2 10 40 50", movements="0 0 0   0 0 0
										      0 0 0   0 0 0
										      0 0 -1  0 0 0
										      0 0 -1  0 0 6.3
										      0 0 -1   0 0 6.3")

        coli = Spoon1.addChild('coli')
        coli.addObject('MeshOBJLoader', name="loader", filename="mesh/liver.obj")
        coli.addObject('MeshTopology', src="@loader")
        coli.addObject('MechanicalObject', src="@loader", template="Vec3", name="dofs")
        coli.addObject('TriangleCollisionModel', moving="1", simulated="1", contactStiffness="100000000")
        coli.addObject('RigidMapping', template="Rigid3,Vec3")

        Visu = Spoon1.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/liver.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="red")
        Visu.addObject('RigidMapping', template="Rigid3,Vec3", name="default161", input="@..", output="@Visual")

        Spoon2 = Root.addChild('Spoon2')
        Spoon2.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        Spoon2.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        Spoon2.addObject('MechanicalObject', template="Rigid3", dx="10", dy="0", dz="0", name="default118", position="0 1.41421 0 0 0 0.382683 0.92388", rest_position="0 1.41421 0 0 0 0.382683 0.92388")
        Spoon2.addObject('LinearMovementProjectiveConstraint', template="Rigid3", keyTimes="0 2 10 40 50", movements="0 0 0   0 0 0
										      0 0 0   0 0 0
										      0 0 -1  0 0 0
										      0 0 -1  0 0 6.3
										      0 0 0   0 0 6.3")

        coli = Spoon2.addChild('coli')
        coli.addObject('MeshOBJLoader', name="loader", filename="mesh/liver.obj")
        coli.addObject('MeshTopology', src="@loader")
        coli.addObject('MechanicalObject', src="@loader", template="Vec3", name="dofs")
        coli.addObject('TriangleCollisionModel', moving="1", simulated="1", contactStiffness="100000000")
        coli.addObject('RigidMapping', template="Rigid3,Vec3")

        Visu = Spoon2.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/liver.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="green")
        Visu.addObject('RigidMapping', template="Rigid3,Vec3", name="default161", input="@..", output="@Visual")

        Spoon3 = Root.addChild('Spoon3')
        Spoon3.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        Spoon3.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        Spoon3.addObject('MechanicalObject', template="Rigid3", dx="20", dy="0", dz="0", name="default118", position="0 1.41421 0 0 0 0.382683 0.92388", rest_position="0 1.41421 0 0 0 0.382683 0.92388")
        Spoon3.addObject('LinearMovementProjectiveConstraint', template="Rigid3", keyTimes="0 2 10 40 50", movements="0 0 0   0 0 0
										      0 0 0   0 0 0
										      0 0 -1  0 0 0
										      0 0 -1  0 0 6.3
										      0 0 -1   0 0 0")

        coli = Spoon3.addChild('coli')
        coli.addObject('MeshOBJLoader', name="loader", filename="mesh/liver.obj")
        coli.addObject('MeshTopology', src="@loader")
        coli.addObject('MechanicalObject', src="@loader", template="Vec3", name="dofs")
        coli.addObject('TriangleCollisionModel', moving="1", simulated="1", contactStiffness="100000000")
        coli.addObject('RigidMapping', template="Rigid3,Vec3")

        Visu = Spoon3.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/liver.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_2", color="blue")
        Visu.addObject('RigidMapping', template="Rigid3,Vec3", name="default161", input="@..", output="@Visual")
    ```

