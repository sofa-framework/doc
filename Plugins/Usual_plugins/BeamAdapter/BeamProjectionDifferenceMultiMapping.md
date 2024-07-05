# BeamProjectionDifferenceMultiMapping

Computes the difference between given points and their projection on a beam.


__Templates__:

- `#!c++ Rigid3d,Rigid3d,Rigid3d`

__Target__: `BeamAdapter`

__namespace__: `#!c++ beamadapter::mapping`

__parents__: 

- `#!c++ Multi2Mapping`

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
		<td>mapForces</td>
		<td>
Are forces mapped ?
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapConstraints</td>
		<td>
Are constraints mapped ?
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapMasses</td>
		<td>
Are masses mapped ?
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapMatrices</td>
		<td>
Are matrix explicit mapped?
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>applyRestPosition</td>
		<td>
set to true to apply this mapping to restPosition at init
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>indicesInput1</td>
		<td>
Indices of model1 to project on model2 (beams)
</td>
		<td></td>
	</tr>
	<tr>
		<td>directions</td>
		<td>
Directions to project (in the local frame).
</td>
		<td></td>
	</tr>
	<tr>
		<td>updateProjectionPosition</td>
		<td>
Update the projection on the beam at each time step even when direction[0]=1.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>updateProjectionOrientation</td>
		<td>
Update the projection on the beam at each time step even when direction[0]=1.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>draw</td>
		<td>
Draw projection points and directions
</td>
		<td></td>
	</tr>
	<tr>
		<td>drawSize</td>
		<td>

</td>
		<td>3</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|input1|Input Object(s) (1st Data type)|
|input2|Input Object(s) (2st Data type)|
|output|Output Object(s)|
|topologyInput2|link to input2's topology container (beams to project on)|
|interpolationInput2|link to input2's interpolation component (BeamInterpolation)|



