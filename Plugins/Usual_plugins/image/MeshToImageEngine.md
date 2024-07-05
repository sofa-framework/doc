# MeshToImageEngine

Compute a rasterization image from several meshes


__Templates__:

- `#!c++ ImageB`
- `#!c++ ImageD`
- `#!c++ ImageUC`
- `#!c++ ImageUS`

__Target__: `image`

__namespace__: `#!c++ sofa::component::engine`

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
		<td>voxelSize</td>
		<td>
voxel Size (redondant with and not priority over nbVoxels)
</td>
		<td>1 1 1</td>
	</tr>
	<tr>
		<td>nbVoxels</td>
		<td>
number of voxel (redondant with and priority over voxelSize)
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>rotateImage</td>
		<td>
orient the image bounding box according to the mesh (OBB)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>padSize</td>
		<td>
size of border in number of voxels
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>subdiv</td>
		<td>
number of subdivisions for face rasterization (if needed, increase to avoid holes)
</td>
		<td>4</td>
	</tr>
	<tr>
		<td>image</td>
		<td>

</td>
		<td>0 0 0 0 0</td>
	</tr>
	<tr>
		<td>transform</td>
		<td>

</td>
		<td>0 0 0 0 0 0 1 1 1 0 1 0</td>
	</tr>
	<tr>
		<td>backgroundValue</td>
		<td>
pixel value at background
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>nbMeshes</td>
		<td>
number of meshes to voxelize (Note that the last one write on the previous ones)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>gridSnap</td>
		<td>
align voxel centers on voxelSize multiples for perfect image merging (nbVoxels and rotateImage should be off)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>worldGridAligned</td>
		<td>
perform rasterization on a world aligned grid using nbVoxels and voxelSize
</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>position1</td>
		<td>
input positions for mesh (1)
</td>
		<td></td>
	</tr>
	<tr>
		<td>edges1</td>
		<td>
input edges for mesh (1)
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles1</td>
		<td>
input triangles for mesh (1)
</td>
		<td></td>
	</tr>
	<tr>
		<td>value1</td>
		<td>
pixel value on mesh surface (1)
</td>
		<td></td>
	</tr>
	<tr>
		<td>fillInside1</td>
		<td>
fill the mesh using insideValue?(1)
</td>
		<td></td>
	</tr>
	<tr>
		<td>insideValue1</td>
		<td>
pixel value inside the mesh(1)
</td>
		<td></td>
	</tr>
	<tr>
		<td>roiIndices1</td>
		<td>
List of Regions Of Interest, vertex indices(1)
</td>
		<td></td>
	</tr>
	<tr>
		<td>roiValue1</td>
		<td>
pixel value for ROIs, list of values(1)
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



