# ImageCoordValuesFromPositions

Get interpolated coordinates at sample locations in an image with 3 channels


__Templates__:

- `#!c++ ImageD`
- `#!c++ ImageF`

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
		<td>image</td>
		<td>

</td>
		<td>0 0 0 0 0</td>
	</tr>
	<tr>
		<td>transform</td>
		<td>

</td>
		<td>0 0 0 0 0 0 1 1 1 0 1 0</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
input positions
</td>
		<td></td>
	</tr>
	<tr>
		<td>interpolation</td>
		<td>
Interpolation method.
</td>
		<td></td>
	</tr>
	<tr>
		<td>values</td>
		<td>
Interpolated values.
</td>
		<td></td>
	</tr>
	<tr>
		<td>outValue</td>
		<td>
default value outside image
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>addPosition</td>
		<td>
add positions to interpolated values (to get translated positions)
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



