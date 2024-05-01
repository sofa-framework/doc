MeshSTLLoader
=============

This component belongs to the category of the [MeshLoaders](https://www.sofa-framework.org/community/doc/simulation-principles/topology/#meshloaders).

The MeshSTLLoader loads a mesh from a file under the [format \*.stl](https://en.wikipedia.org/wiki/STL_(file_format)). Such a mesh file **only supports surface meshes**. The \*.stl format is widely spread and such meshes can be generated using softwares like [MeshLab](https://www.meshlab.net/) or [Paraview](https://www.paraview.org) among many other solutions.

Usage
-----

**No pre-requisite** in your scene to use a MeshLoader.


Example
-------

This component is used as follows in XML format:

``` xml
<MeshSTLLoader name="STLLoader" filename="mesh/circle_knot_ascii.stl" printLog="true" flipNormals="0" />
```

or using SofaPython3:

``` python
node.addObject('MeshSTLLoader', name="STLLoader", filename="mesh/circle_knot_ascii.stl", flipNormals="0")
```

An example scene involving a MeshSTLLoader is available in [*examples/Component/IO/Mesh/MeshSTLLoader.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/IO/Mesh/MeshSTLLoader.scn)
