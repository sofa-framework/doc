# SphereLoader

Loader for sphere model description files


__Target__: `Sofa.Component.IO.Mesh`

__namespace__: `#!c++ sofa::component::io::mesh`

__parents__: 

- `#!c++ BaseLoader`

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
		<td>filename</td>
		<td>
Filename of the object
</td>
		<td></td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Sphere centers
</td>
		<td></td>
	</tr>
	<tr>
		<td>listRadius</td>
		<td>
Radius of each sphere
</td>
		<td></td>
	</tr>
	<tr>
		<td>scale</td>
		<td>
Scale applied to sphere positions & radius
</td>
		<td>1 1 1</td>
	</tr>
	<tr>
		<td>rotation</td>
		<td>
Rotation of the DOFs
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>translation</td>
		<td>
Translation applied to sphere positions
</td>
		<td>0 0 0</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|



