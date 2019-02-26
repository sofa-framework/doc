DefaultAnimationLoop
====================

This component belongs to the category of [AnimationLoop](https://www.sofa-framework.org/community/doc/main-principles/animationloop-and-visitors/).

The DefaultAnimationLoop is the component that rules the steps of the simulation in the default order. It consists in computing the collision (if any), the projective constraints, the physics, solving the resulting linear system and finally updating all data before another step begins.

Usage
-----

The DefaultAnimationLoop has no pre-requisite. If no AnimationLoop is specified in the scene, this animation loop is included by default at the root node of the graph.

Note that this AnimationLoop does not handle constraints solved using [Lagrange multipliers](https://www.sofa-framework.org/community/doc/main-principles/constraints/lagrange-constraint/).


Example
-------

This component is used as follows in XML format:

``` xml
<DefaultAnimationLoop />
```

or using Python:

``` python
node.createObject('DefaultAnimationLoop')
```

An example scene involving a DefaultAnimationLoop is available in *examples/Components/mass/UniformMass.scn*