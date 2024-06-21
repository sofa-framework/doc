# AdaptiveBeamMapping

Set the positions and velocities of points attached to a beam using linear interpolation between DOFs


__Templates__:

- `#!c++ Rigid3d,Rigid3d`
- `#!c++ Rigid3d,Vec3d`

__Target__: `BeamAdapter`

__namespace__: `#!c++ sofa::component::mapping::_adaptivebeammapping_`

__parents__: 

- `#!c++ Mapping`

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
		<td>useCurvAbs</td>
		<td>
true if the curvilinear abscissa of the points remains the same during the simulation if not the curvilinear abscissa moves with adaptivity and the num of segment per beam is always the same
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>points</td>
		<td>
defines the mapped points along the beam axis (in beam frame local coordinates)
</td>
		<td></td>
	</tr>
	<tr>
		<td>proximity</td>
		<td>
if positive, the mapping is modified for the constraints to take into account the lever created by the proximity
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>contactDuplicate</td>
		<td>
if true, this mapping is a copy of an input mapping and is used to gather contact points (ContinuousFrictionContact Response)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>nameOfInputMap</td>
		<td>
if contactDuplicate==true, it provides the name of the input mapping
</td>
		<td></td>
	</tr>
	<tr>
		<td>nbPointsPerBeam</td>
		<td>
if non zero, we will adapt the points depending on the discretization, with this num of points per beam (compatible with useCurvAbs)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>segmentsCurvAbs</td>
		<td>
the abscissa of each point on the collision model
</td>
		<td></td>
	</tr>
	<tr>
		<td>parallelMapping</td>
		<td>
flag to enable parallel internal computation
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
|input|Input object to map|
|output|Output object to map|
|interpolation|Path to the Interpolation component on scene|



