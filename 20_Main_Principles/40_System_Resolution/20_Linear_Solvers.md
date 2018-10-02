Linear solvers
==============

Once the [integration scheme](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/integration-schemes/) described how the linear matrix system is built, this system <img src="https://latex.codecogs.com/gif.latex?$$\mathbf{A}x=b$$" title="Linear system" /> must be solved in order to find the solution <img src="https://latex.codecogs.com/gif.latex?$$x(t+dt)$$" title="DOF at next time step system" /> at the next time step.


Two categories
--------------

To solve this system, two main categories of algorithms are available:

  * **direct solvers**: these solvers aim at finding the exact solution <img src="https://latex.codecogs.com/gif.latex?$$x(t+dt)$$" title="DOF at next time step system" /> of the system by computing in one single step <img src="https://latex.codecogs.com/gif.latex?$$\mathbf{A}^{-1}b$$" title="Compute inverse matrix" />. To do so, various methods exist to compute the inverse matrix of <img src="https://latex.codecogs.com/gif.latex?$$\mathbf{A}$$" title="System matrix" />. For small-size linear systems, the direct methods will be efficient. Large and sparse systems may imply time-consuming inverse of the matrix <img src="https://latex.codecogs.com/gif.latex?$$\mathbf{A}$$" title="System matrix" />. The advantage of direct methods is that they succeed to solve well-conditioned and even some quite ill-conditioned problems. The computation of the inverse of <img src="https://latex.codecogs.com/gif.latex?$$\mathbf{A}$$" title="System matrix" /> often relies on decomposition of this matrix: [Cholesky](https://en.wikipedia.org/wiki/Cholesky_decomposition), LU or LDL and their sparse versions are available.

  * **iterative solvers**: contrary to direct solvers, iterative methods converge towards the solution gradually. The solution is approximated at each iteration a little bit more accurately, rather than computed in one single large iteration. With iterative methods, the error esimated in the solution decreases with the number of iterations. For well-conditioned problems (even large systems), the convergence remains monotonic. However, for ill-conditioned systems, the convergence might be much slower. Since these methods compute the residual <img src="https://latex.codecogs.com/gif.latex?$$r=\mathbf{A}x-b$$" title="Residual computation" /> at each iteration, the matrix <img src="https://latex.codecogs.com/gif.latex?$$\mathbf{A}$$" title="System matrix" /> does not have to be built to improve performances (only matrix vector computations). Numerical settings of the solver (maximum number of iterations, tolerance for instance) must be appropriately defined. Two available methods are the [conjugate gradient method](http://en.wikipedia.org/wiki/Conjugate_gradient_method) (using the CGLinearSolver) or the [minimal residual method](http://en.wikipedia.org/wiki/Generalized_minimal_residual_method) (using the MinResLinearSolver).


In the SOFA code
----------------

The abstract description is done within the MatrixLinearSolver and depends on the category of the linear system (i.e. direct or iterative):

* with direct solvers, the integration scheme sucessively calls the two following functions:
``` cpp
invert(Matrix& M)
```
implementing the targeted decomposition method:
``` cpp
solve(Matrix& A, Vector& x, Vector& b)
```
* with iterative solvers, the integration scheme only calls the function:
``` cpp
solve(Matrix& A, Vector& x, Vector& b)
```
and will handle these vectors as TempVectorContainer and create any new vector using the function *vtmp.createTempVector()* as follows:
``` cpp
typename Inherit::TempVectorContainer vtmp(this, params, A, x, b);
Vector* r1 =  vtmp.createTempVector();
```
