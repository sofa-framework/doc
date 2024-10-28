<!-- generate_doc -->
# ArticulationCenter

This class defines an articulation center. This contains a set of articulations.


__Target__: ArticulatedSystemPlugin

__namespace__: sofa::component::container

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
		<td>parentIndex</td>
		<td>
Parent of the center articulation
		</td>
		<td></td>
	</tr>
	<tr>
		<td>childIndex</td>
		<td>
Child of the center articulation
		</td>
		<td></td>
	</tr>
	<tr>
		<td>globalPosition</td>
		<td>
Global position of the articulation center
		</td>
		<td></td>
	</tr>
	<tr>
		<td>posOnParent</td>
		<td>
Parent position of the articulation center
		</td>
		<td></td>
	</tr>
	<tr>
		<td>posOnChild</td>
		<td>
Child position of the articulation center
		</td>
		<td></td>
	</tr>
	<tr>
		<td>articulationProcess</td>
		<td>
 0 - (default) hierarchy between articulations (euler angles)
 1- ( on Parent) no hierarchy - axis are attached to the parent
 2- (attached on Child) no hierarchy - axis are attached to the child
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

