---
title: DirectSAPNarrowPhase
---

Narrow Phase: Direct SAP Narrow Phase
=====================================

_DirectSAPNarrowPhase_ is a [narrow phase component](./narrowphase), which is used in the detection phase of a [CollisionPipeline](../collisionpipeline/#collision-detection).
The algorithm is based on the "[Sweep and Prune](https://en.wikipedia.org/wiki/Sweep_and_prune)" algorithm, noted SAP.

The Algorithm
=============

As mentioned in [Narrow Phase](./narrowphase), _DirectSAPNarrowPhase_ input is a list of pairs of [collision models](../../../geometry/collisionmodels/).
Among this list, if it is the first time that a [collision model](../../../geometry/collisionmodels/) is provided to _DirectSAPNarrowPhase_, a list of Axis-Aligned Bounding Box (AABB) is created.
Each associated to a collision element of the new [collision model](../../../geometry/collisionmodels/).
This list is saved from a time step to the next.

In the second step, all the AABB are updated according to the geometry of the collision elements in the current time step.
The size of the AABB takes into account the alarm distance defined in the intersection method.

Then, the boxes end points are sorted, according to their position projected on the axis of the greatest variance.

Finally, the sorted end points are processed.
A list of active end points is used.
If an end point corresponds to the beginning of an AABB, it is added to the active list.
If an end point corresponds to the end of an AABB, it is removed from the active list.
For each end point, it is tested against the active list.

Direct vs Inc.
--------------

_DirectSAPNarrowPhase_ corresponds to the implementation of SAP in its "direct" version, i.e. at each step it sorts all the primitives along an axis (**not checking the moving ones**) and computes overlapping pairs without saving it.
But the memory used to save these primitives is created just once, the first time CollisionModels are added.

Example of Usage
================

This component is used as follows in XML format:

```xml
<FreeMotionAnimationLoop />
<DefaultPipeline depth="15" verbose="0" draw="0" />
<BruteForceBroadPhase name="N2" />
<DirectSAPNarrowPhase/>
<MinProximityIntersection name="Proximity" alarmDistance="1.5" contactDistance="1" />
<DefaultContactManager name="Response" response="FrictionContactConstraint" />
```<!-- automatically generated doc START -->
<!-- generate_doc -->

Collision detection using sweep and prune


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
		<td>nbPairs</td>
		<td>
number of pairs of elements sent to narrow phase
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showOnlyInvestigatedBoxes</td>
		<td>
Show only boxes which will be sent to narrow phase
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
