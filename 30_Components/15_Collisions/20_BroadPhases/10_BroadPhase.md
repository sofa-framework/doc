Broad Phase Components
======================

The broad phase collision detection components are executed in a [collision pipeline](https://www.sofa-framework.org/community/doc/using-sofa/components/collisions/pipelines/collisionpipeline).

Introduction
============

In SOFA, collision detection usually involves complex meshes (e.g. a set of triangles).
For an accurate collision response, the collision detection detects which pairs of collision elements are in intersection.

The naive approach would be to test every pair of collision elements.
The number of tests depends on the number of objects, and the number of collision elements in each object.
For performances reasons, this approach is never selected because of its quadratic complexity.

Instead, the collision detection will be divided in two parts:
1. The broad phase collision detection
2. The [narrow phase collision detection](https://www.sofa-framework.org/community/doc/using-sofa/components/collisions/narrowphases/narrowphase)

The Broad Phase
===============

In SOFA, the role of the broad phase is usually to prune a maximum number of pairs of collision models which are not in intersection.
Considering <img class="latex" src="https://latex.codecogs.com/png.latex?n" title="Number of objects" /> collision models (usually there are more than one collision model per object), there are between <img class="latex" src="https://latex.codecogs.com/png.latex?n*(n-1)/2" title="Complexity of pairwise checks" />(no self collision) and <img class="latex" src="https://latex.codecogs.com/png.latex?n^2/2" title="Complexity of pairwise checks" />(if all collision models can self collide) pairs of collision models.

The output of the broad phase is a collection of pairs of collision models which are potentially in intersection.
At this stage, it is not known if those pairs are actually in intersection or not.
It is not known which collision elements (i.e. point/line/triangle) are in intersection with which collision elements.
The list of pairs is provided as an input to the narrow phase collision detection.

The Implementation
------------------

Before starting the broad phase, all collision models in the scene must be listed. This is done in the function ```void PipelineImpl::computeCollisionDetection()```  with:
```cpp
std::vector<CollisionModel*> collisionModels;
root->getTreeObjects<CollisionModel> (&collisionModels);
```

Then, the broad phase collision detection is executed in 3 functions:

```cpp
void BroadPhaseDetection::beginBroadPhase()
```

```cpp
void BroadPhaseDetection::addCollisionModels(const sofa::helper::vector<core::CollisionModel *>& v)
```

```cpp
void BroadPhaseDetection::endBroadPhase()
```

The function `addCollisionModels` is called on the list of all collision models in the scene.
Internally, this function is just a loop calling the following function:
```cpp
void BroadPhaseDetection::addCollisionModel(core::CollisionModel *cm)
```

The implementation of these 3 functions (`beginBroadPhase`, `addCollisionModel` and `endBroadPhase`) defines the behavior of the broad phase.
It is where the algorithm is implemented.
To implement a new broad phase algorithm, a developer will probably derive a class from `BroadPhaseDetection` and override the 3 mentioned functions.

After the execution of the broad phase, the list of potential colliding pairs is stored in
```cpp
sofa::helper::vector< CollisionModelPair > BroadPhaseDetection::cmPairs;
```
Finally, the [collision pipeline](https://www.sofa-framework.org/community/doc/using-sofa/components/collisions/pipelines/collisionpipeline) provides this list to a [narrow phase collision detection](https://www.sofa-framework.org/community/doc/using-sofa/components/collisions/narrowphases/narrowphase).

Examples of Components
======================

The following components are all broad phase collision detections, and can be placed in a simulation scene:

- [BruteForceBroadPhase](https://www.sofa-framework.org/community/doc/using-sofa/components/collisions/broadphases/bruteforcebroadphase)
- ParallelBruteForceBroadPhase (plugin MultiThreading)
- BruteForceDetection
- THMPGSpatialHashing (plugin THMPGSpatialHashing)
- BulletCollisionDetection (plugin BulletCollisionDetection)

Inheritance Diagram
===================

<a href="https://www.sofa-framework.org/api/master/sofa/html/classsofa_1_1core_1_1collision_1_1_broad_phase_detection.html">
<img src="https://www.sofa-framework.org/api/master/sofa/html/classsofa_1_1core_1_1collision_1_1_broad_phase_detection__inherit__graph.png" title="BroadPhaseDetection diagram class"/>
</a>

Read more on [SOFA API documentation](https://www.sofa-framework.org/api/master/sofa/html/classsofa_1_1core_1_1collision_1_1_broad_phase_detection.html)