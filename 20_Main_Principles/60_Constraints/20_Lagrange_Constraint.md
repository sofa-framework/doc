Constraint based on Lagrange Multipliers
========================================

SOFA allows the use of Lagrange multipliers to handle complex constraints, such as contacts and joints between moving objets that can not be straightforwarly implemented using [projection matrices](https://www.sofa-framework.org/community/doc/main-principles/constraints/projective-constraint/).



FreeAnimationLoop
-----------------

To solve such complex constraint-based interactions, the simulation requires a specific [animation loop](https://www.sofa-framework.org/community/doc/main-principles/animationloop-and-visitors/): the _FreeAnimationLoop_. This animation loop divides each simulation step into two successive resolution steps: the free motion and a corrective motion.


#### Free motion ####
The first step triggered by the _FreeAnimationLoop_ is the free motion step. It consists in the resolution of the unconstrained (free) system <img src="https://latex.codecogs.com/gif.latex?$$\mathbf{A}x=b$$" title="Linear system" /> as described in the System Resolution section. Note that this free resolution may also include [projective constraints](https://www.sofa-framework.org/community/doc/main-principles/constraints/projective-constraint) that will be projected on the linear system. In the same way, [collision](https://www.sofa-framework.org/community/doc/main-principles/multi-model-representation/collisions) might also be detected and a response would be created.	

In the _solve()_ function of the _FreeAnimationLoop_, you will find the following functions responsible for the free motion:
``` cpp
///Solve visitor is triggered to solve the free motion
simulation::SolveVisitor freeMotion(params, dt, true);

///Apply the projective constraint if any
mop.projectResponse(freeVel);
mop.propagateDx(freeVel, true);

///Detect and respond to collision
computeCollision(params);
```

The result of the resolution of the linear system <img src="https://latex.codecogs.com/gif.latex?$$\mathbf{A}x=b$$" title="Linear system" /> is noted : <img src="https://latex.codecogs.com/gif.latex?$$x_free$$" title="Free motion solution" />.

#### Constraint-based correction ####
Once the free motion <img src="https://latex.codecogs.com/gif.latex?$$x_free$$" title="Free motion solution" /> has been computed, the animation loop will look for an existing _ConstraintSolver_ in the scene graph. If one is found, it will handle the entire constraint process: computation of the constraint system, resolution and application of the corrective motion ensuring valid constraints.

In the _solve()_ function of the _FreeAnimationLoop_, the constraint resolution simply appears as:
``` cpp
///if a ConstraintSolver is in the simulation, trigger the constraint pipeline
if (constraintSolver)
{
	constraintSolver->solveConstraint(&cparams, pos, vel);
}
```



ConstraintSolver
----------------

The _ConstraintSolver_ is 
organize all the steps of the resolution
it builds the constraint problem, solve it and apply a correction to find a corrected solution from the free motion solution xfree

prepare states
build system ++++
solve system
apply the correction



ConstraintCorrection
--------------------





ConstraintResolution
--------------------

Gauss Seidel
two implementations available depending on the type of constraint solver you use:
LCP --> sofa::helper::GaussSeidel
Generic --> Generic::GaussSeidel



More about Lagrange multipliers and constraints
-----------------------------------------------

To read more and go further regarding constraints relying on Lagrange multipliers, please read Pr. Duriez habilitation [thesis available online](http://tel.archives-ouvertes.fr/tel-00785118/).











Interaction constraint
----------------------

Unlike the previous project constraints, an interaction constraint is applied between a pair of simulated body.

In SOFA, you can find several of these projective constraints in the SofaBoundaryConditions module, among them:
  - the _BilateralInteractionConstraint_: 
  - 
  

Classes defining constraints between a pair of objects inherit from the class _PairInteractionConstraint_. The associated API functions are:

``` cpp
/// Retrieve the associated MechanicalState of both paired objects
MechanicalState<DataTypes>* getMState1()
BaseMechanicalState* getMechModel1()
MechanicalState<DataTypes>* getMState2()
BaseMechanicalState* getMechModel2()

/// Construct the Constraint violations vector of each constraint
/// \param v is the result vector that contains the whole constraints violations
/// \param cParams defines the state vectors to use for positions and velocities. Also defines the order of the constraint (POS, VEL, ACC)
virtual void getConstraintViolation(const ConstraintParams* cParams, defaulttype::BaseVector *v) override;

/// Construct the Constraint violations vector of each constraint
///
/// \param v is the result vector that contains the whole constraints violations
/// \param x1 and x2 are the position vectors used to compute contraint position violation
/// \param v1 and v2 are the velocity vectors used to compute contraint velocity violation
/// \param cParams defines the state vectors to use for positions and velocities. Also defines the order of the constraint (POS, VEL, ACC)
///
/// This is the method that should be implemented by the component
virtual void getConstraintViolation(const ConstraintParams* cParams, defaulttype::BaseVector *v, const DataVecCoord &x1, const DataVecCoord &x2
, const DataVecDeriv &v1, const DataVecDeriv &v2) = 0;

/// Construct the Jacobian Matrix
///
/// \param cId is the result constraint sparse matrix Id
/// \param cIndex is the index of the next constraint equation: when building the constraint matrix, you have to use this index, and then update it
/// \param cParams defines the state vectors to use for positions and velocities. Also defines the order of the constraint (POS, VEL, ACC)
virtual void buildConstraintMatrix(const ConstraintParams* cParams, MultiMatrixDerivId cId, unsigned int &cIndex) override;

/// Construct the Jacobian Matrix
///
/// \param c1 and c2 are the results constraint sparse matrix
/// \param cIndex is the index of the next constraint equation: when building the constraint matrix, you have to use this index, and then update it
/// \param x1 and x2 are the position vectors used for contraint equation computation
/// \param cParams defines the state vectors to use for positions and velocities. Also defines the order of the constraint (POS, VEL, ACC)
///
/// This is the method that should be implemented by the component
virtual void buildConstraintMatrix(const ConstraintParams* cParams, DataMatrixDeriv &c1, DataMatrixDeriv &c2, unsigned int &cIndex
, const DataVecCoord &x1, const DataVecCoord &x2) = 0;

```

