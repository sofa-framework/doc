<!-- generate_doc -->
# CompositeCollisionPipeline

Multiple collision pipelines in one.


__Target__: Sofa.Component.Collision.Detection.Algorithm

__namespace__: sofa::component::collision::detection::algorithm

__parents__:

- Pipeline
- Base

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
		<td>nbThreads</td>
		<td>
If not yet initialized, the main task scheduler is initialized with this number of threads. 0 corresponds to the number of available cores on the CPU. -n (minus) corresponds to the number of available cores on the CPU minus the provided number.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>taskSchedulerType</td>
		<td>
Type of task scheduler to use.
		</td>
		<td>_default</td>
	</tr>
	<tr>
		<td>parallelDetection</td>
		<td>
Parallelize collision detection.
		</td>
		<td>0</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseComponent|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseComponent|
|subCollisionPipelines|List of sub collision pipelines to handle.|BaseSubCollisionPipeline|

## Examples 

CompositeCollisionPipeline_none.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01">
        <RequiredPlugin pluginName="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BruteForceBroadPhase,CollisionPipeline,RayTraceNarrowPhase] -->
        <RequiredPlugin pluginName="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [NewProximityIntersection] -->
        <RequiredPlugin pluginName="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel,PointCollisionModel,SphereCollisionModel,TriangleCollisionModel] -->
        <RequiredPlugin pluginName="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin pluginName="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin pluginName="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin pluginName="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin pluginName="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin pluginName="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin pluginName="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin pluginName="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <DefaultAnimationLoop/>
        
        <CollisionPipeline />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <NewProximityIntersection name="Proximity" alarmDistance="5" contactDistance="1" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
    
        <VisualStyle displayFlags="showVisualModels hideBehaviorModels showCollisionModels hideMappings hideForceFields" />
    
        <MeshOBJLoader name="torus_loader" filename="mesh/torus.obj" />
        <Node name="FixedTorusAndFallingSphere_1" >
            <Node name="FallingSphere" >
                <EulerImplicitSolver name="odesolver" />
                <CGLinearSolver name="linear_solver" iterations="250"  tolerance="1.0e-9" threshold="1.0e-9" />
    
                <MechanicalObject name="rigid" template="Rigid3d" position="-5 10 0 0 0 0 1" />
                <UniformMass totalMass="1.0" />
                <Node name="Collision" >
                    <MechanicalObject name="collision_rigid"/>
                    <SphereCollisionModel name="sphere" radius="1" contactStiffness="1"/>
                    <IdentityMapping input="@../rigid" output="@collision_rigid" />
                </Node>
            </Node>
            <Node name="FixedTorus" >
                <Node name="Collision" >
                    <MechanicalObject name="collision_torus" src="@../../../torus_loader" translation="-5 0 0" scale3d="0.8 0.8 0.8"/>
                    <MeshTopology name="topology" src="@../../../torus_loader"/>
                    <TriangleCollisionModel simulated="0" moving="0" contactStiffness="1" />  
                    <LineCollisionModel simulated="0" moving="0" contactStiffness="1" />
                    <PointCollisionModel simulated="0" moving="0" contactStiffness="1" />
                </Node>
            </Node>
        </Node>
    
        <Node name="FixedTorusAndFallingSphere_2" >
            <Node name="FallingSphere" >
                <EulerImplicitSolver name="odesolver" />
                <CGLinearSolver name="linear_solver" iterations="250"  tolerance="1.0e-9" threshold="1.0e-9" />
    
                <MechanicalObject name="rigid" template="Rigid3d" position="5 10 0 0 0 0 1" />
                <UniformMass totalMass="1.0" />
                <Node name="Collision" >
                    <MechanicalObject name="collision_rigid"/>
                    <SphereCollisionModel name="sphere" radius="0.7" contactStiffness="1" />
                    <IdentityMapping input="@../rigid" output="@collision_rigid" />
                </Node>
            </Node>
            <Node name="FixedTorus" >
                <Node name="Collision" >
                    <MechanicalObject name="collision_torus" src="@../../../torus_loader" translation="5 0 0" scale3d="0.5 0.5 0.5"/>
                    <MeshTopology name="topology" src="@../../../torus_loader"/>
                    <TriangleCollisionModel simulated="0" moving="0" contactStiffness="1"/>  
                    <LineCollisionModel simulated="0" moving="0" contactStiffness="1" />
                    <PointCollisionModel simulated="0" moving="0" contactStiffness="1" />
                </Node>
            </Node>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01")

       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Visual")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('CollisionPipeline', )
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('NewProximityIntersection', name="Proximity", alarmDistance="5", contactDistance="1")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")
       root.addObject('VisualStyle', displayFlags="showVisualModels hideBehaviorModels showCollisionModels hideMappings hideForceFields")
       root.addObject('MeshOBJLoader', name="torus_loader", filename="mesh/torus.obj")

       fixed_torus_and_falling_sphere_1 = root.addChild('FixedTorusAndFallingSphere_1')

       falling_sphere = FixedTorusAndFallingSphere_1.addChild('FallingSphere')

       falling_sphere.addObject('EulerImplicitSolver', name="odesolver")
       falling_sphere.addObject('CGLinearSolver', name="linear_solver", iterations="250", tolerance="1.0e-9", threshold="1.0e-9")
       falling_sphere.addObject('MechanicalObject', name="rigid", template="Rigid3d", position="-5 10 0 0 0 0 1")
       falling_sphere.addObject('UniformMass', totalMass="1.0")

       collision = FallingSphere.addChild('Collision')

       collision.addObject('MechanicalObject', name="collision_rigid")
       collision.addObject('SphereCollisionModel', name="sphere", radius="1", contactStiffness="1")
       collision.addObject('IdentityMapping', input="@../rigid", output="@collision_rigid")

       fixed_torus = FixedTorusAndFallingSphere_1.addChild('FixedTorus')

       collision = FixedTorus.addChild('Collision')

       collision.addObject('MechanicalObject', name="collision_torus", src="@../../../torus_loader", translation="-5 0 0", scale3d="0.8 0.8 0.8")
       collision.addObject('MeshTopology', name="topology", src="@../../../torus_loader")
       collision.addObject('TriangleCollisionModel', simulated="0", moving="0", contactStiffness="1")
       collision.addObject('LineCollisionModel', simulated="0", moving="0", contactStiffness="1")
       collision.addObject('PointCollisionModel', simulated="0", moving="0", contactStiffness="1")

       fixed_torus_and_falling_sphere_2 = root.addChild('FixedTorusAndFallingSphere_2')

       falling_sphere = FixedTorusAndFallingSphere_2.addChild('FallingSphere')

       falling_sphere.addObject('EulerImplicitSolver', name="odesolver")
       falling_sphere.addObject('CGLinearSolver', name="linear_solver", iterations="250", tolerance="1.0e-9", threshold="1.0e-9")
       falling_sphere.addObject('MechanicalObject', name="rigid", template="Rigid3d", position="5 10 0 0 0 0 1")
       falling_sphere.addObject('UniformMass', totalMass="1.0")

       collision = FallingSphere.addChild('Collision')

       collision.addObject('MechanicalObject', name="collision_rigid")
       collision.addObject('SphereCollisionModel', name="sphere", radius="0.7", contactStiffness="1")
       collision.addObject('IdentityMapping', input="@../rigid", output="@collision_rigid")

       fixed_torus = FixedTorusAndFallingSphere_2.addChild('FixedTorus')

       collision = FixedTorus.addChild('Collision')

       collision.addObject('MechanicalObject', name="collision_torus", src="@../../../torus_loader", translation="5 0 0", scale3d="0.5 0.5 0.5")
       collision.addObject('MeshTopology', name="topology", src="@../../../torus_loader")
       collision.addObject('TriangleCollisionModel', simulated="0", moving="0", contactStiffness="1")
       collision.addObject('LineCollisionModel', simulated="0", moving="0", contactStiffness="1")
       collision.addObject('PointCollisionModel', simulated="0", moving="0", contactStiffness="1")
    ```

CompositeCollisionPipeline.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01">
        <RequiredPlugin pluginName="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BruteForceBroadPhase,CollisionPipeline,RayTraceNarrowPhase] -->
        <RequiredPlugin pluginName="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [NewProximityIntersection] -->
        <RequiredPlugin pluginName="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel,PointCollisionModel,SphereCollisionModel,TriangleCollisionModel] -->
        <RequiredPlugin pluginName="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin pluginName="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin pluginName="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin pluginName="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin pluginName="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin pluginName="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin pluginName="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin pluginName="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <DefaultAnimationLoop/>
    
        <VisualStyle displayFlags="showVisualModels hideBehaviorModels showCollisionModels hideMappings hideForceFields" />
    
        <MeshOBJLoader name="torus_loader" filename="mesh/torus.obj" />
        <Node name="FixedTorusAndFallingSphere_1" >
            <Node name="FallingSphere" >
                <EulerImplicitSolver name="odesolver" />
                <CGLinearSolver name="linear_solver" iterations="250"  tolerance="1.0e-9" threshold="1.0e-9" />
    
                <MechanicalObject name="rigid" template="Rigid3d" position="-5 10 0 0 0 0 1" />
                <UniformMass totalMass="1.0" />
                <Node name="Collision" >
                    <MechanicalObject name="collision_rigid"/>
                    <SphereCollisionModel name="sphere" radius="1" contactStiffness="1"/>
                    <IdentityMapping input="@../rigid" output="@collision_rigid" />
                </Node>
            </Node>
            <Node name="FixedTorus" >
                <Node name="Collision" >
                    <MechanicalObject name="collision_torus" src="@../../../torus_loader" translation="-5 0 0" scale3d="0.8 0.8 0.8"/>
                    <MeshTopology name="topology" src="@../../../torus_loader"/>
                    <TriangleCollisionModel name="triangle_collision" simulated="0" moving="0" contactStiffness="1" />  
                    <LineCollisionModel name="line_collision" simulated="0" moving="0" contactStiffness="1" />
                    <PointCollisionModel name="point_collision" simulated="0" moving="0" contactStiffness="1" />
                </Node>
            </Node>
        </Node>
    
        <Node name="FixedTorusAndFallingSphere_2" >
            <Node name="FallingSphere" >
                <EulerImplicitSolver name="odesolver" />
                <CGLinearSolver name="linear_solver" iterations="250"  tolerance="1.0e-9" threshold="1.0e-9" />
    
                <MechanicalObject name="rigid" template="Rigid3d" position="5 10 0 0 0 0 1" />
                <UniformMass totalMass="1.0" />
                <Node name="Collision" >
                    <MechanicalObject name="collision_rigid"/>
                    <SphereCollisionModel name="sphere" radius="0.7" contactStiffness="1" />
                    <IdentityMapping input="@../rigid" output="@collision_rigid" />
                </Node>
            </Node>
            <Node name="FixedTorus" >
                <Node name="Collision" >
                    <MechanicalObject name="collision_torus" src="@../../../torus_loader" translation="5 0 0" scale3d="0.5 0.5 0.5"/>
                    <MeshTopology name="topology" src="@../../../torus_loader"/>
                    <TriangleCollisionModel name="triangle_collision" simulated="0" moving="0" contactStiffness="1" />  
                    <LineCollisionModel name="line_collision" simulated="0" moving="0" contactStiffness="1" />
                    <PointCollisionModel name="point_collision" simulated="0" moving="0" contactStiffness="1" />
                </Node>
            </Node>
        </Node>
    
    
        <BruteForceBroadPhase name="broad_phase_large"/>
        <BVHNarrowPhase name="narrow_phase_large"/>
        <NewProximityIntersection name="intersection_large" alarmDistance="5" contactDistance="1" />
        <CollisionResponse name="response_large" response="PenalityContactForceField" />
        <SubCollisionPipeline name="collision_pipeline_large"
            collisionModels="@/FixedTorusAndFallingSphere_1/FallingSphere/Collision/sphere
            @FixedTorusAndFallingSphere_1/FixedTorus/Collision/triangle_collision @FixedTorusAndFallingSphere_1/FixedTorus/Collision/line_collision @FixedTorusAndFallingSphere_1/FixedTorus/Collision/point_collision"
            broadPhaseDetection="@broad_phase_large"
            narrowPhaseDetection="@narrow_phase_large"
            intersectionMethod="@intersection_large"
            contactManager="@response_large"
        />
        <BruteForceBroadPhase name="broad_phase_small"/>
        <BVHNarrowPhase name="narrow_phase_small"/>
        <NewProximityIntersection name="intersection_small" alarmDistance="2.5" contactDistance="0.6" />
        <CollisionResponse name="response_small" response="PenalityContactForceField" />
        <SubCollisionPipeline name="collision_pipeline_small"
            collisionModels="@FixedTorusAndFallingSphere_2/FallingSphere/Collision/sphere 
            @FixedTorusAndFallingSphere_2/FixedTorus/Collision/triangle_collision @FixedTorusAndFallingSphere_2/FixedTorus/Collision/line_collision @FixedTorusAndFallingSphere_2/FixedTorus/Collision/point_collision"
            broadPhaseDetection="@broad_phase_small"
            narrowPhaseDetection="@narrow_phase_small"
            intersectionMethod="@intersection_small"
            contactManager="@response_small"
        />
        <CompositeCollisionPipeline name="composite_pipeline" subCollisionPipelines="@collision_pipeline_large @collision_pipeline_small"/>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01")

       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Visual")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showVisualModels hideBehaviorModels showCollisionModels hideMappings hideForceFields")
       root.addObject('MeshOBJLoader', name="torus_loader", filename="mesh/torus.obj")

       fixed_torus_and_falling_sphere_1 = root.addChild('FixedTorusAndFallingSphere_1')

       falling_sphere = FixedTorusAndFallingSphere_1.addChild('FallingSphere')

       falling_sphere.addObject('EulerImplicitSolver', name="odesolver")
       falling_sphere.addObject('CGLinearSolver', name="linear_solver", iterations="250", tolerance="1.0e-9", threshold="1.0e-9")
       falling_sphere.addObject('MechanicalObject', name="rigid", template="Rigid3d", position="-5 10 0 0 0 0 1")
       falling_sphere.addObject('UniformMass', totalMass="1.0")

       collision = FallingSphere.addChild('Collision')

       collision.addObject('MechanicalObject', name="collision_rigid")
       collision.addObject('SphereCollisionModel', name="sphere", radius="1", contactStiffness="1")
       collision.addObject('IdentityMapping', input="@../rigid", output="@collision_rigid")

       fixed_torus = FixedTorusAndFallingSphere_1.addChild('FixedTorus')

       collision = FixedTorus.addChild('Collision')

       collision.addObject('MechanicalObject', name="collision_torus", src="@../../../torus_loader", translation="-5 0 0", scale3d="0.8 0.8 0.8")
       collision.addObject('MeshTopology', name="topology", src="@../../../torus_loader")
       collision.addObject('TriangleCollisionModel', name="triangle_collision", simulated="0", moving="0", contactStiffness="1")
       collision.addObject('LineCollisionModel', name="line_collision", simulated="0", moving="0", contactStiffness="1")
       collision.addObject('PointCollisionModel', name="point_collision", simulated="0", moving="0", contactStiffness="1")

       fixed_torus_and_falling_sphere_2 = root.addChild('FixedTorusAndFallingSphere_2')

       falling_sphere = FixedTorusAndFallingSphere_2.addChild('FallingSphere')

       falling_sphere.addObject('EulerImplicitSolver', name="odesolver")
       falling_sphere.addObject('CGLinearSolver', name="linear_solver", iterations="250", tolerance="1.0e-9", threshold="1.0e-9")
       falling_sphere.addObject('MechanicalObject', name="rigid", template="Rigid3d", position="5 10 0 0 0 0 1")
       falling_sphere.addObject('UniformMass', totalMass="1.0")

       collision = FallingSphere.addChild('Collision')

       collision.addObject('MechanicalObject', name="collision_rigid")
       collision.addObject('SphereCollisionModel', name="sphere", radius="0.7", contactStiffness="1")
       collision.addObject('IdentityMapping', input="@../rigid", output="@collision_rigid")

       fixed_torus = FixedTorusAndFallingSphere_2.addChild('FixedTorus')

       collision = FixedTorus.addChild('Collision')

       collision.addObject('MechanicalObject', name="collision_torus", src="@../../../torus_loader", translation="5 0 0", scale3d="0.5 0.5 0.5")
       collision.addObject('MeshTopology', name="topology", src="@../../../torus_loader")
       collision.addObject('TriangleCollisionModel', name="triangle_collision", simulated="0", moving="0", contactStiffness="1")
       collision.addObject('LineCollisionModel', name="line_collision", simulated="0", moving="0", contactStiffness="1")
       collision.addObject('PointCollisionModel', name="point_collision", simulated="0", moving="0", contactStiffness="1")

       root.addObject('BruteForceBroadPhase', name="broad_phase_large")
       root.addObject('BVHNarrowPhase', name="narrow_phase_large")
       root.addObject('NewProximityIntersection', name="intersection_large", alarmDistance="5", contactDistance="1")
       root.addObject('CollisionResponse', name="response_large", response="PenalityContactForceField")
       root.addObject('SubCollisionPipeline', name="collision_pipeline_large", collisionModels="@/FixedTorusAndFallingSphere_1/FallingSphere/Collision/sphere         @FixedTorusAndFallingSphere_1/FixedTorus/Collision/triangle_collision @FixedTorusAndFallingSphere_1/FixedTorus/Collision/line_collision @FixedTorusAndFallingSphere_1/FixedTorus/Collision/point_collision", broadPhaseDetection="@broad_phase_large", narrowPhaseDetection="@narrow_phase_large", intersectionMethod="@intersection_large", contactManager="@response_large")
       root.addObject('BruteForceBroadPhase', name="broad_phase_small")
       root.addObject('BVHNarrowPhase', name="narrow_phase_small")
       root.addObject('NewProximityIntersection', name="intersection_small", alarmDistance="2.5", contactDistance="0.6")
       root.addObject('CollisionResponse', name="response_small", response="PenalityContactForceField")
       root.addObject('SubCollisionPipeline', name="collision_pipeline_small", collisionModels="@FixedTorusAndFallingSphere_2/FallingSphere/Collision/sphere          @FixedTorusAndFallingSphere_2/FixedTorus/Collision/triangle_collision @FixedTorusAndFallingSphere_2/FixedTorus/Collision/line_collision @FixedTorusAndFallingSphere_2/FixedTorus/Collision/point_collision", broadPhaseDetection="@broad_phase_small", narrowPhaseDetection="@narrow_phase_small", intersectionMethod="@intersection_small", contactManager="@response_small")
       root.addObject('CompositeCollisionPipeline', name="composite_pipeline", subCollisionPipelines="@collision_pipeline_large @collision_pipeline_small")
    ```

