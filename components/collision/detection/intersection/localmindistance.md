---
title: LocalMinDistance
---

LocalMinDistance
================

This proximity method is an [intersection detection](../../../../simulation-principles/multi-model-representation/collision/#narrow-phase-detect-intersection) close to the previous [MinProximityIntersection](./minproximityintersection/) but in addition, it filters the list of DetectionOutput to keep only the contacts with the local minimal distance.

To find an optimal number of contact points, the LocalMinDistance computes cones on all nodes of the collision model. A cone is the combination of the orthogonal directions/planes of the neighboring lines/surfaces.


<a href="https://github.com/sofa-framework/doc/blob/master/images/collision/LocalMinDistance-cones.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/collision/LocalMinDistance-cones.png?raw=true" title="Cones computation using LocalMinDistance" style="width: 70%;"/></a>

All contact outputs which are outside these cones will be invalidated (even if they are below the contactDistance). Thus, only the geometrically closest contacts remain: for convex surfaces, this method even ensures to find one and only one contact point.

<a href="https://github.com/sofa-framework/doc/blob/master/images/collision/LocalMinDistance-detection.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/collision/LocalMinDistance-detection.png?raw=true" title="Proximity detection using LocalMinDistance" style="width: 70%;"/></a>

Degenerated cases can occur when, for instance, surfaces are perfectly parallel. If we think about configuration described below:

The cones on the sides (no 1 and 3) are open with an 90 degree angle, while the middle cone (2) is closed. No contact will therefore be detected from the cone 2.


<a href="https://github.com/sofa-framework/doc/blob/master/images/collision/LocalMinDistance-degenerated.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/collision/LocalMinDistance-degenerated.png?raw=true" title="Degenerated case" style="width: 70%;"/></a>

- In case our object is rigid, having the two cones exactly equal to 90 degrees may lead to instabilities: a small rotation would lead to the invalidation of one of the two corner contacts, and the object would start to oscillate. To prevent such cases, a data is available to open the cone: "coneFactor"
- In case of a soft body, the LocalMinDistance would not detect the middle point as a contact since the cone is closed. The method would therefore fail to keep the object over the surface. To solve such a generated case, a data aiming at opening all existing cones is defined: "angleCone"




Usage
-----

The MinProximityIntersection must be placed right after the CollisionPipeline and the associated Detection method (usually [BruteForce](../algorithm/bruteforcebroadphase/)) on top the scene graph.


Additional information
----------------------

- collision models in the scene will have the data **proximity** corresponding to an enlargement of the collision model, i.e., value added to the alarmDistance and the contactDistance and also when building AABBs in the broad phase
- a different alarmDistance and contactDistance can be specified for each CollisionModel by setting alarmDistance and contactDistance to zero and changing the proximity parameter

<!-- automatically generated doc START -->
__Target__: `Sofa.Component.Collision.Detection.Intersection`

__namespace__: `#!c++ sofa::component::collision::detection::intersection`

__parents__: 

- `#!c++ BaseProximityIntersection`

__categories__: 

- CollisionAlgorithm

Data: 

<table>
<thead>
    <tr>
        <th>Name</th>
        <th>Description</th>
        <th>Default value</th>
    </tr>
</thead>
<tbody>
	<tr>
		<td>name</td>
		<td>
object name
</td>
		<td>unnamed</td>
	</tr>
	<tr>
		<td>printLog</td>
		<td>
if true, emits extra messages at runtime.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>tags</td>
		<td>
list of the subsets the objet belongs to
</td>
		<td></td>
	</tr>
	<tr>
		<td>bbox</td>
		<td>
this object bounding box
</td>
		<td></td>
	</tr>
	<tr>
		<td>componentState</td>
		<td>
The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
</td>
		<td>Undefined</td>
	</tr>
	<tr>
		<td>listening</td>
		<td>
if true, handle the events, otherwise ignore the events
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>alarmDistance</td>
		<td>
Distance above which the intersection computations ignores the promixity pair. This distance can also be used in some broad phase algorithms to reduce the search area
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>contactDistance</td>
		<td>
Distance below which a contact is created
</td>
		<td>0.5</td>
	</tr>
	<tr>
		<td>filterIntersection</td>
		<td>
Activate LMD filter
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>angleCone</td>
		<td>
Filtering cone extension angle
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>coneFactor</td>
		<td>
Factor for filtering cone angle computation
</td>
		<td>0.5</td>
	</tr>
	<tr>
		<td>useLMDFilters</td>
		<td>
Use external cone computation
</td>
		<td>0</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|




<!-- automatically generated doc END -->
