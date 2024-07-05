# LCPForceFeedback

LCP force feedback for the device


__Templates__:

- `#!c++ Rigid3d`
- `#!c++ Vec1d`

__Target__: `Sofa.Component.Haptics`

__namespace__: `#!c++ sofa::component::haptics`

__parents__: 

- `#!c++ MechanicalStateForceFeedback`

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
		<td>activate</td>
		<td>
boolean to activate or deactivate the forcefeedback
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>indice</td>
		<td>
Tool indice in the OmniDriver
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>forceCoef</td>
		<td>
multiply haptic force by this coef.
</td>
		<td>0.03</td>
	</tr>
	<tr>
		<td>solverTimeout</td>
		<td>
max time to spend solving constraints.
</td>
		<td>0.0008</td>
	</tr>
	<tr>
		<td>solverMaxIt</td>
		<td>
max iteration to spend solving constraints
</td>
		<td>100</td>
	</tr>
	<tr>
		<td>derivRotations</td>
		<td>
if true, deriv the rotations when updating the violations
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>localHapticConstraintAllFrames</td>
		<td>
Flag to enable/disable constraint haptic influence from all frames
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



