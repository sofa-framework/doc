FreeMotionAnimationLoop
=======================

This component belongs to the category of [AnimationLoop](https://www.sofa-framework.org/community/doc/main-principles/animation-loop/).

The FreeMotionAnimationLoop is the component that rules the simulation in two main steps: a free motion, then a correction step. First, the free motion computes the projective constraints, the physics, solving the resulting free linear system. Second, the correction step solves the constraints based on the Lagrange multipliers. More information on the constraint resolution can be found [here](https://www.sofa-framework.org/community/doc/main-principles/constraints/lagrange-constraint/).

<a href="https://github.com/sofa-framework/doc/blob/master/images/animationloop/FreeMotionAnimationLoop.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/animationloop/FreeMotionAnimationLoop.png?raw=true" title="Flow diagram for a FreeMotionAnimationLoop"/></a>

Data
----

The DefaultAnimationLoop has one data:

- **computeBoundingBox**: a boolean defining whether the global bounding box of the scene is computed at each time step. Used mostly for rendering.


Usage
-----

The FreeMotionAnimationLoop must be used specifically for constraint resolution based on the Lagrange multiplier. It therefore **requires**:

- a [ConstraintSolver](https://www.sofa-framework.org/community/doc/main-principles/constraints/lagrange-constraint/#constraintsolver-in-sofa). If no constraint solver can be found, a LCPConstraintSolver is automatically created by default.

Note that one or multiple [ConstraintCorrection](https://www.sofa-framework.org/community/doc/main-principles/constraints/lagrange-constraint/#constraintcorrection) may be required by the [ConstraintSolver](https://www.sofa-framework.org/community/doc/main-principles/constraints/lagrange-constraint/#constraintsolver-in-sofa).


Example
-------

This component is used as follows in XML format:

``` xml
<FreeMotionAnimationLoop />
```

or using SofaPython3:

``` python
node.addObject('FreeMotionAnimationLoop')
```

An example scene involving a FreeAnimationLoop is available in [*examples/Components/animationloop/FreeMotionAnimationLoop.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/animationloop/FreeMotionAnimationLoop.scn)
