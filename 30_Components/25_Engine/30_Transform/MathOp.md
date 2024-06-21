# MathOp

Apply a math operation to combine several inputs


__Templates__:

- `#!c++ vector<RigidCoord2d>`
- `#!c++ vector<RigidCoord3d>`
- `#!c++ vector<RigidDeriv2d>`
- `#!c++ vector<RigidDeriv3d>`
- `#!c++ vector<Vec2d>`
- `#!c++ vector<Vec3d>`
- `#!c++ vector<bool>`
- `#!c++ vector<d>`
- `#!c++ vector<i>`

__Target__: `Sofa.Component.Engine.Transform`

__namespace__: `#!c++ sofa::component::engine::transform`

__parents__: 

- `#!c++ DataEngine`

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
		<td>nbInputs</td>
		<td>
Number of input values
</td>
		<td>2</td>
	</tr>
	<tr>
		<td>op</td>
		<td>
Selected operation to apply
</td>
		<td></td>
	</tr>
	<tr>
		<td>output</td>
		<td>
Output values
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>input1</td>
		<td>
input values 1
</td>
		<td></td>
	</tr>
	<tr>
		<td>input2</td>
		<td>
input values 2
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



