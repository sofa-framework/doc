# SpatialGridContainer

Hashing spatial grid container, used for SPH fluids for instance.
GPU support using CUDA.


__Templates__:

- `#!c++ Vec3d`

__Target__: `SofaSphFluid`

__namespace__: `#!c++ sofa::component::container`

__parents__: 

- `#!c++ BaseObject`

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
		<td>cellWidth</td>
		<td>
Width each cell in the grid. If it is used to compute neighboors, it should be greater than the max radius considered.
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>autoUpdate</td>
		<td>
Automatically update the grid at each iteration.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>sortPoints</td>
		<td>
Sort points depending on which cell they are in the grid. This is required for efficient collision detection.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showGrid</td>
		<td>
activate rendering of the grid
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



