---
title: BruteForceBroadPhase
---

Broad Phase: Brute Force Broad Phase
====================================

BruteForceBroadPhase is a [broad phase component](./broadphase), which is used in a [Collision Detection](../collisionpipeline/#collision-detection) pipeline.

The method is based on the comparison of the overall [bounding volumes](https://en.wikipedia.org/wiki/Bounding_volume) of objects to determine if they are in collision or not.
This test is very exhaustive because of its $$n^2/2$$ pairwise checks.
In SOFA, the proposed bounding volumes are commonly Axis-Aligned-Bounding-Box (AABB).

Since, the bounding volumes are very simple (AABB), the tests are very fast for a few collision models.
A more advanced method must be selected for simulations involving a high number of objects.

A parallel implementation (_ParallelBruteForceBroadPhase_) can be found in the plugin MultiThreading.

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
<!-- generate_doc -->

Broad phase collision detection using extensive pair-wise tests


__Target__: Sofa.Component.Collision.Detection.Algorithm

__namespace__: sofa::component::collision::detection::algorithm

__parents__:

- BroadPhaseDetection

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
		<td>box</td>
		<td>
if not empty, objects that do not intersect this bounding-box will be ignored
		</td>
		<td></td>
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
