MeshVTKLoader
=============

This component belongs to the category of the [MeshLoaders](https://www.sofa-framework.org/community/doc/simulation-principles/topology/#meshloaders).

The MeshVTKLoader loads a mesh from a file under the format \*.vtk. Such a mesh file can be either surface or volumetric meshes. The \*.vtk meshes can be generated using the [Paraview](https://www.paraview.org) software.

Usage
-----

**No pre-requisite** in your scene to use a MeshLoader.


Example
-------

This component is used as follows in XML format:

``` xml
<MeshVTKLoader name="VtkLoader" filename="mesh/liver.vtk" flipNormals="0"/>
```

or using SofaPython3:

``` python
node.addObject('MeshVTKLoader', name="VtkLoader", filename="mesh/liver.vtk", flipNormals="0")
```

An example scene involving a MeshVTKLoader is available in [*examples/Components/loader/MeshVTKLoader.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/loader/MeshVTKLoader.scn)