<!-- generate_doc -->
# BottleField

A bottle implicit field.


__Target__: SofaImplicitField

__namespace__: sofa::component::geometry::_BottleField_

__parents__:

- ScalarField

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
		<td>epsilon</td>
		<td>
Tolerance when evaluating the gradient and/or the hessian of the implicit surface numerically
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>inside</td>
		<td>
If true the field is oriented inside (resp. outside) the bottle-shaped object. (default = false)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
Radius of Sphere emitting the field. (default = 1)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>center</td>
		<td>
Position of the Sphere Surface. (default=0 0 0)
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>shift</td>
		<td>
How much the top ellipsoid is shifted from the bottom sphere. (default=1)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>ellipsoidRadius</td>
		<td>
Radius of the ellipsoid whose intersection with the sphere is taken off
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>excentricity</td>
		<td>
excentricity of ellipsoid
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

