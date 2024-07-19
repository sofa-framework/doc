MeshMatrixMass  
==============

This component belongs to the category of [Masses](../../simulation-principles/multi-model-representation/mass/). In the dynamic equation (see [Physics integration](../../simulation-principles/multi-model-representation/physics-integration/) page), the mass density results from the first derivative in time of the momentum term. The MeshMatrixMass computes the integral of this mass density over the volume of the object geometry. To do so and for any given topology (triangles, quads, tetrahedra or hexahedra), the MeshMatrixMass integrates the mass density inside each elements and sums the mass matrix $$\mathbf{M}$$ in the system matrix $$\mathbf{A}$$.


### Volume integration

As detailed in the [Physics integration](../../simulation-principles/multi-model-representation/physics-integration/) page, the left hand side part of the linear momentum conservation equals $$\rho\dot{v}$$. To integrate over the domain, its weak form will result in the mass matrix:

$$\mathbf{M}\dot{v}=\int_{\Omega}%20\phi_j%20\rho%20\dot{v}d\Omega$$

where $$\phi_j$$ are the test functions, which are basis functions ensuring the existence of a solution. Since no exact integration can be performed on a random domain $$\Omega$$, the MeshMatrixMass relies on the Finite Element Method (FEM) and accumulates the result of the integral over each finite element (triangles, quads, tetrahedra or hexahedra):

$$\mathbf{M}\dot{v}=\sum_{e=0}^E%20\int_{V_e}%20\phi_j%20\rho%20\dot{v}dV_e$$

The FEM relies on simple geometries in which any field can be interpolated using shape functions $$\phi_i$$ (see [FEM at a glance](../../simulation-principles/multi-model-representation/physics-integration/#fem-at-a-glance)). Note that the same basis functions are chosen for both the test and the shape functions. The interpolation of the acceleration term $$\dot{v}$$ thus gives:

$$\mathbf{M}\dot{v}=\sum_{e=0}^E%20\rho%20\int_{V_e}%20\phi_j%20\sum_{i=0}^{N}%20\phi_i%20\dot{v}_i%20dV_e$$

By change of variables, the computation of the mass matrix results in solving the following integration of the shape functions $$\phi$$ in each element:

$$\mathbf{M}\dot{v}=\sum_{e=0}^E%20\rho%20\int_{V_e}%20|det(J)|%20\sum_{i=0}^{N}\phi_j(\boldsymbol{\xi})%20\phi_i(\boldsymbol{\xi})%20\dot{v}_i%20d%20\boldsymbol{\xi}$$


### Case of a linear tetrahedron
In the case of a linear tetrahedron, the shape functions are:

$$\begin{align*}&\phi_1=1-\xi%20-\eta%20-\zeta%20\\&\phi_2=\xi%20\\&\phi_3=\eta%20\\&\phi_4=\zeta%20\\%20\end{align*}$$

By replacing the shape functions, we therefore obtain:

$$\mathbf{M}\dot{v}=\sum_{e=0}^E%20\rho%20\int_{V_e}%20|det(J)|%20\phi_j%20\phi_i%20\dot{v}_i%20d%20\boldsymbol{\xi}$$

$$\mathbf{M}\dot{v}=\sum_{e=0}^E%20\rho%20\int_{V_e}%20|det(J)|%20\begin{bmatrix}\phi_1^2&\phi_1\phi_2&\phi_1\phi_3&\phi_1\phi_4%20\\\phi_2\phi_1&\phi_2^2&\phi_2\phi_3&\phi_2\phi_4%20\\\phi_3\phi_1&\phi_3\phi_2&\phi_3^2&\phi_3\phi_4%20\\\phi_4\phi_1&\phi_4\phi_2&\phi_4\phi_3&\phi_4^2%20\\%20\end{bmatrix}%20\begin{bmatrix}\dot{v}_1\\%20\dot{v}_2\\%20\dot{v}_3\\%20\dot{v}_4\\%20\end{bmatrix}%20d%20\boldsymbol{\xi}$$

$$\mathbf{M}\dot{v}=\sum_{e=0}^E%20\rho%20\int_{\xi}%20\int_{\eta}%20\int_{\zeta}%20|det(J)|%20\begin{bmatrix}(1-\xi%20-\eta%20-\zeta)^2&\xi-\xi^2%20-\eta\xi%20-\zeta\xi&\eta-\xi\eta%20-\eta^2%20-\zeta\eta&\zeta-\xi\zeta%20-\eta\zeta\zeta%20-\zeta^2%20\\\phi_2\phi_1&\xi^2&\xi\eta&\xi\zeta%20\\\phi_3\phi_1&\phi_3\phi_2&\eta^2&\eta\zeta%20\\\phi_4\phi_1&\phi_4\phi_2&\phi_4\phi_3&\zeta^2%20\\%20\end{bmatrix}%20\begin{bmatrix}\dot{v}_1\\%20\dot{v}_2\\%20\dot{v}_3\\%20\dot{v}_4\\%20\end{bmatrix}%20d\xi%20d\eta%20d\zeta$$

We can note that the matrix is symmetric. The integration in the reference (or parent) space $$\boldsymbol{\xi}$$ can be numerically computed using a [Gauss quadrature](https://en.wikipedia.org/wiki/Gaussian_quadrature) (or Gauss point integration). The resulting mass matrix is:

$$\mathbf{M}\dot{v}=\sum_{e=0}^E%20\frac{\rho%20V_e}{20}\begin{bmatrix}2&1&1&1\\1&2&1&1\\1&1&2&1\\1&1&1&2\\%20\end{bmatrix}\begin{bmatrix}\dot{v}_1\\%20\dot{v}_2\\%20\dot{v}_3\\%20\dot{v}_4\\%20\end{bmatrix}$$


### API

Depending on the type of [LinearSolver](../../simulation-principles/system-resolution/linear-solver/) used:

- for iterative solvers, the result of the multiplication between the mass matrix $$\mathbf{M}$$ and an approximated solution is computed by the function:

``` cpp
template <class DataTypes, class MassType>
void MeshMatrixMass<DataTypes, MassType>::addMDx(const core::MechanicalParams*, DataVecDeriv& vres, const DataVecDeriv& vdx, SReal factor)
{
    const MassVector &vertexMass= d_vertexMassInfo.getValue();
    const MassVector &edgeMass= d_edgeMassInfo.getValue();

    helper::WriteAccessor< DataVecDeriv > res = vres;
    helper::ReadAccessor< DataVecDeriv > dx = vdx;

    size_t v0,v1,nbEdges=_topology->getNbEdges();

    for (unsigned int i=0; i<dx.size(); i++)
    {
        res[i] += dx[i] * vertexMass[i] * (Real)factor;
    }

    for (unsigned int j=0; j<nbEdges; ++j)
    {
        v0=_topology->getEdge(j)[0];
        v1=_topology->getEdge(j)[1];

        res[v0] += dx[v1] * edgeMass[j] * (Real)factor;
        res[v1] += dx[v0] * edgeMass[j] * (Real)factor;
    }
}
```

- for direct solvers, the mass matrix $$\mathbf{M}$$ is built by the function:

``` cpp
template <class DataTypes, class MassType>
void MeshMatrixMass<DataTypes, MassType>::addMToMatrix(const core::MechanicalParams *mparams, const sofa::core::behavior::MultiMatrixAccessor* matrix)
{
    const MassVector &vertexMass= d_vertexMassInfo.getValue();
    const MassVector &edgeMass= d_edgeMassInfo.getValue();

    size_t v0,v1,nbEdges=_topology->getNbEdges();

    const int N = defaulttype::DataTypeInfo<Deriv>::size();
    AddMToMatrixFunctor<Deriv,MassType> calc;
    sofa::core::behavior::MultiMatrixAccessor::MatrixRef r = matrix->getMatrix(this->mstate);
    sofa::defaulttype::BaseMatrix* mat = r.matrix;
    Real mFactor = (Real)mparams->mFactorIncludingRayleighDamping(this->rayleighMass.getValue());


    for (size_t i = 0; i < vertexMass.size(); i++)
    {
        calc(r.matrix, vertexMass[i], r.offset + N*i, mFactor);
    }

    for (size_t j = 0; j < nbEdges; ++j)
    {
        v0 = _topology->getEdge(j)[0];
        v1 = _topology->getEdge(j)[1];

        calc(r.matrix, edgeMass[j], r.offset + N*v0, r.offset + N*v1, mFactor);
        calc(r.matrix, edgeMass[j], r.offset + N*v1, r.offset + N*v0, mFactor);
    }
}

```
### Case of mass lumping

Note that using the optional data **lumping**, it is possible to simply the mass matrix by making it diagonal. This is called mass lumping and it consists in summing all mass values of a line on the diagonal. The DiagonalMass is an optimized version of this mass lumping approach. In case of a linear tetrahedron, if the data **lumping** is true, the (lumped) mass matrix becomes:

$$\mathbf{M}\dot{v}=\sum_{e=0}^E%20\frac{\rho%20V_e}{4}\begin{bmatrix}1&0&0&0\\&1&0&0\\&0&1&0\\&0&0&1\\%20\end{bmatrix}\begin{bmatrix}\dot{v}_1\\%20\dot{v}_2\\%20\dot{v}_3\\%20\dot{v}_4\\%20\end{bmatrix}$$

Use lumping with caution since it is a numerical approximation, thus decreasing the accuracy of the integration.



Usage
-----

The MeshMatrixMass **requires** a MechanicalObject to store the degrees of freedom associated to the nodes, as well as a Topology. An integration scheme and a solver are also necessary to solve the linear system at each time step.

Several topologies are handled by the MeshMatrixMass, namely: triangles, quads, tetrahedra or hexahedra. Only the beam model (edge topology) is not handled by this component.
