MeshLoader/ImageLoader
----------------------

These components can be used in SOFA since revision (r5359). File
formats supported are: - In SOFA trunk: .obj, .vtk, .gmsh, .trian, .xsp
- In SOFA at asclepios (still in project): .tr, .tr3D, .atr3D, .vol,
.tet3D, .atet3D Volumetric msh files can be generated based on surface
meshes, using an external tool (with some limitations, though):
http://www.dennis2society.de/main/archives/285 Another tool is presented
here: http://smart.seecs.nust.edu.pk/tutorial.html

#### Architecture

[![Uml\_loaders](https://www.sofa-framework.org/wp-content/uploads/2015/01/Uml_loaders1.png){.aligncenter
.size-full .wp-image-1360 width="633"
height="400"}](https://www.sofa-framework.org/wp-content/uploads/2015/01/Uml_loaders1.png)
Comments: - The branch of Image loader has not been implemented yet. -
The function canCreate will be used by the factory to create the
appropriate loader when no specific loader is used (i.e "&lt;MeshLoader
filename="myfile.obj /&ut;") in this case the function will recognize
the file extension) or if the file format is unknown.

#### How to use it

To use these specific loaders, you have to connect manually Data
dependencies in the XML scene file. For example:

    <MeshObjLoader name="ObjLoader" filename="mesh/my_mesh.obj" />
    <MechanicalObject name="dofs" position="@ObjLoader.position" />
    <Node>
     <TriangleSetTopologyContainer name="triangulation" triangles="@../ObjLoader.triangles" position="@../ObjLoader.position" />
    </Node>

If you want to connect all the Data from the Loader to a component. You
can use the attribute "src". A parser will automatically connect
together Data named the same in the loader and in the component. Using
the attribute "src", the previous example can be written this way:

    <MeshObjLoader name="ObjLoader" filename="mesh/my_mesh.obj" />
    <MechanicalObject name="dofs" src="@ObjLoader" />
    <Node>
     <TriangleSetTopologyContainer name="triangulation" src="@../ObjLoader" />
    </Node>

Notes that, when using this attribute, Data not empty will not be
overwrite. For example:

    <MeshObjLoader name="ObjLoader" filename="mesh/my_mesh.obj" />
    <MechanicalObject name="dofs" src="@ObjLoader" position="0 0 0"/>

In this case, the Data position of the !MechanicalObject will not be
field by the !MeshObjLoader. Thus, it is possible to combine Data
dependencies. Data standard names It is important to have homogeneous
Data names to be able to connect Data and to use the attribute "src".
That is why this section propose standard names used Loaders: Standard
names for **\[doxygen:sofa::core::componentmodel::loader::MeshLoader
MeshLoader\]**:

``` {.ignore:true}
list of points coordinates:
  position     =>   type: Data < helper::vector  > positions;

For 2D elements:
  edges        =>  type: Data< helper::vector< helper::fixed_array  > > edges;
  triangles    =>  type: Data< helper::vector< helper::fixed_array  > > triangles;
  Quads        =>  type: Data< helper::vector< helper::fixed_array  > > quads;
  polygons     =>  type: Data< helper::vector > > polygons;

For 3D elements:
  tetrahedra   =>  type: Data< helper::vector< helper::fixed_array  > > tetrahedra;
  hexahedra    =>  type: Data< helper::vector< helper::fixed_array  > > hexahedra;
```

Standard names for
**\[doxygen:sofa::core::componentmodel::loader::ImageLoader
ImageLoader\]**:

``` {.ignore:true}
 Not yet implemented.
```

#### Generic mesh loaders

This is a list of the loaders available in SOFA, with their specific
Data. **\[doxygen:sofa::component::loader::MeshGmshLoader
MeshGmshLoader\]**: (example in:
*Sofa/examples/Components/loader/MeshGmshLoader.scn*)

``` {.ignore:true}
No other Data.
```

**\[doxygen:sofa::component::loader::MeshObjLoader MeshObjLoader\]**:
(example in: *Sofa/examples/Components/loader/MeshObjLoader.scn*)

``` {.ignore:true}
  texturesList =>  type: Data  > > texturesList;
  texcoords    =>  type: Data< helper::vector< sofa::defaulttype::Vector2> > texCoords;
  normalsList  =>  type: Data  > > normalsList;
  normals      =>  type: Data< helper::vector< sofa::defaulttype::Vector3> > normals;

  Data  > materials;
    With Material, a inner class of MeshObjLoader
```

**\[doxygen:sofa::component::loader::MeshTrianLoader
MeshTrianLoader\]**: (example in:
*Sofa/examples/Components/loader/MeshTrianLoader.scn*)

``` {.ignore:true}
  neighborTable          => type: Data  > > neighborTable;
  edgesOnBorder          => type: Data  > > edgesOnBorder;
  trianglesOnBorderList  => type: Data < helper::vector  > trianglesOnBorderList;
```

**\[doxygen:sofa::component::loader::MeshVTKLoader MeshVTKLoader\]**:
(example in: *Sofa/examples/Components/loader/MeshVTKLoader.scn*)

``` {.ignore:true}
  No other Data. For the moment.
```

**\[doxygen:sofa::component::loader::MeshXspLoader MeshXspLoader\]**:

``` {.ignore:true}
  gravity      =>  type: Data  > gravity;
  viscosity    =>  type: Data  > viscosity;
```

#### Current architecture of MeshLoader/ImageLoader

TODO
