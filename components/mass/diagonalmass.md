---
title: DiagonalMass
---

DiagonalMass  
============

This component belongs to the category of [Masses](../../../simulation-principles/multi-model-representation/mass/). In the dynamic equation (see [Physics integration](../../../simulation-principles/multi-model-representation/physics-integration/) page), the mass density results from the first derivative in time of the momentum term. Like the MeshMatrixMass, the DiagonalMass computes the integral of this mass density over the volume of the object geometry. To do so and for any given topology (edges, triangles, quads, tetrahedra or hexahedra), the DiagonalMass integrates the mass density inside each elements and sums the mass matrix $\mathbf{M}$ in the system matrix $\mathbf{A}$.

However, the DiagonalMass makes a strong simplification: it considers the mass matrix $\mathbf{M}$ as being diagonal. To build this diagonal mass matrix, the DiagonalMass relies on a numerical method called the mass lumping. It consists in summing all mass values of a line on the diagonal. This approach is already implemented in the MeshMatrixMass but the DiagonalMass proposes an optimized version of the mass lumping and extend it to edge topology.

For details on the volume integration, please report to the [MeshMatrixMass](./../meshmatrixmass/) page. As demonstrated in the [MeshMatrixMass](./../meshmatrixmass/#case-of-a-linear-tetrahedron) page, in case of a topology using linear tetrahedra, the diagonal mass matrix corresponds to:


$$
\mathbf{M}\dot{v}=\sum_{e=0}^E \frac{\rho V_e}{4}\begin{bmatrix}1&0&0&0\\&1&0&0\\&0&1&0\\&0&0&1\\ \end{bmatrix}\begin{bmatrix}\dot{v}_1\\ \dot{v}_2\\ \dot{v}_3\\ \dot{v}_4\\ \end{bmatrix}
$$


By making the matrix diagonal (i.e. removing extra-diagonal terms), the lumping method removes the connectivity (neighborhood) information from the matrix. Due to this numerical approximation, the accuracy of the integration is decreased compared to the MeshMatrixMass integration. It is therefore advised to use the DiagonalMass carefully.




### API

Depending on the type of [LinearSolver](../../../simulation-principles/system-resolution/linear-solver/) used:

- for iterative solvers, the result of the multiplication between the mass matrix $\mathbf{M}$ and an approximated solution is computed by the function:

``` cpp
template <class DataTypes, class MassType>
void DiagonalMass<DataTypes, MassType>::addMDx(const core::MechanicalParams* /*mparams*/, DataVecDeriv& res, const DataVecDeriv& dx, SReal factor)
{
    const MassVector &masses= d_vertexMass.getValue();
    helper::WriteAccessor< DataVecDeriv > _res = res;
    helper::ReadAccessor< DataVecDeriv > _dx = dx;

    size_t n = masses.size();

    for (size_t i=0; i<n; i++)
    {
        _res[i] += (_dx[i] * masses[i]) * (Real)factor;
    }
}
```

- for direct solvers, the mass matrix $\mathbf{M}$ is built by the function:

``` cpp
template <class DataTypes, class MassType>
void DiagonalMass<DataTypes, MassType>::addMToMatrix(const core::MechanicalParams *mparams, const sofa::core::behavior::MultiMatrixAccessor* matrix)
{
    const MassVector &masses= d_vertexMass.getValue();
    const int N = defaulttype::DataTypeInfo<Deriv>::size();
    AddMToMatrixFunctor<Deriv,MassType> calc;
    sofa::core::behavior::MultiMatrixAccessor::MatrixRef r = matrix->getMatrix(this->mstate);
    Real mFactor = (Real)mparams->mFactorIncludingRayleighDamping(this->rayleighMass.getValue());
    for (unsigned int i=0; i<masses.size(); i++)
        calc(r.matrix, masses[i], r.offset + N*i, mFactor);
}
```


Usage
-----

The DiagonalMass **requires** a MechanicalObject to store the degrees of freedom associated to the nodes, as well as a Topology. An integration scheme and a solver are also necessary to solve the linear system at each time step.

All topologies are handled by the DiagonalMass, namely: edges, triangles, quads, tetrahedra or hexahedra.
