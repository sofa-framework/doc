# SurfacePressureConstraint

This component constrains a model by applying pressure on surfaces (for exemple cavities)


__Templates__:

- `#!c++ Vec3d`

__Target__: `SoftRobots`

__namespace__: `#!c++ softrobots::constraint`

__parents__: 

- `#!c++ SurfacePressureModel`

__categories__: 

- ConstraintSet

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
		<td>group</td>
		<td>
ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>constraintIndex</td>
		<td>
Constraint index (first index in the right hand term resolution vector)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>endTime</td>
		<td>
The SoftRobotsConstraint stops acting after the given value.
Use a negative value for infinite SoftRobotsConstraints
</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
List of triangles on which the surface pressure is applied.
If no list is given, the component will 
fill the two lists with the context topology.
</td>
		<td></td>
	</tr>
	<tr>
		<td>quads</td>
		<td>
List of quads on which the surface pressure is applied. 
If no list is given, the component will 
fill the two lists with the context topology.
</td>
		<td></td>
	</tr>
	<tr>
		<td>initialCavityVolume</td>
		<td>
Output volume of the cavity at init (only relevant in case of closed mesh)
</td>
		<td></td>
	</tr>
	<tr>
		<td>cavityVolume</td>
		<td>
Output volume of the cavity (only relevant in case of closed mesh)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>flipNormal</td>
		<td>
Allows to invert cavity faces orientation. 
If a positive pressure acts like a depressurization, try to set 
flipNormal to true.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>maxPressure</td>
		<td>
Maximum pressure allowed for actuation. If no value is set by user, no 
maximum pressure constraint will be considered.
</td>
		<td></td>
	</tr>
	<tr>
		<td>minPressure</td>
		<td>
Minimum pressure allowed for actuation. If no value is set by user, no 
minimum pressure constraint will be considered. A negative pressure will empty/drain the cavity.
</td>
		<td></td>
	</tr>
	<tr>
		<td>eqPressure</td>
		<td>
Equality constraint for the pressure. 
Solver will try to maintain the pressure at this value.
If unspecified, no equality constraint will be considered.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>maxPressureVariation</td>
		<td>
Maximum pressure variation allowed for actuation. If no value is set by user, no 
maximum will be considered.
</td>
		<td></td>
	</tr>
	<tr>
		<td>maxVolumeGrowth</td>
		<td>
Maximum volume growth allowed for actuation. If no value is set by user, no 
maximum will be considered. NB: this value has a dependancy with the time step 
(volume/dt) in the dynamic case.
</td>
		<td></td>
	</tr>
	<tr>
		<td>minVolumeGrowth</td>
		<td>
Minimum volume growth allowed for actuation. If no value is set by user, no 
minimum will be considered. NB: this value has a dependancy with the time step 
(volume/dt) in the dynamic case.
</td>
		<td></td>
	</tr>
	<tr>
		<td>eqVolumeGrowth</td>
		<td>
Equality constraint for the volume growth. 
Solver will try to maintain the volume growth at this value.
If unspecified, no equality constraint will be considered.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>maxVolumeGrowthVariation</td>
		<td>
Maximum volume growth variation allowed for actuation. If no value is set by user, no 
maximum will be considered. NB: this value has a dependancy with the time step 
(volume/dt) in the dynamic case.
</td>
		<td></td>
	</tr>
	<tr>
		<td>value</td>
		<td>
List of choices for volume growth or pressure to impose.

</td>
		<td></td>
	</tr>
	<tr>
		<td>valueIndex</td>
		<td>
Index of the value (in InputValue vector) that we want to impose 
If unspecified the default value is {0}
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>valueType</td>
		<td>
volumeGrowth = the constraint will impose the volume growth provided in data value[valueIndex] 
pressure = the constraint will impose the pressure provided in data value[valueIndex] 
If unspecified, the default value is pressure
</td>
		<td>pressure</td>
	</tr>
	<tr>
		<td colspan="3">Vector</td>
	</tr>
	<tr>
		<td>pressure</td>
		<td>
Output pressure. Warning: to get the actual pressure you should divide this value by dt.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>volumeGrowth</td>
		<td>
Output volume growth.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawPressure</td>
		<td>
Visualization of the value of pressure. 
If unspecified, the default value is {false}
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawScale</td>
		<td>
Scale for visualization. If unspecified the default value is {0.1}
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



