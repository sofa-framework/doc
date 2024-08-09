<!-- generate_doc -->
# MapIndices

Apply a permutation to a set of indices


Templates:

- I
- fixed_array<I,2>
- fixed_array<I,3>
- fixed_array<I,4>
- fixed_array<I,8>
- i

__Target__: Sofa.Component.Engine.Transform

__namespace__: sofa::component::engine::transform

__parents__:

- DataEngine

### Data

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
		<td>outStr</td>
		<td>
Output indices, converted as a string
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>in</td>
		<td>
input indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
array containing in ith cell the input index corresponding to the output index i (or reversively if transpose=true)
		</td>
		<td></td>
	</tr>
	<tr>
		<td>transpose</td>
		<td>
Should the transposed mapping be used ?
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>out</td>
		<td>
Output indices
		</td>
		<td></td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|

