DataTypes
=========

As you may know, many SOFA C++ classes are templated, mostly on the type of DOF you want to simulate. Examples of templates can be found in the [MechanicalObject page](https://www.sofa-framework.org/community/doc/simulation-principles/mechanicalobject/), in the [templates section](https://www.sofa-framework.org/community/doc/simulation-principles/mechanicalobject/#templates). In the code, the use of templates can be confusing, especially when the type used in place of the template has itself many types. This page provides a short introduction to all these DOF types.

All DOF Types must implement (or define) all the following types:

- **Real**: corresponds to a double or float value, depending on the DataTypes used: a class templated in Vec3d will return a double, whereas a a class templated in Vec3f will return a float

- **Coord**: standing for "coordinate", corresponds to a vector of _Real_ with a size given by the number of degrees of freedom: a class templated in Vec6d will return a vector of 6 doubles. This vector is homogeneous to your degrees of freedom.

- **Deriv** standing for "derivative", corresponds to a vector of _Real_ with a size given by the number of degrees of freedom: a class templated in Vec6d will return a vector of 6 doubles

- **VecCoord** or **VecDeriv**: correspond to a vector of respectively _Coord_ or _Deriv_

- **DataVecCoord or DataVecDeriv**: correspond to a [Data](../../simulation-principles/scene-graph/#data) containing a vector of respectively _Coord_ or _Deriv_. As noted in the associated article, the Data are variable of the class exposed to the user and other components in the scene

- **MatrixCoord or MatrixDeriv**: correspond to a matrix of respectively _Coord_ or _Deriv_, this is more especially used by solvers and constraint algorithms

- **VecCoordId, VecDerivId, MatrixCoordId or MatrixDerivId**: correspond to an identifiant value (int) pointing to a vector or matrix of respectively _Coord_ or _Deriv_. This is very useful to access specific vectors or matrix in the simulation. [State vectors](https://www.sofa-framework.org/community/doc/simulation-principles/mechanicalobject/#state-vectors) for instance are managed with specific protected Ids by the solvers.
