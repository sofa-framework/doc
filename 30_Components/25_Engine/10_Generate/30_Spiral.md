---
title: Spiral
---

Spiral
======

This component belongs to the category of [Engines](https://www.sofa-framework.org/community/doc/simulation-principles/engine/). This engine turns on spiral any topological model.

Input Data
----------

-   **rest_position**: rest position of the mechanical object

Output Data
----------

-   **position**: position of the mechanical object once it has been turned on spiral

Additional Parameter
--------------------

-   **curvature**: real defining the curvature of the spiral

Examples
--------

An example scene involving the Spiral engine is available in [*examples/Component/Engine/Generate/spiral.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/Engine/Generate/spiral.scn)
<!-- automatically generated doc START -->
__Target__: `Sofa.Component.Engine.Generate`

__namespace__: `#!c++ sofa::component::engine::generate`

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
		<td>curvature</td>
		<td>
Spiral curvature factor
</td>
		<td>0.2</td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>rest_position</td>
		<td>
Rest position coordinates of the degrees of freedom
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Position coordinates of the degrees of freedom
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




<!-- automatically generated doc END -->
