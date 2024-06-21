# CompareTopology

Compare Topology containers from a reference frame to the associated Topology


__Target__: `Sofa.Component.Playback`

__namespace__: `#!c++ sofa::component::playback`

__parents__: 

- `#!c++ ReadTopology`

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
input file name
</td>
		<td></td>
	</tr>
	<tr>
		<td>interval</td>
		<td>
time duration between inputs
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>shift</td>
		<td>
shift between times in the file and times when they will be read
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>loop</td>
		<td>
set to 'true' to re-read the file when reaching the end
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



