Narrow Phase Components
======================

The narrow phase collision detection components are executed in a [collision pipeline](https://www.sofa-framework.org/community/doc/using-sofa/components/collisions/pipelines/collisionpipeline).

Introduction
============

In SOFA, collision detection usually involves complex meshes (e.g. a set of triangles).
For an accurate collision response, the collision detection detects which pairs of collision elements are in intersection.

The naive approach would be to test every pair of collision elements.
The number of tests depends on the number of objects, and the number of collision elements in each object.
For performances reasons, this approach is never selected because of its quadratic complexity.

Instead, the collision detection will be divided in two parts:
1. The [broad phase collision detection](../20_BroadPhases/10_BroadPhase.md)
2. The narrow phase collision detection

The Narrow Phase
================

The narrow phase is executed after the broad phase.
The broad phase output is a list of collision models potentially in collision.
The goal of the narrow phase is to examine the list more closely and determine if they are actually in intersection.
If it is the case, it detects which elements are in intersection.

Following the [DefaultPipeline](../10_Pipelines/20_DefaultPipeline.md), the output of the narrow phase is provided to the contact manager.

The Implementation
------------------

The narrow phase is executed in 3 functions:

```cpp
/// Clear all the potentially colliding pairs detected in the previous simulation step
void NarrowPhaseDetection::beginNarrowPhase()
```

```cpp
/// Add a new list of potentially colliding pairs of models
void NarrowPhaseDetection::addCollisionPairs(const sofa::helper::vector< std::pair<core::CollisionModel*, core::CollisionModel*> >& v)
```

```cpp
void NarrowPhaseDetection::endNarrowPhase()
```

The function `addCollisionPairs` is called on the list of pairs of collision models provided by the broad phase.
Internally, this function is just a loop calling the following function:
```cpp
void NarrowPhaseDetection::addCollisionPair (const std::pair<core::CollisionModel*, core::CollisionModel*>& cmPair)
```

The implementation of these 3 functions (`beginNarrowPhase`, `addCollisionPair` and `endNarrowPhase`) defines the behavior of the narrow phase.
It is where the algorithm is implemented.
To implement a new narrow phase algorithm, a developer will probably derive a class from `NarrowPhaseDetection` and override the 3 mentioned functions.

After the execution of the narrow phase, the list of contact is stored in
```cpp
DetectionOutputMap NarrowPhaseDetection::m_outputsMap;
```

Finally, the collision pipeline provides this list to the contact manager.

Examples of Components
======================

The following components are all narrow phase collision detections, and can be placed in a simulation scene:
- [BVHNarrowPhase](20_BVHNarrowPhase.md)
- ParallelBVHNarrowPhase (plugin MultiThreading)
- DirectSAPNarrowPhase

Inheritance Diagram
===================

<a href="https://www.sofa-framework.org/api/master/sofa/html/classsofa_1_1core_1_1collision_1_1_narrow_phase_detection.html">
<img src="https://www.sofa-framework.org/api/master/sofa/html/classsofa_1_1core_1_1collision_1_1_narrow_phase_detection__inherit__graph.png" title="NarrowPhaseDetection diagram class"/>
</a>

Read more on [SOFA API documentation](https://www.sofa-framework.org/api/master/sofa/html/classsofa_1_1core_1_1collision_1_1_narrow_phase_detection.html)