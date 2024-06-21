# TransferFunction

Transforms pixel intensities


__Templates__:

- `#!c++ ImageD,ImageD`
- `#!c++ ImageD,ImageUC`
- `#!c++ ImageUC,ImageB`
- `#!c++ ImageUC,ImageD`
- `#!c++ ImageUC,ImageF`
- `#!c++ ImageUC,ImageUC`
- `#!c++ ImageUC,ImageUI`
- `#!c++ ImageUC,ImageUS`
- `#!c++ ImageUS,ImageUC`

__Target__: `image`

__namespace__: `#!c++ sofa::component::engine`

__parents__: 

- `#!c++ DataEngine`

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
		<td>filter</td>
		<td>
Filter
</td>
		<td>0 - Piecewise Linear ( i1, o1, i2, o2 ...)</td>
	</tr>
	<tr>
		<td>param</td>
		<td>
Parameters
</td>
		<td></td>
	</tr>
	<tr>
		<td>inputImage</td>
		<td>

</td>
		<td>0 0 0 0 0</td>
	</tr>
	<tr>
		<td>outputImage</td>
		<td>

</td>
		<td>0 0 0 0 0</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|



