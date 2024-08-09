<!-- generate_doc -->
# TetrahedronSetGeometryAlgorithms

Tetrahedron set geometry algorithms


Templates:

- Vec2d
- Vec3d

__Target__: Sofa.Component.Topology.Container.Dynamic

__namespace__: sofa::component::topology::container::dynamic

__parents__:

- TriangleSetGeometryAlgorithms

### Data

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
	<tr>
		<td>showTetrahedraIndices</td>
		<td>
Debug : view Tetrahedrons indices
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawTetrahedra</td>
		<td>
if true, draw the tetrahedra in the topology
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawScaleTetrahedra</td>
		<td>
Scale of the terahedra (between 0 and 1; if <1.0, it produces gaps between the tetrahedra)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>drawColorTetrahedra</td>
		<td>
RGBA code color used to draw tetrahedra.
		</td>
		<td>1 1 0 1</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|topology|link to the topology container|BaseMeshTopology|

