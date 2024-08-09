---
title: Vertex2Frame
---

Vertex2Frame
============

This component belongs to the category of [Engines](../../../../simulation-principles/engine/). For each point defined in an .obj file, this engine computes a set of rigid points using the normals. Normal vector will be collinear to the Z axis and orthonormal to X and Y as showed bellow:

```
Y
|
|   / X
|  /
| /
|/_ _ _ _ _ Z/normal
```
