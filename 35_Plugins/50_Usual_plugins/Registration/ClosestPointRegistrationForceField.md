# ClosestPointRegistrationForceField

Compute forces based on closest points from/to a target surface/point set


__Templates__:

- `#!c++ Vec3d`

__Target__: `Registration`

__namespace__: `#!c++ sofa::component::forcefield`

__parents__: 

- `#!c++ ForceField`

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
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping - stiffness matrix coefficient
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>stiffness</td>
		<td>
uniform stiffness for the all springs.
</td>
		<td>100</td>
	</tr>
	<tr>
		<td>damping</td>
		<td>
uniform damping for the all springs.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>cacheSize</td>
		<td>
number of closest points used in the cache to speed up closest point computation.
</td>
		<td>5</td>
	</tr>
	<tr>
		<td>blendingFactor</td>
		<td>
blending between projection (=0) and attraction (=1) forces.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>outlierThreshold</td>
		<td>
suppress outliers when distance &gt; (meandistance + threshold*stddev).
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>normalThreshold</td>
		<td>
suppress outliers when normal.closestPointNormal &lt; threshold.
</td>
		<td>0.5</td>
	</tr>
	<tr>
		<td>projectToPlane</td>
		<td>
project closest points in the plane defined by the normal.
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>rejectBorders</td>
		<td>
ignore border vertices.
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>rejectOutsideBbox</td>
		<td>
ignore source points outside bounding box of target points.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>sourceTriangles</td>
		<td>
Triangles of the source mesh.
</td>
		<td></td>
	</tr>
	<tr>
		<td>sourceNormals</td>
		<td>
Normals of the source mesh.
</td>
		<td></td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Vertices of the target mesh.
</td>
		<td></td>
	</tr>
	<tr>
		<td>normals</td>
		<td>
Normals of the target mesh.
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
Triangles of the target mesh.
</td>
		<td></td>
	</tr>
	<tr>
		<td>theCloserTheStiffer</td>
		<td>
Modify stiffness according to distance
</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showArrowSize</td>
		<td>
size of the axis.
</td>
		<td>0.01</td>
	</tr>
	<tr>
		<td>drawMode</td>
		<td>
The way springs will be drawn:
- 0: Line
- 1:Cylinder
- 2: Arrow.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawColorMap</td>
		<td>
Hue mapping of distances to closest point
</td>
		<td>0</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|mechanicalStates|List of mechanical states to which this component is associated|
|mstate|MechanicalState used by this component|



