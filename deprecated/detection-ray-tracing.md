Collisions Detection: Ray tracing
=================================

The RayTraceDetection component belongs to the category of [Collision Detection](../../simulation-principles/collision/#collision-detection). This method traces a ray for each point in one object following the opposite of the point's normal up to find a triangle in the other object. Both triangles are tested to evaluate if they are in a colliding state. 

It **must be used with a TriangleOctreeModel**, as an octree is used to traverse the object.

### Preliminary phase

Before starting the broad phase, two steps are therefore required before the brute force detection starts:

- all present collision models in the scene must be listed. This is done in the function ```void PipelineImpl::computeCollisionDetection()```  with:
```cpp
root->getTreeObjects<CollisionModel> (&collisionModels);
```
- RayTraceDetection does not create a BVH but an Octree. This specific collision model is using a triangular mesh and maps it to an Octree with CubeModels. This is done by each TriangleOctreeModel in the scene in the function: 
```cpp
computeBoundingTree(maxDepth=0);
```

### Broad phase

The hierarchy is browsed, and the intersection between pairs of CubeModels is tested (using the [intersection method](../../simulation-principles/collision/#intersection-methods) in the scene). If a collision is detected, the models are adding in the ```cmPair``` vector, containing potentially colliding pairs. This is done in the ```addCollisionModel()``` function. The detection between bounding volumes (CubeModel) is performed using [intersection method](../../simulation-principles/collision/#intersection-methods) defined in the scene.


### Narrow phase

The CollisionModel at the lowest level is saved, in this case it must be a TriangleOctreeModel. If the octree would not be constructed already, build it. Then, rays are traced against the TriangleOctreeModel. Distances computed with the ray indicates if a collision occurs between the pair of TriangleOctreeModels. Finally, the DetectionOutput vector containing elements of TriangleOctreeModels in collision is returned, as well as the contact points on the triangle of each model.



Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/collision/RayTraceDetection.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/collision/RayTraceDetection.png?raw=true" title="Flow diagram for the broad & narrow phase of the RayTraceDetection"/></a>
