<!-- generate_doc -->
# HyperReducedTriangleFEMForceField

Triangular finite elements


## Vec3d

Templates:

- Vec3d

__Target__: ModelOrderReduction

__namespace__: sofa::component::solidmechanics::fem::elastic

__parents__:

- TriangleFEMForceField
- HyperReducedHelper

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
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping - stiffness matrix coefficient
		</td>
		<td>0</td>
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
		<td>5000</td>
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
large: large displacements, small: small displacements
		</td>
		<td>large</td>
	</tr>
	<tr>
		<td>thickness</td>
		<td>
Thickness of the elements
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>planeStrain</td>
		<td>
Plane strain or plane stress assumption
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

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|
|topology|link to the topology container|BaseMeshTopology|

