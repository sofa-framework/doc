<!-- generate_doc -->
# GlobalSystemMatrixImage

View the global linear system matrix as a binary image.


__Target__: SofaMatrix

__namespace__: sofa::component::linearsolver

__parents__:

- BaseObject

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
		<td colspan="3">Image</td>
	</tr>
	<tr>
		<td>bitmap</td>
		<td>
Visualization of the representation of the matrix as a binary image. White pixels are zeros, black pixels are non-zeros.
		</td>
		<td>invalid matrix</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|linearSystem|Link to the linear system containing a matrix|BaseMatrixLinearSystem|

## Examples 

GlobalSystemMatrixImage.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.02" gravity="0 -10 0">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [SparseLDLSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="SofaMatrix"/> <!-- Needed to use components [GlobalSystemMatrixImage] -->
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
    
        <!-- Node containing 2 objects under a single linear solver -->
        <Node name="M3">
            <EulerImplicitSolver name="odesolver"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <MatrixLinearSystem template="CompressedRowSparseMatrixMat3x3d"/>
            <SparseLDLSolver printLog="false" template="CompressedRowSparseMatrixMat3x3d"/>
            <GlobalSystemMatrixImage/>
    
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
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02", gravity="0 -10 0")

       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="SofaMatrix")
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")

       m3 = root.addChild('M3')

       m3.addObject('EulerImplicitSolver', name="odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
       m3.addObject('MatrixLinearSystem', template="CompressedRowSparseMatrixMat3x3d")
       m3.addObject('SparseLDLSolver', printLog="false", template="CompressedRowSparseMatrixMat3x3d")
       m3.addObject('GlobalSystemMatrixImage', )

       n1 = M3.addChild('N1')

       n1.addObject('MechanicalObject', )
       n1.addObject('UniformMass', vertexMass="1")
       n1.addObject('RegularGridTopology', nx="4", ny="4", nz="10", xmin="-3", xmax="0", ymin="0", ymax="3", zmin="0", zmax="9")
       n1.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15")
       n1.addObject('HexahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3", method="large")

       n2 = M3.addChild('N2')

       n2.addObject('MechanicalObject', )
       n2.addObject('UniformMass', vertexMass="1")
       n2.addObject('RegularGridTopology', nx="4", ny="4", nz="10", xmin="0", xmax="3", ymin="0", ymax="3", zmin="0", zmax="9")
       n2.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15")
       n2.addObject('HexahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3", method="large")
    ```

