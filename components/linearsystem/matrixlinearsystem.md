<!-- generate_doc -->
# MatrixLinearSystem

Linear system dedicated to a Band Tri Diagonal matrix.
Linear system.


Templates:

- BlockDiagonalMatrixMat3x3d
- CompressedRowSparseMatrixMat2x2d
- CompressedRowSparseMatrixMat3x3d
- CompressedRowSparseMatrixMat4x4d
- CompressedRowSparseMatrixMat6x6d
- CompressedRowSparseMatrixMat8x8d
- CompressedRowSparseMatrixd
- DiagonalMatrix
- FullMatrix
- RotationMatrixd
- SparseMatrix

__Target__: Sofa.Component.LinearSystem

__namespace__: sofa::component::linearsystem

__parents__:

- TypedMatrixLinearSystem

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
		<td>matrixSize</td>
		<td>
Size of the global matrix
		</td>
		<td></td>
	</tr>
	<tr>
		<td>enableAssembly</td>
		<td>
Allows to assemble the system matrix
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>factorizationInvalidation</td>
		<td>
Internal Data indicating a change in the matrix
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>assembleStiffness</td>
		<td>
If true, the stiffness is added to the global matrix
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>assembleMass</td>
		<td>
If true, the mass is added to the global matrix
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>assembleDamping</td>
		<td>
If true, the damping is added to the global matrix
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>assembleGeometricStiffness</td>
		<td>
If true, the geometric stiffness of mappings is added to the global matrix
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>applyProjectiveConstraints</td>
		<td>
If true, projective constraints are applied on the global matrix
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>applyMappedComponents</td>
		<td>
If true, mapped components contribute to the global matrix
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>checkIndices</td>
		<td>
If true, indices are verified before being added in to the global matrix, favoring security over speed
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>parallelAssemblyIndependentMatrices</td>
		<td>
If true, independent matrices (global matrix vs mapped matrices) are assembled in parallel
		</td>
		<td>0</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|

## Examples 

MatrixLinearSystem.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.02" gravity="0 -10 0">
    
        <Node name="plugins">
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [EigenSimplicialLDLT] -->
            <RequiredPlugin name="Sofa.Component.LinearSystem"/> <!-- Needed to use components [CompositeLinearSystem MatrixLinearSystem MatrixProjectionMethod] -->
            <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping IdentityMapping SubsetMapping] -->
            <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [MeshMatrixMass] -->
            <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [ConstantForceField] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [SpringForceField] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [HexahedronSetGeometryAlgorithms] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
            <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
            <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
            <RequiredPlugin name="SofaMatrix.Qt"/> <!-- Needed to use components [GlobalSystemMatrixImage] -->
    
        </Node>
    
        <VisualStyle displayFlags="showBehaviorModels showWireframe" />
    
        <DefaultAnimationLoop/>
        <DefaultVisualManagerLoop/>
    
        <Node name="rigidSections">
            <EulerImplicitSolver name="odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
    
            <Node name="matrices">
                <MatrixLinearSystem template="CompressedRowSparseMatrixd" name="system" checkIndices="true" printLog="true"/>
                <MatrixLinearSystem template="CompressedRowSparseMatrixd" name="GS" assembleStiffness="false" assembleMass="false" assembleDamping="false" assembleGeometricStiffness="true" applyProjectiveConstraints="false"/>
                <GlobalSystemMatrixImage name="imageA" linearSystem="@system"/>
                <GlobalSystemMatrixImage name="imageGS" linearSystem="@GS"/>
            </Node>
    
            <CompositeLinearSystem template="CompressedRowSparseMatrixd" name="solverSystem" linearSystems="@matrices/system @matrices/GS" solverLinearSystem="@matrices/system"/>
            <EigenSimplicialLDLT template="CompressedRowSparseMatrixd" linearSystem="@solverSystem"/>
    
            <Node name="red">
    
                <RegularGridTopology name="grid" nx="1" ny="1" nz="20" xmin="0" xmax="0" ymin="-1.5" ymax="1.5" zmin="0" zmax="19" />
                <MechanicalObject template="Rigid3d" name="DOFs" showObject="true" showObjectScale="1" position="@grid.position"/>
                <FixedProjectiveConstraint indices="0" />
                <Node name="FEM">
                    <RegularGridTopology name="FEM_grid" nx="4" ny="4" nz="20" xmin="-1.5" xmax="1.5" ymin="-1.5" ymax="1.5" zmin="0" zmax="19" />
                    <MechanicalObject template="Vec3d" name="DOFs" position="@FEM_grid.position" printLog="false"/>
                    <HexahedronSetGeometryAlgorithms/>
                    <MeshMatrixMass totalMass="320"/>
                    <HexahedronFEMForceField name="FEM_a" youngModulus="10000" poissonRatio="0.45" method="large" printLog="false"/>
    
                    <RigidMapping geometricStiffness="2" globalToLocalCoords="true" rigidIndexPerPoint="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19"/>
    
                    <Node name="Visual">
                        <RegularGridTopology name="grid" nx="2" ny="2" nz="20" xmin="-1.5" xmax="1.5" ymin="-1.5" ymax="1.5" zmin="0" zmax="19" computeTriangleList="false" />
                        <OglModel name="visu" lineWidth="5" material="Default Diffuse 0 1 1 1 1 Ambient 1 1 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45"/>
                        <BarycentricMapping input="@../DOFs" output="@visu"/>
                    </Node>
                </Node>
            </Node>
    
            <Node name="green">
                <VisualStyle displayFlags="showInteractionForceFields" />
                <MechanicalObject template="Vec3d" name="DOFs" printLog="false"/>
                <RegularGridTopology name="grid" nx="4" ny="4" nz="20" xmin="-1.5" xmax="1.5" ymin="-9" ymax="-6" zmin="0" zmax="19" />
                <HexahedronSetGeometryAlgorithms/>
                <MeshMatrixMass totalMass="320"/>
                <BoxROI template="Vec3d" name="box" box="-1.6 -9.1 -0.1 1.6 -5.1 0.0001"/>
                <FixedProjectiveConstraint indices="@box.indices" />
                <HexahedronFEMForceField name="FEM_b" youngModulus="10000" poissonRatio="0.45" method="large" printLog="false"/>
    
                <Node name="a">
                    <BoxROI name="box" position="@../DOFs.position" box="1.4 -6.1 18.9 1.6 -5.9 19.1" drawBoxes="true" doUpdate="false"/>
                    <MechanicalObject template="Vec3d" name="DOFs"/>
                    <SubsetMapping input="@../DOFs" output="@DOFs" indices="@box.indices"/>
                </Node>
                <Node name="b">
                    <BoxROI name="box" position="@../DOFs.position" box="1.4 -6.1 1.9 1.6 -5.9 2.1" drawBoxes="true" doUpdate="false"/>
                    <MechanicalObject template="Vec3d" name="DOFs"/>
                    <SubsetMapping input="@../DOFs" output="@DOFs" indices="@box.indices"/>
                </Node>
                <MatrixProjectionMethod areJacobiansConstant="true" mechanicalStates="@/rigidSections/green/a/DOFs @/rigidSections/green/a/DOFs"/>
                <MatrixProjectionMethod areJacobiansConstant="true" mechanicalStates="@/rigidSections/green/a/DOFs @/rigidSections/green/b/DOFs"/>
                <MatrixProjectionMethod areJacobiansConstant="true" mechanicalStates="@/rigidSections/green/b/DOFs @/rigidSections/green/a/DOFs"/>
                <MatrixProjectionMethod areJacobiansConstant="true" mechanicalStates="@/rigidSections/green/b/DOFs @/rigidSections/green/b/DOFs"/>
                <SpringForceField object1="@a/DOFs" object2="@b/DOFs" spring="0 0 100 1 1" showArrowSize="0.05" drawMode="2"/>
    
                <Node name="Visual">
                    <RegularGridTopology name="grid" n="@../grid.n" xmin="-1.5" xmax="1.5" ymin="-9" ymax="-6" zmin="0" zmax="19" computeTriangleList="false" />
                    <OglModel name="visu" lineWidth="2" material="Default Diffuse 0 1 1 1 1 Ambient 1 0 1 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45"/>
                    <BarycentricMapping input="@../DOFs" output="@visu"/>
                </Node>
            </Node>
    
            <Node name="blue">
    
                <RegularGridTopology name="grid" nx="1" ny="1" nz="20" xmin="5" xmax="5" ymin="-1.5" ymax="1.5" zmin="0" zmax="19" />
                <MechanicalObject template="Rigid3d" name="DOFs" showObject="true" showObjectScale="1" position="@grid.position"/>
                <FixedProjectiveConstraint indices="0" />
    
                <Node name="intermediateMapping"> <!-- this mapping is introduced just to verify that geometric stiffness is well projected -->
    
                    <MechanicalObject template="Rigid3d" name="DOFs" showObject="false"/>
                    <ConstantForceField forces="0 0 0.0005 0 0 0"/>
                    <IdentityMapping input="@../DOFs" output="@DOFs"/>
    
                    <Node name="FEM">
                        <RegularGridTopology name="FEM_grid" nx="4" ny="4" nz="20" xmin="3.5" xmax="6.5" ymin="-1.5" ymax="1.5" zmin="0" zmax="19" />
                        <MechanicalObject template="Vec3d" name="DOFs" position="@FEM_grid.position" printLog="false"/>
                        <HexahedronSetGeometryAlgorithms/>
                        <MeshMatrixMass totalMass="320"/>
                        <HexahedronFEMForceField name="FEM_c" youngModulus="10000" poissonRatio="0.45" method="large" printLog="false"/>
    
                        <RigidMapping geometricStiffness="2" globalToLocalCoords="true" rigidIndexPerPoint="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19"/>
    
                        <Node name="Visual">
                            <RegularGridTopology name="grid" nx="2" ny="2" nz="20" xmin="3.5" xmax="6.5" ymin="-1.5" ymax="1.5" zmin="0" zmax="19" computeTriangleList="false" />
                            <OglModel name="visu" lineWidth="5" material="Default Diffuse 0 1 1 1 1 Ambient 1 0 0 1 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45"/>
                            <BarycentricMapping input="@../DOFs" output="@visu"/>
                        </Node>
                    </Node>
                </Node>
            </Node>
    
            <Node name="spring">
                <VisualStyle displayFlags="showInteractionForceFields" />
    
                <Node name="nonMappedDOFsSpring">
                    <SpringForceField object1="@red/DOFs" object2="@blue/DOFs" spring="19 19 50 1 1" showArrowSize="0.05" drawMode="2"/>
                </Node>
    
                <Node name="springBetweenMappedAndNonMapped">
                    <BoxROI position="@red/FEM/DOFs.position" box="-1.6 -1.6 18.9 -1.4 -1.4 19.1" drawBoxes="true"/>
                    <BoxROI position="@green/DOFs.position" box="-1.6 -6.1 18.9 -1.4 -5.9 19.1" drawBoxes="true"/>
                    <SpringForceField object1="@red/FEM/DOFs" object2="@green/DOFs" spring="304 316 100 1 1" showArrowSize="0.05" drawMode="2"/>
                </Node>
            </Node>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02", gravity="0 -10 0")

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSystem")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       plugins.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       plugins.addObject('RequiredPlugin', name="SofaMatrix.Qt")

       root.addObject('VisualStyle', displayFlags="showBehaviorModels showWireframe")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('DefaultVisualManagerLoop', )

       rigid_sections = root.addChild('rigidSections')

       rigid_sections.addObject('EulerImplicitSolver', name="odesolver", rayleighStiffness="0.1", rayleighMass="0.1")

       matrices = rigidSections.addChild('matrices')

       matrices.addObject('MatrixLinearSystem', template="CompressedRowSparseMatrixd", name="system", checkIndices="true", printLog="true")
       matrices.addObject('MatrixLinearSystem', template="CompressedRowSparseMatrixd", name="GS", assembleStiffness="false", assembleMass="false", assembleDamping="false", assembleGeometricStiffness="true", applyProjectiveConstraints="false")
       matrices.addObject('GlobalSystemMatrixImage', name="imageA", linearSystem="@system")
       matrices.addObject('GlobalSystemMatrixImage', name="imageGS", linearSystem="@GS")

       rigid_sections.addObject('CompositeLinearSystem', template="CompressedRowSparseMatrixd", name="solverSystem", linearSystems="@matrices/system @matrices/GS", solverLinearSystem="@matrices/system")
       rigid_sections.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrixd", linearSystem="@solverSystem")

       red = rigidSections.addChild('red')

       red.addObject('RegularGridTopology', name="grid", nx="1", ny="1", nz="20", xmin="0", xmax="0", ymin="-1.5", ymax="1.5", zmin="0", zmax="19")
       red.addObject('MechanicalObject', template="Rigid3d", name="DOFs", showObject="true", showObjectScale="1", position="@grid.position")
       red.addObject('FixedProjectiveConstraint', indices="0")

       fem = red.addChild('FEM')

       fem.addObject('RegularGridTopology', name="FEM_grid", nx="4", ny="4", nz="20", xmin="-1.5", xmax="1.5", ymin="-1.5", ymax="1.5", zmin="0", zmax="19")
       fem.addObject('MechanicalObject', template="Vec3d", name="DOFs", position="@FEM_grid.position", printLog="false")
       fem.addObject('HexahedronSetGeometryAlgorithms', )
       fem.addObject('MeshMatrixMass', totalMass="320")
       fem.addObject('HexahedronFEMForceField', name="FEM_a", youngModulus="10000", poissonRatio="0.45", method="large", printLog="false")
       fem.addObject('RigidMapping', geometricStiffness="2", globalToLocalCoords="true", rigidIndexPerPoint="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19")

       visual = FEM.addChild('Visual')

       visual.addObject('RegularGridTopology', name="grid", nx="2", ny="2", nz="20", xmin="-1.5", xmax="1.5", ymin="-1.5", ymax="1.5", zmin="0", zmax="19", computeTriangleList="false")
       visual.addObject('OglModel', name="visu", lineWidth="5", material="Default Diffuse 0 1 1 1 1 Ambient 1 1 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45")
       visual.addObject('BarycentricMapping', input="@../DOFs", output="@visu")

       green = rigidSections.addChild('green')

       green.addObject('VisualStyle', displayFlags="showInteractionForceFields")
       green.addObject('MechanicalObject', template="Vec3d", name="DOFs", printLog="false")
       green.addObject('RegularGridTopology', name="grid", nx="4", ny="4", nz="20", xmin="-1.5", xmax="1.5", ymin="-9", ymax="-6", zmin="0", zmax="19")
       green.addObject('HexahedronSetGeometryAlgorithms', )
       green.addObject('MeshMatrixMass', totalMass="320")
       green.addObject('BoxROI', template="Vec3d", name="box", box="-1.6 -9.1 -0.1 1.6 -5.1 0.0001")
       green.addObject('FixedProjectiveConstraint', indices="@box.indices")
       green.addObject('HexahedronFEMForceField', name="FEM_b", youngModulus="10000", poissonRatio="0.45", method="large", printLog="false")

       a = green.addChild('a')

       a.addObject('BoxROI', name="box", position="@../DOFs.position", box="1.4 -6.1 18.9 1.6 -5.9 19.1", drawBoxes="true", doUpdate="false")
       a.addObject('MechanicalObject', template="Vec3d", name="DOFs")
       a.addObject('SubsetMapping', input="@../DOFs", output="@DOFs", indices="@box.indices")

       b = green.addChild('b')

       b.addObject('BoxROI', name="box", position="@../DOFs.position", box="1.4 -6.1 1.9 1.6 -5.9 2.1", drawBoxes="true", doUpdate="false")
       b.addObject('MechanicalObject', template="Vec3d", name="DOFs")
       b.addObject('SubsetMapping', input="@../DOFs", output="@DOFs", indices="@box.indices")

       green.addObject('MatrixProjectionMethod', areJacobiansConstant="true", mechanicalStates="@/rigidSections/green/a/DOFs @/rigidSections/green/a/DOFs")
       green.addObject('MatrixProjectionMethod', areJacobiansConstant="true", mechanicalStates="@/rigidSections/green/a/DOFs @/rigidSections/green/b/DOFs")
       green.addObject('MatrixProjectionMethod', areJacobiansConstant="true", mechanicalStates="@/rigidSections/green/b/DOFs @/rigidSections/green/a/DOFs")
       green.addObject('MatrixProjectionMethod', areJacobiansConstant="true", mechanicalStates="@/rigidSections/green/b/DOFs @/rigidSections/green/b/DOFs")
       green.addObject('SpringForceField', object1="@a/DOFs", object2="@b/DOFs", spring="0 0 100 1 1", showArrowSize="0.05", drawMode="2")

       visual = green.addChild('Visual')

       visual.addObject('RegularGridTopology', name="grid", n="@../grid.n", xmin="-1.5", xmax="1.5", ymin="-9", ymax="-6", zmin="0", zmax="19", computeTriangleList="false")
       visual.addObject('OglModel', name="visu", lineWidth="2", material="Default Diffuse 0 1 1 1 1 Ambient 1 0 1 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45")
       visual.addObject('BarycentricMapping', input="@../DOFs", output="@visu")

       blue = rigidSections.addChild('blue')

       blue.addObject('RegularGridTopology', name="grid", nx="1", ny="1", nz="20", xmin="5", xmax="5", ymin="-1.5", ymax="1.5", zmin="0", zmax="19")
       blue.addObject('MechanicalObject', template="Rigid3d", name="DOFs", showObject="true", showObjectScale="1", position="@grid.position")
       blue.addObject('FixedProjectiveConstraint', indices="0")

       intermediate_mapping = blue.addChild('intermediateMapping')

       intermediate_mapping.addObject('MechanicalObject', template="Rigid3d", name="DOFs", showObject="false")
       intermediate_mapping.addObject('ConstantForceField', forces="0 0 0.0005 0 0 0")
       intermediate_mapping.addObject('IdentityMapping', input="@../DOFs", output="@DOFs")

       fem = intermediateMapping.addChild('FEM')

       fem.addObject('RegularGridTopology', name="FEM_grid", nx="4", ny="4", nz="20", xmin="3.5", xmax="6.5", ymin="-1.5", ymax="1.5", zmin="0", zmax="19")
       fem.addObject('MechanicalObject', template="Vec3d", name="DOFs", position="@FEM_grid.position", printLog="false")
       fem.addObject('HexahedronSetGeometryAlgorithms', )
       fem.addObject('MeshMatrixMass', totalMass="320")
       fem.addObject('HexahedronFEMForceField', name="FEM_c", youngModulus="10000", poissonRatio="0.45", method="large", printLog="false")
       fem.addObject('RigidMapping', geometricStiffness="2", globalToLocalCoords="true", rigidIndexPerPoint="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19")

       visual = FEM.addChild('Visual')

       visual.addObject('RegularGridTopology', name="grid", nx="2", ny="2", nz="20", xmin="3.5", xmax="6.5", ymin="-1.5", ymax="1.5", zmin="0", zmax="19", computeTriangleList="false")
       visual.addObject('OglModel', name="visu", lineWidth="5", material="Default Diffuse 0 1 1 1 1 Ambient 1 0 0 1 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45")
       visual.addObject('BarycentricMapping', input="@../DOFs", output="@visu")

       spring = rigidSections.addChild('spring')

       spring.addObject('VisualStyle', displayFlags="showInteractionForceFields")

       non_mapped_do_fs_spring = spring.addChild('nonMappedDOFsSpring')

       non_mapped_do_fs_spring.addObject('SpringForceField', object1="@red/DOFs", object2="@blue/DOFs", spring="19 19 50 1 1", showArrowSize="0.05", drawMode="2")

       spring_between_mapped_and_non_mapped = spring.addChild('springBetweenMappedAndNonMapped')

       spring_between_mapped_and_non_mapped.addObject('BoxROI', position="@red/FEM/DOFs.position", box="-1.6 -1.6 18.9 -1.4 -1.4 19.1", drawBoxes="true")
       spring_between_mapped_and_non_mapped.addObject('BoxROI', position="@green/DOFs.position", box="-1.6 -6.1 18.9 -1.4 -5.9 19.1", drawBoxes="true")
       spring_between_mapped_and_non_mapped.addObject('SpringForceField', object1="@red/FEM/DOFs", object2="@green/DOFs", spring="304 316 100 1 1", showArrowSize="0.05", drawMode="2")
    ```

