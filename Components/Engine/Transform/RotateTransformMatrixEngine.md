# RotateTransformMatrixEngine

Compose the input transform (if any) with the given rotation


__Target__: `Sofa.Component.Engine.Transform`

__namespace__: `#!c++ sofa::component::engine::transform`

__parents__: 

- `#!c++ AbstractTransformMatrixEngine`

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
		<td>rotation</td>
		<td>
euler angles
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>inT</td>
		<td>
input transformation if any
</td>
		<td>[1 0 0 0,0 1 0 0,0 0 1 0,0 0 0 1]</td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>outT</td>
		<td>
output transformation
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



