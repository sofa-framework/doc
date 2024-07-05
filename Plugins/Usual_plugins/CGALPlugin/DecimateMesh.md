# DecimateMesh

Simplification of a mesh by the process of reducing the number of faces


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
		<td>inputVertices</td>
		<td>
List of vertices
</td>
		<td></td>
	</tr>
	<tr>
		<td>inputTriangles</td>
		<td>
List of triangles
</td>
		<td></td>
	</tr>
	<tr>
		<td>targetedNumberOfEdges</td>
		<td>
Desired number of edges after simplification
</td>
		<td></td>
	</tr>
	<tr>
		<td>targetedRatioOfEdges</td>
		<td>
Ratio between the number of edges and number of initial edges
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputPoints</td>
		<td>
New vertices after decimation
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputTriangles</td>
		<td>
New triangles after decimation
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputNormals</td>
		<td>
New normals after decimation
</td>
		<td></td>
	</tr>
	<tr>
		<td>writeToFile</td>
		<td>
Writes the decimated mesh into a file
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



