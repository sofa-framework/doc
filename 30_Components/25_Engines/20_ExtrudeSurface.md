ExtrudeSurface
==============

This engine extrude a surface and returns corresponding triangles.

Input Data
----------

-   **triangles**: list of triangles of the object to extrude. It must me a vector of BaseMeshTopology::Triangle
-   **surfaceTriangles**: list of triangles of the surface to extrude. The type of triangle must be BaseMeshTopology::TriangleID, and not BaseMeshTopology::Triangle
-   **surfaceVertices**: list of positions

Output Data
----------

-   **extrusionVertices**: list of positions of the new triangles, created from extrusion
-   **extrusionTriangles**: list of triangles from extrusion (vector of BaseMeshTopology::Triangle)


Important Parameter
-------------------


-   **heightFactor**: extrusion is based on normals. So, this factor defines the final height of the extrusion.

Examples
--------

An example scene involving the ExtrudeSurface engine is available in [*examples/Components/engine/ExtrudeSurface.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/engine/ExtrudeSurface.scn)