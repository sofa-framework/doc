DataTypes
=========

As you may know, many SOFA C++ classes are templated. Examples of templates can be found in the [MechanicalObject page](https://www.sofa-framework.org/community/doc/simulation-principles/mechanicalobject/), in the [templates section](https://www.sofa-framework.org/community/doc/simulation-principles/mechanicalobject/#templates). In the code, the use of templates implies the many types in the C++ variable, that are not always easy to understand. This page provides a short introduction to all these types.

All following types are defined from the DataTypes class, and can therefore be used by writing: **DataTypes::MyType**.

**Real**: corresponds to a double or float value, depending on the DataTypes used: a class templated in Vec3d will return a double, whereas a a class templated in Vec3f will return a float

**Coord**: standing for "coordinate", corresponds to a vector of _Real_ with a size given by the number of degrees of freedom: a class templated in Vec6d will return a vector of 6 doubles. This vector is homogeneous to your degrees of freedom.

**Deriv** standing for "derivative", corresponds to a vector of _Real_ with a size given by the number of degrees of freedom: a class templated in Vec6d will return a vector of 6 doubles

**VecCoord** or **VecDeriv**: corresponds to a vector of respectively _Coord_ or _Deriv_

**DataVecCoord or DataVecDeriv**: corresponds to a [Data](https://www.sofa-framework.org/community/doc/main-principles/scene-graph/#data) containing a vector of respectively _Coord_ or _Deriv_. As noted in the assocaited article, the Data are variable of the class exposed to the user and other components in the scene

**MatrixCoord or MatrixDeriv**: corresponds to a matrix of respectively _Coord_ or _Deriv_, this is more especially used by solvers and constraint algorithms

**VecCoordId, VecDerivId, MatrixCoordId or MatrixDerivId**: corresponds to an identifiant value (int) pointing to a vector or matrix of respectively _Coord_ or _Deriv_. This is very useful to access specific vectors or matrix in the simulation. [State vectors](https://www.sofa-framework.org/community/doc/simulation-principles/mechanicalobject/#state-vectors) for instance are managed with specific protected Ids by the solvers.