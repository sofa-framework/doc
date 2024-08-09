FreeMotionAnimationLoop
=======================

This component belongs to the category of [AnimationLoop](../../../simulation-principles/animation-loop/).

The FreeMotionAnimationLoop is the component that rules the simulation in two main steps: a free motion, then a correction step. First, the free motion computes the projective constraints, the physics, solving the resulting free linear system. Second, the correction step solves the constraints based on the Lagrange multipliers. More information on the constraint resolution can be found [here](../../../simulation-principles/constraint/lagrange-constraint/).

<a href="https://github.com/sofa-framework/doc/blob/master/images/animationloop/FreeMotionAnimationLoop.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/animationloop/FreeMotionAnimationLoop.png?raw=true" title="Flow diagram for a FreeMotionAnimationLoop"/></a>


Usage
-----

The FreeMotionAnimationLoop must be used specifically for constraint resolution based on the Lagrange multiplier. It therefore **requires**:

- a [ConstraintSolver](../../../simulation-principles/constraint/lagrange-constraint/#constraintsolver-in-sofa). If no constraint solver can be found, a LCPConstraintSolver is automatically created by default.

Note that one or multiple [ConstraintCorrection](../../../simulation-principles/constraint/lagrange-constraint/#constraintcorrection) may be required by the [ConstraintSolver](../../../simulation-principles/constraint/lagrange-constraint/#constraintsolver-in-sofa).

