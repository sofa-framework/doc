# ExtrudeEdgesAndGenerateQuads

This engine extrudes an edge-based curve into a quad surface patch


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
		<td>extrudeDirection</td>
		<td>
Direction along which to extrude the curve
</td>
		<td>1 0 0</td>
	</tr>
	<tr>
		<td>thicknessIn</td>
		<td>
Thickness of the extruded volume in the opposite direction of the normals
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>thicknessOut</td>
		<td>
Thickness of the extruded volume in the direction of the normals
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>numberOfSections</td>
		<td>
Number of sections / steps in the extrusion
</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>curveVertices</td>
		<td>
Position coordinates along the initial curve
</td>
		<td></td>
	</tr>
	<tr>
		<td>curveEdges</td>
		<td>
Indices of the edges of the curve to extrude
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>extrudedVertices</td>
		<td>
Coordinates of the extruded vertices
</td>
		<td></td>
	</tr>
	<tr>
		<td>extrudedEdges</td>
		<td>
List of all edges generated during the extrusion
</td>
		<td></td>
	</tr>
	<tr>
		<td>extrudedQuads</td>
		<td>
List of all quads generated during the extrusion
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



