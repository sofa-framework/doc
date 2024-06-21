# NonUniformHexahedralFEMForceFieldAndMass

Non uniform Hexahedral finite elements


__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.Component.SolidMechanics.FEM.NonUniform`

__namespace__: `#!c++ sofa::component::solidmechanics::fem::nonuniform`

__parents__: 

- `#!c++ HexahedralFEMForceFieldAndMass`

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
		<td>isCompliance</td>
		<td>
Consider the component as a compliance, else as a stiffness
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping - stiffness matrix coefficient
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>separateGravity</td>
		<td>
add separately gravity to velocity computation
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>rayleighMass</td>
		<td>
Rayleigh damping - mass matrix coefficient
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>method</td>
		<td>
"large" or "polar" displacements
</td>
		<td>large</td>
	</tr>
	<tr>
		<td>poissonRatio</td>
		<td>

</td>
		<td>0.45</td>
	</tr>
	<tr>
		<td>youngModulus</td>
		<td>

</td>
		<td>5000</td>
	</tr>
	<tr>
		<td>hexahedronInfo</td>
		<td>
Internal hexahedron data
</td>
		<td></td>
	</tr>
	<tr>
		<td>density</td>
		<td>
density == volumetric mass in english (kg.m-3)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>lumpedMass</td>
		<td>
Does it use lumped masses?
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>massMatrices</td>
		<td>
Mass matrices per element (M_i)
</td>
		<td></td>
	</tr>
	<tr>
		<td>totalMass</td>
		<td>
Total mass per element
</td>
		<td></td>
	</tr>
	<tr>
		<td>particleMasses</td>
		<td>
Mass per particle
</td>
		<td></td>
	</tr>
	<tr>
		<td>lumpedMasses</td>
		<td>
Lumped masses
</td>
		<td></td>
	</tr>
	<tr>
		<td>recursive</td>
		<td>
Use recursive matrix computation
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>useMBK</td>
		<td>
compute MBK and use it in addMBKdx, instead of using addDForce and addMDx.
</td>
		<td>1</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|mechanicalStates|List of mechanical states to which this component is associated|
|mstate|MechanicalState used by this component|



