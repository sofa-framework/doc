<!-- generate_doc -->
# WireBeamInterpolation

Adaptive Beam Interpolation on Wire rest Shape


## Rigid3d

Templates:

- Rigid3d

__Target__: BeamAdapter

__namespace__: beamadapter

__parents__:

- BaseBeamInterpolation

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
		<td>edgeList</td>
		<td>
list of the edge in the topology that are concerned by the Interpolation
		</td>
		<td></td>
	</tr>
	<tr>
		<td>lengthList</td>
		<td>
list of the length of each beam
		</td>
		<td></td>
	</tr>
	<tr>
		<td>DOF0TransformNode0</td>
		<td>
Optional rigid transformation between the degree of Freedom and the first node of the beam
		</td>
		<td></td>
	</tr>
	<tr>
		<td>DOF1TransformNode1</td>
		<td>
Optional rigid transformation between the degree of Freedom and the second node of the beam
		</td>
		<td></td>
	</tr>
	<tr>
		<td>curvAbsList</td>
		<td>

		</td>
		<td></td>
	</tr>
	<tr>
		<td>beamCollision</td>
		<td>
list of beam (in edgeList) that needs to be considered for collision
		</td>
		<td></td>
	</tr>
	<tr>
		<td>dofsAndBeamsAligned</td>
		<td>
if false, a transformation for each beam is computed between the DOF and the beam nodes
		</td>
		<td>1</td>
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Rigid3d&gt;|
|topology|link to the topology (must contain edges)|BaseMeshTopology|
|WireRestShape|link to the component on the scene|WireRestShape&lt;Rigid3d&gt;|

