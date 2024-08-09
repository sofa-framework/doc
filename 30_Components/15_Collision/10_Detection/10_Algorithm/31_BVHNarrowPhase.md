Narrow Phase: BVH Narrow Phase
==============================

BVHNarrowPhase is [narrow phase component](./../narrowphase), which is used in the detection phase of a [CollisionPipeline](../../collisionpipeline/#collision-detection).
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
```