<!-- generate_doc -->
# DynamicSparseGridTopologyContainer

Dynamic sparse grid geometry container.


__Target__: Sofa.Component.Topology.Container.Dynamic

__namespace__: sofa::component::topology::container::dynamic

__parents__:

- HexahedronSetTopologyContainer

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
Initial position of points
		</td>
		<td></td>
	</tr>
	<tr>
		<td>checkTopology</td>
		<td>
Parameter to activate internal topology checks (might slow down the simulation)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>nbPoints</td>
		<td>
Number of points
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>edges</td>
		<td>
List of edge indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>checkConnexity</td>
		<td>
It true, will check the connexity of the mesh.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>quads</td>
		<td>
List of quad indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>createQuadArray</td>
		<td>
Force the creation of a set of quads associated with the hexahedra
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>hexahedra</td>
		<td>
List of hexahedron indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>resolution</td>
		<td>
voxel grid resolution
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>valuesIndexedInRegularGrid</td>
		<td>
values indexed in the Regular Grid
		</td>
		<td></td>
	</tr>
	<tr>
		<td>valuesIndexedInTopology</td>
		<td>
values indexed in the topology
		</td>
		<td></td>
	</tr>
	<tr>
		<td>idxInRegularGrid</td>
		<td>
indices in the Regular Grid
		</td>
		<td></td>
	</tr>
	<tr>
		<td>idInRegularGrid2IndexInTopo</td>
		<td>
map between id in the Regular Grid and index in the topology
		</td>
		<td></td>
	</tr>
	<tr>
		<td>voxelSize</td>
		<td>
Size of the Voxels
		</td>
		<td>1 1 1</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|

