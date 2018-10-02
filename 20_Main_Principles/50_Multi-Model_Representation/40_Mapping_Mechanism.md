Mappings
========


In SOFA, all the different representations of an object can be modeled and considered separately:
  - the physical model (e.g. a mechanical behavior relying on a linear elasticity, computed on a tetrahedral topology)
  - the visual model (e.g. a triangular mesh using a very high resolution)
  - the collision model (e.g. a grid bounding with quad faces around our physical object)

Relying on different geometrical models, this modular approach allows to tune the computational effort set on each of these representations in order to find the best trade-off between accuracy and efficiency. However, the simulation must ensure the coherency of these different representations: for instance, we want our visual model to move according to the physics. To do so, SOFA relies on _Mappings_ to ensure this corresponding between the different representations of one-or-more object (physics, visual, collision etc.)


Matrix approach
---------------

Typical mappings compute the correspondance between different geometrical models by computing local coordinates (for rigid bodies) or barycentric coordinates (for deformable bodies). Once this correspondance is computed, it allows to project vectors (like forces) from one representation to another.


One can define two representations of an object, both using a different topology:
  - one mechanical model with its degrees of freedom _q_
  - one collision model with its degrees of freedom _p_
The mapping defines a function (that can be non-linear) <img src="https://latex.codecogs.com/gif.latex?$$\mathbb{J}$$" title="Mapping function" /> mapping kinematically the position of the parent mechnaical model to the child collision model: <img src="https://latex.codecogs.com/gif.latex?$$p=\mathbb{J}(p)$$" title="Mapping relationship" />. The derivative of the degrees of freedom (velocities in case of positions) can be mapped in a similar way using $$v_p=\mathbf{J}v_q$$, the mechanical model thus driving the collision model. $$\mathbf{J}$$ is therefore a Jacobian function. In the case of a _BarycentricMapping_, the matrix $$\mathbf{J}$$ includes the barycentric coordinates.

By applying the principle of virtual work, the mapping can also translate forces applied to the child collision model $$f_p$$ into forces applied to the parent mechanical model $$f_q$$, using $$f_q = \mathbf{J}^T f_p$$. Mappings can therefore build a bijective correspondance between two representations of an object. Note that several mappings can also be applied recursively when necessary.



Topological mapping
-------------------

Topological mappings are an additional type of mappings making the correspondance between hierarchical topologies. You can thus find :
  - a _Hexa2TetraTopologicalMapping_: computing the correspondance between a hexahedral and a tetrahedral topology, by dividing each hexahedron into 6 tetrahedra
  - a _Hexa2QuadTopologicalMapping_: computing the correspondance between a hexahedral topology and its surface quadrangular topology
  - a _Tetra2TriangleTopologicalMapping_: computing the correspondance between a tetrahedral topology and its surface triangular topology
  - a _Quad2TriangleTopologicalMapping_: computing the correspondance between a quadrangular and a triangular topology, by dividing each quad into 2 triangles
  - a _Triangle2EdgeTopologicalMapping_: computing the correspondance between a triangular and an edge topology