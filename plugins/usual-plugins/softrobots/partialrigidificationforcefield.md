<!-- generate_doc -->
# PartialRigidificationForceField

Partially rigidify a mechanical object using a rigid mapping.


## Vec3d,Rigid3d

Templates:

- Vec3d,Rigid3d

__Target__: SoftRobots

__namespace__: softrobots::forcefield

__parents__:

- MixedInteractionForceField

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
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping - stiffness matrix coefficient
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
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|object1|First object associated to this component|MechanicalState&lt;Vec3d&gt;|
|object2|Second object associated to this component|MechanicalState&lt;Rigid3d&gt;|
|rigidMapping|link to the rigidMapping that does the rigidification|RigidMapping&lt;Rigid3d,Vec3d&gt;|
|subsetMultiMapping|link to the subsetMultiMapping that unifies rigid and deformable parts|SubsetMultiMapping&lt;Vec3d,Vec3d&gt;|
|mappedForceField|link to the forcefield that is mapped under the subsetMultiMapping|BaseForceField|

