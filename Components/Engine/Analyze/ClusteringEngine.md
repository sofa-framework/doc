# ClusteringEngine

Group points into overlapping clusters according to a user defined number of clusters and radius


__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.Component.Engine.Analyze`

__namespace__: `#!c++ sofa::component::engine::analyze`

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
		<td>useTopo</td>
		<td>
Use avalaible topology to compute neighborhood.
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>outFile</td>
		<td>
export clusters
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
Neighborhood range.
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>fixedRadius</td>
		<td>
Neighborhood range (for non mechanical particles).
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>number</td>
		<td>
Number of clusters (-1 means that all input points are selected).
</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>fixedPosition</td>
		<td>
Input positions of fixed (non mechanical) particles.
</td>
		<td></td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Input rest positions.
</td>
		<td></td>
	</tr>
	<tr>
		<td>inFile</td>
		<td>
import precomputed clusters
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>cluster</td>
		<td>
Computed clusters.
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



