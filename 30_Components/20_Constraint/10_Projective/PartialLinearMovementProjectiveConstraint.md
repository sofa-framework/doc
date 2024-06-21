# PartialLinearMovementProjectiveConstraint

translate given particles


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
		<td>linearMovementBetweenNodesInIndices</td>
		<td>
Take into account the linear movement between the constrained points
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>mainIndice</td>
		<td>
The main indice node in the list of constrained nodes, it defines how to apply the linear movement between this constrained nodes 
</td>
		<td></td>
	</tr>
	<tr>
		<td>minDepIndice</td>
		<td>
The indice node in the list of constrained nodes, which is imposed the minimum displacment 
</td>
		<td></td>
	</tr>
	<tr>
		<td>maxDepIndice</td>
		<td>
The indice node in the list of constrained nodes, which is imposed the maximum displacment 
</td>
		<td></td>
	</tr>
	<tr>
		<td>imposedDisplacmentOnMacroNodes</td>
		<td>
The imposed displacment on macro nodes
</td>
		<td></td>
	</tr>
	<tr>
		<td>X0</td>
		<td>
Size of specimen in X-direction
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>Y0</td>
		<td>
Size of specimen in Y-direction
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>Z0</td>
		<td>
Size of specimen in Z-direction
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>movedDirections</td>
		<td>
Defines the directions in which the particles are moved: true (or 1) for fixed, false (or 0) for free
</td>
		<td></td>
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



