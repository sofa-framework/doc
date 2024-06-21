# ParabolicProjectiveConstraint

Apply a parabolic trajectory to given points


__Templates__:

- `#!c++ Rigid3d`
- `#!c++ Vec3d`

__Target__: `Sofa.Component.Constraint.Projective`

__namespace__: `#!c++ sofa::component::constraint::projective`

__parents__: 

- `#!c++ ProjectiveConstraintSet`

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
		<td>group</td>
		<td>
ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>endTime</td>
		<td>
The constraint stops acting after the given value.
Use a negative value for infinite constraints
</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
Indices of the constrained points
</td>
		<td></td>
	</tr>
	<tr>
		<td>P1</td>
		<td>
first point of the parabol
</td>
		<td></td>
	</tr>
	<tr>
		<td>P2</td>
		<td>
second point of the parabol
</td>
		<td></td>
	</tr>
	<tr>
		<td>P3</td>
		<td>
third point of the parabol
</td>
		<td></td>
	</tr>
	<tr>
		<td>BeginTime</td>
		<td>
Begin Time of the motion
</td>
		<td></td>
	</tr>
	<tr>
		<td>EndTime</td>
		<td>
End Time of the motion
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
|mechanicalStates|List of mechanical states to which this component is associated|
|mstate|MechanicalState used by this component|
|topology|link to the topology container|



## Examples

Component/Constraint/Projective/ParabolicProjectiveConstraint.scn

=== "XML"

    ```xml
    <Node dt="0.01" multiThreadSimulation="0" name="root" time="0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [NewProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [SphereCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [ParabolicProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader SphereLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showVisual showBehaviorModels" />
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <NewProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="LiverParabolic">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject template="Rigid3" name="DOFs" position="0 0 0 0 0 0 1" />
            <UniformMass name="mass" totalMass="1" showAxisSizeFactor="0.1" />
            <ParabolicProjectiveConstraint name="parabol" indices="0" P1="1 0 0" P2="5 3 1" P3="7 6 -5" BeginTime="0.5" EndTime="1.5" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_1" filename="mesh/liver-smooth.obj" handleSeams="1" />
                <OglModel name="VisualModel" src="@meshLoader_1" color="red" />
                <RigidMapping input="@.." output="@VisualModel" name="visual mapping" />
            </Node>
            <Node name="Surf">
    	    <SphereLoader filename="mesh/liver.sph" />
                <MechanicalObject position="@[-1].position" />
                <SphereCollisionModel name="CollisionModel" listRadius="@[-2].listRadius" />
                <RigidMapping name="sphere mapping" />
            </Node>
        </Node>
        <Node name="CubeFixed">
            <MeshOBJLoader name="loader" filename="mesh/cube.obj" />
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader" scale="20" dz="-35" />
            <TriangleCollisionModel simulated="0" moving="0" />
            <MeshOBJLoader name="meshLoader_0" filename="mesh/cube.obj" scale="20" handleSeams="1" />
            <OglModel name="Visual" src="@meshLoader_0" color="gray" dz="-35" />
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01", multiThreadSimulation="0", time="0")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')
        root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels")
        root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('NewProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
        root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

        LiverParabolic = root.addChild('LiverParabolic')
        LiverParabolic.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        LiverParabolic.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        LiverParabolic.addObject('MechanicalObject', template="Rigid3", name="DOFs", position="0 0 0 0 0 0 1")
        LiverParabolic.addObject('UniformMass', name="mass", totalMass="1", showAxisSizeFactor="0.1")
        LiverParabolic.addObject('ParabolicProjectiveConstraint', name="parabol", indices="0", P1="1 0 0", P2="5 3 1", P3="7 6 -5", BeginTime="0.5", EndTime="1.5")

        Visu = LiverParabolic.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/liver-smooth.obj", handleSeams="1")
        Visu.addObject('OglModel', name="VisualModel", src="@meshLoader_1", color="red")
        Visu.addObject('RigidMapping', input="@..", output="@VisualModel", name="visual mapping")

        Surf = LiverParabolic.addChild('Surf')
        Surf.addObject('SphereLoader', filename="mesh/liver.sph")
        Surf.addObject('MechanicalObject', position="@[-1].position")
        Surf.addObject('SphereCollisionModel', name="CollisionModel", listRadius="@[-2].listRadius")
        Surf.addObject('RigidMapping', name="sphere mapping")

        CubeFixed = root.addChild('CubeFixed')
        CubeFixed.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj")
        CubeFixed.addObject('MeshTopology', src="@loader")
        CubeFixed.addObject('MechanicalObject', src="@loader", scale="20", dz="-35")
        CubeFixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
        CubeFixed.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/cube.obj", scale="20", handleSeams="1")
        CubeFixed.addObject('OglModel', name="Visual", src="@meshLoader_0", color="gray", dz="-35")
    ```

