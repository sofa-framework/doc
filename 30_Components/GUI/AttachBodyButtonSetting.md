# AttachBodyButtonSetting

Attach Body Button configuration


__Target__: `Sofa.GUI.Component`

__namespace__: `#!c++ sofa::gui::component`

__parents__: 

- `#!c++ MouseButtonSetting`

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
		<td>button</td>
		<td>
Mouse button used
</td>
		<td></td>
	</tr>
	<tr>
		<td>stiffness</td>
		<td>
Stiffness of the spring to attach a particule
</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>arrowSize</td>
		<td>
Size of the drawn spring: if &gt;0 an arrow will be drawn
</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showFactorSize</td>
		<td>
Show factor size of the JointSpringForcefield  when interacting with rigids
</td>
		<td>1</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|



