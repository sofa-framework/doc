# HyperReducedTetrahedronFEMForceField

Tetrahedral finite elements


__Templates__:

- `#!c++ Vec3d`

__Target__: `ModelOrderReduction`

__namespace__: `#!c++ sofa::component::forcefield`

__parents__: 

- `#!c++ TetrahedronFEMForceField`
- `#!c++ HyperReducedHelper`

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
		<td>initialPoints</td>
		<td>
Initial Position
</td>
		<td></td>
	</tr>
	<tr>
		<td>method</td>
		<td>
"small", "large" (by QR), "polar" or "svd" displacements
</td>
		<td>large</td>
	</tr>
	<tr>
		<td>poissonRatio</td>
		<td>
FEM Poisson Ratio in Hooke's law [0,0.5[
</td>
		<td>0.45</td>
	</tr>
	<tr>
		<td>youngModulus</td>
		<td>
FEM Young's Modulus in Hooke's law
</td>
		<td></td>
	</tr>
	<tr>
		<td>localStiffnessFactor</td>
		<td>
Allow specification of different stiffness per element. If there are N element and M values are specified, the youngModulus factor for element i would be localStiffnessFactor[i*M/N]
</td>
		<td></td>
	</tr>
	<tr>
		<td>updateStiffnessMatrix</td>
		<td>

</td>
		<td>0</td>
	</tr>
	<tr>
		<td>computeGlobalMatrix</td>
		<td>

</td>
		<td>0</td>
	</tr>
	<tr>
		<td>plasticMaxThreshold</td>
		<td>
Plastic Max Threshold (2-norm of the strain)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>plasticYieldThreshold</td>
		<td>
Plastic Yield Threshold (2-norm of the strain)
</td>
		<td>0.0001</td>
	</tr>
	<tr>
		<td>plasticCreep</td>
		<td>
Plastic Creep Factor * dt [0,1]. Warning this factor depends on dt.
</td>
		<td>0.9</td>
	</tr>
	<tr>
		<td>gatherPt</td>
		<td>
number of dof accumulated per threads during the gather operation (Only use in GPU version)
</td>
		<td></td>
	</tr>
	<tr>
		<td>gatherBsize</td>
		<td>
number of dof accumulated per threads during the gather operation (Only use in GPU version)
</td>
		<td></td>
	</tr>
	<tr>
		<td>computeVonMisesStress</td>
		<td>
compute and display von Mises stress: 0: no computations, 1: using corotational strain, 2: using full Green strain. Set listening=1
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>vonMisesPerElement</td>
		<td>
von Mises Stress per element
</td>
		<td></td>
	</tr>
	<tr>
		<td>vonMisesPerNode</td>
		<td>
von Mises Stress per node
</td>
		<td></td>
	</tr>
	<tr>
		<td>vonMisesStressColors</td>
		<td>
Vector of colors describing the VonMises stress
</td>
		<td></td>
	</tr>
	<tr>
		<td>updateStiffness</td>
		<td>
udpate structures (precomputed in init) using stiffness parameters in each iteration (set listening=1)
</td>
		<td>0</td>
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
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawHeterogeneousTetra</td>
		<td>
Draw Heterogeneous Tetra in different color
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showStressColorMap</td>
		<td>
Color map used to show stress values
</td>
		<td>Blue to Red</td>
	</tr>
	<tr>
		<td>showStressAlpha</td>
		<td>
Alpha for vonMises visualisation
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>showVonMisesStressPerNode</td>
		<td>
draw points showing vonMises stress interpolated in nodes
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showVonMisesStressPerNodeColorMap</td>
		<td>
draw elements showing vonMises stress interpolated in nodes
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showVonMisesStressPerElement</td>
		<td>
draw triangles showing vonMises stress interpolated in elements
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showElementGapScale</td>
		<td>
draw gap between elements (when showWireFrame is disabled) [0,1]: 0: no gap, 1: no element
</td>
		<td>0.333</td>
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
|topology|link to the tetrahedron topology container|



