<!-- generate_doc -->
# TetrahedralTensorMassForceField

Linear Elastic Tetrahedral Mesh


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.SolidMechanics.TensorMass

__namespace__: sofa::component::solidmechanics::tensormass

__parents__:

- ForceField

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

TetrahedralTensorMassForceField.scn

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
    def createScene(root_node):

       root = root_node.addChild('root')

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

       visu = quads.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="yellow")
       visu.addObject('IdentityMapping', input="@../../DoFs", output="@Visual")
    ```

TetrahedralTensorMassForceFieldCUDA.scn

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
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01")

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
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('NewProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       chain_fem = root.addChild('ChainFEM')

       torus_fixed = ChainFEM.addChild('TorusFixed')

       torus_fixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       torus_fixed.addObject('MeshTopology', src="@loader")
       torus_fixed.addObject('MechanicalObject', src="@loader")
       torus_fixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/torus2.obj", handleSeams="1")
       torus_fixed.addObject('OglModel', name="Visual", src="@meshLoader_2", color="gray")

       torus_tensor_mass = ChainFEM.addChild('TorusTensorMass')

       torus_tensor_mass.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       torus_tensor_mass.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       torus_tensor_mass.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
       torus_tensor_mass.addObject('MeshTopology', src="@loader")
       torus_tensor_mass.addObject('MechanicalObject', src="@loader", dx="2.5", template="CudaVec3f")
       torus_tensor_mass.addObject('UniformMass', totalMass="5")
       torus_tensor_mass.addObject('TetrahedralTensorMassForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", atomicGPU="false")

       visu = TorusTensorMass.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="red", dx="2.5")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusTensorMass.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="2.5")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       torus_fem__polar = ChainFEM.addChild('TorusFEM_POLAR')

       torus_fem__polar.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       torus_fem__polar.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       torus_fem__polar.addObject('MeshGmshLoader', name="loader", filename="mesh/torus2_low_res.msh")
       torus_fem__polar.addObject('MeshTopology', src="@loader")
       torus_fem__polar.addObject('MechanicalObject', src="@loader", dx="5")
       torus_fem__polar.addObject('UniformMass', totalMass="5")
       torus_fem__polar.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="polar")

       visu = TorusFEM_POLAR.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/torus2.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="blue", dx="5")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusFEM_POLAR.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="5")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       torus_fem__svd = ChainFEM.addChild('TorusFEM_SVD')

       torus_fem__svd.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       torus_fem__svd.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       torus_fem__svd.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
       torus_fem__svd.addObject('MeshTopology', src="@loader")
       torus_fem__svd.addObject('MechanicalObject', src="@loader", dx="7.5")
       torus_fem__svd.addObject('UniformMass', totalMass="5")
       torus_fem__svd.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="svd")

       visu = TorusFEM_SVD.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_3", color="yellow", dx="7.5")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusFEM_SVD.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="7.5")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('BarycentricMapping', )
    ```

TetrahedralTensorMassForceFieldCPU.scn

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
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01")

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
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('NewProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       chain_fem = root.addChild('ChainFEM')

       torus_fixed = ChainFEM.addChild('TorusFixed')

       torus_fixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       torus_fixed.addObject('MeshTopology', src="@loader")
       torus_fixed.addObject('MechanicalObject', src="@loader")
       torus_fixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/torus2.obj", handleSeams="1")
       torus_fixed.addObject('OglModel', name="Visual", src="@meshLoader_3", color="gray")

       torus_tensor_mass = ChainFEM.addChild('TorusTensorMass')

       torus_tensor_mass.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       torus_tensor_mass.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       torus_tensor_mass.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh", createSubelements="true")
       torus_tensor_mass.addObject('MeshTopology', src="@loader")
       torus_tensor_mass.addObject('MechanicalObject', src="@loader", dx="2.5", template="Vec3d")
       torus_tensor_mass.addObject('UniformMass', totalMass="5")
       torus_tensor_mass.addObject('TetrahedralTensorMassForceField', name="FEM", youngModulus="1000", poissonRatio="0.4")

       visu = TorusTensorMass.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="red", dx="2.5")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusTensorMass.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="2.5")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       torus_fem__polar = ChainFEM.addChild('TorusFEM_POLAR')

       torus_fem__polar.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       torus_fem__polar.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       torus_fem__polar.addObject('MeshGmshLoader', name="loader", filename="mesh/torus2_low_res.msh", createSubelements="true")
       torus_fem__polar.addObject('MeshTopology', src="@loader")
       torus_fem__polar.addObject('MechanicalObject', src="@loader", dx="5")
       torus_fem__polar.addObject('UniformMass', totalMass="5")
       torus_fem__polar.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="polar")

       visu = TorusFEM_POLAR.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/torus2.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_2", color="blue", dx="5")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusFEM_POLAR.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="5")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       torus_fem__svd = ChainFEM.addChild('TorusFEM_SVD')

       torus_fem__svd.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       torus_fem__svd.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       torus_fem__svd.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh", createSubelements="true")
       torus_fem__svd.addObject('MeshTopology', src="@loader")
       torus_fem__svd.addObject('MechanicalObject', src="@loader", dx="7.5")
       torus_fem__svd.addObject('UniformMass', totalMass="5")
       torus_fem__svd.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="svd")

       visu = TorusFEM_SVD.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="yellow", dx="7.5")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusFEM_SVD.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="7.5")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('BarycentricMapping', )
    ```

