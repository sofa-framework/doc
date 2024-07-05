# ConstantSparsityPatternSystem

Linear system taking advantage of the constant sparsity pattern of the global matrix to speed up the matrix assembly. Do not use if sparsity pattern is not constant (topological changes, ...).


__Templates__:

- `#!c++ CompressedRowSparseMatrixd`

__Target__: `Sofa.Component.LinearSystem`

__namespace__: `#!c++ sofa::component::linearsystem`

__parents__: 

- `#!c++ MatrixLinearSystem`

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
		<td>matrixSize</td>
		<td>
Size of the global matrix
</td>
		<td></td>
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

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|



## Examples

Component/LinearSystem/ConstantSparsityPatternSystem.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.02" gravity="0 -10 0">
        <VisualStyle displayFlags="showBehaviorModels showWireframe" />
    
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [EigenSimplicialLDLT] -->
        <RequiredPlugin name="Sofa.Component.LinearSystem"/> <!-- Needed to use components [ConstantSparsityPatternSystem] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [HexahedronSetGeometryAlgorithms] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <DefaultVisualManagerLoop/>
    
        <Node name="beams">
            <EulerImplicitSolver name="odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <ConstantSparsityPatternSystem template="CompressedRowSparseMatrixd" name="A" printLog="true" checkIndices="false"/>
            <EigenSimplicialLDLT template="CompressedRowSparseMatrixd" linearSystem="@A"/>
    
            <Node name="object_a">
    
                <RegularGridTopology name="grid" nx="1" ny="1" nz="20" xmin="0" xmax="0" ymin="-1.5" ymax="1.5" zmin="0" zmax="19" />
                <MechanicalObject template="Rigid3d" name="DOFs" showObject="true" showObjectScale="1" position="@grid.position"/>
                <FixedProjectiveConstraint indices="0" />
                <Node name="FEM">
                    <RegularGridTopology name="FEM_grid" nx="4" ny="4" nz="20" xmin="-1.5" xmax="1.5" ymin="-1.5" ymax="1.5" zmin="0" zmax="19" />
                    <MechanicalObject template="Vec3d" name="FEM_DOFs_a" position="@FEM_grid.position" printLog="false"/>
                    <HexahedronSetGeometryAlgorithms/>
                    <UniformMass totalMass="320"/>
                    <HexahedronFEMForceField name="FEM_a" youngModulus="10000" poissonRatio="0.45" method="large" printLog="false"/>
    
                    <RigidMapping globalToLocalCoords="true" rigidIndexPerPoint="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19"/>
    
                    <Node name="Visual">
                        <RegularGridTopology name="grid" nx="2" ny="2" nz="20" xmin="-1.5" xmax="1.5" ymin="-1.5" ymax="1.5" zmin="0" zmax="19" computeTriangleList="false" />
                        <OglModel name="visu" lineWidth="5" material="Default Diffuse 0 1 1 1 1 Ambient 1 1 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45"/>
                        <BarycentricMapping input="@../FEM_DOFs_a" output="@visu"/>
                    </Node>
                </Node>
            </Node>
    
            <Node name="object_b">
                <MechanicalObject template="Vec3d" name="FEM_DOFs_b" printLog="false"/>
                <RegularGridTopology name="grid" nx="4" ny="4" nz="20" xmin="-1.5" xmax="1.5" ymin="-9" ymax="-6" zmin="0" zmax="19" />
                <HexahedronSetGeometryAlgorithms/>
                <UniformMass totalMass="320"/>
                <BoxROI template="Vec3d" name="box" box="-1.6 -9.1 -0.1 1.6 -5.1 0.0001"/>
                <FixedProjectiveConstraint indices="@box.indices" />
                <HexahedronFEMForceField name="FEM_b" youngModulus="10000" poissonRatio="0.45" method="large" printLog="false"/>
    
                <Node name="Visual">
                    <RegularGridTopology name="grid" n="@../grid.n" xmin="-1.5" xmax="1.5" ymin="-9" ymax="-6" zmin="0" zmax="19" computeTriangleList="false" />
                    <OglModel name="visu" lineWidth="2" material="Default Diffuse 0 1 1 1 1 Ambient 1 0 1 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45"/>
                    <BarycentricMapping input="@../FEM_DOFs_b" output="@visu"/>
                </Node>
            </Node>
    
            <Node name="object_c">
    
                <RegularGridTopology name="grid" nx="1" ny="1" nz="20" xmin="5" xmax="5" ymin="-1.5" ymax="1.5" zmin="0" zmax="19" />
                <MechanicalObject template="Rigid3d" name="DOFs" showObject="true" showObjectScale="1" position="@grid.position"/>
                <FixedProjectiveConstraint indices="0" />
                <Node name="FEM">
                    <RegularGridTopology name="FEM_grid" nx="4" ny="4" nz="20" xmin="3.5" xmax="6.5" ymin="-1.5" ymax="1.5" zmin="0" zmax="19" />
                    <MechanicalObject template="Vec3d" name="FEM_DOFs_c" position="@FEM_grid.position" printLog="false"/>
                    <HexahedronSetGeometryAlgorithms/>
                    <UniformMass totalMass="320"/>
                    <HexahedronFEMForceField name="FEM_c" youngModulus="10000" poissonRatio="0.45" method="large" printLog="false"/>
    
                    <RigidMapping globalToLocalCoords="true" rigidIndexPerPoint="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19"/>
    
                    <Node name="Visual">
                        <RegularGridTopology name="grid" nx="2" ny="2" nz="20" xmin="3.5" xmax="6.5" ymin="-1.5" ymax="1.5" zmin="0" zmax="19" computeTriangleList="false" />
                        <OglModel name="visu" lineWidth="5" material="Default Diffuse 0 1 1 1 1 Ambient 1 0 0 1 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45"/>
                        <BarycentricMapping input="@../FEM_DOFs_c" output="@visu"/>
                    </Node>
                </Node>
            </Node>
        </Node>
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02", gravity="0 -10 0")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showWireframe")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSystem")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')
        root.addObject('DefaultVisualManagerLoop')

        beams = root.addChild('beams')
        beams.addObject('EulerImplicitSolver', name="odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        beams.addObject('ConstantSparsityPatternSystem', template="CompressedRowSparseMatrixd", name="A", printLog="true", checkIndices="false")
        beams.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrixd", linearSystem="@A")

        object_a = beams.addChild('object_a')
        object_a.addObject('RegularGridTopology', name="grid", nx="1", ny="1", nz="20", xmin="0", xmax="0", ymin="-1.5", ymax="1.5", zmin="0", zmax="19")
        object_a.addObject('MechanicalObject', template="Rigid3d", name="DOFs", showObject="true", showObjectScale="1", position="@grid.position")
        object_a.addObject('FixedProjectiveConstraint', indices="0")

        FEM = object_a.addChild('FEM')
        FEM.addObject('RegularGridTopology', name="FEM_grid", nx="4", ny="4", nz="20", xmin="-1.5", xmax="1.5", ymin="-1.5", ymax="1.5", zmin="0", zmax="19")
        FEM.addObject('MechanicalObject', template="Vec3d", name="FEM_DOFs_a", position="@FEM_grid.position", printLog="false")
        FEM.addObject('HexahedronSetGeometryAlgorithms')
        FEM.addObject('UniformMass', totalMass="320")
        FEM.addObject('HexahedronFEMForceField', name="FEM_a", youngModulus="10000", poissonRatio="0.45", method="large", printLog="false")
        FEM.addObject('RigidMapping', globalToLocalCoords="true", rigidIndexPerPoint="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19")

        Visual = FEM.addChild('Visual')
        Visual.addObject('RegularGridTopology', name="grid", nx="2", ny="2", nz="20", xmin="-1.5", xmax="1.5", ymin="-1.5", ymax="1.5", zmin="0", zmax="19", computeTriangleList="false")
        Visual.addObject('OglModel', name="visu", lineWidth="5", material="Default Diffuse 0 1 1 1 1 Ambient 1 1 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45")
        Visual.addObject('BarycentricMapping', input="@../FEM_DOFs_a", output="@visu")

        object_b = beams.addChild('object_b')
        object_b.addObject('MechanicalObject', template="Vec3d", name="FEM_DOFs_b", printLog="false")
        object_b.addObject('RegularGridTopology', name="grid", nx="4", ny="4", nz="20", xmin="-1.5", xmax="1.5", ymin="-9", ymax="-6", zmin="0", zmax="19")
        object_b.addObject('HexahedronSetGeometryAlgorithms')
        object_b.addObject('UniformMass', totalMass="320")
        object_b.addObject('BoxROI', template="Vec3d", name="box", box="-1.6 -9.1 -0.1 1.6 -5.1 0.0001")
        object_b.addObject('FixedProjectiveConstraint', indices="@box.indices")
        object_b.addObject('HexahedronFEMForceField', name="FEM_b", youngModulus="10000", poissonRatio="0.45", method="large", printLog="false")

        Visual = object_b.addChild('Visual')
        Visual.addObject('RegularGridTopology', name="grid", n="@../grid.n", xmin="-1.5", xmax="1.5", ymin="-9", ymax="-6", zmin="0", zmax="19", computeTriangleList="false")
        Visual.addObject('OglModel', name="visu", lineWidth="2", material="Default Diffuse 0 1 1 1 1 Ambient 1 0 1 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45")
        Visual.addObject('BarycentricMapping', input="@../FEM_DOFs_b", output="@visu")

        object_c = beams.addChild('object_c')
        object_c.addObject('RegularGridTopology', name="grid", nx="1", ny="1", nz="20", xmin="5", xmax="5", ymin="-1.5", ymax="1.5", zmin="0", zmax="19")
        object_c.addObject('MechanicalObject', template="Rigid3d", name="DOFs", showObject="true", showObjectScale="1", position="@grid.position")
        object_c.addObject('FixedProjectiveConstraint', indices="0")

        FEM = object_c.addChild('FEM')
        FEM.addObject('RegularGridTopology', name="FEM_grid", nx="4", ny="4", nz="20", xmin="3.5", xmax="6.5", ymin="-1.5", ymax="1.5", zmin="0", zmax="19")
        FEM.addObject('MechanicalObject', template="Vec3d", name="FEM_DOFs_c", position="@FEM_grid.position", printLog="false")
        FEM.addObject('HexahedronSetGeometryAlgorithms')
        FEM.addObject('UniformMass', totalMass="320")
        FEM.addObject('HexahedronFEMForceField', name="FEM_c", youngModulus="10000", poissonRatio="0.45", method="large", printLog="false")
        FEM.addObject('RigidMapping', globalToLocalCoords="true", rigidIndexPerPoint="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19")

        Visual = FEM.addChild('Visual')
        Visual.addObject('RegularGridTopology', name="grid", nx="2", ny="2", nz="20", xmin="3.5", xmax="6.5", ymin="-1.5", ymax="1.5", zmin="0", zmax="19", computeTriangleList="false")
        Visual.addObject('OglModel', name="visu", lineWidth="5", material="Default Diffuse 0 1 1 1 1 Ambient 1 0 0 1 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45")
        Visual.addObject('BarycentricMapping', input="@../FEM_DOFs_c", output="@visu")
    ```

