<!-- generate_doc -->
# HyperelasticityFEMForceField

Hyperelasticity


## Vec1d,Edge

Templates:

- Vec1d,Edge

__Target__: Sofa.Component.SolidMechanics.FEM.HyperElastic

__namespace__: sofa::component::solidmechanics::fem::hyperelastic

__parents__:

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
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec1d&gt;|
|topology|Link to a topology|BaseMeshTopology|
|material|Link to the material containing the constitutive law|HyperelasticMaterial&lt;Vec1d&gt;|

<!-- generate_doc -->
## Vec2d,Quad...

Templates:

- Vec2d,Quad
- Vec2d,Triangle

__Target__: Sofa.Component.SolidMechanics.FEM.HyperElastic

__namespace__: sofa::component::solidmechanics::fem::hyperelastic

__parents__:

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
|material|Link to the material containing the constitutive law|HyperelasticMaterial&lt;Vec2d&gt;|

<!-- generate_doc -->
## Vec3d,Hexahedron...

Templates:

- Vec3d,Hexahedron
- Vec3d,Tetrahedron

__Target__: Sofa.Component.SolidMechanics.FEM.HyperElastic

__namespace__: sofa::component::solidmechanics::fem::hyperelastic

__parents__:

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
|material|Link to the material containing the constitutive law|HyperelasticMaterial&lt;Vec3d&gt;|

## Examples 

HyperelasticityFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 -9.81 0">
        <include href="../../../../CantileverBeam_ElementFEMForceField.xml"/>
    
        <ConstantSparsityPatternSystem template="CompressedRowSparseMatrix" name="A" checkIndices="false"/>
        <NaturalOrderingMethod/>
        <SparseLDLSolver name="linear_solver" template="CompressedRowSparseMatrix"/>
    
        <StVenantKirchhoffMaterial name="material" youngModulus="2e6" poissonRatio="0.45"/>
        <HyperelasticityFEMForceField name="FEM" template="Vec3,Hexahedron" topology="@grid"
                                      computeForceStrategy="parallel" computeForceDerivStrategy="parallel"/>
        <VonMisesStress template="Vec3,Hexahedron" name="stress" topology="@grid" stressEvaluator="@material"
                        colorMap="green yellow orange red purple #221C35"/>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 -9.81 0")

       root.addObject('include', href="../../../../CantileverBeam_ElementFEMForceField.xml")
       root.addObject('ConstantSparsityPatternSystem', template="CompressedRowSparseMatrix", name="A", checkIndices="false")
       root.addObject('NaturalOrderingMethod', )
       root.addObject('SparseLDLSolver', name="linear_solver", template="CompressedRowSparseMatrix")
       root.addObject('StVenantKirchhoffMaterial', name="material", youngModulus="2e6", poissonRatio="0.45")
       root.addObject('HyperelasticityFEMForceField', name="FEM", template="Vec3,Hexahedron", topology="@grid", computeForceStrategy="parallel", computeForceDerivStrategy="parallel")
       root.addObject('VonMisesStress', template="Vec3,Hexahedron", name="stress", topology="@grid", stressEvaluator="@material", colorMap="green yellow orange red purple #221C35")
    ```

HyperelasticityFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 -9.81 0">
        <include href="../../../../CantileverBeam_ElementFEMForceField.xml"/>
    
        <CGLinearSolver iterations="250" name="linear_solver" tolerance="1.0e-12" threshold="1.0e-12" />
    
        <StVenantKirchhoffMaterial name="material" youngModulus="2e6" poissonRatio="0.45"/>
        <HyperelasticityFEMForceField name="FEM" template="Vec3,Hexahedron" topology="@grid"
                                      computeForceStrategy="parallel" computeForceDerivStrategy="parallel"/>
        <VonMisesStress template="Vec3,Hexahedron" name="stress" topology="@grid" stressEvaluator="@material"
                        colorMap="green yellow orange red purple #221C35"/>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 -9.81 0")

       root.addObject('include', href="../../../../CantileverBeam_ElementFEMForceField.xml")
       root.addObject('CGLinearSolver', iterations="250", name="linear_solver", tolerance="1.0e-12", threshold="1.0e-12")
       root.addObject('StVenantKirchhoffMaterial', name="material", youngModulus="2e6", poissonRatio="0.45")
       root.addObject('HyperelasticityFEMForceField', name="FEM", template="Vec3,Hexahedron", topology="@grid", computeForceStrategy="parallel", computeForceDerivStrategy="parallel")
       root.addObject('VonMisesStress', template="Vec3,Hexahedron", name="stress", topology="@grid", stressEvaluator="@material", colorMap="green yellow orange red purple #221C35")
    ```

HyperelasticityFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 -9.81 0">
        <include href="../../../../CantileverBeam_ElementFEMForceField.xml"/>
    
        <ConstantSparsityPatternSystem template="CompressedRowSparseMatrix" name="A" checkIndices="false"/>
        <NaturalOrderingMethod/>
        <SparseLDLSolver name="linear_solver" template="CompressedRowSparseMatrix"/>
    
        <StVenantKirchhoffMaterial name="material" youngModulus="2e6" poissonRatio="0.45"/>
        <HyperelasticityFEMForceField name="FEM" template="Vec3,Hexahedron" topology="@grid"
                                      computeForceStrategy="sequenced" computeForceDerivStrategy="sequenced"/>
        <VonMisesStress template="Vec3,Hexahedron" name="stress" topology="@grid" stressEvaluator="@material"
                        colorMap="green yellow orange red purple #221C35"/>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 -9.81 0")

       root.addObject('include', href="../../../../CantileverBeam_ElementFEMForceField.xml")
       root.addObject('ConstantSparsityPatternSystem', template="CompressedRowSparseMatrix", name="A", checkIndices="false")
       root.addObject('NaturalOrderingMethod', )
       root.addObject('SparseLDLSolver', name="linear_solver", template="CompressedRowSparseMatrix")
       root.addObject('StVenantKirchhoffMaterial', name="material", youngModulus="2e6", poissonRatio="0.45")
       root.addObject('HyperelasticityFEMForceField', name="FEM", template="Vec3,Hexahedron", topology="@grid", computeForceStrategy="sequenced", computeForceDerivStrategy="sequenced")
       root.addObject('VonMisesStress', template="Vec3,Hexahedron", name="stress", topology="@grid", stressEvaluator="@material", colorMap="green yellow orange red purple #221C35")
    ```

HyperelasticityFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 -9.81 0">
        <include href="../../../../CantileverBeam_ElementFEMForceField.xml"/>
    
        <CGLinearSolver iterations="250" name="linear_solver" tolerance="1.0e-12" threshold="1.0e-12" />
    
        <StVenantKirchhoffMaterial name="material" youngModulus="2e6" poissonRatio="0.45"/>
        <HyperelasticityFEMForceField name="FEM" template="Vec3,Hexahedron" topology="@grid"
                                      computeForceStrategy="sequenced" computeForceDerivStrategy="sequenced"/>
        <VonMisesStress template="Vec3,Hexahedron" name="stress" topology="@grid" stressEvaluator="@material"
                        colorMap="green yellow orange red purple #221C35"/>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 -9.81 0")

       root.addObject('include', href="../../../../CantileverBeam_ElementFEMForceField.xml")
       root.addObject('CGLinearSolver', iterations="250", name="linear_solver", tolerance="1.0e-12", threshold="1.0e-12")
       root.addObject('StVenantKirchhoffMaterial', name="material", youngModulus="2e6", poissonRatio="0.45")
       root.addObject('HyperelasticityFEMForceField', name="FEM", template="Vec3,Hexahedron", topology="@grid", computeForceStrategy="sequenced", computeForceDerivStrategy="sequenced")
       root.addObject('VonMisesStress', template="Vec3,Hexahedron", name="stress", topology="@grid", stressEvaluator="@material", colorMap="green yellow orange red purple #221C35")
    ```

HyperelasticityFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 -9.81 0">
        <include href="../../../../CantileverBeam_ElementFEMForceField.xml"/>
    
        <ConstantSparsityPatternSystem template="CompressedRowSparseMatrix" name="A" checkIndices="false"/>
        <NaturalOrderingMethod/>
        <SparseLDLSolver name="linear_solver" template="CompressedRowSparseMatrix"/>
    
        <Node name="fem">
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" drawTetrahedra="false"/>
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" swapping="true"/>
    
            <StVenantKirchhoffMaterial name="material" youngModulus="2e6" poissonRatio="0.45"/>
            <HyperelasticityFEMForceField name="FEM" template="Vec3,Tetrahedron" topology="@Tetra_topo"
                                          computeForceStrategy="parallel" computeForceDerivStrategy="parallel"/>
            <VonMisesStress template="Vec3,Tetrahedron" name="stress" topology="@Tetra_topo" stressEvaluator="@material"
                            colorMap="green yellow orange red purple #221C35"/>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 -9.81 0")

       root.addObject('include', href="../../../../CantileverBeam_ElementFEMForceField.xml")
       root.addObject('ConstantSparsityPatternSystem', template="CompressedRowSparseMatrix", name="A", checkIndices="false")
       root.addObject('NaturalOrderingMethod', )
       root.addObject('SparseLDLSolver', name="linear_solver", template="CompressedRowSparseMatrix")

       fem = root.addChild('fem')

       fem.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
       fem.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       fem.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo", drawTetrahedra="false")
       fem.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo", swapping="true")
       fem.addObject('StVenantKirchhoffMaterial', name="material", youngModulus="2e6", poissonRatio="0.45")
       fem.addObject('HyperelasticityFEMForceField', name="FEM", template="Vec3,Tetrahedron", topology="@Tetra_topo", computeForceStrategy="parallel", computeForceDerivStrategy="parallel")
       fem.addObject('VonMisesStress', template="Vec3,Tetrahedron", name="stress", topology="@Tetra_topo", stressEvaluator="@material", colorMap="green yellow orange red purple #221C35")
    ```

HyperelasticityFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 -9.81 0">
        <include href="../../../../CantileverBeam_ElementFEMForceField.xml"/>
    
        <CGLinearSolver iterations="250" name="linear_solver" tolerance="1.0e-12" threshold="1.0e-12" />
    
        <Node name="fem">
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" drawTetrahedra="false"/>
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" swapping="true"/>
    
            <StVenantKirchhoffMaterial name="material" youngModulus="2e6" poissonRatio="0.45"/>
            <HyperelasticityFEMForceField name="FEM" template="Vec3,Tetrahedron" topology="@Tetra_topo"
                                          computeForceStrategy="parallel" computeForceDerivStrategy="parallel"/>
            <VonMisesStress template="Vec3,Tetrahedron" name="stress" topology="@Tetra_topo" stressEvaluator="@material"
                            colorMap="green yellow orange red purple #221C35"/>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 -9.81 0")

       root.addObject('include', href="../../../../CantileverBeam_ElementFEMForceField.xml")
       root.addObject('CGLinearSolver', iterations="250", name="linear_solver", tolerance="1.0e-12", threshold="1.0e-12")

       fem = root.addChild('fem')

       fem.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
       fem.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       fem.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo", drawTetrahedra="false")
       fem.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo", swapping="true")
       fem.addObject('StVenantKirchhoffMaterial', name="material", youngModulus="2e6", poissonRatio="0.45")
       fem.addObject('HyperelasticityFEMForceField', name="FEM", template="Vec3,Tetrahedron", topology="@Tetra_topo", computeForceStrategy="parallel", computeForceDerivStrategy="parallel")
       fem.addObject('VonMisesStress', template="Vec3,Tetrahedron", name="stress", topology="@Tetra_topo", stressEvaluator="@material", colorMap="green yellow orange red purple #221C35")
    ```

HyperelasticityFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 -9.81 0">
        <include href="../../../../CantileverBeam_ElementFEMForceField.xml"/>
    
        <ConstantSparsityPatternSystem template="CompressedRowSparseMatrix" name="A" checkIndices="false"/>
        <NaturalOrderingMethod/>
        <SparseLDLSolver name="linear_solver" template="CompressedRowSparseMatrix"/>
    
        <Node name="fem">
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" drawTetrahedra="false"/>
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" swapping="true"/>
    
            <StVenantKirchhoffMaterial name="material" youngModulus="2e6" poissonRatio="0.45"/>
            <HyperelasticityFEMForceField name="FEM" template="Vec3,Tetrahedron" topology="@Tetra_topo"
                                          computeForceStrategy="sequenced" computeForceDerivStrategy="sequenced"/>
            <VonMisesStress template="Vec3,Tetrahedron" name="stress" topology="@Tetra_topo" stressEvaluator="@material"
                            colorMap="green yellow orange red purple #221C35"/>
        </Node>
    
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 -9.81 0")

       root.addObject('include', href="../../../../CantileverBeam_ElementFEMForceField.xml")
       root.addObject('ConstantSparsityPatternSystem', template="CompressedRowSparseMatrix", name="A", checkIndices="false")
       root.addObject('NaturalOrderingMethod', )
       root.addObject('SparseLDLSolver', name="linear_solver", template="CompressedRowSparseMatrix")

       fem = root.addChild('fem')

       fem.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
       fem.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       fem.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo", drawTetrahedra="false")
       fem.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo", swapping="true")
       fem.addObject('StVenantKirchhoffMaterial', name="material", youngModulus="2e6", poissonRatio="0.45")
       fem.addObject('HyperelasticityFEMForceField', name="FEM", template="Vec3,Tetrahedron", topology="@Tetra_topo", computeForceStrategy="sequenced", computeForceDerivStrategy="sequenced")
       fem.addObject('VonMisesStress', template="Vec3,Tetrahedron", name="stress", topology="@Tetra_topo", stressEvaluator="@material", colorMap="green yellow orange red purple #221C35")
    ```

HyperelasticityFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 -9.81 0">
        <include href="../../../../CantileverBeam_ElementFEMForceField.xml"/>
    
        <CGLinearSolver iterations="250" name="linear_solver" tolerance="1.0e-12" threshold="1.0e-12" />
    
        <Node name="fem">
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" drawTetrahedra="false"/>
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" swapping="true"/>
    
            <StVenantKirchhoffMaterial name="material" youngModulus="2e6" poissonRatio="0.45"/>
            <HyperelasticityFEMForceField name="FEM" template="Vec3,Tetrahedron" topology="@Tetra_topo"
                                          computeForceStrategy="sequenced" computeForceDerivStrategy="sequenced"/>
            <VonMisesStress template="Vec3,Tetrahedron" name="stress" topology="@Tetra_topo" stressEvaluator="@material"
                            colorMap="green yellow orange red purple #221C35"/>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 -9.81 0")

       root.addObject('include', href="../../../../CantileverBeam_ElementFEMForceField.xml")
       root.addObject('CGLinearSolver', iterations="250", name="linear_solver", tolerance="1.0e-12", threshold="1.0e-12")

       fem = root.addChild('fem')

       fem.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
       fem.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       fem.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo", drawTetrahedra="false")
       fem.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo", swapping="true")
       fem.addObject('StVenantKirchhoffMaterial', name="material", youngModulus="2e6", poissonRatio="0.45")
       fem.addObject('HyperelasticityFEMForceField', name="FEM", template="Vec3,Tetrahedron", topology="@Tetra_topo", computeForceStrategy="sequenced", computeForceDerivStrategy="sequenced")
       fem.addObject('VonMisesStress', template="Vec3,Tetrahedron", name="stress", topology="@Tetra_topo", stressEvaluator="@material", colorMap="green yellow orange red purple #221C35")
    ```

