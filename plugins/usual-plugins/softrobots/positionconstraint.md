<!-- generate_doc -->
# PositionConstraint

Simulate a Position.


## Rigid3d

Templates:

- Rigid3d

__Target__: SoftRobots

__namespace__: softrobots::constraint

__parents__:

- PositionModel

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
If indices size is lower than target size, 
some target will not be considered
		</td>
		<td></td>
	</tr>
	<tr>
		<td>weight</td>
		<td>
The parameter sets a weight to the minimization.
		</td>
		<td>1 1 1 1 1 1</td>
	</tr>
	<tr>
		<td>directions</td>
		<td>
The parameter directions allows to specify the directions in 
which you want to solve the position.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>useDirections</td>
		<td>
The parameter useDirections allows to select the directions in 
which you want to solve the position. If unspecified, the default 
values are all true.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>delta</td>
		<td>
Distance to target
		</td>
		<td></td>
	</tr>
	<tr>
		<td>maxForce</td>
		<td>
Maximum force allowed. 
If unspecified no maximum value will be considered.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>minForce</td>
		<td>
Minimum force allowed. 
If unspecified no minimum value will be considered.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>maxPositiveDisp</td>
		<td>
Maximum displacement in the positive direction. 
If unspecified no maximum value will be considered.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>maxNegativeDisp</td>
		<td>
Maximum displacement in the negative direction. 
If unspecified no maximum value will be considered.
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
displacement = the constraint will impose the displacement provided in data value[valueIndex] 
force = the constraint will impose the force provided in data value[valueIndex] 
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
Output displacement compared to the initial position.
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

<!-- generate_doc -->
## Vec2d

Templates:

- Vec2d

__Target__: SoftRobots

__namespace__: softrobots::constraint

__parents__:

- PositionModel

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
If indices size is lower than target size, 
some target will not be considered
		</td>
		<td></td>
	</tr>
	<tr>
		<td>weight</td>
		<td>
The parameter sets a weight to the minimization.
		</td>
		<td>1 1</td>
	</tr>
	<tr>
		<td>directions</td>
		<td>
The parameter directions allows to specify the directions in 
which you want to solve the position.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>useDirections</td>
		<td>
The parameter useDirections allows to select the directions in 
which you want to solve the position. If unspecified, the default 
values are all true.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>delta</td>
		<td>
Distance to target
		</td>
		<td></td>
	</tr>
	<tr>
		<td>maxForce</td>
		<td>
Maximum force allowed. 
If unspecified no maximum value will be considered.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>minForce</td>
		<td>
Minimum force allowed. 
If unspecified no minimum value will be considered.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>maxPositiveDisp</td>
		<td>
Maximum displacement in the positive direction. 
If unspecified no maximum value will be considered.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>maxNegativeDisp</td>
		<td>
Maximum displacement in the negative direction. 
If unspecified no maximum value will be considered.
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
displacement = the constraint will impose the displacement provided in data value[valueIndex] 
force = the constraint will impose the force provided in data value[valueIndex] 
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
Output displacement compared to the initial position.
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

<!-- generate_doc -->
## Vec3d

Templates:

- Vec3d

__Target__: SoftRobots

__namespace__: softrobots::constraint

__parents__:

- PositionModel

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
If indices size is lower than target size, 
some target will not be considered
		</td>
		<td></td>
	</tr>
	<tr>
		<td>weight</td>
		<td>
The parameter sets a weight to the minimization.
		</td>
		<td>1 1 1</td>
	</tr>
	<tr>
		<td>directions</td>
		<td>
The parameter directions allows to specify the directions in 
which you want to solve the position.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>useDirections</td>
		<td>
The parameter useDirections allows to select the directions in 
which you want to solve the position. If unspecified, the default 
values are all true.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>delta</td>
		<td>
Distance to target
		</td>
		<td></td>
	</tr>
	<tr>
		<td>maxForce</td>
		<td>
Maximum force allowed. 
If unspecified no maximum value will be considered.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>minForce</td>
		<td>
Minimum force allowed. 
If unspecified no minimum value will be considered.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>maxPositiveDisp</td>
		<td>
Maximum displacement in the positive direction. 
If unspecified no maximum value will be considered.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>maxNegativeDisp</td>
		<td>
Maximum displacement in the negative direction. 
If unspecified no maximum value will be considered.
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
displacement = the constraint will impose the displacement provided in data value[valueIndex] 
force = the constraint will impose the force provided in data value[valueIndex] 
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
Output displacement compared to the initial position.
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

