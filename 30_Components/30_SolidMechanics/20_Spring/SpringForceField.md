# SpringForceField

Springs


__Templates__:

- `#!c++ Rigid3d`
- `#!c++ Vec1d`
- `#!c++ Vec2d`
- `#!c++ Vec3d`
- `#!c++ Vec6d`

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
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping - stiffness matrix coefficient
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>stiffness</td>
		<td>
uniform stiffness for the all springs
</td>
		<td>100</td>
	</tr>
	<tr>
		<td>damping</td>
		<td>
uniform damping for the all springs
</td>
		<td>5</td>
	</tr>
	<tr>
		<td>spring</td>
		<td>
pairs of indices, stiffness, damping, rest length
</td>
		<td></td>
	</tr>
	<tr>
		<td>springsIndices1</td>
		<td>
List of indices in springs from the first mstate
</td>
		<td></td>
	</tr>
	<tr>
		<td>springsIndices2</td>
		<td>
List of indices in springs from the second mstate
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showArrowSize</td>
		<td>
size of the axis
</td>
		<td>0.01</td>
	</tr>
	<tr>
		<td>drawMode</td>
		<td>
The way springs will be drawn:
- 0: Line
- 1:Cylinder
- 2: Arrow
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



