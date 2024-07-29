ShewchukPCGLinearSolver  
=======================

This component belongs to the category of [LinearSolver](../../../simulation-principles/system-resolution/linear-solver/), it therefore aims at solving the linear system $$\mathbf{A}x=b$$. The ShewchukPCGLinearSolver is an iterative solver using the [conjugate gradient method](https://en.wikipedia.org/wiki/Conjugate_gradient_method) as implemented in the [CGLinearSolver](./cglinearsolver/) in SOFA but it adds the possibility to define a [preconditioner](https://en.wikipedia.org/wiki/Preconditioner). It must be reminded that the ShewchukPCGLinearSolver relies on the conjugate gradient method, meaning that as all iterative approaches, no exact solution can be found. The accuracy of your solution will always depend on the conditioning of your system and your input data (iterations, tolerance and threshold).


Preconditioners are used in cases where the convergence of the system is slow, which is usually due to a ill-conditioned system (high [condition number](https://en.wikipedia.org/wiki/Condition_number)). In order to preserve accuracy, while improving performance, preconditioning methods aims at projecting a matrix $$\mathbf{P}$$ (preconditioner) on the linear system $$\mathbf{A}x=b$$, in order to get closer to the solution. The efficiency of the preconditioner will depend on the choice of the preconditioner $$\mathbf{P}$$.

The ShewchukPCGLinearSolver allows to choose the preconditioner of our choice based on an external direct linear solver: LULinearSolver, [SparseLDLSolver](../direct/sparseldlsolver/), etc. These solvers will allow to compute $$\mathbf{P} \approx \mathbf{A}$$ and use it to compute at each iteration _k_ of the conjugate gradient:

$$\mathbf{P}^{-1}(\mathbf{A}x_k-b)=0$$

Using an appropriate preconditioner $$\mathbf{P}$$ of a matrix $$\mathbf{A}$$ means that $$\mathbf{P}^{-1}\mathbf{A}$$ has a smaller condition number than $$\mathbf{A}$$.


Usage
-----

The ShewchukPCGLinearSolver **requires**:

- the use (above in the scene graph) of an integration scheme
- (below in the scene graph) of a MechanicalObject storing the state information that the ShewchukPCGLinearSolver will access
- and, if a preconditioning is desired, a linear solver to compute the $$\mathbf{P}^{-1}$$

As for the CGLinearSolver, when using a ShewchukPCGLinearSolver, make sure you carefully chose the value of the free data field iterations, tolerance and threshold. Both tolerance and threshold data must be chosen in accordance with the dimension of the degrees of freedom (DOFs). Usually, the value of these two data is close to the square of the expected error on the DOFs.
