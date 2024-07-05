# SteerableCatheter



__Templates__:

- `#!c++ Rigid3d`

__Target__: `BeamAdapter`

__namespace__: `#!c++ sofa::component::engine`

__parents__: 

- `#!c++ WireRestShape`

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
		<td>densityOfBeams</td>
		<td>
density of beams between key points
</td>
		<td></td>
	</tr>
	<tr>
		<td>keyPoints</td>
		<td>
key points of the shape (curv absc)
</td>
		<td></td>
	</tr>
	<tr>
		<td>activeBending</td>
		<td>
Boolean activating the bending of the steerable catheter
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>deactiveBending</td>
		<td>
Boolean deactivating the bending of the steerable catheter
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>angleMax</td>
		<td>
Maximum angle that the catheter can reach 
 (in degree [0-360])
</td>
		<td>180</td>
	</tr>
	<tr>
		<td>flatAngle</td>
		<td>
Angle below which we consider the catheter as flat/n (Can't be zero)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>bendingRate</td>
		<td>
Nb of step needed to reach the maximum bending angle /n (the lower, the faster)
</td>
		<td>10</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|wireMaterials|link to Wire Section Materials (to be ordered according to the instrument, from handle to tip)|
|topology|link to the topology container|



