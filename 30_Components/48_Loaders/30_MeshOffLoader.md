MeshOffLoader
=============

This component belongs to the category of the [MeshLoaders](https://www.sofa-framework.org/community/doc/simulation-principles/topology/#meshloaders).

The MeshOffLoader loads a mesh from a file under the format \*.off. Such a mesh file can be either surface or volumetric meshes. The \*.off meshes can be generated using softwares like [MeshLab](https://www.meshlab.net/).

Usage
-----

**No pre-requisite** in your scene to use a MeshLoader.


Example
-------

This component is used as follows in XML format:

``` xml
<MeshOffLoader name="offLoader" filename="mesh/aneurysm3D_1.off" />
```

or using SofaPython3:

``` python
node.addObject('MeshOffLoader', name="offLoader", filename="mesh/aneurysm3D_1.off")
```

An example scene involving a MeshOffLoader is available in [*examples/Component/IO/Mesh/MeshOffLoader.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/IO/Mesh/MeshOffLoader.scn)
