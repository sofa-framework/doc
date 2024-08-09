---
title: DefaultAnimationLoop
---

DefaultAnimationLoop
====================

This component belongs to the category of [AnimationLoop](../../simulation-principles/animation-loop/).

The DefaultAnimationLoop is the component that rules the steps of the simulation in the default order. It consists in computing the collision (if any), the projective constraints, the physics, solving the resulting linear system and finally updating all data before another step begins.

<a href="https://github.com/sofa-framework/doc/blob/master/images/animationloop/DefaultAnimationLoop.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/animationloop/DefaultAnimationLoop.png?raw=true" title="Flow diagram for a DefaultAnimationLoop"/></a>


Data
----

The DefaultAnimationLoop has one data:

- **parallelODESolving**: if true, solves all the ODEs in parallel
- **computeBoundingBox**: a boolean defining whether the global bounding box of the scene is computed at each time step. Used mostly for rendering.


Usage
-----

The DefaultAnimationLoop has **no pre-requisite**. If no AnimationLoop is specified in the scene, this animation loop is included by default at the root node of the graph.

Note that this AnimationLoop does not support constraints solved using [Lagrange multipliers](../../simulation-principles/constraint/lagrange-constraint/).


Example
-------

This component is used as follows in XML format:

``` xml
<DefaultAnimationLoop />
```

or using SofaPython3:

``` python
node.addObject('DefaultAnimationLoop')
```

An example scene involving a DefaultAnimationLoop is available in [*examples/Component/AnimationLoop/DefaultAnimationLoop.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/AnimationLoop/DefaultAnimationLoop.scn)
