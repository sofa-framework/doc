AsyncSparseLDLSolver
====================

(since SOFA v22.06)

AsyncSparseLDLSolver is based on [SparseLDLSolver](https://www.sofa-framework.org/community/doc/components/linearsolvers/sparseldlsolver/).
It follows some ideas presented in:

> Courtecuisse, Hadrien, et al. "Asynchronous preconditioners for efficient solving of non-linear deformations." VRIPHYS-Virtual Reality Interaction and Physical Simulation. Eurographics Association, 2010.
https://hal.inria.fr/hal-00688865/document

## Asynchronous Factorization

The difference compared to SparseLDLSolver is the factorization of the matrix in a different thread in order to speed up a simulation step.

The synchronous version performs the following operations (synchronously):
1) Build the matrix
2) Factorize the matrix
3) Solve the system based on the factorization

In the asynchronous version, the factorization is performed asynchronously.
A consequence is that the solving process uses a factorization which may not be up to date.
In practice, the factorization is at least one time step old.
Because of this, the solver computes an approximation of the solution, based on an old factorization.
It changes the behavior compared to a synchronous version, but it also changes the behavior depending on the duration of the factorization step.
It may introduce instabilities.

## A Preconditioner

AsyncSparseLDLSolver can be used as a preconditioner of [ShewchukPCGLinearSolver](https://www.sofa-framework.org/community/doc/components/linearsolvers/preconditioned-cg/).

## Performances

The idea to have the factorization of the matrix in a different thread is to reduce the time taken to solve a linear system.
However, building the matrix and solving a system based on a factorization will not be reduced.
Since the factorization of a matrix is a time-consuming step of the simulation, this strategy greatly improves the performances.
This speed up is at the price of an approximation of the solution, because solving the linear system relies on a factorization of a matrix from a previous time step.

## Example

This component is used as follows in XML format:

``` xml
<AsyncSparseLDLSolver />
```

or using SofaPython3:

``` python
node.addObject('AsyncSparseLDLSolver')
```

An example where AsyncSparseLDLSolver is used as a standalone linear solver is available in [*examples/Components/linearsolver/FEMBAR-AsyncSparseLDLSolver.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/linearsolver/FEMBAR-AsyncSparseLDLSolver.scn).
The example in [*examples/Components/linearsolver/preconditioner/FEMBAR-ShewchukPCGLinearSolver-AsyncSparseLDLSolver.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/linearsolver/preconditioner/FEMBAR-ShewchukPCGLinearSolver-AsyncSparseLDLSolver.scn) shows how to use AsyncSparseLDLSolver as a preconditioner of ShewchukPCGLinearSolver.
Finally, the example in [*examples/Components/linearsolver/preconditioner/FEMBAR-ShewchukPCGLinearSolver-WarpedAsyncSparseLDLSolver.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/linearsolver/preconditioner/FEMBAR-ShewchukPCGLinearSolver-WarpedAsyncSparseLDLSolver.scn) shows how the factorization in AsyncSparseLDLSolver can be warped using a WarpPreconditioner.
