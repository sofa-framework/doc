# TetrahedralCorotationalFEMForceField

Corotational FEM Tetrahedral finite elements


__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.Component.SolidMechanics.FEM.Elastic`

__namespace__: `#!c++ sofa::component::solidmechanics::fem::elastic`

__parents__: 

- `#!c++ ForceField`

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
		<td>isCompliance</td>
		<td>
Consider the component as a compliance, else as a stiffness
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
		<td>tetrahedronInfo</td>
		<td>
Internal tetrahedron data
</td>
		<td></td>
	</tr>
	<tr>
		<td>method</td>
		<td>
"small", "large" (by QR) or "polar" displacements
</td>
		<td>large</td>
	</tr>
	<tr>
		<td>poissonRatio</td>
		<td>
FEM Poisson Ratio
</td>
		<td>0.45</td>
	</tr>
	<tr>
		<td>youngModulus</td>
		<td>
FEM Young Modulus
</td>
		<td>5000</td>
	</tr>
	<tr>
		<td>localStiffnessFactor</td>
		<td>
Allow specification of different stiffness per element. If there are N element and M values are specified, the youngModulus factor for element i would be localStiffnessFactor[i*M/N]
</td>
		<td></td>
	</tr>
	<tr>
		<td>updateStiffnessMatrix</td>
		<td>

</td>
		<td>0</td>
	</tr>
	<tr>
		<td>computeGlobalMatrix</td>
		<td>

</td>
		<td>0</td>
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

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|mechanicalStates|List of mechanical states to which this component is associated|
|mstate|MechanicalState used by this component|
|topology|link to the topology container|



## Examples

Component/SolidMechanics/FEM/TetrahedralCorotationalFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <!-- Mechanical Tetrahedral Corotational FEM Basic Example -->
    <Node name="root" dt="0.05" showBoundingTree="0" gravity="0 -9 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedralCorotationalFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <CollisionPipeline verbose="0" />
        <CollisionResponse />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
        <DefaultAnimationLoop/>
        
        <Node name="BeamFEM_SMALL">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            
            <RegularGridTopology name="grid" min="-5 -5 0" max="5 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3" />
            
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" />
            
            <DiagonalMass massDensity="0.2" />
            <TetrahedralCorotationalFEMForceField name="CFEM" youngModulus="1000" poissonRatio="0.3" method="small" />
            
            <BoxROI template="Vec3" name="box_roi" box="-6 -6 -1 30 6 0.1" drawBoxes="1" />
            <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
        </Node>
        
        <Node name="BeamFEM_LARGE">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            
            <RegularGridTopology name="grid" min="-5 -5 0" max="5 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3" translation="11 0 0"/>
            
            <TetrahedronSetTopologyContainer name="Tetra_topo" />
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" />
            
            <DiagonalMass massDensity="0.2" />
            <TetrahedralCorotationalFEMForceField name="CFEM" youngModulus="1000" poissonRatio="0.3" method="large" />
            
            <BoxROI template="Vec3" name="box_roi" box="-6 -6 -1 30 6 0.1" drawBoxes="1" />
            <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
        </Node>
        
        <Node name="BeamFEM_POLAR">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            
            <RegularGridTopology name="grid" min="-5 -5 0" max="5 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3" translation="22 0 0"/>
            
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" />
            
            <DiagonalMass massDensity="0.2" />
            <TetrahedralCorotationalFEMForceField name="CFEM" youngModulus="1000" poissonRatio="0.3" method="polar" />
            
            <BoxROI template="Vec3" name="box_roi" box="-6 -6 -1 30 6 0.1" drawBoxes="1" />
            <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
        </Node>
        
        
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.05", showBoundingTree="0", gravity="0 -9 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
        root.addObject('CollisionPipeline', verbose="0")
        root.addObject('CollisionResponse')
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")
        root.addObject('DefaultAnimationLoop')

        BeamFEM_SMALL = root.addChild('BeamFEM_SMALL')
        BeamFEM_SMALL.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        BeamFEM_SMALL.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        BeamFEM_SMALL.addObject('RegularGridTopology', name="grid", min="-5 -5 0", max="5 5 40", n="5 5 20")
        BeamFEM_SMALL.addObject('MechanicalObject', template="Vec3")
        BeamFEM_SMALL.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
        BeamFEM_SMALL.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        BeamFEM_SMALL.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        BeamFEM_SMALL.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo")
        BeamFEM_SMALL.addObject('DiagonalMass', massDensity="0.2")
        BeamFEM_SMALL.addObject('TetrahedralCorotationalFEMForceField', name="CFEM", youngModulus="1000", poissonRatio="0.3", method="small")
        BeamFEM_SMALL.addObject('BoxROI', template="Vec3", name="box_roi", box="-6 -6 -1 30 6 0.1", drawBoxes="1")
        BeamFEM_SMALL.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")

        BeamFEM_LARGE = root.addChild('BeamFEM_LARGE')
        BeamFEM_LARGE.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        BeamFEM_LARGE.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        BeamFEM_LARGE.addObject('RegularGridTopology', name="grid", min="-5 -5 0", max="5 5 40", n="5 5 20")
        BeamFEM_LARGE.addObject('MechanicalObject', template="Vec3", translation="11 0 0")
        BeamFEM_LARGE.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
        BeamFEM_LARGE.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        BeamFEM_LARGE.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        BeamFEM_LARGE.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo")
        BeamFEM_LARGE.addObject('DiagonalMass', massDensity="0.2")
        BeamFEM_LARGE.addObject('TetrahedralCorotationalFEMForceField', name="CFEM", youngModulus="1000", poissonRatio="0.3", method="large")
        BeamFEM_LARGE.addObject('BoxROI', template="Vec3", name="box_roi", box="-6 -6 -1 30 6 0.1", drawBoxes="1")
        BeamFEM_LARGE.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")

        BeamFEM_POLAR = root.addChild('BeamFEM_POLAR')
        BeamFEM_POLAR.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        BeamFEM_POLAR.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        BeamFEM_POLAR.addObject('RegularGridTopology', name="grid", min="-5 -5 0", max="5 5 40", n="5 5 20")
        BeamFEM_POLAR.addObject('MechanicalObject', template="Vec3", translation="22 0 0")
        BeamFEM_POLAR.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
        BeamFEM_POLAR.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        BeamFEM_POLAR.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        BeamFEM_POLAR.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo")
        BeamFEM_POLAR.addObject('DiagonalMass', massDensity="0.2")
        BeamFEM_POLAR.addObject('TetrahedralCorotationalFEMForceField', name="CFEM", youngModulus="1000", poissonRatio="0.3", method="polar")
        BeamFEM_POLAR.addObject('BoxROI', template="Vec3", name="box_roi", box="-6 -6 -1 30 6 0.1", drawBoxes="1")
        BeamFEM_POLAR.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")
    ```

