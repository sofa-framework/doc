MeshMatrixMass  
==============

This component belongs to the category of [Masses](https://www.sofa-framework.org/community/doc/main-principles/multi-model-representation/mass/). In the dynamic equation (see [Physics integration](https://www.sofa-framework.org/community/doc/main-principles/multi-model-representation/physics-integration/) page), the mass density results from the first derivative in time of the momentum term. The MeshMatrixMass computes the integral of this mass density over the volume of the object geometry. To do so and for any given topology (triangles, quads, tetrahedra or hexahedra), the MeshMatrixMass integrates the mass density inside each elements and sums the mass matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}" title="Mass matrix" /> in the system matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" />.


### Volume integration

As detailed in the [Physics integration](https://www.sofa-framework.org/community/doc/main-principles/multi-model-representation/physics-integration/) page, the left hand side part of the linear momentum conservation equals <img class="latex" src="https://latex.codecogs.com/png.latex?\rho\dot{v}" title="Strong form of the momentum" />. To integrate over the domain, its weak form will result in the mass matrix:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}\dot{v}=\int_{\Omega}%20\phi_j%20\rho%20\dot{v}d\Omega" title="Mass integration" />

where <img class="latex" src="https://latex.codecogs.com/png.latex?\phi_j" title="Test function" /> are the test functions, which are basis functions ensuring the existence of a solution. Since no exact integration can be performed on a random domain <img class="latex" src="https://latex.codecogs.com/png.latex?\Omega" title="Random domain" />, the MeshMatrixMass relies on the Finite Element Method (FEM) and accumulates the result of the integral over each finite element (triangles, quads, tetrahedra or hexahedra):

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}\dot{v}=\sum_{e=0}^E%20\int_{V_e}%20\phi_j%20\rho%20\dot{v}dV_e" title="Mass integration" />

The FEM relies on simple geometries in which any field can be interpolated using shape functions <img class="latex" src="https://latex.codecogs.com/png.latex?\phi_i" title="Shape functions" /> (see [FEM at a glance](https://www.sofa-framework.org/community/doc/main-principles/multi-model-representation/physics-integration/#fem-at-a-glance)). Note that the same basis functions are chosen for both the test and the shape functions. The interpolation of the acceleration term <img class="latex" src="https://latex.codecogs.com/png.latex?\dot{v}" title="Acceleration term" /> thus gives:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}\dot{v}=\sum_{e=0}^E%20\rho%20\int_{V_e}%20\phi_j%20\sum_{i=0}^{N}%20\phi_i%20\dot{v}_i%20dV_e" title="Mass integration" />

By change of variables, the computation of the mass matrix results in solving the following integration of the shape functions <img class="latex" src="https://latex.codecogs.com/png.latex?\phi" title="Shape function" /> in each element:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}\dot{v}=\sum_{e=0}^E%20\rho%20\int_{V_e}%20|det(J)|%20\sum_{i=0}^{N}\phi_j(\boldsymbol{\xi})%20\phi_i(\boldsymbol{\xi})%20\dot{v}_i%20d%20\boldsymbol{\xi}" title="Mass integration" />


### Case of a linear tetrahedron
In the case of a linear tetrahedron, the shape functions are:

<img class="latex" src="https://latex.codecogs.com/png.latex?\begin{align*}&\phi_1=1-\xi%20-\eta%20-\zeta%20\\&\phi_2=\xi%20\\&\phi_3=\eta%20\\&\phi_4=\zeta%20\\%20\end{align*}" title="Shape functions of a linear tetrahedron" />

By replacing the shape functions, we therefore obtain:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}\dot{v}=\sum_{e=0}^E%20\rho%20\int_{V_e}%20|det(J)|%20\phi_j%20\phi_i%20\dot{v}_i%20d%20\boldsymbol{\xi}" title="Mass integration in a tetrahedron" />

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}\dot{v}=\sum_{e=0}^E%20\rho%20\int_{V_e}%20|det(J)|%20\begin{bmatrix}\phi_1^2&\phi_1\phi_2&\phi_1\phi_3&\phi_1\phi_4%20\\\phi_2\phi_1&\phi_2^2&\phi_2\phi_3&\phi_2\phi_4%20\\\phi_3\phi_1&\phi_3\phi_2&\phi_3^2&\phi_3\phi_4%20\\\phi_4\phi_1&\phi_4\phi_2&\phi_4\phi_3&\phi_4^2%20\\%20\end{bmatrix}%20\begin{bmatrix}\dot{v}_1\\%20\dot{v}_2\\%20\dot{v}_3\\%20\dot{v}_4\\%20\end{bmatrix}%20d%20\boldsymbol{\xi}" title="Mass integration in a tetrahedron" />

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}\dot{v}=\sum_{e=0}^E%20\rho%20\int_{\xi}%20\int_{\eta}%20\int_{\zeta}%20|det(J)|%20\begin{bmatrix}(1-\xi%20-\eta%20-\zeta)^2&\xi-\xi^2%20-\eta\xi%20-\zeta\xi&\eta-\xi\eta%20-\eta^2%20-\zeta\eta&\zeta-\xi\zeta%20-\eta\zeta\zeta%20-\zeta^2%20\\\phi_2\phi_1&\xi^2&\xi\eta&\xi\zeta%20\\\phi_3\phi_1&\phi_3\phi_2&\eta^2&\eta\zeta%20\\\phi_4\phi_1&\phi_4\phi_2&\phi_4\phi_3&\zeta^2%20\\%20\end{bmatrix}%20\begin{bmatrix}\dot{v}_1\\%20\dot{v}_2\\%20\dot{v}_3\\%20\dot{v}_4\\%20\end{bmatrix}%20d\xi%20d\eta%20d\zeta" title="Mass integration in a tetrahedron" />

We can note that the matrix is symmetric. The integration in the reference (or parent) space <img class="latex" src="https://latex.codecogs.com/png.latex?\boldsymbol{\xi}" title="Reference coordinates" /> can be numerically computed using a [Gauss quadrature](https://en.wikipedia.org/wiki/Gaussian_quadrature) (or Gauss point integration). The resulting mass matrix is:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}\dot{v}=\sum_{e=0}^E%20\frac{\rho%20V_e}{20}\begin{bmatrix}2&1&1&1\\1&2&1&1\\1&1&2&1\\1&1&1&2\\%20\end{bmatrix}\begin{bmatrix}\dot{v}_1\\%20\dot{v}_2\\%20\dot{v}_3\\%20\dot{v}_4\\%20\end{bmatrix}" title="Mass integration" />


### API

Depending on the type of [LinearSolver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/linear-solvers/) used:

- for iterative solvers, the result of the multiplication between the mass matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}" title="Mass matrix" /> and an approximated solution is computed by the function:

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

- for direct solvers, the mass matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}" title="Mass matrix" /> is built by the function:

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


Data  
----

The MeshMatrixMass can be initialized using two different input data:

- **totalMass**: corresponding to the total mass of the object, which will be distributed over its volume taking into account the geometry
- **massDensity**: corresponding to the mass density used for the integration detailed above

Note that using the optional data **lumping**, it is possible to simply the mass matrix by making it diagonal. This is called mass lumping and it consists in summing all mass values of a line on the diagonal. The DiagonalMass is an optimized version of this mass lumping approach. In case of a linear tetrahedron, if the data **lumping** is true, the (lumped) mass matrix becomes:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}\dot{v}=\sum_{e=0}^E%20\frac{\rho%20V_e}{4}\begin{bmatrix}1&0&0&0\\%30&1&0&0\\%30&0&1&0\\%30&0&0&1\\%20\end{bmatrix}\begin{bmatrix}\dot{v}_1\\%20\dot{v}_2\\%20\dot{v}_3\\%20\dot{v}_4\\%20\end{bmatrix}" title="Mass integration" />

Use lumping with caution since it is a numerical approximation, thus decreasing the accuracy of the integration.



Usage
-----

The MeshMatrixMass **requires** a MechanicalObject to store the degrees of freedom associated to the nodes, as well as a Topology. An integration scheme and a solver are also necessary to solve the linear system at each time step.

Several topologies are handled by the MeshMatrixMass, namely: triangles, quads, tetrahedra or hexahedra. Only the beam model (edge topology) is not handled by this component.



Example
-------

This component is used as follows in XML format:

``` xml
<MeshMatrixMass massDensity="1000" />
```

or using SofaPython3:

``` python
node.addObject('MeshMatrixMass', massDensity='1000')
```

An example scene involving a MeshMatrixMass is available in [*examples/Components/mass/MeshMatrixMass.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/mass/MeshMatrixMass.scn)