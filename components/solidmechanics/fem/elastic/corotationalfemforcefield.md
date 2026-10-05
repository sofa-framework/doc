<!-- generate_doc -->
# CorotationalFEMForceField

Hooke's law using the corotational approach


Templates:

- Vec2d,Edge
- Vec2d,Quad
- Vec2d,QuadraticEdge
- Vec2d,QuadraticQuad
- Vec2d,QuadraticTriangle
- Vec2d,Triangle

__Target__: Sofa.Component.SolidMechanics.FEM.Elastic

__namespace__: sofa::component::solidmechanics::fem::elastic

__parents__:

- BaseElementLinearFEMForceField
- FEMForceField

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
		<td>elementStiffness</td>
		<td>
List of stiffness matrices per element
		</td>
		<td></td>
	</tr>
	<tr>
		<td>rotationMethod</td>
		<td>
The method used to compute the element rotations.
- stable_polar: Stable polar decomposition
- polar: Polar decomposition
- identity: Identity rotation. Equivalent to the linear small strain FEM.
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Multithreading</td>
	</tr>
	<tr>
		<td>computeForceStrategy</td>
		<td>
The compute strategy used to compute the forces.
- parallel: The algorithm is executed in parallel
- sequenced: The algorithm is executed sequentially
		</td>
		<td></td>
	</tr>
	<tr>
		<td>computeForceDerivStrategy</td>
		<td>
The compute strategy used to compute the forces derivatives.
- parallel: The algorithm is executed in parallel
- sequenced: The algorithm is executed sequentially
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>elementSpace</td>
		<td>
When rendering, the space between elements
		</td>
		<td>0.125</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseComponent|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseComponent|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec2d&gt;|
|topology|Link to a topology|BaseMeshTopology|

<!-- generate_doc -->
## Vec3d,Edge...

Templates:

- Vec3d,Edge
- Vec3d,Prism
- Vec3d,Pyramid
- Vec3d,Quad
- Vec3d,QuadraticEdge
- Vec3d,QuadraticHexahedron
- Vec3d,QuadraticQuad
- Vec3d,QuadraticTriangle

__Target__: Sofa.Component.SolidMechanics.FEM.Elastic

__namespace__: sofa::component::solidmechanics::fem::elastic

__parents__:

- BaseElementLinearFEMForceField
- FEMForceField

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
		<td>elementStiffness</td>
		<td>
List of stiffness matrices per element
		</td>
		<td></td>
	</tr>
	<tr>
		<td>rotationMethod</td>
		<td>
The method used to compute the element rotations.
- stable_polar: Stable polar decomposition
- polar: Polar decomposition
- identity: Identity rotation. Equivalent to the linear small strain FEM.
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Multithreading</td>
	</tr>
	<tr>
		<td>computeForceStrategy</td>
		<td>
The compute strategy used to compute the forces.
- parallel: The algorithm is executed in parallel
- sequenced: The algorithm is executed sequentially
		</td>
		<td></td>
	</tr>
	<tr>
		<td>computeForceDerivStrategy</td>
		<td>
The compute strategy used to compute the forces derivatives.
- parallel: The algorithm is executed in parallel
- sequenced: The algorithm is executed sequentially
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>elementSpace</td>
		<td>
When rendering, the space between elements
		</td>
		<td>0.125</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseComponent|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseComponent|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|
|topology|Link to a topology|BaseMeshTopology|

<!-- generate_doc -->
## Vec3d,Hexahedron

Templates:

- Vec3d,Hexahedron

__Target__: Sofa.Component.SolidMechanics.FEM.Elastic

__namespace__: sofa::component::solidmechanics::fem::elastic

__parents__:

- BaseElementLinearFEMForceField
- FEMForceField

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
		<td>elementStiffness</td>
		<td>
List of stiffness matrices per element
		</td>
		<td></td>
	</tr>
	<tr>
		<td>rotationMethod</td>
		<td>
The method used to compute the element rotations.
- stable_polar: Stable polar decomposition
- polar: Polar decomposition
- identity: Identity rotation. Equivalent to the linear small strain FEM.
- hexahedron: Compute the rotation based on two average edges in the hexahedron
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Multithreading</td>
	</tr>
	<tr>
		<td>computeForceStrategy</td>
		<td>
The compute strategy used to compute the forces.
- parallel: The algorithm is executed in parallel
- sequenced: The algorithm is executed sequentially
		</td>
		<td></td>
	</tr>
	<tr>
		<td>computeForceDerivStrategy</td>
		<td>
The compute strategy used to compute the forces derivatives.
- parallel: The algorithm is executed in parallel
- sequenced: The algorithm is executed sequentially
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>elementSpace</td>
		<td>
When rendering, the space between elements
		</td>
		<td>0.125</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseComponent|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseComponent|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|
|topology|Link to a topology|BaseMeshTopology|

<!-- generate_doc -->
## Vec3d,QuadraticTetrahedron

Templates:

- Vec3d,QuadraticTetrahedron

__Target__: Sofa.Component.SolidMechanics.FEM.Elastic

__namespace__: sofa::component::solidmechanics::fem::elastic

__parents__:

- BaseElementLinearFEMForceField
- FEMForceField

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
		<td>elementStiffness</td>
		<td>
List of stiffness matrices per element
		</td>
		<td></td>
	</tr>
	<tr>
		<td>rotationMethod</td>
		<td>
The method used to compute the element rotations.
- polar: Polar decomposition
- identity: Identity rotation. Equivalent to the linear small strain FEM.
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Multithreading</td>
	</tr>
	<tr>
		<td>computeForceStrategy</td>
		<td>
The compute strategy used to compute the forces.
- parallel: The algorithm is executed in parallel
- sequenced: The algorithm is executed sequentially
		</td>
		<td></td>
	</tr>
	<tr>
		<td>computeForceDerivStrategy</td>
		<td>
The compute strategy used to compute the forces derivatives.
- parallel: The algorithm is executed in parallel
- sequenced: The algorithm is executed sequentially
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>elementSpace</td>
		<td>
When rendering, the space between elements
		</td>
		<td>0.125</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseComponent|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseComponent|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|
|topology|Link to a topology|BaseMeshTopology|

<!-- generate_doc -->
## Vec3d,Tetrahedron...

Templates:

- Vec3d,Tetrahedron
- Vec3d,Triangle

__Target__: Sofa.Component.SolidMechanics.FEM.Elastic

__namespace__: sofa::component::solidmechanics::fem::elastic

__parents__:

- BaseElementLinearFEMForceField
- FEMForceField

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
		<td>elementStiffness</td>
		<td>
List of stiffness matrices per element
		</td>
		<td></td>
	</tr>
	<tr>
		<td>rotationMethod</td>
		<td>
The method used to compute the element rotations.
- stable_polar: Stable polar decomposition
- polar: Polar decomposition
- identity: Identity rotation. Equivalent to the linear small strain FEM.
- triangle: Compute the rotation based on the Gram-Schmidt frame alignment
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Multithreading</td>
	</tr>
	<tr>
		<td>computeForceStrategy</td>
		<td>
The compute strategy used to compute the forces.
- parallel: The algorithm is executed in parallel
- sequenced: The algorithm is executed sequentially
		</td>
		<td></td>
	</tr>
	<tr>
		<td>computeForceDerivStrategy</td>
		<td>
The compute strategy used to compute the forces derivatives.
- parallel: The algorithm is executed in parallel
- sequenced: The algorithm is executed sequentially
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>elementSpace</td>
		<td>
When rendering, the space between elements
		</td>
		<td>0.125</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseComponent|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseComponent|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|
|topology|Link to a topology|BaseMeshTopology|

## Examples 

CorotationalFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.001" gravity="0 -9.81 0">
    
        <include href="../../../plugins.xml"/>
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
    
        <VisualGrid size="0.1"/>
        <LineAxis size="0.1"/>
    
        <include href="../../../QuadraticTopology.xml"/>
    
        <Node name="simulation">
            <EulerImplicitIntegrationScheme name="backward_Euler" rayleighStiffness="0.1" rayleighMass="0.1" />
    
            <ConstantSparsityPatternSystem template="CompressedRowSparseMatrix" name="A" checkIndices="false"/>
            <SparseLDLSolver name="linear_solver" template="CompressedRowSparseMatrix"/>
    
            <Node name="beam">
                <MeshTopology name="topology"
                              position="@../../preprocessing/tetrahedra/engine.position"
                              quadratic_tetrahedra="@../../preprocessing/tetrahedra/engine.quadratic_tetrahedra"/>
                <MechanicalObject template="Vec3" name="state" position="@../../preprocessing/tetrahedra/engine.position"/>
    
                <VisualPointCloud position="@state.position" drawMode="Sphere" sphereRadius="0.0005" color="orange"/>
                <VisualMesh position="@state.position" topology="@topology"/>
    
                <NodalMassDensity property="1100"/>
                <FEMMass template="Vec3,QuadraticTetrahedron"/>
    
                <BoxROI template="Vec3" name="box_roi" box="-0.011 -0.011 -0.0001   0.011 0.011 0.0001" drawBoxes="1" />
                <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
    
                <CorotationalFEMForceField name="FEM" template="Vec3,QuadraticTetrahedron"
                                           youngModulus="2e6" poissonRatio="0.45" topology="@topology"
                                           computeForceStrategy="parallel" computeForceDerivStrategy="parallel"/>
            </Node>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.001", gravity="0 -9.81 0")

       root.addObject('include', href="../../../plugins.xml")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
       root.addObject('VisualGrid', size="0.1")
       root.addObject('LineAxis', size="0.1")
       root.addObject('include', href="../../../QuadraticTopology.xml")

       simulation = root.addChild('simulation')

       simulation.addObject('EulerImplicitIntegrationScheme', name="backward_Euler", rayleighStiffness="0.1", rayleighMass="0.1")
       simulation.addObject('ConstantSparsityPatternSystem', template="CompressedRowSparseMatrix", name="A", checkIndices="false")
       simulation.addObject('SparseLDLSolver', name="linear_solver", template="CompressedRowSparseMatrix")

       beam = simulation.addChild('beam')

       beam.addObject('MeshTopology', name="topology", position="@../../preprocessing/tetrahedra/engine.position", quadratic_tetrahedra="@../../preprocessing/tetrahedra/engine.quadratic_tetrahedra")
       beam.addObject('MechanicalObject', template="Vec3", name="state", position="@../../preprocessing/tetrahedra/engine.position")
       beam.addObject('VisualPointCloud', position="@state.position", drawMode="Sphere", sphereRadius="0.0005", color="orange")
       beam.addObject('VisualMesh', position="@state.position", topology="@topology")
       beam.addObject('NodalMassDensity', property="1100")
       beam.addObject('FEMMass', template="Vec3,QuadraticTetrahedron")
       beam.addObject('BoxROI', template="Vec3", name="box_roi", box="-0.011 -0.011 -0.0001   0.011 0.011 0.0001", drawBoxes="1")
       beam.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")
       beam.addObject('CorotationalFEMForceField', name="FEM", template="Vec3,QuadraticTetrahedron", youngModulus="2e6", poissonRatio="0.45", topology="@topology", computeForceStrategy="parallel", computeForceDerivStrategy="parallel")
    ```

CorotationalFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.001" gravity="0 -9.81 0">
    
        <include href="../../../plugins.xml"/>
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
    
        <VisualGrid size="0.1"/>
        <LineAxis size="0.1"/>
    
        <include href="../../../QuadraticTopology.xml"/>
    
        <Node name="simulation">
            <EulerImplicitIntegrationScheme name="backward_Euler" rayleighStiffness="0.1" rayleighMass="0.1" />
    
            <CGLinearSolver iterations="250" name="linear_solver" tolerance="1.0e-12" threshold="1.0e-12" />
    
            <Node name="beam">
                <MeshTopology name="topology"
                              position="@../../preprocessing/tetrahedra/engine.position"
                              quadratic_tetrahedra="@../../preprocessing/tetrahedra/engine.quadratic_tetrahedra"/>
                <MechanicalObject template="Vec3" name="state" position="@../../preprocessing/tetrahedra/engine.position"/>
    
                <VisualPointCloud position="@state.position" drawMode="Sphere" sphereRadius="0.0005" color="orange"/>
                <VisualMesh position="@state.position" topology="@topology"/>
    
                <NodalMassDensity property="1100"/>
                <FEMMass template="Vec3,QuadraticTetrahedron"/>
    
                <BoxROI template="Vec3" name="box_roi" box="-0.011 -0.011 -0.0001   0.011 0.011 0.0001" drawBoxes="1" />
                <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
    
                <CorotationalFEMForceField name="FEM" template="Vec3,QuadraticTetrahedron"
                                           youngModulus="2e6" poissonRatio="0.45" topology="@topology"
                                           computeForceStrategy="parallel" computeForceDerivStrategy="parallel"/>
            </Node>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.001", gravity="0 -9.81 0")

       root.addObject('include', href="../../../plugins.xml")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
       root.addObject('VisualGrid', size="0.1")
       root.addObject('LineAxis', size="0.1")
       root.addObject('include', href="../../../QuadraticTopology.xml")

       simulation = root.addChild('simulation')

       simulation.addObject('EulerImplicitIntegrationScheme', name="backward_Euler", rayleighStiffness="0.1", rayleighMass="0.1")
       simulation.addObject('CGLinearSolver', iterations="250", name="linear_solver", tolerance="1.0e-12", threshold="1.0e-12")

       beam = simulation.addChild('beam')

       beam.addObject('MeshTopology', name="topology", position="@../../preprocessing/tetrahedra/engine.position", quadratic_tetrahedra="@../../preprocessing/tetrahedra/engine.quadratic_tetrahedra")
       beam.addObject('MechanicalObject', template="Vec3", name="state", position="@../../preprocessing/tetrahedra/engine.position")
       beam.addObject('VisualPointCloud', position="@state.position", drawMode="Sphere", sphereRadius="0.0005", color="orange")
       beam.addObject('VisualMesh', position="@state.position", topology="@topology")
       beam.addObject('NodalMassDensity', property="1100")
       beam.addObject('FEMMass', template="Vec3,QuadraticTetrahedron")
       beam.addObject('BoxROI', template="Vec3", name="box_roi", box="-0.011 -0.011 -0.0001   0.011 0.011 0.0001", drawBoxes="1")
       beam.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")
       beam.addObject('CorotationalFEMForceField', name="FEM", template="Vec3,QuadraticTetrahedron", youngModulus="2e6", poissonRatio="0.45", topology="@topology", computeForceStrategy="parallel", computeForceDerivStrategy="parallel")
    ```

CorotationalFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.001" gravity="0 -9.81 0">
    
        <include href="../../../plugins.xml"/>
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
    
        <VisualGrid size="0.1"/>
        <LineAxis size="0.1"/>
    
        <include href="../../../QuadraticTopology.xml"/>
    
        <Node name="simulation">
            <EulerImplicitIntegrationScheme name="backward_Euler" rayleighStiffness="0.1" rayleighMass="0.1" />
    
            <ConstantSparsityPatternSystem template="CompressedRowSparseMatrix" name="A" checkIndices="false"/>
            <SparseLDLSolver name="linear_solver" template="CompressedRowSparseMatrix"/>
    
            <Node name="beam">
                <MeshTopology name="topology"
                              position="@../../preprocessing/tetrahedra/engine.position"
                              quadratic_tetrahedra="@../../preprocessing/tetrahedra/engine.quadratic_tetrahedra"/>
                <MechanicalObject template="Vec3" name="state" position="@../../preprocessing/tetrahedra/engine.position"/>
    
                <VisualPointCloud position="@state.position" drawMode="Sphere" sphereRadius="0.0005" color="orange"/>
                <VisualMesh position="@state.position" topology="@topology"/>
    
                <NodalMassDensity property="1100"/>
                <FEMMass template="Vec3,QuadraticTetrahedron"/>
    
                <BoxROI template="Vec3" name="box_roi" box="-0.011 -0.011 -0.0001   0.011 0.011 0.0001" drawBoxes="1" />
                <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
    
                <CorotationalFEMForceField name="FEM" template="Vec3,QuadraticTetrahedron"
                                           youngModulus="2e6" poissonRatio="0.45" topology="@topology"
                                           computeForceStrategy="sequenced" computeForceDerivStrategy="sequenced"/>
            </Node>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.001", gravity="0 -9.81 0")

       root.addObject('include', href="../../../plugins.xml")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
       root.addObject('VisualGrid', size="0.1")
       root.addObject('LineAxis', size="0.1")
       root.addObject('include', href="../../../QuadraticTopology.xml")

       simulation = root.addChild('simulation')

       simulation.addObject('EulerImplicitIntegrationScheme', name="backward_Euler", rayleighStiffness="0.1", rayleighMass="0.1")
       simulation.addObject('ConstantSparsityPatternSystem', template="CompressedRowSparseMatrix", name="A", checkIndices="false")
       simulation.addObject('SparseLDLSolver', name="linear_solver", template="CompressedRowSparseMatrix")

       beam = simulation.addChild('beam')

       beam.addObject('MeshTopology', name="topology", position="@../../preprocessing/tetrahedra/engine.position", quadratic_tetrahedra="@../../preprocessing/tetrahedra/engine.quadratic_tetrahedra")
       beam.addObject('MechanicalObject', template="Vec3", name="state", position="@../../preprocessing/tetrahedra/engine.position")
       beam.addObject('VisualPointCloud', position="@state.position", drawMode="Sphere", sphereRadius="0.0005", color="orange")
       beam.addObject('VisualMesh', position="@state.position", topology="@topology")
       beam.addObject('NodalMassDensity', property="1100")
       beam.addObject('FEMMass', template="Vec3,QuadraticTetrahedron")
       beam.addObject('BoxROI', template="Vec3", name="box_roi", box="-0.011 -0.011 -0.0001   0.011 0.011 0.0001", drawBoxes="1")
       beam.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")
       beam.addObject('CorotationalFEMForceField', name="FEM", template="Vec3,QuadraticTetrahedron", youngModulus="2e6", poissonRatio="0.45", topology="@topology", computeForceStrategy="sequenced", computeForceDerivStrategy="sequenced")
    ```

CorotationalFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.001" gravity="0 -9.81 0">
    
        <include href="../../../plugins.xml"/>
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
    
        <VisualGrid size="0.1"/>
        <LineAxis size="0.1"/>
    
        <include href="../../../QuadraticTopology.xml"/>
    
        <Node name="simulation">
            <EulerImplicitIntegrationScheme name="backward_Euler" rayleighStiffness="0.1" rayleighMass="0.1" />
    
            <CGLinearSolver iterations="250" name="linear_solver" tolerance="1.0e-12" threshold="1.0e-12" />
    
            <Node name="beam">
                <MeshTopology name="topology"
                              position="@../../preprocessing/tetrahedra/engine.position"
                              quadratic_tetrahedra="@../../preprocessing/tetrahedra/engine.quadratic_tetrahedra"/>
                <MechanicalObject template="Vec3" name="state" position="@../../preprocessing/tetrahedra/engine.position"/>
    
                <VisualPointCloud position="@state.position" drawMode="Sphere" sphereRadius="0.0005" color="orange"/>
                <VisualMesh position="@state.position" topology="@topology"/>
    
                <NodalMassDensity property="1100"/>
                <FEMMass template="Vec3,QuadraticTetrahedron"/>
    
                <BoxROI template="Vec3" name="box_roi" box="-0.011 -0.011 -0.0001   0.011 0.011 0.0001" drawBoxes="1" />
                <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
    
                <CorotationalFEMForceField name="FEM" template="Vec3,QuadraticTetrahedron"
                                           youngModulus="2e6" poissonRatio="0.45" topology="@topology"
                                           computeForceStrategy="sequenced" computeForceDerivStrategy="sequenced"/>
            </Node>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.001", gravity="0 -9.81 0")

       root.addObject('include', href="../../../plugins.xml")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
       root.addObject('VisualGrid', size="0.1")
       root.addObject('LineAxis', size="0.1")
       root.addObject('include', href="../../../QuadraticTopology.xml")

       simulation = root.addChild('simulation')

       simulation.addObject('EulerImplicitIntegrationScheme', name="backward_Euler", rayleighStiffness="0.1", rayleighMass="0.1")
       simulation.addObject('CGLinearSolver', iterations="250", name="linear_solver", tolerance="1.0e-12", threshold="1.0e-12")

       beam = simulation.addChild('beam')

       beam.addObject('MeshTopology', name="topology", position="@../../preprocessing/tetrahedra/engine.position", quadratic_tetrahedra="@../../preprocessing/tetrahedra/engine.quadratic_tetrahedra")
       beam.addObject('MechanicalObject', template="Vec3", name="state", position="@../../preprocessing/tetrahedra/engine.position")
       beam.addObject('VisualPointCloud', position="@state.position", drawMode="Sphere", sphereRadius="0.0005", color="orange")
       beam.addObject('VisualMesh', position="@state.position", topology="@topology")
       beam.addObject('NodalMassDensity', property="1100")
       beam.addObject('FEMMass', template="Vec3,QuadraticTetrahedron")
       beam.addObject('BoxROI', template="Vec3", name="box_roi", box="-0.011 -0.011 -0.0001   0.011 0.011 0.0001", drawBoxes="1")
       beam.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")
       beam.addObject('CorotationalFEMForceField', name="FEM", template="Vec3,QuadraticTetrahedron", youngModulus="2e6", poissonRatio="0.45", topology="@topology", computeForceStrategy="sequenced", computeForceDerivStrategy="sequenced")
    ```

CorotationalFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.001" gravity="0 -9.81 0">
    
        <include href="../../../plugins.xml"/>
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
    
        <VisualGrid size="0.1"/>
        <LineAxis size="0.1"/>
    
        <include href="../../../QuadraticTopology.xml"/>
    
        <Node name="simulation">
            <EulerImplicitIntegrationScheme name="backward_Euler" rayleighStiffness="0.1" rayleighMass="0.1" />
    
            <ConstantSparsityPatternSystem template="CompressedRowSparseMatrix" name="A" checkIndices="true"/>
            <SparseLDLSolver name="linear_solver" template="CompressedRowSparseMatrix"/>
    
            <Node name="beam">
                <MeshTopology name="topology"
                              position="@../../preprocessing/engine.position"
                              quadratic_hexahedra="@../../preprocessing/engine.quadratic_hexahedra"/>
                <MechanicalObject template="Vec3" name="state" position="@../../preprocessing/engine.position"/>
    
                <VisualPointCloud position="@state.position" drawMode="Sphere" sphereRadius="0.0005" color="orange"/>
                <VisualMesh position="@state.position" topology="@topology"/>
    
                <NodalMassDensity property="1100"/>
                <FEMMass template="Vec3,QuadraticHexahedron"/>
    
                <BoxROI template="Vec3" name="box_roi" box="-0.011 -0.011 -0.0001   0.011 0.011 0.0001" drawBoxes="1" />
                <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
    
                <CorotationalFEMForceField name="FEM" template="Vec3,QuadraticHexahedron" rotationMethod="polar"
                                           youngModulus="2e6" poissonRatio="0.45" topology="@topology"
                                           computeForceStrategy="parallel" computeForceDerivStrategy="parallel"/>
            </Node>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.001", gravity="0 -9.81 0")

       root.addObject('include', href="../../../plugins.xml")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
       root.addObject('VisualGrid', size="0.1")
       root.addObject('LineAxis', size="0.1")
       root.addObject('include', href="../../../QuadraticTopology.xml")

       simulation = root.addChild('simulation')

       simulation.addObject('EulerImplicitIntegrationScheme', name="backward_Euler", rayleighStiffness="0.1", rayleighMass="0.1")
       simulation.addObject('ConstantSparsityPatternSystem', template="CompressedRowSparseMatrix", name="A", checkIndices="true")
       simulation.addObject('SparseLDLSolver', name="linear_solver", template="CompressedRowSparseMatrix")

       beam = simulation.addChild('beam')

       beam.addObject('MeshTopology', name="topology", position="@../../preprocessing/engine.position", quadratic_hexahedra="@../../preprocessing/engine.quadratic_hexahedra")
       beam.addObject('MechanicalObject', template="Vec3", name="state", position="@../../preprocessing/engine.position")
       beam.addObject('VisualPointCloud', position="@state.position", drawMode="Sphere", sphereRadius="0.0005", color="orange")
       beam.addObject('VisualMesh', position="@state.position", topology="@topology")
       beam.addObject('NodalMassDensity', property="1100")
       beam.addObject('FEMMass', template="Vec3,QuadraticHexahedron")
       beam.addObject('BoxROI', template="Vec3", name="box_roi", box="-0.011 -0.011 -0.0001   0.011 0.011 0.0001", drawBoxes="1")
       beam.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")
       beam.addObject('CorotationalFEMForceField', name="FEM", template="Vec3,QuadraticHexahedron", rotationMethod="polar", youngModulus="2e6", poissonRatio="0.45", topology="@topology", computeForceStrategy="parallel", computeForceDerivStrategy="parallel")
    ```

CorotationalFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.001" gravity="0 -9.81 0">
    
        <include href="../../../plugins.xml"/>
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
    
        <VisualGrid size="0.1"/>
        <LineAxis size="0.1"/>
    
        <include href="../../../QuadraticTopology.xml"/>
    
        <Node name="simulation">
            <EulerImplicitIntegrationScheme name="backward_Euler" rayleighStiffness="0.1" rayleighMass="0.1" />
    
            <CGLinearSolver iterations="250" name="linear_solver" tolerance="1.0e-12" threshold="1.0e-12" />
    
            <Node name="beam">
                <MeshTopology name="topology"
                              position="@../../preprocessing/engine.position"
                              quadratic_hexahedra="@../../preprocessing/engine.quadratic_hexahedra"/>
                <MechanicalObject template="Vec3" name="state" position="@../../preprocessing/engine.position"/>
    
                <VisualPointCloud position="@state.position" drawMode="Sphere" sphereRadius="0.0005" color="orange"/>
                <VisualMesh position="@state.position" topology="@topology"/>
    
                <NodalMassDensity property="1100"/>
                <FEMMass template="Vec3,QuadraticHexahedron"/>
    
                <BoxROI template="Vec3" name="box_roi" box="-0.011 -0.011 -0.0001   0.011 0.011 0.0001" drawBoxes="1" />
                <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
    
                <CorotationalFEMForceField name="FEM" template="Vec3,QuadraticHexahedron" rotationMethod="polar"
                                           youngModulus="2e6" poissonRatio="0.45" topology="@topology"
                                           computeForceStrategy="parallel" computeForceDerivStrategy="parallel"/>
            </Node>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.001", gravity="0 -9.81 0")

       root.addObject('include', href="../../../plugins.xml")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
       root.addObject('VisualGrid', size="0.1")
       root.addObject('LineAxis', size="0.1")
       root.addObject('include', href="../../../QuadraticTopology.xml")

       simulation = root.addChild('simulation')

       simulation.addObject('EulerImplicitIntegrationScheme', name="backward_Euler", rayleighStiffness="0.1", rayleighMass="0.1")
       simulation.addObject('CGLinearSolver', iterations="250", name="linear_solver", tolerance="1.0e-12", threshold="1.0e-12")

       beam = simulation.addChild('beam')

       beam.addObject('MeshTopology', name="topology", position="@../../preprocessing/engine.position", quadratic_hexahedra="@../../preprocessing/engine.quadratic_hexahedra")
       beam.addObject('MechanicalObject', template="Vec3", name="state", position="@../../preprocessing/engine.position")
       beam.addObject('VisualPointCloud', position="@state.position", drawMode="Sphere", sphereRadius="0.0005", color="orange")
       beam.addObject('VisualMesh', position="@state.position", topology="@topology")
       beam.addObject('NodalMassDensity', property="1100")
       beam.addObject('FEMMass', template="Vec3,QuadraticHexahedron")
       beam.addObject('BoxROI', template="Vec3", name="box_roi", box="-0.011 -0.011 -0.0001   0.011 0.011 0.0001", drawBoxes="1")
       beam.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")
       beam.addObject('CorotationalFEMForceField', name="FEM", template="Vec3,QuadraticHexahedron", rotationMethod="polar", youngModulus="2e6", poissonRatio="0.45", topology="@topology", computeForceStrategy="parallel", computeForceDerivStrategy="parallel")
    ```

CorotationalFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.001" gravity="0 -9.81 0">
    
        <include href="../../../plugins.xml"/>
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
    
        <VisualGrid size="0.1"/>
        <LineAxis size="0.1"/>
    
        <include href="../../../QuadraticTopology.xml"/>
    
        <Node name="simulation">
            <EulerImplicitIntegrationScheme name="backward_Euler" rayleighStiffness="0.1" rayleighMass="0.1" />
    
            <ConstantSparsityPatternSystem template="CompressedRowSparseMatrix" name="A" checkIndices="true"/>
            <SparseLDLSolver name="linear_solver" template="CompressedRowSparseMatrix"/>
    
            <Node name="beam">
                <MeshTopology name="topology"
                              position="@../../preprocessing/engine.position"
                              quadratic_hexahedra="@../../preprocessing/engine.quadratic_hexahedra"/>
                <MechanicalObject template="Vec3" name="state" position="@../../preprocessing/engine.position"/>
    
                <VisualPointCloud position="@state.position" drawMode="Sphere" sphereRadius="0.0005" color="orange"/>
                <VisualMesh position="@state.position" topology="@topology"/>
    
                <NodalMassDensity property="1100"/>
                <FEMMass template="Vec3,QuadraticHexahedron"/>
    
                <BoxROI template="Vec3" name="box_roi" box="-0.011 -0.011 -0.0001   0.011 0.011 0.0001" drawBoxes="1" />
                <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
    
                <CorotationalFEMForceField name="FEM" template="Vec3,QuadraticHexahedron" rotationMethod="polar"
                                           youngModulus="2e6" poissonRatio="0.45" topology="@topology"
                                           computeForceStrategy="sequenced" computeForceDerivStrategy="sequenced"/>
            </Node>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.001", gravity="0 -9.81 0")

       root.addObject('include', href="../../../plugins.xml")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
       root.addObject('VisualGrid', size="0.1")
       root.addObject('LineAxis', size="0.1")
       root.addObject('include', href="../../../QuadraticTopology.xml")

       simulation = root.addChild('simulation')

       simulation.addObject('EulerImplicitIntegrationScheme', name="backward_Euler", rayleighStiffness="0.1", rayleighMass="0.1")
       simulation.addObject('ConstantSparsityPatternSystem', template="CompressedRowSparseMatrix", name="A", checkIndices="true")
       simulation.addObject('SparseLDLSolver', name="linear_solver", template="CompressedRowSparseMatrix")

       beam = simulation.addChild('beam')

       beam.addObject('MeshTopology', name="topology", position="@../../preprocessing/engine.position", quadratic_hexahedra="@../../preprocessing/engine.quadratic_hexahedra")
       beam.addObject('MechanicalObject', template="Vec3", name="state", position="@../../preprocessing/engine.position")
       beam.addObject('VisualPointCloud', position="@state.position", drawMode="Sphere", sphereRadius="0.0005", color="orange")
       beam.addObject('VisualMesh', position="@state.position", topology="@topology")
       beam.addObject('NodalMassDensity', property="1100")
       beam.addObject('FEMMass', template="Vec3,QuadraticHexahedron")
       beam.addObject('BoxROI', template="Vec3", name="box_roi", box="-0.011 -0.011 -0.0001   0.011 0.011 0.0001", drawBoxes="1")
       beam.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")
       beam.addObject('CorotationalFEMForceField', name="FEM", template="Vec3,QuadraticHexahedron", rotationMethod="polar", youngModulus="2e6", poissonRatio="0.45", topology="@topology", computeForceStrategy="sequenced", computeForceDerivStrategy="sequenced")
    ```

CorotationalFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.001" gravity="0 -9.81 0">
        <include href="../../../plugins.xml"/>
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
    
        <VisualGrid size="0.1"/>
        <LineAxis size="0.1"/>
    
        <include href="../../../QuadraticTopology.xml"/>
    
        <Node name="simulation">
            <EulerImplicitIntegrationScheme name="backward_Euler" rayleighStiffness="0.1" rayleighMass="0.1" />
    
            <CGLinearSolver iterations="250" name="linear_solver" tolerance="1.0e-12" threshold="1.0e-12" />
    
            <Node name="beam">
                <MeshTopology name="topology"
                              position="@../../preprocessing/engine.position"
                              quadratic_hexahedra="@../../preprocessing/engine.quadratic_hexahedra"/>
                <MechanicalObject template="Vec3" name="state" position="@../../preprocessing/engine.position"/>
    
                <VisualPointCloud position="@state.position" drawMode="Sphere" sphereRadius="0.0005" color="orange"/>
                <VisualMesh position="@state.position" topology="@topology"/>
    
                <NodalMassDensity property="1100"/>
                <FEMMass template="Vec3,QuadraticHexahedron"/>
    
                <BoxROI template="Vec3" name="box_roi" box="-0.011 -0.011 -0.0001   0.011 0.011 0.0001" drawBoxes="1" />
                <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
    
                <CorotationalFEMForceField name="FEM" template="Vec3,QuadraticHexahedron" rotationMethod="polar"
                                           youngModulus="2e6" poissonRatio="0.45" topology="@topology"
                                           computeForceStrategy="sequenced" computeForceDerivStrategy="sequenced"/>
            </Node>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.001", gravity="0 -9.81 0")

       root.addObject('include', href="../../../plugins.xml")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
       root.addObject('VisualGrid', size="0.1")
       root.addObject('LineAxis', size="0.1")
       root.addObject('include', href="../../../QuadraticTopology.xml")

       simulation = root.addChild('simulation')

       simulation.addObject('EulerImplicitIntegrationScheme', name="backward_Euler", rayleighStiffness="0.1", rayleighMass="0.1")
       simulation.addObject('CGLinearSolver', iterations="250", name="linear_solver", tolerance="1.0e-12", threshold="1.0e-12")

       beam = simulation.addChild('beam')

       beam.addObject('MeshTopology', name="topology", position="@../../preprocessing/engine.position", quadratic_hexahedra="@../../preprocessing/engine.quadratic_hexahedra")
       beam.addObject('MechanicalObject', template="Vec3", name="state", position="@../../preprocessing/engine.position")
       beam.addObject('VisualPointCloud', position="@state.position", drawMode="Sphere", sphereRadius="0.0005", color="orange")
       beam.addObject('VisualMesh', position="@state.position", topology="@topology")
       beam.addObject('NodalMassDensity', property="1100")
       beam.addObject('FEMMass', template="Vec3,QuadraticHexahedron")
       beam.addObject('BoxROI', template="Vec3", name="box_roi", box="-0.011 -0.011 -0.0001   0.011 0.011 0.0001", drawBoxes="1")
       beam.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")
       beam.addObject('CorotationalFEMForceField', name="FEM", template="Vec3,QuadraticHexahedron", rotationMethod="polar", youngModulus="2e6", poissonRatio="0.45", topology="@topology", computeForceStrategy="sequenced", computeForceDerivStrategy="sequenced")
    ```

CorotationalFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 0 0">
        <include href="../../../../beam.xml"/>
    
        <ConstantSparsityPatternSystem template="CompressedRowSparseMatrix" name="A" checkIndices="false"/>
        <NaturalOrderingMethod/>
        <SparseLDLSolver name="linear_solver" template="CompressedRowSparseMatrix"/>
    
        <CorotationalFEMForceField name="FEM" template="Vec3,Hexahedron"
                                   youngModulus="2e6" poissonRatio="0.45" topology="@grid"
                                   computeForceStrategy="parallel" computeForceDerivStrategy="parallel"/>
        <VonMisesStress template="Vec3,Hexahedron" name="stress" topology="@grid" stressEvaluator="@FEM"
                        colorMap="green yellow orange red purple #221C35"/>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 0 0")

       root.addObject('include', href="../../../../beam.xml")
       root.addObject('ConstantSparsityPatternSystem', template="CompressedRowSparseMatrix", name="A", checkIndices="false")
       root.addObject('NaturalOrderingMethod', )
       root.addObject('SparseLDLSolver', name="linear_solver", template="CompressedRowSparseMatrix")
       root.addObject('CorotationalFEMForceField', name="FEM", template="Vec3,Hexahedron", youngModulus="2e6", poissonRatio="0.45", topology="@grid", computeForceStrategy="parallel", computeForceDerivStrategy="parallel")
       root.addObject('VonMisesStress', template="Vec3,Hexahedron", name="stress", topology="@grid", stressEvaluator="@FEM", colorMap="green yellow orange red purple #221C35")
    ```

CorotationalFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 0 0">
        <include href="../../../../beam.xml"/>
    
        <CGLinearSolver iterations="250" name="linear_solver" tolerance="1.0e-12" threshold="1.0e-12" />
    
        <CorotationalFEMForceField name="FEM" template="Vec3,Hexahedron"
                                   youngModulus="2e6" poissonRatio="0.45" topology="@grid"
                                   computeForceStrategy="parallel" computeForceDerivStrategy="parallel"/>
        <VonMisesStress template="Vec3,Hexahedron" name="stress" topology="@grid" stressEvaluator="@FEM"
                        colorMap="green yellow orange red purple #221C35"/>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 0 0")

       root.addObject('include', href="../../../../beam.xml")
       root.addObject('CGLinearSolver', iterations="250", name="linear_solver", tolerance="1.0e-12", threshold="1.0e-12")
       root.addObject('CorotationalFEMForceField', name="FEM", template="Vec3,Hexahedron", youngModulus="2e6", poissonRatio="0.45", topology="@grid", computeForceStrategy="parallel", computeForceDerivStrategy="parallel")
       root.addObject('VonMisesStress', template="Vec3,Hexahedron", name="stress", topology="@grid", stressEvaluator="@FEM", colorMap="green yellow orange red purple #221C35")
    ```

CorotationalFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 0 0">
        <include href="../../../../beam.xml"/>
    
        <ConstantSparsityPatternSystem template="CompressedRowSparseMatrix" name="A" checkIndices="false"/>
        <NaturalOrderingMethod/>
        <SparseLDLSolver name="linear_solver" template="CompressedRowSparseMatrix"/>
    
        <CorotationalFEMForceField name="FEM" template="Vec3,Hexahedron"
                                   youngModulus="2e6" poissonRatio="0.45" topology="@grid"
                                   computeForceStrategy="sequenced" computeForceDerivStrategy="sequenced"/>
        <VonMisesStress template="Vec3,Hexahedron" name="stress" topology="@grid" stressEvaluator="@FEM"
                        colorMap="green yellow orange red purple #221C35"/>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 0 0")

       root.addObject('include', href="../../../../beam.xml")
       root.addObject('ConstantSparsityPatternSystem', template="CompressedRowSparseMatrix", name="A", checkIndices="false")
       root.addObject('NaturalOrderingMethod', )
       root.addObject('SparseLDLSolver', name="linear_solver", template="CompressedRowSparseMatrix")
       root.addObject('CorotationalFEMForceField', name="FEM", template="Vec3,Hexahedron", youngModulus="2e6", poissonRatio="0.45", topology="@grid", computeForceStrategy="sequenced", computeForceDerivStrategy="sequenced")
       root.addObject('VonMisesStress', template="Vec3,Hexahedron", name="stress", topology="@grid", stressEvaluator="@FEM", colorMap="green yellow orange red purple #221C35")
    ```

CorotationalFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 0 0">
        <include href="../../../../beam.xml"/>
    
        <CGLinearSolver iterations="250" name="linear_solver" tolerance="1.0e-12" threshold="1.0e-12" />
    
        <CorotationalFEMForceField name="FEM" template="Vec3,Hexahedron"
                                   youngModulus="2e6" poissonRatio="0.45" topology="@grid"
                                   computeForceStrategy="sequenced" computeForceDerivStrategy="sequenced"/>
        <VonMisesStress template="Vec3,Hexahedron" name="stress" topology="@grid" stressEvaluator="@FEM"
                        colorMap="green yellow orange red purple #221C35"/>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 0 0")

       root.addObject('include', href="../../../../beam.xml")
       root.addObject('CGLinearSolver', iterations="250", name="linear_solver", tolerance="1.0e-12", threshold="1.0e-12")
       root.addObject('CorotationalFEMForceField', name="FEM", template="Vec3,Hexahedron", youngModulus="2e6", poissonRatio="0.45", topology="@grid", computeForceStrategy="sequenced", computeForceDerivStrategy="sequenced")
       root.addObject('VonMisesStress', template="Vec3,Hexahedron", name="stress", topology="@grid", stressEvaluator="@FEM", colorMap="green yellow orange red purple #221C35")
    ```

CorotationalFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 0 0">
        <include href="../../../../beam.xml"/>
    
        <ConstantSparsityPatternSystem template="CompressedRowSparseMatrix" name="A" checkIndices="false"/>
        <NaturalOrderingMethod/>
        <SparseLDLSolver name="linear_solver" template="CompressedRowSparseMatrix"/>
    
        <Node name="fem">
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" drawTetrahedra="false"/>
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" swapping="true"/>
    
            <CorotationalFEMForceField name="FEM" template="Vec3,Tetrahedron"
                                       youngModulus="2e6" poissonRatio="0.45" topology="@Tetra_topo"
                                       computeForceStrategy="parallel" computeForceDerivStrategy="parallel"/>
            <VonMisesStress template="Vec3,Tetrahedron" name="stress" topology="@Tetra_topo" stressEvaluator="@FEM"
                            colorMap="green yellow orange red purple #221C35"/>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 0 0")

       root.addObject('include', href="../../../../beam.xml")
       root.addObject('ConstantSparsityPatternSystem', template="CompressedRowSparseMatrix", name="A", checkIndices="false")
       root.addObject('NaturalOrderingMethod', )
       root.addObject('SparseLDLSolver', name="linear_solver", template="CompressedRowSparseMatrix")

       fem = root.addChild('fem')

       fem.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
       fem.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       fem.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo", drawTetrahedra="false")
       fem.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo", swapping="true")
       fem.addObject('CorotationalFEMForceField', name="FEM", template="Vec3,Tetrahedron", youngModulus="2e6", poissonRatio="0.45", topology="@Tetra_topo", computeForceStrategy="parallel", computeForceDerivStrategy="parallel")
       fem.addObject('VonMisesStress', template="Vec3,Tetrahedron", name="stress", topology="@Tetra_topo", stressEvaluator="@FEM", colorMap="green yellow orange red purple #221C35")
    ```

CorotationalFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 0 0">
        <include href="../../../../beam.xml"/>
    
        <CGLinearSolver iterations="250" name="linear_solver" tolerance="1.0e-12" threshold="1.0e-12" />
    
        <Node name="fem">
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" drawTetrahedra="false"/>
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" swapping="true"/>
    
            <CorotationalFEMForceField name="FEM" template="Vec3,Tetrahedron"
                                       youngModulus="2e6" poissonRatio="0.45" topology="@Tetra_topo"
                                       computeForceStrategy="parallel" computeForceDerivStrategy="parallel"/>
            <VonMisesStress template="Vec3,Tetrahedron" name="stress" topology="@Tetra_topo" stressEvaluator="@FEM"
                            colorMap="green yellow orange red purple #221C35"/>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 0 0")

       root.addObject('include', href="../../../../beam.xml")
       root.addObject('CGLinearSolver', iterations="250", name="linear_solver", tolerance="1.0e-12", threshold="1.0e-12")

       fem = root.addChild('fem')

       fem.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
       fem.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       fem.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo", drawTetrahedra="false")
       fem.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo", swapping="true")
       fem.addObject('CorotationalFEMForceField', name="FEM", template="Vec3,Tetrahedron", youngModulus="2e6", poissonRatio="0.45", topology="@Tetra_topo", computeForceStrategy="parallel", computeForceDerivStrategy="parallel")
       fem.addObject('VonMisesStress', template="Vec3,Tetrahedron", name="stress", topology="@Tetra_topo", stressEvaluator="@FEM", colorMap="green yellow orange red purple #221C35")
    ```

CorotationalFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 0 0">
        <include href="../../../../beam.xml"/>
    
        <ConstantSparsityPatternSystem template="CompressedRowSparseMatrix" name="A" checkIndices="false"/>
        <NaturalOrderingMethod/>
        <SparseLDLSolver name="linear_solver" template="CompressedRowSparseMatrix"/>
    
        <Node name="fem">
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" drawTetrahedra="false"/>
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" swapping="true"/>
    
            <CorotationalFEMForceField name="FEM" template="Vec3,Tetrahedron"
                                       youngModulus="2e6" poissonRatio="0.45" topology="@Tetra_topo"
                                       computeForceStrategy="sequenced" computeForceDerivStrategy="sequenced"/>
            <VonMisesStress template="Vec3,Tetrahedron" name="stress" topology="@Tetra_topo" stressEvaluator="@FEM"
                            colorMap="green yellow orange red purple #221C35"/>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 0 0")

       root.addObject('include', href="../../../../beam.xml")
       root.addObject('ConstantSparsityPatternSystem', template="CompressedRowSparseMatrix", name="A", checkIndices="false")
       root.addObject('NaturalOrderingMethod', )
       root.addObject('SparseLDLSolver', name="linear_solver", template="CompressedRowSparseMatrix")

       fem = root.addChild('fem')

       fem.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
       fem.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       fem.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo", drawTetrahedra="false")
       fem.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo", swapping="true")
       fem.addObject('CorotationalFEMForceField', name="FEM", template="Vec3,Tetrahedron", youngModulus="2e6", poissonRatio="0.45", topology="@Tetra_topo", computeForceStrategy="sequenced", computeForceDerivStrategy="sequenced")
       fem.addObject('VonMisesStress', template="Vec3,Tetrahedron", name="stress", topology="@Tetra_topo", stressEvaluator="@FEM", colorMap="green yellow orange red purple #221C35")
    ```

CorotationalFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 0 0">
        <include href="../../../../beam.xml"/>
    
        <CGLinearSolver iterations="250" name="linear_solver" tolerance="1.0e-12" threshold="1.0e-12" />
    
        <Node name="fem">
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" drawTetrahedra="false"/>
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" swapping="true"/>
    
            <CorotationalFEMForceField name="FEM" template="Vec3,Tetrahedron"
                                       youngModulus="2e6" poissonRatio="0.45" topology="@Tetra_topo"
                                       computeForceStrategy="sequenced" computeForceDerivStrategy="sequenced"/>
            <VonMisesStress template="Vec3,Tetrahedron" name="stress" topology="@Tetra_topo" stressEvaluator="@FEM"
                            colorMap="green yellow orange red purple #221C35"/>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 0 0")

       root.addObject('include', href="../../../../beam.xml")
       root.addObject('CGLinearSolver', iterations="250", name="linear_solver", tolerance="1.0e-12", threshold="1.0e-12")

       fem = root.addChild('fem')

       fem.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
       fem.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       fem.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo", drawTetrahedra="false")
       fem.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo", swapping="true")
       fem.addObject('CorotationalFEMForceField', name="FEM", template="Vec3,Tetrahedron", youngModulus="2e6", poissonRatio="0.45", topology="@Tetra_topo", computeForceStrategy="sequenced", computeForceDerivStrategy="sequenced")
       fem.addObject('VonMisesStress', template="Vec3,Tetrahedron", name="stress", topology="@Tetra_topo", stressEvaluator="@FEM", colorMap="green yellow orange red purple #221C35")
    ```

