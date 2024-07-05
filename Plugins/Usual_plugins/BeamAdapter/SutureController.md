# SutureController

Provides a Mouse & Keyboard user control on an EdgeSet Topology.


__Templates__:

- `#!c++ Rigid3d`

__Target__: `BeamAdapter`

__namespace__: `#!c++ sofa::component::controller::_suturecontroller_`

__parents__: 

- `#!c++ MechanicalStateController`

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
		<td>handleEventTriggersUpdate</td>
		<td>
Event handling frequency controls the controller update frequency
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>index</td>
		<td>
Index of the controlled DOF
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>onlyTranslation</td>
		<td>
Controlling the DOF only in translation
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>buttonDeviceState</td>
		<td>
state of ths device button
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>mainDirection</td>
		<td>
Main direction and orientation of the controlled DOF
</td>
		<td>0 0 -1</td>
	</tr>
	<tr>
		<td>startingPos</td>
		<td>
starting pos for inserting the instrument
</td>
		<td>0 0 0 0 0 0 1</td>
	</tr>
	<tr>
		<td>threshold</td>
		<td>
threshold for controller precision which is homogeneous to the unit of length
</td>
		<td>1e-06</td>
	</tr>
	<tr>
		<td>maxBendingAngle</td>
		<td>
max bending criterion (in rad) for one beam
</td>
		<td>0.1</td>
	</tr>
	<tr>
		<td>useDummyController</td>
		<td>
 use a very simple controller of adaptativity (use for debug)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>fixRigidTransforms</td>
		<td>
fix the sampling and transformations of rigid segments
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>rigidCurvAbs</td>
		<td>
pairs of curv abs for beams we want to rigidify
</td>
		<td></td>
	</tr>
	<tr>
		<td>nodeCurvAbs</td>
		<td>

</td>
		<td></td>
	</tr>
	<tr>
		<td>curvatureList</td>
		<td>
List of the beams curvature (abscissa - curvature)
</td>
		<td></td>
	</tr>
	<tr>
		<td>controlPoints</td>
		<td>
List of the spline control points positions
</td>
		<td></td>
	</tr>
	<tr>
		<td>updateOnBeginAnimationStep</td>
		<td>
If true update interpolation and subgraph on beginAnimationStep
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>applyOrientationFirstInCreateNeedle</td>
		<td>
if true, it sets first the orientation, then the rotation for a init node of the needle
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>reinitilizeWireOnInit</td>
		<td>
 reinitialize the wire everytime init() is called (for planning purposes)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>m_actualStepNoticeablePoints</td>
		<td>
points (as curv. absc.) that are to be considered when computing a new sampling in the actual time step
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
|interpolation|Path to the Interpolation component on scene|



