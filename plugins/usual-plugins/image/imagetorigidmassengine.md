# ImageToRigidMassEngine

Compute rigid mass from a density image


__Templates__:

- `#!c++ ImageB`
- `#!c++ ImageD`
- `#!c++ ImageUC`

__Target__: `image`

__namespace__: `#!c++ sofa::component::engine`

__parents__: 

- `#!c++ DataEngine`

__categories__: 

- Engine

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
		<td>image</td>
		<td>

</td>
		<td>0 0 0 0 0</td>
	</tr>
	<tr>
		<td>transform</td>
		<td>

</td>
		<td>0 0 0 0 0 0 1 1 1 0 1 0</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
position
</td>
		<td>0 0 0 0 0 0 1</td>
	</tr>
	<tr>
		<td>mass</td>
		<td>
mass
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>inertia</td>
		<td>
axis-aligned inertia tensor
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>rigidMass</td>
		<td>
rigidMass
</td>
		<td>1 1 [1 0 0,0 1 0,0 0 1]</td>
	</tr>
	<tr>
		<td>density</td>
		<td>
density (in kg/m^3)
</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>multiply</td>
		<td>
multiply density by image intensity?
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



