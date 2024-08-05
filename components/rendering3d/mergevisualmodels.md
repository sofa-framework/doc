# MergeVisualModels

Merge several visual models


__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.GL.Component.Rendering3D`

__namespace__: `#!c++ sofa::gl::component::rendering3d`

__parents__: 

- `#!c++ OglModel`

__categories__: 

- VisualModel

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
		<td>initRestPositions</td>
		<td>
True if rest positions must be initialized with initial positions
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>useNormals</td>
		<td>
True if normal smoothing groups should be read from file
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>updateNormals</td>
		<td>
True if normals should be updated at each iteration
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>computeTangents</td>
		<td>
True if tangents should be computed at startup
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>updateTangents</td>
		<td>
True if tangents should be updated at each iteration
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>handleDynamicTopology</td>
		<td>
True if topological changes should be handled
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>fixMergedUVSeams</td>
		<td>
True if UV seams should be handled even when duplicate UVs are merged
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>keepLines</td>
		<td>
keep and draw lines (false by default)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>vertPosIdx</td>
		<td>
If vertices have multiple normals/texcoords stores vertices position indices
</td>
		<td></td>
	</tr>
	<tr>
		<td>vertNormIdx</td>
		<td>
If vertices have multiple normals/texcoords stores vertices normal indices
</td>
		<td></td>
	</tr>
	<tr>
		<td>filename</td>
		<td>
 Path to an ogl model
</td>
		<td></td>
	</tr>
	<tr>
		<td>texturename</td>
		<td>
Name of the Texture
</td>
		<td></td>
	</tr>
	<tr>
		<td>scaleTex</td>
		<td>
Scale of the texture
</td>
		<td>1 1</td>
	</tr>
	<tr>
		<td>translationTex</td>
		<td>
Translation of the texture
</td>
		<td>0 0</td>
	</tr>
	<tr>
		<td>material</td>
		<td>
Material
</td>
		<td></td>
	</tr>
	<tr>
		<td>putOnlyTexCoords</td>
		<td>
Give Texture Coordinates without the texture binding
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>srgbTexturing</td>
		<td>
When sRGB rendering is enabled, is the texture in sRGB colorspace?
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>materials</td>
		<td>
List of materials
</td>
		<td></td>
	</tr>
	<tr>
		<td>groups</td>
		<td>
Groups of triangles and quads using a given material
</td>
		<td></td>
	</tr>
	<tr>
		<td>blendTranslucency</td>
		<td>
Blend transparent parts
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>premultipliedAlpha</td>
		<td>
is alpha premultiplied ?
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>writeZTransparent</td>
		<td>
Write into Z Buffer for Transparent Object
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>alphaBlend</td>
		<td>
Enable alpha blending
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>depthTest</td>
		<td>
Enable depth testing
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>cullFace</td>
		<td>
Face culling (0 = no culling, 1 = cull back faces, 2 = cull front faces)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>lineWidth</td>
		<td>
Line width (set if != 1, only for lines rendering)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>pointSize</td>
		<td>
Point size (set if != 1, only for points rendering)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>lineSmooth</td>
		<td>
Enable smooth line rendering
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>pointSmooth</td>
		<td>
Enable smooth point rendering
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>primitiveType</td>
		<td>
Select types of primitives to send (necessary for some shader types such as geometry or tesselation)
</td>
		<td></td>
	</tr>
	<tr>
		<td>blendEquation</td>
		<td>
if alpha blending is enabled this specifies how source and destination colors are combined
</td>
		<td></td>
	</tr>
	<tr>
		<td>sfactor</td>
		<td>
if alpha blending is enabled this specifies how the red, green, blue, and alpha source blending factors are computed
</td>
		<td></td>
	</tr>
	<tr>
		<td>dfactor</td>
		<td>
if alpha blending is enabled this specifies how the red, green, blue, and alpha destination blending factors are computed
</td>
		<td></td>
	</tr>
	<tr>
		<td>nb</td>
		<td>
number of input visual models to merge
</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Transformation</td>
	</tr>
	<tr>
		<td>translation</td>
		<td>
Initial Translation of the object
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>rotation</td>
		<td>
Initial Rotation of the object
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>scale3d</td>
		<td>
Initial Scale of the object
</td>
		<td>1 1 1</td>
	</tr>
	<tr>
		<td colspan="3">Vector</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Vertices coordinates
</td>
		<td></td>
	</tr>
	<tr>
		<td>restPosition</td>
		<td>
Vertices rest coordinates
</td>
		<td></td>
	</tr>
	<tr>
		<td>normal</td>
		<td>
Normals of the model
</td>
		<td></td>
	</tr>
	<tr>
		<td>vertices</td>
		<td>
vertices of the model (only if vertices have multiple normals/texcoords, otherwise positions are used)
</td>
		<td></td>
	</tr>
	<tr>
		<td>texcoords</td>
		<td>
coordinates of the texture
</td>
		<td></td>
	</tr>
	<tr>
		<td>tangents</td>
		<td>
tangents for normal mapping
</td>
		<td></td>
	</tr>
	<tr>
		<td>bitangents</td>
		<td>
tangents for normal mapping
</td>
		<td></td>
	</tr>
	<tr>
		<td>edges</td>
		<td>
edges of the model
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
triangles of the model
</td>
		<td></td>
	</tr>
	<tr>
		<td>quads</td>
		<td>
quads of the model
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
|topology|link to the topology container|
|input1|input visual model(1)|



## Examples

Component/Visual/MergeVisualModels.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01">
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [MergeVisualModels OglModel] -->
        <DefaultAnimationLoop/>
    
        <MeshOBJLoader name="meshLoader" filename="mesh/snake_body.obj" handleSeams="1"/>
        <MeshTopology src="@meshLoader"/>
    
        <OglModel name="visualModel1" src="@meshLoader" useNormals="0" translation="0 0 0" />
        <OglModel name="visualModel2" src="@meshLoader" useNormals="0" translation="10 0 0"/>
        <OglModel name="visualModel3" src="@meshLoader" useNormals="0" translation="20 0 0"/>
        
    
        <MergeVisualModels name="merged" nb="2" input1="@visualModel1"  input2="@visualModel3"   texturename="textures/snakeColorMap.png" color="red"  />
        
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')
        root.addObject('MeshOBJLoader', name="meshLoader", filename="mesh/snake_body.obj", handleSeams="1")
        root.addObject('MeshTopology', src="@meshLoader")
        root.addObject('OglModel', name="visualModel1", src="@meshLoader", useNormals="0", translation="0 0 0")
        root.addObject('OglModel', name="visualModel2", src="@meshLoader", useNormals="0", translation="10 0 0")
        root.addObject('OglModel', name="visualModel3", src="@meshLoader", useNormals="0", translation="20 0 0")
        root.addObject('MergeVisualModels', name="merged", nb="2", input1="@visualModel1", input2="@visualModel3", texturename="textures/snakeColorMap.png", color="red")
    ```

