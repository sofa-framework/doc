# SpatialGridPointModel

Collision model which represents a set of points, spatially grouped using a SpatialGridContainer


__Target__: `SofaSphFluid`

__namespace__: `#!c++ sofa::component::collision`

__parents__: 

- `#!c++ PointCollisionModel`

__categories__: 

- CollisionModel

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
		<td>active</td>
		<td>
flag indicating if this collision model is active and should be included in default collision detections
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>moving</td>
		<td>
flag indicating if this object is changing position between iterations
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>simulated</td>
		<td>
flag indicating if this object is controlled by a simulation
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>selfCollision</td>
		<td>
flag indication if the object can self collide
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>proximity</td>
		<td>
Distance to the actual (visual) surface
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>contactStiffness</td>
		<td>
Contact stiffness
</td>
		<td>10</td>
	</tr>
	<tr>
		<td>contactFriction</td>
		<td>
Contact friction coefficient (dry or viscous or unused depending on the contact method)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>contactRestitution</td>
		<td>
Contact coefficient of restitution
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>contactResponse</td>
		<td>
if set, indicate to the ContactManager that this model should use the given class of contacts.
Note that this is only indicative, and in particular if both collision models specify a different class it is up to the manager to choose.
</td>
		<td></td>
	</tr>
	<tr>
		<td>color</td>
		<td>
color used to display the collision model if requested
</td>
		<td>1 0 0 1</td>
	</tr>
	<tr>
		<td>group</td>
		<td>
IDs of the groups containing this model. No collision can occur between collision models included in a common group (e.g. allowing the same object to have multiple collision models)
</td>
		<td></td>
	</tr>
	<tr>
		<td>numberOfContacts</td>
		<td>
Number of collision models this collision model is currently attached to
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>bothSide</td>
		<td>
activate collision on both side of the point model (when surface normals are defined on these points)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>computeNormals</td>
		<td>
activate computation of normal vectors (required for some collision detection algorithms)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>displayFreePosition</td>
		<td>
Display Collision Model Points free position(in green)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>leafScale</td>
		<td>
at which level should the first cube layer be constructed.
Note that this must not be greater than GRIDDIM_LOG2
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
|previous|Previous (coarser / upper / parent level) CollisionModel in the hierarchy.|
|next|Next (finer / lower / child level) CollisionModel in the hierarchy.|
|collisionElementActiver|CollisionElementActiver component that activates or deactivates collision element(s) during execution|
|topology|link to the topology container|



## Examples

SofaSphFluid/share/sofa/examples/SofaSphFluid/SpatialGridPointModel.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node dt="0.005" gravity="0 -10 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [NewProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Forward"/> <!-- Needed to use components [RungeKutta4Solver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="SofaSphFluid"/> <!-- Needed to use components [ParticleSink ParticleSource SPHFluidForceField SPHFluidSurfaceMapping SpatialGridContainer SpatialGridPointModel] -->
    
    
        <VisualStyle displayFlags="showVisual showBehaviorModels hideForceFields" />
        <DefaultAnimationLoop/>
        <CollisionPipeline verbose="0" />
        <NewProximityIntersection alarmDistance="0.5" contactDistance="0.3" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <Node name="Fluid">
            <RungeKutta4Solver />        
            <RegularGridTopology nx="5" ny="30" nz="5" xmin="-1.5" xmax="0" ymin="-3" ymax="9" zmin="-1.5" zmax="0" drawEdges="0"/>
            <MechanicalObject name="MModel" />
            <UniformMass name="M1" vertexMass="1" />
            <SpatialGridContainer cellWidth="0.75" sortPoints="true" />
            <SPHFluidForceField radius="0.745" density="15" viscosity="10" pressure="1000" surfaceTension="-1000" />
            <Node name="Visual">
                <OglModel name="VModel" color="blue" />
                <SPHFluidSurfaceMapping name="MarchingCube" input="@../MModel" output="@VModel" isoValue="0.5" radius="0.75" step="0.25" />
            </Node>
            <SpatialGridPointModel contactStiffness="1000" />
        </Node>
        <Node name="World">
            <MechanicalObject position="&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;    -4 -1.6 -4    4 -5.6 -4    4 -6.4 4    -4 -2.4 4&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;    -4 -1.6 -4    -4 -1.5 -4    4 -1.5 -4    4 -5.6 -4&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;    4 -5.6 -4    4 -1.5 -4    4 -1.5 4    4 -6.4 4&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;    4 -6.4 4    4 -1.5 4    -4 -1.5 4    -4 -2.4 4&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;    -4 -2.4 4    -4 -1.5 4    -4 -1.5 -4    -4 -1.6 -4&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;    " scale="1.075" />
            <MeshTopology triangles="0 1 2  0 2 3    4 5 6  4 6 7    8 9 10  8 10 11    12 13 14  12 14 15    16 17 18  16 18 19" />
            <TriangleCollisionModel contactStiffness="20" moving="false" simulated="false" />
            <LineCollisionModel contactStiffness="20" moving="false" simulated="false" />
            <PointCollisionModel contactStiffness="20" moving="false" simulated="false" />
            <OglModel name="VModel" color="0.95 1.0 0.95 0.25" printLog="false" />
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        rootNode = rootNode.addChild('rootNode', dt="0.005", gravity="0 -10 0")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Forward")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        rootNode.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        rootNode.addObject('RequiredPlugin', name="SofaSphFluid")
        rootNode.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels hideForceFields")
        rootNode.addObject('DefaultAnimationLoop')
        rootNode.addObject('CollisionPipeline', verbose="0")
        rootNode.addObject('NewProximityIntersection', alarmDistance="0.5", contactDistance="0.3")
        rootNode.addObject('BruteForceBroadPhase')
        rootNode.addObject('BVHNarrowPhase')
        rootNode.addObject('CollisionResponse', response="PenalityContactForceField")

        Fluid = rootNode.addChild('Fluid')
        Fluid.addObject('RungeKutta4Solver')
        Fluid.addObject('RegularGridTopology', nx="5", ny="30", nz="5", xmin="-1.5", xmax="0", ymin="-3", ymax="9", zmin="-1.5", zmax="0", drawEdges="0")
        Fluid.addObject('MechanicalObject', name="MModel")
        Fluid.addObject('UniformMass', name="M1", vertexMass="1")
        Fluid.addObject('SpatialGridContainer', cellWidth="0.75", sortPoints="true")
        Fluid.addObject('SPHFluidForceField', radius="0.745", density="15", viscosity="10", pressure="1000", surfaceTension="-1000")

        Visual = Fluid.addChild('Visual')
        Visual.addObject('OglModel', name="VModel", color="blue")
        Visual.addObject('SPHFluidSurfaceMapping', name="MarchingCube", input="@../MModel", output="@VModel", isoValue="0.5", radius="0.75", step="0.25")
        Fluid.addObject('SpatialGridPointModel', contactStiffness="1000")

        World = rootNode.addChild('World')
        World.addObject('MechanicalObject', position="
						    -4 -1.6 -4    4 -5.6 -4    4 -6.4 4    -4 -2.4 4
						    -4 -1.6 -4    -4 -1.5 -4    4 -1.5 -4    4 -5.6 -4
						    4 -5.6 -4    4 -1.5 -4    4 -1.5 4    4 -6.4 4
						    4 -6.4 4    4 -1.5 4    -4 -1.5 4    -4 -2.4 4
						    -4 -2.4 4    -4 -1.5 4    -4 -1.5 -4    -4 -1.6 -4
						    ", scale="1.075")
        World.addObject('MeshTopology', triangles="0 1 2  0 2 3    4 5 6  4 6 7    8 9 10  8 10 11    12 13 14  12 14 15    16 17 18  16 18 19")
        World.addObject('TriangleCollisionModel', contactStiffness="20", moving="false", simulated="false")
        World.addObject('LineCollisionModel', contactStiffness="20", moving="false", simulated="false")
        World.addObject('PointCollisionModel', contactStiffness="20", moving="false", simulated="false")
        World.addObject('OglModel', name="VModel", color="0.95 1.0 0.95 0.25", printLog="false")
    ```

