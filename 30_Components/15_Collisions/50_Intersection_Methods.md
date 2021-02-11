Collisions Detection: Narrow Phase
==================================

This phase computes a set of contact points, given a set of potentially colliding pairs of models.


The different intersection methods available in SOFA are:

- **DiscreteIntersection** (BaseProximityIntersection : DiscreteIntersection): contact created when collision elements are intersecting, not fitted to surfacic collision models.

- **MinProximityIntersection**: contact created when collision elements are close to each other, optimized for mesh intersections. The intersection is implemented for the following primitives: Triangle/Point, Line/Point, Line/Line, so that it covers all Triangle/Triangle intersections. To get a proper detection, the TriangleModel, LineModel and PointModel must be simultaneaously used in the scene.

- **NewProximityIntersection**: contact created when collision elements are close to each other, not optimized for meshes. The intersection computation is done between all pairs of collision primitives. This method is not as well optimized for meshes, as MinProximityIntersection, to not duplicate contacts, each edge has its owner triangle, so when computing an intersection between two triangles, if one find a contact on an edge of the first triangle, if this edge does not belong to this triangle, the result will be false. It is the same for points.
you must use only one CollisionModel among TriangleModel, LineModel, PointModel for a single object


- **MeshNewProximityIntersection**
- **LocalMinDistance**
- **FFDDistanceGridDiscreteIntersection**: compute the intersection based on distance grids
- **RigidDistanceGridDiscreteIntersection**: compute distance grids between rigid objects
- **RayNewProximityIntersection**
- **RayDiscreteIntersection**: dedicated to ray casting method


More information on these intersection methods will come soon.



Data
----

The intersection methods include the following data:

-   **alarmDistance**: maximum distance between collision elements for wich a contact is created
-   **contactDistance** : parameter used in the contact creation


Additional information:

- collision models in the scene will have the data **proximity** corresponding to an enlargement of the collision model, i.e., value added to the alarmDistance and the contactDistance and also when building AABBs in the broad phase
- a different alarmDistance and contactDistance can be specified for each CollisionModel by setting alarmDistance and contactDistance to zero and changing the proximity parameter