# CudaProximityIntersection

GPGPU Proximity Intersection based on CUDA


__Target__: `SofaCUDA`

__namespace__: `#!c++ sofa::gpu::cuda`

__parents__: 

- `#!c++ NewProximityIntersection`

__categories__: 

- CollisionAlgorithm

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
		<td>alarmDistance</td>
		<td>
Distance above which the intersection computations ignores the promixity pair. This distance can also be used in some broad phase algorithms to reduce the search area
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>contactDistance</td>
		<td>
Distance below which a contact is created
</td>
		<td>0.5</td>
	</tr>
	<tr>
		<td>useLineLine</td>
		<td>
Line-line collision detection enabled
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


