Collisions
==========

In all SOFA simulations, i.e. using any [animation loop](https://www.sofa-framework.org/community/doc/main-principles/animationloop-and-visitors/), the collision phase is done separately from the physics simulation, and usually before the call to the solvers.

Collision detection is split in several phases, each implemented in a different component, and organized using a collision pipeline component.


Collision pipeline
------------------

The collision pipeline follows two steps:
  1. a collision detection
  2. a collision response

In _PipelineImpl.h_ you can find the three associated functions:
``` cpp
/// Remove collision response from last step
virtual void computeCollisionReset();
/// Detect new collisions. Note that this step must not modify the simulation graph
virtual void computeCollisionDetection();
/// Add collision response in the simulation graph
virtual void computeCollisionResponse();
```

Collision detection
-------------------

The collision detection is usually divided into two detection steps:
  - a broad phase
  - a narrow phase


**Broad phase**

The broad phase uses the bounding boxes of each object with a collision model and checks whether these boxes collide or not. Inaccurate but efficient, this first step allows to quickly detect a supposed collision. As output, the broad phase returns pairs of colliding bounding boxes. Among the broad phase


**Narrow phase**

The narrow phase of detection can rely on different intersection methods that use collision models to detect a contact.Note that different collision models are available to detect a contact:
  - using primitives: point, line, triangle, sphere, cube, cylinder or oriented bounding boxes (OBB)
  - using distance grid, associated to each object in the scene
  - using ray casting: that send rays in the volume of simulation to compute a volume of intersection

The different intersection methods available in SOFA are:
  - DiscreteIntersection : contact created when collision elements are intersecting, not fitted to surfacic collision models
  - MinProximityIntersection : contact created when collision elements are close to each other, optimized for meshes
  - NewProximityIntersection : contact created when collision elements are close to each other, not optimized for meshes
  - RayDiscreteIntersection : dedicated to ray casting method
 
As output, the narrow phase returns pairs of geometric primitives with the corresponding collision points.


Collision response
------------------

The colliding models returned by the narrow phase are finally given to the contact manager, which creates contact interactions of various types based on customizable rules. You can specify which one you want to use in the DefaultContactManager. Repulsion has been implemented based on penalties or on constraints using Lagrange multipliers, and is processed by the solvers together with the other forces and constraints.

When stiff contact penalties or contact constraints are created by the contact manager, an optional GroupManager component is used to create interaction groups handled by a common solver. When contacts disappear, interaction groups can be split to keep them as small as possible. The scenegraph structure thus changes along with the interaction groups.


Collision group
---------------

Just as a notice, it is possible to create group of contact, create integration groups. Given a set of contacts, the CollisionGroupManager allows this. Contacts between models define a graph: by creating contact groups, the collision resolution will process each graph (i.e. collision group) separately.