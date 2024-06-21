# EdgeSetGeometryAlgorithms

Edge set geometry algorithms


__Templates__:

- `#!c++ Rigid2d`
- `#!c++ Rigid3d`
- `#!c++ Vec1d`
- `#!c++ Vec2d`
- `#!c++ Vec3d`

__Target__: `Sofa.Component.Topology.Container.Dynamic`

__namespace__: `#!c++ sofa::component::topology::container::dynamic`

__parents__: 

- `#!c++ PointSetGeometryAlgorithms`

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

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|topology|link to the topology container|



