# InterpolatedImplicitSurface

Deprecated. This class is forwarding DiscreteGridField.


__Target__: `SofaImplicitField`

__namespace__: `#!c++ sofa::component::container`

__parents__: 

- `#!c++ DiscreteGridField`

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
		<td>epsilon</td>
		<td>
Tolerance when evaluating the gradient and/or the hessian of the implicit surface numerically
</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>file</td>
		<td>
MHD file for the distance map
</td>
		<td></td>
	</tr>
	<tr>
		<td>maxDomains</td>
		<td>
Number of domains available for caching
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>dx</td>
		<td>
x translation
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>dy</td>
		<td>
y translation
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>dz</td>
		<td>
z translation
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



