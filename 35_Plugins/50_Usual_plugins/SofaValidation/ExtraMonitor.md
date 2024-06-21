# ExtraMonitor

Monitoring of particles
Supports GPU-side computation using CUDA


__Templates__:

- `#!c++ Rigid3d`
- `#!c++ Vec3d`
- `#!c++ Vec6d`

__Target__: `SofaValidation`

__namespace__: `#!c++ sofa::component::misc`

__parents__: 

- `#!c++ Monitor`

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
		<td>indices</td>
		<td>
MechanicalObject points indices to monitor
</td>
		<td></td>
	</tr>
	<tr>
		<td>ExportPositions</td>
		<td>
export Monitored positions as gnuplot file
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>ExportVelocities</td>
		<td>
export Monitored velocities as gnuplot file
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>ExportForces</td>
		<td>
export Monitored forces as gnuplot file
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>PositionsColor</td>
		<td>
define the color of positions
</td>
		<td></td>
	</tr>
	<tr>
		<td>VelocitiesColor</td>
		<td>
define the color of velocities
</td>
		<td></td>
	</tr>
	<tr>
		<td>ForcesColor</td>
		<td>
define the color of forces
</td>
		<td></td>
	</tr>
	<tr>
		<td>TrajectoriesPrecision</td>
		<td>
set the dt between to save of positions
</td>
		<td>0.1</td>
	</tr>
	<tr>
		<td>TrajectoriesColor</td>
		<td>
define the color of the trajectories
</td>
		<td></td>
	</tr>
	<tr>
		<td>sizeFactor</td>
		<td>
factor to multiply to arrows
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>fileName</td>
		<td>
name of the plot files to be generated
</td>
		<td></td>
	</tr>
	<tr>
		<td>ExportWcin</td>
		<td>
export Wcin of the monitored dofs as gnuplot file
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>ExportWext</td>
		<td>
export Wext of the monitored dofs as gnuplot file
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>resultantF</td>
		<td>
export force resultant of the monitored dofs as gnuplot file instead of all dofs
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>minCoord</td>
		<td>
export minimum displacement on the given coordinate as gnuplot file instead of positions of all dofs
</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>maxCoord</td>
		<td>
export minimum displacement on the given coordinate as gnuplot file instead of positions of all dofs
</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>dispCoord</td>
		<td>
export displacement on the given coordinate as gnuplot file
</td>
		<td>-1</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showPositions</td>
		<td>
see the Monitored positions
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showVelocities</td>
		<td>
see the Monitored velocities
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showForces</td>
		<td>
see the Monitored forces
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showMinThreshold</td>
		<td>
under this value, vectors are not represented
</td>
		<td>0.01</td>
	</tr>
	<tr>
		<td>showTrajectories</td>
		<td>
print the trajectory of Monitored particles
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



