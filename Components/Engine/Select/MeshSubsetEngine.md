# MeshSubsetEngine

Extract a mesh subset based on selected vertices


__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.Component.Engine.Select`

__namespace__: `#!c++ sofa::component::engine::select`

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
		<td>inputEdges</td>
		<td>
input edges
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
		<td>indices</td>
		<td>
Index lists of the selected vertices
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Vertices of mesh subset
</td>
		<td></td>
	</tr>
	<tr>
		<td>edges</td>
		<td>
edges of mesh subset
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
Triangles of mesh subset
</td>
		<td></td>
	</tr>
	<tr>
		<td>quads</td>
		<td>
Quads of mesh subset
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

Component/Engine/Select/MeshSubsetEngine.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node 	name="root" gravity="0 -1 0" dt="0.05"  >
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI MeshSubsetEngine] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.Setting"/> <!-- Needed to use components [BackgroundSetting] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <BackgroundSetting color="1 1 1"/>
        <DefaultAnimationLoop/>
        
        <MeshOBJLoader name="loader" filename="mesh/dragon.obj" />
        <BoxROI name="boxroi" template="Vec3" position="@loader.position" box="-15 0 -5 0 10 5" drawBoxes="1"/>
        <MeshSubsetEngine name="engine" inputPosition="@loader.position" inputTriangles="@loader.triangles" inputQuads="@loader.quads" indices="@boxroi.indices"/>
    
        <MeshOBJLoader name="meshLoader_0" filename="mesh/dragon.obj" handleSeams="1" />
        <OglModel name="Original Mesh (red)" src="@meshLoader_0" color="1 0 0 0.4" dz="0" />
        <OglModel name="Subset Mesh (blue)" position="@engine.position" triangles="@engine.triangles" quads="@engine.quads" color="0 0.4 1 1"  />
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -1 0", dt="0.05")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.Setting")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
        root.addObject('BackgroundSetting', color="1 1 1")
        root.addObject('DefaultAnimationLoop')
        root.addObject('MeshOBJLoader', name="loader", filename="mesh/dragon.obj")
        root.addObject('BoxROI', name="boxroi", template="Vec3", position="@loader.position", box="-15 0 -5 0 10 5", drawBoxes="1")
        root.addObject('MeshSubsetEngine', name="engine", inputPosition="@loader.position", inputTriangles="@loader.triangles", inputQuads="@loader.quads", indices="@boxroi.indices")
        root.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/dragon.obj", handleSeams="1")
        root.addObject('OglModel', name="Original Mesh (red)", src="@meshLoader_0", color="1 0 0 0.4", dz="0")
        root.addObject('OglModel', name="Subset Mesh (blue)", position="@engine.position", triangles="@engine.triangles", quads="@engine.quads", color="0 0.4 1 1")
    ```

