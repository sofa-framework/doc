<!-- generate_doc -->
# BeamInterpolation

Adaptive Beam Interpolation


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
	<tr>
		<td>crossSectionShape</td>
		<td>
shape of the cross-section. Can be: circular, elliptic, square, rectangular. Default is circular
		</td>
		<td>circular</td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
radius of the beam (if circular cross-section is considered)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>innerRadius</td>
		<td>
inner radius of the beam if it applies
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>sideLength</td>
		<td>
side length of the beam (if square cross-section is considered)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>smallRadius</td>
		<td>
small radius of the beam (if elliptic cross-section is considered)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>largeRadius</td>
		<td>
large radius of the beam (if elliptic cross-section is considered)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>lengthY</td>
		<td>
length of the beam section along Y (if rectangular cross-section is considered)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>lengthZ</td>
		<td>
length of the beam section along Z (if rectangular cross-section is considered)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>defaultYoungModulus</td>
		<td>
value of the young modulus if not defined in an other component
		</td>
		<td>100000</td>
	</tr>
	<tr>
		<td>defaultPoissonRatio</td>
		<td>
value of the poisson ratio if not defined in an other component
		</td>
		<td>0.4</td>
	</tr>
	<tr>
		<td>straight</td>
		<td>
If true, will consider straight beams for the rest position
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>vecID</td>
		<td>
input pos and vel (current, free pos/vel, rest pos)
		</td>
		<td>current</td>
	</tr>
	<tr>
		<td>InterpolationInputs</td>
		<td>
vector containing (beamID, baryCoord)
		</td>
		<td></td>
	</tr>
	<tr>
		<td>InterpolatedPos</td>
		<td>
output Interpolated Position
		</td>
		<td></td>
	</tr>
	<tr>
		<td>InterpolatedVel</td>
		<td>
output Interpolated Velocity
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
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Rigid3d&gt;|
|topology|link to the topology (must contain edges)|BaseMeshTopology|

