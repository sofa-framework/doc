<!-- generate_doc -->
# RecordedCamera

A camera that is moving along a predetermined path.


__Target__: Sofa.Component.Visual

__namespace__: sofa::component::visual

__parents__:

- BaseCamera

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
		<td>position</td>
		<td>
Camera's position
		</td>
		<td></td>
	</tr>
	<tr>
		<td>orientation</td>
		<td>
Camera's orientation
		</td>
		<td></td>
	</tr>
	<tr>
		<td>lookAt</td>
		<td>
Camera's look at
		</td>
		<td></td>
	</tr>
	<tr>
		<td>distance</td>
		<td>
Distance between camera and look at
		</td>
		<td></td>
	</tr>
	<tr>
		<td>fieldOfView</td>
		<td>
Camera's FOV
		</td>
		<td>45</td>
	</tr>
	<tr>
		<td>zNear</td>
		<td>
Camera's zNear
		</td>
		<td>0.01</td>
	</tr>
	<tr>
		<td>zFar</td>
		<td>
Camera's zFar
		</td>
		<td>100</td>
	</tr>
	<tr>
		<td>computeZClip</td>
		<td>
Compute Z clip planes (Near and Far) according to the bounding box
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>minBBox</td>
		<td>
minBBox
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>maxBBox</td>
		<td>
maxBBox
		</td>
		<td>1 1 1</td>
	</tr>
	<tr>
		<td>widthViewport</td>
		<td>
widthViewport
		</td>
		<td>800</td>
	</tr>
	<tr>
		<td>heightViewport</td>
		<td>
heightViewport
		</td>
		<td>600</td>
	</tr>
	<tr>
		<td>projectionType</td>
		<td>
Camera Type (0 = Perspective, 1 = Orthographic)
		</td>
		<td></td>
	</tr>
	<tr>
		<td>activated</td>
		<td>
Camera activated ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>fixedLookAt</td>
		<td>
keep the lookAt point always fixed
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>modelViewMatrix</td>
		<td>
ModelView Matrix
		</td>
		<td></td>
	</tr>
	<tr>
		<td>projectionMatrix</td>
		<td>
Projection Matrix
		</td>
		<td></td>
	</tr>
	<tr>
		<td>zoomSpeed</td>
		<td>
Zoom Speed
		</td>
		<td>250</td>
	</tr>
	<tr>
		<td>panSpeed</td>
		<td>
Pan Speed
		</td>
		<td>0.1</td>
	</tr>
	<tr>
		<td>pivot</td>
		<td>
Pivot (0 => Scene center, 1 => World Center
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>startTime</td>
		<td>
Time when the camera moves will start
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>endTime</td>
		<td>
Time when the camera moves will end (or loop)
		</td>
		<td>200</td>
	</tr>
	<tr>
		<td>rotationMode</td>
		<td>
If true, rotation will be performed
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>translationMode</td>
		<td>
If true, translation will be performed
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>navigationMode</td>
		<td>
If true, navigation will be performed
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>rotationSpeed</td>
		<td>
rotation Speed
		</td>
		<td>0.1</td>
	</tr>
	<tr>
		<td>rotationCenter</td>
		<td>
Rotation center coordinates
		</td>
		<td></td>
	</tr>
	<tr>
		<td>rotationStartPoint</td>
		<td>
Rotation start position coordinates
		</td>
		<td></td>
	</tr>
	<tr>
		<td>rotationLookAt</td>
		<td>
Position to be focused during rotation
		</td>
		<td></td>
	</tr>
	<tr>
		<td>rotationAxis</td>
		<td>
Rotation axis
		</td>
		<td>0 1 0</td>
	</tr>
	<tr>
		<td>cameraUp</td>
		<td>
Camera Up axis
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>cameraPositions</td>
		<td>
Intermediate camera's positions
		</td>
		<td></td>
	</tr>
	<tr>
		<td>cameraOrientations</td>
		<td>
Intermediate camera's orientations
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawRotation</td>
		<td>
If true, will draw the rotation path
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawTranslation</td>
		<td>
If true, will draw the translation path
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

