FixedProjectiveConstraint
=========================

This component belongs to the category of [Projective Constraint](../../../../simulation-principles/constraint/projective-constraint/).
The FixedProjectiveConstraint projects a constant velocity.  If the fixed points have a zero velocity at the simulation start, they will keep a zero velocity i.e. be fixed.

As introduced in the page about the Projective Constraint, the FixedProjectiveConstraint corresponds to a projection matrix noted $$\mathbf{P}$$ which will multiply the system matrix $$\mathbf{A}$$ so that: $$\mathbf{P}^T\mathbf{A}\mathbf{P}\Deltav=\mathbf{P}^Tb$$. This projection matrix $$\mathbf{P}$$ is the identity matrix in which the diagonal value corresponding to the indices of the fixed points equals zero. These lines and columns equals 0. As a consequence, when the integration scheme (ODESolver) will call the ```projectResponse()``` or ```projectVelocity()``` the constraint will be applied, ensuring that the desired degrees of freedom remain fixed.

Example of a system of size 6, with a fixed constraint at the index 5:

$$\mathbf{P}=\begin{bmatrix}1&0&0&0&0&0\\0&1&0&0&0&0\\0&0&1&0&0&0\\0&0&0&1&0&0\\0&0&0&0&\mathbf{0}&0\\0&0&0&0&0&1\end{bmatrix}$$

By projecting this $$\mathbf{P}$$ matrix on the right hand side vector we have $$\mathbf{P}^Tb$$. This ensures to have the projection $$b[5]=0$$, thus preventing any time evolution of the fifth degree of freedom. In such case, we function _projectResponse()_:

```cpp
template <class DataTypes>
void FixedProjectiveConstraint<DataTypes>::projectResponse(const core::MechanicalParams* mparams, DataVecDeriv& resData)
{
    SOFA_UNUSED(mparams);

    helper::WriteAccessor<DataVecDeriv> res (resData );
    const SetIndexArray & indices = d_indices.getValue();

    if( d_fixAll.getValue() )
    {
        // fix everything
        typename VecDeriv::iterator it;
        for( it = res.begin(); it != res.end(); ++it )
        {
            *it = Deriv();
        }
    }
    else
    {
        for (SetIndexArray::const_iterator it = indices.begin(); it != indices.end(); ++it)
        {
            res[*it] = Deriv();
        }
    }
}
```



Usage
-----

The FixedProjectiveConstraint **requires** a MechanicalObject to store the degrees of freedom associated to the nodes, as well as a Mass so that the system matrix is not null. An integration scheme and a solver are also necessary to solve the linear system at each time step.

Note that if only a part of the degrees of freedom must be constraint, you can use the PartialFixedProjectiveConstraint working in the same way as the FixedProjectiveConstraint.

