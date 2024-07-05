# ManifoldTriangleSetGeometryAlgorithms

ManifoldTriangle set topology algorithms


__Templates__:

- `#!c++ Vec2d`
- `#!c++ Vec3d`

__Target__: `ManifoldTopologies`

__namespace__: `#!c++ sofa::component::topology::container::dynamic`

__parents__: 

- `#!c++ TriangleSetGeometryAlgorithms`

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
		<td>tagMechanics</td>
		<td>
Tag of the Mechanical Object
</td>
		<td></td>
	</tr>
	<tr>
		<td>recomputeTrianglesOrientation</td>
		<td>
if true, will recompute triangles orientation according to normals
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>flipNormals</td>
		<td>
if true, will flip normal of the first triangle used to recompute triangle orientation.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>swap 2 triangles by their index</td>
		<td>
Debug : Test swap function (only while animate).
</td>
		<td></td>
	</tr>
	<tr>
		<td>Mesh Optimization</td>
		<td>
If true, optimize the mesh only by swapping edges
</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showIndicesScale</td>
		<td>
Debug : scale for view topology indices
</td>
		<td>0.02</td>
	</tr>
	<tr>
		<td>showPointIndices</td>
		<td>
Debug : view Point indices
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showEdgeIndices</td>
		<td>
Debug : view Edge indices.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawEdges</td>
		<td>
if true, draw the edges in the topology.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawColorEdges</td>
		<td>
RGB code color used to draw edges.
</td>
		<td>0.4 1 0.3 1</td>
	</tr>
	<tr>
		<td>showTriangleIndices</td>
		<td>
Debug : view Triangle indices
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawTriangles</td>
		<td>
if true, draw the triangles in the topology
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawColorTriangles</td>
		<td>
RGBA code color used to draw triangles
</td>
		<td>0.3 0.5 0.8 1</td>
	</tr>
	<tr>
		<td>drawNormals</td>
		<td>
if true, draw the triangles in the topology
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawNormalLength</td>
		<td>
Fiber length visualisation.
</td>
		<td>10</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|topology|link to the topology container|



