BilateralLagrangianConstraint
==============================

This component belongs to the category of [Constraint Laws](../../../../../simulation-principles/constraint/lagrange-constraint/#constraint-laws) used for the Lagrange constraint resolution and inherits from the PairInteractionConstraint. The BilateralLagrangianConstraint defines an [holonomic constraint](https://en.wikipedia.org/wiki/Holonomic_constraints) law between a pair of simulated body, i.e. the constraint defined between the pair of objects must have an equality form:

$$
\Phi(x_1,x_2...)~=~0
$$

Such a constraint is suited for attachment cases or sliding joints. For an attachment case, if the vertex _i_ of object 1 and the vertex _j_ of object 2 are attached, the holonomic constraint law can be written as $x_1(i)-x_2(j)~=~0$.

For a BilateralLagrangianConstraint, the constraint matrix $\mathbf{H}$ (derivative of the constraint law) corresponds to:

- $\mathbf{H}_1 = \begin{bmatrix} \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 &  ... & \begin{bmatrix} 1 & 0 & 0\\\end{bmatrix}_i &  ... & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_1}\\ \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 &  ... & \begin{bmatrix} 0 & 1 & 0\\\end{bmatrix}_i &  ... & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_1}\\ \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 &  ... & \begin{bmatrix} 0 & 0 & 1\\\end{bmatrix}_i &  ... & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_1}\\ \end{bmatrix}$ for object 1
- $\mathbf{H}_2 = \begin{bmatrix} \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 &  ... & \begin{bmatrix} -1 & 0 & 0\\\end{bmatrix}_j &  ... & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_2}\\ \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 &  ... & \begin{bmatrix} 0 & -1 & 0\\\end{bmatrix}_j &  ... & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_2}\\ \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 &  ... & \begin{bmatrix} 0 & 0 & -1\\\end{bmatrix}_j &  ... & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_2}\\ \end{bmatrix}$ for object 2


As all constraint laws, the BilateralLagrangianConstraint will be called in the following functions and for the following steps:

- `getConstraintViolation()`: project the free velocity in the constraint space and compute the free interpenetration $\dot{\delta}_1^{free}=\mathbf{H}_1v_1^{free}$
- `buildConstraintMatrix()`: build the compliance made up of $dt\mathbf{H}_1\mathbf{A}_1^{-1}\mathbf{H}_1^T$ and $dt\mathbf{H}_2\mathbf{A}_2^{-1}\mathbf{H}_2^T$



Usage
-----

The BilateralLagrangianConstraint can only be used in the context of [Lagrange constraint](../../../../../simulation-principles/constraint/lagrange-constraint/) resolution. The scene must therefore contain:

- a FreeMotionAnimationLoop
- a ConstraintSolver

Moreover, each constrained object must define in its node a ConstraintCorrection so that the corrective motion can be applied.
