---
title: Shaders
---

General use of Shaders
----------------------

A complete set of tools about using shaders is implemented into SOFA.
The three kinds of shaders (vertex and fragments (mandatory), geometry
(optional)) are available. Shader is used only for Visual Model as
**OglModel**. The effects of the shader is spread to the associated
subtree. Finally, there is only one shader activated for each visual
model : if two shaders are present in the same node, only the second
will be effective. To simply include a shader, add this into your node :

```xml
```

vertFilename and fragFilename are the only mandatory parameters. Other
optional parameters are about geometry shader : geoFilename,
geometryInputType, geometryOutputType and geometryVerticesOut. A last
parameter, turnOn, is for debugging purpose, when you want to disable
shader without restarting the scene. If you want to send values to
uniform variables defined into the shader, a certain number of objects
is available :

-   OglIntVariable,OglInt{2,3,4}Variable : for int and ivec{2,3,4}
-   OglFloatVariable,OglFloat{2,3,4}Variable : for float and vec{2,3,4}
-   OglIntVectorVariable, OglIntVector{2,3,4}Variable : for arrays of
    int and ivec{2,3,4}
-   OglFloatVectorVariable, OglFloatVector{2,3,4}Variable : for arrays
    of float and vec{2,3,4}
-   OglMatrix{2,3,4}x{2,3,4} : for matrix n\*m where n and m = {2,3,4}

<!-- -->


