Collisions Detection: IncrSAP
=============================

The IncrSAP component belongs to the category of [Collision Detection](../../../../../simulation-principles/multi-model-representation/collision/#collision-detection). In this section, we describe the two collision detection methods based on the "[Sweep and Prune](https://en.wikipedia.org/wiki/Sweep_and_prune)" algorithm, noted SAP. The SAP method belongs to the topological methods for broad phase, based on the positions of objects in relation to others.

<a href="https://github.com/sofa-framework/doc/blob/master/images/collision/SAP.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/collision/SAP.png?raw=true" title="SAP algorithm on x- and y-axis with a non-overlapping condition (left) and an overlapping one (right). Image from paper: Collision Detection: Broad Phase Adaptation from Multi-Core to Multi-GPU Architecture"/></a>

IncrSAP corresponds to the implementation of SAP in an incremental manner, i.e. collision primitives are stored and updated which should speed up the collision detection compared to the [DirectSAPNarrowPhase](./../directsapnarrowphase/).

### Preliminary phase

Before starting the broad phase, two steps are therefore required before the brute force detection starts:

- all present collision models in the scene must be listed. This is done in the function ```void PipelineImpl::computeCollisionDetection()```  with:
```cpp
root->getTreeObjects<CollisionModel> (&collisionModels);
```
- from the collision, Axis-Aligned-Bounding-Box (AABB, i.e. CubeModel) will be computed without needing a deep bounding tree (depth level = 1). This is done by each CollisionModel in the scene in the function:
```cpp
computeBoundingTree(used_depth);
```


### Broad phase

It is one of the most used methods in the broad-phase algorithms because it provides an efficient and quick pairs removal (two objects too far one to the other is deleted) and it does not depend on the objects complexity. The sequential algorithm of SAP takes in input the overall objects of the environment and feeds in output a collided objects pairs list. The algorithm is divided in two principal parts:

- the first one is in charge of the bounding volume update of each active virtual objects. In SOFA, these bounding volume are defined in ISAPBoxes which are simple bounding boxes. It contains a Cube which contains only one final CollisionElement and pointers to min and max EndPoints along the three dimensions. min and max end points are respectively min and max coordinates of the cube on a coordinate axis. The between end points (\_min, \_max) and the field cube is that cube is always updated whereas \_min and \_max are stored values of the cube end points at previous time step.
- the second part is in charge of the detection of overlapping between objects. To do that a projection of higher and upper bounds on the three axis of coordinates (x, y and z) of each
AABBs is made. 

Only the pairs of objects whose projected bounding volumes overlap on all axes will be saved in the set of active boxes to be considered for the narrow phase. Unlike like the [DirectSAPNarrowPhase](./../directsapnarrowphase/) which starts from scratch at each time step, the IncrSAP updates internal structures: this is the **IncrSAP** and should therefore be fore efficient.



### Narrow phase

The narrow phase browses all boxes considered as active by the broad phase. From this information, it is possible to recover the finest CollisionModel (which is not a CubeModel) corresponding to each box. An intersection check will then be done between these pairs. This check also depends on the [intersection method](../../../../../simulation-principles/multi-model-representation/collision/#intersection-methods) used. This last phase returns the DetectionOutput vector containing elements of CollisionModels in collision and the contact points on the surface of each model.



Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/collision/IncrSAP.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/collision/IncrSAP.png?raw=true" title="Flow diagram for the broad & narrow phase of the IncrSAP"/></a>