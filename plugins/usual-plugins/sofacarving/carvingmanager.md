# CarvingManager

Manager handling carving operations between a tool and an object.


__Target__: `SofaCarving`

__namespace__: `#!c++ sofa::component::collision`

__parents__: 

- `#!c++ BaseController`

__categories__: 

- Controller

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
		<td>surfaceModelPath</td>
		<td>
TriangleSetModel or SphereCollisionModel&lt;sofa::defaulttype::Vec3Types&gt; path
</td>
		<td></td>
	</tr>
	<tr>
		<td>carvingDistance</td>
		<td>
Collision distance at which cavring will start. Equal to contactDistance by default.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>active</td>
		<td>
Activate this object.
Note that this can be dynamically controlled by using a key
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>key</td>
		<td>
key to press to activate this object until the key is released
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>keySwitch</td>
		<td>
key to activate this object until the key is pressed again
</td>
		<td>4</td>
	</tr>
	<tr>
		<td>mouseEvent</td>
		<td>
Activate carving with middle mouse button
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>omniEvent</td>
		<td>
Activate carving with omni button
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>button1</td>
		<td>
activatorName
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
|toolModel|link to the carving collision model, if not set, manager will search for a collision model with tag: CarvingTool.|
|narrowPhaseDetection|link to the narrow Phase Detection component, if not set, manager will search for it in root Node.|



