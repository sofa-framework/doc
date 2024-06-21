# BeamAdapterActionController

BeamAdapterActionController


__Templates__:

- `#!c++ Rigid3d`

__Target__: `BeamAdapter`

__namespace__: `#!c++ sofa::component::controller`

__parents__: 

- `#!c++ MechanicalStateController`

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
		<td>handleEventTriggersUpdate</td>
		<td>
Event handling frequency controls the controller update frequency
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>index</td>
		<td>
Index of the controlled DOF
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>onlyTranslation</td>
		<td>
Controlling the DOF only in translation
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>buttonDeviceState</td>
		<td>
state of ths device button
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>mainDirection</td>
		<td>
Main direction and orientation of the controlled DOF
</td>
		<td>0 0 -1</td>
	</tr>
	<tr>
		<td>writeMode</td>
		<td>
If true, will accumulate actions from keyboard and dump the actions and times when key 'E' is pressed.
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>actions</td>
		<td>
List of actions to script the BeamAdapter
</td>
		<td></td>
	</tr>
	<tr>
		<td>actionString</td>
		<td>
List of actions as string to script the BeamAdapter
</td>
		<td></td>
	</tr>
	<tr>
		<td>timeSteps</td>
		<td>
List of key times corresponding to the actions
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
|interventionController|Path to the InterventionalRadiologyController component on scene|



