FreeMotionAnimationLoop
=======================

This component belongs to the category of [AnimationLoop](https://www.sofa-framework.org/community/doc/main-principles/animationloop-and-visitors/).

The FreeMotionAnimationLoop is the component that rules the simulation in two main steps: a free motion, then a correction step. First, the free motion computes the projective constraints, the physics, solving the resulting free linear system. Second, the correction step solves the constraints based on the Lagrange multipliers. More information on the constraint resolution can be found [here](https://www.sofa-framework.org/community/doc/main-principles/constraints/lagrange-constraint/).

![Flow diagram for a FreeMotionAnimationLoop](https://github.com/sofa-framework/doc/blob/master/Images/animationloop/FreeMotionAnimationLoop.png)

Usage
-----

The FreeMotionAnimationLoop must be used specifically for constraint resolution based on the Lagrange multiplier. It therefore **requires**:
- a [ConstraintSolver](https://www.sofa-framework.org/community/doc/main-principles/constraints/lagrange-constraint/#constraintsolver-in-sofa)
- and a [ConstraintCorrection](https://www.sofa-framework.org/community/doc/main-principles/constraints/lagrange-constraint/#constraintcorrection).


Example
-------

This component is used as follows in XML format:

``` xml
<FreeMotionAnimationLoop />
```

or using Python:

``` python
node.createObject('FreeMotionAnimationLoop')
```

An example scene involving a FreeAnimationLoop is available in [*examples/Components/animationloop/FreeMotionAnimationLoop.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/animationloop/FreeMotionAnimationLoop.scn)