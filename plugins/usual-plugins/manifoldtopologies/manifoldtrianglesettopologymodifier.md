<!-- generate_doc -->
# ManifoldTriangleSetTopologyModifier

Triangle set topology manifold modifier


__Target__: ManifoldTopologies

__namespace__: sofa::component::topology::container::dynamic

__parents__:

- TriangleSetTopologyModifier

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
		<td>propagateToDOF</td>
		<td>
Propagate changes to Mechanical object DOFs
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>list_Out</td>
		<td>
triangles with at least one null values.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>swap 2 triangles by their index</td>
		<td>
Debug : Test swap function (only while animate).
		</td>
		<td></td>
	</tr>
	<tr>
		<td>Mesh Optimization</td>
		<td>
If true, optimize the mesh only by swapping edges
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

