Broad Phase: Brute Force Broad Phase
====================================

BruteForceBroadPhase is a [broad phase component](10_BroadPhase.md), which is used in a [Collision Detection](https://www.sofa-framework.org/community/doc/main-principles/collision/#collision-detection) pipeline.

The method is based on the comparison of the overall [bounding volumes](https://en.wikipedia.org/wiki/Bounding_volume) of objects to determine if they are in collision or not.
This test is very exhaustive because of its <img class="latex" src="https://latex.codecogs.com/png.latex?n^2/2" title="Complexity of pairwise checks" /> pairwise checks.
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
<DefaultContactManager name="Response" response="FrictionContact" />
```