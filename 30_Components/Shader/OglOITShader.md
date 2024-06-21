# OglOITShader

OglOITShader


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



