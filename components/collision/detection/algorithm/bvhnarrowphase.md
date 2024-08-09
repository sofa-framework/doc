---
title: BVHNarrowPhase
---

Narrow Phase: BVH Narrow Phase
==============================

BVHNarrowPhase is [narrow phase component](./narrowphase), which is used in the detection phase of a [CollisionPipeline](../collisionpipeline/#collision-detection).
The algorithm is based on a Bounding Volume Hierarchy (BVH).


Bounding Volume Hierarchy
=========================

The data structure is built or updated by the collision pipeline before the actual collision detection.
The hierarchy is contained internally into the collision models, through linked collision models and lists of elements (see CollisionModel).

The Algorithm
=============

The algorithm examines a potential collision between a pair of collision models, which has been detected in the broad phase.
This test is time-consuming, this is why it is necessary to have a broad phase which eliminates a maximum number of pairs.
For a pair of collision models, the algorithm traverses the hierarchy of collision elements to rapidly eliminate pairs of elements which are not in intersection.
Finally, the intersection method is called on the remaining pairs of elements.

Note that the algorithm is written in its iterative form, instead of a recursive form.

A parallel implementation (ParallelBVHNarrowPhase) can be found in the plugin MultiThreading.

Example of Usage
================

This component is used as follows in XML format:

```xml
<FreeMotionAnimationLoop />
<DefaultPipeline depth="15" verbose="0" draw="0" />
<BruteForceBroadPhase name="N2" />
<BVHNarrowPhase/>
<MinProximityIntersection name="Proximity" alarmDistance="1.5" contactDistance="1" />
<DefaultContactManager name="Response" response="FrictionContactConstraint" />
```<!-- automatically generated doc START -->
__Target__: `Sofa.Component.Collision.Detection.Algorithm`

__namespace__: `#!c++ sofa::component::collision::detection::algorithm`

__parents__: 

- `#!c++ NarrowPhaseDetection`

__categories__: 

- CollisionAlgorithm

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

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|




<!-- automatically generated doc END -->
