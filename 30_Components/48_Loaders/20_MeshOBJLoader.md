MeshOBJLoader
=============

This component belongs to the category of the [MeshLoaders](https://www.sofa-framework.org/community/doc/simulation-principles/topology/#meshloaders).

The MeshOBJLoader loads a mesh from a file under the format \*.obj. Such a mesh file **only supports surface meshes**. The \*.obj meshes can be generated using softwares like [Blender](https://blender.org/).

Usage
-----

**No pre-requisite** in your scene to use a MeshLoader.


Example
-------

This component is used as follows in XML format:

``` xml
<MeshOBJLoader name="ObjLoader" filename="mesh/floor3.obj" />
```

or using SofaPython3:

``` python
node.addObject('MeshOBJLoader', name="ObjLoader", filename="mesh/floor3.obj")
```

An example scene involving a MeshOBJLoader is available in [*examples/Component/IO/Mesh/MeshOBJLoader.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/IO/Mesh/MeshObjLoader.scn)