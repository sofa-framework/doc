<!-- generate_doc -->
# MechanicalObject

mechanical state vectors


Templates:

- Rigid2d
- Rigid3d
- Vec1d
- Vec2d
- Vec3d
- Vec6d

__Target__: Sofa.Component.StateContainer

__namespace__: sofa::component::statecontainer

__parents__:

- MechanicalState

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
		<td>restScale</td>
		<td>
optional scaling of rest position coordinates (to simulated pre-existing internal tension).(default = 1.0)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>useTopology</td>
		<td>
Shall this object rely on any active topology to initialize its size and positions
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>size</td>
		<td>
Size of the vectors
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>reserve</td>
		<td>
Size to reserve when creating vectors. (default=0)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">States</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
position coordinates of the degrees of freedom
		</td>
		<td></td>
	</tr>
	<tr>
		<td>velocity</td>
		<td>
velocity coordinates of the degrees of freedom
		</td>
		<td></td>
	</tr>
	<tr>
		<td>derivX</td>
		<td>
dx vector of the degrees of freedom
		</td>
		<td></td>
	</tr>
	<tr>
		<td>reset_position</td>
		<td>
reset position coordinates of the degrees of freedom
		</td>
		<td></td>
	</tr>
	<tr>
		<td>reset_velocity</td>
		<td>
reset velocity coordinates of the degrees of freedom
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Force</td>
	</tr>
	<tr>
		<td>force</td>
		<td>
force vector of the degrees of freedom
		</td>
		<td></td>
	</tr>
	<tr>
		<td>externalForce</td>
		<td>
externalForces vector of the degrees of freedom
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Rest States</td>
	</tr>
	<tr>
		<td>rest_position</td>
		<td>
rest position coordinates of the degrees of freedom
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Free Motion</td>
	</tr>
	<tr>
		<td>free_position</td>
		<td>
free position coordinates of the degrees of freedom
		</td>
		<td></td>
	</tr>
	<tr>
		<td>free_velocity</td>
		<td>
free velocity coordinates of the degrees of freedom
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Jacobian</td>
	</tr>
	<tr>
		<td>constraint</td>
		<td>
constraints applied to the degrees of freedom
		</td>
		<td></td>
	</tr>
	<tr>
		<td>mappingJacobian</td>
		<td>
mappingJacobian applied to the degrees of freedom
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showObject</td>
		<td>
Show objects. (default=false)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showObjectScale</td>
		<td>
Scale for object display. (default=0.1)
		</td>
		<td>0.1</td>
	</tr>
	<tr>
		<td>showIndices</td>
		<td>
Show indices. (default=false)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showIndicesScale</td>
		<td>
Scale for indices display. (default=0.02)
		</td>
		<td>0.02</td>
	</tr>
	<tr>
		<td>showVectors</td>
		<td>
Show velocity. (default=false)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showVectorsScale</td>
		<td>
Scale for vectors display. (default=0.0001)
		</td>
		<td>0.0001</td>
	</tr>
	<tr>
		<td>drawMode</td>
		<td>
The way vectors will be drawn:
- 0: Line
- 1:Cylinder
- 2: Arrow.

The DOFS will be drawn:
- 0: point
- >1: sphere. (default=0)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showColor</td>
		<td>
Color for object display. (default=[1 1 1 1])
		</td>
		<td>1 1 1 1</td>
	</tr>
	<tr>
		<td colspan="3">Transformation</td>
	</tr>
	<tr>
		<td>translation</td>
		<td>
Translation of the DOFs
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>rotation</td>
		<td>
Rotation of the DOFs
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>scale3d</td>
		<td>
Scale of the DOFs in 3 dimensions
		</td>
		<td>1 1 1</td>
	</tr>
	<tr>
		<td>translation2</td>
		<td>
Translation of the DOFs, applied after the rest position has been computed
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>rotation2</td>
		<td>
Rotation of the DOFs, applied the after the rest position has been computed
		</td>
		<td>0 0 0</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|topology|Link to the topology relevant for this object|BaseMeshTopology|

