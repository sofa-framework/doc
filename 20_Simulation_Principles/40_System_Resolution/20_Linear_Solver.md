Linear solvers
==============

Once the [integration scheme](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/integration-schemes/) described how the linear matrix system is built, this system <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="Linear system" /> must be solved in order to find the solution <img class="latex" src="https://latex.codecogs.com/png.latex?x(t+dt)" title="DOF at next time step system" /> at the next time step.


To solve this system, two main categories of algorithms exist: the **direct** solvers and the **iterative** solvers.

Direct solvers
--------------

These solvers aim at finding the exact solution <img class="latex" src="https://latex.codecogs.com/png.latex?x(t+dt)" title="DOF at next time step system" /> of the system by computing in one single step <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}^{-1}b" title="Compute inverse matrix" />. To do so, various methods exist to compute the inverse matrix of <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" />.

For small-size linear systems, the direct methods will be efficient. Large and sparse systems may imply time-consuming inverse of the matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" />. The advantage of direct methods is that they succeed to solve well-conditioned and even some quite ill-conditioned problems. The computation of the inverse of <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> often relies on decomposition of this matrix: Cholesky, LU or LDL and their sparse versions are available.


#### Direct solver implementation

Direct solvers in SOFA are:

- [SparseLDLSolver](https://www.sofa-framework.org/community/doc/using-sofa/components/linearsolver/sparseldlsolver/)
- LULinearSolver / SparseLUSolver
- CholeskySolver / SparseCholeskySolver
- SVDLinearSolver (Jacobi SVD)
- BTDLinearSolver



#### In the SOFA code


The resolution of the linear system is computed in the `solve()` function of the LinearSolver. With direct solvers, the integration scheme sucessively calls the two following functions:

``` cpp
invert(Matrix& M)
```
implementing the targeted decomposition method:
``` cpp
solve(Matrix& A, Vector& x, Vector& b)
```



Iterative solvers
-----------------

Contrary to direct solvers, iterative methods converge towards the solution gradually. The solution is approximated at each iteration a little bit more accurately, rather than computed in one single large iteration. With iterative methods, the error esimated in the solution decreases with the number of iterations.

For well-conditioned problems (even large systems), the convergence remains monotonic. However, for ill-conditioned systems, the convergence might be much slower. Since these methods compute the residual <img class="latex" src="https://latex.codecogs.com/png.latex?r=\mathbf{A}x-b" title="Residual computation" /> at each iteration, the matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> does not have to be built to improve performances (only matrix vector computations). Numerical settings of the solver (maximum number of iterations, tolerance for instance) must be appropriately defined. Two available methods are the [conjugate gradient method](http://en.wikipedia.org/wiki/Conjugate_gradient_method) (using the CGLinearSolver) or the [minimal residual method](http://en.wikipedia.org/wiki/Generalized_minimal_residual_method) (using the MinResLinearSolver).


#### Iterative solver implementation

Iterative solvers in SOFA are:

- [CGLinearSolver](https://www.sofa-framework.org/community/doc/using-sofa/components/linearsolver/cglinearsolver/)
- MinResLinearSolver


#### In the SOFA code


The resolution of the linear system is computed in the `solve()` function of the LinearSolver. With iterative solvers, the integration scheme only calls the function:

``` cpp
solve(Matrix& A, Vector& x, Vector& b)
```
and will handle these vectors as TempVectorContainer and create any new vector using the function *vtmp.createTempVector()* as follows:
``` cpp
typename Inherit::TempVectorContainer vtmp(this, params, A, x, b);
Vector* r1 =  vtmp.createTempVector();
```
