<!-- generate_doc -->
# TetrahedronLinearSmallStrainFEMForceField

Hooke's law on linear tetrahedra assuming small strain


## Vec3d

Templates:

- Vec3d

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

TetrahedronLinearSmallStrainFEMForceField.scn

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
    
            <TetrahedronLinearSmallStrainFEMForceField name="FEM" youngModulus="2e6" poissonRatio="0.45" topology="@Tetra_topo"
                                                       computeForceStrategy="sequenced" computeForceDerivStrategy="sequenced"/>
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
       fem.addObject('TetrahedronLinearSmallStrainFEMForceField', name="FEM", youngModulus="2e6", poissonRatio="0.45", topology="@Tetra_topo", computeForceStrategy="sequenced", computeForceDerivStrategy="sequenced")
    ```

TetrahedronLinearSmallStrainFEMForceField.scn

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
    
            <TetrahedronLinearSmallStrainFEMForceField name="FEM" youngModulus="2e6" poissonRatio="0.45" topology="@Tetra_topo"
                                                       computeForceStrategy="sequenced" computeForceDerivStrategy="sequenced"/>
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
       fem.addObject('TetrahedronLinearSmallStrainFEMForceField', name="FEM", youngModulus="2e6", poissonRatio="0.45", topology="@Tetra_topo", computeForceStrategy="sequenced", computeForceDerivStrategy="sequenced")
    ```

TetrahedronLinearSmallStrainFEMForceField.scn

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
    
            <TetrahedronLinearSmallStrainFEMForceField name="FEM" youngModulus="2e6" poissonRatio="0.45" topology="@Tetra_topo"
                                                       computeForceStrategy="parallel" computeForceDerivStrategy="parallel"/>
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
       fem.addObject('TetrahedronLinearSmallStrainFEMForceField', name="FEM", youngModulus="2e6", poissonRatio="0.45", topology="@Tetra_topo", computeForceStrategy="parallel", computeForceDerivStrategy="parallel")
    ```

TetrahedronLinearSmallStrainFEMForceField.scn

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
    
            <TetrahedronLinearSmallStrainFEMForceField name="FEM" youngModulus="2e6" poissonRatio="0.45" topology="@Tetra_topo"
                                                  computeForceStrategy="parallel" computeForceDerivStrategy="parallel"/>
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
       fem.addObject('TetrahedronLinearSmallStrainFEMForceField', name="FEM", youngModulus="2e6", poissonRatio="0.45", topology="@Tetra_topo", computeForceStrategy="parallel", computeForceDerivStrategy="parallel")
    ```

