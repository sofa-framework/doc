FixedLagrangianConstraint
=========================

This component belongs to the category of [Constraint Laws](../../../../../simulation-principles/constraint/lagrange-constraint/#constraint-laws) used for the Lagrange constraint resolution.
The FixedLagrangianConstraint defines a [holonomic constraint](https://en.wikipedia.org/wiki/Holonomic_constraints) law applied on some degrees on freedom to fix them in space.

The constraint equation can be written as:

$$
\Phi(q) = q - q_0
$$

where $q$ is the position and $q_0$ is the initial position.

The constraint matrix $\mathbf{H}$ (derivative of the constraint law) is then filled with blocks of the identity matrix (of the dimension of the number of degrees of freedom per point) under each considered fixed index. If `fixAll` is selected, then this Jacobian is the identity matrix. 

$$
\mathbf{H} = \mathbf{I} 
$$
