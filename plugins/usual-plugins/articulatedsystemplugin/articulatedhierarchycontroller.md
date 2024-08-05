# ArticulatedHierarchyController

Implements an user interaction handler that controls the values of the articulations of an articulated hierarchy container.


__Target__: `ArticulatedSystemPlugin`

__namespace__: `#!c++ sofa::component::controller`

__parents__: 

- `#!c++ Controller`

__categories__: 

- Controller

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
		<td>articulationsIndices</td>
		<td>
Indices of articulations controlled by the keyboard
</td>
		<td></td>
	</tr>
	<tr>
		<td>bindingKeys</td>
		<td>
Keys to press to control the articulations
</td>
		<td></td>
	</tr>
	<tr>
		<td>angleDelta</td>
		<td>
Angle incrementation due to each user interaction
</td>
		<td>0.01</td>
	</tr>
	<tr>
		<td>propagateUserInteraction</td>
		<td>
Says wether or not the user interaction is local on the articulations, or must be propagated to children recursively
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



