<!-- generate_doc -->
# OgdenMaterial

Ogden material


Templates:

- Vec1d
- Vec2d
- Vec3d

__Target__: 

__namespace__: sofa::component::solidmechanics::fem::hyperelastic

__parents__:

- PK2HyperelasticMaterial

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
		<td>mu</td>
		<td>
Material constant relevant to the shear modulus
		</td>
		<td>100</td>
	</tr>
	<tr>
		<td>alpha</td>
		<td>
Material constant exponent related to strain-stiffening
		</td>
		<td>1.5</td>
	</tr>
	<tr>
		<td>kappa</td>
		<td>
Material constant related to the bulk modulus
		</td>
		<td>1000</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseComponent|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseComponent|

