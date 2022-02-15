TextureInterpolation
--------------------

This engine creates texture coordinate in 1D according to an input state vector. Coordinate can be interpolated either from min and max value of input states (default behavior) or on a manual define scale.

#### Input data's

-   **input\_states**: input array of state values
-   **input\_coordinates**: input array of coordinates values (not mandatory)

#### Output data's

-   **output\_coordinates**: output array of texture coordinates

#### Additional Parameter

**For manual scale :**

-   **min\_value**: minimum value of state value for interpolation
-   **max\_value**: maximum value of state value for interpolation
-   **manual\_scale**: compute texture interpolation on manually scale defined above

#### Examples

An example scene involving the TextureInterpolation engine is available in [*examples/Components/engine/TextureInterpolation.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/engine/TextureInterpolation.scn)