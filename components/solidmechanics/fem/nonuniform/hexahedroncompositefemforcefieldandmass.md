<!-- generate_doc -->
# HexahedronCompositeFEMForceFieldAndMass

Non uniform Hexahedral finite elements.


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.SolidMechanics.FEM.NonUniform

__namespace__: sofa::component::solidmechanics::fem::nonuniform

__parents__:

- NonUniformHexahedronFEMForceFieldAndMass

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
		<td>finestToCoarse</td>
		<td>
Does the homogenization is done directly from the finest level to the coarse one?
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>homogenizationMethod</td>
		<td>
0->static, 1->constrained static, 2->modal analysis
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>completeInterpolation</td>
		<td>
Is the non-linear, complete interpolation used?
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>useRamification</td>
		<td>
If SparseGridRamification, are ramifications taken into account?
		</td>
		<td>1</td>
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
	<tr>
		<td>drawType</td>
		<td>

		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawColor</td>
		<td>

		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawSize</td>
		<td>

		</td>
		<td>-1</td>
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

HexahedronCompositeFEMForceFieldAndMass.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -700 0" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.NonUniform"/> <!-- Needed to use components [HexahedronCompositeFEMForceFieldAndMass HexahedronCompositeFEMMapping] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [SparseGridMultipleTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <!-- A soft gelatin object contains 2 bead, one stiff and one soft. Even using large embedding mesh, the
    	  HexahedronCompositeFEM permits to well simulate the global behavior, and the HexahedronCompositeFEMMapping
    	  permits to have a good interpolation of the inside bead behaviors.-->
          <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showVisual showForceFields" />
        <Node name="plane">
            <MeshOBJLoader name="meshLoader_0" filename="mesh/plane_loop_2.obj" scale=".2" handleSeams="1" />
            <OglModel name="plan" src="@meshLoader_0" rx="90" rz="90" dy="-2.01" material="Default Diffuse 1 1 0.4 0.4 1 Ambient 1 0.8 0.8 0.8 1 Specular 0 1 1 1 1 Emissive 0 1 1 1 1 Shininess 0 45" />
        </Node>
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.5" contactDistance="0.3" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="Composite elements with 3 differents material stiffnesses">
            <SparseGridMultipleTopology n="6 3 3" fileTopology="mesh/bubille_out.obj" fileTopologies="mesh/bubille_out.obj mesh/bubille_in1.obj mesh/bubille_in2.obj" nbVirtualFinerLevels="3" finestConnectivity="false" stiffnessCoefs="1 0.0001 50" massCoefs="1 1 1" />
            <EulerImplicitSolver vdamping="0" rayleighMass="0" rayleighStiffness="0" />
            <CGLinearSolver iterations="100" tolerance="1e-5" threshold="1e-5"/>
    <!--         <SparseLDLSolver printLog="false"/>
     -->        <MechanicalObject />
            <HexahedronCompositeFEMForceFieldAndMass drawType="0" lumpedMass="false" nbVirtualFinerLevels="2" youngModulus="600" poissonRatio="0.3" method="polar" density=".1" updateStiffnessMatrix="false" printLog="0" />
            <BoxConstraint box="-5 -2.1 -10    10 -1.9 10" />
            <Node name="Collinonunif">
                <MeshOBJLoader name="loader" filename="mesh/bubille_out.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <HexahedronCompositeFEMMapping />
                <TriangleCollisionModel />
                <Node name="Soft gelatin">
                    <MeshOBJLoader name="meshLoader_2" filename="mesh/bubille_out.obj" handleSeams="1" />
                    <OglModel name="VisualBody" src="@meshLoader_2" normals="0" color="0.1 .8 .3 .6" />
                    <IdentityMapping input="@.." output="@VisualBody" />
                </Node>
            </Node>
            <Node name="soft bead">
                <MeshOBJLoader name="meshLoader_1" filename="mesh/bubille_in1.obj" handleSeams="1" />
                <OglModel name="VisualBody1" src="@meshLoader_1" normals="0" color="1 0 0 1" />
                <HexahedronCompositeFEMMapping input="@.." output="@VisualBody1" />
            </Node>
            <Node name="stiff bead">
                <MeshOBJLoader name="meshLoader_3" filename="mesh/bubille_in2.obj" handleSeams="1" />
                <OglModel name="VisualBody2" src="@meshLoader_3" normals="0" color="0 0 1 1" />
                <HexahedronCompositeFEMMapping input="@.." output="@VisualBody2" />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -700 0", dt="0.02")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.NonUniform")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showVisual showForceFields")

       plane = root.addChild('plane')

       plane.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/plane_loop_2.obj", scale=".2", handleSeams="1")
       plane.addObject('OglModel', name="plan", src="@meshLoader_0", rx="90", rz="90", dy="-2.01", material="Default Diffuse 1 1 0.4 0.4 1 Ambient 1 0.8 0.8 0.8 1 Specular 0 1 1 1 1 Emissive 0 1 1 1 1 Shininess 0 45")

       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.5", contactDistance="0.3")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       composite_elements_with_3_differents_material_stiffnesses = root.addChild('Composite elements with 3 differents material stiffnesses')

       composite_elements_with_3_differents_material_stiffnesses.addObject('SparseGridMultipleTopology', n="6 3 3", fileTopology="mesh/bubille_out.obj", fileTopologies="mesh/bubille_out.obj mesh/bubille_in1.obj mesh/bubille_in2.obj", nbVirtualFinerLevels="3", finestConnectivity="false", stiffnessCoefs="1 0.0001 50", massCoefs="1 1 1")
       composite_elements_with_3_differents_material_stiffnesses.addObject('EulerImplicitSolver', vdamping="0", rayleighMass="0", rayleighStiffness="0")
       composite_elements_with_3_differents_material_stiffnesses.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")
       composite_elements_with_3_differents_material_stiffnesses.addObject('MechanicalObject', )
       composite_elements_with_3_differents_material_stiffnesses.addObject('HexahedronCompositeFEMForceFieldAndMass', drawType="0", lumpedMass="false", nbVirtualFinerLevels="2", youngModulus="600", poissonRatio="0.3", method="polar", density=".1", updateStiffnessMatrix="false", printLog="0")
       composite_elements_with_3_differents_material_stiffnesses.addObject('BoxConstraint', box="-5 -2.1 -10    10 -1.9 10")

       collinonunif = Composite elements with 3 differents material stiffnesses.addChild('Collinonunif')

       collinonunif.addObject('MeshOBJLoader', name="loader", filename="mesh/bubille_out.obj")
       collinonunif.addObject('MeshTopology', src="@loader")
       collinonunif.addObject('MechanicalObject', src="@loader")
       collinonunif.addObject('HexahedronCompositeFEMMapping', )
       collinonunif.addObject('TriangleCollisionModel', )

       soft_gelatin = Collinonunif.addChild('Soft gelatin')

       soft_gelatin.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/bubille_out.obj", handleSeams="1")
       soft_gelatin.addObject('OglModel', name="VisualBody", src="@meshLoader_2", normals="0", color="0.1 .8 .3 .6")
       soft_gelatin.addObject('IdentityMapping', input="@..", output="@VisualBody")

       soft_bead = Composite elements with 3 differents material stiffnesses.addChild('soft bead')

       soft_bead.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/bubille_in1.obj", handleSeams="1")
       soft_bead.addObject('OglModel', name="VisualBody1", src="@meshLoader_1", normals="0", color="1 0 0 1")
       soft_bead.addObject('HexahedronCompositeFEMMapping', input="@..", output="@VisualBody1")

       stiff_bead = Composite elements with 3 differents material stiffnesses.addChild('stiff bead')

       stiff_bead.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/bubille_in2.obj", handleSeams="1")
       stiff_bead.addObject('OglModel', name="VisualBody2", src="@meshLoader_3", normals="0", color="0 0 1 1")
       stiff_bead.addObject('HexahedronCompositeFEMMapping', input="@..", output="@VisualBody2")
    ```

