---
title: Mass
---

Mass
====

In simulation, the mass usually results from the volume integration of a density (see the [Physics Integration](./../physics-integration/) section). It can be a mass density, but it can be an electrical or electrical conductivity among others. In all these equations, the density appears on the left hand side part of the equation. The mass matrix therefore contributes to $$\mathbf{A}$$, in the linear System $$\mathbf{A}x=b$$.

Mass API
--------------

The choice of the temporal scheme will influence the way the linear system $$\mathbf{A}x=b$$ is built. As a consequence, it also impacts the API:

- for iterative solvers, the result of the multiplication between the mass matrix $$\mathbf{M}$$ and an approximated solution is computed by the function: `addMDx()`
- for direct solvers, the mass matrix $$\mathbf{M}$$ is built by the function: `addMToMatrix()` and will be used later when the system matrix will be inversed



Mass implementations
-------------------------

See examples of Mass implementation:

- [UniformMass](../../../components/mass/uniformmass/)
- [MeshMatrixMass](../../../components/mass/meshmatrixmass/)
- [DiagonalMass](../../../components/mass/diagonalmass/)


Template of a Mass
------------------


TemplateMass.h : declares the variable, the Data and the functions of the class

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
#ifndef SOFA_COMPONENT_MASS_TEMPLATEMASS_H
#define SOFA_COMPONENT_MASS_TEMPLATEMASS_H

#include "config.h"

namespace sofa
{

namespace component
{

namespace mass
{

template <class DataTypes, class TMassType>
class TemplateMass : public core::behavior::Mass<DataTypes>
{
public:
    SOFA_CLASS(SOFA_TEMPLATE2(TemplateMass,DataTypes,TMassType),
               SOFA_TEMPLATE(core::behavior::Mass,DataTypes));


    /// Declare here the data and their type, you want the user to have access to
    Data<SReal> d_massDensity;

    /// Function responsible for the initialization of the component
    void init() override;

    // IF iterative solver, compute the mass contribution and multiplies it with dx
    void addMDx(const core::MechanicalParams* mparams, DataVecDeriv& f, const DataVecDeriv& dx, SReal factor) override;

    // IF direct solver, compute the mass contribution to global Matrix assembling
    void buildMassMatrix(sofa::core::behavior::MassMatrixAccumulator* matrices) override;

    // Compute the acceleration resulting from the acc = F/M
    // in explicit cases, the solution can directly be found when the matrix is diagonal
    void accFromF(const core::MechanicalParams* mparams, DataVecDeriv& a, const DataVecDeriv& f) override;

    // Boolean function informing about the structure of the resulting mass matrix
    bool isDiagonal() override {return false;}

    // Compute the kinetic energy : vMv/2
    SReal getKineticEnergy(const core::MechanicalParams* mparams, const DataVecDeriv& d_v) const override;

    // Compute the potential energt Mgx in a uniform gravity field, null at origin
    SReal getPotentialEnergy(const core::MechanicalParams* mparams, const DataVecCoord& x) const override;

    // Compute the momentum induced by the mass inertia (Mv,cross(x,Mv)+Iw)
    defaulttype::Vector6 getMomentum(const core::MechanicalParams* mparams, const DataVecCoord& x, const DataVecDeriv& v) const override;

protected:

    TemplateMass();
    ~TemplateMass();

};



#if  !defined(SOFA_COMPONENT_MASS_TEMPLATEMASS_CPP)
extern template class TemplateMass<defaulttype::Vec3Types, double>;
extern template class TemplateMass<defaulttype::Vec2Types, double>;
extern template class TemplateMass<defaulttype::Vec1Types, double>;
extern template class TemplateMass<defaulttype::Vec6Types, double>;

#endif

} // namespace mass

} // namespace component

} // namespace sofa

#endif


```



TemplateMass.inl : implements the functions of the class

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
#ifndef SOFA_COMPONENT_MASS_TEMPLATEMASS_INL
#define SOFA_COMPONENT_MASS_TEMPLATEMASS_INL

#include "TemplateMass.h"

namespace sofa
{

namespace component
{

namespace mass
{

template <class DataTypes, class MassType>
TemplateMass<DataTypes, MassType>::TemplateMass()
    : d_massDensity ( initData ( &d_massDensity, SReal ( 1.0 ), "massDensity", "Description of the data" ) )
{
}

template <class DataTypes, class MassType>
TemplateMass<DataTypes, MassType>::~TemplateMass()
{
}

template <class DataTypes, class MassType>
void TemplateMass<DataTypes, MassType>::init()
{
    // Initialization of your TemplateMass class and variables
}


template <class DataTypes, class MassType>
void TemplateMass<DataTypes, MassType>::addMDx(const core::MechanicalParams* mparams, DataVecDeriv& f, const DataVecDeriv& dx, SReal factor)
{
    // Compute the multiplication of the mass matrix with the vector dx, save the result in the f vector
}

template <class DataTypes, class MassType>
void TemplateMass<DataTypes, MassType>::buildMassMatrix(sofa::core::behavior::MassMatrixAccumulator* matrices)
{
    // Build the mass matrix and store it in the system matrix
}

template <class DataTypes, class MassType>
void TemplateMass<DataTypes, MassType>::accFromF(const core::MechanicalParams* mparams, DataVecDeriv& a, const DataVecDeriv& f)
{
    // Compute the resulting a vector due to the division of the f vector by a (diagonal) mass matrix (vector)
}

template <class DataTypes, class MassType>
SReal TemplateMass<DataTypes, MassType>::getKineticEnergy(const core::MechanicalParams* mparams, const DataVecDeriv& d_v) const
{
    // Compute the kinetic energy
}

template <class DataTypes, class MassType>
SReal TemplateMass<DataTypes, MassType>::getPotentialEnergy(const core::MechanicalParams* mparams, const DataVecCoord& x) const
{
    // Compute the potential energy
}

template <class DataTypes, class MassType>
defaulttype::Vector6 TemplateMass<DataTypes, MassType>::getMomentum(const core::MechanicalParams* mparams, const DataVecCoord& x, const DataVecDeriv& v) const
{
    // Compute the momentum
}


} // namespace mass

} // namespace component

} // namespace sofa

#endif // SOFA_COMPONENT_MASS_TEMPLATEMASS_INL


```



TemplateMass.cpp : declares the different templates used for this ForceField (DataType)

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
#define SOFA_COMPONENT_MASS_TEMPLATEMASS_CPP

#include "TemplateMass.inl"
#include <sofa/defaulttype/VecTypes.h>
#include <sofa/defaulttype/RigidTypes.h>
#include <sofa/core/ObjectFactory.h>


using namespace sofa::defaulttype;

namespace sofa
{

namespace component
{

namespace mass
{


/// Registration to the factory
int TemplateMassClass = core::RegisterObject("Description of your TemplateMass class")

        .add< TemplateMass<Vec3Types,double> >()
        .add< TemplateMass<Vec2Types,double> >()
        .add< TemplateMass<Vec1Types,double> >()
        .add< TemplateMass<Vec6Types,double> >()

        ;



/// Template Initialization
/// Force template specialization for the most common SOFA type.
/// This goes with the extern template declaration in the .h. Declaring extern template
/// avoid the code generation of the template for each compilation unit

template class TemplateMass<Vec3Types,double>;
template class TemplateMass<Vec2Types,double>;
template class TemplateMass<Vec1Types,double>;
template class TemplateMass<Vec6Types,double>;


} // namespace mass

} // namespace component

} // namespace sofa

```