MeshGmshLoader
==============

This component belongs to the category of the [MeshLoaders](https://www.sofa-framework.org/community/doc/simulation-principles/topology/#meshloaders).

The MeshGmshLoader loads a mesh from a file under the format \*.msh. Such a mesh file can be either surface or volumetric meshes. The \*.msh meshes can be generated using softwares like [Gmsh](https://gmsh.info/).
To be noted, an interesting [project couples SOFA and Gmsh in python](https://github.com/sescaida/gmsh-sofa_tutorial) for applications such as parametric design or design optimization.

Usage
-----

**No pre-requisite** in your scene to use a MeshLoader.


Example
-------

This component is used as follows in XML format:

``` xml
<MeshGmshLoader name="GmshLoader" filename="mesh/square3.msh" createSubelements="true" flipNormals="0" />
```

or using SofaPython3:

``` python
node.addObject('MeshGmshLoader', name="ObjLoader", filename="mesh/square3.msh", createSubelements="true", flipNormals="0")
```

An example scene involving a MeshGmshLoader is available in [*examples/Components/loader/MeshGmshLoader.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/loader/MeshGmshLoader.scn)