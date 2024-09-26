<!-- generate_doc -->
# QuadPressureForceField

Pressure applied on a quadrangular geometry.


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.MechanicalLoad

__namespace__: sofa::component::mechanicalload

__parents__:

- ForceField

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
	<tr>
		<td>pressure</td>
		<td>
Pressure force per unit area
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quadList</td>
		<td>
Indices of quads separated with commas where a pressure is applied
		</td>
		<td></td>
	</tr>
	<tr>
		<td>normal</td>
		<td>
Normal direction for the plane selection of quads
		</td>
		<td></td>
	</tr>
	<tr>
		<td>dmin</td>
		<td>
Minimum distance from the origin along the normal direction
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>dmax</td>
		<td>
Maximum distance from the origin along the normal direction
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>quadPressureMap</td>
		<td>
Map between quad indices and their pressure
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showForces</td>
		<td>
draw quads which have a given pressure
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|
|topology|link to the topology container|BaseMeshTopology|

