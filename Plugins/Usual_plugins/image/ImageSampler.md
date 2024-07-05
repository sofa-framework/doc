# ImageSampler

Samples an object represented by an image


__Templates__:

- `#!c++ ImageB`
- `#!c++ ImageD`
- `#!c++ ImageUC`

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
		<td>method</td>
		<td>
method (param)
</td>
		<td></td>
	</tr>
	<tr>
		<td>computeRecursive</td>
		<td>
if true: insert nodes recursively and build the graph
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>param</td>
		<td>
Parameters
</td>
		<td></td>
	</tr>
	<tr>
		<td>position</td>
		<td>
output positions
</td>
		<td></td>
	</tr>
	<tr>
		<td>fixedPosition</td>
		<td>
user defined sample positions
</td>
		<td></td>
	</tr>
	<tr>
		<td>edges</td>
		<td>
edges connecting neighboring nodes
</td>
		<td></td>
	</tr>
	<tr>
		<td>graphEdges</td>
		<td>
oriented graph connecting parent to child nodes
</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedra</td>
		<td>
output hexahedra
</td>
		<td></td>
	</tr>
	<tr>
		<td>distances</td>
		<td>

</td>
		<td>0 0 0 0 0</td>
	</tr>
	<tr>
		<td>voronoi</td>
		<td>

</td>
		<td>0 0 0 0 0</td>
	</tr>
	<tr>
		<td>clearData</td>
		<td>
clear distance image after computation
</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showSamplesScale</td>
		<td>
show samples
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawMode</td>
		<td>
0: points, 1: spheres
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showEdges</td>
		<td>
show edges
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showGraph</td>
		<td>
show graph
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showFaces</td>
		<td>
show the faces of cubes
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



