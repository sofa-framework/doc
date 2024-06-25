# IntensityProfileRegistrationForceField

Compute normal forces on a point set based on the closest intensity profile in the target image


__Templates__:

- `#!c++ Vec3d,ImageB`
- `#!c++ Vec3d,ImageC`
- `#!c++ Vec3d,ImageD`
- `#!c++ Vec3d,ImageF`
- `#!c++ Vec3d,ImageI`
- `#!c++ Vec3d,ImageL`
- `#!c++ Vec3d,ImageS`
- `#!c++ Vec3d,ImageUC`
- `#!c++ Vec3d,ImageUI`
- `#!c++ Vec3d,ImageUL`
- `#!c++ Vec3d,ImageUS`

__Target__: `Registration`

__namespace__: `#!c++ sofa::component::forcefield`

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
		<td>maskOutside</td>
		<td>
discard profiles outside images
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>useAnisotropicStiffness</td>
		<td>
use more accurate but non constant stiffness matrix.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>sizes</td>
		<td>
Inwards/outwards profile size.
</td>
		<td>5 5</td>
	</tr>
	<tr>
		<td>step</td>
		<td>
Spacing of the profile discretization.
</td>
		<td>0.01</td>
	</tr>
	<tr>
		<td>interpolation</td>
		<td>
Interpolation method.
</td>
		<td></td>
	</tr>
	<tr>
		<td>measure</td>
		<td>
Similarity measure.
</td>
		<td></td>
	</tr>
	<tr>
		<td>threshold</td>
		<td>
threshold for the distance minimization.
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>searchRange</td>
		<td>
Number of inwards/outwards steps for searching the most similar profiles.
</td>
		<td>10</td>
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
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>refImage</td>
		<td>

</td>
		<td>0 0 0 0 0</td>
	</tr>
	<tr>
		<td>image</td>
		<td>

</td>
		<td>0 0 0 0 0</td>
	</tr>
	<tr>
		<td>refTransform</td>
		<td>

</td>
		<td>0 0 0 0 0 0 1 1 1 0 1 0</td>
	</tr>
	<tr>
		<td>transform</td>
		<td>

</td>
		<td>0 0 0 0 0 0 1 1 1 0 1 0</td>
	</tr>
	<tr>
		<td>refDirections</td>
		<td>
Profile reference directions.
</td>
		<td></td>
	</tr>
	<tr>
		<td>directions</td>
		<td>
Profile directions.
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>refProfiles</td>
		<td>
reference intensity profiles
</td>
		<td>0 0 0 0 0</td>
	</tr>
	<tr>
		<td>profiles</td>
		<td>
computed intensity profiles
</td>
		<td>0 0 0 0 0</td>
	</tr>
	<tr>
		<td>similarity</td>
		<td>
similarity image
</td>
		<td>0 0 0 0 0</td>
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
|mstate|MechanicalState used by this component|



