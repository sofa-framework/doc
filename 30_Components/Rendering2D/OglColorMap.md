# OglColorMap

Provides color palette and support for conversion of numbers to colors.


__Target__: `Sofa.GL.Component.Rendering2D`

__namespace__: `#!c++ sofa::gl::component::rendering2d`

__parents__: 

- `#!c++ VisualModel`

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
		<td>enable</td>
		<td>
Display the object or not
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>paletteSize</td>
		<td>
How many colors to use
</td>
		<td>256</td>
	</tr>
	<tr>
		<td>colorScheme</td>
		<td>
Color scheme to use
</td>
		<td></td>
	</tr>
	<tr>
		<td>legendOffset</td>
		<td>
Draw the legend on screen with an x,y offset
</td>
		<td>10 5</td>
	</tr>
	<tr>
		<td>legendTitle</td>
		<td>
Font size of the legend (if any)
</td>
		<td></td>
	</tr>
	<tr>
		<td>legendSize</td>
		<td>
Add a title to the legend
</td>
		<td>11</td>
	</tr>
	<tr>
		<td>min</td>
		<td>
min value for drawing the legend without the need to actually use the range with getEvaluator method wich sets the min
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>max</td>
		<td>
max value for drawing the legend without the need to actually use the range with getEvaluator method wich sets the max
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>legendRangeScale</td>
		<td>
to change the unit of the min/max value of the legend
</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showLegend</td>
		<td>
Activate rendering of color scale legend on the side
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



