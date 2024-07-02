# Distances

Compute distances based on a grid.


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
		<td>offset</td>
		<td>
translation offset between the topology and the point set.
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>d_distanceType</td>
		<td>
type of distance to compute for inserted frames.
</td>
		<td>Geodesic</td>
	</tr>
	<tr>
		<td>initTarget</td>
		<td>
initialize the target MechanicalObject from the grid.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>initTargetStep</td>
		<td>
initialize the target MechanicalObject from the grid using this step.
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>zonesFramePair</td>
		<td>
Correspondence between the segmented value and the frames.
</td>
		<td></td>
	</tr>
	<tr>
		<td>harmonicMaxValue</td>
		<td>
Max value used to initialize the harmonic distance grid.
</td>
		<td>100</td>
	</tr>
	<tr>
		<td>filename</td>
		<td>
file containing the result of the computation of the distances
</td>
		<td></td>
	</tr>
	<tr>
		<td>targetPath</td>
		<td>
path to the goal point set topology
</td>
		<td></td>
	</tr>
	<tr>
		<td>hexaContainerPath</td>
		<td>
path to the grid used to compute the distances
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showMapIndex</td>
		<td>
Frame DOF index on which display values.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showDistancesMap</td>
		<td>
show the distance for each point of the target point set.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showGoalDistancesMap</td>
		<td>
show the distance for each point of the target point set.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showTextScaleFactor</td>
		<td>
Scale to apply on the text.
</td>
		<td>0.001</td>
	</tr>
	<tr>
		<td>showGradients</td>
		<td>
show gradients for each point of the target point set.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showGradientsScaleFactor</td>
		<td>
scale for the gradients displayed.
</td>
		<td>0.1</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|



