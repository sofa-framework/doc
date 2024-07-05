# RodStraightSection

Class defining a rod straight section Material, defining material and geometry parameters.


__Templates__:

- `#!c++ Rigid3d`

__Target__: `BeamAdapter`

__namespace__: `#!c++ sofa::beamadapter`

__parents__: 

- `#!c++ BaseRodSectionMaterial`

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
		<td>poissonRatio</td>
		<td>
Poisson Ratio of this section
</td>
		<td>0.49</td>
	</tr>
	<tr>
		<td>youngModulus</td>
		<td>
Young Modulus of this section
</td>
		<td>5000</td>
	</tr>
	<tr>
		<td>massDensity</td>
		<td>
Density of the mass (usually in kg/m^3)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
Full radius of this section
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>innerRadius</td>
		<td>
Inner radius of this section if hollow
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>length</td>
		<td>
Total length of this section
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>nbEdgesVisu</td>
		<td>
number of Edges for the visual model
</td>
		<td>10</td>
	</tr>
	<tr>
		<td>nbEdgesCollis</td>
		<td>
number of Edges for the collision model
</td>
		<td>20</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|



