#### Exporting in VTK format

In this section, we will explain how to export a 3D object in a VTK
format file.

##### How to use it

Put :

into a node where a BaseMeshTopology exists.

-   filename = : where to save exported VTK file
-   edges/triangles/quads/tetras/hexas= : which primitive you want to
    export (at least one type is required)
-   pointsDataFields= where string= : indicates where the exporter will
    get its values to put on the points. Obviously, the number of values
    has to be the same as the number of points. Several data can be
    listed, just separate them with a space.
-   cellsDataFields= where string= : the same as the points. You must
    notice that, for now, the mapping between a primitive and a value is
    not possible. Consequently, only one primitive can get values (as
    the number of values must equal the number of cells)

 

##### Limitations

For now, this class supports only , for the data, Vec{1,2}{f/d} as an
array of values and Vec3{f/d} as an array of vectors ('real' vector with
arrow and so on ...) The export is processed when Control+E keys are
pressed.Don't forget to set listening to true.  

##### Example

-   example/Component/misc/VTKExporter.scn

[![Example\_vtkexporter\_paraview](https://www.sofa-framework.org/wp-content/uploads/2014/11/Example_vtkexporter_paraview.jpg){.size-full
.wp-image-1624 .aligncenter width="600"
height="357"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/Example_vtkexporter_paraview.jpg)
 

#### Reconstruct VTK mesh in ParaView

The **VTKExporter** component will export the mesh as a "*VTK
Unstructured Grid*". This part will explain how to get back a "*VTK
Polygonal Mesh*" which could be reload in SOFA. This pipeline has been
realised using ParaView release 3.6.2.

-   Step 1: Open your export file: example.vtk0.vtu (File -&gt; Open).
-   Step 2: unselect "position" and then apply.
-   Step 3: Extract Surface (Filters-&gt; Extract Surface), and apply.
-   Step 4: Save Data as VTK file, either in ascii or binary (File -&gt;
    Save Data).

You can now use the component **MeshVTKLoader** to load this mesh in
SOFA. Additionally, if you want to save only the principal component of
the mesh (remove small elements) Between step 2 and 3 do:

-   Step 2.1: Filter -&gt; Connectivity, and apply.
-   Step 2.2: Filter -&gt; Threshold, and change the boundary to keep
    region between 0 and 1

