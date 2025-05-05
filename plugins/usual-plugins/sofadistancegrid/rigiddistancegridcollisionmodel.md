<!-- generate_doc -->
# RigidDistanceGridCollisionModel

Grid-based distance field.


__Target__: SofaDistanceGrid

__namespace__: sofa::component::collision

__parents__:

- CollisionModel

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
	<tr>
		<td>filename</td>
		<td>
Load distance grid from specified file
		</td>
		<td></td>
	</tr>
	<tr>
		<td>scale</td>
		<td>
scaling factor for input file
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>translation</td>
		<td>
translation to apply to input file
		</td>
		<td></td>
	</tr>
	<tr>
		<td>rotation</td>
		<td>
rotation to apply to input file
		</td>
		<td></td>
	</tr>
	<tr>
		<td>sampling</td>
		<td>
if not zero: sample the surface with points approximately separated by the given sampling distance (expressed in voxels if the value is negative)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>box</td>
		<td>
Field bounding box defined by xmin,ymin,zmin, xmax,ymax,zmax
		</td>
		<td></td>
	</tr>
	<tr>
		<td>nx</td>
		<td>
number of values on X axis
		</td>
		<td>64</td>
	</tr>
	<tr>
		<td>ny</td>
		<td>
number of values on Y axis
		</td>
		<td>64</td>
	</tr>
	<tr>
		<td>nz</td>
		<td>
number of values on Z axis
		</td>
		<td>64</td>
	</tr>
	<tr>
		<td>dumpfilename</td>
		<td>
write distance grid to specified file
		</td>
		<td></td>
	</tr>
	<tr>
		<td>usePoints</td>
		<td>
use mesh vertices for collision detection
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>flipNormals</td>
		<td>
reverse surface direction, i.e. points are considered in collision if they move outside of the object instead of inside
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showMeshPoints</td>
		<td>
Enable rendering of mesh points
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>showGridPoints</td>
		<td>
Enable rendering of grid points
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showMinDist</td>
		<td>
Min distance to render gradients
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showMaxDist</td>
		<td>
Max distance to render gradients
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
|previous|Previous (coarser / upper / parent level) CollisionModel in the hierarchy.|CollisionModel|
|next|Next (finer / lower / child level) CollisionModel in the hierarchy.|CollisionModel|
|collisionElementActiver|CollisionElementActiver component that activates or deactivates collision element(s) during execution|BaseObject|

