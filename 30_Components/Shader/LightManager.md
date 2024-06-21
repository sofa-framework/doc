# LightManager

Manage a set of lights that can cast hard and soft shadows.Soft Shadows is done using Variance Shadow Mapping (http://developer.download.nvidia.com/SDK/10.5/direct3d/Source/VarianceShadowMapping/Doc/VarianceShadowMapping.pdf)


__Target__: `Sofa.GL.Component.Shader`

__namespace__: `#!c++ sofa::gl::component::shader`

__parents__: 

- `#!c++ VisualManager`

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
		<td>shadows</td>
		<td>
Enable Shadow in the scene. (default=0)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>softShadows</td>
		<td>
If Shadows enabled, Enable Variance Soft Shadow in the scene. (default=0)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>ambient</td>
		<td>
Ambient lights contribution (Vec4f)(default=[0.0f,0.0f,0.0f,0.0f])
</td>
		<td>0 0 0 1</td>
	</tr>
	<tr>
		<td>debugDraw</td>
		<td>
enable/disable drawing of lights shadow textures. (default=false)
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



## Examples

Component/Visual/LightManager.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.01" gravity="0 0 -10" showBoundingTree="0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="Sofa.GL.Component.Shader"/> <!-- Needed to use components [DirectionalLight LightManager PositionalLight SpotLight] -->
    
        <DefaultAnimationLoop/>
        <CollisionPipeline verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <MinProximityIntersection name="Proximity" alarmDistance="0.02" contactDistance="0.02" />
        <LightManager />
        <SpotLight name="light1" color="1 0 0" position="0.5 0.7 2" cutoff="25" exponent="1" />
        <PositionalLight name="light2" color="0 1 0" attenuation="0.1" position="0.5 -0.7 2" />
        <DirectionalLight name="light3" color="0 0 1" direction="1 1 0" />
        <include href="Objects/SaladBowl.xml" />
        <include href="Objects/TorusRigid.xml" scale="0.05" rx="30" ry="15" dz="1" />
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01", gravity="0 0 -10", showBoundingTree="0")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Shader")
        root.addObject('DefaultAnimationLoop')
        root.addObject('CollisionPipeline', verbose="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField")
        root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.02", contactDistance="0.02")
        root.addObject('LightManager')
        root.addObject('SpotLight', name="light1", color="1 0 0", position="0.5 0.7 2", cutoff="25", exponent="1")
        root.addObject('PositionalLight', name="light2", color="0 1 0", attenuation="0.1", position="0.5 -0.7 2")
        root.addObject('DirectionalLight', name="light3", color="0 0 1", direction="1 1 0")
        root.addObject('include', href="Objects/SaladBowl.xml")
        root.addObject('include', href="Objects/TorusRigid.xml", scale="0.05", rx="30", ry="15", dz="1")
    ```

