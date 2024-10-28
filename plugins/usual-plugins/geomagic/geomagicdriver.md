<!-- generate_doc -->
# GeomagicDriver

Driver allowing interfacing with Geomagic haptic devices.


__Target__: Geomagic

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
list of the subsets the object belongs to
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
		<td>deviceName</td>
		<td>
Name of device Configuration
		</td>
		<td>Default Device</td>
	</tr>
	<tr>
		<td>positionBase</td>
		<td>
Position of the device base in the SOFA scene world coordinates
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>orientationBase</td>
		<td>
Orientation of the device base in the SOFA scene world coordinates
		</td>
		<td>0 0 0 1</td>
	</tr>
	<tr>
		<td>orientationTool</td>
		<td>
Orientation of the tool in the SOFA scene world coordinates
		</td>
		<td>0 0 0 1</td>
	</tr>
	<tr>
		<td>scale</td>
		<td>
Default scale applied to the Device coordinates
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>forceScale</td>
		<td>
Default scaling factor applied to the force feedback
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>maxInputForceFeedback</td>
		<td>
Maximum value of the normed input force feedback for device security
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>inputForceFeedback</td>
		<td>
Input force feedback in case of no LCPForceFeedback is found (manual setting)
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>manualStart</td>
		<td>
If true, will not automatically initDevice at component init phase.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>emitButtonEvent</td>
		<td>
If true, will send event through the graph when button are pushed/released
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>positionDevice</td>
		<td>
position of the base of the part of the device
		</td>
		<td></td>
	</tr>
	<tr>
		<td>angle</td>
		<td>
Angular values of joint (rad)
		</td>
		<td></td>
	</tr>
	<tr>
		<td>button1</td>
		<td>
Button state 1
		</td>
		<td></td>
	</tr>
	<tr>
		<td>button2</td>
		<td>
Button state 2
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawDeviceFrame</td>
		<td>
Visualize the frame corresponding to the device tooltip
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawDevice</td>
		<td>
Visualize the Geomagic device in the virtual scene
		</td>
		<td>0</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|forceFeedBack|link to the forceFeedBack component, if not set will search through graph and take first one encountered.|ForceFeedback|

