<!-- generate_doc -->
# TetrahedronFEMForceField

Tetrahedral finite elements.


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.SolidMechanics.FEM.Elastic

__namespace__: sofa::component::solidmechanics::fem::elastic

__parents__:

- BaseLinearElasticityFEMForceField
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
		<td>initialPoints</td>
		<td>
Initial Position
		</td>
		<td></td>
	</tr>
	<tr>
		<td>method</td>
		<td>
"small", "large" (by QR), "polar" or "svd" displacements
		</td>
		<td>large</td>
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
		<td>plasticMaxThreshold</td>
		<td>
Plastic Max Threshold (2-norm of the strain)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>plasticYieldThreshold</td>
		<td>
Plastic Yield Threshold (2-norm of the strain)
		</td>
		<td>0.0001</td>
	</tr>
	<tr>
		<td>plasticCreep</td>
		<td>
Plastic Creep Factor * dt [0,1]. Warning this factor depends on dt.
		</td>
		<td>0.9</td>
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
		<td>computeVonMisesStress</td>
		<td>
compute and display von Mises stress: 0: no computations, 1: using corotational strain, 2: using full Green strain. Set listening=1
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>vonMisesPerElement</td>
		<td>
von Mises Stress per element
		</td>
		<td></td>
	</tr>
	<tr>
		<td>vonMisesPerNode</td>
		<td>
von Mises Stress per node
		</td>
		<td></td>
	</tr>
	<tr>
		<td>vonMisesStressColors</td>
		<td>
Vector of colors describing the VonMises stress
		</td>
		<td></td>
	</tr>
	<tr>
		<td>updateStiffness</td>
		<td>
update structures (precomputed in init) using stiffness parameters in each iteration (set listening=1)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawHeterogeneousTetra</td>
		<td>
Draw Heterogeneous Tetra in different color
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showStressColorMap</td>
		<td>
Color map used to show stress values
		</td>
		<td>Blue to Red</td>
	</tr>
	<tr>
		<td>showStressAlpha</td>
		<td>
Alpha for vonMises visualisation
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>showVonMisesStressPerNode</td>
		<td>
draw points showing vonMises stress interpolated in nodes
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showVonMisesStressPerNodeColorMap</td>
		<td>
draw elements showing vonMises stress interpolated in nodes
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showVonMisesStressPerElement</td>
		<td>
draw triangles showing vonMises stress interpolated in elements
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showElementGapScale</td>
		<td>
draw gap between elements (when showWireFrame is disabled) [0,1]: 0: no gap, 1: no element
		</td>
		<td>0.333</td>
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

TetrahedronFEMForceField_Chain.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
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
    
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase name="N2" />
        <BVHNarrowPhase />
        <NewProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <DefaultAnimationLoop/>
        
        <Node name="ChainFEM">
            <Node name="TorusFixed">
                <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <MeshOBJLoader name="meshLoader_3" filename="mesh/torus2.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_3" color="gray" />
            </Node>
            <Node name="TorusFEM_LARGE">
                <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="2.5" />
                <UniformMass totalMass="5" />
                <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false" method="large" />
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
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" />
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
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', name="N2")
       root.addObject('BVHNarrowPhase', )
       root.addObject('NewProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")
       root.addObject('DefaultAnimationLoop', )

       chain_fem = root.addChild('ChainFEM')

       torus_fixed = ChainFEM.addChild('TorusFixed')

       torus_fixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       torus_fixed.addObject('MeshTopology', src="@loader")
       torus_fixed.addObject('MechanicalObject', src="@loader")
       torus_fixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/torus2.obj", handleSeams="1")
       torus_fixed.addObject('OglModel', name="Visual", src="@meshLoader_3", color="gray")

       torus_fem__large = ChainFEM.addChild('TorusFEM_LARGE')

       torus_fem__large.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       torus_fem__large.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       torus_fem__large.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
       torus_fem__large.addObject('MeshTopology', src="@loader")
       torus_fem__large.addObject('MechanicalObject', src="@loader", dx="2.5")
       torus_fem__large.addObject('UniformMass', totalMass="5")
       torus_fem__large.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="large")

       visu = TorusFEM_LARGE.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="red", dx="2.5")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusFEM_LARGE.addChild('Surf2')

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
       torus_fem__svd.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
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

TetrahedronFEMForceField_assemble.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 -9 0">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <DefaultAnimationLoop/>
        
        <Node name="BeamFEM_SMALL">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9"/>
            
            <RegularGridTopology name="grid" min="-5 -5 0" max="5 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3" />
            
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" />
            
            <DiagonalMass massDensity="0.2" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="true"
            method="small" computeVonMisesStress="2" showVonMisesStressPerElement="true"/>
            
            <BoxROI template="Vec3" name="box_roi" box="-6 -6 -1 50 6 0.1" drawBoxes="1" />
            <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
        </Node>
    
        
        <Node name="BeamFEM_LARGE">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            
            <RegularGridTopology name="grid" min="-5 -5 0" max="5 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3" translation="11 0 0"/>
            
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" />
            
            <DiagonalMass massDensity="0.2" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="true"
            method="large" computeVonMisesStress="1" showVonMisesStressPerElement="true"/>
            
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
       root.addObject('DefaultAnimationLoop', )

       beam_fem__small = root.addChild('BeamFEM_SMALL')

       beam_fem__small.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       beam_fem__small.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       beam_fem__small.addObject('RegularGridTopology', name="grid", min="-5 -5 0", max="5 5 40", n="5 5 20")
       beam_fem__small.addObject('MechanicalObject', template="Vec3")
       beam_fem__small.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
       beam_fem__small.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       beam_fem__small.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       beam_fem__small.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo")
       beam_fem__small.addObject('DiagonalMass', massDensity="0.2")
       beam_fem__small.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="true", method="small", computeVonMisesStress="2", showVonMisesStressPerElement="true")
       beam_fem__small.addObject('BoxROI', template="Vec3", name="box_roi", box="-6 -6 -1 50 6 0.1", drawBoxes="1")
       beam_fem__small.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")

       beam_fem__large = root.addChild('BeamFEM_LARGE')

       beam_fem__large.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       beam_fem__large.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       beam_fem__large.addObject('RegularGridTopology', name="grid", min="-5 -5 0", max="5 5 40", n="5 5 20")
       beam_fem__large.addObject('MechanicalObject', template="Vec3", translation="11 0 0")
       beam_fem__large.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
       beam_fem__large.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       beam_fem__large.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       beam_fem__large.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo")
       beam_fem__large.addObject('DiagonalMass', massDensity="0.2")
       beam_fem__large.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="true", method="large", computeVonMisesStress="1", showVonMisesStressPerElement="true")
       beam_fem__large.addObject('BoxROI', template="Vec3", name="box_roi", box="-6 -6 -1 50 6 0.1", drawBoxes="1")
       beam_fem__large.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")
    ```

TetrahedronFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 -9 0">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
    
        <Node name="BeamFEM_SMALL">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9"/>
    
            <RegularGridTopology name="grid" min="-5 -5 0" max="5 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3" />
    
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" />
    
            <DiagonalMass massDensity="0.2" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false"
                                      method="small" computeVonMisesStress="2" showVonMisesStressPerNodeColorMap="true"/>
    
            <BoxROI template="Vec3" name="box_roi" box="-6 -6 -1 50 6 0.1" drawBoxes="1" />
            <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
        </Node>
    
    
        <Node name="BeamFEM_LARGE">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
            <RegularGridTopology name="grid" min="-5 -5 0" max="5 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3" translation="11 0 0"/>
    
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" />
    
            <DiagonalMass massDensity="0.2" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false"
                                      method="large" computeVonMisesStress="1" showVonMisesStressPerNodeColorMap="true"/>
    
            <BoxROI template="Vec3" name="box_roi" box="-6 -6 -1 50 6 0.1" drawBoxes="1" />
            <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
        </Node>
    
        <Node name="BeamFEM_POLAR">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
            <RegularGridTopology name="grid" min="-5 -5 0" max="5 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3" translation="22 0 0"/>
    
            <TetrahedronSetTopologyContainer name="Tetra_topo" />
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" />
    
            <DiagonalMass massDensity="0.2" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false"
                                      method="polar" computeVonMisesStress="1" showVonMisesStressPerNodeColorMap="true"/>
    
            <BoxROI template="Vec3" name="box_roi" box="-6 -6 -1 50 6 0.1" drawBoxes="1" />
            <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
        </Node>
    
        <Node name="BeamFEM_SVD">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
            <RegularGridTopology name="grid" min="-5 -5 0" max="5 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3" translation="33 0 0"/>
    
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" />
    
            <DiagonalMass massDensity="0.2" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false"
                                      method="svd" computeVonMisesStress="1" showVonMisesStressPerNodeColorMap="true"/>
    
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
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")

       beam_fem__small = root.addChild('BeamFEM_SMALL')

       beam_fem__small.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       beam_fem__small.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       beam_fem__small.addObject('RegularGridTopology', name="grid", min="-5 -5 0", max="5 5 40", n="5 5 20")
       beam_fem__small.addObject('MechanicalObject', template="Vec3")
       beam_fem__small.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
       beam_fem__small.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       beam_fem__small.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       beam_fem__small.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo")
       beam_fem__small.addObject('DiagonalMass', massDensity="0.2")
       beam_fem__small.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="small", computeVonMisesStress="2", showVonMisesStressPerNodeColorMap="true")
       beam_fem__small.addObject('BoxROI', template="Vec3", name="box_roi", box="-6 -6 -1 50 6 0.1", drawBoxes="1")
       beam_fem__small.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")

       beam_fem__large = root.addChild('BeamFEM_LARGE')

       beam_fem__large.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       beam_fem__large.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       beam_fem__large.addObject('RegularGridTopology', name="grid", min="-5 -5 0", max="5 5 40", n="5 5 20")
       beam_fem__large.addObject('MechanicalObject', template="Vec3", translation="11 0 0")
       beam_fem__large.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
       beam_fem__large.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       beam_fem__large.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       beam_fem__large.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo")
       beam_fem__large.addObject('DiagonalMass', massDensity="0.2")
       beam_fem__large.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="large", computeVonMisesStress="1", showVonMisesStressPerNodeColorMap="true")
       beam_fem__large.addObject('BoxROI', template="Vec3", name="box_roi", box="-6 -6 -1 50 6 0.1", drawBoxes="1")
       beam_fem__large.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")

       beam_fem__polar = root.addChild('BeamFEM_POLAR')

       beam_fem__polar.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       beam_fem__polar.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       beam_fem__polar.addObject('RegularGridTopology', name="grid", min="-5 -5 0", max="5 5 40", n="5 5 20")
       beam_fem__polar.addObject('MechanicalObject', template="Vec3", translation="22 0 0")
       beam_fem__polar.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
       beam_fem__polar.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       beam_fem__polar.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       beam_fem__polar.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo")
       beam_fem__polar.addObject('DiagonalMass', massDensity="0.2")
       beam_fem__polar.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="polar", computeVonMisesStress="1", showVonMisesStressPerNodeColorMap="true")
       beam_fem__polar.addObject('BoxROI', template="Vec3", name="box_roi", box="-6 -6 -1 50 6 0.1", drawBoxes="1")
       beam_fem__polar.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")

       beam_fem__svd = root.addChild('BeamFEM_SVD')

       beam_fem__svd.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       beam_fem__svd.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       beam_fem__svd.addObject('RegularGridTopology', name="grid", min="-5 -5 0", max="5 5 40", n="5 5 20")
       beam_fem__svd.addObject('MechanicalObject', template="Vec3", translation="33 0 0")
       beam_fem__svd.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
       beam_fem__svd.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       beam_fem__svd.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       beam_fem__svd.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo")
       beam_fem__svd.addObject('DiagonalMass', massDensity="0.2")
       beam_fem__svd.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="svd", computeVonMisesStress="1", showVonMisesStressPerNodeColorMap="true")
       beam_fem__svd.addObject('BoxROI', template="Vec3", name="box_roi", box="-6 -6 -1 50 6 0.1", drawBoxes="1")
       beam_fem__svd.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")
    ```

TetrahedronFEMForceField_plasticity.scn

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
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [PlaneForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <VisualStyle displayFlags="showForceFields" />
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <NewProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <DefaultAnimationLoop/>
    
        <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
        <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
        <Node name="Plastic1">
            <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" rotation="90 0 0" />
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader"  />
            <UniformMass totalMass="5" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false" method="large" plasticYieldThreshold="0.01" plasticMaxThreshold="0.025" plasticCreep="1"/>
            <PlaneForceField normal="0 1 0" d="-3" stiffness="100000" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_2" filename="mesh/torus.obj" rotation="90 0 0" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_2" color="red"/>
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Surf2">
                <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" rotation="90 0 0"/>
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader"  />
                <TriangleCollisionModel />
                <BarycentricMapping />
            </Node>
        </Node>
    
    
        <Node name="Plastic2">
            <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" rotation="90 0 0" translation="-6 0 0"/>
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader"  />
            <UniformMass totalMass="5" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false" method="large" plasticYieldThreshold="0.005" plasticMaxThreshold="0.5" plasticCreep="1"/>
            <PlaneForceField normal="0 1 0" d="-3" stiffness="100000" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/torus.obj" rotation="90 0 0" translation="-6 0 0" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_0" color="blue"/>
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Surf2">
                <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" rotation="90 0 0" translation="-6 0 0"/>
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader"  />
                <TriangleCollisionModel />
                <BarycentricMapping />
            </Node>
        </Node>
    
    
        <Node name="Plastic3">
            <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" rotation="90 0 0" translation="-12 0 0"/>
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader"  />
            <UniformMass totalMass="5" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false" method="large" plasticYieldThreshold="0.005" plasticMaxThreshold="0.5" plasticCreep=".1"/>
            <PlaneForceField normal="0 1 0" d="-3" stiffness="100000" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_3" filename="mesh/torus.obj" rotation="90 0 0" translation="-12 0 0" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_3" color="yellow"/>
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Surf2">
                <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" rotation="90 0 0" translation="-12 0 0"/>
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader"  />
                <TriangleCollisionModel />
                <BarycentricMapping />
            </Node>
        </Node>
    
        <Node name="Elastic">
        <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" rotation="90 0 0" translation="6 0 0" />
        <MeshTopology src="@loader" />
        <MechanicalObject src="@loader"  />
        <UniformMass totalMass="5" />
        <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false" method="large" />
        <PlaneForceField normal="0 1 0" d="-3" stiffness="100000" />
        <Node name="Visu">
        <MeshOBJLoader name="meshLoader_1" filename="mesh/torus.obj" rotation="90 0 0" translation="6 0 0" handleSeams="1" />
        <OglModel name="Visual" src="@meshLoader_1" color="green"/>
        <BarycentricMapping input="@.." output="@Visual" />
        </Node>
            <Node name="Surf2">
                <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" rotation="90 0 0" translation="6 0 0"/>
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader"  />
                <TriangleCollisionModel />
                <BarycentricMapping />
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
       root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="showForceFields")
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('NewProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       root.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")

       plastic1 = root.addChild('Plastic1')

       plastic1.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh", rotation="90 0 0")
       plastic1.addObject('MeshTopology', src="@loader")
       plastic1.addObject('MechanicalObject', src="@loader")
       plastic1.addObject('UniformMass', totalMass="5")
       plastic1.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="large", plasticYieldThreshold="0.01", plasticMaxThreshold="0.025", plasticCreep="1")
       plastic1.addObject('PlaneForceField', normal="0 1 0", d="-3", stiffness="100000")

       visu = Plastic1.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/torus.obj", rotation="90 0 0", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_2", color="red")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = Plastic1.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj", rotation="90 0 0")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       plastic2 = root.addChild('Plastic2')

       plastic2.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh", rotation="90 0 0", translation="-6 0 0")
       plastic2.addObject('MeshTopology', src="@loader")
       plastic2.addObject('MechanicalObject', src="@loader")
       plastic2.addObject('UniformMass', totalMass="5")
       plastic2.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="large", plasticYieldThreshold="0.005", plasticMaxThreshold="0.5", plasticCreep="1")
       plastic2.addObject('PlaneForceField', normal="0 1 0", d="-3", stiffness="100000")

       visu = Plastic2.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", rotation="90 0 0", translation="-6 0 0", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="blue")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = Plastic2.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj", rotation="90 0 0", translation="-6 0 0")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       plastic3 = root.addChild('Plastic3')

       plastic3.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh", rotation="90 0 0", translation="-12 0 0")
       plastic3.addObject('MeshTopology', src="@loader")
       plastic3.addObject('MechanicalObject', src="@loader")
       plastic3.addObject('UniformMass', totalMass="5")
       plastic3.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="large", plasticYieldThreshold="0.005", plasticMaxThreshold="0.5", plasticCreep=".1")
       plastic3.addObject('PlaneForceField', normal="0 1 0", d="-3", stiffness="100000")

       visu = Plastic3.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/torus.obj", rotation="90 0 0", translation="-12 0 0", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_3", color="yellow")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = Plastic3.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj", rotation="90 0 0", translation="-12 0 0")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       elastic = root.addChild('Elastic')

       elastic.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh", rotation="90 0 0", translation="6 0 0")
       elastic.addObject('MeshTopology', src="@loader")
       elastic.addObject('MechanicalObject', src="@loader")
       elastic.addObject('UniformMass', totalMass="5")
       elastic.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="large")
       elastic.addObject('PlaneForceField', normal="0 1 0", d="-3", stiffness="100000")

       visu = Elastic.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/torus.obj", rotation="90 0 0", translation="6 0 0", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="green")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = Elastic.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj", rotation="90 0 0", translation="6 0 0")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('BarycentricMapping', )
    ```

TetrahedronFEMForceField_beam10x10x40_cpu.scn

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
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping Tetra2TriangleTopologicalMapping] -->
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
        
        <Node name="Beam">
            <RegularGridTopology name="grid" n="40 10 10" min="0 6 -2" max="16 10 2" />
            <TetrahedronSetTopologyContainer name="BeamTopo" />
            <TetrahedronSetTopologyModifier name="Modifier" />
    
            <Hexa2TetraTopologicalMapping input="@grid" output="@BeamTopo" />
        </Node>
       
        <Node name="TetrahedronFEMForceField-CPU-red">
            <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="20" name="linear solver" tolerance="1.0e-6" threshold="1.0e-6" />
            
            <MechanicalObject position="@../Beam/grid.position" name="Volume" template="Vec3"/>
    
            <TetrahedronSetTopologyContainer name="Container" src="@../Beam/BeamTopo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms name="GeomAlgo" template="Vec3" />
    
            <DiagonalMass totalMass="50.0" />
            <BoxROI name="ROI1" box="-0.1 5 -3 0.1 11 3" drawBoxes="1" />
            
            <FixedProjectiveConstraint indices="@ROI1.indices" />
            <TetrahedronFEMForceField template="Vec3" name="FEM" computeGlobalMatrix="false" method="large" poissonRatio="0.3" youngModulus="2000" />
            
            <Node name="surface">
                <TriangleSetTopologyContainer name="Container" />
                <TriangleSetTopologyModifier name="Modifier" />
                <TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                
                <Tetra2TriangleTopologicalMapping input="@../Container" output="@Container" />
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
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9 0", dt="0.01")

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
       root.addObject('DefaultAnimationLoop', )
       root.addObject('DefaultVisualManagerLoop', )
       root.addObject('CollisionPipeline', name="CollisionPipeline", verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', name="collision response", response="PenalityContactForceField")
       root.addObject('DiscreteIntersection', )

       beam = root.addChild('Beam')

       beam.addObject('RegularGridTopology', name="grid", n="40 10 10", min="0 6 -2", max="16 10 2")
       beam.addObject('TetrahedronSetTopologyContainer', name="BeamTopo")
       beam.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       beam.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@BeamTopo")

       tetrahedron_fem_force_field__cpu_red = root.addChild('TetrahedronFEMForceField-CPU-red')

       tetrahedron_fem_force_field__cpu_red.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
       tetrahedron_fem_force_field__cpu_red.addObject('CGLinearSolver', iterations="20", name="linear solver", tolerance="1.0e-6", threshold="1.0e-6")
       tetrahedron_fem_force_field__cpu_red.addObject('MechanicalObject', position="@../Beam/grid.position", name="Volume", template="Vec3")
       tetrahedron_fem_force_field__cpu_red.addObject('TetrahedronSetTopologyContainer', name="Container", src="@../Beam/BeamTopo")
       tetrahedron_fem_force_field__cpu_red.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       tetrahedron_fem_force_field__cpu_red.addObject('TetrahedronSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
       tetrahedron_fem_force_field__cpu_red.addObject('DiagonalMass', totalMass="50.0")
       tetrahedron_fem_force_field__cpu_red.addObject('BoxROI', name="ROI1", box="-0.1 5 -3 0.1 11 3", drawBoxes="1")
       tetrahedron_fem_force_field__cpu_red.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")
       tetrahedron_fem_force_field__cpu_red.addObject('TetrahedronFEMForceField', template="Vec3", name="FEM", computeGlobalMatrix="false", method="large", poissonRatio="0.3", youngModulus="2000")

       surface = TetrahedronFEMForceField-CPU-red.addChild('surface')

       surface.addObject('TriangleSetTopologyContainer', name="Container")
       surface.addObject('TriangleSetTopologyModifier', name="Modifier")
       surface.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       surface.addObject('Tetra2TriangleTopologicalMapping', input="@../Container", output="@Container")

       visu = surface.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="red")
       visu.addObject('IdentityMapping', input="@../../Volume", output="@Visual")
    ```

TetrahedronFEMForceField_beam10x10x40_gpu.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -9 0" dt="0.01">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping Tetra2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="SofaCUDA"/> <!-- Needed to use components [BoxROI DiagonalMass FixedProjectiveConstraint IdentityMapping MechanicalObject TetrahedronFEMForceField TetrahedronSetGeometryAlgorithms TriangleSetGeometryAlgorithms] -->
        
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
    	
        <DefaultAnimationLoop />
        <DefaultVisualManagerLoop />
        <CollisionPipeline name="CollisionPipeline" verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="collision response" response="PenalityContactForceField" />
        <DiscreteIntersection/>
        
        <Node name="Beam">
            <RegularGridTopology name="grid" n="40 10 10" min="0 6 -2" max="16 10 2" />
            <TetrahedronSetTopologyContainer name="BeamTopo" />
            <TetrahedronSetTopologyModifier name="Modifier" />
    
            <Hexa2TetraTopologicalMapping input="@grid" output="@BeamTopo" />
        </Node>
        
        
        <Node name="TetrahedronFEMForceField-GPU-Green">
            <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="20" name="linear solver" tolerance="1.0e-6" threshold="1.0e-6" />
            
            <MechanicalObject position="@../Beam/grid.position" name="Volume" template="CudaVec3f"/>
    
            <TetrahedronSetTopologyContainer name="Container" src="@../Beam/BeamTopo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms name="GeomAlgo" template="CudaVec3f" />
    
            <DiagonalMass totalMass="50.0" />
            <BoxROI name="ROI1" box="-0.1 5 -3 0.1 11 3" drawBoxes="1" />
            
            <FixedProjectiveConstraint indices="@ROI1.indices" />
            <TetrahedronFEMForceField template="CudaVec3f" name="FEM" computeGlobalMatrix="false" method="large" poissonRatio="0.3" youngModulus="2000" />
            
            <Node name="surface">
                <TriangleSetTopologyContainer name="Container" />
                <TriangleSetTopologyModifier name="Modifier" />
                <TriangleSetGeometryAlgorithms template="CudaVec3f" name="GeomAlgo" />
                
                <Tetra2TriangleTopologicalMapping input="@../Container" output="@Container" />
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
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9 0", dt="0.01")

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
       root.addObject('DefaultAnimationLoop', )
       root.addObject('DefaultVisualManagerLoop', )
       root.addObject('CollisionPipeline', name="CollisionPipeline", verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', name="collision response", response="PenalityContactForceField")
       root.addObject('DiscreteIntersection', )

       beam = root.addChild('Beam')

       beam.addObject('RegularGridTopology', name="grid", n="40 10 10", min="0 6 -2", max="16 10 2")
       beam.addObject('TetrahedronSetTopologyContainer', name="BeamTopo")
       beam.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       beam.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@BeamTopo")

       tetrahedron_fem_force_field__gpu__green = root.addChild('TetrahedronFEMForceField-GPU-Green')

       tetrahedron_fem_force_field__gpu__green.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
       tetrahedron_fem_force_field__gpu__green.addObject('CGLinearSolver', iterations="20", name="linear solver", tolerance="1.0e-6", threshold="1.0e-6")
       tetrahedron_fem_force_field__gpu__green.addObject('MechanicalObject', position="@../Beam/grid.position", name="Volume", template="CudaVec3f")
       tetrahedron_fem_force_field__gpu__green.addObject('TetrahedronSetTopologyContainer', name="Container", src="@../Beam/BeamTopo")
       tetrahedron_fem_force_field__gpu__green.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       tetrahedron_fem_force_field__gpu__green.addObject('TetrahedronSetGeometryAlgorithms', name="GeomAlgo", template="CudaVec3f")
       tetrahedron_fem_force_field__gpu__green.addObject('DiagonalMass', totalMass="50.0")
       tetrahedron_fem_force_field__gpu__green.addObject('BoxROI', name="ROI1", box="-0.1 5 -3 0.1 11 3", drawBoxes="1")
       tetrahedron_fem_force_field__gpu__green.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")
       tetrahedron_fem_force_field__gpu__green.addObject('TetrahedronFEMForceField', template="CudaVec3f", name="FEM", computeGlobalMatrix="false", method="large", poissonRatio="0.3", youngModulus="2000")

       surface = TetrahedronFEMForceField-GPU-Green.addChild('surface')

       surface.addObject('TriangleSetTopologyContainer', name="Container")
       surface.addObject('TriangleSetTopologyModifier', name="Modifier")
       surface.addObject('TriangleSetGeometryAlgorithms', template="CudaVec3f", name="GeomAlgo")
       surface.addObject('Tetra2TriangleTopologicalMapping', input="@../Container", output="@Container")

       visu = surface.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="green")
       visu.addObject('IdentityMapping', input="@../../Volume", output="@Visual")
    ```

TetrahedronFEMForceField_beam16x16x76_cpu.scn

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
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping Tetra2TriangleTopologicalMapping] -->
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
        
        <Node name="Beam">
            <RegularGridTopology name="grid" n="76 16 16" min="0 6 -2" max="19 10 2" />
            <TetrahedronSetTopologyContainer name="BeamTopo" />
            <TetrahedronSetTopologyModifier name="Modifier" />
    
            <Hexa2TetraTopologicalMapping input="@grid" output="@BeamTopo" />
        </Node>
       
        <Node name="TetrahedronFEMForceField-CPU-red">
            <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="10" name="linear solver" tolerance="1.0e-6" threshold="1.0e-6" />
            
            <MechanicalObject position="@../Beam/grid.position" name="Volume" template="Vec3"/>
    
            <TetrahedronSetTopologyContainer name="Container" src="@../Beam/BeamTopo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms name="GeomAlgo" template="Vec3" />
    
            <DiagonalMass totalMass="50.0" />
            <BoxROI name="ROI1" box="-0.1 5 -3 0.1 11 3" drawBoxes="1" />
            
            <FixedProjectiveConstraint indices="@ROI1.indices" />
            <TetrahedronFEMForceField template="Vec3" name="FEM" computeGlobalMatrix="false" method="large" poissonRatio="0.3" youngModulus="1000" />
    		<PlaneForceField normal="0 1 0" d="2" stiffness="10000"  showPlane="1" />
            
            <Node name="surface">
                <TriangleSetTopologyContainer name="Container" />
                <TriangleSetTopologyModifier name="Modifier" />
                <TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                
                <Tetra2TriangleTopologicalMapping input="@../Container" output="@Container" />
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
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9 0", dt="0.04")

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
       root.addObject('DefaultAnimationLoop', )
       root.addObject('DefaultVisualManagerLoop', )
       root.addObject('CollisionPipeline', name="CollisionPipeline", verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', name="collision response", response="PenalityContactForceField")
       root.addObject('DiscreteIntersection', )

       beam = root.addChild('Beam')

       beam.addObject('RegularGridTopology', name="grid", n="76 16 16", min="0 6 -2", max="19 10 2")
       beam.addObject('TetrahedronSetTopologyContainer', name="BeamTopo")
       beam.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       beam.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@BeamTopo")

       tetrahedron_fem_force_field__cpu_red = root.addChild('TetrahedronFEMForceField-CPU-red')

       tetrahedron_fem_force_field__cpu_red.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
       tetrahedron_fem_force_field__cpu_red.addObject('CGLinearSolver', iterations="10", name="linear solver", tolerance="1.0e-6", threshold="1.0e-6")
       tetrahedron_fem_force_field__cpu_red.addObject('MechanicalObject', position="@../Beam/grid.position", name="Volume", template="Vec3")
       tetrahedron_fem_force_field__cpu_red.addObject('TetrahedronSetTopologyContainer', name="Container", src="@../Beam/BeamTopo")
       tetrahedron_fem_force_field__cpu_red.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       tetrahedron_fem_force_field__cpu_red.addObject('TetrahedronSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
       tetrahedron_fem_force_field__cpu_red.addObject('DiagonalMass', totalMass="50.0")
       tetrahedron_fem_force_field__cpu_red.addObject('BoxROI', name="ROI1", box="-0.1 5 -3 0.1 11 3", drawBoxes="1")
       tetrahedron_fem_force_field__cpu_red.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")
       tetrahedron_fem_force_field__cpu_red.addObject('TetrahedronFEMForceField', template="Vec3", name="FEM", computeGlobalMatrix="false", method="large", poissonRatio="0.3", youngModulus="1000")
       tetrahedron_fem_force_field__cpu_red.addObject('PlaneForceField', normal="0 1 0", d="2", stiffness="10000", showPlane="1")

       surface = TetrahedronFEMForceField-CPU-red.addChild('surface')

       surface.addObject('TriangleSetTopologyContainer', name="Container")
       surface.addObject('TriangleSetTopologyModifier', name="Modifier")
       surface.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       surface.addObject('Tetra2TriangleTopologicalMapping', input="@../Container", output="@Container")

       visu = surface.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="red")
       visu.addObject('IdentityMapping', input="@../../Volume", output="@Visual")

       floor = root.addChild('Floor')

       floor.addObject('RegularGridTopology', nx="4", ny="1", nz="4", xmin="-10", xmax="30", ymin="1.9", ymax="1.9", zmin="-20", zmax="20")
       floor.addObject('MechanicalObject', )

       visu = Floor.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="white")
       visu.addObject('IdentityMapping', input="@..", output="@Visual")
    ```

TetrahedronFEMForceField_beam16x16x76_gpu.scn

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
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping Tetra2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="SofaCUDA"/> <!-- Needed to use components [BoxROI DiagonalMass FixedProjectiveConstraint IdentityMapping MechanicalObject PlaneForceField TetrahedronFEMForceField TetrahedronSetGeometryAlgorithms TriangleSetGeometryAlgorithms] -->
      
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
    	
        <DefaultAnimationLoop />
        <DefaultVisualManagerLoop />
        <CollisionPipeline name="CollisionPipeline" verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="collision response" response="PenalityContactForceField" />
        <DiscreteIntersection/>
        
        <Node name="Beam">
            <RegularGridTopology name="grid" n="76 16 16" min="0 6 -2" max="19 10 2" />
            <TetrahedronSetTopologyContainer name="BeamTopo" />
            <TetrahedronSetTopologyModifier name="Modifier" />
    
            <Hexa2TetraTopologicalMapping input="@grid" output="@BeamTopo" />
        </Node>
       
        <Node name="TetrahedronFEMForceField-GPU-Green">
            <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="10" name="linear solver" tolerance="1.0e-6" threshold="1.0e-6" />
            
            <MechanicalObject position="@../Beam/grid.position" name="Volume" template="CudaVec3f"/>
    
            <TetrahedronSetTopologyContainer name="Container" src="@../Beam/BeamTopo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms name="GeomAlgo" template="CudaVec3f" />
    
            <DiagonalMass totalMass="50.0" />
            <BoxROI name="ROI1" box="-0.1 5 -3 0.1 11 3" drawBoxes="1" />
            
            <FixedProjectiveConstraint indices="@ROI1.indices" />
            <TetrahedronFEMForceField template="CudaVec3f" name="FEM" computeGlobalMatrix="false" method="large" poissonRatio="0.3" youngModulus="1000" />
    		<PlaneForceField normal="0 1 0" d="2" stiffness="10000"  showPlane="1" />
            
            <Node name="surface">
                <TriangleSetTopologyContainer name="Container" />
                <TriangleSetTopologyModifier name="Modifier" />
                <TriangleSetGeometryAlgorithms template="CudaVec3f" name="GeomAlgo" />
                
                <Tetra2TriangleTopologicalMapping input="@../Container" output="@Container" />
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
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9 0", dt="0.04")

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
       root.addObject('DefaultAnimationLoop', )
       root.addObject('DefaultVisualManagerLoop', )
       root.addObject('CollisionPipeline', name="CollisionPipeline", verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', name="collision response", response="PenalityContactForceField")
       root.addObject('DiscreteIntersection', )

       beam = root.addChild('Beam')

       beam.addObject('RegularGridTopology', name="grid", n="76 16 16", min="0 6 -2", max="19 10 2")
       beam.addObject('TetrahedronSetTopologyContainer', name="BeamTopo")
       beam.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       beam.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@BeamTopo")

       tetrahedron_fem_force_field__gpu__green = root.addChild('TetrahedronFEMForceField-GPU-Green')

       tetrahedron_fem_force_field__gpu__green.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
       tetrahedron_fem_force_field__gpu__green.addObject('CGLinearSolver', iterations="10", name="linear solver", tolerance="1.0e-6", threshold="1.0e-6")
       tetrahedron_fem_force_field__gpu__green.addObject('MechanicalObject', position="@../Beam/grid.position", name="Volume", template="CudaVec3f")
       tetrahedron_fem_force_field__gpu__green.addObject('TetrahedronSetTopologyContainer', name="Container", src="@../Beam/BeamTopo")
       tetrahedron_fem_force_field__gpu__green.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       tetrahedron_fem_force_field__gpu__green.addObject('TetrahedronSetGeometryAlgorithms', name="GeomAlgo", template="CudaVec3f")
       tetrahedron_fem_force_field__gpu__green.addObject('DiagonalMass', totalMass="50.0")
       tetrahedron_fem_force_field__gpu__green.addObject('BoxROI', name="ROI1", box="-0.1 5 -3 0.1 11 3", drawBoxes="1")
       tetrahedron_fem_force_field__gpu__green.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")
       tetrahedron_fem_force_field__gpu__green.addObject('TetrahedronFEMForceField', template="CudaVec3f", name="FEM", computeGlobalMatrix="false", method="large", poissonRatio="0.3", youngModulus="1000")
       tetrahedron_fem_force_field__gpu__green.addObject('PlaneForceField', normal="0 1 0", d="2", stiffness="10000", showPlane="1")

       surface = TetrahedronFEMForceField-GPU-Green.addChild('surface')

       surface.addObject('TriangleSetTopologyContainer', name="Container")
       surface.addObject('TriangleSetTopologyModifier', name="Modifier")
       surface.addObject('TriangleSetGeometryAlgorithms', template="CudaVec3f", name="GeomAlgo")
       surface.addObject('Tetra2TriangleTopologicalMapping', input="@../Container", output="@Container")

       visu = surface.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="green")
       visu.addObject('IdentityMapping', input="@../../Volume", output="@Visual")

       floor = root.addChild('Floor')

       floor.addObject('RegularGridTopology', nx="4", ny="1", nz="4", xmin="-10", xmax="30", ymin="1.9", ymax="1.9", zmin="-20", zmax="20")
       floor.addObject('MechanicalObject', )

       visu = Floor.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="white")
       visu.addObject('IdentityMapping', input="@..", output="@Visual")
    ```

