<!-- generate_doc -->
# DataVariationLimiter

This component interpolates between two consecutive inputs when a jump is detected.


Templates:

- Vec1d
- Vec1i
- Vec2d
- Vec2i
- Vec3d
- Vec3i

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
		<td>input</td>
		<td>
 
		</td>
		<td></td>
	</tr>
	<tr>
		<td>output</td>
		<td>
 
		</td>
		<td></td>
	</tr>
	<tr>
		<td>size</td>
		<td>
Input size.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>maxJump</td>
		<td>
Maximal jump allowed. Default 10% is equivalent to jump = 0.1.
		</td>
		<td>0.1</td>
	</tr>
	<tr>
		<td>nbStep</td>
		<td>
Number of interpolation steps. Default is 50.
		</td>
		<td>50</td>
	</tr>
	<tr>
		<td>initOutput</td>
		<td>
If true, will initialize the output with the input.
		</td>
		<td>1</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|

