ForceField
==========

ForceFields are components that are adding "forces". These forces will influence the equilibrium of a system by contributing to its change of state.

In continuum mechanics, these forces can be either internal or external forces. Internal forces corresponds to the effect of the soft body mechanics (elasticity, plasticity etc) and the external forces arise from external phenomenon (gravity, pressure etc). As detailed in the page [Physics Integration](./../physics-integration/), the conservation of linear momentum in its generalized form can be written:

$$\rho \dot{v}=\rho \boldsymbol{b}+\nabla \cdot \boldsymbol{\sigma}$$

The analogy can be done on other physics. In thermodynamics, all thermal effects (like diffusion, blood heat, metabolic heat, etc.) of the bioheat equation can be considered as ForceFields as well since these terms appear in the equilibrium:

$$\rho c\dot{T}=\nabla \cdot k\nabla T+\rho_{b}c_{b}w(T_a-T)+Q_m$$




ForceField API
--------------

To explain the API associated to the ForceField, we will consider the system resulting from the conservation of linear momentum (mechanics):

$$\mathbf{M}\Delta{v}=dt \cdot f(x)$$

where $$x$$ is the position (degrees of freedom), $$v$$ is the velocity (derivative in time of the degrees of freedom) and $$\mathbf{M}$$ is the mass matrix.

As it is explained in the section [Integration Scheme](../../system-resolution/integration-scheme/), the choice of the temporal scheme will influence the way the linear system $$\mathbf{A}x=b$$ is built.


### Explicit force

Using an [explicit scheme](../../../components/odesolver/forward/eulerexplicitsolver/) means that forces $$f(x)$$ are computed using the degrees of freedom of the current time step $$t$$ (which are known): $$f(x)=f(x(t))$$. Regardless the form of the function $$f$$, the value of $$f(x(t))$$ can directly be obtained and set in the right hand side vector $$b$$ of our linear system $$\mathbf{A}x=b$$.

The computation of the term $$f$$, the value of $$dt\cdot f(x(t))$$ is done through the function `addForce()` of the ForceField class, called by the integration scheme (ODESolver).



### Implicit force


Using an [implicit scheme](../../../components/odesolver/backward/eulerimplicitsolver/) means that forces $$f(x)$$ are computed using the degrees of freedom of the next time step $$t+dt$$ (unknown yet): $$f(x)=f(x(t+dt))$$.
The value of $$f(x(t))$$ can not be directly be computed. By using a Taylor expansion, we get:

$$\mathbf{M} \Delta v=dt \cdot \left( f(x(t)+\cdot \frac{\partial f}{\partial x} \Delta x \right)$$
since we have: $$\Delta x=dt(v(t)+\Delta v)$$, then:
$$\mathbf{M}\Delta v=dt\cdot \left( f(x(t)+dt\cdot \frac{\partial f}{\partial x}v(t)+dt\cdot \frac{\partial f}{\partial x} \Delta v \right)$$

Finally, gathering the unknown (depending on $$\Delta v$$) in the left hand side, we have:
$$\left( \mathbf{M}-dt^2 \cdot \frac{\partial f}{\partial x} \right) \Delta v=dt\cdot f(x(t)+dt^2\cdot \frac{\partial f}{\partial x}v(t)$$

We can notice the appearance of the stiffness matrix : $$\mathbf{K}_{ij}=\textstyle\frac{\partial f_i}{\partial x_j}$$. The stiffness matrix $$\mathbf{K}$$ is a symmetric matrix, can either be linear or non-linear regarding $$x$$.


For the **right hand side**:

- the term $$dt\cdot f(x(t)$$ is computed by the function: `addForce()` (as in explicit case)
- the term $$dt^2\cdot \frac{\partial f}{\partial x}v(t)$$ is computed by the function: `addDForce()`


For the **left hand side**, the API used to compute it depends on the type of [Integration Scheme](../../system-resolution/integration-scheme/) used: direct (the system matrix $$\mathbf{A}$$ is built and inversed) or iterative (unbuilt approach). We have:

$$\mathbf{A}=\left( M-dt^2 \cdot \frac{\partial f}{\partial x} \right)$$

- for iterative solvers, the term $$-dt^2 \cdot \frac{\partial f}{\partial x}$$ is computed by the function: `addDForce()`
- for direct solvers, the term $$dt^2\cdot \frac{\partial f}{\partial x}v(t)$$ is computed by the function: `addKToMatrix()`



### Summary

For explicit case, we have:

| Linear solver | $$dt \cdot f(x(t))$$ |
|:-------------:|:-------------------------------------------------------------------------------------------------------------:|
| **Iterative** |                                                 `addForce()`                                                  | 
|  **Direct**   |                                                 `addForce()`                                                  | 

For implicit case, we have:

| Linear solver | $$-dt^2 \cdot \textstyle\frac{\partial f}{\partial x}\Delta v$$ | $$dt \cdot f(x(t))$$ | $$dt^2\textstyle\frac{\partial f}{\partial x}v(t)$$ |
|:-------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------:|
| **Iterative** |                                                                           `addDForce()`                                                                           |                                                 `addForce()`                                                  |                                                                  `addDForce()`                                                                  |
|  **Direct**   |                                                                         `addKToMatrix()`                                                                          |                                                 `addForce()`                                                  |                                                                  `addDForce()`                                                                  |


ForceField implementations
--------------------------

See examples of ForceField implementation:

- [ConstantForceField](../../../components/mechanicalload/constantforcefield/)
- [TetrahedronFEMForceField](../../../components/solidmechanics/fem/elasticity/tetrahedronfemforcefield/)



Template of a ForceField
------------------------

TemplateForceField.h : declares the variable, the Data and the functions of the class

``` cpp
/******************************************************************************
*       SOFA, Simulation Open-Framework Architecture, development version     *
*                (c) 2006-2019 INRIA, USTL, UJF, CNRS, MGH                    *
*                                                                             *
* This program is free software; you can redistribute it and/or modify it     *
* under the terms of the GNU Lesser General Public License as published by    *
* the Free Software Foundation; either version 2.1 of the License, or (at     *
* your option) any later version.                                             *
*                                                                             *
* This program is distributed in the hope that it will be useful, but WITHOUT *
* ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or       *
* FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License *
* for more details.                                                           *
*                                                                             *
* You should have received a copy of the GNU Lesser General Public License    *
* along with this program. If not, see <http://www.gnu.org/licenses/>.        *
*******************************************************************************
* Authors: The SOFA Team and external contributors (see Authors.txt)          *
*                                                                             *
* Contact information: contact@sofa-framework.org                             *
******************************************************************************/
#ifndef SOFA_COMPONENT_FORCEFIELD_TEMPLATEFORCEFIELD_H
#define SOFA_COMPONENT_FORCEFIELD_TEMPLATEFORCEFIELD_H

#include "config.h"
#include <sofa/core/behavior/ForceField.h>

namespace sofa
{

namespace component
{

namespace forcefield
{

/// Apply constant forces to given degrees of freedom.
template<class DataTypes>
class TemplateForceField : public core::behavior::ForceField<DataTypes>
{

public:

    SOFA_CLASS(SOFA_TEMPLATE(TemplateForceField, DataTypes), SOFA_TEMPLATE(core::behavior::ForceField, DataTypes));

    /// Declare here the data and their type, you want the user to have access to
    Data< int > d_inputForTheUser;

    /// Function responsible for the initialization of the component
    void init() override;

    /// Add the explicit forces (right hand side)
    void addForce (const core::MechanicalParams* params, DataVecDeriv& f, const DataVecCoord& x, const DataVecDeriv& v) override;

    /// Add the explicit derivatives of the forces (contributing to the right hand side vector b)
    /// IF iterative solver: add the implicit derivatives of the forces (contributing to the left hand side matrix A)
    void addDForce(const core::MechanicalParams* mparams, DataVecDeriv& d_df , const DataVecDeriv& d_dx) override;

    /// IF direct solver: add the implicit derivatives of the forces (contributing to the left hand side matrix A)
    void buildStiffnessMatrix(core::behavior::StiffnessMatrix* matrix) override;

    /// Same as previous, but using accessor
    void addKToMatrix(const sofa::core::behavior::MultiMatrixAccessor* /*matrix*/, SReal /*kFact*/) ;

    SReal getPotentialEnergy(const core::MechanicalParams* params, const DataVecCoord& x) const override;

protected:

    TemplateForceField();
    ~TemplateForceField();

};


#if  !defined(SOFA_COMPONENT_FORCEFIELD_TEMPLATEFORCEFIELD_CPP)
extern template class SOFA_BOUNDARY_CONDITION_API TemplateForceField<sofa::defaulttype::Vec3Types>;
extern template class SOFA_BOUNDARY_CONDITION_API TemplateForceField<sofa::defaulttype::Vec2Types>;
extern template class SOFA_BOUNDARY_CONDITION_API TemplateForceField<sofa::defaulttype::Vec1Types>;
extern template class SOFA_BOUNDARY_CONDITION_API TemplateForceField<sofa::defaulttype::Vec6Types>;
#endif


} // namespace forcefield

} // namespace component

} // namespace sofa

#endif // SOFA_COMPONENT_FORCEFIELD_TEMPLATEFORCEFIELD_H

```



TemplateForceField.inl : implements the functions of the class

``` cpp
/******************************************************************************
*       SOFA, Simulation Open-Framework Architecture, development version     *
*                (c) 2006-2019 INRIA, USTL, UJF, CNRS, MGH                    *
*                                                                             *
* This program is free software; you can redistribute it and/or modify it     *
* under the terms of the GNU Lesser General Public License as published by    *
* the Free Software Foundation; either version 2.1 of the License, or (at     *
* your option) any later version.                                             *
*                                                                             *
* This program is distributed in the hope that it will be useful, but WITHOUT *
* ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or       *
* FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License *
* for more details.                                                           *
*                                                                             *
* You should have received a copy of the GNU Lesser General Public License    *
* along with this program. If not, see <http://www.gnu.org/licenses/>.        *
*******************************************************************************
* Authors: The SOFA Team and external contributors (see Authors.txt)          *
*                                                                             *
* Contact information: contact@sofa-framework.org                             *
******************************************************************************/
#ifndef SOFA_COMPONENT_FORCEFIELD_TEMPLATEFORCEFIELD_INL
#define SOFA_COMPONENT_FORCEFIELD_TEMPLATEFORCEFIELD_INL

#include <SofaBoundaryCondition/TemplateForceField.h>
#include <sofa/helper/system/config.h>

namespace sofa
{

namespace component
{

namespace forcefield
{


// Constructor of the class TemplateForceField
// initializing data with their default value (here d_inputForTheUser=20)
template<class DataTypes>
TemplateForceField<DataTypes>::TemplateForceField()
    : d_inputForTheUser(initData(&d_inputForTheUser, (int) 20, "inputForTheUser", "Description of the data inputForTheUser"))
{
}


template<class DataTypes>
TemplateForceField<DataTypes>::~TemplateForceField()
{
}


template<class DataTypes>
void TemplateForceField<DataTypes>::init()
{
    // Initialization of your ForceField class and variables
}


template<class DataTypes>
void TemplateForceField<DataTypes>::addForce(const core::MechanicalParams* /*params*/,
                                             DataVecDeriv& f, const DataVecCoord& p, const DataVecDeriv&)
{
    // Compute the forces f from the current DOFs p
}


template<class DataTypes>
void TemplateForceField<DataTypes>::addDForce(const core::MechanicalParams* mparams,
                                              DataVecDeriv& d_df , const DataVecDeriv& d_dx)
{
    // Compute the force derivative d_df from the current, which will be multiplied with the field d_dx
}


template<class DataTypes>
void TemplateForceField<DataTypes>::buildStiffnessMatrix(core::behavior::StiffnessMatrix* matrix)
{
    // Compute the force derivative d_df from the current and store the resulting matrix
}


template <class DataTypes>
SReal TemplateForceField<DataTypes>::getPotentialEnergy(const core::MechanicalParams* /*params*/,
                                                        const DataVecCoord& x) const
{
    // Compute the potential energy associated to the force f
}




} // namespace forcefield

} // namespace component

} // namespace sofa

#endif // SOFA_COMPONENT_FORCEFIELD_TEMPLATEFORCEFIELD_INL

```



TemplateForceField.cpp : declares the different templates used for this ForceField (DataType)

``` cpp
/******************************************************************************
*       SOFA, Simulation Open-Framework Architecture, development version     *
*                (c) 2006-2019 INRIA, USTL, UJF, CNRS, MGH                    *
*                                                                             *
* This program is free software; you can redistribute it and/or modify it     *
* under the terms of the GNU Lesser General Public License as published by    *
* the Free Software Foundation; either version 2.1 of the License, or (at     *
* your option) any later version.                                             *
*                                                                             *
* This program is distributed in the hope that it will be useful, but WITHOUT *
* ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or       *
* FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License *
* for more details.                                                           *
*                                                                             *
* You should have received a copy of the GNU Lesser General Public License    *
* along with this program. If not, see <http://www.gnu.org/licenses/>.        *
*******************************************************************************
* Authors: The SOFA Team and external contributors (see Authors.txt)          *
*                                                                             *
* Contact information: contact@sofa-framework.org                             *
******************************************************************************/
#define SOFA_COMPONENT_FORCEFIELD_TEMPLATEFORCEFIELD_CPP

namespace sofa
{

namespace component
{

namespace forcefield
{

using namespace sofa::defaulttype;


// Give a description of your class
// and declare the DataTypes on which the ForceField is instantiated

int TemplateForceFieldClass = core::RegisterObject("Description here of the physics of your ForceField")
        .add< TemplateForceFieldClass<Vec3Types> >()
        .add< TemplateForceFieldClass<Vec2Types> >()
        .add< TemplateForceFieldClass<Vec1Types> >()
        .add< TemplateForceFieldClass<Vec6Types> >()

        ;

template class TemplateForceField<Vec3Types>;
template class TemplateForceField<Vec2Types>;
template class TemplateForceField<Vec1Types>;
template class TemplateForceField<Vec6Types>;



} // namespace forcefield

} // namespace component

} // namespace sofa

```
