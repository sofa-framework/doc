<!-- generate_doc -->
# TriangularAnisotropicFEMForceField

Triangular finite element model using anisotropic material.


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.SolidMechanics.FEM.Elastic

__namespace__: sofa::component::solidmechanics::fem::elastic

__parents__:

- TriangularFEMForceField

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
		<td>triangleInfo</td>
		<td>
Internal triangle data
		</td>
		<td></td>
	</tr>
	<tr>
		<td>vertexInfo</td>
		<td>
Internal point data
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
		<td>rotatedInitialElements</td>
		<td>
Flag activating rendering of stress directions within each triangle
		</td>
		<td></td>
	</tr>
	<tr>
		<td>initialTransformation</td>
		<td>
Flag activating rendering of stress directions within each triangle
		</td>
		<td></td>
	</tr>
	<tr>
		<td>hosfordExponant</td>
		<td>
Exponent in the Hosford yield criteria
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>criteriaValue</td>
		<td>
Fracturable threshold used to draw fracturable triangles
		</td>
		<td>1e+15</td>
	</tr>
	<tr>
		<td>computePrincipalStress</td>
		<td>
Compute principal stress for each triangle
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>transverseYoungModulus</td>
		<td>
transverseYoungModulus
		</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>fiberAngle</td>
		<td>
Fiber angle in global reference frame (in degrees)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>fiberCenter</td>
		<td>
Concentric fiber center in global reference frame
		</td>
		<td></td>
	</tr>
	<tr>
		<td>localFiberDirection</td>
		<td>
Computed fibers direction within each triangle
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showStressValue</td>
		<td>
Flag activating rendering of stress values as a color in each triangle
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>showStressVector</td>
		<td>
Flag activating rendering of stress directions within each triangle
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showFracturableTriangles</td>
		<td>
Flag activating rendering of triangles to fracture
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showFiber</td>
		<td>
Flag activating rendering of fiber directions within each triangle
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
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|
|topology|link to the topology container|BaseMeshTopology|

