# BooleanOperations

Functions to corefine triangulated surface meshes and compute triangulated surface meshes of the union, difference and intersection of the bounded volumes.


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
		<td>operation</td>
		<td>
Boolean operation
</td>
		<td>union</td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>position1</td>
		<td>
Input positions of the first mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>position2</td>
		<td>
Input positions of the second mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles1</td>
		<td>
Input triangles of the first mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles2</td>
		<td>
Input triangles of the second mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>computeDistrubution</td>
		<td>
If true, computes outputIndices1 and outputIndices2
</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>outputPosition</td>
		<td>
Output positions of the surface mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputTriangles</td>
		<td>
Output triangles of the surface mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputPosition1</td>
		<td>
Output positions of transformation on the first surface mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputTriangles1</td>
		<td>
Output triangles of transformation on the first surface mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputPosition2</td>
		<td>
Output positions of transformation on the second surface mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputTriangles2</td>
		<td>
Output triangles of transformation on the second surface mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputIndices1</td>
		<td>
Indices of the surface mesh points that are on the first object
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputIndices2</td>
		<td>
Indices of the surface mesh points that are on the second object
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



