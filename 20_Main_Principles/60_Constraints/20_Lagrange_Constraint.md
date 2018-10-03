Constraint based on Lagrange Multipliers
========================================

SOFA allows the use of Lagrange multipliers to handle complex constraints, such as contacts and joints between moving objets that can not be straightforwarly implemented using [projection matrices](https://www.sofa-framework.org/community/doc/main-principles/constraints/projective-constraint/).


Constraint problem
------------------

To solve the dynamic of two constrained objects, we use a Lagrange Multipliers approach and a single linearization by time step. From the [physical system](https://www.sofa-framework.org/community/doc/main-principles/multi-model-representation/physical-model/) to solve, the constraint problem can be expressed with the linear system as:

<img src="https://latex.codecogs.com/gif.latex?$$\left(\mathbf{M}+dt\textstyle\frac{\partial%20f}{\partial%20\dot{x}}+dt^2\textstyle\frac{\partial%20f}{\partial%20x}\right)\Delta%20v=-dt(f+dt\textstyle\frac{\partial%20f}{\partial%20x}%20-%20\mathbf{H}^T\lambda)$$" title="Constraint problem" />

that can be written in a simpler way as:

<img src="https://latex.codecogs.com/gif.latex?$$\mathbf{A}\Delta%20v=b+dt\mathbf{H}^T\lambda$$" title="Shortened constraint problem" />

where <img src="https://latex.codecogs.com/gif.latex?$$\mathbf{H}^T\lambda$$" title="Constraint forces" /> is the vector of constraint forces contribution with <img src="https://latex.codecogs.com/gif.latex?$$\mathbf{H}$$" title="Constraint matrix" /> matrix containing the constraint directions and <img src="https://latex.codecogs.com/gif.latex?$$\lambda$$" title="Lagrange multipliers" /> are the so-called Lagrange multipliers. Both holonomic and nonholonomic constraints can be used to model the various mechanical interactions involved in the simulation. For each constraint, a constraint law is assigned, which depends on the relative position of the interacting objects:

<img src="https://latex.codecogs.com/gif.latex?$$\Phi(x_1,x_2%20...)~=~0$$" title="Constraint law1" />

<img src="https://latex.codecogs.com/gif.latex?$$\Psi(x_1,x_2%20...)~\geq~0$$" title="Constraint law2" />

where <img src="https://latex.codecogs.com/gif.latex?$$\Phi$$" title="Phi" /> represents the bilateral interaction laws (attachments, sliding joints, etc.) whereas <img src="https://latex.codecogs.com/gif.latex?$$\Psi$$" title="Psi" /> represents unilateral interaction laws (contact, needle puncture, friction, etc.). These functions can be nonlinear.

In the constrained system presented above, the constraint matrix <img src="https://latex.codecogs.com/gif.latex?$$\mathbf{H}$$" title="Constraint matrix" /> appeared. The definition of the constraint laws <img src="https://latex.codecogs.com/gif.latex?$$\Phi$$" title="Phi" /> and <img src="https://latex.codecogs.com/gif.latex?$$\Psi$$" title="Psi" /> allows to define:

<img src="https://latex.codecogs.com/gif.latex?$$\mathbf{H}_1(x)=\left[\frac{\partial%20\Phi}{\partial%20x1};\frac{\partial%20\Psi}{\partial%20x_1}\right]~~$$" title="H1" /><img src="https://latex.codecogs.com/gif.latex?$$~~\mathbf{H}_2(x)=\left[\frac{\partial%20\Phi}{\partial%20x2};\frac{\partial%20\Psi}{\partial%20x_2}\right]$$" title="H2" />

Note that <img src="https://latex.codecogs.com/gif.latex?$$\mathbf{H}$$" title="Constraint matrix" /> the matrix containing the constraint directions can be considered as the Jacobian of the mapping between the physical space and the constraint space. The constraint will always be linearized in SOFA. For two interacting objects (object 1 and object 2), the complete constrained system therefore corresponds to:

- <img src="https://latex.codecogs.com/gif.latex?$$\mathbf{A}_1\Delta%20v_1=b_1+dt\mathbf{H}^T_1\lambda$$" title="Shortened constraint problem1" />
- <img src="https://latex.codecogs.com/gif.latex?$$\mathbf{A}_2\Delta%20v_2=b_2+dt\mathbf{H}^T_2\lambda$$" title="Shortened constraint problem2" />

However, this system will not be solved diretly. It will be decomposed into two steps:


**Step 1**: interacting objects are solved independently while setting <img src="https://latex.codecogs.com/gif.latex?$$\lambda=0$$" title="Lagrange multipliers" />. We obtain what we call the free motion <img src="https://latex.codecogs.com/gif.latex?$$\Delta%20v_1^{free}$$" title="Free motion 1" /> and <img src="https://latex.codecogs.com/gif.latex?$$\Delta%20v_2^{free}$$" title="Free motion 2" /> for each object.


**Step 2**: now, the constraints are taken into account while considering <img src="https://latex.codecogs.com/gif.latex?$$b_1=b_2=0" title="No force condition" />. The constrained system can therefore be presented as:

<img src="https://latex.codecogs.com/gif.latex?$$\dot{\delta}=\mathbf{H}_1%20v_1^{free}-\mathbf{H}_2%20v_2^{free}+dt\left[\mathbf{H}_1\mathbf{A}_1^{-1}\mathbf{H}_1^T+\mathbf{H}_2\mathbf{A}_2^{-1}\mathbf{H}_2^T\right]\lambda$$" title="Constraint problem" />

where <img src="https://latex.codecogs.com/gif.latex?$$\mathbf{W}=dt\left[\mathbf{H}_1\mathbf{A}_1^{-1}\mathbf{H}_1^T+\mathbf{H}_2\mathbf{A}_2^{-1}\mathbf{H}_2^T\right]\lambda$$" title="Constraint problem" /> is the matrix <img src="https://latex.codecogs.com/gif.latex?$$\mathbf{W}$$" title="Compliance matrix" /> of our linearized constraint system, this matrix is homogeneous to a compliance. <img src="https://latex.codecogs.com/gif.latex?$$\dot{\delta}$$" title="Compliance matrix" /> is the constraint violation (here in velocity), that can be directly obtained from the expression of our constraint laws <img src="https://latex.codecogs.com/gif.latex?$$\Phi$$" title="Phi" /> and <img src="https://latex.codecogs.com/gif.latex?$$\Psi$$" title="Psi" />.

Finally, the resolution of the constraint problem is done using the [Gauss-Seidel algorithm](https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method). After resolution of this new linear system, the motion can be corrected as follows:

- <img src="https://latex.codecogs.com/gif.latex?$$x_1=x_1^{free}+dt\cdot%20\Delta%20v_1^{cor}$$" title="Correction1" />
- <img src="https://latex.codecogs.com/gif.latex?$$x_1=x_2^{free}+dt\cdot%20\Delta%20v_2^{cor}$$" title="Correction2" />
with <img src="https://latex.codecogs.com/gif.latex?$$x\Delta%20v_1^{cor}=\mathbf{A}_1^{-1}\mathbf{H}_1^T\lambda$$" title="Corrective displacement1" /> and <img src="https://latex.codecogs.com/gif.latex?$$x\Delta%20v_2^{cor}=\mathbf{A}_2^{-1}\mathbf{H}_2^T\lambda$$" title="Corrective displacement2" />


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

The result of the resolution of the linear system <img src="https://latex.codecogs.com/gif.latex?$$\mathbf{A}x=b$$" title="Linear system" /> is noted : <img src="https://latex.codecogs.com/gif.latex?$$x_{free}$$" title="Free motion solution" />.

#### Constraint-based correction ####
Once the free motion <img src="https://latex.codecogs.com/gif.latex?$$x_{free}$$" title="Free motion solution" /> has been computed, the animation loop will look for an existing _ConstraintSolver_ in the scene graph. If one is found, it will handle the entire constraint process: computation of the constraint system, resolution and application of the corrective motion ensuring valid constraints.


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

A _ConstraintSolver_ is called by the _AnimationLoop_ within the _step()_ function. The _solveConstraint()_ function of the _ConstraintSolver_ organizes and rules all the steps of the resolution of the constraint problem. It builds the constraint system, solves it and applies a correction to find a corrected solution based on the free motion <img src="https://latex.codecogs.com/gif.latex?$$x_{free}$$" title="Free motion solution" />. In the code of any _ConstraintSolver_, you find the following functions:


``` cpp
bool prepareStates(const core::ConstraintParams * , MultiVecId res1, MultiVecId res2=MultiVecId::null());
bool buildSystem(const core::ConstraintParams * , MultiVecId res1, MultiVecId res2=MultiVecId::null());
bool solveSystem(const core::ConstraintParams * , MultiVecId res1, MultiVecId res2=MultiVecId::null());
bool applyCorrection(const core::ConstraintParams * , MultiVecId res1, MultiVecId res2=MultiVecId::null());
```

Each of these functions corresponds to a step described below:
  - **Prepare states**: allocates in memory vectors corresponding to the corrective motion <img src="https://latex.codecogs.com/gif.latex?$$\Delta%20v^{cor}$$" title="Corrective displacement" /> and the Lagrange multipliers <img src="https://latex.codecogs.com/gif.latex?$$\lambda$$" title="Lagrange multipliers" />
  - **Build system**: ensures itself the construction of the constraint matrix system
  - **Solve system**: the _ConstraintResolution_ finds a solution for the constraint problem
  - **Apply the correction**: recovers the result <img src="https://latex.codecogs.com/gif.latex?$$\Delta%20v^{cor}$$" title="Corrective displacement" /> and applies this corrective motion to the free motion <img src="https://latex.codecogs.com/gif.latex?$$x=x^{free}+dt\cdot%20\Delta%20v^{cor}$$" title="Correction" />

The step of building the system (see the "Build system" section) and solving it (see the "ConstraintResolution" section) will now be detailed.

#### Build system ####

This is the denser part of the constraint resolution. Most steps done to build the constraint problem are triggered using (visitors)[https://www.sofa-framework.org/community/doc/main-principles/animationloop-and-visitors/] browsing the simulation graph. The following steps are processed one after another:

  - reset
  See the visitor _MechanicalResetConstraintVisitor_.
  - X
  See the visitor _MechanicalBuildConstraintMatrix_.
  - 
  See the visitor _MechanicalAccumulateMatrixDeriv_
  - 
  See the visitor _MechanicalProjectJacobianMatrixVisitor_
  - clear constraints
  - 
  See the visitor _MechanicalGetConstraintViolationVisitor_
  - 
  See the visitor _MechanicalGetConstraintResolutionVisitor_
  - addComplianceInConstraintSpace

In the code, the _buildSystem()_ function looks like this:

``` cpp
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



#### ConstraintSolver in SOFA ####

Two different _ConstraintSolver_ implementations exist in SOFA:
  - _GenericConstraintSolver_: 
  - _LCPConstraintSolver_: 

Moreover, you may find the class _ConstraintSolver_. This class does not implement a real solver but actually just browses the graph in order to find and use one of the two implementations mentioned above.





ConstraintCorrection
--------------------

Different classes of _ConstraintCorrection_ exist in SOFA:
  - _GenericConstraintCorrection_: 
  - _UncoupledConstraintCorrection_: 
  - _LinearSolverConstraintCorrection_: 
  - _PrecomputedConstraintCorrection_: 



ConstraintResolution
--------------------

The resolution of the system will be processed when the _solveSystem()_ function of the _ConstraintSolver_ is called (see). In SOFA, the current resolution always relies on a [Gauss-Seidel algorithm](https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method). Depending on the type of _ConstraintSolver_ used, two implementations are available:
  - using a _LCPConstraintSolver_, the Gauss-Seidel implementation running is implemented in _sofa::helper::GaussSeidel_
  - using a _GenericConstraintSolver_, the Gauss-Seidel algorithm triggered is the one implemented internally in _GenericConstraintSolver::GaussSeidel_

The output of the _ConstraintResolution_ is the corrected motion <img src="https://latex.codecogs.com/gif.latex?$$\Delta%20v^{cor}$$" title="Corrective displacement" /> for each object involved.




More about Lagrange multipliers and constraints
-----------------------------------------------

To read more and go further regarding constraints relying on Lagrange multipliers, please read Pr. Duriez habilitation [thesis available online](http://tel.archives-ouvertes.fr/tel-00785118/).

You can also look at examples in the scenes of SOFA like:
  - _examples/Components/animationloop/FreeMotionAnimationLoop.scn_
  - _examples/Components/constraint/SlidingConstraint.scn_
