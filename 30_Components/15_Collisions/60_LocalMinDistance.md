LocalMinDistance
================

This proximity method is an [intersection detection](https://www.sofa-framework.org/community/doc/simulation-principles/multi-model-representation/collision/#narrow-phase-detect-intersection) close to the previous [MinProximityIntersection](https://www.sofa-framework.org/community/doc/components/collision/minproximityintersection/) but in addition, it filters the list of DetectionOutput to keep only the contacts with the local minimal distance.

To find an optimal number of contact points, the LocalMinDistance computes cones on all nodes of the collision model. A cone is the combination of the orthogonal directions/planes of the neighboring lines/surfaces.


<a href="https://github.com/sofa-framework/doc/blob/master/images/collision/LocalMinDistance-cones.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/collision/LocalMinDistance-cones.png?raw=true" title="Cones computation using LocalMinDistance" style="width: 70%;"/></a>

All contact outputs which are outside these cones will be invalidated (even if they are below the contactDistance). Thus, only the geometrically closest contacts remain: for convex surfaces, this method even ensures to find one and only one contact point.

<a href="https://github.com/sofa-framework/doc/blob/master/images/collision/LocalMinDistance-detection.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/collision/LocalMinDistance-detection.png?raw=true" title="Proximity detection using LocalMinDistance" style="width: 70%;"/></a>

Degenerated cases can occur when, for instance, surfaces are perfectly parallel. If we think about configuration described below:

The cones on the sides (no 1 and 3) are open with an 90 degree angle, while the middle cone (2) is closed. No contact will therefore be detected from the cone 2.


<a href="https://github.com/sofa-framework/doc/blob/master/images/collision/LocalMinDistance-degenerated.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/collision/LocalMinDistance-degenerated.png?raw=true" title="Degenerated case" style="width: 70%;"/></a>

- In case our object is rigid, having the two cones exactly equal to 90 degrees may lead to instabilities: a small rotation would lead to the invalidation of one of the two corner contacts, and the object would start to oscillate. To prevent such cases, a data is available to open the cone: "coneFactor"
- In case of a soft body, the LocalMinDistance would not detect the middle point as a contact since the cone is closed. The method would therefore fail to keep the object over the surface. To solve such a generated case, a data aiming at opening all existing cones is defined: "coneAngle"


Data
----

The intersection methods include the following data:

-   **alarmDistance**: maximum distance between collision elements for wich a contact is created
-   **contactDistance** : parameter used in the contact creation


Usage
-----

The MinProximityIntersection must be placed right after the CollisionPipeline and the associated Detection method (usually [BruteForce](https://www.sofa-framework.org/community/doc/components/collisions/detection-brute-force/)) on top the scene graph.


Additional information
----------------------

- collision models in the scene will have the data **proximity** corresponding to an enlargement of the collision model, i.e., value added to the alarmDistance and the contactDistance and also when building AABBs in the broad phase
- a different alarmDistance and contactDistance can be specified for each CollisionModel by setting alarmDistance and contactDistance to zero and changing the proximity parameter



Example
-------

This component is used as follows in XML format:

``` xml
<LocalMinDistance name="LMD-proximity" alarmDistance="0.5" contactDistance="0.3" angleCone="0.0" />
```

or using SofaPython3:

``` python
node.addObject('LocalMinDistance', name='LMD-proximity', alarmDistance='.5', contactDistance='.3', angleCone='0.0')
```

An example scene involving a LocalMinDistance is available in [*examples/Components/constraint/FrictionContact.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/constraint/FrictionContact.scn)