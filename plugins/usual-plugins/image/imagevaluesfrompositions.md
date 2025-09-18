<!-- generate_doc -->
# ImageValuesFromPositions

Get image intensities at sample locations


Templates:

- ImageB
- ImageD
- ImageUC

__Target__: image

__namespace__: sofa::component::engine

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
list of the subsets the object belongs to
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

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|

