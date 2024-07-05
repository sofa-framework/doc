# SpotLight

A spot light illuminating the scene.The light has a location and a illumination cone restricting the directionstaken by the rays of light  (can cast shadows).


__Target__: `Sofa.GL.Component.Shader`

__namespace__: `#!c++ sofa::gl::component::shader`

__parents__: 

- `#!c++ PositionalLight`

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
		<td>color</td>
		<td>
Set the color of the light. (default=[1.0,1.0,1.0,1.0])
</td>
		<td>1 1 1 1</td>
	</tr>
	<tr>
		<td>shadowTextureSize</td>
		<td>
[Shadowing] Set size for shadow texture 
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>zNear</td>
		<td>
[Shadowing] Light's ZNear
</td>
		<td></td>
	</tr>
	<tr>
		<td>zFar</td>
		<td>
[Shadowing] Light's ZFar
</td>
		<td></td>
	</tr>
	<tr>
		<td>shadowsEnabled</td>
		<td>
[Shadowing] Enable Shadow from this light
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>softShadows</td>
		<td>
[Shadowing] Turn on Soft Shadow from this light
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>shadowFactor</td>
		<td>
[Shadowing] Shadow Factor (decrease/increase darkness)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>VSMLightBleeding</td>
		<td>
[Shadowing] (VSM only) Light bleeding paramter
</td>
		<td>0.05</td>
	</tr>
	<tr>
		<td>VSMMinVariance</td>
		<td>
[Shadowing] (VSM only) Minimum variance parameter
</td>
		<td>0.001</td>
	</tr>
	<tr>
		<td>textureUnit</td>
		<td>
[Shadowing] Texture unit for the genereated shadow texture
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>modelViewMatrix</td>
		<td>
[Shadowing] ModelView Matrix
</td>
		<td></td>
	</tr>
	<tr>
		<td>projectionMatrix</td>
		<td>
[Shadowing] Projection Matrix
</td>
		<td></td>
	</tr>
	<tr>
		<td>fixed</td>
		<td>
Fix light position from the camera
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Set the position of the light
</td>
		<td>-0.7 0.3 0</td>
	</tr>
	<tr>
		<td>attenuation</td>
		<td>
Set the attenuation of the light
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>direction</td>
		<td>
Set the direction of the light
</td>
		<td>0 0 -1</td>
	</tr>
	<tr>
		<td>cutoff</td>
		<td>
Set the angle (cutoff) of the spot
</td>
		<td>30</td>
	</tr>
	<tr>
		<td>exponent</td>
		<td>
Set the exponent of the spot
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>lookat</td>
		<td>
If true, direction specify the point at which the spotlight should be pointed to
</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawSource</td>
		<td>
Draw Light Source
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

Component/Visual/SpotLight.scn

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
        <RequiredPlugin name="Sofa.GL.Component.Shader"/> <!-- Needed to use components [LightManager SpotLight] -->
    
        <DefaultAnimationLoop/>
        <CollisionPipeline verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <MinProximityIntersection name="Proximity" alarmDistance="0.02" contactDistance="0.02" />
        <LightManager />
        <SpotLight name="light1" color="1 0 0" position="0.5 0.7 2" cutoff="25" exponent="1" drawSource="false" />
        <SpotLight name="light2" color="0 1 0" position="0.5 -0.7 2" cutoff="25" exponent="1"  drawSource="false"/>
        <SpotLight name="light3" color="0 0 1" position="-0.8 0 2" cutoff="25" exponent="1"  drawSource="false"/>
        <SpotLight name="light4" color="1 1 1" position="0 0 2" cutoff="10" exponent="1000" drawSource="false" />
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
        root.addObject('SpotLight', name="light1", color="1 0 0", position="0.5 0.7 2", cutoff="25", exponent="1", drawSource="false")
        root.addObject('SpotLight', name="light2", color="0 1 0", position="0.5 -0.7 2", cutoff="25", exponent="1", drawSource="false")
        root.addObject('SpotLight', name="light3", color="0 0 1", position="-0.8 0 2", cutoff="25", exponent="1", drawSource="false")
        root.addObject('SpotLight', name="light4", color="1 1 1", position="0 0 2", cutoff="10", exponent="1000", drawSource="false")
        root.addObject('include', href="Objects/SaladBowl.xml")
        root.addObject('include', href="Objects/TorusRigid.xml", scale="0.05", rx="30", ry="15", dz="1")
    ```

