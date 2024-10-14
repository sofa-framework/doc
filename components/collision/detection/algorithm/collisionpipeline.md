---
title: CollisionPipeline
---

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
<!-- automatically generated doc START -->
<!-- generate_doc -->

The default collision detection and modeling pipeline.


__Target__: Sofa.Component.Collision.Detection.Algorithm

__namespace__: sofa::component::collision::detection::algorithm

__parents__:

- Pipeline

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
		<td>verbose</td>
		<td>
Display extra informations at each computation step. (default=false)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>depth</td>
		<td>
Max depth of bounding trees. (default=6, min=?, max=?)
		</td>
		<td>6</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>draw</td>
		<td>
Draw the detected collisions. (default=false)
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