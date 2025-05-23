Mappings
========


In SOFA, all the different representations of an object can be modeled and considered separately:

  - the physical model (e.g. a mechanical behavior relying on a linear elasticity, computed on a tetrahedral topology)
  - the visual model (e.g. a triangular mesh using a very high resolution)
  - the collision model (e.g. a grid bounding with quad faces around our physical object)

Relying on different geometrical models, this modular approach allows to tune the computational effort set on each of these representations in order to find the best trade-off between accuracy and efficiency. However, the simulation must ensure the coherency of these different representations: for instance, we want our visual model to move according to the physics. To do so, SOFA relies on _Mappings_ to ensure this corresponding between the different representations of one-or-more object (physics, visual, collision etc.)


Matrix approach
---------------

Typical mappings compute the correspondence between different geometrical models by computing local coordinates (for rigid bodies) or barycentric coordinates (for deformable bodies). Once this correspondence is computed, it allows to project vectors (like forces) from one representation to another.


One can define two representations of an object, both using a different topology:

  - one mechanical model with its degrees of freedom $q$
  - one collision model with its degrees of freedom $p$

![Application of mappings](https://www.sofa-framework.org/wp-content/uploads/2018/10/Mapping-illustration.png)

The mapping defines a function (that can be non-linear) $\mathbb{J}$ mapping kinematically the position of the parent mechanical model to the child collision model: $p=\mathbb{J}(q)$. The derivative of the degrees of freedom (velocities in case of positions) can be mapped in a similar way using the relationship $v_p=\mathbf{J}v_q$, with $\mathbf{J}=\textstyle\frac{\partial p}{\partial q}$ is the associated Jacobian matrix. The mechanical model thus drives the collision model. In the case of a _BarycentricMapping_, the matrix $\mathbf{J}$ includes the barycentric coordinates.

By applying the principle of virtual work, the mapping can also translate forces applied to the child collision model $f_p$ into forces applied to the parent mechanical model $f_q$, using the relationship $f_{q}=\mathbf{J}^{T}f_{p}$. Mappings can therefore build a bijective correspondence between two representations of an object. Note that several mappings can also be applied recursively when necessary.

When a force field is associated to a mapped state, it contributes to the stiffness matrix indirectly, through the mapping. Two terms appear.

- The first term is the projection of the mapped stiffness matrix from the mapped space into the main state $\mathbf{J}^{T}\frac{\partial f_p}{\partial p}\mathbf{J}$.
- The second term is called geometric stiffness: $\frac{\partial \mathbf{J}^{T}}{\partial q}f_p$. Geometric stiffness relies on the derivative of the Jacobian matrix. This derivative is null if the mapping is linear.

> ⚠️ **WARNING**: Depending on the nature of a non-linear mapping, geometric stiffness may lead to non-symmetric terms in the mechanical matrix. Such mappings have an option to make the contributions symmetric. An alternative is to use an appropriate linear solver (LU solver for example).

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

Nomenclature of Mappings
------------------------

Mappings in SOFA are designed to link two objects, enabling data transfer or interaction between them. However, some scenarios require connections where multiple objects serve as sources or targets. To handle these cases, SOFA provides specialized mapping classes that support these complex interactions:

| Class         | Input                           | Output | Description                                                                                                                           |
|---------------|---------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------|
| Mapping       | Single                          | Single | Standard mapping between two objects. Both objects can have different types.                                                          |
| MultiMapping  | Multiple of the same type       | Multiple of the same type | Maps multiple input objects of the same type to multiple output objects of the same type. Types in input and output can be different. |
| Multi2Mapping | Multiple of two different types | Multiple of the same type | Maps multiple input objects of two different types to multiple output objects of the same type.                                       |

Mappings can also be categorized according to the linearity of the mapping function:

| Type               | Description                                                                        |
|--------------------|------------------------------------------------------------------------------------|
| Linear mapping     | The Hessian tensor is null. The functions related to non-linear terms are empty.   |
| Non-linear mapping | The Hessian tensor is not null. A geometric stiffness is generated by the mapping. |


Common mappings
---------------
- [IdentityMapping](../../../components/mapping/linear/identitymapping/) when both models have the same degrees of freedom
- [BarycentricMapping](../../../components/mapping/linear/barycentricmapping/) interpolating degrees of freedom using barycentric coordinates
- [RigidMapping](../../../components/mapping/nonlinear/rigidmapping/) used with RigidObject


Topological mapping
-------------------

Topological mappings are an additional type of mappings making the correspondence between hierarchical topologies. You can thus find :

  - a [Hexa2TetraTopologicalMapping](../../../components/topology/mapping/hexa2tetratopologicalmapping/): computing the correspondence between a hexahedral and a tetrahedral topology, by dividing each hexahedron into 6 tetrahedra
  - a [Hexa2QuadTopologicalMapping](../../../components/topology/mapping/hexa2quadtopologicalmapping/): computing the correspondence between a hexahedral topology and its surface quadrangular topology
  - a [Tetra2TriangleTopologicalMapping](../../../components/topology/mapping/tetra2triangletopologicalmapping/): computing the correspondence between a tetrahedral topology and its surface triangular topology
  - a [Quad2TriangleTopologicalMapping](../../../components/topology/mapping/quad2triangletopologicalmapping/): computing the correspondence between a quadrangular and a triangular topology, by dividing each quad into 2 triangles
  - a [Triangle2EdgeTopologicalMapping](../../../components/topology/mapping/triangle2edgetopologicalmapping/): computing the correspondence between a triangular and an edge topology
