<!-- generate_doc -->
# FastTetrahedralCorotationalForceField

Fast Corotational Tetrahedral Mesh.


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.SolidMechanics.FEM.Elastic

__namespace__: sofa::component::solidmechanics::fem::elastic

__parents__:

- BaseLinearElasticityFEMForceField

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
		<td>pointInfo</td>
		<td>
Internal point data
		</td>
		<td></td>
	</tr>
	<tr>
		<td>edgeInfo</td>
		<td>
Internal edge data
		</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedronInfo</td>
		<td>
Internal tetrahedron data
		</td>
		<td></td>
	</tr>
	<tr>
		<td>method</td>
		<td>
 method for rotation computation :"qr" (by QR) or "polar" or "polar2" or "none" (Linear elastic) 
		</td>
		<td>qr</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawing</td>
		<td>
 draw the forcefield if true
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>drawColor1</td>
		<td>
 draw color for faces 1
		</td>
		<td>0 0 1 1</td>
	</tr>
	<tr>
		<td>drawColor2</td>
		<td>
 draw color for faces 2
		</td>
		<td>0 0.5 1 1</td>
	</tr>
	<tr>
		<td>drawColor3</td>
		<td>
 draw color for faces 3
		</td>
		<td>0 1 1 1</td>
	</tr>
	<tr>
		<td>drawColor4</td>
		<td>
 draw color for faces 4
		</td>
		<td>0.5 1 1 1</td>
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

## Examples 

FastTetrahedralCorotationalForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 -9 0">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [EigenSimplicialLDLT] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [FastTetrahedralCorotationalForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <DefaultAnimationLoop parallelODESolving="true"/>
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
    
        <Node name="BeamFEM_SMALL">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <EigenSimplicialLDLT template="CompressedRowSparseMatrixMat3x3"/>
    
            <RegularGridTopology name="grid" min="-5 -5 0" max="5 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3" />
    
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" />
    
            <DiagonalMass massDensity="0.2" />
            <FastTetrahedralCorotationalForceField name="FEM" youngModulus="1000" poissonRatio="0.4" method="small"/>
    
            <BoxROI template="Vec3" name="box_roi" box="-6 -6 -1 50 6 0.1" drawBoxes="1" />
            <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
        </Node>
    
    
        <Node name="BeamFEM_LARGE">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <EigenSimplicialLDLT template="CompressedRowSparseMatrixMat3x3"/>
    
            <RegularGridTopology name="grid" min="-5 -5 0" max="5 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3" translation="11 0 0"/>
    
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" />
    
            <DiagonalMass massDensity="0.2" />
            <FastTetrahedralCorotationalForceField name="FEM" youngModulus="1000" poissonRatio="0.4" method="large"/>
    
            <BoxROI template="Vec3" name="box_roi" box="-6 -6 -1 50 6 0.1" drawBoxes="1" />
            <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
        </Node>
    
        <Node name="BeamFEM_POLAR">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <EigenSimplicialLDLT template="CompressedRowSparseMatrixMat3x3"/>
    
            <RegularGridTopology name="grid" min="-5 -5 0" max="5 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3" translation="22 0 0"/>
    
            <TetrahedronSetTopologyContainer name="Tetra_topo" />
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" />
    
            <DiagonalMass massDensity="0.2" />
            <FastTetrahedralCorotationalForceField name="FEM" youngModulus="1000" poissonRatio="0.4" method="polar"/>
    
            <BoxROI template="Vec3" name="box_roi" box="-6 -6 -1 50 6 0.1" drawBoxes="1" />
            <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
        </Node>
    
        <Node name="BeamFEM_polar2">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <EigenSimplicialLDLT template="CompressedRowSparseMatrixMat3x3"/>
    
            <RegularGridTopology name="grid" min="-5 -5 0" max="5 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3" translation="33 0 0"/>
    
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" />
    
            <DiagonalMass massDensity="0.2" />
            <FastTetrahedralCorotationalForceField name="FEM" youngModulus="1000" poissonRatio="0.4" method="polar2"/>
    
            <BoxROI template="Vec3" name="box_roi" box="-6 -6 -1 50 6 0.1" drawBoxes="1" />
            <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 -9 0")

       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('DefaultAnimationLoop', parallelODESolving="true")
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")

       beam_fem__small = root.addChild('BeamFEM_SMALL')

       beam_fem__small.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       beam_fem__small.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrixMat3x3")
       beam_fem__small.addObject('RegularGridTopology', name="grid", min="-5 -5 0", max="5 5 40", n="5 5 20")
       beam_fem__small.addObject('MechanicalObject', template="Vec3")
       beam_fem__small.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
       beam_fem__small.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       beam_fem__small.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       beam_fem__small.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo")
       beam_fem__small.addObject('DiagonalMass', massDensity="0.2")
       beam_fem__small.addObject('FastTetrahedralCorotationalForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", method="small")
       beam_fem__small.addObject('BoxROI', template="Vec3", name="box_roi", box="-6 -6 -1 50 6 0.1", drawBoxes="1")
       beam_fem__small.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")

       beam_fem__large = root.addChild('BeamFEM_LARGE')

       beam_fem__large.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       beam_fem__large.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrixMat3x3")
       beam_fem__large.addObject('RegularGridTopology', name="grid", min="-5 -5 0", max="5 5 40", n="5 5 20")
       beam_fem__large.addObject('MechanicalObject', template="Vec3", translation="11 0 0")
       beam_fem__large.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
       beam_fem__large.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       beam_fem__large.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       beam_fem__large.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo")
       beam_fem__large.addObject('DiagonalMass', massDensity="0.2")
       beam_fem__large.addObject('FastTetrahedralCorotationalForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", method="large")
       beam_fem__large.addObject('BoxROI', template="Vec3", name="box_roi", box="-6 -6 -1 50 6 0.1", drawBoxes="1")
       beam_fem__large.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")

       beam_fem__polar = root.addChild('BeamFEM_POLAR')

       beam_fem__polar.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       beam_fem__polar.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrixMat3x3")
       beam_fem__polar.addObject('RegularGridTopology', name="grid", min="-5 -5 0", max="5 5 40", n="5 5 20")
       beam_fem__polar.addObject('MechanicalObject', template="Vec3", translation="22 0 0")
       beam_fem__polar.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
       beam_fem__polar.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       beam_fem__polar.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       beam_fem__polar.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo")
       beam_fem__polar.addObject('DiagonalMass', massDensity="0.2")
       beam_fem__polar.addObject('FastTetrahedralCorotationalForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", method="polar")
       beam_fem__polar.addObject('BoxROI', template="Vec3", name="box_roi", box="-6 -6 -1 50 6 0.1", drawBoxes="1")
       beam_fem__polar.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")

       beam_fem_polar2 = root.addChild('BeamFEM_polar2')

       beam_fem_polar2.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       beam_fem_polar2.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrixMat3x3")
       beam_fem_polar2.addObject('RegularGridTopology', name="grid", min="-5 -5 0", max="5 5 40", n="5 5 20")
       beam_fem_polar2.addObject('MechanicalObject', template="Vec3", translation="33 0 0")
       beam_fem_polar2.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
       beam_fem_polar2.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       beam_fem_polar2.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       beam_fem_polar2.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo")
       beam_fem_polar2.addObject('DiagonalMass', massDensity="0.2")
       beam_fem_polar2.addObject('FastTetrahedralCorotationalForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", method="polar2")
       beam_fem_polar2.addObject('BoxROI', template="Vec3", name="box_roi", box="-6 -6 -1 50 6 0.1", drawBoxes="1")
       beam_fem_polar2.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")
    ```

