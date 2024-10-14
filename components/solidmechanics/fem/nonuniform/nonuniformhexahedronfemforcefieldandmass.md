<!-- generate_doc -->
# NonUniformHexahedronFEMForceFieldAndMass

Non uniform Hexahedral finite elements.


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.SolidMechanics.FEM.NonUniform

__namespace__: sofa::component::solidmechanics::fem::nonuniform

__parents__:

- HexahedronFEMForceFieldAndMass

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
		<td>separateGravity</td>
		<td>
add separately gravity to velocity computation
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>rayleighMass</td>
		<td>
Rayleigh damping - mass matrix coefficient
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
		<td>massMatrices</td>
		<td>
Mass matrices per element (M_i)
		</td>
		<td></td>
	</tr>
	<tr>
		<td>density</td>
		<td>
density == volumetric mass in english (kg.m-3)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>lumpedMass</td>
		<td>
Does it use lumped masses?
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>nbVirtualFinerLevels</td>
		<td>
use virtual finer levels, in order to compte non-uniform stiffness
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>useMass</td>
		<td>
Using this ForceField like a Mass? (rather than using a separated Mass)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>totalMass</td>
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
		<td>drawPercentageOffset</td>
		<td>
size of the hexa
		</td>
		<td>0.15</td>
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

NonUniformHexahedronFEMForceFieldAndMass.scn

=== "XML"

    ```xml
    <Node name="SandBox" animate="0" dt="0.06" gravity="0 0 -9.81" multiThreadSimulation="0" time="0.0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceFieldAndMass] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.NonUniform"/> <!-- Needed to use components [NonUniformHexahedronFEMForceFieldAndMass] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [SparseGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showVisual" />
        <CollisionPipeline verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <include name="Salad Bowl 1" href="Objects/SaladBowl.xml" contactStiffness="10000" dy="-10" dz="-20" scale="100" />
        <include name="Salad Bowl 2" href="Objects/SaladBowl.xml" contactStiffness="10000" dx="70" dy="-10" dz="-20" scale="100" />
        <Node name="uniform">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <SparseGridTopology n="8 6 7" fileTopology="mesh/Armadillo_verysimplified.obj" />
            <MechanicalObject dx="70" ry="25" />
            <HexahedronFEMForceFieldAndMass youngModulus="20000" poissonRatio="0.3" method="large" density="10" updateStiffnessMatrix="false" printLog="0" />
            <Node name="Visuunif">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/Armadillo_simplified.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_0" color="1 .4 0 1" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Colliunif">
                <MeshOBJLoader name="loader" filename="mesh/Armadillo_verysimplified.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel contactStiffness="1" />
                <LineCollisionModel contactStiffness="1" />
                <PointCollisionModel contactStiffness="1" />
                <BarycentricMapping />
            </Node>
        </Node>
        <Node name="non uniform">
            <EulerImplicitSolver name="cg_odesolver" printLog="false" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <SparseGridTopology n="8 6 7" fileTopology="mesh/Armadillo_verysimplified.obj" nbVirtualFinerLevels="2" />
            <MechanicalObject ry="25" />
            <NonUniformHexahedronFEMForceFieldAndMass nbVirtualFinerLevels="2" youngModulus="20000" poissonRatio="0.3" method="large" density="10" updateStiffnessMatrix="false" printLog="0" />
            <Node name="Visunonunif">
                <MeshOBJLoader name="meshLoader_1" filename="mesh/Armadillo_simplified.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_1" color="0.4 0.6 1.0" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Collinonunif">
                <MeshOBJLoader name="loader" filename="mesh/Armadillo_verysimplified.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel contactStiffness="1" />
                <LineCollisionModel contactStiffness="1" />
                <PointCollisionModel contactStiffness="1" />
                <BarycentricMapping />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       sand_box = root_node.addChild('SandBox', animate="0", dt="0.06", gravity="0 0 -9.81", multiThreadSimulation="0", time="0.0")

       sand_box.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       sand_box.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       sand_box.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       sand_box.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       sand_box.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       sand_box.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       sand_box.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       sand_box.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       sand_box.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       sand_box.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.NonUniform")
       sand_box.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       sand_box.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       sand_box.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       sand_box.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       sand_box.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       sand_box.addObject('DefaultAnimationLoop', )
       sand_box.addObject('VisualStyle', displayFlags="showVisual")
       sand_box.addObject('CollisionPipeline', verbose="0", draw="0")
       sand_box.addObject('BruteForceBroadPhase', )
       sand_box.addObject('BVHNarrowPhase', )
       sand_box.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")
       sand_box.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")
       sand_box.addObject('include', name="Salad Bowl 1", href="Objects/SaladBowl.xml", contactStiffness="10000", dy="-10", dz="-20", scale="100")
       sand_box.addObject('include', name="Salad Bowl 2", href="Objects/SaladBowl.xml", contactStiffness="10000", dx="70", dy="-10", dz="-20", scale="100")

       uniform = SandBox.addChild('uniform')

       uniform.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       uniform.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       uniform.addObject('SparseGridTopology', n="8 6 7", fileTopology="mesh/Armadillo_verysimplified.obj")
       uniform.addObject('MechanicalObject', dx="70", ry="25")
       uniform.addObject('HexahedronFEMForceFieldAndMass', youngModulus="20000", poissonRatio="0.3", method="large", density="10", updateStiffnessMatrix="false", printLog="0")

       visuunif = uniform.addChild('Visuunif')

       visuunif.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/Armadillo_simplified.obj", handleSeams="1")
       visuunif.addObject('OglModel', name="Visual", src="@meshLoader_0", color="1 .4 0 1")
       visuunif.addObject('BarycentricMapping', input="@..", output="@Visual")

       colliunif = uniform.addChild('Colliunif')

       colliunif.addObject('MeshOBJLoader', name="loader", filename="mesh/Armadillo_verysimplified.obj")
       colliunif.addObject('MeshTopology', src="@loader")
       colliunif.addObject('MechanicalObject', src="@loader")
       colliunif.addObject('TriangleCollisionModel', contactStiffness="1")
       colliunif.addObject('LineCollisionModel', contactStiffness="1")
       colliunif.addObject('PointCollisionModel', contactStiffness="1")
       colliunif.addObject('BarycentricMapping', )

       non_uniform = SandBox.addChild('non uniform')

       non_uniform.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       non_uniform.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       non_uniform.addObject('SparseGridTopology', n="8 6 7", fileTopology="mesh/Armadillo_verysimplified.obj", nbVirtualFinerLevels="2")
       non_uniform.addObject('MechanicalObject', ry="25")
       non_uniform.addObject('NonUniformHexahedronFEMForceFieldAndMass', nbVirtualFinerLevels="2", youngModulus="20000", poissonRatio="0.3", method="large", density="10", updateStiffnessMatrix="false", printLog="0")

       visunonunif = non uniform.addChild('Visunonunif')

       visunonunif.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/Armadillo_simplified.obj", handleSeams="1")
       visunonunif.addObject('OglModel', name="Visual", src="@meshLoader_1", color="0.4 0.6 1.0")
       visunonunif.addObject('BarycentricMapping', input="@..", output="@Visual")

       collinonunif = non uniform.addChild('Collinonunif')

       collinonunif.addObject('MeshOBJLoader', name="loader", filename="mesh/Armadillo_verysimplified.obj")
       collinonunif.addObject('MeshTopology', src="@loader")
       collinonunif.addObject('MechanicalObject', src="@loader")
       collinonunif.addObject('TriangleCollisionModel', contactStiffness="1")
       collinonunif.addObject('LineCollisionModel', contactStiffness="1")
       collinonunif.addObject('PointCollisionModel', contactStiffness="1")
       collinonunif.addObject('BarycentricMapping', )
    ```

