Narrow Phase: Direct SAP Narrow Phase
=====================================

_DirectSAPNarrowPhase_ is a [narrow phase component](10_NarrowPhase.md), which is used in a [collision pipeline](https://www.sofa-framework.org/community/doc/using-sofa/components/collisions/pipelines/collisionpipeline).
The algorithm is based on the "[Sweep and Prune](https://en.wikipedia.org/wiki/Sweep_and_prune)" algorithm, noted SAP.

The Algorithm
=============

As mentioned in [Narrow Phase](20_BVHNarrowPhase.md), _DirectSAPNarrowPhase_ input is a list of pairs of [collision models](../40_CollisionModels/80_CollisionModels.md).
Among this list, if it is the first time that a [collision model](../40_CollisionModels/80_CollisionModels.md) is provided to _DirectSAPNarrowPhase_, a list of Axis-Aligned Bounding Box (AABB) is created.
Each associated to a collision element of the new [collision model](../40_CollisionModels/80_CollisionModels.md).
This list is saved from a time step to the next.

In the second step, all the AABB are updated according to the geometry of the collision elements in the current time step.
The size of the AABB takes into account the alarm distance defined in the intersection method.

Then, the boxes end points are sorted, according to their position projected on the axis of the greatest variance.

Finally, the sorted end points are processed.
A list of active end points is used.
If an end point corresponds to the begining of an AABB, it is added to the active list.
If an end point corresponds to the end of an AABB, it is removed from the active list.
For each end point, it is tested against the active list.

Direct vs Inc.
--------------

_DirectSAPNarrowPhase_ corresponds to the implementation of SAP in its "direct" version, i.e. at each step it sorts all the primitives along an axis (**not checking the moving ones**) and computes overlaping pairs without saving it.
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
<DefaultContactManager name="Response" response="FrictionContact" />
```