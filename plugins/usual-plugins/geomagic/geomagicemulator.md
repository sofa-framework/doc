# GeomagicEmulator

Driver allowing interfacing with Geomagic haptic devices.


__Target__: `Geomagic`

__namespace__: `#!c++ sofa::component::controller`

__parents__: 

- `#!c++ GeomagicDriver`

__categories__: 

- Controller

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
		<td>handleEventTriggersUpdate</td>
		<td>
Event handling frequency controls the controller update frequency
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>deviceName</td>
		<td>
Name of device Configuration
</td>
		<td>Default Device</td>
	</tr>
	<tr>
		<td>positionBase</td>
		<td>
Position of the device base in the SOFA scene world coordinates
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>orientationBase</td>
		<td>
Orientation of the device base in the SOFA scene world coordinates
</td>
		<td>0 0 0 1</td>
	</tr>
	<tr>
		<td>orientationTool</td>
		<td>
Orientation of the tool in the SOFA scene world coordinates
</td>
		<td>0 0 0 1</td>
	</tr>
	<tr>
		<td>scale</td>
		<td>
Default scale applied to the Device coordinates
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>forceScale</td>
		<td>
Default scaling factor applied to the force feedback
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>maxInputForceFeedback</td>
		<td>
Maximum value of the normed input force feedback for device security
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>inputForceFeedback</td>
		<td>
Input force feedback in case of no LCPForceFeedback is found (manual setting)
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>manualStart</td>
		<td>
If true, will not automatically initDevice at component init phase.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>emitButtonEvent</td>
		<td>
If true, will send event through the graph when button are pushed/released
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>positionDevice</td>
		<td>
position of the base of the part of the device
</td>
		<td></td>
	</tr>
	<tr>
		<td>angle</td>
		<td>
Angluar values of joint (rad)
</td>
		<td></td>
	</tr>
	<tr>
		<td>button1</td>
		<td>
Button state 1
</td>
		<td></td>
	</tr>
	<tr>
		<td>button2</td>
		<td>
Button state 2
</td>
		<td></td>
	</tr>
	<tr>
		<td>speedFactor</td>
		<td>
factor to increase/decrease the movements speed
</td>
		<td>0.1</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawDeviceFrame</td>
		<td>
Visualize the frame corresponding to the device tooltip
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawDevice</td>
		<td>
Visualize the Geomagic device in the virtual scene
</td>
		<td>0</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|forceFeedBack|link to the forceFeedBack component, if not set will search through graph and take first one encountered.|



## Examples

Geomagic/share/sofa/examples/Geomagic/GeomagicEmulator-RigidCubes.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.05" showBoundingTree="0" gravity="0 0 0">
        <RequiredPlugin name="Geomagic"/> <!-- Needed to use components [GeomagicEmulator] -->
        <RequiredPlugin name="Sofa.Component.AnimationLoop"/> <!-- Needed to use components [FreeMotionAnimationLoop] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [LocalMinDistance] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [UncoupledConstraintCorrection] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Solver"/> <!-- Needed to use components [LCPConstraintSolver] -->
        <RequiredPlugin name="Sofa.Component.Controller"/> <!-- Needed to use components [MechanicalStateController] -->
        <RequiredPlugin name="Sofa.Component.Haptics"/> <!-- Needed to use components [LCPForceFeedback] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [RestShapeSpringsForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        
        <DefaultVisualManagerLoop />
        <CollisionPipeline name="pipeline" depth="6" verbose="0"/>
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="response" response="FrictionContactConstraint" />
        <LocalMinDistance name="proximity" alarmDistance="0.15" contactDistance="0.05" angleCone="0.0" />
        <FreeMotionAnimationLoop/>
        
        <LCPConstraintSolver tolerance="0.001" maxIt="1000"/>
        
    	<GeomagicEmulator name="GeomagicDevice" deviceName="Default Device" scale="1" positionBase="0 0 0" orientationBase="0 0.707 0 -0.707"
        drawDevice="1" drawDeviceFrame="1" forceFeedBack="@Instrument/LCPFF1"/>	
    	
    	<Node name="CubeStatic1">
    		<MeshOBJLoader name="loaderC" filename="mesh/cube.obj" scale3d="4 6 1" translation="-2 -2 -8" />
            <MechanicalObject name="Cube"  position="@loaderC.position" />     
    		<MeshTopology name="grid" src="@loaderC" />
    		<TriangleCollisionModel simulated="0" moving="0" bothSide="false" group="1"/>
    		<LineCollisionModel simulated="0" moving="0" group="1"/>
    		<PointCollisionModel simulated="0" moving="0" group="1"/>
    		<Node name="CubeVisu">
    			<OglModel name="CubeVisualModel"/>
    			<IdentityMapping input="@../" output="@CubeVisualModel" />
    		</Node>
        </Node>
        
        <Node name="CubeStatic2">
    		<MeshOBJLoader name="loaderC2" filename="mesh/cube.obj" scale3d="4 6 1" translation="-2 -2 8" />
            <MechanicalObject position="@loaderC2.position"/>
            <MeshTopology name="grid" src="@loaderC2" />
    		
            <TriangleCollisionModel bothSide="false"/>
    		<LineCollisionModel />
    		<PointCollisionModel />
            <Node name="Cube2Visu">
    			<OglModel name="Cube2VisualModel"/>
    			<IdentityMapping input="@../" output="@Cube2VisualModel" />
    		</Node>
        </Node>
    	
    	<Node name="Floor">
            <MeshOBJLoader name="loaderF" filename="mesh/cube.obj" scale3d="20 0.5 20" translation="0 -10 0"/>
            <MeshTopology src="@loaderF" />
            <MechanicalObject src="@loaderF" />
            <TriangleCollisionModel simulated="0" moving="0" bothSide="false" group="1"/>
            <LineCollisionModel simulated="0" moving="0" group="1" />
            <PointCollisionModel simulated="0" moving="0" group="1"/>
    		<Node name="VisuFloor" >
                <OglModel name="FloorVisualModel"/>
                <IdentityMapping input="@../" output="@FloorVisualModel" />
            </Node>
        </Node>
    
    	
        <!-- ADDED: the Mechanical state Controller gathers events from the Omni driver and populates the Mechanical state -->
        <Node name="Omni">
            <MechanicalObject template="Rigid3" name="DOFs" position="@GeomagicDevice.positionDevice"/>
            <MechanicalStateController template="Rigid3" listening="true" mainDirection="-1.0 0.0 0.0" handleEventTriggersUpdate="true"/>
        </Node>
    	
    	<Node name="Instrument" >
            <EulerImplicitSolver name="ODE solver" rayleighStiffness="0.05" rayleighMass="1.0" />
            <CGLinearSolver name="linear solver" iterations="25" tolerance="1e-10" threshold="10e-10" /> 
            
    		<MechanicalObject name="instrumentState" template="Rigid3" />
    		<UniformMass name="mass" totalMass="0.5" />
    		
    		<RestShapeSpringsForceField stiffness='1000000' angularStiffness='1000000' external_rest_shape='@../Omni/DOFs' points='0' external_points='0'/>
            <LCPForceFeedback name="LCPFF1" activate="true" forceCoef="1.0"/> 
            <UncoupledConstraintCorrection/>
    		
    		<Node name="VisuTool" >
                <MeshOBJLoader name="meshLoader_1" filename="Demos/Dentistry/data/mesh/dental_instrument.obj" handleSeams="1" />
                <OglModel name="InstrumentVisualModel" src="@meshLoader_1" color="1.0 0.2 0.2 1.0" ry="-180" rz="-90" dz="3.5" dx="-0.3"/>
                <RigidMapping name="MM->VM mapping" input="@instrumentState" output="@InstrumentVisualModel" />
            </Node>
    		
            <Node name="CollisionModel" >
                <MeshOBJLoader filename="Demos/Dentistry/data/mesh/dental_instrument_centerline.obj"  name="loader"/>
                <MeshTopology src="@loader" name="InstrumentCollisionModel" />
                <MechanicalObject src="@loader" name="instrumentCollisionState"  ry="-180" rz="-90" dz="3.5" dx="-0.3" />
                <LineCollisionModel contactStiffness="100"/>			
                <PointCollisionModel contactStiffness="100"/>
                <RigidMapping name="MM->CM mapping" input="@instrumentState" output="@instrumentCollisionState" />		
            </Node>       
        </Node> 
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.05", showBoundingTree="0", gravity="0 0 0")
        root.addObject('RequiredPlugin', name="Geomagic")
        root.addObject('RequiredPlugin', name="Sofa.Component.AnimationLoop")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Solver")
        root.addObject('RequiredPlugin', name="Sofa.Component.Controller")
        root.addObject('RequiredPlugin', name="Sofa.Component.Haptics")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultVisualManagerLoop')
        root.addObject('CollisionPipeline', name="pipeline", depth="6", verbose="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', name="response", response="FrictionContactConstraint")
        root.addObject('LocalMinDistance', name="proximity", alarmDistance="0.15", contactDistance="0.05", angleCone="0.0")
        root.addObject('FreeMotionAnimationLoop')
        root.addObject('LCPConstraintSolver', tolerance="0.001", maxIt="1000")
        root.addObject('GeomagicEmulator', name="GeomagicDevice", deviceName="Default Device", scale="1", positionBase="0 0 0", orientationBase="0 0.707 0 -0.707", drawDevice="1", drawDeviceFrame="1", forceFeedBack="@Instrument/LCPFF1")

        CubeStatic1 = root.addChild('CubeStatic1')
        CubeStatic1.addObject('MeshOBJLoader', name="loaderC", filename="mesh/cube.obj", scale3d="4 6 1", translation="-2 -2 -8")
        CubeStatic1.addObject('MechanicalObject', name="Cube", position="@loaderC.position")
        CubeStatic1.addObject('MeshTopology', name="grid", src="@loaderC")
        CubeStatic1.addObject('TriangleCollisionModel', simulated="0", moving="0", bothSide="false", group="1")
        CubeStatic1.addObject('LineCollisionModel', simulated="0", moving="0", group="1")
        CubeStatic1.addObject('PointCollisionModel', simulated="0", moving="0", group="1")

        CubeVisu = CubeStatic1.addChild('CubeVisu')
        CubeVisu.addObject('OglModel', name="CubeVisualModel")
        CubeVisu.addObject('IdentityMapping', input="@../", output="@CubeVisualModel")

        CubeStatic2 = root.addChild('CubeStatic2')
        CubeStatic2.addObject('MeshOBJLoader', name="loaderC2", filename="mesh/cube.obj", scale3d="4 6 1", translation="-2 -2 8")
        CubeStatic2.addObject('MechanicalObject', position="@loaderC2.position")
        CubeStatic2.addObject('MeshTopology', name="grid", src="@loaderC2")
        CubeStatic2.addObject('TriangleCollisionModel', bothSide="false")
        CubeStatic2.addObject('LineCollisionModel')
        CubeStatic2.addObject('PointCollisionModel')

        Cube2Visu = CubeStatic2.addChild('Cube2Visu')
        Cube2Visu.addObject('OglModel', name="Cube2VisualModel")
        Cube2Visu.addObject('IdentityMapping', input="@../", output="@Cube2VisualModel")

        Floor = root.addChild('Floor')
        Floor.addObject('MeshOBJLoader', name="loaderF", filename="mesh/cube.obj", scale3d="20 0.5 20", translation="0 -10 0")
        Floor.addObject('MeshTopology', src="@loaderF")
        Floor.addObject('MechanicalObject', src="@loaderF")
        Floor.addObject('TriangleCollisionModel', simulated="0", moving="0", bothSide="false", group="1")
        Floor.addObject('LineCollisionModel', simulated="0", moving="0", group="1")
        Floor.addObject('PointCollisionModel', simulated="0", moving="0", group="1")

        VisuFloor = Floor.addChild('VisuFloor')
        VisuFloor.addObject('OglModel', name="FloorVisualModel")
        VisuFloor.addObject('IdentityMapping', input="@../", output="@FloorVisualModel")

        Omni = root.addChild('Omni')
        Omni.addObject('MechanicalObject', template="Rigid3", name="DOFs", position="@GeomagicDevice.positionDevice")
        Omni.addObject('MechanicalStateController', template="Rigid3", listening="true", mainDirection="-1.0 0.0 0.0", handleEventTriggersUpdate="true")

        Instrument = root.addChild('Instrument')
        Instrument.addObject('EulerImplicitSolver', name="ODE solver", rayleighStiffness="0.05", rayleighMass="1.0")
        Instrument.addObject('CGLinearSolver', name="linear solver", iterations="25", tolerance="1e-10", threshold="10e-10")
        Instrument.addObject('MechanicalObject', name="instrumentState", template="Rigid3")
        Instrument.addObject('UniformMass', name="mass", totalMass="0.5")
        Instrument.addObject('RestShapeSpringsForceField', stiffness="1000000", angularStiffness="1000000", external_rest_shape="@../Omni/DOFs", points="0", external_points="0")
        Instrument.addObject('LCPForceFeedback', name="LCPFF1", activate="true", forceCoef="1.0")
        Instrument.addObject('UncoupledConstraintCorrection')

        VisuTool = Instrument.addChild('VisuTool')
        VisuTool.addObject('MeshOBJLoader', name="meshLoader_1", filename="Demos/Dentistry/data/mesh/dental_instrument.obj", handleSeams="1")
        VisuTool.addObject('OglModel', name="InstrumentVisualModel", src="@meshLoader_1", color="1.0 0.2 0.2 1.0", ry="-180", rz="-90", dz="3.5", dx="-0.3")
        VisuTool.addObject('RigidMapping', name="MM->VM mapping", input="@instrumentState", output="@InstrumentVisualModel")

        CollisionModel = Instrument.addChild('CollisionModel')
        CollisionModel.addObject('MeshOBJLoader', filename="Demos/Dentistry/data/mesh/dental_instrument_centerline.obj", name="loader")
        CollisionModel.addObject('MeshTopology', src="@loader", name="InstrumentCollisionModel")
        CollisionModel.addObject('MechanicalObject', src="@loader", name="instrumentCollisionState", ry="-180", rz="-90", dz="3.5", dx="-0.3")
        CollisionModel.addObject('LineCollisionModel', contactStiffness="100")
        CollisionModel.addObject('PointCollisionModel', contactStiffness="100")
        CollisionModel.addObject('RigidMapping', name="MM->CM mapping", input="@instrumentState", output="@instrumentCollisionState")
    ```
