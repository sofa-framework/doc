FreeAnimationLoop
=================

This component belongs to the category of [AnimationLoop](https://www.sofa-framework.org/community/doc/main-principles/animationloop-and-visitors/).

The FreeAnimationLoop is the component that rules the simulation in two main steps: a free motion, then a correction step. The free motion computes the projective constraints, the physics, solving the resulting free linear system. The correction step solves the constraints based on the Lagrange multipliers. More information on the constraint resolution can be found [here](Note that this AnimationLoop does not handle constraints solved using [Lagrange multipliers](https://www.sofa-framework.org/community/doc/main-principles/constraints/lagrange-constraint/).

It consists in computing the collision (if any), the projective constraints, the physics, solving the resulting linear system and finally updating all data before another step begins.


Usage
-----

The FreeAnimationLoop must be used specifically for constraint resolution based on the Lagrange multiplier. It therefore requires a [ConstraintSolver](https://www.sofa-framework.org/community/doc/main-principles/constraints/lagrange-constraint/#constraintsolver-in-sofa) and [ConstraintCorrection](https://www.sofa-framework.org/community/doc/main-principles/constraints/lagrange-constraint/#constraintcorrection).


Example
-------

This component is used as follows in XML format:

``` xml
<FreeAnimationLoop />
```

or using Python:

``` python
node.createObject('FreeAnimationLoop')
```

An example scene involving a FreeAnimationLoop is available in *examples/Components/animationloop/FreeAnimationLoop.scn*