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
  - one mechanical model with its degrees of freedom <img class="latex" src="https://latex.codecogs.com/png.latex?$$q$$" title="DOF of mechanical model" />
  - one collision model with its degrees of freedom <img class="latex" src="https://latex.codecogs.com/png.latex?$$p$$" title="DOF of collision model" />

![Application of mappings](https://www.sofa-framework.org/wp-content/uploads/2018/10/Mapping-illustration.png)

The mapping defines a function (that can be non-linear) <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbb{J}$$" title="Mapping function" /> mapping kinematically the position of the parent mechanical model to the child collision model: <img class="latex" src="https://latex.codecogs.com/png.latex?$$p=\mathbb{J}(p)$$" title="Mapping relationship" />. The derivative of the degrees of freedom (velocities in case of positions) can be mapped in a similar way using the relationship <img class="latex" src="https://latex.codecogs.com/png.latex?$$v_p=\mathbf{J}v_q$$" title="Jacobian function" />, with <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{J}=\textstyle\frac{\partial%20p}{\partial%20q}" title="Jacobian matrix" /> is the associated Jacobian matrix. The mechanical model thus drives the collision model. In the case of a _BarycentricMapping_, the matrix <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{J}$$" title="Jacobian matrix" /> includes the barycentric coordinates.

By applying the principle of virtual work, the mapping can also translate forces applied to the child collision model <img class="latex" src="https://latex.codecogs.com/png.latex?$$f_p$$" title="Forces on collision model" /> into forces applied to the parent mechanical model <img class="latex" src="https://latex.codecogs.com/png.latex?$$f_q$$" title="Forces on mechanical model" />, using the relationship <img class="latex" src="https://latex.codecogs.com/png.latex?$$f_{q}=\mathbf{J}^{T}f_{p}$$" title="Bidirectional use of mapping" />. Mappings can therefore build a bijective correspondance between two representations of an object. Note that several mappings can also be applied recursively when necessary.


API of mappings
---------------

As explained above, the mappings propagate positions, velocities, displacements and accelerations top-down, and they propagate forces bottom-up. The top-down propagation methods are:

```cpp
//for positions
apply (const MechanicalParams*, MultiVecCoordId outPos, ConstMultiVecCoordId inPos );

//for velocities and small displacements
applyJ(const MechanicalParams*, MultiVecDerivId outVel, ConstMultiVecDerivId inVel );

//for accelerations, taking into account velocity-dependent accelerations in nonlinear mappings
computeAccFromMapping(const MechanicalParams*, MultiVecDerivId outAcc, ConstMultiVecDeri inVel, ConstMultiVecDerivId inAcc );
```

The bottom-up propagation methods are:

```cpp
//for child forces or changes of child forces
applyJT(const MechanicalParams*, MultiVecDerivId inForce, ConstMultiVecDerivId outForce );

//for changes of parent force due to a change of mapping with constant child force
applyDJT(const MechanicalParams*, MultiVecDerivId parentForce, ConstMultiVecDerivId childForce );

//for constraint Jacobians
applyJT(const ConstraintParams*, MultiMatrixDerivId inConst, ConstMultiMatrixDerivId outConst );
```

Topological mapping
-------------------

Topological mappings are an additional type of mappings making the correspondance between hierarchical topologies. You can thus find :
  - a _Hexa2TetraTopologicalMapping_: computing the correspondance between a hexahedral and a tetrahedral topology, by dividing each hexahedron into 6 tetrahedra
  - a _Hexa2QuadTopologicalMapping_: computing the correspondance between a hexahedral topology and its surface quadrangular topology
  - a _Tetra2TriangleTopologicalMapping_: computing the correspondance between a tetrahedral topology and its surface triangular topology
  - a _Quad2TriangleTopologicalMapping_: computing the correspondance between a quadrangular and a triangular topology, by dividing each quad into 2 triangles
  - a _Triangle2EdgeTopologicalMapping_: computing the correspondance between a triangular and an edge topology
