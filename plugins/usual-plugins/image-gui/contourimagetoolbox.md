# ContourImageToolBox

ContourImageToolBox


__Templates__:

- `#!c++ ImageD`
- `#!c++ ImageUC`

__Target__: `image_gui`

__namespace__: `#!c++ sofa::component::engine`

__parents__: 

- `#!c++ ContourImageToolBoxNoTemplated`

__categories__: 

- Engine

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
		<td>islinkedtotoolbox</td>
		<td>
true if a toobbox use this Label
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>color</td>
		<td>

</td>
		<td>1 1 1 1</td>
	</tr>
	<tr>
		<td>imageposition</td>
		<td>

</td>
		<td></td>
	</tr>
	<tr>
		<td>3Dposition</td>
		<td>

</td>
		<td></td>
	</tr>
	<tr>
		<td>axis</td>
		<td>

</td>
		<td>4</td>
	</tr>
	<tr>
		<td>value</td>
		<td>

</td>
		<td></td>
	</tr>
	<tr>
		<td>out</td>
		<td>
Output list of space position of each pixel on contour
</td>
		<td></td>
	</tr>
	<tr>
		<td>out2</td>
		<td>
Output list of image position of each pixel on contour
</td>
		<td></td>
	</tr>
	<tr>
		<td>threshold</td>
		<td>

</td>
		<td></td>
	</tr>
	<tr>
		<td>radius</td>
		<td>

</td>
		<td></td>
	</tr>
	<tr>
		<td>image</td>
		<td>
Input image
</td>
		<td></td>
	</tr>
	<tr>
		<td>transform</td>
		<td>
Transform
</td>
		<td></td>
	</tr>
	<tr>
		<td>imageOut</td>
		<td>
Image containing the contour
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



