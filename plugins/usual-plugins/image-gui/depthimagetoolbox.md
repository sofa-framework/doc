# DepthImageToolBox

DepthImageToolBox


__Target__: `image_gui`

__namespace__: `#!c++ sofa::component::engine`

__parents__: 

- `#!c++ LabelImageToolBox`

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
		<td>filename</td>
		<td>

</td>
		<td></td>
	</tr>
	<tr>
		<td>scnfilename</td>
		<td>

</td>
		<td></td>
	</tr>
	<tr>
		<td>transform</td>
		<td>
Transform
</td>
		<td>0 0 0 0 0 0 1 1 1 0 1 0</td>
	</tr>
	<tr>
		<td>tagfilter</td>
		<td>

</td>
		<td></td>
	</tr>
	<tr>
		<td>image</td>
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



