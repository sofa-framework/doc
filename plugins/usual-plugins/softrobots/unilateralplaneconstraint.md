<!-- generate_doc -->
# UnilateralPlaneConstraint

This component is a simple point plane collision model. 
By providing 4 points to the component, the first point will 
be constrained to stay in one side of the plane described 
by the three other points (in the direction of the plane normal). 
All the four points, the triangle and the normal can be 
seen by allowing the 'Collision Model' in the 'View' tab.


## Vec3d

Templates:

- Vec3d

__Target__: SoftRobots

__namespace__: softrobots::constraint

__parents__:

- SoftRobotsConstraint

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
Four indices: 
-First one for the constrained point 
-The others to describe the plane
		</td>
		<td></td>
	</tr>
	<tr>
		<td>flipNormal</td>
		<td>
The normal must be to the direction of the point
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

