# StatsSetting

Stats settings


__Target__: `Sofa.Component.Setting`

__namespace__: `#!c++ sofa::component::setting`

__parents__: 

- `#!c++ ConfigurationSetting`

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
		<td>dumpState</td>
		<td>
Dump state vectors at each time step of the simulation
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>logTime</td>
		<td>
Output in the console an average of the time spent during different stages of the simulation
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>exportState</td>
		<td>
Create GNUPLOT files with the positions, velocities and forces of all the simulated objects of the scene
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>traceVisitors</td>
		<td>
Trace the time spent by each visitor, and allows to profile precisely one step of a simulation
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



