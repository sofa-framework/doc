Linear solvers
==============

Once the [integration scheme](https://www.sofa-framework.org/community/doc/simulation-principles/system-resolution/integration-scheme/) described how the linear matrix system is built, this system <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="Linear system" /> must be solved in order to find the solution <img class="latex" src="https://latex.codecogs.com/png.latex?x(t+dt)" title="DOF at next time step system" /> at the next time step.


To solve this system, two main categories of algorithms exist: the **direct** solvers and the **iterative** solvers.

Direct solvers
--------------

These solvers aim at finding the exact solution <img class="latex" src="https://latex.codecogs.com/png.latex?x(t+dt)" title="DOF at next time step system" /> of the system by computing in one single step <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}^{-1}b" title="Compute inverse matrix" />. To do so, various methods exist to compute the inverse matrix of <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" />.

For small-size linear systems, the direct methods will be efficient. Large and sparse systems may imply time-consuming inverse of the matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" />. The advantage of direct methods is that they succeed to solve well-conditioned and even some quite ill-conditioned problems. The computation of the inverse of <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> often relies on decomposition of this matrix: Cholesky, LU or LDL and their sparse versions are available.


#### Direct solver implementation

Direct solvers in SOFA are:

- [SparseLDLSolver](https://www.sofa-framework.org/community/doc/using-sofa/components/linearsolver/sparseldlsolver/) and [AsyncSparseLDLSolver](https://www.sofa-framework.org/community/doc/components/linearsolvers/asyncsparseldlsolver//)
- LULinearSolver (in SofaNewmat plugin) / SparseLUSolver
- CholeskySolver / SparseCholeskySolver
- SVDLinearSolver (Jacobi SVD)
- BTDLinearSolver



#### In the SOFA code


The resolution of the linear system is computed in the `solve()` function of the LinearSolver. With direct solvers, the integration scheme successively calls the two following functions:

``` cpp
invert(Matrix& M)
```
implementing the targeted decomposition method:
``` cpp
solve(Matrix& A, Vector& x, Vector& b)
```



Iterative solvers
-----------------

Contrary to direct solvers, iterative methods converge towards the solution gradually. The solution is approximated at each iteration a little bit more accurately, rather than computed in one single large iteration. With iterative methods, the error estimated in the solution decreases with the number of iterations.

For well-conditioned problems (even large systems), the convergence remains monotonic. However, for ill-conditioned systems, the convergence might be much slower. Since these methods compute the residual <img class="latex" src="https://latex.codecogs.com/png.latex?r=\mathbf{A}x-b" title="Residual computation" /> at each iteration, the matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> does not have to be built to improve performances (only matrix vector computations). Numerical settings of the solver (maximum number of iterations, tolerance for instance) must be appropriately defined. Two available methods are the [conjugate gradient method](http://en.wikipedia.org/wiki/Conjugate_gradient_method) (using the CGLinearSolver) or the [minimal residual method](http://en.wikipedia.org/wiki/Generalized_minimal_residual_method) (using the MinResLinearSolver).


#### Iterative solver implementation

Iterative solvers in SOFA are:

- [CGLinearSolver](https://www.sofa-framework.org/community/doc/using-sofa/components/linearsolver/cglinearsolver/)
- [ShewchukPCGLinearSolver](https://www.sofa-framework.org/community/doc/components/linearsolvers/preconditioned-cg/)
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


### Matrix Assembly vs. Matrix Free

Linear solvers can also be divided into the two following categories:
- Matrix Assembly: the matrix of the system is explicitly assembled before being used to solve the system.
- Matrix Free: there is no data structure or allocated memory used to store a matrix.
Instead, the solver only calls matrix-vector operations (e.g. product), which do not require the explicit assembly of the matrix.

In SOFA, the choice of the type of solver is made through the template parameter of the linear solver component.
For example, `<SparseLDLSolver/>` is a shortcut for `<SparseLDLSolver template="CompressedRowSparseMatrixd"/>` (`CompressedRowSparseMatrixd` is the default template parameter of SparseLDLSolver).
`CompressedRowSparseMatrixd` means the matrix is assembled in a compressed sparse row data structure.
SparseLDLSolver also supports the template parameter `CompressedRowSparseMatrixMat3x3d`, where the entries of the matrix are 3x3 blocks.

Another example is [CGLinearSolver](https://www.sofa-framework.org/community/doc/components/linearsolvers/cglinearsolver/).
Its default template parameter is `GraphScattered`.
This template parameter means the implementation is matrix-free.
However, [CGLinearSolver](https://www.sofa-framework.org/community/doc/components/linearsolvers/cglinearsolver/) is a solver supporting also assembled matrices.
For example, it is possible to declare `<CGLinearSolver template="CompressedRowSparseMatrixMat3x3d"/>`.
