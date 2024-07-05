# PatchTestMovementProjectiveConstraint

bilinear constraint


__Templates__:

- `#!c++ Rigid3d`
- `#!c++ Vec3d`

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
		<td>meshIndices</td>
		<td>
Indices of the mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
Indices of the constrained points
</td>
		<td></td>
	</tr>
	<tr>
		<td>beginConstraintTime</td>
		<td>
Begin time of the bilinear constraint
</td>
		<td></td>
	</tr>
	<tr>
		<td>endConstraintTime</td>
		<td>
End time of the bilinear constraint
</td>
		<td></td>
	</tr>
	<tr>
		<td>constrainedPoints</td>
		<td>
Coordinates of the constrained points
</td>
		<td></td>
	</tr>
	<tr>
		<td>cornerMovements</td>
		<td>
movements of the corners of the grid
</td>
		<td></td>
	</tr>
	<tr>
		<td>cornerPoints</td>
		<td>
corner points for computing constraint
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawConstrainedPoints</td>
		<td>
draw constrained points
</td>
		<td></td>
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



