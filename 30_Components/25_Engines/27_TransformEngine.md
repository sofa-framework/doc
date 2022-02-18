TransformEngine
===============

This component belongs to the category of [Engines](https://www.sofa-framework.org/community/doc/simulation-principles/engine/). The TransformEngine transforms the positions of one DataFields into new positions after applying a transformation. This transformation can be either: translation, rotation or scale.

Input Data
----------

- **input\_position**: input array of 3d points
Output Data
----------

- **output\_position**: output array of 3d points

Additional Parameter
--------------------

- **translation**: Vector3 defining the translation to be applied
- **rotation**: Vector3 defining the rotation to be applied
- **scale**: Vector3 describing the scale to be applied

Examples
--------

This component is used as follows in XML format:

``` xml
<TransformEngine name="translationEngine" template="Vec3d" translation="10 0 0" input_position="@meshLoader.position" />
<MechanicalObject name="transform" template="Vec3d" position="@translationEngine.output_position" />
```

or in python:

``` python
node.addObject("TransformEngine", name="translationEngine", template="Vec3d", translation="10 0 0", input_position="@meshLoader.position")
node.addObject("MechanicalObject", name="transform", template="Vec3d", position="@translationEngine.output_position")
```


An example scene involving the TransformEngine engine is available in [*examples/Components/engine/TransformEngine.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/engine/TransformEngine.scn)
