This page presents how to use MinProximityIntersection and
NewProximityIntersection and other IntersectionMethod parameters.

**MinProximityIntersection**
----------------------------

-   optimized for mesh intersections
-   intersection computation for : Triangle/Point, Line/Point,
    Line/Line, so that it covers all Triangle/Triangle intersections
-   you must use simultaneaously in the Sofa scene the TriangleModel,
    LineModel and PointModel

 

**NewProximityIntersection**
----------------------------

-   intersection computation is done between all pairs of collision
    primitives
-   not as well optimized for meshes as MinProximityIntersection, to not
    duplicate contacts, each edge has its owner triangle, so when
    computing an intersection between two triangles, if one find a
    contact on an edge of the first triangle, if this edge does not
    belong to this triangle, the result will be false. It is the same
    for points.
-   you must use only one CollisionModel among TriangleModel, LineModel,
    PointModel for a single object

 

**IntesectionMehtod parameters**
--------------------------------

-   alarmDistance : maximum distance between collision elements for wich
    a contact is created
-   contactDistance : parameter used in the contact creation

 

**CollisionModel parameters**
-----------------------------

-   proximity : enlargement of the collision model, i.e., value added to
    the alarmDistance and the contactDistance and also when building
    AABBs in the broad phase

 

**Trick**
---------

-   you can specify a different alarmDistance and contactDistance for
    each CollisionModel by setting alarmDistance and contactDistance to
    zero and changing the proximity parameter

