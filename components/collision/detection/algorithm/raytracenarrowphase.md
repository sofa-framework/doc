---
title: RayTraceNarrowPhase
---

Narrow Phase: Ray Trace Narrow Phase
====================================

The RayTraceNarrowPhase component is a [narrow phase component](./../narrowphase), which is used in the detection phase of a [CollisionPipeline](../../collisionpipeline/#collision-detection).
This method traces a ray for each point in one object following the opposite of the point's normal up to find a triangle in the other object.
Both triangles are tested to evaluate if they are in a colliding state.

It **must be used with a TriangleOctreeModel**, as an octree is used to traverse the object.

The Algorithm
=============

The CollisionModel at the lowest level is saved, in this case it must be a TriangleOctreeModel. If the octree would not be constructed already, build it. Then, rays are traced against the TriangleOctreeModel. Distances computed with the ray indicates if a collision occurs between the pair of TriangleOctreeModels. Finally, the DetectionOutput vector containing elements of TriangleOctreeModels in collision is returned, as well as the contact points on the triangle of each model.

Example of Usage
================

This component can be used as follows in XML format:

```xml
<FreeMotionAnimationLoop />
<DefaultPipeline depth="15" verbose="0" draw="0" />
<BruteForceBroadPhase name="N2" />
<RayTraceNarrowPhase/>
<MinProximityIntersection name="Proximity" alarmDistance="1.5" contactDistance="1" />
<DefaultContactManager name="Response" response="FrictionContactConstraint" />
```

Colliding objects must have a TriangleOctreeModel:

```xml
<TriangleOctreeModel/>
```<!-- automatically generated doc START -->
<!-- generate_doc -->

Narrow phase of the collision detection using TriangleOctreeModel


__Target__: Sofa.Component.Collision.Detection.Algorithm

__namespace__: sofa::component::collision::detection::algorithm

__parents__:

- NarrowPhaseDetection

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

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|


<!-- automatically generated doc END -->
