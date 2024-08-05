# IndicesFromValues

Find the indices of a list of values within a larger set of values


__Templates__:

- `#!c++ I`
- `#!c++ Vec2d`
- `#!c++ Vec3d`
- `#!c++ d`
- `#!c++ fixed_array<I,2>`
- `#!c++ fixed_array<I,3>`
- `#!c++ fixed_array<I,4>`
- `#!c++ fixed_array<I,8>`
- `#!c++ i`
- `#!c++ string`

__Target__: `Sofa.Component.Engine.Select`

__namespace__: `#!c++ sofa::component::engine::select`

__parents__: 

- `#!c++ DataEngine`

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
		<td>recursiveSearch</td>
		<td>
if set to true, output are indices of the "global" data matching with one of the values
</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>values</td>
		<td>
input values
</td>
		<td></td>
	</tr>
	<tr>
		<td>global</td>
		<td>
Global values, in which the input values are searched
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
Output indices of the given values, searched in global
</td>
		<td></td>
	</tr>
	<tr>
		<td>otherIndices</td>
		<td>
Output indices of the other values, (NOT the given ones) searched in global
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



