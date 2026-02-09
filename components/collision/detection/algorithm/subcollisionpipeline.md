<!-- generate_doc -->
# SubCollisionPipeline

Collision pipeline to be used with CompositeCollisionPipeline.


__Target__: Sofa.Component.Collision.Detection.Algorithm

__namespace__: sofa::component::collision::detection::algorithm

__parents__:

- BaseSubCollisionPipeline

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
		<td>depth</td>
		<td>
Max depth of bounding trees. (default=6, min=?, max=?)
		</td>
		<td>6</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|collisionModels|List of collision models to consider in this pipeline|CollisionModel|
|intersectionMethod|Intersection method to use in this pipeline|Intersection|
|contactManager|Contact manager to use in this pipeline|ContactManager|
|broadPhaseDetection|Broad phase detection to use in this pipeline|BroadPhaseDetection|
|narrowPhaseDetection|Narrow phase detection to use in this pipeline|NarrowPhaseDetection|

