Mappings
========


In SOFA, all the different representations of an object can be modeled and considered separately:
  - the physical model (e.g. a mechanical behavior relying on a linear elasticity, computed on a tetrahedral topology)
  - the visual model (e.g. a triangular mesh using a very high resolution)
  - the collision model (e.g. a grid bounding with quad faces around our physical object)

Relying on different geometrical models, this modular approach allows to tune the computational effort set on each of these representations. However, the simulation must ensure the coherency of these different representations. For instance, we want our visual model to move according to the physics. How is this done? The mappings in SOFA ensure this corresponding between the different representations of our object (physics, visual, collision etc.)


Matrix approach
---------------

Typical mappings compute the correspondance between different geometrical models by computing local coordinates (for rigid bodies) or barycentric coordinates (for deformable bodies).

 include polygonal shapes attached to rigid bodies using local coordinates, or
embedded in deformable cells using barycentric coordinates


Topological mapping
-------------------

Topological mappings are an additional type of mappings making the correspondance between hierarchical topologies. You can thus find :
  - a _Hexa2TetraTopologicalMapping_: computing the correspondance between a hexahedral and a tetrahedral topology, by dividing each hexahedron into 6 tetrahedra
  - a _Hexa2QuadTopologicalMapping_: computing the correspondance between a hexahedral topology and its surface quadrangular topology
  - a _Tetra2TriangleTopologicalMapping_: computing the correspondance between a tetrahedral topology and its surface triangular topology
  - a _Quad2TriangleTopologicalMapping_: computing the correspondance between a quadrangular and a triangular topology, by dividing each quad into 2 triangles
  - a _Triangle2EdgeTopologicalMapping_: computing the correspondance between a triangular and an edge topology