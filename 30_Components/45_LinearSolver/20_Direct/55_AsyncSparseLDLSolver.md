AsyncSparseLDLSolver
====================

AsyncSparseLDLSolver is based on [SparseLDLSolver](./../sparseldlsolver/).
It follows some ideas presented in:

> Courtecuisse, Hadrien, et al. "Asynchronous preconditioners for efficient solving of non-linear deformations." VRIPHYS-Virtual Reality Interaction and Physical Simulation. Eurographics Association, 2010.
https://hal.inria.fr/hal-00688865/document

## Asynchronous Factorization

The difference compared to SparseLDLSolver resides in the fact that the factorization of the matrix is performed in a different thread in order to speed up the simulation.

The synchronous version performs the following operations (synchronously):
1) Build the matrix
2) Factorize the matrix
3) Solve the system based on the factorization

In the asynchronous version, the factorization is performed asynchronously.
A consequence is that the solving process uses a factorization which may not be up-to-date.
In practice, the factorization is at least one time step old, but it can be an older factorization depending on the duration of the asynchronous factorization step.
Because of this, the solver computes an approximation of the solution, based on an old factorization.
It is therefore important to understand that using AsyncSparseLDLSolver changes the behavior of your simulation compared to a synchronous version.
It may also introduce instabilities.

## A Preconditioner

AsyncSparseLDLSolver can be used as a preconditioner of [ShewchukPCGLinearSolver](../../iterative/preconditioned-cg/).

## Performances

The idea to have the factorization of the matrix in a different thread is to reduce the time taken to solve a linear system.
However, building the matrix and solving a system based on a factorization will not be reduced.
Since the factorization of a matrix is a time-consuming step of the simulation, this strategy greatly improves the performances.
This speed up is at the price of an approximation of the solution, because solving the linear system relies on a factorization of a matrix from a previous time step.
