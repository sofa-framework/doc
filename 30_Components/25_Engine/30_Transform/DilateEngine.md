# DilateEngine

Dilates a given mesh by moving vertices along their normal.


__Templates__:

- `#!c++ Vec3d`

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
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>input_position</td>
		<td>
input array of 3d points
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
input mesh triangles
</td>
		<td></td>
	</tr>
	<tr>
		<td>quads</td>
		<td>
input mesh quads
</td>
		<td></td>
	</tr>
	<tr>
		<td>distance</td>
		<td>
distance to move the points (positive for dilatation, negative for erosion)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>minThickness</td>
		<td>
minimal thickness to enforce
</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>output_position</td>
		<td>
output array of 3d points
</td>
		<td></td>
	</tr>
	<tr>
		<td>normal</td>
		<td>
point normals
</td>
		<td></td>
	</tr>
	<tr>
		<td>thickness</td>
		<td>
point thickness
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



