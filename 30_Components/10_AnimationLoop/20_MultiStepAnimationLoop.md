MultiStepAnimationLoop
======================

This component belongs to the category of [AnimationLoop](../../simulation-principles/animation-loop/).

The MultiStepAnimationLoop derives from the [DefaultAnimationLoop](../../components/animationloop/defaultanimationloop/). This animation loop is different due to the fact that it allows - at each iteration - for running several collision (_collisionSteps_), and within each of these collision steps, several integration sub-steps can be computed (_integrationSteps_).

<a href="https://github.com/sofa-framework/doc/blob/master/images/animationloop/MultiStepAnimationLoop.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/animationloop/MultiStepAnimationLoop.png?raw=true" title="Flow diagram for a MultiStepAnimationLoop"/></a>


Usage
-----

The MultiStepAnimationLoop has **no pre-requisite**.

Note that this MultiStepAnimationLoop does not handle constraints solved using [Lagrange multipliers](../../simulation-principles/constraint/lagrange-constraint/).
