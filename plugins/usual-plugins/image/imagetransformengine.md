<!-- generate_doc -->
# ImageTransformEngine

Apply a transform to the data 'transform


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
		<td>inputTransform</td>
		<td>

		</td>
		<td>0 0 0 0 0 0 1 1 1 0 1 0</td>
	</tr>
	<tr>
		<td>outputTransform</td>
		<td>

		</td>
		<td>0 0 0 0 0 0 1 1 1 0 1 0</td>
	</tr>
	<tr>
		<td>translation</td>
		<td>
translation vector 
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>rotation</td>
		<td>
rotation vector 
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>scale</td>
		<td>
scale factor
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>inverse</td>
		<td>
true to apply inverse transformation
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

