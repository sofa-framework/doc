Constraint based on Lagrange Multipliers
========================================

SOFA allows the use of Lagrange multipliers to handle complex constraints, such as contacts and joints between moving objets that can not be straightforwarly implemented using [projection matrices](https://www.sofa-framework.org/community/doc/main-principles/constraint/projective-constraint/).


General presentation of the constraint problem
----------------------------------------------

To solve the dynamic of two constrained objects, we use a Lagrange Multipliers approach and a single linearization by time step. From the [physical system](https://www.sofa-framework.org/community/doc/simulation-principles/multi-model-representation/physics-integration/) to solve, the constraint problem can be expressed with the linear system as:

<img class="latex" src="https://latex.codecogs.com/png.latex?\left(\mathbf{M}+dt\textstyle\frac{\partial%20f}{\partial%20\dot{x}}+dt^2\textstyle\frac{\partial%20f}{\partial%20x}\right)\Delta%20v=-dt(f+dt\textstyle\frac{\partial%20f}{\partial%20x}v%20-%20\mathbf{H}^T\lambda)" title="Constraint problem" />

that can be written in a simpler way as:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}\Delta%20v=b+dt\mathbf{H}^T\lambda" title="Shortened constraint problem" />

where <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{H}^T\lambda" title="Constraint forces" /> is the vector of constraint forces contribution with <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{H}" title="Constraint matrix" /> matrix containing the constraint directions and <img class="latex" src="https://latex.codecogs.com/png.latex?\lambda" title="Lagrange multipliers" /> are the so-called Lagrange multipliers. Both holonomic and nonholonomic constraints can be used to model the various mechanical interactions involved in the simulation. For each constraint, a constraint law is assigned, which depends on the relative position of the interacting objects:

<img class="latex" src="https://latex.codecogs.com/png.latex?\Phi(x_1,x_2%20...)~=~0" title="Constraint law1" />

<img class="latex" src="https://latex.codecogs.com/png.latex?\Psi(x_1,x_2%20...)~\geq~0" title="Constraint law2" />

where <img class="latex" src="https://latex.codecogs.com/png.latex?\Phi" title="Phi" /> represents the bilateral interaction laws (attachments, sliding joints, etc.) whereas <img class="latex" src="https://latex.codecogs.com/png.latex?\Psi" title="Psi" /> represents unilateral interaction laws (contact, needle puncture, friction, etc.). These functions can be nonlinear. In the constrained system presented above, the constraint matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{H}" title="Constraint matrix" /> appeared. The definition of the constraint laws <img class="latex" src="https://latex.codecogs.com/png.latex?\Phi" title="Phi" /> and <img class="latex" src="https://latex.codecogs.com/png.latex?\Psi" title="Psi" /> allows to define:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{H}_1(x)=\left[\frac{\partial%20\Phi}{\partial%20x1};\frac{\partial%20\Psi}{\partial%20x_1}\right]~~" title="H1" /><img class="latex" src="https://latex.codecogs.com/png.latex?~~\mathbf{H}_2(x)=\left[\frac{\partial%20\Phi}{\partial%20x2};\frac{\partial%20\Psi}{\partial%20x_2}\right]" title="H2" />

Note that <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{H}" title="Constraint matrix" /> the matrix containing the constraint directions can be considered as the Jacobian of the mapping between the physics space and the constraint space. The constraint will always be linearized in SOFA. For two interacting objects (object 1 and object 2), the complete constrained system therefore corresponds to:

- <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}_1\Delta%20v_1=b_1+dt\mathbf{H}^T_1\lambda" title="Shortened constraint problem1" />
- <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}_2\Delta%20v_2=b_2+dt\mathbf{H}^T_2\lambda" title="Shortened constraint problem2" />

However, this system will not be solved directly. It will be decomposed into two steps:


**Step 1**: Each interacting object is solved independently, i.e. as no constraint law is defined, while setting <img class="latex" src="https://latex.codecogs.com/png.latex?\lambda=0" title="Lagrange multipliers" />. This so-called free motion aims at finding the change in velocity <img class="latex" src="https://latex.codecogs.com/png.latex?\Delta%20v_1^{free}" title="Free motion 1" /> and <img class="latex" src="https://latex.codecogs.com/png.latex?\Delta%20v_2^{free}" title="Free motion 2" /> for each object from the resolution of:

- <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}_1\Delta%20v_1^{free}=b_1" title="Free motion of object1" />
- <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}_2\Delta%20v_2^{free}=b_2" title="Free motion of object2" />


**Step 2**: now, the constraints are taken into account while considering <img class="latex" src="https://latex.codecogs.com/png.latex?b_1=b_2=0" title="No force condition" />. We are looking for a corrective change in velocity  <img class="latex" src="https://latex.codecogs.com/png.latex?\Delta%20v_1^{corr}" title="Corrective motion 1" /> and <img class="latex" src="https://latex.codecogs.com/png.latex?\Delta%20v_2^{corr}" title="Corrective motion 2" /> for each object from the resolution of:

- <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}_1\Delta%20v_1^{corr}=dt\mathbf{H}^T_1\lambda" title="Free motion of object1" />
- <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}_2\Delta%20v_2^{corr}=dt\mathbf{H}^T_2\lambda" title="Free motion of object2" />

Defining <img class="latex" src="https://latex.codecogs.com/png.latex?\lambda" title="Lagrange multipliers" /> the Lagrange multipliers, as the forces to be applied in the constraint space to satisfy all constraint laws, the constrained system can therefore be presented as:

<img class="latex" src="https://latex.codecogs.com/png.latex?\dot{\delta}=\mathbf{H}_1%20v_1^{free}-\mathbf{H}_2%20v_2^{free}+dt\left[\mathbf{H}_1\mathbf{A}_1^{-1}\mathbf{H}_1^T+\mathbf{H}_2\mathbf{A}_2^{-1}\mathbf{H}_2^T\right]\lambda" title="Constraint problem" />

where <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{W}=dt\left[\mathbf{H}_1\mathbf{A}_1^{-1}\mathbf{H}_1^T+\mathbf{H}_2\mathbf{A}_2^{-1}\mathbf{H}_2^T\right]" title="Compliance matrix" /> is the matrix of our linearized constraint system, this matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{W}" title="Compliance matrix" /> is homogeneous to a compliance. <img class="latex" src="https://latex.codecogs.com/png.latex?\dot{\delta}" title="Constraint violation" /> is the constraint violation (here in velocity), that can be directly obtained from the expression of our constraint laws <img class="latex" src="https://latex.codecogs.com/png.latex?\Phi" title="Phi" /> and <img class="latex" src="https://latex.codecogs.com/png.latex?\Psi" title="Psi" />.

Finally, the resolution of the constraint problem is done using the [Gauss-Seidel algorithm](https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method). After resolution of this new linear system, the motion can be corrected as follows:

- <img class="latex" src="https://latex.codecogs.com/png.latex?x_1=x_1^{free}+dt\cdot%20\Delta%20v_1^{cor}" title="Correction1" />
- <img class="latex" src="https://latex.codecogs.com/png.latex?x_1=x_2^{free}+dt\cdot%20\Delta%20v_2^{cor}" title="Correction2" /> 
  with <img class="latex" src="https://latex.codecogs.com/png.latex?\Delta%20v_1^{cor}=dt\mathbf{A}_1^{-1}\mathbf{H}_1\lambda" title="Corrective displacement1" /> and <img class="latex" src="https://latex.codecogs.com/png.latex?\Delta%20v_2^{cor}=dt\mathbf{A}_2^{-1}\mathbf{H}_2\lambda" title="Corrective displacement2" />


FreeMotionAnimationLoop
-----------------

To solve such complex constraint-based interactions, the simulation requires a specific [animation loop](https://www.sofa-framework.org/community/doc/simulation-principles/animation-loop/): the [_FreeMotionAnimationLoop_](https://www.sofa-framework.org/community/doc/components/animationloops/freemotionanimationloop/). This animation loop divides each simulation step into two successive resolution steps: the free motion and a corrective motion.


#### Free motion ####
The first step triggered by the _FreeMotionAnimationLoop_ is the free motion step. It consists in the resolution of the unconstrained (free) system <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="Linear system" /> as described in the System Resolution section. Note that this free resolution may also include [projective constraints](https://www.sofa-framework.org/community/doc/main-principles/constraint/projective-constraint) that will be projected on the linear system. In the same way, [collision](https://www.sofa-framework.org/community/doc/main-principles/multi-model-representation/collisions) might also be detected and a response would be created.	

In the _solve()_ function of the _FreeMotionAnimationLoop_, you will find the following functions responsible for the free motion:
``` cpp
///Solve visitor is triggered to solve the free motion
simulation::SolveVisitor freeMotion(params, dt, true);

///Apply the projective constraint if any
mop.projectResponse(freeVel);
mop.propagateDx(freeVel, true);

///Detect and respond to collision
computeCollision(params);
```

The result of the resolution of the linear system <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="Linear system" /> is noted : <img class="latex" src="https://latex.codecogs.com/png.latex?x_{free}" title="Free motion solution" />.

#### Constraint-based correction ####
Once the free motion <img class="latex" src="https://latex.codecogs.com/png.latex?x_{free}" title="Free motion solution" /> has been computed, the animation loop will look for an existing _ConstraintSolver_ in the scene graph. If one is found, it will handle the entire constraint process: computation of the constraint system, resolution and application of the corrective motion ensuring valid constraints.


In the _solve()_ function of the _FreeMotionAnimationLoop_, the constraint resolution simply appears as:
``` cpp
///if a ConstraintSolver is in the simulation, trigger the constraint pipeline
if (constraintSolver)
{
	constraintSolver->solveConstraint(&cparams, pos, vel);
}
```



ConstraintSolver
----------------

A _ConstraintSolver_ is called by the _AnimationLoop_ within the _step()_ function. The _solveConstraint()_ function of the _ConstraintSolver_ organizes and rules all the steps of the resolution of the constraint problem. It builds the constraint system, solves it and applies a correction to find a corrected solution based on the free motion <img class="latex" src="https://latex.codecogs.com/png.latex?x_{free}" title="Free motion solution" />. In the code of any _ConstraintSolver_, you find the following functions:


``` cpp
bool prepareStates(const core::ConstraintParams * , MultiVecId res1, MultiVecId res2=MultiVecId::null());
bool buildSystem(const core::ConstraintParams * , MultiVecId res1, MultiVecId res2=MultiVecId::null());
bool solveSystem(const core::ConstraintParams * , MultiVecId res1, MultiVecId res2=MultiVecId::null());
bool applyCorrection(const core::ConstraintParams * , MultiVecId res1, MultiVecId res2=MultiVecId::null());
```

Each of these functions corresponds to a step described below:

  - **Prepare states**: allocates in memory vectors corresponding to the corrective motion <img class="latex" src="https://latex.codecogs.com/png.latex?\Delta%20v^{cor}" title="Corrective displacement" /> and the Lagrange multipliers <img class="latex" src="https://latex.codecogs.com/png.latex?\lambda" title="Lagrange multipliers" />

  - **Build system**: ensures itself the construction of the constraint matrix system

  - **Solve system**: the constraint resolution finds a solution for the constraint problem

  - **Apply the correction**: recovers the result <img class="latex" src="https://latex.codecogs.com/png.latex?\Delta%20v^{cor}" title="Corrective displacement" /> and applies this corrective motion to the free motion <img class="latex" src="https://latex.codecogs.com/png.latex?x=x^{free}+dt\cdot%20\Delta%20v^{cor}" title="Correction" />

The step of building the system (see the [Build system](https://www.sofa-framework.org/community/doc/main-principles/constraint/lagrange-constraint/#build-system), [Constraint laws](https://www.sofa-framework.org/community/doc/main-principles/constraint/lagrange-constraint/#constraint-laws) and [ConstraintCorrection](https://www.sofa-framework.org/community/doc/main-principles/constraint/lagrange-constraint/#constraintcorrection) sections) and solving it will now be detailed.

#### Build system ####

This is the denser part of the constraint resolution. Most steps done to build the constraint problem are triggered using [visitors](https://www.sofa-framework.org/community/doc/simulation-principles/visitors/) browsing the simulation graph. All the following functions are actually not implemented by _ConstraintSolver_ but by the constraint laws available in the scene <img class="latex" src="https://latex.codecogs.com/png.latex?\Phi" title="Phi" /> and <img class="latex" src="https://latex.codecogs.com/png.latex?\Psi" title="Psi" /> (see the [Constraint law](https://www.sofa-framework.org/community/doc/main-principles/constraint/lagrange-constraint/#constraint-laws) section).

The following steps are processed one after another:

  - reset the constraint matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{H}" title="Constraint matrix" />. The associated visitor is _MechanicalResetConstraintVisitor_

  - build a new constraint matrix (or Jacobian matrix) <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{H}" title="Constraint matrix" /> depending on the constraint laws available in the scene  <img class="latex" src="https://latex.codecogs.com/png.latex?\Phi" title="Phi" /> and <img class="latex" src="https://latex.codecogs.com/png.latex?\Psi" title="Psi" />. The associated visitor is _MechanicalBuildConstraintMatrix_

  - accumulate additional contributions to the constraint matrix (or Jacobian matrix) <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{H}" title="Constraint matrix" /> coming from underlying mappings. The associated visitor is _MechanicalAccumulateMatrixDeriv_

  - take into account the projective constraint <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{P}" title="Projective constraint" />. This step removes the constraints that are affecting the degrees of freedom currently concerned by a project constraint. The associated visitor is _MechanicalProjectJacobianMatrixVisitor_

  - clear previous values of the Lagrange multipliers

  - project the free motion <img class="latex" src="https://latex.codecogs.com/png.latex?v^{free}" title="Free motion" /> (computed at Step 1) into the constraint space <img class="latex" src="https://latex.codecogs.com/png.latex?\dot{\delta}=\mathbf{H}%20v^{free}" title="Projected free motion" /> where <img class="latex" src="https://latex.codecogs.com/png.latex?\dot{\delta}" title="Violation" /> is the violation in velocity. See the visitor _MechanicalGetConstraintViolationVisitor_

  - select which method will be used to solve the constraint problem. The associated visitor is _MechanicalGetConstraintResolutionVisitor_

  - finally build the "compliance" matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{W}=dt\left[\mathbf{H}_1\mathbf{A}_1^{-1}\mathbf{H}_1^T+\mathbf{H}_2\mathbf{A}_2^{-1}\mathbf{H}_2^T\right]" title="Compliance matrix" /> based on the previously computed matrices. This task is performed by the _ConstraintCorrection_. The detail of the assembly of <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{W}" title="Compliance matrix" /> is given below in the [ConstraintCorrection](https://www.sofa-framework.org/community/doc/main-principles/constraint/lagrange-constraint/#constraintcorrection) section. The associated function of the _ConstraintCorrection_ is _addComplianceInConstraintSpace()_

  - store <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{H}^T\lambda" title="Projected lambda" /> which corresponds to the projection of the Lagrange multipliers <img class="latex" src="https://latex.codecogs.com/png.latex?\lambda" title="Lagrange multipliers" /> into the physics space, and is homogeneous to forces. This vector is made available with the function _storeLambda()_. This will be finally used to compute the corrective motion, resulting from the constraint resolution



In the code, the _buildSystem()_ function performs each of the steps just described and looks as follows:

```cpp
simulation::MechanicalResetConstraintVisitor(cParams).execute(context);
simulation::MechanicalBuildConstraintMatrix(cParams, cParams->j(), numConstraints).execute(context);
simulation::MechanicalAccumulateMatrixDeriv(cParams, cParams->j(), reverseAccumulateOrder.getValue()).execute(context);
simulation::MechanicalProjectJacobianMatrixVisitor(&mparams).execute(context);

current_cp->clear(numConstraints);

MechanicalGetConstraintViolationVisitor(cParams, &current_cp->dFree).execute(context);
MechanicalGetConstraintResolutionVisitor(cParams, current_cp->constraintsResolutions).execute(context);

cc->addComplianceInConstraintSpace(cParams, &current_cp->W);
```


#### Solve system ####

The resolution of the system will be processed when the _solveSystem()_ function of the _ConstraintSolver_ is called. In SOFA, two different _ConstraintSolver_ implementations exist in SOFA:

  - _LCPConstraintSolver_: this solvers targets on collision constraints, contacts with frictions which corresponds to unilateral constraints. This solver proposes one implementation of a [Gauss-Seidel algorithm](https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method) available in in _sofa::helper::GaussSeidel_

  - _GenericConstraintSolver_: this solver handles all kind of constraints, i.e. works with any constraint resolution algorithm. This solver proposes three different resolution methods:
    - a Projective [Gauss-Seidel algorithm](https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method) (PGS) algorithm implemented in _GenericConstraintSolver::GaussSeidel_. To use this PGS algorithm, you must select the data *resolutionMethod* as _ProjectedGaussSeidel_
    - an Unbuilt (matrix-free) approach of the [Gauss-Seidel algorithm](https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method) (UGS) algorithm is also available, thus avoiding the assembly of the constraint system. To use this UGS algorithm, you must select the data *resolutionMethod* as _UnbuiltGaussSeidel_
    - a [Non-smooth Non-linear Conjugate Gradient](https://link.springer.com/article/10.1007/s00371-010-0502-6) (NNCG) algorithm implemented in _GenericConstraintSolver::NNCG()_. To use this NNCG algorithm, you must select the data  *resolutionMethod* as _NonsmoothNonlinearConjugateGradient_. Using the data _newtonIterations_, you can define the maximum number of iterations for the classical Newton method, solving the generic roots search problem.

NB: you may find the class _ConstraintSolver_. This class does not implement a real solver but actually just browses the graph in order to find and use one of the two implementations mentioned above.

The output of the constraint resolution is the corrected motion <img class="latex" src="https://latex.codecogs.com/png.latex?\Delta%20v^{cor}" title="Corrective displacement" /> for each object involved.



ConstraintCorrection
--------------------

As explained above, a _ConstraintCorrection_ is required in the simulation to define the way the compliance matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{W}" title="Compliance matrix" /> is computed. Different classes of _ConstraintCorrection_ exist in SOFA corresponding to different approaches:

  - _UncoupledConstraintCorrection_: makes the approximation that the compliance matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{W}" title="Compliance matrix" /> is diagonal. This is as strong assumption since a diagonal matrix means that all constraints are independent from each other. Note that you can directly specify the compliance matrix values within the Data field "compliance"

  - _LinearSolverConstraintCorrection_: computes the compliance matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{W}=\mathbf{H}\mathbf{A}^{-1}\mathbf{H}^T" title="Compliance matrix" /> where <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}^{-1}" title="Inverse of A" /> comes from a direct solver associated to the object. Since the direct solvers in SOFA factorize the matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> (for instance using a LDL factorization if you use the _LDLSolver_), the factorization is reused to compute the compliance matrix. The matrix-matrix multiplication <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{H}\mathbf{A}^{-1}\mathbf{H}^T" title="Compliance matrix" /> is not possible in case of a matrix-free solver, since the assembled inverse matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}^{-1}" title="Inverse of A" /> is not available. From the factorization of <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" />, the computation of <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{H}\mathbf{A}^{-1}\mathbf{H}^T" title="Compliance matrix" /> done in the function _addJMInvJt()_ requires to call the _solve()_ function from the direct solver, computing a matrix-vector multiplication, for each line of the constraint matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{H}" title="Constraint matrix" />, i.e. for each constraint. This approach can therefore be very computationally-demanding if you have many constraints. Note that this ConstraintCorrection proposes an optimization for wire-like structures (boolean option)

  - _PrecomputedConstraintCorrection_: instead of computing <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}^{-1}" title="Inverse of A" /> at each time step, this constraint correction precomputes once the inverse of <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> at the initialization of the simulation and stores this matrix into a file. This speeds up the simulation but it can lead to a lack of accuracy in case the system matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> changes during the simulation

  - _GenericConstraintCorrection_: similar to the _LinearSolverConstraintCorrection_, it allows to declare only once all the direct solvers (one for each constraint object) used to compute the global <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{W}" title="Compliance matrix" />, whereas the previously described constraint correction needs to be added for each object




Constraint laws
---------------

In SOFA, you can find several of interaction constraint laws available to include in your simulation. A lot of them is available in the SofaConstraint module, among them:

  - _UnilateralInteractionConstraint_: constraint of inequality (like the <img class="latex" src="https://latex.codecogs.com/png.latex?\Psi" title="Psi" /> function described above in the [Constraint problem](https://www.sofa-framework.org/community/doc/main-principles/constraint/lagrange-constraint/#constraint-problem) section), that fits for instance contact and collision cases

  - _BilateralInteractionConstraint_: constraint of equality (like the <img class="latex" src="https://latex.codecogs.com/png.latex?\Phi" title="Phi" /> function described above in the [Constraint problem](https://www.sofa-framework.org/community/doc/main-principles/constraint/lagrange-constraint/#constraint-problem) section), that fits for instance interactions, attachments between two paired objects

  - _SlidingConstraint_: constraint in equality, like the _BilateralInteractionConstraint_, but only active for some vectors of the physics space (for instance only the x-direction)

Classes defining constraints between a pair of objects inherit from the class _PairInteractionConstraint_. The associated API functions are:

``` cpp
/// Retrieve the associated MechanicalState of both paired objects
MechanicalState<DataTypes>* getMState1();
BaseMechanicalState* getMechModel1();
MechanicalState<DataTypes>* getMState2();
BaseMechanicalState* getMechModel2();

/// Construct the Constraint violations vector of each constraint
virtual void getConstraintViolation(const ConstraintParams* cParams, defaulttype::BaseVector *v);

/// Construct the Jacobian Matrix or constraint matrix H
virtual void buildConstraintMatrix(const ConstraintParams* cParams, MultiMatrixDerivId cId, unsigned int &cIndex);

```





More about Lagrange multipliers and constraints
-----------------------------------------------

To read more and go further regarding constraints relying on Lagrange multipliers, please read:

  - Pr. Duriez's [habilitation thesis](http://tel.archives-ouvertes.fr/tel-00785118/)

  - Pr. Baraff's [courses](https://www.cs.cmu.edu/~baraff/sigcourse/)

You can also look at examples in the scenes of SOFA like:

  - _examples/Components/animationloop/FreeMotionAnimationLoop.scn_

  - _examples/Components/constraint/SlidingConstraint.scn_
