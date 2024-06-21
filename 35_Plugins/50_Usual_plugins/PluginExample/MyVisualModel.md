# MyVisualModel

Dummy visual component.


__Templates__:

- `#!c++ Vec3d`

__Target__: `PluginExample`

__namespace__: `#!c++ sofa::component::visual`

__parents__: 

- `#!c++ VisualModelImpl`

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



