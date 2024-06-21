# PointSplatModel

A simple visualization for a cloud of points.


__Target__: `Sofa.GL.Component.Rendering3D`

__namespace__: `#!c++ sofa::gl::component::rendering3d`

__parents__: 

- `#!c++ VisualModel`

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

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|



## Examples

Component/Visual/PointSplatModel.scn

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
    def createScene(rootNode):

        rootNode = rootNode.addChild('rootNode', dt="0.005", gravity="0 -10 0")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Forward")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        rootNode.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        rootNode.addObject('DefaultAnimationLoop')
        rootNode.addObject('CollisionPipeline', verbose="0")
        rootNode.addObject('NewProximityIntersection', alarmDistance="0.5", contactDistance="0.3")
        rootNode.addObject('BruteForceBroadPhase')
        rootNode.addObject('BVHNarrowPhase')
        rootNode.addObject('CollisionResponse', response="PenalityContactForceField")

        Fluid = rootNode.addChild('Fluid')
        Fluid.addObject('RungeKutta4Solver')
        Fluid.addObject('MeshOBJLoader', name="meshLoader", filename="mesh/dragon_clean.obj", scale3d="0.2 0.2 0.2")
        Fluid.addObject('PointSetTopologyContainer')
        Fluid.addObject('MechanicalObject', name="MModel", position="@meshLoader.position")
        Fluid.addObject('PointSetTopologyContainer', name="con")
        Fluid.addObject('PointSetTopologyModifier', name="mod")
        Fluid.addObject('UniformMass', name="M1", vertexMass="1")
        Fluid.addObject('PointSplatModel', name="VModel", radius="0.25", alpha="0.1", color="cyan")
        Fluid.addObject('PointCollisionModel', contactStiffness="100")

        World = rootNode.addChild('World')
        World.addObject('MechanicalObject', position="-4 -1.6 -4    4 -5.6 -4    4 -6.4 4    -4 -2.4 4", scale="1.075")
        World.addObject('MeshTopology', triangles="0 1 2  0 2 3")
        World.addObject('TriangleCollisionModel', contactStiffness="20", moving="false", simulated="false")
        World.addObject('LineCollisionModel', contactStiffness="20", moving="false", simulated="false")
        World.addObject('PointCollisionModel', contactStiffness="20", moving="false", simulated="false")
        World.addObject('OglModel', name="VModel", color="blue", printLog="true")
    ```

