<!-- generate_doc -->
# GroupFilterYoungModulus

Engine defining a vector of young modulus according of a list of defined groups.


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.Engine.Generate

__namespace__: sofa::component::engine::generate

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
		<td>elementsGroup</td>
		<td>
Vector of groups (each element gives its group
		</td>
		<td></td>
	</tr>
	<tr>
		<td>mapGroupModulus</td>
		<td>
Mapping between groups and modulus
		</td>
		<td></td>
	</tr>
	<tr>
		<td>defaultYoungModulus</td>
		<td>
Default value if the primitive is not in a group
		</td>
		<td>10000</td>
	</tr>
	<tr>
		<td>groupModulus</td>
		<td>
list of young modulus for each group
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>groups</td>
		<td>
Groups
		</td>
		<td></td>
	</tr>
	<tr>
		<td>primitives</td>
		<td>
Vector of primitives (indices)
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>youngModulus</td>
		<td>
Vector of young modulus for each primitive
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
