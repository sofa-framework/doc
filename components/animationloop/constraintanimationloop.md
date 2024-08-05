# ConstraintAnimationLoop

Constraint animation loop manager


__Target__: `Sofa.Component.AnimationLoop`

__namespace__: `#!c++ sofa::component::animationloop`

__parents__: 

- `#!c++ BaseAnimationLoop`

__categories__: 

- AnimationLoop

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
		<td>computeBoundingBox</td>
		<td>
If true, compute the global bounding box of the scene at each time step. Used mostly for rendering.
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>displayTime</td>
		<td>
Display time for each important step of ConstraintAnimationLoop.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>tolerance</td>
		<td>
Tolerance of the Gauss-Seidel
</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>maxIterations</td>
		<td>
Maximum number of iterations of the Gauss-Seidel
</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>doCollisionsFirst</td>
		<td>
Compute the collisions first (to support penality-based contacts)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>doubleBuffer</td>
		<td>
Double the buffer dedicated to the constraint problem to make it accessible to another thread
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>scaleTolerance</td>
		<td>
Scale the error tolerance with the number of constraints
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>allVerified</td>
		<td>
All contraints must be verified (each constraint's error &lt; tolerance)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>sor</td>
		<td>
Successive Over Relaxation parameter (0-2)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>schemeCorrection</td>
		<td>
Apply new scheme where compliance is progressively corrected
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>realTimeCompensation</td>
		<td>
If the total computational time T &lt; dt, sleep(dt-T)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Graph</td>
	</tr>
	<tr>
		<td>graphErrors</td>
		<td>
Sum of the constraints' errors at each iteration
</td>
		<td></td>
	</tr>
	<tr>
		<td>graphConstraints</td>
		<td>
Graph of each constraint's error at the end of the resolution
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Graph2</td>
	</tr>
	<tr>
		<td>graphForces</td>
		<td>
Graph of each constraint's force at each step of the resolution
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
|targetNode|Link to the scene's node that will be processed by the loop|



