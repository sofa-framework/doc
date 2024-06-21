# PoissonSurfaceReconstruction

Generate triangular surface mesh from point cloud


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
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Input point cloud positions
</td>
		<td></td>
	</tr>
	<tr>
		<td>normals</td>
		<td>
Input point cloud normals
</td>
		<td></td>
	</tr>
	<tr>
		<td>angle</td>
		<td>
Bound for the minimum facet angle in degrees
</td>
		<td>20</td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
Bound for the radius of the surface Delaunay balls (relatively to the average_spacing)
</td>
		<td>30</td>
	</tr>
	<tr>
		<td>distance</td>
		<td>
Bound for the center-center distances (relatively to the average_spacing)
</td>
		<td>0.375</td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>outputPosition</td>
		<td>
Output position of the surface mesh
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

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|



