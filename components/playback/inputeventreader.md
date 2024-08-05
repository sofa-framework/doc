# InputEventReader

Read events from file


__Target__: `Sofa.Component.Playback`

__namespace__: `#!c++ sofa::component::playback`

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
		<td>filename</td>
		<td>
input events file name
</td>
		<td>/dev/input/mouse2</td>
	</tr>
	<tr>
		<td>inverseSense</td>
		<td>
inverse the sense of the mouvement
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>printEvent</td>
		<td>
Print event informations
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>key1</td>
		<td>
Key event generated when the left pedal is pressed
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>key2</td>
		<td>
Key event generated when the right pedal is pressed
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>writeEvents</td>
		<td>
If true, write incoming events ; if false, read events from that file (if an output filename is provided)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>outputFilename</td>
		<td>
Other filename where events will be stored (or read)
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



