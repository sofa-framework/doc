---
title: MinProximityIntersection
---

MinProximityIntersection
========================

This proximity method for [intersection detection](../../../../../simulation-principles/multi-model-representation/collision/#narrow-phase-detect-intersection):

- detects a possible contact as soon as pair of collision elements are close to each other (distance smaller than the alarmDistance)
- and creates contact (aka DetectionOutput) when the distance is lower than contactDistance.

This method is optimized for meshes. The intersection is implemented for the following primitives: Triangle/Point, Line/Point, Line/Line, so that it covers all Triangle/Triangle intersections. To get a proper detection, the TriangleModel, LineModel and PointModel must be simultaneously used in the scene.

In the figure below, we describe the detection of the contacts for Object 1 due to an Object 2. It assumes here that a PointCollisionModel and a LineCollisionModel are defined. The detection gives:
- 2 Point-Point contacts (yellow)
- 1 Point-Line contact (blue)
- 1 Line-Line contact (pink)


<a href="https://github.com/sofa-framework/doc/blob/master/images/collision/MinProximityIntersection.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/collision/MinProximityIntersection.png?raw=true" title="Proximity detection using MinProximityIntersection" style="width: 70%;"/></a>

Although the method is working properly, the intersection might result in a high number of contacts. This works just fine for Penalty method (many springs will be generated). However, using a response method based on Lagrange multipliers, many constraints will be generated which might rapidly become computationally-demanding.

Moreover, the contacts can be a bit degenerated: many contacts with different orientations. Again, using Penalty, it might only create some numerical friction but, using the Lagrange multiplier resolution, this can lead to contradictory constraints (worsening the convergence).



Usage
-----

The MinProximityIntersection must be placed right after the CollisionPipeline and the associated Detection methods (usually [BruteForceBroadPhase](../../algorithm/bruteforcebroadphase/) and [BVHNarrowPhase](../../algorithm/bvhnarrowphase/)) on top the scene graph.


Additional information
----------------------

- collision models in the scene will have the data **proximity** corresponding to an enlargement of the collision model, i.e., value added to the alarmDistance and the contactDistance and also when building AABBs in the broad phase
- a different alarmDistance and contactDistance can be specified for each CollisionModel by setting alarmDistance and contactDistance to zero and changing the proximity parameter

<!-- automatically generated doc START -->
<!-- generate_doc -->

A set of methods to compute if two primitives are close enough to consider they collide.


__Target__: Sofa.Component.Collision.Detection.Intersection

__namespace__: sofa::component::collision::detection::intersection

__parents__:

- BaseProximityIntersection

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
		<td>alarmDistance</td>
		<td>
Distance above which the intersection computations ignores the proximity pair. This distance can also be used in some broad phase algorithms to reduce the search area
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>contactDistance</td>
		<td>
Distance below which a contact is created
		</td>
		<td>0.5</td>
	</tr>
	<tr>
		<td>useSphereTriangle</td>
		<td>
activate Sphere-Triangle intersection tests
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>usePointPoint</td>
		<td>
activate Point-Point intersection tests
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>useSurfaceNormals</td>
		<td>
Compute the norms of the Detection Outputs by considering the normals of the surfaces involved.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>useLinePoint</td>
		<td>
activate Line-Point intersection tests
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>useLineLine</td>
		<td>
activate Line-Line  intersection tests
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


<!-- automatically generated doc END -->
