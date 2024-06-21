# OglFluidModel

Particle model for OpenGL display, using glsl


__Templates__:

- `#!c++ Vec3d`

__Target__: `SofaSphFluid`

__namespace__: `#!c++ sofa::component::visualmodel`

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
		<td>position</td>
		<td>
Vertices coordinates
</td>
		<td></td>
	</tr>
	<tr>
		<td>debugFBO</td>
		<td>
DEBUG FBO
</td>
		<td>9</td>
	</tr>
	<tr>
		<td>spriteRadius</td>
		<td>
Radius of sprites
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>spriteThickness</td>
		<td>
Thickness of sprites
</td>
		<td>0.01</td>
	</tr>
	<tr>
		<td>spriteBlurRadius</td>
		<td>
Blur radius (in pixels)
</td>
		<td>10</td>
	</tr>
	<tr>
		<td>spriteBlurScale</td>
		<td>
Blur scale
</td>
		<td>0.1</td>
	</tr>
	<tr>
		<td>spriteBlurDepthFalloff</td>
		<td>
Blur Depth Falloff
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>spriteDiffuseColor</td>
		<td>
Diffuse Color
</td>
		<td>0 0 1 1</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|



