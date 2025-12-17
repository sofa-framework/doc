---
title: UnilateralLagrangianConstraint
---

UnilateralLagrangianConstraint
===============================


This component belongs to the category of [Constraint Laws](../../../../../simulation-principles/constraint/lagrange-constraint/#constraint-laws) used for the Lagrange constraint resolution and inherits from the PairInteractionConstraint. The UnilateralLagrangianConstraint defines an [non-holonomic constraint](https://en.wikipedia.org/wiki/Nonholonomic_system) law between a pair of simulated body, i.e. the constraint defined between the pair of objects must have an inequality form:

$$
\Psi(x_1,x_2...)~\geq~0
$$

Such a constraint are used for friction-less and friction contact modeling (it can even be used as a starting point for puncture modeling). For a UnilateralLagrangianConstraint, the constraint matrix $\mathbf{H}$ (derivative of the constraint law) corresponds to:

- $\mathbf{H}_1 = \begin{bmatrix} \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 & ... & \vec{n}_i & ... & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_1}\\ \end{bmatrix}$ for object 1
- $\mathbf{H}_1 = \begin{bmatrix} \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 & ... & \vec{n}_j & ... & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_2} \\ \end{bmatrix}$ for object 2

We can see from these matrices that the UnilateralLagrangianConstraint is a transformation towards the constraint space, by building a projection of any field against the contact direction (normal here, and possibly tangential directions as well if friction is defined).


As all constraint laws, the UnilateralLagrangianConstraint will be called in the following functions and for the following steps:

- `getConstraintViolation()`: project the free velocity in the constraint space and compute the free interpenetration $\dot{\delta}_1^{free}=\mathbf{H}_1v_1^{free}$
- `buildConstraintMatrix()`: build the compliance made up of $dt\mathbf{H}_1\mathbf{A}_1^{-1}\mathbf{H}_1^T$ and $dt\mathbf{H}_2\mathbf{A}_2^{-1}\mathbf{H}_2^T$



Usage
-----

The UnilateralLagrangianConstraint can only be used in the context of [Lagrange constraint](../../../../../simulation-principles/constraint/lagrange-constraint/) resolution. The scene must therefore contain:

- a FreeMotionAnimationLoop
- a ConstraintSolver

Moreover, each constrained object must define in its node a ConstraintCorrection so that the corrective motion can be applied. Unlike other constraints, the UnilateralLagrangianConstraint is mostly used in SOFA for contact modeling. UnilateralLagrangianConstraint are therefore dynamically and automatically created within the scene graph when two objects are colliding: when the CollisionPipeline defines new DetectionOutput with ContactResponse using Lagrange multipliers, each DetectionOutput generates a new UnilateralLagrangianConstraint.

