Collisions
==========

In all SOFA simulations, i.e. using any [animation loop](https://www.sofa-framework.org/community/doc/main-principles/animationloop-and-visitors/), the collision phase is done separately from the physics simulation, and usually before the call to the solvers.

Collision detection is split in several phases, each implemented in a different component. Each phase is scheduled by the collision pipeline.

<a href="https://github.com/sofa-framework/doc/blob/master/images/collision/CollisionSteps.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/collision/CollisionSteps.png?raw=true" title="Steps of the collision in SOFA"/></a>

Collision pipeline
------------------

The collision pipeline follows three steps:

  1. reset of the collision
  2. a collision detection
  3. a collision response

In _PipelineImpl.h_ you can find the three associated functions triggered by the CollisionVisitor:
``` cpp
/// Remove collision response from last step
virtual void computeCollisionReset();
/// Detect new collisions. Note that this step must not modify the simulation graph
virtual void computeCollisionDetection();
/// Add collision response in the simulation graph
virtual void computeCollisionResponse();
```

Each of these functions will call a delegate, available in the Pipeline (see _DefaultPipeline.h_):
``` cpp
/// Remove collision response from last step
void doCollisionReset() override;
/// Detect new collisions. Note that this step must not modify the simulation graph
void doCollisionDetection(const sofa::helper::vector<core::CollisionModel*>& collisionModels) override;
/// Add collision response in the simulation graph
void doCollisionResponse() override;
```


### Sequence Diagram

<a href="https://github.com/sofa-framework/doc/blob/master/images/collision/CollisionVisitor.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/collision/CollisionVisitor.png?raw=true" title="Flow diagram for a CollisionVisitor"/></a>

Let's now focus on the steps performed by the collision pipeline, namely the collision detection and the collision response.





Collision detection
-------------------

Collision detection aims at determining if two (or several) objects collide. In SOFA, the collision detection takes as input the collision models (geometric data) and returns pairs of geometric primitives as output, along with the associated contact points. This contact information is passed to the contact manager , which creates contact interactions of various types based on customizable rules.

Given <img class="latex" src="https://latex.codecogs.com/png.latex?n" title="Number of objects" /> moving objects in a virtual environment, testing all objects pairs tend to perform <img class="latex" src="https://latex.codecogs.com/png.latex?n^2" title="Complexity of pairwise checks" /> pairwise checks. When <img class="latex" src="https://latex.codecogs.com/png.latex?%5Cmathcal%7BO%7D%20%28%20n%5E2%29" title="Asymptotic complexity" /> complexity, the collision detection is usually divided into two successive steps triggered within the ```doCollisionDetection()``` function:

- a broad phase
- a narrow phase


Several collision detection methods are available in SOFA. All of these methods will compute the contact points between collision models. The evaluation of these contacts will be done using Intersection Methods. Here again, various intersection methods are available in SOFA. The choice of the collision detection method and the intersection method depends on your specific simulation use case.
Available collision detection methods are:

- [Brute Force](https://www.sofa-framework.org/community/doc/components/collision/detection-brute-force)
- [Direct Sweep and Prune](https://www.sofa-framework.org/community/doc/components/collision/detection-sweep-and-prune/)
- [Incremental Sweep and Prune](https://www.sofa-framework.org/community/doc/components/collision/detection-sap-incremental/)
- [Ray Tracing](https://www.sofa-framework.org/community/doc/components/collision/detection-ray-tracing)


### Broad phase

The first step of the pipeline is the so-called broad-phase. It aims at quickly and efficiently removing objects pairs that are not in collision.

The broad phase uses a set of root collision models in order to compute potentially colliding pairs. It can for instance rely on the bounding boxes of each object with a collision model, thus efficiently checking whether boxes collide or not. This step does not state if pairs of objects collide, but it detects if they *potentially* collide. As output, the broad phase returns pairs of potentially colliding collision models.


### Narrow phase

The narrow phase of detection can rely on different intersection methods that use collision models to detect a contact.Note that different collision models are available to detect a contact:

  - using primitives: point, line, triangle, sphere, cube, cylinder or oriented bounding boxes (OBB)
  - using distance grid, associated to each object in the scene
  - using ray casting: that send rays in the volume of simulation to compute a volume of intersection


### Intersection methods

All collision detection methods will rely on intersection methods during the broad and/or narrow phase in order to assess if the models do collide. Given 2 collision elements, these intersection methods test if an intersection is possible.
Available intersection methods are:

- [DiscreteIntersection](https://www.sofa-framework.org/community/doc/components/collision/intersection-methods/)
- [MinProximityIntersection](https://www.sofa-framework.org/community/doc/components/collision/intersection-methods/)
- [NewProximityIntersection](https://www.sofa-framework.org/community/doc/components/collision/intersection-methods/)
- [MeshNewProximityIntersection](https://www.sofa-framework.org/community/doc/components/collision/intersection-methods/)
- [LocalMinDistance](https://www.sofa-framework.org/community/doc/components/collision/intersection-methods/)
- [FFDDistanceGridDiscreteIntersection](https://www.sofa-framework.org/community/doc/components/collision/intersection-methods/)
- [RigidDistanceGridDiscreteIntersection](https://www.sofa-framework.org/community/doc/components/collision/intersection-methods/)
- [RayNewProximityIntersection](https://www.sofa-framework.org/community/doc/components/collision/intersection-methods/)
- [RayDiscreteIntersection](https://www.sofa-framework.org/community/doc/components/collision/intersection-methods/)


### Output of the detection

As output, the collision detection (further to the narrow phase) returns pairs of geometric primitives with the corresponding collision points. The collision information is saved in a vector of DetectionOutput. This data structure is a generic description of a contact point, used for most collision models except special cases such as GPU-based collisions.
Each contact point is described by :

- elem: pair of colliding elements.
- id: unique id of the contact for the given pair of collision models. This id is used to filter redundant contacts (only the contact with the smallest distance is kept), and to store persistant data over time for the response.
- point: contact points on the surface of each model.
- normal: normal of the contact, pointing outward from the first model.
- value: signed distance (negative if objects are interpenetrating).
- deltaT: estimated of time of contact.



Collision response
------------------

The step of collision response is triggered within the ```doCollisionResponse()``` function in the CollisionPipeline. The colliding models returned by the narrow phase are finally given to the ContactManager, which creates contact interactions of various types based on customizable rules. You can specify which one you want to use in the DefaultContactManager. Response has been implemented based on:

- the penalty method, efficient but subject to instability if not properly tuned
- the persistent method
- or on constraints using [Lagrange multipliers](https://www.sofa-framework.org/community/doc/simulation-principles/constraint/lagrange-constraint/), and is processed by the solvers together with the other forces and constraints.

When stiff contact penalties or contact constraints are created by the contact manager, an optional GroupManager component is used to create interaction groups handled by a common solver. When contacts disappear, interaction groups can be split to keep them as small as possible. The scenegraph structure thus changes along with the interaction groups.


### Sequence Diagram

<a href="https://github.com/sofa-framework/doc/blob/master/images/collision/CollisionContactManager.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/collision/CollisionContactManager.png?raw=true" title="Flow diagram for a CollisionContactManager"/></a>





Additional information
----------------------

### Collision model data

Each collision model (e.g. TriangleCollisionModel) will inherit three boolean options:

- _active_: true if this CollisionModel should be used for collisions (true by default)
- _moving_: true if the CollisionModel is changing position between time steps (true by default)
- _simulated_: true if the CollisionModel is attached to a simulation. It is false for immobile or procedurally animated objects that don't use contact forces

### Collision group

Just as a notice, it is possible to create group of contact, create integration groups. Given a set of contacts, the CollisionGroupManager allows this. Contacts between models define a graph: by creating contact groups, the collision resolution will process each graph (i.e. collision group) separately.


### Read more

Do not hesitate browse and report interesting articles.
We suggest this paper from Avril et al.: [Collision Detection: Broad Phase Adaptation from Multi-Core to Multi-GPU Architecture](https://hal.archives-ouvertes.fr/hal-01018759/ ) and the [reference SOFA paper](https://hal.inria.fr/hal-00681539/).