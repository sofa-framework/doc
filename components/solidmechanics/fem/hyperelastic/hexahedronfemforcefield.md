# HexahedronFEMForceField

Hexahedral finite elements
Hexahedron FEM ForceField Supports GPU-side computations using CUDA


__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.Component.SolidMechanics.FEM.Elastic`

__namespace__: `#!c++ sofa::component::solidmechanics::fem::elastic`

__parents__: 

- `#!c++ BaseLinearElasticityFEMForceField`

__categories__: 

- ForceField

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
		<td>method</td>
		<td>
"large" or "polar" or "small" displacements
</td>
		<td>large</td>
	</tr>
	<tr>
		<td>updateStiffnessMatrix</td>
		<td>

</td>
		<td>0</td>
	</tr>
	<tr>
		<td>gatherPt</td>
		<td>
number of dof accumulated per threads during the gather operation (Only use in GPU version)
</td>
		<td></td>
	</tr>
	<tr>
		<td>gatherBsize</td>
		<td>
number of dof accumulated per threads during the gather operation (Only use in GPU version)
</td>
		<td></td>
	</tr>
	<tr>
		<td>stiffnessMatrices</td>
		<td>
Stiffness matrices per element (K_i)
</td>
		<td></td>
	</tr>
	<tr>
		<td>initialPoints</td>
		<td>
Initial Position
</td>
		<td></td>
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
		<td>drawPercentageOffset</td>
		<td>
size of the hexa
</td>
		<td>0.15</td>
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

Component/SolidMechanics/FEM/HexahedronFEMForceFieldAndMass.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceFieldAndMass] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.5" contactDistance="0.3" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="M1">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject />
            <RegularGridTopology nx="4" ny="4" nz="20" xmin="-9" xmax="-6" ymin="0" ymax="3" zmin="0" zmax="19" />
            <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15" />
            <HexahedronFEMForceFieldAndMass name="FEM" youngModulus="40000" poissonRatio="0.3" method="large" density="1" />
            <TriangleCollisionModel />
            <LineCollisionModel />
            <PointCollisionModel />
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('DefaultAnimationLoop')
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
        root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.5", contactDistance="0.3")
        root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

        M1 = root.addChild('M1')
        M1.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        M1.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        M1.addObject('MechanicalObject')
        M1.addObject('RegularGridTopology', nx="4", ny="4", nz="20", xmin="-9", xmax="-6", ymin="0", ymax="3", zmin="0", zmax="19")
        M1.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15")
        M1.addObject('HexahedronFEMForceFieldAndMass', name="FEM", youngModulus="40000", poissonRatio="0.3", method="large", density="1")
        M1.addObject('TriangleCollisionModel')
        M1.addObject('LineCollisionModel')
        M1.addObject('PointCollisionModel')
    ```

Component/SolidMechanics/FEM/HexahedronFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.5" contactDistance="0.3" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="M1">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" template="CompressedRowSparseMatrixMat3x3"/>
            <MechanicalObject />
            <UniformMass vertexMass="1" />
            <RegularGridTopology nx="4" ny="4" nz="20" xmin="-9" xmax="-6" ymin="0" ymax="3" zmin="0" zmax="19" />
            <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15" />
            <HexahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" method="large" />
            <TriangleCollisionModel />
            <LineCollisionModel />
            <PointCollisionModel />
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('DefaultAnimationLoop')
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
        root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.5", contactDistance="0.3")
        root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

        M1 = root.addChild('M1')
        M1.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        M1.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9", template="CompressedRowSparseMatrixMat3x3")
        M1.addObject('MechanicalObject')
        M1.addObject('UniformMass', vertexMass="1")
        M1.addObject('RegularGridTopology', nx="4", ny="4", nz="20", xmin="-9", xmax="-6", ymin="0", ymax="3", zmin="0", zmax="19")
        M1.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15")
        M1.addObject('HexahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3", method="large")
        M1.addObject('TriangleCollisionModel')
        M1.addObject('LineCollisionModel')
        M1.addObject('PointCollisionModel')
    ```

SofaCUDA/share/sofa/examples/SofaCUDA/benchmarks/HexahedronFEMForceField_beam16x16x76_cpu.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -9 0" dt="0.04">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [PlaneForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [HexahedronSetTopologyContainer HexahedronSetTopologyModifier QuadSetTopologyContainer QuadSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2QuadTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
    	
        <DefaultAnimationLoop />
        <DefaultVisualManagerLoop />
        <CollisionPipeline name="CollisionPipeline" verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="collision response" response="PenalityContactForceField" />
        <DiscreteIntersection/>
        
        <Node name="HexahedronFEMForceField-CPU-Red">
            <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="10" name="linear solver" tolerance="1.0e-6" threshold="1.0e-6" />
            
            <RegularGridTopology name="grid" n="76 16 16" min="0 6 -2" max="19 10 2" />
            <MechanicalObject name="Volume" template="Vec3"/>
    
            <HexahedronSetTopologyContainer name="Container" src="@grid"/>
            <HexahedronSetTopologyModifier name="Modifier" />
            
            <DiagonalMass totalMass="50.0" />
            <BoxROI name="ROI1" box="-0.1 5 -3 0.1 11 3" drawBoxes="1" />
            
            <FixedProjectiveConstraint indices="@ROI1.indices" />
            <HexahedronFEMForceField name="FEM" template="Vec3" youngModulus="1000" poissonRatio="0.3" method="large" />
            <PlaneForceField normal="0 1 0" d="2" stiffness="10000"  showPlane="1" />
            
            <Node name="surface">
                <QuadSetTopologyContainer name="Container" />
                <QuadSetTopologyModifier name="Modifier" />
                
                <Hexa2QuadTopologicalMapping input="@../Container" output="@Container" />
                <Node name="Visu">
                    <OglModel name="Visual" color="red" />
                    <IdentityMapping input="@../../Volume" output="@Visual" />
                </Node>
            </Node>
        </Node>
        
        
        <Node name="Floor">
    		<RegularGridTopology
    			nx="4" ny="1" nz="4"
    			xmin="-10" xmax="30"
    			ymin="1.9" ymax="1.9"
    			zmin="-20" zmax="20" />
    		<MechanicalObject />
    		<Node name="Visu">
    			<OglModel name="Visual" color="white"/>
    			<IdentityMapping input="@.." output="@Visual"/>
    		</Node>
    	</Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -9 0", dt="0.04")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
        root.addObject('DefaultAnimationLoop')
        root.addObject('DefaultVisualManagerLoop')
        root.addObject('CollisionPipeline', name="CollisionPipeline", verbose="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', name="collision response", response="PenalityContactForceField")
        root.addObject('DiscreteIntersection')

        HexahedronFEMForceField-CPU-Red = root.addChild('HexahedronFEMForceField-CPU-Red')
        HexahedronFEMForceField-CPU-Red.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        HexahedronFEMForceField-CPU-Red.addObject('CGLinearSolver', iterations="10", name="linear solver", tolerance="1.0e-6", threshold="1.0e-6")
        HexahedronFEMForceField-CPU-Red.addObject('RegularGridTopology', name="grid", n="76 16 16", min="0 6 -2", max="19 10 2")
        HexahedronFEMForceField-CPU-Red.addObject('MechanicalObject', name="Volume", template="Vec3")
        HexahedronFEMForceField-CPU-Red.addObject('HexahedronSetTopologyContainer', name="Container", src="@grid")
        HexahedronFEMForceField-CPU-Red.addObject('HexahedronSetTopologyModifier', name="Modifier")
        HexahedronFEMForceField-CPU-Red.addObject('DiagonalMass', totalMass="50.0")
        HexahedronFEMForceField-CPU-Red.addObject('BoxROI', name="ROI1", box="-0.1 5 -3 0.1 11 3", drawBoxes="1")
        HexahedronFEMForceField-CPU-Red.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")
        HexahedronFEMForceField-CPU-Red.addObject('HexahedronFEMForceField', name="FEM", template="Vec3", youngModulus="1000", poissonRatio="0.3", method="large")
        HexahedronFEMForceField-CPU-Red.addObject('PlaneForceField', normal="0 1 0", d="2", stiffness="10000", showPlane="1")

        surface = HexahedronFEMForceField-CPU-Red.addChild('surface')
        surface.addObject('QuadSetTopologyContainer', name="Container")
        surface.addObject('QuadSetTopologyModifier', name="Modifier")
        surface.addObject('Hexa2QuadTopologicalMapping', input="@../Container", output="@Container")

        Visu = surface.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="red")
        Visu.addObject('IdentityMapping', input="@../../Volume", output="@Visual")

        Floor = root.addChild('Floor')
        Floor.addObject('RegularGridTopology', nx="4", ny="1", nz="4", xmin="-10", xmax="30", ymin="1.9", ymax="1.9", zmin="-20", zmax="20")
        Floor.addObject('MechanicalObject')

        Visu = Floor.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="white")
        Visu.addObject('IdentityMapping', input="@..", output="@Visual")
    ```

SofaCUDA/share/sofa/examples/SofaCUDA/benchmarks/HexahedronFEMForceField_beam16x16x76_gpu.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -9 0" dt="0.04">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [HexahedronSetTopologyContainer HexahedronSetTopologyModifier QuadSetTopologyContainer QuadSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2QuadTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="SofaCUDA"/> <!-- Needed to use components [BoxROI DiagonalMass FixedProjectiveConstraint HexahedronFEMForceField IdentityMapping MechanicalObject PlaneForceField] -->
        
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
    	
        <DefaultAnimationLoop />
        <DefaultVisualManagerLoop />
        <CollisionPipeline name="CollisionPipeline" verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="collision response" response="PenalityContactForceField" />
        <DiscreteIntersection/>
        
        <Node name="HexahedronFEMForceField-GPU-Green">
            <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="10" name="linear solver" tolerance="1.0e-6" threshold="1.0e-6" />
            
            <RegularGridTopology name="grid" n="76 16 16" min="0 6 -2" max="19 10 2" />
            <MechanicalObject name="Volume" template="CudaVec3f"/>
    
            <HexahedronSetTopologyContainer name="Container" src="@grid"/>
            <HexahedronSetTopologyModifier name="Modifier" />
            
            <DiagonalMass totalMass="50.0" />
            <BoxROI name="ROI1" box="-0.1 5 -3 0.1 11 3" drawBoxes="1" />
            
            <FixedProjectiveConstraint indices="@ROI1.indices" />
            <HexahedronFEMForceField name="FEM" template="CudaVec3f" youngModulus="1000" poissonRatio="0.3" method="large" />
            <PlaneForceField normal="0 1 0" d="2" stiffness="10000"  showPlane="1" />
            
            <Node name="surface">
                <QuadSetTopologyContainer name="Container" />
                <QuadSetTopologyModifier name="Modifier" />
                
                <Hexa2QuadTopologicalMapping input="@../Container" output="@Container" />
                <Node name="Visu">
                    <OglModel name="Visual" color="green" />
                    <IdentityMapping input="@../../Volume" output="@Visual" />
                </Node>
            </Node>
        </Node>
        
        
        <Node name="Floor">
    		<RegularGridTopology
    			nx="4" ny="1" nz="4"
    			xmin="-10" xmax="30"
    			ymin="1.9" ymax="1.9"
    			zmin="-20" zmax="20" />
    		<MechanicalObject />
    		<Node name="Visu">
    			<OglModel name="Visual" color="white"/>
    			<IdentityMapping input="@.." output="@Visual"/>
    		</Node>
    	</Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -9 0", dt="0.04")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('RequiredPlugin', name="SofaCUDA")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
        root.addObject('DefaultAnimationLoop')
        root.addObject('DefaultVisualManagerLoop')
        root.addObject('CollisionPipeline', name="CollisionPipeline", verbose="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', name="collision response", response="PenalityContactForceField")
        root.addObject('DiscreteIntersection')

        HexahedronFEMForceField-GPU-Green = root.addChild('HexahedronFEMForceField-GPU-Green')
        HexahedronFEMForceField-GPU-Green.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        HexahedronFEMForceField-GPU-Green.addObject('CGLinearSolver', iterations="10", name="linear solver", tolerance="1.0e-6", threshold="1.0e-6")
        HexahedronFEMForceField-GPU-Green.addObject('RegularGridTopology', name="grid", n="76 16 16", min="0 6 -2", max="19 10 2")
        HexahedronFEMForceField-GPU-Green.addObject('MechanicalObject', name="Volume", template="CudaVec3f")
        HexahedronFEMForceField-GPU-Green.addObject('HexahedronSetTopologyContainer', name="Container", src="@grid")
        HexahedronFEMForceField-GPU-Green.addObject('HexahedronSetTopologyModifier', name="Modifier")
        HexahedronFEMForceField-GPU-Green.addObject('DiagonalMass', totalMass="50.0")
        HexahedronFEMForceField-GPU-Green.addObject('BoxROI', name="ROI1", box="-0.1 5 -3 0.1 11 3", drawBoxes="1")
        HexahedronFEMForceField-GPU-Green.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")
        HexahedronFEMForceField-GPU-Green.addObject('HexahedronFEMForceField', name="FEM", template="CudaVec3f", youngModulus="1000", poissonRatio="0.3", method="large")
        HexahedronFEMForceField-GPU-Green.addObject('PlaneForceField', normal="0 1 0", d="2", stiffness="10000", showPlane="1")

        surface = HexahedronFEMForceField-GPU-Green.addChild('surface')
        surface.addObject('QuadSetTopologyContainer', name="Container")
        surface.addObject('QuadSetTopologyModifier', name="Modifier")
        surface.addObject('Hexa2QuadTopologicalMapping', input="@../Container", output="@Container")

        Visu = surface.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="green")
        Visu.addObject('IdentityMapping', input="@../../Volume", output="@Visual")

        Floor = root.addChild('Floor')
        Floor.addObject('RegularGridTopology', nx="4", ny="1", nz="4", xmin="-10", xmax="30", ymin="1.9", ymax="1.9", zmin="-20", zmax="20")
        Floor.addObject('MechanicalObject')

        Visu = Floor.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="white")
        Visu.addObject('IdentityMapping', input="@..", output="@Visual")
    ```

SofaCUDA/share/sofa/examples/SofaCUDA/benchmarks/HexahedronFEMForceField_beam10x10x40_cpu.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -9 0" dt="0.01">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [HexahedronSetTopologyContainer HexahedronSetTopologyModifier QuadSetTopologyContainer QuadSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2QuadTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
      
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
    	
        <DefaultAnimationLoop />
        <DefaultVisualManagerLoop />
        <CollisionPipeline name="CollisionPipeline" verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="collision response" response="PenalityContactForceField" />
        <DiscreteIntersection/>
        
        <Node name="HexahedronFEMForceField-CPU-red">
            <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="20" name="linear solver" tolerance="1.0e-6" threshold="1.0e-6" />
            
            <RegularGridTopology name="grid" n="40 10 10" min="0 6 -2" max="16 10 2" />
            <MechanicalObject name="Volume" template="Vec3"/>
    
            <HexahedronSetTopologyContainer name="Container" src="@grid"/>
            <HexahedronSetTopologyModifier name="Modifier" />
    
            <DiagonalMass totalMass="50.0" />
            <BoxROI name="ROI1" box="-0.1 5 -3 0.1 11 3" drawBoxes="1" />
            
            <FixedProjectiveConstraint indices="@ROI1.indices" />
            <HexahedronFEMForceField name="FEM" template="Vec3" youngModulus="2000" poissonRatio="0.3" method="large" />
            
            <Node name="surface">
                <QuadSetTopologyContainer name="Container" />
                <QuadSetTopologyModifier name="Modifier" />
                
                <Hexa2QuadTopologicalMapping input="@../Container" output="@Container" />
                <Node name="Visu">
                    <OglModel name="Visual" color="red" />
                    <IdentityMapping input="@../../Volume" output="@Visual" />
                </Node>
            </Node>
        </Node>  
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -9 0", dt="0.01")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
        root.addObject('DefaultAnimationLoop')
        root.addObject('DefaultVisualManagerLoop')
        root.addObject('CollisionPipeline', name="CollisionPipeline", verbose="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', name="collision response", response="PenalityContactForceField")
        root.addObject('DiscreteIntersection')

        HexahedronFEMForceField-CPU-red = root.addChild('HexahedronFEMForceField-CPU-red')
        HexahedronFEMForceField-CPU-red.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        HexahedronFEMForceField-CPU-red.addObject('CGLinearSolver', iterations="20", name="linear solver", tolerance="1.0e-6", threshold="1.0e-6")
        HexahedronFEMForceField-CPU-red.addObject('RegularGridTopology', name="grid", n="40 10 10", min="0 6 -2", max="16 10 2")
        HexahedronFEMForceField-CPU-red.addObject('MechanicalObject', name="Volume", template="Vec3")
        HexahedronFEMForceField-CPU-red.addObject('HexahedronSetTopologyContainer', name="Container", src="@grid")
        HexahedronFEMForceField-CPU-red.addObject('HexahedronSetTopologyModifier', name="Modifier")
        HexahedronFEMForceField-CPU-red.addObject('DiagonalMass', totalMass="50.0")
        HexahedronFEMForceField-CPU-red.addObject('BoxROI', name="ROI1", box="-0.1 5 -3 0.1 11 3", drawBoxes="1")
        HexahedronFEMForceField-CPU-red.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")
        HexahedronFEMForceField-CPU-red.addObject('HexahedronFEMForceField', name="FEM", template="Vec3", youngModulus="2000", poissonRatio="0.3", method="large")

        surface = HexahedronFEMForceField-CPU-red.addChild('surface')
        surface.addObject('QuadSetTopologyContainer', name="Container")
        surface.addObject('QuadSetTopologyModifier', name="Modifier")
        surface.addObject('Hexa2QuadTopologicalMapping', input="@../Container", output="@Container")

        Visu = surface.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="red")
        Visu.addObject('IdentityMapping', input="@../../Volume", output="@Visual")
    ```

SofaCUDA/share/sofa/examples/SofaCUDA/benchmarks/HexahedronFEMForceField_beam10x10x40_gpu.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -9 0" dt="0.01">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [HexahedronSetTopologyContainer HexahedronSetTopologyModifier QuadSetTopologyContainer QuadSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2QuadTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="SofaCUDA"/> <!-- Needed to use components [BoxROI DiagonalMass FixedProjectiveConstraint HexahedronFEMForceField IdentityMapping MechanicalObject] -->
        
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
    	
        <DefaultAnimationLoop />
        <DefaultVisualManagerLoop />
        <CollisionPipeline name="CollisionPipeline" verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="collision response" response="PenalityContactForceField" />
        <DiscreteIntersection/>
        
        <Node name="HexahedronFEMForceField-GPU-Green">
            <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="20" name="linear solver" tolerance="1.0e-6" threshold="1.0e-6" />
            
            <RegularGridTopology name="grid" n="40 10 10" min="0 6 -2" max="16 10 2" />
            <MechanicalObject name="Volume" template="CudaVec3f"/>
    
            <HexahedronSetTopologyContainer name="Container" src="@grid"/>
            <HexahedronSetTopologyModifier name="Modifier" />
            
            <DiagonalMass totalMass="50.0" />
            <BoxROI name="ROI1" box="-0.1 5 -3 0.1 11 3" drawBoxes="1" />
            
            <FixedProjectiveConstraint indices="@ROI1.indices" />
            <HexahedronFEMForceField name="FEM" template="CudaVec3f" youngModulus="2000" poissonRatio="0.3" method="large" />
    
            <Node name="surface">
                <QuadSetTopologyContainer name="Container" />
                <QuadSetTopologyModifier name="Modifier" />
                
                <Hexa2QuadTopologicalMapping input="@../Container" output="@Container" />
                <Node name="Visu">
                    <OglModel name="Visual" color="green" />
                    <IdentityMapping input="@../../Volume" output="@Visual" />
                </Node>
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -9 0", dt="0.01")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('RequiredPlugin', name="SofaCUDA")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
        root.addObject('DefaultAnimationLoop')
        root.addObject('DefaultVisualManagerLoop')
        root.addObject('CollisionPipeline', name="CollisionPipeline", verbose="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', name="collision response", response="PenalityContactForceField")
        root.addObject('DiscreteIntersection')

        HexahedronFEMForceField-GPU-Green = root.addChild('HexahedronFEMForceField-GPU-Green')
        HexahedronFEMForceField-GPU-Green.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        HexahedronFEMForceField-GPU-Green.addObject('CGLinearSolver', iterations="20", name="linear solver", tolerance="1.0e-6", threshold="1.0e-6")
        HexahedronFEMForceField-GPU-Green.addObject('RegularGridTopology', name="grid", n="40 10 10", min="0 6 -2", max="16 10 2")
        HexahedronFEMForceField-GPU-Green.addObject('MechanicalObject', name="Volume", template="CudaVec3f")
        HexahedronFEMForceField-GPU-Green.addObject('HexahedronSetTopologyContainer', name="Container", src="@grid")
        HexahedronFEMForceField-GPU-Green.addObject('HexahedronSetTopologyModifier', name="Modifier")
        HexahedronFEMForceField-GPU-Green.addObject('DiagonalMass', totalMass="50.0")
        HexahedronFEMForceField-GPU-Green.addObject('BoxROI', name="ROI1", box="-0.1 5 -3 0.1 11 3", drawBoxes="1")
        HexahedronFEMForceField-GPU-Green.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")
        HexahedronFEMForceField-GPU-Green.addObject('HexahedronFEMForceField', name="FEM", template="CudaVec3f", youngModulus="2000", poissonRatio="0.3", method="large")

        surface = HexahedronFEMForceField-GPU-Green.addChild('surface')
        surface.addObject('QuadSetTopologyContainer', name="Container")
        surface.addObject('QuadSetTopologyModifier', name="Modifier")
        surface.addObject('Hexa2QuadTopologicalMapping', input="@../Container", output="@Container")

        Visu = surface.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="green")
        Visu.addObject('IdentityMapping', input="@../../Volume", output="@Visual")
    ```

