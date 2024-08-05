# GlobalSystemMatrixExporter

Export the global system matrix from a linear solver.


__Target__: `SofaMatrix`

__namespace__: `#!c++ sofa::component::linearsystem`

__parents__: 

- `#!c++ BaseSimulationExporter`

__categories__: 

- _Miscellaneous

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
		<td>filename</td>
		<td>
Path or filename where to export the data.  If missing the name of the component is used.
</td>
		<td></td>
	</tr>
	<tr>
		<td>exportEveryNumberOfSteps</td>
		<td>
export file only at specified number of steps (0=disable, default=0)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>exportAtBegin</td>
		<td>
export file before the simulation starts, once the simulation is initialized (default=false)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>exportAtEnd</td>
		<td>
export file when the simulation is over and cleanup is called, i.e. just before deleting the simulation (default=false)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>enable</td>
		<td>
Enable or disable the component. (default=true)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>format</td>
		<td>
File format
</td>
		<td>txt</td>
	</tr>
	<tr>
		<td>precision</td>
		<td>
Number of digits used to write an entry of the matrix, default is 6
</td>
		<td>6</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|linearSystem|Linear system used to export its matrix|



## Examples

SofaMatrix/share/sofa/examples/SofaMatrix/GlobalSystemMatrixExporter.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.02" gravity="0 -10 0">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [SparseLDLSolver] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="SofaMatrix"/> <!-- Needed to use components [GlobalSystemMatrixExporter] -->
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
    
        <Node name="M1">
            <EulerImplicitSolver name="odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <MatrixLinearSystem template="CompressedRowSparseMatrixMat3x3d"/>
            <SparseLDLSolver printLog="false" template="CompressedRowSparseMatrixMat3x3d"/>
            <GlobalSystemMatrixExporter exportEveryNumberOfSteps="1" filename="global_matrix_ldl" printLog="true" format="txt" precision="12"/>
            <MechanicalObject />
            <UniformMass vertexMass="1"/>
            <RegularGridTopology nx="4" ny="4" nz="10" xmin="-9" xmax="-6" ymin="0" ymax="3" zmin="0" zmax="9" />
            <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15" />
            <HexahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" method="large" />
        </Node>
    
        <Node name="M2">
            <EulerImplicitSolver name="odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver template="GraphScattered" iterations="25" tolerance="1e-5" threshold="1e-5"/>
            <!-- The following exporter will warn that the matrix cannot be exported because the matrix is not assembled -->
            <GlobalSystemMatrixExporter exportEveryNumberOfSteps="1" filename="global_matrix_cg" printLog="true"/>
            <MechanicalObject />
            <UniformMass vertexMass="1"/>
            <RegularGridTopology nx="4" ny="4" nz="10" xmin="-6" xmax="-3" ymin="0" ymax="3" zmin="0" zmax="9" />
            <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15" />
            <HexahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" method="large" />
        </Node>
    
        <!-- Node containing 2 objects under a single linear solver -->
        <Node name="M3">
            <EulerImplicitSolver name="odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <MatrixLinearSystem template="CompressedRowSparseMatrixMat3x3d"/>
            <SparseLDLSolver printLog="false" template="CompressedRowSparseMatrixMat3x3d"/>
            <GlobalSystemMatrixExporter exportEveryNumberOfSteps="1" filename="global_matrix_ldl_2objects" printLog="true" format="jpg"/>
    
            <Node name="N1">
                <MechanicalObject />
                <UniformMass vertexMass="1"/>
                <RegularGridTopology nx="4" ny="4" nz="10" xmin="-3" xmax="0" ymin="0" ymax="3" zmin="0" zmax="9" />
                <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15" />
                <HexahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" method="large" />
            </Node>
            <Node name="N2">
                <MechanicalObject />
                <UniformMass vertexMass="1"/>
                <RegularGridTopology nx="4" ny="4" nz="10" xmin="0" xmax="3" ymin="0" ymax="3" zmin="0" zmax="9" />
                <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15" />
                <HexahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" method="large" />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02", gravity="0 -10 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="SofaMatrix")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")

        M1 = root.addChild('M1')
        M1.addObject('EulerImplicitSolver', name="odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        M1.addObject('MatrixLinearSystem', template="CompressedRowSparseMatrixMat3x3d")
        M1.addObject('SparseLDLSolver', printLog="false", template="CompressedRowSparseMatrixMat3x3d")
        M1.addObject('GlobalSystemMatrixExporter', exportEveryNumberOfSteps="1", filename="global_matrix_ldl", printLog="true", format="txt", precision="12")
        M1.addObject('MechanicalObject')
        M1.addObject('UniformMass', vertexMass="1")
        M1.addObject('RegularGridTopology', nx="4", ny="4", nz="10", xmin="-9", xmax="-6", ymin="0", ymax="3", zmin="0", zmax="9")
        M1.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15")
        M1.addObject('HexahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3", method="large")

        M2 = root.addChild('M2')
        M2.addObject('EulerImplicitSolver', name="odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        M2.addObject('CGLinearSolver', template="GraphScattered", iterations="25", tolerance="1e-5", threshold="1e-5")
        M2.addObject('GlobalSystemMatrixExporter', exportEveryNumberOfSteps="1", filename="global_matrix_cg", printLog="true")
        M2.addObject('MechanicalObject')
        M2.addObject('UniformMass', vertexMass="1")
        M2.addObject('RegularGridTopology', nx="4", ny="4", nz="10", xmin="-6", xmax="-3", ymin="0", ymax="3", zmin="0", zmax="9")
        M2.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15")
        M2.addObject('HexahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3", method="large")

        M3 = root.addChild('M3')
        M3.addObject('EulerImplicitSolver', name="odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        M3.addObject('MatrixLinearSystem', template="CompressedRowSparseMatrixMat3x3d")
        M3.addObject('SparseLDLSolver', printLog="false", template="CompressedRowSparseMatrixMat3x3d")
        M3.addObject('GlobalSystemMatrixExporter', exportEveryNumberOfSteps="1", filename="global_matrix_ldl_2objects", printLog="true", format="jpg")

        N1 = M3.addChild('N1')
        N1.addObject('MechanicalObject')
        N1.addObject('UniformMass', vertexMass="1")
        N1.addObject('RegularGridTopology', nx="4", ny="4", nz="10", xmin="-3", xmax="0", ymin="0", ymax="3", zmin="0", zmax="9")
        N1.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15")
        N1.addObject('HexahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3", method="large")

        N2 = M3.addChild('N2')
        N2.addObject('MechanicalObject')
        N2.addObject('UniformMass', vertexMass="1")
        N2.addObject('RegularGridTopology', nx="4", ny="4", nz="10", xmin="0", xmax="3", ymin="0", ymax="3", zmin="0", zmax="9")
        N2.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15")
        N2.addObject('HexahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3", method="large")
    ```

