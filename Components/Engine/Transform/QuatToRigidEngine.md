# QuatToRigidEngine

Transform a vector of Rigids into two independant vectors for positions (Vec3) and orientations (Quat).


__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.Component.Engine.Transform`

__namespace__: `#!c++ sofa::component::engine::transform`

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
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>positions</td>
		<td>
Positions (Vector of 3)
</td>
		<td></td>
	</tr>
	<tr>
		<td>orientations</td>
		<td>
Orientations (Quaternion)
</td>
		<td></td>
	</tr>
	<tr>
		<td>colinearPositions</td>
		<td>
Optional positions to restrict output to be colinear in the quaternion Z direction
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>rigids</td>
		<td>
Rigid (Position + Orientation)
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



