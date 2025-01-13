<!-- generate_doc -->
# GridTopology

Base class fo a regular grid in 3D.


__Target__: Sofa.Component.Topology.Container.Grid

__namespace__: sofa::component::topology::container::grid

__parents__:

- MeshTopology

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
list of the subsets the object belongs to
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
		<td>filename</td>
		<td>
Filename of the mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td>position</td>
		<td>
List of point positions
		</td>
		<td></td>
	</tr>
	<tr>
		<td>edges</td>
		<td>
List of edge indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
List of triangle indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quads</td>
		<td>
List of quad indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedra</td>
		<td>
List of tetrahedron indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedra</td>
		<td>
List of hexahedron indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>uv</td>
		<td>
List of uv coordinates
		</td>
		<td></td>
	</tr>
	<tr>
		<td>computeAllBuffers</td>
		<td>
Option to compute all crossed topology buffers at init. False by default
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>n</td>
		<td>
grid resolution. (default = 2 2 2)
		</td>
		<td>2 2 2</td>
	</tr>
	<tr>
		<td>computeHexaList</td>
		<td>
put true if the list of Hexahedra is needed during init (default=true)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>computeQuadList</td>
		<td>
put true if the list of Quad is needed during init (default=true)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>computeTriangleList</td>
		<td>
put true if the list of Triangles is needed during init (default=true)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>computeEdgeList</td>
		<td>
put true if the list of Lines is needed during init (default=true)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>computePointList</td>
		<td>
put true if the list of Points is needed during init (default=true)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>createTexCoords</td>
		<td>
If set to true, virtual texture coordinates will be generated using 3D interpolation (default=false).
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawEdges</td>
		<td>
if true, draw the topology Edges
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawTriangles</td>
		<td>
if true, draw the topology Triangles
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawQuads</td>
		<td>
if true, draw the topology Quads
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawTetrahedra</td>
		<td>
if true, draw the topology Tetrahedra
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawHexahedra</td>
		<td>
if true, draw the topology hexahedra
		</td>
		<td>0</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|

