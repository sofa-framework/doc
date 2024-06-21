# SPHFluidForceField

Smooth Particle Hydrodynamics
Supports GPU-side computations using CUDA


__Templates__:

- `#!c++ Vec3d`

__Target__: `SofaSphFluid`

__namespace__: `#!c++ sofa::component::forcefield`

__parents__: 

- `#!c++ ForceField`

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
		<td>radius</td>
		<td>
Radius of a Particle
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mass</td>
		<td>
Mass of a Particle
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>pressure</td>
		<td>
Pressure
</td>
		<td>100</td>
	</tr>
	<tr>
		<td>density</td>
		<td>
Density
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>viscosity</td>
		<td>
Viscosity
</td>
		<td>0.001</td>
	</tr>
	<tr>
		<td>surfaceTension</td>
		<td>
Surface Tension
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>kernelType</td>
		<td>
0 = default kernels, 1 = cubic spline
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>pressureType</td>
		<td>
0 = none, 1 = default pressure
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>viscosityType</td>
		<td>
0 = none, 1 = default d_viscosity using kernel Laplacian, 2 = artificial d_viscosity
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>surfaceTensionType</td>
		<td>
0 = none, 1 = default surface tension using kernel Laplacian, 2 = cohesion forces surface tension from Becker et al. 2007
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>debugGrid</td>
		<td>
If true will store additionnal information on the grid to check neighbors and draw them
</td>
		<td>0</td>
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



