<!-- generate_doc -->
# ViewerSetting

Configuration for the Viewer of your application.


__Target__: Sofa.Component.Setting

__namespace__: sofa::component::setting

__parents__:

- ConfigurationSetting

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
		<td>resolution</td>
		<td>
resolution of the Viewer
		</td>
		<td>800 600</td>
	</tr>
	<tr>
		<td>fullscreen</td>
		<td>
Fullscreen mode
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>cameraMode</td>
		<td>
Camera mode
		</td>
		<td>Perspective</td>
	</tr>
	<tr>
		<td>objectPickingMethod</td>
		<td>
The method used to pick objects
		</td>
		<td>Ray casting</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|

## Examples 

ViewerSetting.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -1000 0" dt="0.04">
        <RequiredPlugin name="Sofa.Component.AnimationLoop"/> <!-- Needed to use components [FreeMotionAnimationLoop] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [UncoupledConstraintCorrection] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Solver"/> <!-- Needed to use components [LCPConstraintSolver] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.Setting"/> <!-- Needed to use components [ViewerSetting] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [SparseGridRamificationTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="Sofa.GL.Component.Shader"/> <!-- Needed to use components [LightManager SpotLight] -->
        
        <!-- Change the viewer size here -->
        <ViewerSetting resolution="800 600"/>
    
        <VisualStyle displayFlags="showVisual  " /> <!--showBehaviorModels showCollisionModels-->
    	<LCPConstraintSolver tolerance="1e-3" maxIt="1000" initial_guess="false" build_lcp="false"  printLog="0" mu="0.2"/>
        <FreeMotionAnimationLoop />
        <CollisionPipeline depth="15" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
    	<MinProximityIntersection name="Proximity" alarmDistance="1.5" contactDistance="1" />
    
        <LightManager />
        <SpotLight name="light1" color="1 1 1" position="0 80 25" direction="0 -1 -0.8" cutoff="30" exponent="1" />
    	<SpotLight name="light2" color="1 1 1" position="0 40 100" direction="0 0 -1" cutoff="30" exponent="1" />
    
        <CollisionResponse name="Response" response="FrictionContactConstraint" />
        <Node name="Snake" >
    
    		<SparseGridRamificationTopology n="4 12 3" fileTopology="mesh/snake_body.obj" nbVirtualFinerLevels="3" finestConnectivity="0" />
    
            <EulerImplicitSolver name="cg_odesolver" rayleighMass="1" rayleighStiffness="0.03" />
            <CGLinearSolver name="linear solver" iterations="20" tolerance="1e-12" threshold="1e-18" />
    		<MechanicalObject name="dofs"  scale="1" dy="2"/>
            <UniformMass totalMass="1.0" />
            <HexahedronFEMForceField name="FEM" youngModulus="30000.0" poissonRatio="0.3" method="large" updateStiffnessMatrix="false" printLog="0" />
    
    		<UncoupledConstraintCorrection />
    
    		<Node name="Collis">
                <MeshOBJLoader name="loader" filename="mesh/meca_snake_900tri.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" name="CollisModel" />
                <TriangleCollisionModel  selfCollision="0" />
                <LineCollisionModel    selfCollision="0" />
                <PointCollisionModel  selfCollision="0" />
                <BarycentricMapping input="@.." output="@." />
            </Node>
    
            <Node name="VisuBody" tags="Visual" >
                            <MeshOBJLoader name="meshLoader_0" filename="mesh/snake_body.obj" handleSeams="1" />
                            <OglModel  name="VisualBody" src="@meshLoader_0"   />
    			<BarycentricMapping input="@.." output="@VisualBody" />
            </Node>
    
            <Node name="VisuCornea" tags="Visual" >
                            <MeshOBJLoader name="meshLoader_3" filename="mesh/snake_cornea.obj" handleSeams="1" />
                            <OglModel  name="VisualCornea" src="@meshLoader_3"   />
    			<BarycentricMapping input="@.." output="@VisualCornea" />
            </Node>
    
            <Node name="VisuEye" tags="Visual" >
                            <MeshOBJLoader name="meshLoader_1" filename="mesh/snake_yellowEye.obj" handleSeams="1" />
                            <OglModel  name="VisualEye" src="@meshLoader_1"   />
    			<BarycentricMapping input="@.." output="@VisualEye" />
            </Node>
        </Node>
    
        <Node name="Base" >
    
    		<Node name="Stick">
    			<MeshOBJLoader name="loader" filename="mesh/collision_batons.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" name="CollisModel" />
                <LineCollisionModel simulated="false" moving="false" />
                <PointCollisionModel simulated="false"  moving="false"/>
    		</Node>
    		<Node name="Blobs">
    			<MeshOBJLoader name="loader" filename="mesh/collision_boules_V3.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" name="CollisModel" />
    			<TriangleCollisionModel simulated="false" moving="false"/>
                <LineCollisionModel simulated="false" moving="false"/>
                <PointCollisionModel simulated="false" moving="false"/>
    		</Node>
    
    		<Node name="Foot">
    			<MeshOBJLoader name="loader" filename="mesh/collision_pied.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" name="CollisModel" />
    			<TriangleCollisionModel simulated="false" moving="false"/>
                <LineCollisionModel simulated="false" moving="false"/>
                <PointCollisionModel simulated="false" moving="false"/>
    		</Node>
    
            <Node name="Visu" tags="Visual" >
                <MeshOBJLoader name="meshLoader_2" filename="mesh/SOFA_pod.obj" handleSeams="1" />
                <OglModel  name="OglModel" src="@meshLoader_2" />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -1000 0", dt="0.04")

       root.addObject('RequiredPlugin', name="Sofa.Component.AnimationLoop")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Solver")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.Setting")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Shader")
       root.addObject('ViewerSetting', resolution="800 600")
       root.addObject('VisualStyle', displayFlags="showVisual  ")
       root.addObject('LCPConstraintSolver', tolerance="1e-3", maxIt="1000", initial_guess="false", build_lcp="false", printLog="0", mu="0.2")
       root.addObject('FreeMotionAnimationLoop', )
       root.addObject('CollisionPipeline', depth="15", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="1.5", contactDistance="1")
       root.addObject('LightManager', )
       root.addObject('SpotLight', name="light1", color="1 1 1", position="0 80 25", direction="0 -1 -0.8", cutoff="30", exponent="1")
       root.addObject('SpotLight', name="light2", color="1 1 1", position="0 40 100", direction="0 0 -1", cutoff="30", exponent="1")
       root.addObject('CollisionResponse', name="Response", response="FrictionContactConstraint")

       snake = root.addChild('Snake')

       snake.addObject('SparseGridRamificationTopology', n="4 12 3", fileTopology="mesh/snake_body.obj", nbVirtualFinerLevels="3", finestConnectivity="0")
       snake.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighMass="1", rayleighStiffness="0.03")
       snake.addObject('CGLinearSolver', name="linear solver", iterations="20", tolerance="1e-12", threshold="1e-18")
       snake.addObject('MechanicalObject', name="dofs", scale="1", dy="2")
       snake.addObject('UniformMass', totalMass="1.0")
       snake.addObject('HexahedronFEMForceField', name="FEM", youngModulus="30000.0", poissonRatio="0.3", method="large", updateStiffnessMatrix="false", printLog="0")
       snake.addObject('UncoupledConstraintCorrection', )

       collis = Snake.addChild('Collis')

       collis.addObject('MeshOBJLoader', name="loader", filename="mesh/meca_snake_900tri.obj")
       collis.addObject('MeshTopology', src="@loader")
       collis.addObject('MechanicalObject', src="@loader", name="CollisModel")
       collis.addObject('TriangleCollisionModel', selfCollision="0")
       collis.addObject('LineCollisionModel', selfCollision="0")
       collis.addObject('PointCollisionModel', selfCollision="0")
       collis.addObject('BarycentricMapping', input="@..", output="@.")

       visu_body = Snake.addChild('VisuBody', tags="Visual")

       visu_body.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/snake_body.obj", handleSeams="1")
       visu_body.addObject('OglModel', name="VisualBody", src="@meshLoader_0")
       visu_body.addObject('BarycentricMapping', input="@..", output="@VisualBody")

       visu_cornea = Snake.addChild('VisuCornea', tags="Visual")

       visu_cornea.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/snake_cornea.obj", handleSeams="1")
       visu_cornea.addObject('OglModel', name="VisualCornea", src="@meshLoader_3")
       visu_cornea.addObject('BarycentricMapping', input="@..", output="@VisualCornea")

       visu_eye = Snake.addChild('VisuEye', tags="Visual")

       visu_eye.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/snake_yellowEye.obj", handleSeams="1")
       visu_eye.addObject('OglModel', name="VisualEye", src="@meshLoader_1")
       visu_eye.addObject('BarycentricMapping', input="@..", output="@VisualEye")

       base = root.addChild('Base')

       stick = Base.addChild('Stick')

       stick.addObject('MeshOBJLoader', name="loader", filename="mesh/collision_batons.obj")
       stick.addObject('MeshTopology', src="@loader")
       stick.addObject('MechanicalObject', src="@loader", name="CollisModel")
       stick.addObject('LineCollisionModel', simulated="false", moving="false")
       stick.addObject('PointCollisionModel', simulated="false", moving="false")

       blobs = Base.addChild('Blobs')

       blobs.addObject('MeshOBJLoader', name="loader", filename="mesh/collision_boules_V3.obj")
       blobs.addObject('MeshTopology', src="@loader")
       blobs.addObject('MechanicalObject', src="@loader", name="CollisModel")
       blobs.addObject('TriangleCollisionModel', simulated="false", moving="false")
       blobs.addObject('LineCollisionModel', simulated="false", moving="false")
       blobs.addObject('PointCollisionModel', simulated="false", moving="false")

       foot = Base.addChild('Foot')

       foot.addObject('MeshOBJLoader', name="loader", filename="mesh/collision_pied.obj")
       foot.addObject('MeshTopology', src="@loader")
       foot.addObject('MechanicalObject', src="@loader", name="CollisModel")
       foot.addObject('TriangleCollisionModel', simulated="false", moving="false")
       foot.addObject('LineCollisionModel', simulated="false", moving="false")
       foot.addObject('PointCollisionModel', simulated="false", moving="false")

       visu = Base.addChild('Visu', tags="Visual")

       visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/SOFA_pod.obj", handleSeams="1")
       visu.addObject('OglModel', name="OglModel", src="@meshLoader_2")
    ```

