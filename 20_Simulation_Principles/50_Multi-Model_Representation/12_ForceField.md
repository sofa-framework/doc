ForceField
==========

ForceFields are components that are adding "forces". These forces will influence the equilibrium of a system by contributing to its change of state.

In continuum mechanics, these forces can be either internal or external forces. Internal forces corresponds to the effect of the soft body mechanics (elasticity, plasticity etc) and the external forces arise from external phenomenon (gravity, pressure etc). As detailed in the page [Physics Integration](https://www.sofa-framework.org/community/doc/main-principles/multi-model-representation/physics-integration/), the conservation of linear momentum in its generalized form can be written:

<img class="latex" src="https://latex.codecogs.com/png.latex?\rho%20\dot{v}=\rho%20\boldsymbol{b}+\nabla%20\cdot%20\boldsymbol{\sigma}" title="Dynamic differential equation with internal and external forces (strong form)" />

The analogy can be done on other physics. In thermodynamics, all thermal effects (like diffusion, blood heat, metabolic heat, etc.) of the bioheat equation can be considered as ForceFields as well since these terms appear in the equilibrium:

<img class="latex" src="https://latex.codecogs.com/png.latex?\rho%20c\dot{T}=\nabla%20\cdot%20k\nabla%20T+\rho_{b}c_{b}w(T_a-T)+Q_m" title="Dynamic bio-heat equation" />




ForceField API
--------------

To explain the API associated to the ForceField, we will consider the system resulting from the conservation of linear momentum (mechanics):

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}\Delta{v}=dt%20\cdot%20f(x)" title="Dynamic mechanical system" />

where <img class="latex" src="https://latex.codecogs.com/png.latex?x" title="Position" /> is the position (degrees of freedom), <img class="latex" src="https://latex.codecogs.com/png.latex?v" title="Velocity" /> is the velocity (derivative in time of the degrees of freedom) and <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}" title="Mass matrix" /> is the mass matrix.

As it is explained in the section [Integration Scheme](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/integration-schemes/), the choice of the temporal scheme will influence the way the linear system <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="Linear system" /> is built.


### Explicit force

Using an [explicit scheme](https://www.sofa-framework.org/community/doc/using-sofa/components/integrationscheme/eulerexplicitsolver/) means that forces <img class="latex" src="https://latex.codecogs.com/png.latex?f(x)" title="Forces" /> are computed using the degrees of freedom of the current time step <img class="latex" src="https://latex.codecogs.com/png.latex?t" title="Current time" /> (which are known): <img class="latex" src="https://latex.codecogs.com/png.latex?f(x)=f(x(t))" title="Explicit forces" />. Regardless the form of the function <img class="latex" src="https://latex.codecogs.com/png.latex?f" title="Forces" />, the value of <img class="latex" src="https://latex.codecogs.com/png.latex?f(x(t))" title="Explicit forces" /> can directly be obtained and set in the right hand side vector <img class="latex" src="https://latex.codecogs.com/png.latex?b" title="RHS vector" />  of our linear system <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="Linear system" />.

The computation of the term <img class="latex" src="https://latex.codecogs.com/png.latex?f" title="Forces" />, the value of <img class="latex" src="https://latex.codecogs.com/png.latex?dt\cdot%20f(x(t))" title="Explicit forces" /> is done through the function `addForce()` of the ForceField class, called by the integration scheme (ODESolver).



### Implicit force


Using an [implicit scheme](https://www.sofa-framework.org/community/doc/using-sofa/components/integrationscheme/eulerimplicitsolver/) means that forces <img class="latex" src="https://latex.codecogs.com/png.latex?f(x)" title="Forces" /> are computed using the degrees of freedom of the next time step <img class="latex" src="https://latex.codecogs.com/png.latex?t+dt" title="Current time" /> (unknown yet): <img class="latex" src="https://latex.codecogs.com/png.latex?f(x)=f(x(t+dt))" title="Explicit forces" />.
The value of <img class="latex" src="https://latex.codecogs.com/png.latex?f(x(t))" title="Explicit forces" /> can not be directly be computed. By using a Taylor expansion, we get:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}%20\Delta%20v=dt%20\cdot%20\left(%20f(x(t)+\cdot%20\frac{\partial%20f}{\partial%20x}%20\Delta%20x%20\right)" title="Implicit dynamic system" />

since we have: <img class="latex" src="https://latex.codecogs.com/png.latex?\Delta%20x=dt(v(t)+\Delta%20v)" title="Implicit scheme" />, then:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}\Delta%20v=dt\cdot%20\left(%20f(x(t)+dt\cdot%20\frac{\partial%20f}{\partial%20x}v(t)+dt\cdot%20\frac{\partial%20f}{\partial%20x}%20\Delta%20v%20\right)" title="Implicit dynamic system" />

Finally, gathering the unknown (depending on <img class="latex" src="https://latex.codecogs.com/png.latex?\Delta%20v" title="Unknown delta of velocity" />) in the left hand side, we have:

<img class="latex" src="https://latex.codecogs.com/png.latex?\left(%20\mathbf{M}-dt^2%20\cdot%20\frac{\partial%20f}{\partial%20x}%20\right)%20\Delta%20v=dt\cdot%20f(x(t)+dt^2\cdot%20\frac{\partial%20f}{\partial%20x}v(t)" title="Implicit dynamic system" />

We can notice the appearance of the stiffness matrix : <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{K}_{ij}=\textstyle\frac{\partial%20f_i}{\partial%20x_j}" title="Implicit contribution" />. The stiffness matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{K}" title="Stiffness matrix" /> is a symetric matrix, can either be linear or non-linear regarding <img class="latex" src="https://latex.codecogs.com/png.latex?x" title="DOF" />.


For the **right hand side**:

- the term <img class="latex" src="https://latex.codecogs.com/png.latex?dt\cdot%20f(x(t)" title="Explicit forces" /> is computed by the function: `addForce()` (as in explicit case)

- the term <img class="latex" src="https://latex.codecogs.com/png.latex?dt^2\cdot%20\frac{\partial%20f}{\partial%20x}v(t)" title="Derivative explicit forces" /> is computed by the function: `addDForce()`


For the **left hand side**, the API used to compute it depends on the type of [Integration Scheme](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/integration-schemes/) used: direct (the system matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> is built and inversed) or iterative (unbuilt approach). We have:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}=\left(%20M-dt^2%20\cdot%20\frac{\partial%20f}{\partial%20x}%20\right)" title="System matrix" />

- for iterative solvers, the term <img class="latex" src="https://latex.codecogs.com/png.latex?-dt^2%20\cdot%20\frac{\partial%20f}{\partial%20x}" title="Derivative implicit forces" /> is computed by the function: `addDForce()` 

- for direct solvers, the term <img class="latex" src="https://latex.codecogs.com/png.latex?dt^2\cdot%20\frac{\partial%20f}{\partial%20x}v(t)" title="Derivative forces" /> is computed by the function: `addKToMatrix()`



### Summary

For explicit case, we have:

<center>

| Linear solver | <img class="latex" src="https://latex.codecogs.com/png.latex?dt%20\cdot%20f(x(t))" title="Explicit forces" /> |
|:-------------:|:------------:|
| **Iterative** | `addForce()` | 
| **Direct**    | `addForce()` | 

</center>

For implicit case, we have:

<center>

| Linear solver | <img class="latex" src="https://latex.codecogs.com/png.latex?-dt^2%20\cdot%20\textstyle\frac{\partial%20f}{\partial%20x}\Delta%20v" title="Implicit stiffness" /> | <img class="latex" src="https://latex.codecogs.com/png.latex?dt%20\cdot%20f(x(t))" title="Explicit forces" /> | <img class="latex" src="https://latex.codecogs.com/png.latex?dt^2\textstyle\frac{\partial%20f}{\partial%20x}v(t)" title="Explicit stiffness" /> |
|:-------------:|:--------------:|:--------------:|:----------:|:-----------:|
| **Iterative** | `addDForce()`    | `addForce()` | `addDForce()` |
| **Direct**    | `addKToMatrix()` | `addForce()` | `addDForce()` |

</center>




ForceField implementations
--------------------------

See examples of ForceField implementation:

- [ConstantForceField](https://www.sofa-framework.org/community/doc/using-sofa/components/forcefield/constantforcefield/)
- [TetrahedronFEMForceField](https://www.sofa-framework.org/community/doc/using-sofa/components/forcefield/tetrahedronfemforcefield/)



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
    void addKToMatrix(sofa::defaulttype::BaseMatrix *m, SReal kFactor, unsigned int &offset) override;

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
void TemplateForceField<DataTypes>::addKToMatrix(sofa::defaulttype::BaseMatrix * /* mat */,
                                                 SReal /* k */, unsigned int & /* offset */)
{
    // Compute the force derivative d_df from the current and store the resulting matrix
}


template<class DataTypes>
void TemplateForceField<DataTypes>::addKToMatrix(const sofa::core::behavior::MultiMatrixAccessor* /*matrix*/,
                                                 SReal /*kFact*/)
{
    // Same as previously
    // but using accessor
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