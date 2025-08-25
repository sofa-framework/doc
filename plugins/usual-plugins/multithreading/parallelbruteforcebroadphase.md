# ParallelBruteForceBroadPhase

This component is a parallel implementation of [BruteForceBroadPhase](../../../../components/collision/detection/algorithm/bruteforcebroadphase/) using a global thread pool.
It means the result of a simulation with [BruteForceBroadPhase](../../../../components/collision/detection/algorithm/bruteforcebroadphase/) or with ParallelBruteForceBroadPhase is expected to be equal.
ParallelBruteForceBroadPhase is the most efficient compared to [BruteForceBroadPhase](../../../../components/collision/detection/algorithm/bruteforcebroadphase/) when there is a lot of objects in the scene.
<!-- automatically generated doc START -->
<!-- generate_doc -->

Parallel version of the collision detection using extensive pair-wise tests performed concurrently.


__Target__: MultiThreading

__namespace__: multithreading::component::collision::detection::algorithm

__parents__:

- BruteForceBroadPhase

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
		<td>box</td>
		<td>
if not empty, objects that do not intersect this bounding-box will be ignored
		</td>
		<td></td>
	</tr>
	<tr>
		<td>nbThreads</td>
		<td>
If not yet initialized, the main task scheduler is initialized with this number of threads. 0 corresponds to the number of available cores on the CPU. -n (minus) corresponds to the number of available cores on the CPU minus the provided number.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>taskSchedulerType</td>
		<td>
Type of task scheduler to use.
		</td>
		<td>_default</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|


<!-- automatically generated doc END -->
