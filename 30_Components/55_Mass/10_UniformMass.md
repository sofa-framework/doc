UniformMass  
===========


This component belongs to the category of [Masses](../../simulation-principles/multi-model-representation/mass/). The UniformMass is a very **simplistic mass** component since it does not compute the volume integration of a density term. The mass is equally spread over the number of points, thus resulting in the following diagonal mass matrix:

$$\mathbf{M}=\begin{bmatrix}m&0&\cdots&0\\&m&\cdots&0\\%20\vdots&\vdots&\ddots&\vdots\\&0&\cdots&m\end{bmatrix}$$

Each diagonal term equals the nodal mass $$m=\frac{m_{\textnormal{total}}}{N}$$ where $$m_{\textnormal{total}}$$ is the total mass of the objet and $$N$$ is the number of nodes of the object. Spreading the mass over the nodes without considering their connectivity results in this diagonal mass matrix $$\mathbf{M}$$.


As all mass components, the UniformMass $$\mathbf{M}$$ will contribute to the main matrix $$\mathbf{A}$$ in the system $$\mathbf{A}x=b$$. Depending on the type of [LinearSolver](../../simulation-principles/system-resolution/linear-solver/) used:

- for iterative solvers, the result of the multiplication between the mass matrix $$\mathbf{M}$$ and an approximated solution is computed by the function:

``` cpp
template <class DataTypes, class MassType>
void UniformMass<DataTypes, MassType>::addMDx ( const core::MechanicalParams*, DataVecDeriv& vres, const DataVecDeriv& vdx, SReal factor)
{
    helper::WriteAccessor<DataVecDeriv> res = vres;
    helper::ReadAccessor<DataVecDeriv> dx = vdx;

    WriteAccessor<Data<vector<int> > > indices = d_indices;

    MassType m = d_vertexMass.getValue();
    if ( factor != 1.0 )
        m *= ( typename DataTypes::Real ) factor;

    for ( unsigned int i=0; i<indices.size(); i++ )
        res[indices[i]] += dx[indices[i]] * m;
}
```

- for direct solvers, the mass matrix $$\mathbf{M}$$ is built by the function:

``` cpp
/// Add Mass contribution to global Matrix assembling
template <class DataTypes, class MassType>
void UniformMass<DataTypes, MassType>::addMToMatrix (const MechanicalParams *mparams, const MultiMatrixAccessor* matrix)
{
    const MassType& m = d_vertexMass.getValue();

    const size_t N = DataTypeInfo<Deriv>::size();

    AddMToMatrixFunctor<Deriv,MassType> calc;
    MultiMatrixAccessor::MatrixRef r = matrix->getMatrix(mstate);

    Real mFactor = (Real)mparams->mFactorIncludingRayleighDamping(this->rayleighMass.getValue());

    ReadAccessor<Data<vector<int> > > indices = d_indices;
    for ( unsigned int i=0; i<indices.size(); i++ )
        calc ( r.matrix, m, r.offset + N*indices[i], mFactor);
}
```


Usage
-----

The UniformMass only **requires** a MechanicalObject to store the degrees of freedom associated to the nodes. An integration scheme and a solver are also necessary to solve the linear system at each time step.

Since the UniformMass only set a constant mass at each node without considering their connectivity, no topology is needed for the UniformMass. For this reason, the UniformMass is suitable for rigid frames.

However, the UniformMass should be carefully used if accuracy is a criterion, especially when using surface or volumetric physical models. As written above, the UniformMass does not take into account the geometry and the topology of the object since no space integration is computed.

