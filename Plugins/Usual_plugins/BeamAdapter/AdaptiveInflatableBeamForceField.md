# AdaptiveInflatableBeamForceField

Adaptive Beam finite elements


__Templates__:

- `#!c++ Rigid3d`

__Target__: `BeamAdapter`

__namespace__: `#!c++ sofa::component::forcefield::_AdaptiveInflatableBeamForceField_`

__parents__: 

- `#!c++ Mass`

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
		<td>separateGravity</td>
		<td>
add separately gravity to velocity computation
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>rayleighMass</td>
		<td>
Rayleigh damping - mass matrix coefficient
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>computeMass</td>
		<td>
if false, only compute the stiff elastic model
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>massDensity</td>
		<td>
Density of the mass (usually in kg/m^3)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>reinforceLength</td>
		<td>
if true, a separate computation for the error in elongation is peformed
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>pressure</td>
		<td>
pressure inside the inflatable Beam
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>dataG</td>
		<td>
Gravity 3d vector
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
|mechanicalStates|List of mechanical states to which this component is associated|
|mstate|MechanicalState used by this component|
|interpolation|Path to the Interpolation component on scene|
|instrumentParameters|link to an object specifying physical parameters based on abscissa|



