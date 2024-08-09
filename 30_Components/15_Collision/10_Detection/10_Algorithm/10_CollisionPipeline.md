Collision Pipelines
===================

Collision between objects is split in several phases, each implemented in a different component.
Each phase is scheduled by a collision pipeline.
The collision pipelines are executed in an [animation loop](../../../../../simulation-principles/animation-loop/).

The Steps
=========

The collision pipeline follows three steps:

1. reset of the collision
2. a collision detection
3. a collision response

Implementation
==============

A collision pipeline is called from an [animation loop](../../../../../simulation-principles/animation-loop/) through a CollisionVisitor executing the 3 steps of the pipeline in `CollisionVisitor::processCollisionPipeline`.

The visitor executes the following functions, each corresponding to a step of the pipeline:
```cpp
/// Remove collision response from last step
void Pipeline::computeCollisionReset()
```

```cpp
/// Detect new collisions. Note that this step must not modify the simulation graph
void Pipeline::computeCollisionDetection()
```

```cpp
/// Add collision response in the simulation graph
void Pipeline::computeCollisionResponse()
```

Each of these functions will call a delegate, available in the Pipeline:
``` cpp
/// Remove collision response from last step
void doCollisionReset() override;
```

``` cpp
/// Detect new collisions. Note that this step must not modify the simulation graph
void doCollisionDetection(const sofa::helper::vector<core::CollisionModel*>& collisionModels) override;
```

``` cpp
/// Add collision response in the simulation graph
void doCollisionResponse() override;
```

The 3 delegate functions describe the 3 different steps, and are usually overriden in derived classes.
See an example in [_DefaultPipeline_](./../defaultpipeline).

Notes:
In some cases, the 3 steps are called manually by the animation loop through 3 dedicated visitors ([CollisionResetVisitor](https://www.sofa-framework.org/api/master/sofa/html/classsofa_1_1simulation_1_1_collision_reset_visitor.html), [CollisionDetectionVisitor](https://www.sofa-framework.org/api/master/sofa/html/classsofa_1_1simulation_1_1_collision_detection_visitor.html) and [CollisionResponseVisitor](https://www.sofa-framework.org/api/master/sofa/html/classsofa_1_1simulation_1_1_collision_response_visitor.html)).
Each of these visitors executes only one step (instead of the 3).
This is to avoid race conditions in a multithreaded environment.

Examples of Components
======================

The following components are all collision pipelines, and can be placed in a simulation scene:

- [_DefaultPipeline_](./../defaultpipeline)
