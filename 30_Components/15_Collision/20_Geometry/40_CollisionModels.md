Collision Models
================

SOFA implements a series of collision primitives called CollisionModel. A CollisionModel contains a list of same-type elements. It can be part of a list of CollisionModels or a hierarchy. Here is a list of them:

- [pointcollisionmodel](./../PointCollisionModel)
- [linecollisionmodel](./../LineCollisionModel)
- [trianglecollisionmodel](./../TriangleCollisionModel)
- [spherecollisionmodel](./../SphereCollisionModel)
- [cylindercollisionmodel](./../CylinderCollisionModel)
- [cubecollisionmodel](./../CubeCollisionModel)
- [raycollisionmodel](./../RayCollisionModel)

See the detailed description of the [CollisionModel class](https://www.sofa-framework.org/api/master/sofa/html/classsofa_1_1core_1_1_collision_model.html).

Note that the data **contactStiffness** is only taken into account in the case you are using a collision response using the [Penalty method](../../../../simulation-principles/multi-model-representation/collision/#collision-response).



Usage
-----

To use a CollisionModel, you must first make sure that the collision node in which the CollisionModel is defined does contain the associated topology (e.g. TriangleSetTopologyContainer if you want to use the TriangleCollisionModel).

Moreover, the collision model is usually mapped to a node containing the mechanical representation of the object. The collision node should therefore include a mapping.

