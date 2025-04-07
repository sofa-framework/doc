NewtonRaphsonSolver
===================

NewtonRaphsonSolver is a component able to solve nonlinear equations using [Newton-Raphson method](https://en.wikipedia.org/wiki/Newton%27s_method).
From an initial guess, the algorithm successively computes better approximations of the root of the nonlinear function.
At every iteration, multiple criteria are evaluated to decide to stop the algorithm (because it converged or the maximum number of iterations has been reached), or to continue.

The algorithm relies on the derivative of the function and a linear system to solve.
For a function $F : \mathbb{R}^k \rightarrow \mathbb{R}^k$, the new approximation of the root $x_{n+1}$ is computed as:

$$
\nabla_F(x_n) (x_{n+1} - x_n) = -F(x_n)
$$

where:

- $x_i$ is the $i$-th approximation of the root
- $x_0$ is the initial guess
- $\nabla_F$ is the Jacobian matrix of the function

If $dx$ is the solution of the previous linear system, then

$$
x_{n+1} = dx + x_n
$$

Example
-------

To solve a static equilibrium (see [StaticSolver](StaticSolver.md)), the nonlinear equation to solve is the sum of forces must be equal to zero ($\sum F = 0$). At each iteration, the linear system $K dx = -\sum F$ must be solved to compute the next approximation of the root. Here K is the derivative of the forces, also called the stiffness matrix.

Usage
-----

This component must be linked by another component requiring to solve a nonlinear equation, such as an implicit ODE solver or a static solver.
