# DistanceGridForceField

Force applied by a distancegrid toward the exterior, the interior, or the surface


__Templates__:

- `#!c++ Vec3d`

__Target__: `SofaDistanceGrid`

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
		<td>isCompliance</td>
		<td>
Consider the component as a compliance, else as a stiffness
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
		<td>filename</td>
		<td>
load distance grid from specified file
</td>
		<td></td>
	</tr>
	<tr>
		<td>scale</td>
		<td>
scaling factor for input file
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>box</td>
		<td>
Field bounding box defined by xmin,ymin,zmin, xmax,ymax,zmax
</td>
		<td></td>
	</tr>
	<tr>
		<td>nx</td>
		<td>
number of values on X axis
</td>
		<td>64</td>
	</tr>
	<tr>
		<td>ny</td>
		<td>
number of values on Y axis
</td>
		<td>64</td>
	</tr>
	<tr>
		<td>nz</td>
		<td>
number of values on Z axis
</td>
		<td>64</td>
	</tr>
	<tr>
		<td>stiffnessIn</td>
		<td>
force stiffness when inside of the object
</td>
		<td>500</td>
	</tr>
	<tr>
		<td>stiffnessOut</td>
		<td>
force stiffness when outside of the object
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>damping</td>
		<td>
force damping coefficient
</td>
		<td>0.01</td>
	</tr>
	<tr>
		<td>maxdist</td>
		<td>
max distance of the surface after which no more force is applied
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>minArea</td>
		<td>
minimal area for each triangle, as seen from the direction of the local surface (i.e. a flipped triangle will have a negative area)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>stiffnessArea</td>
		<td>
force stiffness if a triangle have an area less than minArea
</td>
		<td>100</td>
	</tr>
	<tr>
		<td>minVolume</td>
		<td>
minimal volume for each tetrahedron (a flipped triangle will have a negative volume)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>stiffnessVolume</td>
		<td>
force stiffness if a tetrahedron have an volume less than minVolume
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>color</td>
		<td>
display color.(default=[0.0,0.5,0.2,1.0])
</td>
		<td>0 0.5 0.2 1</td>
	</tr>
	<tr>
		<td>localRange</td>
		<td>
optional range of local DOF indices. Any computation involving only indices outside of this range are discarded (useful for parallelization using mesh partitionning)
</td>
		<td>-1 -1</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>draw</td>
		<td>
enable/disable drawing of distancegrid
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawPoints</td>
		<td>
enable/disable drawing of distancegrid
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawSize</td>
		<td>
display size if draw is enabled
</td>
		<td>10</td>
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



