SubSetTopology
==============

This engine separate topology in two parts, considering a ROI, a topology inside and a topology outside the ROI which can be a sphere or a box ROI used in this engine are similar to BoxROI and SphereROI.
![SubsetTopology](https://www.sofa-framework.org/wp-content/uploads/2014/11/SubsetTopology.png){.wp-image-1612 .alignright width="40%" height="auto"}

Input Data
----------

-   **box**: box defined by two points (xmin,ymin,zmin, xmax,ymax,zmax)
-   **centers**: center(s) of the sphere(s)
-   **radii**: radius(i) of the sphere(s)
-   **direction**: edge direction(if edgeAngle > 0)
-   **normal**: normal direction of the triangles (if triAngle > 0)
-   **edgeAngle**: max angle between the direction of the selected edges and the specified direction
-   **triAngle**: max angle between the normal of the selected triangle and the specified normal direction

**Input topology**

-   **position/rest\_position**: rest position coordinates of the degrees of freedom
-   **edges**: edge Topology array
-   **triangles**: triangle Topology array
-   **tetrahedra**: tetrahedron Topology array

Input parameters
----------------

**For display:**

-   **drawROI**: if true, Draw ROI(s).
-   **drawPoints**: if true, Draw Points
-   **drawEdges**: if true, Draw Edges.
-   **drawTriangle**: if true, Draw Triangles.
-   **drawTetrahedra**: if true, draw tetrahedra
-   **drawSize**: rendering size for box and elements.

**For behaviour:**

-   **localIndices**: if true, will compute local dof indices in topological elements. (see examples below)  

Output Data
-----------

-   **indices**: indices of the points contained in the ROI
-   **edgeIndices**: indices of the edges contained in the ROI
-   **triangleIndices**: indices of the triangles contained in the ROI
-   **tetrahedronIndices**: indices of the tetrahedra contained in the ROI
-   **pointsInROI**: points contained in the ROI
-   **pointsOutROI**: points contained out of the ROI
-   **edgesInROI**: edges contained in the ROI
-   **edgesOutROI**: edges contained out of the ROI
-   **trianglesInROI**: triangles contained in the ROI
-   **trianglesOutROI**: triangles contained out of the ROI
-   **tetrahedraInROI**: tetrahedra contained in the ROI
-   **tetrahedraOutROI**: tetrahedra contained out of the ROI
-   **nbrborder**: if localIndices option is activated, will give the number of vertices on the border of the ROI (being the n first points of each output Topology).  



Examples
--------

Three example scenes involving the SubsetTopology engine are available:

- [*examples/Components/engine/SubsetTopology.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/engine/SubsetTopology.scn)
- [*examples/Components/engine/SubsetTopology_localIndicesOption.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/engine/SubsetTopology_localIndicesOption.scn)
- [*examples/Components/engine/SubsetTopology_refiningMesh.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/engine/SubsetTopology_refiningMesh.scn)
