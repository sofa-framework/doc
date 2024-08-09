<!-- generate_doc -->
# RegistrationExporter

Replicate loaded obj files into path, with current positions


__Target__: Registration

__namespace__: sofa::component::misc

__parents__:

- BaseObject

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
		<td>path</td>
		<td>
output path
		</td>
		<td></td>
	</tr>
	<tr>
		<td>position</td>
		<td>
points position (will use mechanical state if this is empty)
		</td>
		<td></td>
	</tr>
	<tr>
		<td>applyInverseTransform</td>
		<td>
apply inverse transform specified in loaders
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>exportEveryNumberOfSteps</td>
		<td>
export file only at specified number of steps (0=disable)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>exportAtBegin</td>
		<td>
export file at the initialization
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>exportAtEnd</td>
		<td>
export file when the simulation is finished
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

