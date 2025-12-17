---
title: EulerExplicitSolver
---

EulerExplicitSolver  
===================

The EulerExplicitSolver component belongs to the category of [integration schemes or ODE Solver](../../../../simulation-principles/system-resolution/integration-scheme/). This scheme allows to solve dynamic systems explicitly: all forces will be computed based on the state information at the current time step $x(t)$.

Looking at continuum mechanics, the linear system $\mathbf{A}x=b$ arises from the dynamic equation. This dynamic is written as follows but other physics (like heat transfer) result in a similar equation:

$$
\mathbf{M}\Delta v=dt\left(f(x,t)\right)
$$

where $x$ is the degrees of freedom, $\mathbf{M}$ the mass matrix and $f(x,t)$ a function of $x$ (and possibly its derivatives) acting on our system. In the case of the EulerExplicitSolver, this equation can be written: 

$$
\mathbf{M}\Delta v=dt\left(f(x(t))\right)
$$

since forces only depend on known state (at our current time step). These forces are computed by the ForceField in the `addForce()` function. The system matrix $\mathbf{A}$ is only equal to the mass matrix $\mathbf{M}$.

Depending on whether the mass matrix is diagonal or not, SOFA supports two cases:

1) The mass matrix is diagonal. It makes the resolution of the linear system trivial (best performances). In this case, the system matrix $\mathbf{A}$ equals a diagonal mass matrix $\mathbf{M}$ which is diagonal, and it can be stored as a vector $|m|$ . Moreover, its inverse can directly be obtained as: $\mathbf{M}^{-1}=|m|^{-1}=\frac{1}{|m|}$.
   The solution $\Delta v_{sol}=dt\cdot \mathbf{M}^{-1}f(x(t))$ finally corresponds to a division operation of $f(x(t))$ by the mass. This computation is actually performed by the Mass component in the `accFromF()` function. Therefore, no LinearSolver is needed to compute directly or iteratively a solution.
2) The mass matrix is not diagonal. Solving the system requires a linear solver. 

Note that the **symplectic** data allows to modify the scheme to make it [symplectic](https://en.wikipedia.org/wiki/Semi-implicit_Euler_method), i.e. velocities are updated before the positions.
It allows to update the positions from the newly computed velocities, instead of velocities from the previous time step.
This option makes the scheme more robust in time.
EulerExplicitSolver is symplectic by default.

Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/EulerExplicitSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/EulerExplicitSolver.png?raw=true" title="Flow diagram for a EulerExplicitSolver"/></a>



Usage  
-----  

The EulerExplicitSolver **requires** a MechanicalObject to store the state vectors. However, as explained above, no LinearSolver is needed and the EulerExplicitSolver is **only working using a [UniformMass](../../../mass/uniformmass/) or [DiagonalMass](../../../mass/diagonalmass/)**, which ensures to have a diagonal system matrix.
