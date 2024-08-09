---
title: Linear Solver
---

Linear solvers
==============

Once the [integration scheme](./../integration-scheme/) described how the linear matrix system is built, this system $$\mathbf{A}x=b$$ must be solved in order to find the solution $$x(t+dt)$$ at the next time step.

To solve this system, two main categories of algorithms exist: the **direct** solvers and the **iterative** solvers.

Direct solvers
--------------

These solvers aim at finding the exact solution $$x(t+dt)$$ of the system by computing in one single step $$\mathbf{A}^{-1}b$$. To do so, various methods exist to compute the inverse matrix of $$\mathbf{A}$$.

For small-size linear systems, the direct methods will be efficient. Large and sparse systems may imply time-consuming inverse of the matrix $$\mathbf{A}$$. The advantage of direct methods is that they succeed to solve well-conditioned and even some quite ill-conditioned problems. The computation of the inverse of $$\mathbf{A}$$ often relies on decomposition of this matrix: Cholesky, LU or LDL and their sparse versions are available.


#### Direct solver implementation

Among the numerous direct solvers available in SOFA, we can mention:

- [SparseLDLSolver](../../../components/linearsolver/direct/sparseldlsolver/) and [AsyncSparseLDLSolver](../../../components/linearsolvers/direct/asyncsparseldlsolver//)
- [SparseLUSolver](../../../components/linearsolvers/direct/sparselusolver/)
- [CholeskySolver](../../../components/linearsolvers/direct/choleskysolver/) / [SparseCholeskySolver](../../../components/linearsolvers/direct/sparsecholeskysolver/)
- [SVDLinearSolver](../../../components/linearsolvers/direct/svdlinearsolver) (Jacobi SVD)
- [BTDLinearSolver](../../../components/linearsolvers/direct/btdlinearsolver)



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

For well-conditioned problems (even large systems), the convergence remains monotonic. However, for ill-conditioned systems, the convergence might be much slower. Since these methods compute the residual $$r=\mathbf{A}x-b$$ at each iteration, the matrix $$\mathbf{A}$$ does not have to be built to improve performances (only matrix vector computations). Numerical settings of the solver (maximum number of iterations, tolerance for instance) must be appropriately defined. Two available methods are the [conjugate gradient method](http://en.wikipedia.org/wiki/Conjugate_gradient_method) (using the CGLinearSolver) or the [minimal residual method](http://en.wikipedia.org/wiki/Generalized_minimal_residual_method) (using the MinResLinearSolver).


#### Iterative solver implementation

Iterative solvers in SOFA are:

- [CGLinearSolver](../../../linearsolver/iterative/cglinearsolver/)
- [ShewchukPCGLinearSolver](../../../components/linearsolver/iterative/preconditioned-cg/)
- [MinResLinearSolver](../../../components/linearsolver/iterative/minreslinearsolver/)


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

Another example is [CGLinearSolver](../../../linearsolver/iterative/cglinearsolver/).
Its default template parameter is `GraphScattered`.
This template parameter means the implementation is matrix-free.
However, [CGLinearSolver](../../../linearsolver/iterative/cglinearsolver/) is a solver supporting also assembled matrices.
For example, it is possible to declare `<CGLinearSolver template="CompressedRowSparseMatrixMat3x3d"/>`.
