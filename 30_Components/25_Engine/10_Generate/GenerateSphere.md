# GenerateSphere

Generate a sphereical (Bezier) Tetrahedral and Triangular Mesh


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
		<td>BezierTetrahedronDegree</td>
		<td>
order of Bezier tetrahedra
</td>
		<td></td>
	</tr>
	<tr>
		<td>BezierTriangleDegree</td>
		<td>
order of Bezier triangles
</td>
		<td></td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
input sphere radius
</td>
		<td>0.2</td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>origin</td>
		<td>
sphere center point
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>tessellationDegree</td>
		<td>
Degree of tessellation of each Platonic triangulation
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>platonicSolid</td>
		<td>
name of the Platonic triangulation used to create the spherical dome : either "tetrahedron", "octahedron" or "icosahedron"
</td>
		<td>icosahedron</td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>output_TetrahedraPosition</td>
		<td>
output array of 3d points of tetrahedra mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedra</td>
		<td>
output mesh tetrahedra
</td>
		<td></td>
	</tr>
	<tr>
		<td>output_TrianglesPosition</td>
		<td>
output array of 3d points of triangle mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
output triangular mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>BezierTetrahedronWeights</td>
		<td>
weights of rational Bezier tetrahedra
</td>
		<td></td>
	</tr>
	<tr>
		<td>isBezierTetrahedronRational</td>
		<td>
booleans indicating if each Bezier tetrahedron is rational or integral
</td>
		<td></td>
	</tr>
	<tr>
		<td>BezierTriangleWeights</td>
		<td>
weights of rational Bezier triangles
</td>
		<td></td>
	</tr>
	<tr>
		<td>isBezierTriangleRational</td>
		<td>
booleans indicating if each Bezier triangle is rational or integral
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



