---
title: MeshSTLLoader
---

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
<!-- automatically generated doc START -->
__Target__: `Sofa.Component.IO.Mesh`

__namespace__: `#!c++ sofa::component::io::mesh`

__parents__: 

- `#!c++ MeshLoader`

__categories__: 

- Loader

Data: 

<table>
<thead>
    <tr>
        <th>Name</th>
        <th>Description</th>
        <th>Default value</th>
    </tr>
</thead>
<tbody>
	<tr>
		<td>name</td>
		<td>
object name
</td>
		<td>unnamed</td>
	</tr>
	<tr>
		<td>printLog</td>
		<td>
if true, emits extra messages at runtime.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>tags</td>
		<td>
list of the subsets the objet belongs to
</td>
		<td></td>
	</tr>
	<tr>
		<td>bbox</td>
		<td>
this object bounding box
</td>
		<td></td>
	</tr>
	<tr>
		<td>componentState</td>
		<td>
The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
</td>
		<td>Undefined</td>
	</tr>
	<tr>
		<td>listening</td>
		<td>
if true, handle the events, otherwise ignore the events
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>filename</td>
		<td>
Filename of the object
</td>
		<td></td>
	</tr>
	<tr>
		<td>flipNormals</td>
		<td>
Flip Normals
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>triangulate</td>
		<td>
Divide all polygons into triangles
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>createSubelements</td>
		<td>
Divide all n-D elements into their (n-1)-D boundary elements (e.g. tetrahedra to triangles)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>onlyAttachedPoints</td>
		<td>
Only keep points attached to elements of the mesh
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>translation</td>
		<td>
Translation of the DOFs
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>rotation</td>
		<td>
Rotation of the DOFs
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>scale3d</td>
		<td>
Scale of the DOFs in 3 dimensions
</td>
		<td>1 1 1</td>
	</tr>
	<tr>
		<td>transformation</td>
		<td>
4x4 Homogeneous matrix to transform the DOFs (when present replace any)
</td>
		<td>[1 0 0 0,0 1 0 0,0 0 1 0,0 0 0 1]</td>
	</tr>
	<tr>
		<td>headerSize</td>
		<td>
Size of the header binary file (just before the number of facet).
</td>
		<td>80</td>
	</tr>
	<tr>
		<td>forceBinary</td>
		<td>
Force reading in binary mode. Even in first keyword of the file is solid.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>mergePositionUsingMap</td>
		<td>
Since positions are duplicated in a STL, they have to be merged. Using a map to do so will temporarily duplicate memory but should be more efficient. Disable it if memory is really an issue.
</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Groups</td>
	</tr>
	<tr>
		<td>edgesGroups</td>
		<td>
Groups of Edges
</td>
		<td></td>
	</tr>
	<tr>
		<td>trianglesGroups</td>
		<td>
Groups of Triangles
</td>
		<td></td>
	</tr>
	<tr>
		<td>quadsGroups</td>
		<td>
Groups of Quads
</td>
		<td></td>
	</tr>
	<tr>
		<td>polygonsGroups</td>
		<td>
Groups of Polygons
</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedraGroups</td>
		<td>
Groups of Tetrahedra
</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedraGroups</td>
		<td>
Groups of Hexahedra
</td>
		<td></td>
	</tr>
	<tr>
		<td>pentahedraGroups</td>
		<td>
Groups of Pentahedra
</td>
		<td></td>
	</tr>
	<tr>
		<td>pyramidsGroups</td>
		<td>
Groups of Pyramids
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Vectors</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Vertices of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>polylines</td>
		<td>
Polylines of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>edges</td>
		<td>
Edges of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
Triangles of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>quads</td>
		<td>
Quads of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>polygons</td>
		<td>
Polygons of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>highOrderEdgePositions</td>
		<td>
High order edge points of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>highOrderTrianglePositions</td>
		<td>
High order triangle points of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>highOrderQuadPositions</td>
		<td>
High order quad points of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedra</td>
		<td>
Tetrahedra of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedra</td>
		<td>
Hexahedra of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>pentahedra</td>
		<td>
Pentahedra of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>highOrderTetrahedronPositions</td>
		<td>
High order tetrahedron points of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>highOrderHexahedronPositions</td>
		<td>
High order hexahedron points of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>pyramids</td>
		<td>
Pyramids of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>normals</td>
		<td>
Normals of the mesh loaded
</td>
		<td></td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|



## Examples

Component/IO/Mesh/MeshSTLLoader.scn

=== "XML"

    ```xml
    <!-- For more details see: https://wiki.sofa-framework.org/tdev/wiki/Notes/NewLoaderArchitecture -->
    <Node>
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshSTLLoader] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <VisualStyle displayFlags="showVisual" />
    
        <DefaultAnimationLoop/>
        <MeshSTLLoader name="STLLoader" filename="mesh/circle_knot_ascii.stl" printLog="true" flipNormals="0" />
        <OglModel src="@STLLoader" name="VisualModel" color="red" />
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        rootNode = rootNode.addChild('rootNode')
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        rootNode.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        rootNode.addObject('VisualStyle', displayFlags="showVisual")
        rootNode.addObject('DefaultAnimationLoop')
        rootNode.addObject('MeshSTLLoader', name="STLLoader", filename="mesh/circle_knot_ascii.stl", printLog="true", flipNormals="0")
        rootNode.addObject('OglModel', src="@STLLoader", name="VisualModel", color="red")
    ```

Component/IO/Mesh/MeshSTLLoader_binary.scn

=== "XML"

    ```xml
    <!-- For more details see: https://wiki.sofa-framework.org/tdev/wiki/Notes/NewLoaderArchitecture -->
    <Node>
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshSTLLoader] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <VisualStyle displayFlags="showVisual" />
        <DefaultAnimationLoop/>
    
        <MeshSTLLoader name="STLLoader" filename="mesh/pliers_binary.stl" printLog="true" />
        <OglModel src="@STLLoader" name="VisualModel" color="red" />
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        rootNode = rootNode.addChild('rootNode')
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        rootNode.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        rootNode.addObject('VisualStyle', displayFlags="showVisual")
        rootNode.addObject('DefaultAnimationLoop')
        rootNode.addObject('MeshSTLLoader', name="STLLoader", filename="mesh/pliers_binary.stl", printLog="true")
        rootNode.addObject('OglModel', src="@STLLoader", name="VisualModel", color="red")
    ```


<!-- automatically generated doc END -->
