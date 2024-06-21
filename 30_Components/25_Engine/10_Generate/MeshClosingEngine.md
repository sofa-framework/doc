# MeshClosingEngine

Merge several meshes


__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.Component.Engine.Generate`

__namespace__: `#!c++ sofa::component::engine::generate`

__parents__: 

- `#!c++ DataEngine`

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
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>inputPosition</td>
		<td>
input vertices
</td>
		<td></td>
	</tr>
	<tr>
		<td>inputTriangles</td>
		<td>
input triangles
</td>
		<td></td>
	</tr>
	<tr>
		<td>inputQuads</td>
		<td>
input quads
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Vertices of closed mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
Triangles of closed mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>quads</td>
		<td>
Quads of closed mesh (=input quads with current method)
</td>
		<td></td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
Index lists of the closing parts
</td>
		<td></td>
	</tr>
	<tr>
		<td>closingPosition</td>
		<td>
Vertices of the closing parts
</td>
		<td></td>
	</tr>
	<tr>
		<td>closingTriangles</td>
		<td>
Triangles of the closing parts
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

Component/Engine/Generate/MeshClosingEngine.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="0 0 0" dt="1"  >
        <RequiredPlugin name="Sofa.Component.Engine.Generate"/> <!-- Needed to use components [MeshClosingEngine] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.Setting"/> <!-- Needed to use components [BackgroundSetting] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <BackgroundSetting color="1 1 1" />
        <MeshOBJLoader name="mesh" filename="mesh/c_open.obj" triangulate="0"/>
        <MeshClosingEngine name="closer" inputPosition="@mesh.position" inputTriangles="@mesh.triangles" inputQuads="@mesh.quads"/>
    
        <Node name="plain visu of closing area (red)" >
            <OglModel name="closingVisual"  position="@../closer.closingPosition" triangles="@../closer.closingTriangles" color="1 0.1 0.1 1"/>
        </Node>
    
        <Node name="visu of closed mesh (green)" >
            <OglModel name="closedMesh"  position="@../closer.position" vertices="@../closer.position" triangles="@../closer.triangles" quads="@../closer.quads" color="0.5 1 0.5 1" translation="0 0 4"/>
        </Node>
    
        <Node name="visu of original open mesh (wireframe)" >
            <VisualStyle displayFlags="showVisual showWireframe" />
            <OglModel name="visual"  src="@../mesh" color="0.5 0.5 1 1" />
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 0 0", dt="1")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Generate")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.Setting")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')
        root.addObject('BackgroundSetting', color="1 1 1")
        root.addObject('MeshOBJLoader', name="mesh", filename="mesh/c_open.obj", triangulate="0")
        root.addObject('MeshClosingEngine', name="closer", inputPosition="@mesh.position", inputTriangles="@mesh.triangles", inputQuads="@mesh.quads")

        plain visu of closing area (red) = root.addChild('plain visu of closing area (red)')
        plain visu of closing area (red).addObject('OglModel', name="closingVisual", position="@../closer.closingPosition", triangles="@../closer.closingTriangles", color="1 0.1 0.1 1")

        visu of closed mesh (green) = root.addChild('visu of closed mesh (green)')
        visu of closed mesh (green).addObject('OglModel', name="closedMesh", position="@../closer.position", vertices="@../closer.position", triangles="@../closer.triangles", quads="@../closer.quads", color="0.5 1 0.5 1", translation="0 0 4")

        visu of original open mesh (wireframe) = root.addChild('visu of original open mesh (wireframe)')
        visu of original open mesh (wireframe).addObject('VisualStyle', displayFlags="showVisual showWireframe")
        visu of original open mesh (wireframe).addObject('OglModel', name="visual", src="@../mesh", color="0.5 0.5 1 1")
    ```

