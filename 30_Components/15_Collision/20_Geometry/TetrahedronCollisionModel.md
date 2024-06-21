# TetrahedronCollisionModel

collision model using a tetrahedral mesh, as described in BaseMeshTopology


__Target__: `Sofa.Component.Collision.Geometry`

__namespace__: `#!c++ sofa::component::collision::geometry`

__parents__: 

- `#!c++ CollisionModel`

Data: 

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
		<td>active</td>
		<td>
flag indicating if this collision model is active and should be included in default collision detections
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>moving</td>
		<td>
flag indicating if this object is changing position between iterations
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>simulated</td>
		<td>
flag indicating if this object is controlled by a simulation
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>selfCollision</td>
		<td>
flag indication if the object can self collide
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>proximity</td>
		<td>
Distance to the actual (visual) surface
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>contactStiffness</td>
		<td>
Contact stiffness
</td>
		<td>10</td>
	</tr>
	<tr>
		<td>contactFriction</td>
		<td>
Contact friction coefficient (dry or viscous or unused depending on the contact method)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>contactRestitution</td>
		<td>
Contact coefficient of restitution
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>contactResponse</td>
		<td>
if set, indicate to the ContactManager that this model should use the given class of contacts.
Note that this is only indicative, and in particular if both collision models specify a different class it is up to the manager to choose.
</td>
		<td></td>
	</tr>
	<tr>
		<td>color</td>
		<td>
color used to display the collision model if requested
</td>
		<td>1 0 0 1</td>
	</tr>
	<tr>
		<td>group</td>
		<td>
IDs of the groups containing this model. No collision can occur between collision models included in a common group (e.g. allowing the same object to have multiple collision models)
</td>
		<td></td>
	</tr>
	<tr>
		<td>numberOfContacts</td>
		<td>
Number of collision models this collision model is currently attached to
</td>
		<td>0</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|previous|Previous (coarser / upper / parent level) CollisionModel in the hierarchy.|
|next|Next (finer / lower / child level) CollisionModel in the hierarchy.|
|collisionElementActiver|CollisionElementActiver component that activates or deactivates collision element(s) during execution|
|topology|link to the topology container|



