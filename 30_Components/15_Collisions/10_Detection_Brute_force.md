Collisions Detection: Brute force
=================================

The BruteForceDetection component belongs to the category of [Collision Detection](https://www.sofa-framework.org/community/doc/main-principles/collision/#collision-detection). This method is based on the comparison of the overall [bounding volumes](https://en.wikipedia.org/wiki/Bounding_volume) of objects to determine if they are in collision or not. This test is very exhaustive because of its <img class="latex" src="https://latex.codecogs.com/png.latex?n^2" title="Complexity of pairwise checks" /> pairwise checks. In SOFA, the proposed bounding volumes are commonly Axis-Aligned-Bounding-Box (AABB).

In order to reduce the number of tests to perform, these bounding volumes are arranged as a Bounding Volume Hierarchy (BVH), in our case a hierarchy of AABB. This common strategy highly improves performances. Deformable objects can be challenging for BVH because hierarchy structures must be updated when an object deforms itself.

### Preliminary phase

Before starting the broad phase, two steps are therefore required before the brute force detection starts:

- all present collision models in the scene must be listed. This is done in the function ```void PipelineImpl::computeCollisionDetection()```  with:
```cpp
root->getTreeObjects<CollisionModel> (&collisionModels);
```
- the BVH must be created, where _used_depth_ is the needed depth level for the hierarchy. This is done by each CollisionModel in the scene in the function: 
```cpp
computeBoundingTree(used_depth);
```

### Broad phase

Once the BVH is created, the broad phase is ready to go. The hierarchy is browsed and the intersection between pairs of AABB is tested (using the [intersection method](https://www.sofa-framework.org/community/doc/main-principles/collisions/#intersection-methods) in the scene). In case the bounding volumes are detected as in collision, the algorithms either goes deeper in the hierarchy or adds the pair of collision models (AABB) in the ```cmPair``` vector if the bounding box is the last in the hierarchy, containing potentially colliding pairs. This is done in the ```addCollisionModel()``` function. The detection betweem bounding volumes (CubeModel) is performed using [intersection method](https://www.sofa-framework.org/community/doc/main-principles/collisions/#intersection-methods) defined in the scene.



### Narrow phase

Then, the narrow phase starts by clearing the DetectionOutputMap containing the CollisionModels in collision and getting the ```cmPair``` vector resulting from the broad phase. From this vector containing the pairs of CollisionModels, the method looks for the finnest CollisionModel (which is not a CubeModel). An intersection check will then be done between these pairs. This check also depends on the [intersection method](https://www.sofa-framework.org/community/doc/main-principles/collisions/#intersection-methods) used. This last phase returns the DetectionOutput vector containing elements of CollisionModels in collision and the contact points on the surface of each model.



Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/collision/BruteForceDetection.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/collision/BruteForceDetection.png?raw=true" title="Flow diagram for the broad & narrow phase of the BruteForceDetection"/></a>
