# OglSceneFrame

Display a frame at the corner of the scene view


__Target__: `Sofa.GL.Component.Rendering3D`

__namespace__: `#!c++ sofa::gl::component::rendering3d`

__parents__: 

- `#!c++ VisualModel`

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
		<td>enable</td>
		<td>
Display the object or not
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>style</td>
		<td>
Style of the frame
</td>
		<td></td>
	</tr>
	<tr>
		<td>alignment</td>
		<td>
Alignment of the frame in the view
</td>
		<td></td>
	</tr>
	<tr>
		<td>viewportSize</td>
		<td>
Size of the viewport where the frame is rendered
</td>
		<td>150</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>draw</td>
		<td>
Display the frame or not
</td>
		<td>1</td>
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

Component/Visual/OglSceneFrame.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.01">
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel OglSceneFrame] -->
        <DefaultAnimationLoop/>
        
        <MeshOBJLoader name="meshLoader_0" filename="mesh/liver-smooth.obj" handleSeams="1" />
        <OglModel name="VisualModel" src="@meshLoader_0" color="red" />
        <!-- <OglSceneFrame style="0"/> -->
        <OglSceneFrame style="1"/>
        <!-- <OglSceneFrame style="2"/> -->
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')
        root.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/liver-smooth.obj", handleSeams="1")
        root.addObject('OglModel', name="VisualModel", src="@meshLoader_0", color="red")
        root.addObject('OglSceneFrame', style="1")
    ```

