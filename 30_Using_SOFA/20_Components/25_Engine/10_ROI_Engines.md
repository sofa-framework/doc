An Engine is a component that computes a set of output Data's from a set
of input Data's. For the moment, Here are some interesting engines which
are implemented in SOFA :

BoxROI, PlaneROI, SphereROI
---------------------------

\[toggle title="Detailed information" open="false"\] **These three
engines have each their own behaviour and their own specific input
parameters :**
![BoxRoi](https://www.sofa-framework.org/wp-content/uploads/2014/11/BoxRoi1.png){.wp-image-1424
.alignright width="259" height="269"}

### BoxROI

**This engine finds the topological primitives which are inside a given
box.**

-   **box**

Box defined by two points (xmin,ymin,zmin, xmax,ymax,zmax).

-   **position/rest\_position**

Rest position coordinates of the degrees of freedom    

### PlaneROI![PlaneRoi](https://www.sofa-framework.org/wp-content/uploads/2014/11/PlaneRoi1.png){.wp-image-1437 .alignright width="404" height="228"}

**This engine finds the points which are inside a given box computed
from a plane defined by three points and a depth distance.**

-    **planes**

Plane defined by 3 points and a depth distance (as shown above).

-   **position/rest\_position**

Rest position coordinates of the degrees of freedom  

### SphereROI[![SphereRoi](https://www.sofa-framework.org/wp-content/uploads/2014/11/SphereRoi1.png){.wp-image-1439 .alignright width="403" height="241"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/SphereRoi1.png)

**This engine finds the topological primitives which are inside a given
sphere.**

-   **centers**

Center(s) of the sphere(s).

-   **radii**

Radius(i) of the sphere(s).

-   **direction**

Edge direction(if edgeAngle &gt; 0).

-   **normal**

Normal direction of the triangles (if triAngle &gt; 0).

-   **edgeAngle**

Max angle between the direction of the selected edges and the specified
direction.

-   **triAngle**

Max angle between the normal of the selected triangle and the specified
normal direction.

-   **position/rest\_position**

Rest position coordinates of the degrees of freedom   These three
engines also have shared input and output parameters that can be used
depending of the need in the scene :

#### Input topology

-   **edges**

Edge Topology array.

-   **triangles**

Triangle Topology array.

-   **tetrahedra**

Tetrahedron Topology array.  

#### Input parameters

Concerning topology Note that those parameters are set to true by
default. So it means that as default behaviour, all topological
component array will be parse. Set some parameters to false if you just
need a part of the information and want to speed-up your simulation.

-   **computeEdges**

If true, will compute edge list and index list inside the ROI.

-   **computeTriangles**

If true, will compute triangle list and index list inside the ROI.

-   **computeTetrahedra**

If true, will compute tetrahedra list and index list inside the ROI.  

#### Output data's

-   **indices**

Indices of the points contained in the ROI.

-   **edgeIndices**

Indices of the edges contained in the ROI.

-   **triangleIndices**

Indices of the triangles contained in the ROI.

-   **tetrahedronIndices**

Indices of the tetrahedra contained in the ROI.

-   **pointsInROI**

Points contained in the ROI.

-   **edgesInROI**

Edges contained in the ROI.

-   **trianglesInROI**

Triangles contained in the ROI.

-   **tetrahedraInROI**

Tetrahedra contained in the ROI.  

#### Examples

**BoxROI :**





and you can also test these other scenes using the engine :

```
Sofa/examples/Components/engine/BoxROI.scn
Sofa/examples/Components/Constraint/BoxConstraint.scn
Sofa/examples/Components/Forcefield/BoxContactForcefield.scn
```

**PlaneROI :**

and you can also test these other scenes using the engine :

```
Sofa/examples/Components/engine/PlaneROI.scn
Sofa/examples/Components/Constraint/PlaneConstraint.scn
```

**SphereROI :**


and you can also test this other scene using the engine:

```
Sofa/examples/Components/engine/SphereROI.scn
```

\[/toggle\]

ExtrudeSurface
--------------

\[toggle title="Detailed information" open="false"\] **This engine
extrude a surface and returns corresponding triangles.**

#### Input data's

-   **triangles**

list of triangles of the object to extrude. /! It must me a vector of
BaseMeshTopology::Triangle

-   **surfaceTriangles**

list of triangles of the surface to extrude. /! The type of triangle
must be BaseMeshTopology::TriangleID, and not BaseMeshTopology::Triangle

-   **surfaceVertices**

list of positions  

#### Output data's

-   **extrusionVertices**

list of positions of the new triangles, created from extrusion

-   **extrusionTriangles**

list of triangles from extrusion (vector of BaseMeshTopology::Triangle)
 

#### Important Parameter

-   **heightFactor**

extrusion is based on normals. So, this factor defines the final height
of the extrusion.  

#### Examples

See multi-engines example. Typically, a line in scene file will be in
this form :

\[/toggle\]

MergePoints
-----------

\[toggle title="Detailed information" open="false"\] **This engine
returns a merged list of positions, given 2 primary lists.**

#### Input data's

-   **X1**

  positions of the 1st object.

-   **X2**

  positions of the 2nd object.  

#### Output data's

-   **points**

  a new list of positions, containing the 2 previous lists

-   **indices1**

  indices of the 1st position list in the new list

-   **indices2**

  indices of the 2nd position list in the new list  

#### Examples

See multi-engines example. \[/toggle\]

PointsFromIndices
-----------------

\[toggle title="Detailed information" open="false"\] **This engine
returns positions from given indices.**

#### Input data's

-   **X**

  positions of the mechanical object.

-   **indices**

  indices we want to have corresponding positions.  

#### Output data's

-   **indices\_position**

  positions according to given indices  

#### Examples

See multi-engines example. \[/toggle\]

RandomDistributionInSurface
---------------------------

\[toggle title="Detailed information" open="false"\] **This engine
creates a set of randomly distributed points in a closed surface.**

#### Input data's

-   **triangles**

 

list of triangles of the closed surface

-   **points**

  list of positions of the previous triangles

-   **surfaceVertices**

  list of positions  

#### Output data's

-   **inPoints**

  list of generated points, which are inside the closed surface.  

#### Important Parameter

-   **numberOfInPoints**

  desired number of generated points

-   **minDistanceBetweenPoints**

  minimum distance between 2 points (put -1 for true randomness)

-   **numberOfTests**

  testing if a point is in a closed surface consists in seeing if the
point and a random direction intersects the surface. Obviously, if the
direction is not very convenient, the result will be not correct. So we
can put a certain number of tests to be valid.

-   **randomSeed**

  if you want the same pattern each time you run the test, fix the seed
to have always the same results.  

#### Examples

See multi-engines example. \[/toggle\]

TextureInterpolation
--------------------

\[toggle title="Detailed information" open="false"\] **This engine
create texture coordinate in 1D according to an imput state vector.
Coordinate can be interpolated either from min and max value of input
states (default behavior) or on a manual define scale.**

#### Input data's

-   **input\_states**

  Input array of state values.

-   **input\_coordinates**

  Input array of coordinates values (not mandatory).  

#### Output data's

-   **output\_coordinates**

  Output array of texture coordinates.  

#### Additional Parameter

**For manual scale :**

-   **min\_value**

  Minimum value of state value for interpolation.

-   **max\_value**

  Maximum value of state value for interpolation.

-   **manual\_scale**

  Compute texture interpolation on manually scale defined above  

#### Examples

See the example scene :

```
Sofa/examples/Components/engine/TextureInterpolation.scn
```

\[/toggle\]

TransformPosition
-----------------

\[toggle title="Detailed information" open="false"\] **This engine
transforms the positions of one DataFields into new positions after
applying a transformation. This transformation can be either:**

-   Projection on a plane (plane defined by an origin and a
    normal vector).
-   Translation, rotation, scale and some combinations of translation,
    rotation and scale.

 

#### Input data's

-   **input\_position**

Input array of 3d points.  

#### Output data's

-   **output\_position**

Output array of 3d points projected on a plane.  

#### Additional Parameter

-   **method**

Transformation method either translation or scale or rotation or
projectOnPlane. \[/toggle\]

Spiral
------

\[toggle title="Detailed information" open="false"\] **This engine turns
on spiral any topological model.**

#### Input data's

-   **f\_X0**

Rest position of the mechanical object.  

#### Output data's

-   **f\_X**

Position of the mechanical object once it has been turned on spiral.  

#### Examples

See the example scene :

```
Sofa/examples/Components/engine/spiral.scn
```

\[/toggle\]

Vertex2Frame
------------

\[toggle title="Detailed information" open="false"\] **For each point
defined in an .obj file, this engine computes a set of rigid points
using the normals. Normal vector will be collinear to the Z axis and
orthonormal to X and Y as showed bellow:**

```
Y
|
|   / X
|  /
| /
|/_ _ _ _ _ Z/normal
```

#### Input data's

-   **normals**

normals defined in the .obj file.

-   **vertices**

vertices defined in the .obj file.  

#### Output data's

-   **frames**

Set of rigid types oriented as described before.  

#### Examples

or you can see the example scene :

```
Sofa/examples/Components/engine/vertex2Frame.scn
```

\[/toggle\]

Spiral
------

\[toggle title="Detailed information" open="false"\] **This engine turns
on spiral any topological model.**

#### Input data's

-   **f\_X0**

Rest position of the mechanical object.  

#### Output data's

-   **f\_X**

Position of the mechanical object once it has been turned on spiral.  

#### Examples

See the example scene :

```
Sofa/examples/Components/engine/spiral.scn
```

\[/toggle\]

SubSetTopology
--------------

\[toggle title="Detailed information" open="false"\]
![SubsetTopology](https://www.sofa-framework.org/wp-content/uploads/2014/11/SubsetTopology.png){.wp-image-1612
.alignright width="328" height="324"} **This engine separate topology in
two parts, considering a ROI, a topology inside and a topology outside
the ROI which can be a sphere or a box ROI used in this engine are
similar to BoxROI and SphereROI.**

#### Input Data's

-   **box**

Box defined by two points (xmin,ymin,zmin, xmax,ymax,zmax).

-   **centers**

Center(s) of the sphere(s).

-   **radii**

Radius(i) of the sphere(s).

-   **direction**

Edge direction(if edgeAngle &gt; 0).

-   **normal**

Normal direction of the triangles (if triAngle &gt; 0).

-   **edgeAngle**

Max angle between the direction of the selected edges and the specified
direction.

-   **triAngle**

Max angle between the normal of the selected triangle and the specified
normal direction.   **Input topology**

-   **position/rest\_position**

Rest position coordinates of the degrees of freedom.

-   **edges**

Edge Topology array.

-   **triangles**

Triangle Topology array.

-   **tetrahedra**

Tetrahedron Topology array.  

#### Input parameters

**For display:**

-   **drawROI**

If true, Draw ROI(s).

-   **drawPoints**

If true, Draw Points.

-   **drawEdges**

If true, Draw Edges.

-   **drawTriangle**

If true, Draw Triangles.

-   **drawTetrahedra**

If true, Draw Tetrahedra.

-   **drawSize**

Rendering size for box and elements. **For behaviour:**

-   **localIndices**

If true, will compute local dof indices in topological elements. (see
examples below)  

#### Output data's

-   **indices**

Indices of the points contained in the ROI.

-   **edgeIndices**

Indices of the edges contained in the ROI.

-   **triangleIndices**

Indices of the triangles contained in the ROI.

-   **tetrahedronIndices**

Indices of the tetrahedra contained in the ROI.

-   **pointsInROI**

Points contained in the ROI.

-   **pointsOutROI**

Points contained out of the ROI.

-   **edgesInROI**

Edges contained in the ROI.

-   **edgesOutROI**

Edges contained out of the ROI.

-   **trianglesInROI**

Triangles contained in the ROI.

-   **trianglesOutROI**

Triangles contained out of the ROI.

-   **tetrahedraInROI**

Tetrahedra contained in the ROI.

-   **tetrahedraOutROI**

Tetrahedra contained out of the ROI.

-   **nbrborder**

If localIndices option is activated, will give the number of vertices on
the border of the ROI (being the n first points of each output
Topology).  

#### Examples

See the example scenes using this engine in :

```
Sofa/examples/Components/engine/SubsetTopology.scn
Sofa/examples/Components/engine/SubsetTopology_localIndicesOption.scn
Sofa/examples/Components/engine/SubsetTopology_refiningMesh.scn
```

\[/toggle\]
