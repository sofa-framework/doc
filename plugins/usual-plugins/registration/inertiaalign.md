<!-- generate_doc -->
# InertiaAlign

An engine computing inertia matrix and the principal direction of a mesh


__Target__: Registration

__namespace__: sofa::component

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
		<td>targetCenter</td>
		<td>
input: the gravity center of the target mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td>sourceCenter</td>
		<td>
input: the gravity center of the source mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td>targetInertiaMatrix</td>
		<td>
input: the inertia matrix of the target mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td>sourceInertiaMatrix</td>
		<td>
input: the inertia matrix of the source mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td>targetPosition</td>
		<td>
input: positions of the target vertices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>sourcePosition</td>
		<td>
input: positions of the source vertices
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

