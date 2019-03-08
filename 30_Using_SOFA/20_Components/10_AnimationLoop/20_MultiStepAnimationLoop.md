MultiStepAnimationLoop
======================

This component belongs to the category of [AnimationLoop](https://www.sofa-framework.org/community/doc/main-principles/animationloop-and-visitors/).

The MultiStepAnimationLoop derives from the [DefaultAnimationLoop](https://www.sofa-framework.org/community/doc/using-SOFA/components/animationloop/defaultanimationloop/). This animation loop is different due to the fact that it allows - at each iteration - for running several collision (_collisionSteps_), and within each of these collision steps, several integration sub-steps can be computes (_integrationSteps_).

<img src="https://github.com/sofa-framework/doc/blob/master/Images/animationloop/MultiStepAnimationLoop.png" title="Flow diagram for a MultiStepAnimationLoop"/>

Usage
-----

The MultiStepAnimationLoop has **no pre-requisite**.

Note that this MultiStepAnimationLoop does not handle constraints solved using [Lagrange multipliers](https://www.sofa-framework.org/community/doc/main-principles/constraints/lagrange-constraint/).


Example
-------

This component is used as follows in XML format:

``` xml
<MultiStepAnimationLoop collisionSteps="10" integrationSteps="2" />
```

or using Python:

``` python
node.createObject('MultiStepAnimationLoop', collisionSteps='10', integrationSteps='2')
```

An example scene involving a MultiStepAnimationLoop is available in [*examples/Components/animationloop/MultiStepAnimationLoop.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/animationloop/MultiStepAnimationLoop.scn)