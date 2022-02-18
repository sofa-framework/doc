Vertex2Frame
============

For each point defined in an .obj file, this engine computes a set of rigid points using the normals. Normal vector will be collinear to the Z axis and orthonormal to X and Y as showed bellow:

```
Y
|
|   / X
|  /
| /
|/_ _ _ _ _ Z/normal
```

Input Data
----------

-   **position**: vertices defined in the loaded mesh
-   **texCoords**: texture coordinate defined in the loaded mesh
-   **normals**: normals defined in the loaded mesh

Output Data
-----------

-   **frames**: set of rigid types oriented as described before.  

Examples
---------

An example scene involving the vertex2Frame engine is available in [*examples/Components/engine/vertex2Frame.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/engine/vertex2Frame.scn)
