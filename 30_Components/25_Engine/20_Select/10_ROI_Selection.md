ROI Selection
=============

An [Engine](https://www.sofa-framework.org/community/doc/simulation-principles/engine/) is a component that computes a set of output Data's from a set of input Data's. Several ROI engines (standing for "Region Of Interest") allow for selecting topological elements of an object. Three engines thus provide point indices, edges, triangles, tetrahedra and/or hexahedra as output:

- BoxROI
- PlaneROI
- SphereROI


Inputs
------

### BoxROI

This engine finds the topological primitives which are inside a given box. Below are given its Data:


-   **box**: defined by two points (xmin,ymin,zmin, xmax,ymax,zmax)
-   **position/rest\_position**: rest position coordinates of the degrees of freedom    

![](https://www.sofa-framework.org/wp-content/uploads/2014/11/BoxRoi1.png){.wp-image-1424 .aligncenter width="40%" height="auto"}


### PlaneROI

This engine finds the points which are inside a given box computed from a plane defined by three points and a depth distance. Below are given its Data:

-    **planes**: plane defined by 3 points and a depth distance (as shown above).
-   **position/rest\_position**: rest position coordinates of the degrees of freedom  

![](https://www.sofa-framework.org/wp-content/uploads/2014/11/PlaneRoi1.png){.wp-image-1437 .aligncenter width="40%" height="auto"}


### SphereROI

This engine finds the topological primitives which are inside a given sphere.


-   **centers**: center(s) of the sphere(s)
-   **radii**: radius(i) of the sphere(s)
-   **direction**: edge direction(if edgeAngle &gt; 0)
-   **normal**: normal direction of the triangles (if triAngle &gt; 0)
-   **edgeAngle**: max angle between the direction of the selected edges and the specified direction
-   **triAngle**: max angle between the normal of the selected triangle and the specified normal direction
-   **position/rest\_position**: rest position coordinates of the degrees of freedom

![](https://www.sofa-framework.org/wp-content/uploads/2014/11/SphereRoi1.png){.wp-image-1439 .aligncenter width="40%" height="auto"}


Output
------

These three engines also have shared input and output parameters that can be used depending on the need in the scene :

#### Input topology

-   **edges**: edge Topology array
-   **triangles**: triangle Topology array
-   **tetrahedra**: tetrahedron Topology array


#### Input parameters

Concerning topology Note that those parameters are set to true by default. So it means that as default behaviour, all topological component array will be parsed. Set some parameters to false if you just need a part of the information and want to speed up your simulation.

-   **computeEdges**: if true, will compute edge list and index list inside the ROI.
-   **computeTriangles**: if true, will compute triangle list and index list inside the ROI.
-   **computeTetrahedra**: if true, will compute tetrahedra list and index list inside the ROI.  

#### Output data's

-   **indices**: indices of the points contained in the ROI
-   **edgeIndices**: indices of the edges contained in the ROI
-   **triangleIndices**: indices of the triangles contained in the ROI
-   **tetrahedronIndices**: indices of the tetrahedra contained in the ROI
-   **pointsInROI**: points contained in the ROI
-   **edgesInROI**: edges contained in the ROI
-   **trianglesInROI**: triangles contained in the ROI
-   **tetrahedraInROI**: tetrahedra contained in the ROI

Examples
--------

**BoxROI** usage is shown in the following scene files:

- [*examples/Component/Engine/Select/BoxROI.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/Engine/Select/BoxROI.scn)
- [*examples/Component/Constraint/Projective/BoxConstraint.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/Constraint/Projective/BoxConstraint.scn)


**PlaneROI** usage is shown in the following scene files:

- [*examples/Component/Engine/Select/PlaneROI.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/Engine/Select/PlaneROI.scn)
- [*examples/Component/Constraint/Projective/PlaneConstraint.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/Constraint/Projective/PlaneConstraint.scn)


**SphereROI** usage is shown in the following scene files:

- [*examples/Component/Engine/Select/SphereROI.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/Engine/Select/SphereROI.scn)
