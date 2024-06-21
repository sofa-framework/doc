# PrecomputedConstraintCorrection

Component computing constraint forces within a simulated body using the compliance method.
Supports GPU-side computations using CUDA.


__Templates__:

- `#!c++ Rigid3d`
- `#!c++ Vec1d`
- `#!c++ Vec3d`

__Target__: `Sofa.Component.Constraint.Lagrangian.Correction`

__namespace__: `#!c++ sofa::component::constraint::lagrangian::correction`

__parents__: 

- `#!c++ ConstraintCorrection`

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
		<td>rotations</td>
		<td>

</td>
		<td>0</td>
	</tr>
	<tr>
		<td>restDeformations</td>
		<td>

</td>
		<td>0</td>
	</tr>
	<tr>
		<td>recompute</td>
		<td>
if true, always recompute the compliance
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>debugViewFrameScale</td>
		<td>
Scale on computed node's frame
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>fileCompliance</td>
		<td>
Precomputed compliance matrix data file
</td>
		<td></td>
	</tr>
	<tr>
		<td>fileDir</td>
		<td>
If not empty, the compliance will be saved in this repertory
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
|constraintSolvers|Constraint solvers using this constraint correction|



