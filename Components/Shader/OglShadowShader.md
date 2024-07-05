# OglShadowShader

This component sets the shader system responsible of the shadowing.


__Target__: `Sofa.GL.Component.Shader`

__namespace__: `#!c++ sofa::gl::component::shader`

__parents__: 

- `#!c++ OglShader`

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
		<td>turnOn</td>
		<td>
Turn On the shader?
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>passive</td>
		<td>
Will this shader be activated manually or automatically?
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>fileVertexShaders</td>
		<td>
Set the vertex shader filename to load
</td>
		<td>[ 'shaders/toonShading.vert' ]</td>
	</tr>
	<tr>
		<td>fileFragmentShaders</td>
		<td>
Set the fragment shader filename to load
</td>
		<td>[ 'shaders/toonShading.frag' ]</td>
	</tr>
	<tr>
		<td>fileGeometryShaders</td>
		<td>
Set the geometry shader filename to load
</td>
		<td></td>
	</tr>
	<tr>
		<td>fileTessellationControlShaders</td>
		<td>
Set the tessellation control filename to load
</td>
		<td></td>
	</tr>
	<tr>
		<td>fileTessellationEvaluationShaders</td>
		<td>
Set the tessellation evaluation filename to load
</td>
		<td></td>
	</tr>
	<tr>
		<td>geometryInputType</td>
		<td>
Set input types for the geometry shader
</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>geometryOutputType</td>
		<td>
Set output types for the geometry shader
</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>geometryVerticesOut</td>
		<td>
Set max number of vertices in output for the geometry shader
</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>tessellationOuterLevel</td>
		<td>
For tessellation without control shader: default outer level (edge subdivisions)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>tessellationInnerLevel</td>
		<td>
For tessellation without control shader: default inner level (face subdivisions)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>indexActiveShader</td>
		<td>
Set current active shader
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>backfaceWriting</td>
		<td>
it enables writing to gl_BackColor inside a GLSL vertex shader
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>clampVertexColor</td>
		<td>
clamp the vertex color between 0 and 1
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

Component/Visual/OglShadowShader_SpotLight2.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node 	 name="root"  dt="0.02"  >
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.Setting"/> <!-- Needed to use components [BackgroundSetting] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="Sofa.GL.Component.Shader"/> <!-- Needed to use components [LightManager OglShaderDefineMacro OglShadowShader OglTexture SpotLight] -->
        
        <DefaultAnimationLoop/>
    	<BackgroundSetting color="0.8 0.8 0.8" />
    	<LightManager name="lightManager1"  listening="1"  shadows="1"  softShadows="1" />
    	
    	<SpotLight name="spotLight1"  shadowTextureSize="2048"  position="0 5 -15"  direction="0 -0.2 1"  cutoff="45" />
    	<SpotLight name="spotLight2"  shadowTextureSize="128"  position="0 5 10"  direction="0 -0.2 -1"  cutoff="45"  />
    	
    	<Node name="shader1">
    		<OglShadowShader name="oglShadowShader1" />
    
    		<MeshOBJLoader name="meshLoader_0" filename="mesh/dragon.obj"  translation="0 0 -5"  scale3d="0.3 0.3 0.3" handleSeams="1" />
    		<OglModel template="Vec3" name="VisualModel" src="@meshLoader_0"  material="Default Diffuse 1 0 1 0 1 Ambient 1 0 0.2 0 1 Specular 0 0 1 0 1 Emissive 0 0 1 0 1 Shininess 0 45 No texture linked to the material No bump texture linked to the material "  blendEquation="GL_FUNC_ADD"  sfactor="GL_SRC_ALPHA"  dfactor="GL_ONE_MINUS_SRC_ALPHA" />
    	</Node>
    	<Node name="shader2">
    		<OglShadowShader name="oglShadowShader1" />
     		<OglTexture textureFilename="textures/ice_chess.bmp" indexShader="0" id="colorTexture" textureUnit="0"  repeat="true" />
    		<OglTexture textureFilename="textures/ice_chess.bmp" indexShader="1" id="colorTexture" textureUnit="1"  repeat="true" />
    		
    		<OglShaderDefineMacro id="USE_TEXTURE" indexShader="0" />
    		<OglShaderDefineMacro id="USE_TEXTURE" indexShader="1" />
    
    		<MeshOBJLoader name="meshLoader_1" filename="mesh/floor2.obj"  translation="0 -2.5 0"  scale3d="1 1 1" handleSeams="1" />
    		<OglModel template="Vec3"  putOnlyTexCoords="true" name="FloorV" src="@meshLoader_1"  material="Default Diffuse 1 0.5 0.5 0.5 1 Ambient 1 0.1 0.1 0.1 1 Specular 0 0.5 0.5 0.5 1 Emissive 0 0.5 0.5 0.5 1 Shininess 0 45 No texture linked to the material No bump texture linked to the material "  blendEquation="GL_FUNC_ADD"  sfactor="GL_SRC_ALPHA"  dfactor="GL_ONE_MINUS_SRC_ALPHA" />	
    	</Node>
    
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.Setting")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Shader")
        root.addObject('DefaultAnimationLoop')
        root.addObject('BackgroundSetting', color="0.8 0.8 0.8")
        root.addObject('LightManager', name="lightManager1", listening="1", shadows="1", softShadows="1")
        root.addObject('SpotLight', name="spotLight1", shadowTextureSize="2048", position="0 5 -15", direction="0 -0.2 1", cutoff="45")
        root.addObject('SpotLight', name="spotLight2", shadowTextureSize="128", position="0 5 10", direction="0 -0.2 -1", cutoff="45")

        shader1 = root.addChild('shader1')
        shader1.addObject('OglShadowShader', name="oglShadowShader1")
        shader1.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/dragon.obj", translation="0 0 -5", scale3d="0.3 0.3 0.3", handleSeams="1")
        shader1.addObject('OglModel', template="Vec3", name="VisualModel", src="@meshLoader_0", material="Default Diffuse 1 0 1 0 1 Ambient 1 0 0.2 0 1 Specular 0 0 1 0 1 Emissive 0 0 1 0 1 Shininess 0 45 No texture linked to the material No bump texture linked to the material ", blendEquation="GL_FUNC_ADD", sfactor="GL_SRC_ALPHA", dfactor="GL_ONE_MINUS_SRC_ALPHA")

        shader2 = root.addChild('shader2')
        shader2.addObject('OglShadowShader', name="oglShadowShader1")
        shader2.addObject('OglTexture', textureFilename="textures/ice_chess.bmp", indexShader="0", id="colorTexture", textureUnit="0", repeat="true")
        shader2.addObject('OglTexture', textureFilename="textures/ice_chess.bmp", indexShader="1", id="colorTexture", textureUnit="1", repeat="true")
        shader2.addObject('OglShaderDefineMacro', id="USE_TEXTURE", indexShader="0")
        shader2.addObject('OglShaderDefineMacro', id="USE_TEXTURE", indexShader="1")
        shader2.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/floor2.obj", translation="0 -2.5 0", scale3d="1 1 1", handleSeams="1")
        shader2.addObject('OglModel', template="Vec3", putOnlyTexCoords="true", name="FloorV", src="@meshLoader_1", material="Default Diffuse 1 0.5 0.5 0.5 1 Ambient 1 0.1 0.1 0.1 1 Specular 0 0.5 0.5 0.5 1 Emissive 0 0.5 0.5 0.5 1 Shininess 0 45 No texture linked to the material No bump texture linked to the material ", blendEquation="GL_FUNC_ADD", sfactor="GL_SRC_ALPHA", dfactor="GL_ONE_MINUS_SRC_ALPHA")
    ```

Component/Visual/OglShadowShader_SpotLight.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node 	 name="root"  dt="0.02"  >
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="Sofa.GL.Component.Shader"/> <!-- Needed to use components [LightManager OglShadowShader SpotLight] -->
        <DefaultAnimationLoop/>
        
    	<MeshOBJLoader name="meshLoader_0" filename="mesh/dragon.obj"  translation="0 0 -5"  scale3d="0.3 0.3 0.3" handleSeams="1" />
    	<OglModel template="Vec3" name="VisualModel" src="@meshLoader_0"  material="Default Diffuse 1 0 1 0 1 Ambient 1 0 0.2 0 1 Specular 0 0 1 0 1 Emissive 0 0 1 0 1 Shininess 0 45 No texture linked to the material No bump texture linked to the material "  blendEquation="GL_FUNC_ADD"  sfactor="GL_SRC_ALPHA"  dfactor="GL_ONE_MINUS_SRC_ALPHA" />
    	<MeshOBJLoader name="meshLoader_1" filename="mesh/floor.obj"  translation="0 -2.5 0"  scale3d="1 1 1" handleSeams="1" />
    	<OglModel template="Vec3" name="FloorV" src="@meshLoader_1"  material="Default Diffuse 1 0.5 0.5 0.5 1 Ambient 1 0.1 0.1 0.1 1 Specular 0 0.5 0.5 0.5 1 Emissive 0 0.5 0.5 0.5 1 Shininess 0 45 No texture linked to the material No bump texture linked to the material "  blendEquation="GL_FUNC_ADD"  sfactor="GL_SRC_ALPHA"  dfactor="GL_ONE_MINUS_SRC_ALPHA" />
    	<LightManager name="lightManager1"  listening="1"  shadows="1"  softShadows="1" />
    	<OglShadowShader name="oglShadowShader1" />
    	<SpotLight name="spotLight1"  shadowTextureSize="2048"  position="0 5 -15"  direction="0 -0.2 1"  cutoff="45" />
    	<SpotLight name="spotLight2"  shadowTextureSize="128"  position="0 5 10"  direction="0 -0.2 -1"  cutoff="45" />
    	<SpotLight name="spotLight3"  shadowTextureSize="512"  position="-15 5 0"  direction="1 -0.2 0"  cutoff="45" />
    	<SpotLight name="spotLight4"  shadowTextureSize="256"  position="10 5 0"  direction="-1 -0.2 0"  cutoff="45" />
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Shader")
        root.addObject('DefaultAnimationLoop')
        root.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/dragon.obj", translation="0 0 -5", scale3d="0.3 0.3 0.3", handleSeams="1")
        root.addObject('OglModel', template="Vec3", name="VisualModel", src="@meshLoader_0", material="Default Diffuse 1 0 1 0 1 Ambient 1 0 0.2 0 1 Specular 0 0 1 0 1 Emissive 0 0 1 0 1 Shininess 0 45 No texture linked to the material No bump texture linked to the material ", blendEquation="GL_FUNC_ADD", sfactor="GL_SRC_ALPHA", dfactor="GL_ONE_MINUS_SRC_ALPHA")
        root.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/floor.obj", translation="0 -2.5 0", scale3d="1 1 1", handleSeams="1")
        root.addObject('OglModel', template="Vec3", name="FloorV", src="@meshLoader_1", material="Default Diffuse 1 0.5 0.5 0.5 1 Ambient 1 0.1 0.1 0.1 1 Specular 0 0.5 0.5 0.5 1 Emissive 0 0.5 0.5 0.5 1 Shininess 0 45 No texture linked to the material No bump texture linked to the material ", blendEquation="GL_FUNC_ADD", sfactor="GL_SRC_ALPHA", dfactor="GL_ONE_MINUS_SRC_ALPHA")
        root.addObject('LightManager', name="lightManager1", listening="1", shadows="1", softShadows="1")
        root.addObject('OglShadowShader', name="oglShadowShader1")
        root.addObject('SpotLight', name="spotLight1", shadowTextureSize="2048", position="0 5 -15", direction="0 -0.2 1", cutoff="45")
        root.addObject('SpotLight', name="spotLight2", shadowTextureSize="128", position="0 5 10", direction="0 -0.2 -1", cutoff="45")
        root.addObject('SpotLight', name="spotLight3", shadowTextureSize="512", position="-15 5 0", direction="1 -0.2 0", cutoff="45")
        root.addObject('SpotLight', name="spotLight4", shadowTextureSize="256", position="10 5 0", direction="-1 -0.2 0", cutoff="45")
    ```

Component/Visual/OglShadowShader_Directional.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node 	 name="root"  dt="0.02"  >
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.Setting"/> <!-- Needed to use components [BackgroundSetting] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="Sofa.GL.Component.Shader"/> <!-- Needed to use components [DirectionalLight LightManager OglShadowShader] -->
    
        <DefaultAnimationLoop/>
    	<BackgroundSetting color="0.5 0.5 0.5" />
    	<MeshOBJLoader name="meshLoader_0" filename="mesh/dragon.obj"  translation="0 0 -5"  scale3d="0.3 0.3 0.3" handleSeams="1" />
    	<OglModel template="Vec3" name="VisualModel" src="@meshLoader_0"  material="Default Diffuse 1 0 1 0 1 Ambient 1 0 0.2 0 1 Specular 0 0 1 0 1 Emissive 0 0 1 0 1 Shininess 0 45 No texture linked to the material No bump texture linked to the material "  blendEquation="GL_FUNC_ADD"  sfactor="GL_SRC_ALPHA"  dfactor="GL_ONE_MINUS_SRC_ALPHA" />
    	
    	<MeshOBJLoader name="meshLoader_1" filename="mesh/floor.obj"  translation="0 -2.5 0"  scale3d="0.5 0.5 0.5" handleSeams="1" />
    	<OglModel template="Vec3" name="FloorV" src="@meshLoader_1"  material="Default Diffuse 1 0.5 0.5 0.8 1 Ambient 1 0.1 0.1 0.1 1 Specular 0 0.5 0.5 0.5 1 Emissive 0 0.5 0.5 0.5 1 Shininess 0 45 No texture linked to the material No bump texture linked to the material "  blendEquation="GL_FUNC_ADD"  sfactor="GL_SRC_ALPHA"  dfactor="GL_ONE_MINUS_SRC_ALPHA" />
    	<LightManager name="lightManager1"  listening="1"  shadows="1"  softShadows="0" />
    	<OglShadowShader name="oglShadowShader1" />
    	<DirectionalLight name="spotLight1"  shadowTextureSize="512" direction="-0.5 -0.5 -0.5"  shadowFactor="1" />
    	<!-- <OglViewport screenPosition="0 0" screenSize="250 250" cameraPosition="-200 0 0" cameraOrientation="0 0.707 0 -0.707" zNear="1" zFar="1000" /> -->
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.Setting")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Shader")
        root.addObject('DefaultAnimationLoop')
        root.addObject('BackgroundSetting', color="0.5 0.5 0.5")
        root.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/dragon.obj", translation="0 0 -5", scale3d="0.3 0.3 0.3", handleSeams="1")
        root.addObject('OglModel', template="Vec3", name="VisualModel", src="@meshLoader_0", material="Default Diffuse 1 0 1 0 1 Ambient 1 0 0.2 0 1 Specular 0 0 1 0 1 Emissive 0 0 1 0 1 Shininess 0 45 No texture linked to the material No bump texture linked to the material ", blendEquation="GL_FUNC_ADD", sfactor="GL_SRC_ALPHA", dfactor="GL_ONE_MINUS_SRC_ALPHA")
        root.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/floor.obj", translation="0 -2.5 0", scale3d="0.5 0.5 0.5", handleSeams="1")
        root.addObject('OglModel', template="Vec3", name="FloorV", src="@meshLoader_1", material="Default Diffuse 1 0.5 0.5 0.8 1 Ambient 1 0.1 0.1 0.1 1 Specular 0 0.5 0.5 0.5 1 Emissive 0 0.5 0.5 0.5 1 Shininess 0 45 No texture linked to the material No bump texture linked to the material ", blendEquation="GL_FUNC_ADD", sfactor="GL_SRC_ALPHA", dfactor="GL_ONE_MINUS_SRC_ALPHA")
        root.addObject('LightManager', name="lightManager1", listening="1", shadows="1", softShadows="0")
        root.addObject('OglShadowShader', name="oglShadowShader1")
        root.addObject('DirectionalLight', name="spotLight1", shadowTextureSize="512", direction="-0.5 -0.5 -0.5", shadowFactor="1")
    ```

