<!-- generate_doc -->
# HermiteSplineProjectiveConstraint

Apply a hermite cubic spline trajectory to given points


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
		<td>BeginTime</td>
		<td>
Begin Time of the motion
		</td>
		<td></td>
	</tr>
	<tr>
		<td>EndTime</td>
		<td>
End Time of the motion
		</td>
		<td></td>
	</tr>
	<tr>
		<td>X0</td>
		<td>
first control point
		</td>
		<td></td>
	</tr>
	<tr>
		<td>dX0</td>
		<td>
first control tangente
		</td>
		<td></td>
	</tr>
	<tr>
		<td>X1</td>
		<td>
second control point
		</td>
		<td></td>
	</tr>
	<tr>
		<td>dX1</td>
		<td>
sceond control tangente
		</td>
		<td></td>
	</tr>
	<tr>
		<td>SX0</td>
		<td>
first interpolation vector
		</td>
		<td></td>
	</tr>
	<tr>
		<td>SX1</td>
		<td>
second interpolation vector
		</td>
		<td></td>
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
		<td>BeginTime</td>
		<td>
Begin Time of the motion
		</td>
		<td></td>
	</tr>
	<tr>
		<td>EndTime</td>
		<td>
End Time of the motion
		</td>
		<td></td>
	</tr>
	<tr>
		<td>X0</td>
		<td>
first control point
		</td>
		<td></td>
	</tr>
	<tr>
		<td>dX0</td>
		<td>
first control tangente
		</td>
		<td></td>
	</tr>
	<tr>
		<td>X1</td>
		<td>
second control point
		</td>
		<td></td>
	</tr>
	<tr>
		<td>dX1</td>
		<td>
sceond control tangente
		</td>
		<td></td>
	</tr>
	<tr>
		<td>SX0</td>
		<td>
first interpolation vector
		</td>
		<td></td>
	</tr>
	<tr>
		<td>SX1</td>
		<td>
second interpolation vector
		</td>
		<td></td>
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

## Examples 

HermiteSplineProjectiveConstraint.scn

=== "XML"

    ```xml
    <Node name="root" gravity="0 -9.81 0" dt="0.01" time="0" animate="0" bbox="-1 -1 -1 1 1 1">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [HermiteSplineProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <VisualStyle displayFlags="showVisual showBehaviorModels showForceFields" />
        <DefaultAnimationLoop/>
        <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0" rayleighMass="0" />
        <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
        <MechanicalObject template="Vec3" showObject="1" drawMode="1">
            <Attribute type="name">
                <Data value="particleDOF" />
            </Attribute>
            <Attribute type="position">
                <Data value="0 0 0" />
            </Attribute>
            <Attribute type="velocity">
                <Data value="0 10 0" />
            </Attribute>
            <Attribute type="derivX">
                <Data value="0 0 0" />
            </Attribute>
            <Attribute type="free_position">
                <Data value="0 0 0" />
            </Attribute>
            <Attribute type="free_velocity">
                <Data value="0 0 0" />
            </Attribute>
            <Attribute type="rest_position">
                <Data value="0 0 0" />
            </Attribute>
            <Attribute type="translation">
                <Data value="0 0 0" />
            </Attribute>
            <Attribute type="rotation">
                <Data value="0 0 0" />
            </Attribute>
            <Attribute type="scale">
                <Data value="1" />
            </Attribute>
        </MechanicalObject>
        <HermiteSplineProjectiveConstraint template="Vec3">
            <Attribute type="name">
                <Data value="thierry" />
            </Attribute>
            <Attribute type="indices">
                <Data value="0" />
            </Attribute>
            <Attribute type="BeginTime">
                <Data value="0" />
            </Attribute>
            <Attribute type="EndTime">
                <Data value="5" />
            </Attribute>
            <Attribute type="X0">
                <Data value="0 0 0" />
            </Attribute>
            <Attribute type="dX0">
                <Data value="0 10 0" />
            </Attribute>
            <Attribute type="X1">
                <Data value="5 0 0" />
            </Attribute>
            <Attribute type="dX1">
                <Data value="0 5 0" />
            </Attribute>
            <Attribute type="SX0">
                <Data value="1 0" />
            </Attribute>
            <Attribute type="SX1">
                <Data value="0 2" />
            </Attribute>
        </HermiteSplineProjectiveConstraint>
        <UniformMass >
            <Attribute type="name">
                <Data value="particleMass" />
            </Attribute>
            <Attribute type="totalMass">
                <Data value="1" />
            </Attribute>
        </UniformMass>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9.81 0", dt="0.01", time="0", animate="0", bbox="-1 -1 -1 1 1 1")

       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels showForceFields")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0", rayleighMass="0")
       root.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       root.addObject('MechanicalObject', template="Vec3", showObject="1", drawMode="1")
       root.addObject('HermiteSplineProjectiveConstraint', template="Vec3")
       root.addObject('UniformMass', )
    ```

