MinProximityIntersection
========================

This proximity method for [intersection detection](../../../../../simulation-principles/multi-model-representation/collision/#narrow-phase-detect-intersection):

- detects a possible contact as soon as pair of collision elements are close to each other (distance smaller than the alarmDistance)
- and creates contact (aka DetectionOutput) when the distance is lower than contactDistance.

This method is optimized for meshes. The intersection is implemented for the following primitives: Triangle/Point, Line/Point, Line/Line, so that it covers all Triangle/Triangle intersections. To get a proper detection, the TriangleModel, LineModel and PointModel must be simultaneously used in the scene.

In the figure below, we describe the detection of the contacts for Object 1 due to an Object 2. It assumes here that a PointCollisionModel and a LineCollisionModel are defined. The detection gives:
- 2 Point-Point contacts (yellow)
- 1 Point-Line contact (blue)
- 1 Line-Line contact (pink)


<a href="https://github.com/sofa-framework/doc/blob/master/images/collision/MinProximityIntersection.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/collision/MinProximityIntersection.png?raw=true" title="Proximity detection using MinProximityIntersection" style="width: 70%;"/></a>

Although the method is working properly, the intersection might result in a high number of contacts. This works just fine for Penalty method (many springs will be generated). However, using a response method based on Lagrange multipliers, many constraints will be generated which might rapidly become computationally-demanding.

Moreover, the contacts can be a bit degenerated: many contacts with different orientations. Again, using Penalty, it might only create some numerical friction but, using the Lagrange multiplier resolution, this can lead to contradictory constraints (worsening the convergence).



Usage
-----

The MinProximityIntersection must be placed right after the CollisionPipeline and the associated Detection methods (usually [BruteForceBroadPhase](../../algorithm/bruteforcebroadphase/) and [BVHNarrowPhase](../../algorithm/bvhnarrowphase/)) on top the scene graph.


Additional information
----------------------

- collision models in the scene will have the data **proximity** corresponding to an enlargement of the collision model, i.e., value added to the alarmDistance and the contactDistance and also when building AABBs in the broad phase
- a different alarmDistance and contactDistance can be specified for each CollisionModel by setting alarmDistance and contactDistance to zero and changing the proximity parameter

