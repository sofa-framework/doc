<!-- generate_doc -->
# ExtrudeQuadsAndGenerateHexas

This engine extrudes a quad-based surface into a set of hexahedral elements


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.Engine.Generate

__namespace__: sofa::component::engine::generate

__parents__:

- DataEngine

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
		<td>isVisible</td>
		<td>
is Visible ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>scale</td>
		<td>
Apply a scaling factor to the extruded mesh
		</td>
		<td>1 1 1</td>
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
		<td>numberOfSlices</td>
		<td>
Number of slices / steps in the extrusion
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>flipNormals</td>
		<td>
If true, will inverse point order when creating hexa
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>surfaceVertices</td>
		<td>
Position coordinates of the surface
		</td>
		<td></td>
	</tr>
	<tr>
		<td>surfaceQuads</td>
		<td>
Indices of the quads of the surface to extrude
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
		<td>extrudedSurfaceQuads</td>
		<td>
List of new surface quads generated during the extrusion
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
	<tr>
		<td>extrudedHexas</td>
		<td>
List of hexahedra generated during the extrusion
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
