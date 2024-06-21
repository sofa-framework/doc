---
title: Projective Constraint
---

Projective constraint
=====================

Different types of constraint exist in SOFA. The projective constraint are method allowing to project the velocity of the constraint points of an object to a desired value.


Matrix approach
---------------

A projection matrix noted <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{P}" title="Projection matrix" /> multiplies the matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> of the linear system <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="Linear system" /> (where our unknown <img class="latex" src="https://latex.codecogs.com/png.latex?x" title="Unknown x" /> is actually <img class="latex" src="https://latex.codecogs.com/png.latex?\Delta{v}" title="Evolution of the first derivative" />) to enforce the so-called project constraint. The system thus becomes: <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{P}^T\mathbf{A}\mathbf{P}%20\Delta%20v=\mathbf{P}^Tb" title="Constrained system" />. Implicit integration has the advantage of being more stable for stiff forces or large time steps. The solution of these equation systems requires [linear solvers](https://www.sofa-framework.org/community/doc/simulation-principles/system-resolution/linear-solver/). Due to the superlinear time complexity of equation solvers, it is generally more efficient to process independent interaction groups using separated solvers rather than a unique solver.

Another type of constraints is available in SOFA focusing on constraint-based interactions which requires the computation of Lagrange multipliers based on interaction Jacobians. This will be discussed in the next article about [Lagrange constraint](https://www.sofa-framework.org/community/doc/main-principles/constraint/lagrange-constraint/).



API of projective constraint
----------------------------

In SOFA, you can find several of these projective constraints in the SofaBoundaryConditions module, among them:

  - the [_FixedConstraint_](https://www.sofa-framework.org/community/doc/components/constraints/fixedconstraint/): projecting a constant velocity, if the vertex is initially fixed, then it is attached to its initial position

  - the _PartialFixedConstraint_: inheriting from _FixedConstraint_, this constraint is projected only along certain degrees of freedom (e.g. only in x direction)

Classes considering on single object inherit from the class _ProjectiveConstraintSet_. The usual API functions associated to projective constraints are:

``` cpp
/// Project dx to constrained space (dx models an acceleration):
void projectResponse(const core::MechanicalParams* mparams, DataVecDeriv& resData);

/// Project v to constrained space (v models a velocity):
void projectVelocity(const core::MechanicalParams* mparams, DataVecDeriv& vData);

/// Project x to constrained space (x models a position):
void projectPosition(const core::MechanicalParams* mparams, DataVecCoord& xData);

/// Project c to constrained space (c models a constraint):
/// this method must be implemented by the component to handle Lagrange Multiplier based constraint
void projectJacobianMatrix(const core::MechanicalParams* mparams, DataMatrixDeriv& cData);

/// Project the global Mechanical Matrix to constrained space using offset parameter
void applyConstraint(const MechanicalParams*, const sofa::core::behavior::MultiMatrixAccessor*);

/// Project the global Mechanical Vector to constrained space using offset parameter
void applyConstraint(const MechanicalParams* , defaulttype::BaseVector*, const sofa::core::behavior::MultiMatrixAccessor*);

```