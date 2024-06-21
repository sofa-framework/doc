# ParticleSource

Parametrable particle generator
Supports GPU-side computations using CUDA


__Templates__:

- `#!c++ Vec3d`

__Target__: `SofaSphFluid`

__namespace__: `#!c++ sofa::component::misc`

__parents__: 

- `#!c++ ProjectiveConstraintSet`

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
		<td>endTime</td>
		<td>
The constraint stops acting after the given value.
Use a negative value for infinite constraints
</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>translation</td>
		<td>
translation applied to center(s)
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>scale</td>
		<td>
scale applied to center(s)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>center</td>
		<td>
Source center(s)
</td>
		<td></td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
Source radius
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>velocity</td>
		<td>
Particle initial velocity
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>delay</td>
		<td>
Delay between particles creation
</td>
		<td>0.01</td>
	</tr>
	<tr>
		<td>start</td>
		<td>
Source starting time
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>stop</td>
		<td>
Source stopping time
</td>
		<td>1e+10</td>
	</tr>
	<tr>
		<td>addNoise</td>
		<td>
Will add random value to the radius of new created particles
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>lastparticles</td>
		<td>
lastparticles indices
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



__Templates__:

- `#!c++ Vec2d`

__Target__: `SofaSphFluid`

__namespace__: `#!c++ sofa::component::misc`

__parents__: 

- `#!c++ ProjectiveConstraintSet`

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
		<td>endTime</td>
		<td>
The constraint stops acting after the given value.
Use a negative value for infinite constraints
</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>translation</td>
		<td>
translation applied to center(s)
</td>
		<td>0 0</td>
	</tr>
	<tr>
		<td>scale</td>
		<td>
scale applied to center(s)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>center</td>
		<td>
Source center(s)
</td>
		<td></td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
Source radius
</td>
		<td>0 0</td>
	</tr>
	<tr>
		<td>velocity</td>
		<td>
Particle initial velocity
</td>
		<td>0 0</td>
	</tr>
	<tr>
		<td>delay</td>
		<td>
Delay between particles creation
</td>
		<td>0.01</td>
	</tr>
	<tr>
		<td>start</td>
		<td>
Source starting time
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>stop</td>
		<td>
Source stopping time
</td>
		<td>1e+10</td>
	</tr>
	<tr>
		<td>addNoise</td>
		<td>
Will add random value to the radius of new created particles
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>lastparticles</td>
		<td>
lastparticles indices
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



