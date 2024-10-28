<!-- generate_doc -->
# AnimationEditor

Build an animation from key points motion: 
ctrl+a: add keyframe 
ctrl+d: delete keyframe 
ctrl+c: copy keyframe 
ctrl+v: paste keyframe 
ctrl+x: cut keyframe 
ctrl+w: write animation 
ctrl+m: play/pause animation 
ctrl+(left/right)arrow: move the cursor along the timeline 
ctrl+(pgDn/pgUp): move the cursor to the next/previous keyframe


Templates:

- Rigid3d
- Vec3d

__Target__: SoftRobots

__namespace__: softrobots::controller

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
		<td>maxKeyFrame</td>
		<td>
Max >= 1, default 150
		</td>
		<td>150</td>
	</tr>
	<tr>
		<td>filename</td>
		<td>
If no filename given, set default to animation.txt
		</td>
		<td>animation.txt</td>
	</tr>
	<tr>
		<td>loop</td>
		<td>
If true, will loop on the animation (only in play mode).
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>load</td>
		<td>
If true, will load the animation at init.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>dx</td>
		<td>
Variation of displacement. You can control the animation on displacement instead of time.
If dx is set, at each time step, the animation will progress in term of displacement/distance.
A positive dx means move forward and a negative dx means backward (on the timeline).
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>frameTime</td>
		<td>
Frame time.
		</td>
		<td>0.01</td>
	</tr>
	<tr>
		<td>cursor</td>
		<td>
Current frame of the cursor along the timeline
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawTimeline</td>
		<td>

		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>drawSize</td>
		<td>

		</td>
		<td>0.1</td>
	</tr>
	<tr>
		<td>drawTrajectory</td>
		<td>

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

