# TetrahedralTensorMassForceField

Linear Elastic Tetrahedral Mesh
Supports GPU-side computations using CUDA


__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.Component.SolidMechanics.TensorMass`

__namespace__: `#!c++ sofa::component::solidmechanics::tensormass`

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
		<td>poissonRatio</td>
		<td>
Poisson ratio in Hooke's law
</td>
		<td>0.3</td>
	</tr>
	<tr>
		<td>youngModulus</td>
		<td>
Young's modulus in Hooke's law
</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>edgeInfo</td>
		<td>
Internal edge data
</td>
		<td></td>
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

Component/SolidMechanics/TensorMass/TetrahedralTensorMassForceField.scn

=== "XML"

    ```xml
    <Node name="root">
        <Node name="plugins">
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [EigenSimplicialLDLT] -->
            <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.TensorMass"/> <!-- Needed to use components [TetrahedralTensorMassForceField] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [QuadSetGeometryAlgorithms QuadSetTopologyContainer QuadSetTopologyModifier TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
            <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2QuadTopologicalMapping Hexa2TetraTopologicalMapping] -->
            <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
            <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        </Node>
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
    
        <DefaultAnimationLoop name="animationLoop"/>
        <DefaultVisualManagerLoop name="visualLoop"/>
    
        <EulerImplicitSolver name="odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
        <EigenSimplicialLDLT template="CompressedRowSparseMatrixMat3x3"/>
        <MechanicalObject name="DoFs" />
        <UniformMass name="mass" totalMass="320" />
        <RegularGridTopology name="grid" nx="4" ny="4" nz="20" xmin="-9" xmax="-6" ymin="0" ymax="3" zmin="0" zmax="19" />
        <BoxROI name="box" box="-10 -1 -0.0001  -5 4 0.0001"/>
        <FixedProjectiveConstraint indices="@box.indices" />
    
        <TetrahedronSetTopologyContainer name="Tetra_topo"/>
        <TetrahedronSetTopologyModifier name="Modifier" />
        <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
        <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" />
        <TetrahedralTensorMassForceField name="deformable" youngModulus="100000" poissonRatio="0.4" />
    
        <Node name="quads">
            <QuadSetTopologyContainer  name="Container" />
            <QuadSetTopologyModifier   name="Modifier" />
            <QuadSetGeometryAlgorithms name="GeomAlgo" template="Vec3" />
            <Hexa2QuadTopologicalMapping input="@../grid" output="@Container" />
            <Node name="Visu">
                <OglModel name="Visual" color="yellow" />
                <IdentityMapping input="@../../DoFs" output="@Visual" />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root')

        plugins = root.addChild('plugins')
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.TensorMass")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        plugins.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
        root.addObject('DefaultAnimationLoop', name="animationLoop")
        root.addObject('DefaultVisualManagerLoop', name="visualLoop")
        root.addObject('EulerImplicitSolver', name="odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        root.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrixMat3x3")
        root.addObject('MechanicalObject', name="DoFs")
        root.addObject('UniformMass', name="mass", totalMass="320")
        root.addObject('RegularGridTopology', name="grid", nx="4", ny="4", nz="20", xmin="-9", xmax="-6", ymin="0", ymax="3", zmin="0", zmax="19")
        root.addObject('BoxROI', name="box", box="-10 -1 -0.0001  -5 4 0.0001")
        root.addObject('FixedProjectiveConstraint', indices="@box.indices")
        root.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
        root.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        root.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        root.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo")
        root.addObject('TetrahedralTensorMassForceField', name="deformable", youngModulus="100000", poissonRatio="0.4")

        quads = root.addChild('quads')
        quads.addObject('QuadSetTopologyContainer', name="Container")
        quads.addObject('QuadSetTopologyModifier', name="Modifier")
        quads.addObject('QuadSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
        quads.addObject('Hexa2QuadTopologicalMapping', input="@../grid", output="@Container")

        Visu = quads.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="yellow")
        Visu.addObject('IdentityMapping', input="@../../DoFs", output="@Visual")
    ```

SofaCUDA/share/sofa/examples/SofaCUDA/TetrahedralTensorMassForceFieldCPU.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.01">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [NewProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.TensorMass"/> <!-- Needed to use components [TetrahedralTensorMassForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <NewProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="ChainFEM">
            <Node name="TorusFixed">
                <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <MeshOBJLoader name="meshLoader_3" filename="mesh/torus2.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_3" color="gray" />
            </Node>
            <Node name="TorusTensorMass">
                <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" createSubelements="true"/>
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="2.5" template="Vec3d" />
                <UniformMass totalMass="5" />
                <TetrahedralTensorMassForceField name="FEM" youngModulus="1000" poissonRatio="0.4" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_0" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_0" color="red" dx="2.5" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="2.5" />
                    <TriangleCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFEM_POLAR">
                <EulerImplicitSolver name="cg_odesolver" printLog="false" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MeshGmshLoader name="loader" filename="mesh/torus2_low_res.msh" createSubelements="true"/>
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="5" />
                <UniformMass totalMass="5" />
                <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false" method="polar" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_2" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_2" color="blue" dx="5" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="5" />
                    <TriangleCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFEM_SVD">
                <EulerImplicitSolver name="cg_odesolver" printLog="false" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" createSubelements="true" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="7.5" />
                <UniformMass totalMass="5" />
                <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false" method="svd" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_1" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_1" color="yellow" dx="7.5" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="7.5" />
                    <TriangleCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.TensorMass")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('NewProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
        root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

        ChainFEM = root.addChild('ChainFEM')

        TorusFixed = ChainFEM.addChild('TorusFixed')
        TorusFixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        TorusFixed.addObject('MeshTopology', src="@loader")
        TorusFixed.addObject('MechanicalObject', src="@loader")
        TorusFixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
        TorusFixed.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/torus2.obj", handleSeams="1")
        TorusFixed.addObject('OglModel', name="Visual", src="@meshLoader_3", color="gray")

        TorusTensorMass = ChainFEM.addChild('TorusTensorMass')
        TorusTensorMass.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        TorusTensorMass.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TorusTensorMass.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh", createSubelements="true")
        TorusTensorMass.addObject('MeshTopology', src="@loader")
        TorusTensorMass.addObject('MechanicalObject', src="@loader", dx="2.5", template="Vec3d")
        TorusTensorMass.addObject('UniformMass', totalMass="5")
        TorusTensorMass.addObject('TetrahedralTensorMassForceField', name="FEM", youngModulus="1000", poissonRatio="0.4")

        Visu = TorusTensorMass.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="red", dx="2.5")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusTensorMass.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="2.5")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusFEM_POLAR = ChainFEM.addChild('TorusFEM_POLAR')
        TorusFEM_POLAR.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        TorusFEM_POLAR.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TorusFEM_POLAR.addObject('MeshGmshLoader', name="loader", filename="mesh/torus2_low_res.msh", createSubelements="true")
        TorusFEM_POLAR.addObject('MeshTopology', src="@loader")
        TorusFEM_POLAR.addObject('MechanicalObject', src="@loader", dx="5")
        TorusFEM_POLAR.addObject('UniformMass', totalMass="5")
        TorusFEM_POLAR.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="polar")

        Visu = TorusFEM_POLAR.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/torus2.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_2", color="blue", dx="5")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFEM_POLAR.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="5")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusFEM_SVD = ChainFEM.addChild('TorusFEM_SVD')
        TorusFEM_SVD.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        TorusFEM_SVD.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TorusFEM_SVD.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh", createSubelements="true")
        TorusFEM_SVD.addObject('MeshTopology', src="@loader")
        TorusFEM_SVD.addObject('MechanicalObject', src="@loader", dx="7.5")
        TorusFEM_SVD.addObject('UniformMass', totalMass="5")
        TorusFEM_SVD.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="svd")

        Visu = TorusFEM_SVD.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="yellow", dx="7.5")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFEM_SVD.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="7.5")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('BarycentricMapping')
    ```

SofaCUDA/share/sofa/examples/SofaCUDA/TetrahedralTensorMassForceFieldCUDA.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.01">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [NewProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="SofaCUDA"/> <!-- Needed to use components [BarycentricMapping MechanicalObject TetrahedralTensorMassForceField UniformMass] -->
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <NewProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="ChainFEM">
            <Node name="TorusFixed">
                <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <MeshOBJLoader name="meshLoader_2" filename="mesh/torus2.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_2" color="gray" />
            </Node>
            <Node name="TorusTensorMass">
                <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="2.5" template="CudaVec3f" />
                <UniformMass totalMass="5" />
                <TetrahedralTensorMassForceField name="FEM" youngModulus="1000" poissonRatio="0.4"  atomicGPU="false" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_0" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_0" color="red" dx="2.5" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="2.5" />
                    <TriangleCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFEM_POLAR">
                <EulerImplicitSolver name="cg_odesolver" printLog="false" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MeshGmshLoader name="loader" filename="mesh/torus2_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="5" />
                <UniformMass totalMass="5" />
                <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false" method="polar" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_1" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_1" color="blue" dx="5" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="5" />
                    <TriangleCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFEM_SVD">
                <EulerImplicitSolver name="cg_odesolver" printLog="false" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="7.5" />
                <UniformMass totalMass="5" />
                <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false" method="svd" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_3" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_3" color="yellow" dx="7.5" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="7.5" />
                    <TriangleCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('RequiredPlugin', name="SofaCUDA")
        root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('NewProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
        root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

        ChainFEM = root.addChild('ChainFEM')

        TorusFixed = ChainFEM.addChild('TorusFixed')
        TorusFixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        TorusFixed.addObject('MeshTopology', src="@loader")
        TorusFixed.addObject('MechanicalObject', src="@loader")
        TorusFixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
        TorusFixed.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/torus2.obj", handleSeams="1")
        TorusFixed.addObject('OglModel', name="Visual", src="@meshLoader_2", color="gray")

        TorusTensorMass = ChainFEM.addChild('TorusTensorMass')
        TorusTensorMass.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        TorusTensorMass.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TorusTensorMass.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
        TorusTensorMass.addObject('MeshTopology', src="@loader")
        TorusTensorMass.addObject('MechanicalObject', src="@loader", dx="2.5", template="CudaVec3f")
        TorusTensorMass.addObject('UniformMass', totalMass="5")
        TorusTensorMass.addObject('TetrahedralTensorMassForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", atomicGPU="false")

        Visu = TorusTensorMass.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="red", dx="2.5")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusTensorMass.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="2.5")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusFEM_POLAR = ChainFEM.addChild('TorusFEM_POLAR')
        TorusFEM_POLAR.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        TorusFEM_POLAR.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TorusFEM_POLAR.addObject('MeshGmshLoader', name="loader", filename="mesh/torus2_low_res.msh")
        TorusFEM_POLAR.addObject('MeshTopology', src="@loader")
        TorusFEM_POLAR.addObject('MechanicalObject', src="@loader", dx="5")
        TorusFEM_POLAR.addObject('UniformMass', totalMass="5")
        TorusFEM_POLAR.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="polar")

        Visu = TorusFEM_POLAR.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/torus2.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="blue", dx="5")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFEM_POLAR.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="5")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusFEM_SVD = ChainFEM.addChild('TorusFEM_SVD')
        TorusFEM_SVD.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        TorusFEM_SVD.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TorusFEM_SVD.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
        TorusFEM_SVD.addObject('MeshTopology', src="@loader")
        TorusFEM_SVD.addObject('MechanicalObject', src="@loader", dx="7.5")
        TorusFEM_SVD.addObject('UniformMass', totalMass="5")
        TorusFEM_SVD.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="svd")

        Visu = TorusFEM_SVD.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_3", color="yellow", dx="7.5")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFEM_SVD.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="7.5")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('BarycentricMapping')
    ```

