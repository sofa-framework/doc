---
title: DefaultPipeline
---

Collision Pipelines: DefaultPipeline
==============================================

The DefaultPipeline is a [Collision Pipeline](./collisionpipeline).
It performs steps related to the collision, mainly collision detection and collision response.

The [animation loop](../../../../simulation-principles/animation-loop/) executes the 3 steps of the pipeline (see documentation on [Collision Pipeline](./collisionpipeline)).

Interaction with Other Components
=================================

_DefaultPipeline_ requires other components defined in the same context:

- An intersection method (e.g. MinProximityIntersection, LocalMinDistance)
- A broad phase detection (e.g. [_BruteForceBroadPhase_](./bruteforcebroadphase))
- A narrow phase detection (e.g. [_BVHNarrowPhase_](./bvhnarrowphase))
- A contact manager (e.g. DefaultContactManager)
- [optional] A group manager (e.g. [_DefaultCollisionGroupManager_](../../collisiongroupmanagers/collisiongroupmanager))

If no intersection method is provided, a default _DiscreteIntersection_ component is created and added to the scene graph, with a warning to the user, and used as the intersection method.

Pipeline
========

Here is a description of the 3 steps of the pipeline:

Collision Reset
---------------

This step mainly clears data computed from the previous time step.
It is implemented in the function
```cpp
void DefaultPipeline::doCollisionReset()
```

1. All the contacts provided by the contact manager are cleared.
2. The group manager clears its groups

Collision Detection
-------------------

1. For all collision models, computes its bounding tree. The depth of the tree is defined by a Data in DefaultPipeline. If the broad phase or the narrow phase does not require a deep tree (`needsDeepBoundingTree()`), the tree is minimal. In any case, a CubeCollisionModel is created and linked to each collision model, to be used as a Axis-Aligned Bounding Box in the broad phase. Building the tree takes into account whether the collision detection is continuous or not. This is defined in the intersection method.
2. Executes the broad phase collision detection
3. Executes the narrow phase collision detection

Collision detection is implemented in the following function
```cpp
void DefaultPipeline::doCollisionDetection()
```

Collision Response
------------------

1. Create contacts in the contact manager, based on the result of the collision detection
2. Create response for all pairs of intersecting collision models, which one is not simulated
3. Create response for the rest of the pairs of intersecting collision models (the ones which are simulated). This step can be performed by the group manager if any.

Creation of the response depends on the type of contact defined in the contact manager.

Collision response is implemented in the following function
```cpp
void DefaultPipeline::doCollisionResponse(const helper::vector<core::CollisionModel*>& collisionModels)
```

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

Note [DefaultPipeline](https://www.sofa-framework.org/api/master/sofa/html/classsofa_1_1component_1_1collision_1_1_default_pipeline.html) is defined alongside other required components.

Inheritance Diagram
===================

<a href="https://www.sofa-framework.org/api/master/sofa/html/classsofa_1_1component_1_1collision_1_1_default_pipeline.html">
<img src="https://www.sofa-framework.org/api/master/sofa/html/classsofa_1_1component_1_1collision_1_1_default_pipeline__inherit__graph.png" title="Steps of the collision in SOFA"/>
</a>

Read more on [SOFA API documentation](https://www.sofa-framework.org/api/master/sofa/html/classsofa_1_1component_1_1collision_1_1_default_pipeline.html)
