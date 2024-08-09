<!-- generate_doc -->
# OmniDriverEmu

Solver to test compliance computation for new articulated system objects


__Target__: SensableEmulation

__namespace__: sofa::component::controller

__parents__:

- Controller

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
		<td>handleEventTriggersUpdate</td>
		<td>
Event handling frequency controls the controller update frequency
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>forceScale</td>
		<td>
Default scaling factor applied to the force feedback
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>scale</td>
		<td>
Default scale applied to the Phantom Coordinates. 
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>positionBase</td>
		<td>
Position of the interface base in the scene world coordinates
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>orientationBase</td>
		<td>
Orientation of the interface base in the scene world coordinates
		</td>
		<td>0 0 0 1</td>
	</tr>
	<tr>
		<td>positionTool</td>
		<td>
Position of the tool in the omni end effector frame
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>orientationTool</td>
		<td>
Orientation of the tool in the omni end effector frame
		</td>
		<td>0 0 0 1</td>
	</tr>
	<tr>
		<td>permanent</td>
		<td>
Apply the force feedback permanently
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>omniVisu</td>
		<td>
Visualize the position of the interface in the virtual scene
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>simuFreq</td>
		<td>
frequency of the "simulated Omni"
		</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>simulateTranslation</td>
		<td>
do very naive "translation simulation" of omni, with constant orientation <0 0 0 1>
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>trajPoints</td>
		<td>
Trajectory positions
		</td>
		<td></td>
	</tr>
	<tr>
		<td>trajTiming</td>
		<td>
Trajectory timing
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

