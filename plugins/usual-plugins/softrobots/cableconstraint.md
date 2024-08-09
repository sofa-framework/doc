<!-- generate_doc -->
# CableConstraint

Simulate a cable.


## Vec2d

Templates:

- Vec2d

__Target__: SoftRobots

__namespace__: softrobots::constraint

__parents__:

- CableModel

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
		<td>group</td>
		<td>
ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>constraintIndex</td>
		<td>
Constraint index (first index in the right hand term resolution vector)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>endTime</td>
		<td>
The SoftRobotsConstraint stops acting after the given value.
Use a negative value for infinite SoftRobotsConstraints
		</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
List of points connected by the cable (from extremity to actuated point). 
If no indices are given, default value is 0. 
In case of multiple indices, one point will be actuated 
and the others will represent sliding points for the cable.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>pullPoint</td>
		<td>
Fixed point from which the cable is pulled. 
If unspecified, the default value is {0.0,0.0,0.0}
		</td>
		<td>0 0</td>
	</tr>
	<tr>
		<td>hasPullPoint</td>
		<td>
If false, the pull point is not considered and the cable is entirely mapped 
 In that case, needs at least 2 different point in indices.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>cableInitialLength</td>
		<td>
This value can be defined by the user. 
If not defined, it will correspond to the length of the cable at the start of the simulation
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>cableLength</td>
		<td>
Computation done at the end of the time step
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>method</td>
		<td>
Default is point method. 
In point method, cable force is applied on a single point. 
Both methods sphere and geodesic are compatible with passing point on a surface only. 
 In sphere method, cable force is dispatched in the intersection between a 3D sphere and a surface. 
In geodesic method, cable force is dispatched in a circle projected on a surface. 

		</td>
		<td>point</td>
	</tr>
	<tr>
		<td>centers</td>
		<td>
List of positions describing attachment of cables on the surface, used only with sphere and geodesic methods. 
Points are centers of cable pulling application areas. 
If not defined, centers are computed from provided indices instead.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>radii</td>
		<td>
List of radius used to compute pulling application areas from centers. 
Used only with sphere and geodesic methods.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>maxForce</td>
		<td>
Maximum force of the actuator. 
If unspecified no maximum value will be considered.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>minForce</td>
		<td>
Minimum force of the actuator. 
If unspecified no minimum value will be considered 
and the cable will then be seen as a stiff rod able to push.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>eqForce</td>
		<td>
Equality force of the actuator. 
Solver will try to maintain the cable force at this value
If unspecified, no value will be considered 

		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>maxPositiveDisp</td>
		<td>
Maximum displacement of the actuator in the positive direction. 
If unspecified no maximum value will be considered.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>maxNegativeDisp</td>
		<td>
Maximum displacement of the actuator in the negative direction. 
If unspecified no maximum value will be considered.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>eqDisp</td>
		<td>
Equality displacement of the actuator. 
Solver will try to maintain the cable displacement at this value
If unspecified, no value will be considered 

		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>maxDispVariation</td>
		<td>
Maximum variation of the displacement allowed. If not set, no max variation will be concidered.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>value</td>
		<td>
Displacement or force to impose.

		</td>
		<td></td>
	</tr>
	<tr>
		<td>valueIndex</td>
		<td>
Index of the value (in InputValue vector) that we want to impose 
If unspecified the default value is {0}
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>valueType</td>
		<td>
displacement = the contstraint will impose the displacement provided in data value[valueIndex] 
force = the contstraint will impose the force provided in data value[valueIndex] 
If unspecified, the default value is displacement
		</td>
		<td>displacement</td>
	</tr>
	<tr>
		<td colspan="3">Vector</td>
	</tr>
	<tr>
		<td>force</td>
		<td>
Output force. Warning: to get the actual force you should divide this value by dt.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>displacement</td>
		<td>
Output displacement compared to the initial cable length.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawPullPoint</td>
		<td>

		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>drawPoints</td>
		<td>

		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>drawPulledAreas</td>
		<td>
Whether to draw pulled area points or not.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>color</td>
		<td>
Color of the string.
		</td>
		<td>0.4 0.4 0.4 1</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|surfaceTopology|Link to the topology container of the surface on which the cable is attached. 
Used only with sphere and geodesic methods.|BaseMeshTopology|

<!-- generate_doc -->
## Vec3d

Templates:

- Vec3d

__Target__: SoftRobots

__namespace__: softrobots::constraint

__parents__:

- CableModel

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
		<td>group</td>
		<td>
ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>constraintIndex</td>
		<td>
Constraint index (first index in the right hand term resolution vector)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>endTime</td>
		<td>
The SoftRobotsConstraint stops acting after the given value.
Use a negative value for infinite SoftRobotsConstraints
		</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
List of points connected by the cable (from extremity to actuated point). 
If no indices are given, default value is 0. 
In case of multiple indices, one point will be actuated 
and the others will represent sliding points for the cable.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>pullPoint</td>
		<td>
Fixed point from which the cable is pulled. 
If unspecified, the default value is {0.0,0.0,0.0}
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>hasPullPoint</td>
		<td>
If false, the pull point is not considered and the cable is entirely mapped 
 In that case, needs at least 2 different point in indices.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>cableInitialLength</td>
		<td>
This value can be defined by the user. 
If not defined, it will correspond to the length of the cable at the start of the simulation
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>cableLength</td>
		<td>
Computation done at the end of the time step
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>method</td>
		<td>
Default is point method. 
In point method, cable force is applied on a single point. 
Both methods sphere and geodesic are compatible with passing point on a surface only. 
 In sphere method, cable force is dispatched in the intersection between a 3D sphere and a surface. 
In geodesic method, cable force is dispatched in a circle projected on a surface. 

		</td>
		<td>point</td>
	</tr>
	<tr>
		<td>centers</td>
		<td>
List of positions describing attachment of cables on the surface, used only with sphere and geodesic methods. 
Points are centers of cable pulling application areas. 
If not defined, centers are computed from provided indices instead.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>radii</td>
		<td>
List of radius used to compute pulling application areas from centers. 
Used only with sphere and geodesic methods.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>maxForce</td>
		<td>
Maximum force of the actuator. 
If unspecified no maximum value will be considered.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>minForce</td>
		<td>
Minimum force of the actuator. 
If unspecified no minimum value will be considered 
and the cable will then be seen as a stiff rod able to push.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>eqForce</td>
		<td>
Equality force of the actuator. 
Solver will try to maintain the cable force at this value
If unspecified, no value will be considered 

		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>maxPositiveDisp</td>
		<td>
Maximum displacement of the actuator in the positive direction. 
If unspecified no maximum value will be considered.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>maxNegativeDisp</td>
		<td>
Maximum displacement of the actuator in the negative direction. 
If unspecified no maximum value will be considered.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>eqDisp</td>
		<td>
Equality displacement of the actuator. 
Solver will try to maintain the cable displacement at this value
If unspecified, no value will be considered 

		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>maxDispVariation</td>
		<td>
Maximum variation of the displacement allowed. If not set, no max variation will be concidered.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>value</td>
		<td>
Displacement or force to impose.

		</td>
		<td></td>
	</tr>
	<tr>
		<td>valueIndex</td>
		<td>
Index of the value (in InputValue vector) that we want to impose 
If unspecified the default value is {0}
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>valueType</td>
		<td>
displacement = the contstraint will impose the displacement provided in data value[valueIndex] 
force = the contstraint will impose the force provided in data value[valueIndex] 
If unspecified, the default value is displacement
		</td>
		<td>displacement</td>
	</tr>
	<tr>
		<td colspan="3">Vector</td>
	</tr>
	<tr>
		<td>force</td>
		<td>
Output force. Warning: to get the actual force you should divide this value by dt.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>displacement</td>
		<td>
Output displacement compared to the initial cable length.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawPullPoint</td>
		<td>

		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>drawPoints</td>
		<td>

		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>drawPulledAreas</td>
		<td>
Whether to draw pulled area points or not.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>color</td>
		<td>
Color of the string.
		</td>
		<td>0.4 0.4 0.4 1</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|surfaceTopology|Link to the topology container of the surface on which the cable is attached. 
Used only with sphere and geodesic methods.|BaseMeshTopology|

