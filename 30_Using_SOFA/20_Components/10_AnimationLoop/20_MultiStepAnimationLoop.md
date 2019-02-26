MultiStepAnimationLoop
======================

This component belongs to the category of [AnimationLoop](https://www.sofa-framework.org/community/doc/main-principles/animationloop-and-visitors/).

The MultiStepAnimationLoop derives from the DefaultAnimationLoop. This animation loop is different due to the fact that it allows for running several collision (C) and several integration time in one step (I), where C and I can be different.

Usage
-----

The MultiStepAnimationLoop has no pre-requisite.

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

An example scene involving a MultiStepAnimationLoop is available in *examples/Components/animationloop/MultiStepAnimationLoop.scn*