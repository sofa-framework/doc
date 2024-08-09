<!-- generate_doc -->
# LinearMovementProjectiveConstraint

translate given particles


## Rigid3d

Templates:

- Rigid3d

__Target__: Sofa.Component.Constraint.Projective

__namespace__: sofa::component::constraint::projective

__parents__:

- ProjectiveConstraintSet

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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Rigid3d&gt;|
|topology|link to the topology container|BaseMeshTopology|

<!-- generate_doc -->
## Vec1d

Templates:

- Vec1d

__Target__: Sofa.Component.Constraint.Projective

__namespace__: sofa::component::constraint::projective

__parents__:

- ProjectiveConstraintSet

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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec1d&gt;|
|topology|link to the topology container|BaseMeshTopology|

<!-- generate_doc -->
## Vec2d

Templates:

- Vec2d

__Target__: Sofa.Component.Constraint.Projective

__namespace__: sofa::component::constraint::projective

__parents__:

- ProjectiveConstraintSet

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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec2d&gt;|
|topology|link to the topology container|BaseMeshTopology|

<!-- generate_doc -->
## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.Constraint.Projective

__namespace__: sofa::component::constraint::projective

__parents__:

- ProjectiveConstraintSet

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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|
|topology|link to the topology container|BaseMeshTopology|

<!-- generate_doc -->
## Vec6d

Templates:

- Vec6d

__Target__: Sofa.Component.Constraint.Projective

__namespace__: sofa::component::constraint::projective

__parents__:

- ProjectiveConstraintSet

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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec6d&gt;|
|topology|link to the topology container|BaseMeshTopology|

## Examples 

LinearMovementProjectiveConstraint.scn

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
    def createScene(root_node):

       root = root_node.addChild('Root', dt="0.1")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('DefaultAnimationLoop', )

       spoon1 = Root.addChild('Spoon1')

       spoon1.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       spoon1.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       spoon1.addObject('MechanicalObject', template="Rigid3", dx="0", dy="0", dz="0", name="default118", position="0 1.41421 0 0 0 0.382683 0.92388", rest_position="0 1.41421 0 0 0 0.382683 0.92388")
       spoon1.addObject('LinearMovementProjectiveConstraint', template="Rigid3", keyTimes="0 2 10 40 50", movements="0 0 0   0 0 0                 0 0 0   0 0 0                 0 0 -1  0 0 0                 0 0 -1  0 0 6.3                 0 0 -1   0 0 6.3")

       coli = Spoon1.addChild('coli')

       coli.addObject('MeshOBJLoader', name="loader", filename="mesh/liver.obj")
       coli.addObject('MeshTopology', src="@loader")
       coli.addObject('MechanicalObject', src="@loader", template="Vec3", name="dofs")
       coli.addObject('TriangleCollisionModel', moving="1", simulated="1", contactStiffness="100000000")
       coli.addObject('RigidMapping', template="Rigid3,Vec3")

       visu = Spoon1.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/liver.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="red")
       visu.addObject('RigidMapping', template="Rigid3,Vec3", name="default161", input="@..", output="@Visual")

       spoon2 = Root.addChild('Spoon2')

       spoon2.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       spoon2.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       spoon2.addObject('MechanicalObject', template="Rigid3", dx="10", dy="0", dz="0", name="default118", position="0 1.41421 0 0 0 0.382683 0.92388", rest_position="0 1.41421 0 0 0 0.382683 0.92388")
       spoon2.addObject('LinearMovementProjectiveConstraint', template="Rigid3", keyTimes="0 2 10 40 50", movements="0 0 0   0 0 0                 0 0 0   0 0 0                 0 0 -1  0 0 0                 0 0 -1  0 0 6.3                 0 0 0   0 0 6.3")

       coli = Spoon2.addChild('coli')

       coli.addObject('MeshOBJLoader', name="loader", filename="mesh/liver.obj")
       coli.addObject('MeshTopology', src="@loader")
       coli.addObject('MechanicalObject', src="@loader", template="Vec3", name="dofs")
       coli.addObject('TriangleCollisionModel', moving="1", simulated="1", contactStiffness="100000000")
       coli.addObject('RigidMapping', template="Rigid3,Vec3")

       visu = Spoon2.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/liver.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="green")
       visu.addObject('RigidMapping', template="Rigid3,Vec3", name="default161", input="@..", output="@Visual")

       spoon3 = Root.addChild('Spoon3')

       spoon3.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       spoon3.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       spoon3.addObject('MechanicalObject', template="Rigid3", dx="20", dy="0", dz="0", name="default118", position="0 1.41421 0 0 0 0.382683 0.92388", rest_position="0 1.41421 0 0 0 0.382683 0.92388")
       spoon3.addObject('LinearMovementProjectiveConstraint', template="Rigid3", keyTimes="0 2 10 40 50", movements="0 0 0   0 0 0                 0 0 0   0 0 0                 0 0 -1  0 0 0                 0 0 -1  0 0 6.3                 0 0 -1   0 0 0")

       coli = Spoon3.addChild('coli')

       coli.addObject('MeshOBJLoader', name="loader", filename="mesh/liver.obj")
       coli.addObject('MeshTopology', src="@loader")
       coli.addObject('MechanicalObject', src="@loader", template="Vec3", name="dofs")
       coli.addObject('TriangleCollisionModel', moving="1", simulated="1", contactStiffness="100000000")
       coli.addObject('RigidMapping', template="Rigid3,Vec3")

       visu = Spoon3.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/liver.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_2", color="blue")
       visu.addObject('RigidMapping', template="Rigid3,Vec3", name="default161", input="@..", output="@Visual")
    ```

