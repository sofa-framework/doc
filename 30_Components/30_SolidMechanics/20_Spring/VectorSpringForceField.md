# VectorSpringForceField

Spring force field acting along the edges of a mesh


__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.Component.SolidMechanics.Spring`

__namespace__: `#!c++ sofa::component::solidmechanics::spring`

__parents__: 

- `#!c++ PairInteractionForceField`

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
		<td>isCompliance</td>
		<td>
Consider the component as a compliance, else as a stiffness
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
		<td>springs</td>
		<td>
springs data
</td>
		<td></td>
	</tr>
	<tr>
		<td>filename</td>
		<td>
File name from which the spring informations are loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>stiffness</td>
		<td>
Default edge stiffness used in absence of file information
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>viscosity</td>
		<td>
Default edge viscosity used in absence of file information
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>useTopology</td>
		<td>
Activate/Desactivate topology mode of the component (springs on each edge)
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
|object1|First object associated to this component|
|object2|Second object associated to this component|
|topology|link to the topology container|



