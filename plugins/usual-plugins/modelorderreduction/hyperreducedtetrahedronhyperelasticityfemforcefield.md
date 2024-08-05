# HyperReducedTetrahedronHyperelasticityFEMForceField

Generic Tetrahedral finite elements


__Templates__:

- `#!c++ Vec3d`

__Target__: `ModelOrderReduction`

__namespace__: `#!c++ sofa::component::forcefield`

__parents__: 

- `#!c++ TetrahedronHyperelasticityFEMForceField`
- `#!c++ HyperReducedHelper`

__categories__: 

- ForceField

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
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping - stiffness matrix coefficient
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>matrixRegularization</td>
		<td>
Regularization of the Stiffness Matrix (between true or false)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>materialName</td>
		<td>
the name of the material to be used. Possible options are: 'ArrudaBoyce', 'Costa', 'MooneyRivlin', 'NeoHookean', 'Ogden', 'StVenantKirchhoff', 'VerondaWestman', 'StableNeoHookean'
</td>
		<td>ArrudaBoyce</td>
	</tr>
	<tr>
		<td>ParameterSet</td>
		<td>
The global parameters specifying the material
</td>
		<td></td>
	</tr>
	<tr>
		<td>AnisotropyDirections</td>
		<td>
The global directions of anisotropy of the material: vector containing anisotropic directions. The vector size is 0 if the material is isotropic, 1 if it is transversely isotropic and 2 for orthotropic materials
</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedronInfo</td>
		<td>
Internal tetrahedron data
</td>
		<td></td>
	</tr>
	<tr>
		<td>edgeInfo</td>
		<td>
Internal edge data
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">HyperReduction</td>
	</tr>
	<tr>
		<td>prepareECSW</td>
		<td>
Save data necessary for the construction of the reduced model
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>nbModes</td>
		<td>
Number of modes when preparing the ECSW method only
</td>
		<td>3</td>
	</tr>
	<tr>
		<td>modesPath</td>
		<td>
Path to the file containing the modes (useful only for preparing ECSW)
</td>
		<td>modes.txt</td>
	</tr>
	<tr>
		<td>nbTrainingSet</td>
		<td>
When preparing the ECSW, size of the training set
</td>
		<td>40</td>
	</tr>
	<tr>
		<td>periodSaveGIE</td>
		<td>
When prepareECSW is true, the values of Gie are taken every periodSaveGIE timesteps.
</td>
		<td>5</td>
	</tr>
	<tr>
		<td>performECSW</td>
		<td>
Use the reduced model with the ECSW method
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>RIDPath</td>
		<td>
Path to the Reduced Integration domain when performing the ECSW method
</td>
		<td>reducedIntegrationDomain.txt</td>
	</tr>
	<tr>
		<td>weightsPath</td>
		<td>
Path to the weights when performing the ECSW method
</td>
		<td>weights.txt</td>
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
|topology|link to the topology container|


