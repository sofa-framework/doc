# OscillatingTorsionPressureForceField

OscillatingTorsionPressure


__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.Component.MechanicalLoad`

__namespace__: `#!c++ sofa::component::mechanicalload`

__parents__: 

- `#!c++ ForceField`

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
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping - stiffness matrix coefficient
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>trianglePressureMap</td>
		<td>
Map between triangle indices and their pressure
</td>
		<td></td>
	</tr>
	<tr>
		<td>moment</td>
		<td>
Moment force applied on the entire surface
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangleList</td>
		<td>
Indices of triangles separated with commas where a pressure is applied
</td>
		<td></td>
	</tr>
	<tr>
		<td>axis</td>
		<td>
Axis of rotation and normal direction for the plane selection of triangles
</td>
		<td>0 0 1</td>
	</tr>
	<tr>
		<td>center</td>
		<td>
Center of rotation
</td>
		<td></td>
	</tr>
	<tr>
		<td>penalty</td>
		<td>
Strength of the penalty force
</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>frequency</td>
		<td>
frequency of oscillation
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>dmin</td>
		<td>
Minimum distance from the origin along the normal direction
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>dmax</td>
		<td>
Maximum distance from the origin along the normal direction
</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showForces</td>
		<td>
draw triangles which have a given pressure
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
|mechanicalStates|List of mechanical states to which this component is associated|
|mstate|MechanicalState used by this component|



