# VolumeFromTriangles

This class computes the volume of a given closed surfacic mesh.


__Templates__:

- `#!c++ Vec3d`

__Target__: `SoftRobots`

__namespace__: `#!c++ softrobots::engine`

__parents__: 

- `#!c++ DataEngine`

__categories__: 

- Engine

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
		<td>positions</td>
		<td>
If not set by user, find the context mechanical.
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
If not set by user, find the context topology.
</td>
		<td></td>
	</tr>
	<tr>
		<td>quads</td>
		<td>
If not set by user, find the context topology.
</td>
		<td></td>
	</tr>
	<tr>
		<td>volume</td>
		<td>
Relevant if closed surface.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>update</td>
		<td>
If true, will update the volume with the current positions.
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



