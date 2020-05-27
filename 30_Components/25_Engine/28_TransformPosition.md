TransformPosition
-----------------

This engine transforms the positions of one DataFields into new positions after applying a transformation. This transformation can be either:

-   Projection on a plane (plane defined by an origin and a normal vector)
-   Translation, rotation, scale and some combinations of translation rotation and scale

#### Input data's

-   **input\_position**: input array of 3d points.  

#### Output data's

-   **output\_position**: output array of 3d points projected on a plane.  

#### Additional Parameter

-   **method**: transformation method either translation or scale or rotation or projectOnPlane.

#### Examples

An example scene involving the TransformPosition engine is available in [*examples/Components/engine/TransformPosition.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/engine/TransformPosition.scn)
