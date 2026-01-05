<!-- generate_doc -->
# CCDTightInclusionIntersection

A set of methods to compute (for constraint methods) if two primitives are close enough to consider they collide


__Target__: Sofa.Component.Collision.Detection.Intersection

__namespace__: sofa::component::collision::detection::intersection

__parents__:

- BaseProximityIntersection

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
		<td>alarmDistance</td>
		<td>
Distance above which the intersection computations ignores the proximity pair. This distance can also be used in some broad phase algorithms to reduce the search area
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>contactDistance</td>
		<td>
Distance below which a contact is created
		</td>
		<td>0.5</td>
	</tr>
	<tr>
		<td>continuousCollisionType</td>
		<td>
Data used for continuous collision detection taken into {'None','Inertia','FreeMotion'}. If 'None' then no CCD is used, if 'Inertia' then only inertia will be used to compute the collision detection and if 'FreeMotion' then the free motion will be used. Note that if 'FreeMotion' is selected, you cannot use the option 'parallelCollisionDetectionAndFreeMotion' in the FreeMotionAnimationLoop
		</td>
		<td>None</td>
	</tr>
	<tr>
		<td>tolerance</td>
		<td>
tolerance used by the tight inclusion CCD algorithm
		</td>
		<td>1e-10</td>
	</tr>
	<tr>
		<td>maxIterations</td>
		<td>
maxIterations used by the tight inclusion CCD algorithm
		</td>
		<td>1000</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|

