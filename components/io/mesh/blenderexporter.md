# BlenderExporter

Export the simulation result as blender point cache files


__Templates__:

- `#!c++ Rigid3d`
- `#!c++ Vec3d`

__Target__: `Sofa.Component.IO.Mesh`

__namespace__: `#!c++ sofa::component::_blenderexporter_`

__parents__: 

- `#!c++ BaseObject`

__categories__: 

- _Miscellaneous

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
		<td>path</td>
		<td>
output path
</td>
		<td></td>
	</tr>
	<tr>
		<td>baseName</td>
		<td>
Base name for the output files
</td>
		<td></td>
	</tr>
	<tr>
		<td>simulationType</td>
		<td>
simulation type (0: soft body, 1: particles, 2:cloth, 3:hair)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>step</td>
		<td>
save the  simulation result every step frames
</td>
		<td>2</td>
	</tr>
	<tr>
		<td>nbPtsByHair</td>
		<td>
number of element by hair strand
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



