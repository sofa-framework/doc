<!-- generate_doc -->
# PointSplatModel

A simple visualization for a cloud of points.


__Target__: Sofa.GL.Component.Rendering3D

__namespace__: sofa::gl::component::rendering3d

__parents__:

- VisualModel

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
		<td>enable</td>
		<td>
Display the object or not
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
Radius of the spheres.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>textureSize</td>
		<td>
Size of the billboard texture.
		</td>
		<td>32</td>
	</tr>
	<tr>
		<td>alpha</td>
		<td>
Opacity of the billboards. 1.0 is 100% opaque.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>color</td>
		<td>
Billboard color.(default=[1.0,1.0,1.0,1.0])
		</td>
		<td>1 1 1 1</td>
	</tr>
	<tr>
		<td>pointData</td>
		<td>
scalar field modulating point colors
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

## Examples 

PointSplatModel.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <!-- Mechanical PointSplatModel Example -->
    <Node dt="0.005" gravity="0 -10 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [NewProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Forward"/> <!-- Needed to use components [RungeKutta4Solver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [PointSetTopologyContainer PointSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel PointSplatModel] -->
    
        <DefaultAnimationLoop/>
        <CollisionPipeline verbose="0" />
        <NewProximityIntersection alarmDistance="0.5" contactDistance="0.3" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <Node name="Fluid">
            <RungeKutta4Solver />
    		<MeshOBJLoader name="meshLoader" filename="mesh/dragon_clean.obj" scale3d="0.2 0.2 0.2"/>
            <PointSetTopologyContainer />
            <MechanicalObject name="MModel" position="@meshLoader.position"/>
    
    		<PointSetTopologyContainer name="con" />
            <PointSetTopologyModifier name="mod" />
    
            <UniformMass name="M1" vertexMass="1" />
            <!-- Visual model -->
            <PointSplatModel name="VModel" radius="0.25" alpha="0.1" color="cyan" />
    		<PointCollisionModel contactStiffness="100"  />
        </Node>
        <Node name="World">
            <MechanicalObject position="-4 -1.6 -4    4 -5.6 -4    4 -6.4 4    -4 -2.4 4" scale="1.075" />
            <MeshTopology triangles="0 1 2  0 2 3" />
            <TriangleCollisionModel contactStiffness="20" moving="false" simulated="false" />
            <LineCollisionModel contactStiffness="20" moving="false" simulated="false" />
            <PointCollisionModel contactStiffness="20" moving="false" simulated="false" />
            <OglModel name="VModel" color="blue" printLog="true" />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       node = root_node.addChild('node', dt="0.005", gravity="0 -10 0")

       node.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       node.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       node.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       node.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       node.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       node.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       node.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Forward")
       node.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       node.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       node.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       node.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       node.addObject('DefaultAnimationLoop', )
       node.addObject('CollisionPipeline', verbose="0")
       node.addObject('NewProximityIntersection', alarmDistance="0.5", contactDistance="0.3")
       node.addObject('BruteForceBroadPhase', )
       node.addObject('BVHNarrowPhase', )
       node.addObject('CollisionResponse', response="PenalityContactForceField")

       fluid = node.addChild('Fluid')

       fluid.addObject('RungeKutta4Solver', )
       fluid.addObject('MeshOBJLoader', name="meshLoader", filename="mesh/dragon_clean.obj", scale3d="0.2 0.2 0.2")
       fluid.addObject('PointSetTopologyContainer', )
       fluid.addObject('MechanicalObject', name="MModel", position="@meshLoader.position")
       fluid.addObject('PointSetTopologyContainer', name="con")
       fluid.addObject('PointSetTopologyModifier', name="mod")
       fluid.addObject('UniformMass', name="M1", vertexMass="1")
       fluid.addObject('PointSplatModel', name="VModel", radius="0.25", alpha="0.1", color="cyan")
       fluid.addObject('PointCollisionModel', contactStiffness="100")

       world = node.addChild('World')

       world.addObject('MechanicalObject', position="-4 -1.6 -4    4 -5.6 -4    4 -6.4 4    -4 -2.4 4", scale="1.075")
       world.addObject('MeshTopology', triangles="0 1 2  0 2 3")
       world.addObject('TriangleCollisionModel', contactStiffness="20", moving="false", simulated="false")
       world.addObject('LineCollisionModel', contactStiffness="20", moving="false", simulated="false")
       world.addObject('PointCollisionModel', contactStiffness="20", moving="false", simulated="false")
       world.addObject('OglModel', name="VModel", color="blue", printLog="true")
    ```

PointSplatModel.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <!-- Mechanical PointSplatModel Example -->
    <Node dt="0.005" gravity="0 -10 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [NewProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Forward"/> <!-- Needed to use components [RungeKutta4Solver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [PointSetTopologyContainer PointSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel PointSplatModel] -->
        <RequiredPlugin name="SofaSphFluid"/> <!-- Needed to use components [ParticleSink ParticleSource SPHFluidForceField SpatialGridContainer SpatialGridPointModel] -->
    
        <DefaultAnimationLoop/>
        <CollisionPipeline verbose="0" />
        <NewProximityIntersection alarmDistance="0.5" contactDistance="0.3" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <Node name="Fluid">
            <RungeKutta4Solver />
            <PointSetTopologyContainer />
            <MechanicalObject name="MModel" />
    
    		<PointSetTopologyContainer name="con" />
            <PointSetTopologyModifier name="mod" />
    		<ParticleSource name="Source" translation="0 3 0" radius="0.01 0.1 0.01" velocity="0 -20 0" delay="0.01875" start="-0.1" stop="2" 
            center="-0.375 0 -0.75 
                0.0 0.0 -0.75 
                0.375 0.0 -0.75 
                -0.75  0.0 -0.375 
                -0.375 0.0 -0.375 
                0.0 0.0 -0.375 
                0.375 0.0 -0.375 
                0.75 0.0 -0.375 
                -0.75 0.0 0.0 
                -0.375 0.0 0.0 
                0.0 0.0 0.0 
                0.375 0.0 0.0 
                0.75 0.0 0.0 
                -0.75 0.0 0.375 
                -0.375 0.0 0.375 
                0.0 0.0 0.375 
                0.375 0.0 0.375 
                0.75 0.0 0.375 
                -0.375 0.0 0.75 
                0.0 0.0 0.75 
                0.375 0.0 0.75"/> 
    		<ParticleSink normal="0 1 0" d0="-10" d1="-11" showPlane="true" printLog="true" />
    
            <UniformMass name="M1" vertexMass="1" />
            <SpatialGridContainer cellWidth="0.75" sortPoints="true" />
            <SPHFluidForceField radius="0.75" density="15" viscosity="10" pressure="1000" surfaceTension="-1000" />
            <!-- Visual model -->
            <PointSplatModel name="VModel" radius="0.5" alpha="0.04" color="cyan" />
            <!-- Collision model -->
            <SpatialGridPointModel contactStiffness="1000" />
        </Node>
        <Node name="World">
            <MechanicalObject position="-4 -1.6 -4    4 -5.6 -4    4 -6.4 4    -4 -2.4 4" scale="1.075" />
            <MeshTopology triangles="0 1 2  0 2 3" />
            <TriangleCollisionModel contactStiffness="20" moving="false" simulated="false" />
            <LineCollisionModel contactStiffness="20" moving="false" simulated="false" />
            <PointCollisionModel contactStiffness="20" moving="false" simulated="false" />
            <OglModel name="VModel" color="blue" printLog="true" />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       node = root_node.addChild('node', dt="0.005", gravity="0 -10 0")

       node.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       node.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       node.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       node.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       node.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       node.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Forward")
       node.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       node.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       node.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       node.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       node.addObject('RequiredPlugin', name="SofaSphFluid")
       node.addObject('DefaultAnimationLoop', )
       node.addObject('CollisionPipeline', verbose="0")
       node.addObject('NewProximityIntersection', alarmDistance="0.5", contactDistance="0.3")
       node.addObject('BruteForceBroadPhase', )
       node.addObject('BVHNarrowPhase', )
       node.addObject('CollisionResponse', response="PenalityContactForceField")

       fluid = node.addChild('Fluid')

       fluid.addObject('RungeKutta4Solver', )
       fluid.addObject('PointSetTopologyContainer', )
       fluid.addObject('MechanicalObject', name="MModel")
       fluid.addObject('PointSetTopologyContainer', name="con")
       fluid.addObject('PointSetTopologyModifier', name="mod")
       fluid.addObject('ParticleSource', name="Source", translation="0 3 0", radius="0.01 0.1 0.01", velocity="0 -20 0", delay="0.01875", start="-0.1", stop="2", center="-0.375 0 -0.75              0.0 0.0 -0.75              0.375 0.0 -0.75              -0.75  0.0 -0.375              -0.375 0.0 -0.375              0.0 0.0 -0.375              0.375 0.0 -0.375              0.75 0.0 -0.375              -0.75 0.0 0.0              -0.375 0.0 0.0              0.0 0.0 0.0              0.375 0.0 0.0              0.75 0.0 0.0              -0.75 0.0 0.375              -0.375 0.0 0.375              0.0 0.0 0.375              0.375 0.0 0.375              0.75 0.0 0.375              -0.375 0.0 0.75              0.0 0.0 0.75              0.375 0.0 0.75")
       fluid.addObject('ParticleSink', normal="0 1 0", d0="-10", d1="-11", showPlane="true", printLog="true")
       fluid.addObject('UniformMass', name="M1", vertexMass="1")
       fluid.addObject('SpatialGridContainer', cellWidth="0.75", sortPoints="true")
       fluid.addObject('SPHFluidForceField', radius="0.75", density="15", viscosity="10", pressure="1000", surfaceTension="-1000")
       fluid.addObject('PointSplatModel', name="VModel", radius="0.5", alpha="0.04", color="cyan")
       fluid.addObject('SpatialGridPointModel', contactStiffness="1000")

       world = node.addChild('World')

       world.addObject('MechanicalObject', position="-4 -1.6 -4    4 -5.6 -4    4 -6.4 4    -4 -2.4 4", scale="1.075")
       world.addObject('MeshTopology', triangles="0 1 2  0 2 3")
       world.addObject('TriangleCollisionModel', contactStiffness="20", moving="false", simulated="false")
       world.addObject('LineCollisionModel', contactStiffness="20", moving="false", simulated="false")
       world.addObject('PointCollisionModel', contactStiffness="20", moving="false", simulated="false")
       world.addObject('OglModel', name="VModel", color="blue", printLog="true")
    ```

