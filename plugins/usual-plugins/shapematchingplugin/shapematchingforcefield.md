<!-- generate_doc -->
# ShapeMatchingForceField

Meshless deformations based on shape matching


## Vec3d

Templates:

- Vec3d

__Target__: ShapeMatchingPlugin

__namespace__: sofa::component::forcefield

__parents__:

- ForceField

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
		<td>stiffness</td>
		<td>
force stiffness
		</td>
		<td>500</td>
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
|rotationFinder|link to the rotation finder|ShapeMatchingRotationFinder&lt;Vec3d&gt;|

## Examples 

ShapeMatchingForceField.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase,BruteForceBroadPhase,CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel,PointCollisionModel,SphereCollisionModel,TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SceneUtility"/> <!-- Needed to use components [InfoComponent] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="ShapeMatchingPlugin"/> <!-- Needed to use components [ShapeMatchingForceField,ShapeMatchingRotationFinder] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <CollisionPipeline verbose="0" draw="0" />
        <BruteForceBroadPhase />
        <BVHNarrowPhase />
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="cubeFEM">
            <EulerImplicitSolver name="cg_odesolver" printLog="false" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshOBJLoader name="loader" filename="mesh/dragon.obj" />
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader" scale="1" dz="10" />
            <UniformMass totalMass="3" />
            <RotationFinder neighborhoodLevel="1" radius="0.1" />
            <ShapeMatchingForceField name="ShapeMatching" stiffness="100" />
            <MeshOBJLoader name="loader" filename="mesh/dragon.obj" />
            <Node name="Visu">
                <OglModel name="Visual" src="@../loader" color="red" dz="10" />
                <IdentityMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Surf">
                <MeshTopology src="@../loader" />
                <MechanicalObject src="@../loader" dz="10" />
                <SphereCollisionModel contactStiffness="10" radius="0.1"/>
                <IdentityMapping />
            </Node>
        </Node>
        <Node name="Floor">
            <MeshOBJLoader name="loader" filename="mesh/floor3.obj" />
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader" dy="-10" scale="1.75" />
            <TriangleCollisionModel name="FloorTriangle" simulated="0" moving="0" />
            <LineCollisionModel name="FloorLine" simulated="0" moving="0" />
            <PointCollisionModel name="FloorPoint" simulated="0" moving="0" />
            <OglModel name="FloorV" src="@loader" texturename="textures/brushed_metal.bmp" dy="-10" scale="1.75" />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SceneUtility")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('RequiredPlugin', name="ShapeMatchingPlugin")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
       root.addObject('CollisionPipeline', verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       cube_fem = root.addChild('cubeFEM')

       cube_fem.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       cube_fem.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       cube_fem.addObject('MeshOBJLoader', name="loader", filename="mesh/dragon.obj")
       cube_fem.addObject('MeshTopology', src="@loader")
       cube_fem.addObject('MechanicalObject', src="@loader", scale="1", dz="10")
       cube_fem.addObject('UniformMass', totalMass="3")
       cube_fem.addObject('RotationFinder', neighborhoodLevel="1", radius="0.1")
       cube_fem.addObject('ShapeMatchingForceField', name="ShapeMatching", stiffness="100")
       cube_fem.addObject('MeshOBJLoader', name="loader", filename="mesh/dragon.obj")

       visu = cubeFEM.addChild('Visu')

       visu.addObject('OglModel', name="Visual", src="@../loader", color="red", dz="10")
       visu.addObject('IdentityMapping', input="@..", output="@Visual")

       surf = cubeFEM.addChild('Surf')

       surf.addObject('MeshTopology', src="@../loader")
       surf.addObject('MechanicalObject', src="@../loader", dz="10")
       surf.addObject('SphereCollisionModel', contactStiffness="10", radius="0.1")
       surf.addObject('IdentityMapping', )

       floor = root.addChild('Floor')

       floor.addObject('MeshOBJLoader', name="loader", filename="mesh/floor3.obj")
       floor.addObject('MeshTopology', src="@loader")
       floor.addObject('MechanicalObject', src="@loader", dy="-10", scale="1.75")
       floor.addObject('TriangleCollisionModel', name="FloorTriangle", simulated="0", moving="0")
       floor.addObject('LineCollisionModel', name="FloorLine", simulated="0", moving="0")
       floor.addObject('PointCollisionModel', name="FloorPoint", simulated="0", moving="0")
       floor.addObject('OglModel', name="FloorV", src="@loader", texturename="textures/brushed_metal.bmp", dy="-10", scale="1.75")
    ```

