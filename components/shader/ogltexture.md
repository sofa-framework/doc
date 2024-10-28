<!-- generate_doc -->
# OglTexture

OglTexture


__Target__: Sofa.GL.Component.Shader

__namespace__: sofa::gl::component::shader

__parents__:

- VisualModel
- ShaderElement

### Data

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
list of the subsets the object belongs to
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
		<td>id</td>
		<td>
Set an ID name
		</td>
		<td></td>
	</tr>
	<tr>
		<td>indexShader</td>
		<td>
Set the index of the desired shader you want to apply this parameter
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>filename</td>
		<td>
Texture Filename
		</td>
		<td></td>
	</tr>
	<tr>
		<td>textureUnit</td>
		<td>
Set the texture unit
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>enabled</td>
		<td>
enabled ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>repeat</td>
		<td>
Repeat Texture ?
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>linearInterpolation</td>
		<td>
Interpolate Texture ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>generateMipmaps</td>
		<td>
Generate mipmaps ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>srgbColorspace</td>
		<td>
SRGB colorspace ?
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>minLod</td>
		<td>
Minimum mipmap lod ?
		</td>
		<td>-1000</td>
	</tr>
	<tr>
		<td>maxLod</td>
		<td>
Maximum mipmap lod ?
		</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>proceduralTextureWidth</td>
		<td>
Width of procedural Texture
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>proceduralTextureHeight</td>
		<td>
Height of procedural Texture
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>proceduralTextureNbBits</td>
		<td>
Nb bits per color
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>proceduralTextureData</td>
		<td>
Data of procedural Texture 
		</td>
		<td></td>
	</tr>
	<tr>
		<td>cubemapFilenamePosX</td>
		<td>
Texture filename of positive-X cubemap face
		</td>
		<td></td>
	</tr>
	<tr>
		<td>cubemapFilenamePosY</td>
		<td>
Texture filename of positive-Y cubemap face
		</td>
		<td></td>
	</tr>
	<tr>
		<td>cubemapFilenamePosZ</td>
		<td>
Texture filename of positive-Z cubemap face
		</td>
		<td></td>
	</tr>
	<tr>
		<td>cubemapFilenameNegX</td>
		<td>
Texture filename of negative-X cubemap face
		</td>
		<td></td>
	</tr>
	<tr>
		<td>cubemapFilenameNegY</td>
		<td>
Texture filename of negative-Y cubemap face
		</td>
		<td></td>
	</tr>
	<tr>
		<td>cubemapFilenameNegZ</td>
		<td>
Texture filename of negative-Z cubemap face
		</td>
		<td></td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|

