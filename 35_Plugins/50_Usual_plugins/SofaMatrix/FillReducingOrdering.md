# FillReducingOrdering

Reorder the degrees of freedom to reduce fill-in


__Templates__:

- `#!c++ Vec3d`

__Target__: `SofaMatrix`

__namespace__: `#!c++ sofa::component::linearsolver`

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
		<td>orderingMethod</td>
		<td>
Ordering method.
nestedDissection is the multilevel nested dissection algorithm implemented in the METIS library.
approximateMinimumDegree is the approximate minimum degree algorithm implemented in the Eigen library.
</td>
		<td>nestedDissection</td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>permutation</td>
		<td>
Output vector of indices mapping the reordered vertices to the initial list
</td>
		<td></td>
	</tr>
	<tr>
		<td>invPermutation</td>
		<td>
Output vector of indices mapping the initial vertices to the reordered list
</td>
		<td></td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Reordered position vector
</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedra</td>
		<td>
Reordered hexahedra
</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedra</td>
		<td>
Reordered tetrahedra
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
|mstate|Mechanical state to reorder|
|topology|Topology to reorder|



