# EvalPointsDistance

Periodically compute the distance between 2 set of points


__Templates__:

- `#!c++ Rigid3d`
- `#!c++ Vec3d`

__Target__: `SofaValidation`

__namespace__: `#!c++ sofa::component::misc`

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
		<td>isToPrint</td>
		<td>
suppress somes data before using save as function
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>filename</td>
		<td>
output file name
</td>
		<td></td>
	</tr>
	<tr>
		<td>period</td>
		<td>
period between outputs
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>distance</td>
		<td>
distances (OUTPUT)
</td>
		<td></td>
	</tr>
	<tr>
		<td>distMean</td>
		<td>
mean distance (OUTPUT)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>distMin</td>
		<td>
min distance (OUTPUT)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>distMax</td>
		<td>
max distance (OUTPUT)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>distDev</td>
		<td>
distance standard deviation (OUTPUT)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>rdistMean</td>
		<td>
mean relative distance (OUTPUT)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>rdistMin</td>
		<td>
min relative distance (OUTPUT)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>rdistMax</td>
		<td>
max relative distance (OUTPUT)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>rdistDev</td>
		<td>
relative distance standard deviation (OUTPUT)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>draw</td>
		<td>
activate rendering of lines between associated points
</td>
		<td>1</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|object1|Mechanical state 1|
|object2|Mechanical state 2|



