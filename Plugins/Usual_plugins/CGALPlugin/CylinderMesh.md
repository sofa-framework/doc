# CylinderMesh

Generate a regular tetrahedron mesh of a cylinder


__Templates__:

- `#!c++ Vec3d`

__Target__: `CGALPlugin`

__namespace__: `#!c++ cgal`

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
		<td>diameter</td>
		<td>
Diameter
</td>
		<td>5</td>
	</tr>
	<tr>
		<td>length</td>
		<td>
Length
</td>
		<td>50</td>
	</tr>
	<tr>
		<td>number</td>
		<td>
Number of intervals
</td>
		<td>5</td>
	</tr>
	<tr>
		<td>scale</td>
		<td>
Scale or not
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>viewPoints</td>
		<td>
Display Points
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>viewTetras</td>
		<td>
Display Tetrahedra
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>outputPoints</td>
		<td>
Points
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputTetras</td>
		<td>
Tetrahedra
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



