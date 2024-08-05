# RuleBasedContactManager

Create different response to the collisions based on a set of rules


__Target__: `Sofa.Component.Collision.Response.Contact`

__namespace__: `#!c++ sofa::component::collision::response::contact`

__parents__: 

- `#!c++ CollisionResponse`

__categories__: 

- CollisionAlgorithm

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
		<td>response</td>
		<td>
contact response class
</td>
		<td></td>
	</tr>
	<tr>
		<td>responseParams</td>
		<td>
contact response parameters (syntax: name1=value1&name2=value2&...)
</td>
		<td></td>
	</tr>
	<tr>
		<td>variables</td>
		<td>
Define a list of variables to be used inside the rules
</td>
		<td></td>
	</tr>
	<tr>
		<td>rules</td>
		<td>
Ordered list of rules, each with a triplet of strings.
The first two define either the name of the collision model, its group number, or * meaning any model.
The last string define the response algorithm to use for contacts matched by this rule.
Rules are applied in the order they are specified. If none match a given contact, the default response is used.

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

Component/Collision/Response/RuleBasedContactManager.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <!-- Mechanical RuleBasedContactManager Example -->
    <Node name="root" dt="0.01">
        <RequiredPlugin name="Sofa.Component.AnimationLoop"/> <!-- Needed to use components [FreeMotionAnimationLoop] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [LocalMinDistance] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [RuleBasedContactManager] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [UncoupledConstraintCorrection] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Solver"/> <!-- Needed to use components [GenericConstraintSolver] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
        <FreeMotionAnimationLoop />
    	<GenericConstraintSolver maxIterations="1000" tolerance="0.001"/>
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <LocalMinDistance name="Proximity" alarmDistance="1.5" contactDistance="1.0" angleCone="0.0" />
        <RuleBasedContactManager name="Response" response="FrictionContactConstraint" rules="default"/>
        
        <Node name="Torus1">
            <MeshOBJLoader filename="mesh/torus2_for_collision.obj" name="loader" />
            <MeshTopology src="@loader"/>
            <MechanicalObject src="@loader" scale="5.0" />
            <TriangleCollisionModel simulated="0" moving="0" name="Torus1Triangle" group="1" />
            <LineCollisionModel simulated="0" moving="0" name="Torus1Line" group="1" />
            <PointCollisionModel simulated="0" moving="0" name="Torus1Point" group="1" />
            <MeshOBJLoader name="meshLoader_2" filename="mesh/torus2.obj" scale="5.0" handleSeams="1" />
            <OglModel name="Visual" src="@meshLoader_2" color="0.5 0.5 0.5 1.0" />
        </Node>
    
        <Node name="Torus2">
            <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" tolerance="1e-5" threshold="1e-5"/>
            <MechanicalObject template="Rigid3" scale="5.0" dx="-12" dy="0" />
            <UniformMass filename="BehaviorModels/torus.rigid"/>
            <UncoupledConstraintCorrection />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_3" filename="mesh/torus.obj" scale="5.0" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_3" color="0.0 0.5 0.5 1.0" />
                <RigidMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Surf2">
                <MeshOBJLoader filename="mesh/torus_for_collision.obj" name="loader" />
                <MeshTopology src="@loader"/>
                <MechanicalObject src="@loader" scale="5.0" />
                <TriangleCollisionModel name="Torus2Triangle" group="2" />
                <LineCollisionModel name="Torus2Line" group="2" />
                <PointCollisionModel name="Torus2Point" group="2" />
                <RigidMapping />
            </Node>
        </Node>
    
        <Node name="Torus3">
            <EulerImplicitSolver rayleighStiffness="0.1" rayleighMass="0.1"/>
            <CGLinearSolver iterations="25" tolerance="1e-5" threshold="1e-5"/>
            <MechanicalObject template="Rigid3" scale="5.0" dx="-25" dy="0" />
            <UniformMass filename="BehaviorModels/torus2.rigid"/>
            <UncoupledConstraintCorrection />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_1" filename="mesh/torus2.obj" scale="5.0" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_1" color="1.0 0.5 0.25 1.0" />
                <RigidMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Surf2">
                <MeshOBJLoader filename="mesh/torus2_for_collision.obj" name="loader" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" scale="5.0" />
                <TriangleCollisionModel name="Torus3Triangle" group="3" />
                <LineCollisionModel name="Torus3Line" group="3" />
                <PointCollisionModel name="Torus3Point" group="3" />
                <RigidMapping />
            </Node>
        </Node>
    	
        <Node name="Torus4">
            <EulerImplicitSolver rayleighStiffness="0.1" rayleighMass="0.1"/>
            <CGLinearSolver iterations="25" tolerance="1e-5" threshold="1e-5"/>
            <MechanicalObject template="Rigid3" scale="5.0" dx="-38" dy="0" />
            <UniformMass filename="BehaviorModels/torus.rigid"/>
            <UncoupledConstraintCorrection />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/torus.obj" scale="5.0" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_0" color="0.0 0.5 0.5 1.0" />
                <RigidMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Surf2">
                <MeshOBJLoader filename="mesh/torus_for_collision.obj" name="loader" />
                <MeshTopology src="@loader"/>
                <MechanicalObject src="@loader" scale="5.0" />
                <TriangleCollisionModel name="Torus4Triangle" group="4" />
                <LineCollisionModel name="Torus4Line" group="4" />
                <PointCollisionModel name="Torus4Point" group="4" />
                <RigidMapping />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01")
        root.addObject('RequiredPlugin', name="Sofa.Component.AnimationLoop")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Solver")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
        root.addObject('FreeMotionAnimationLoop')
        root.addObject('GenericConstraintSolver', maxIterations="1000", tolerance="0.001")
        root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('LocalMinDistance', name="Proximity", alarmDistance="1.5", contactDistance="1.0", angleCone="0.0")
        root.addObject('RuleBasedContactManager', name="Response", response="FrictionContactConstraint", rules="default")

        Torus1 = root.addChild('Torus1')
        Torus1.addObject('MeshOBJLoader', filename="mesh/torus2_for_collision.obj", name="loader")
        Torus1.addObject('MeshTopology', src="@loader")
        Torus1.addObject('MechanicalObject', src="@loader", scale="5.0")
        Torus1.addObject('TriangleCollisionModel', simulated="0", moving="0", name="Torus1Triangle", group="1")
        Torus1.addObject('LineCollisionModel', simulated="0", moving="0", name="Torus1Line", group="1")
        Torus1.addObject('PointCollisionModel', simulated="0", moving="0", name="Torus1Point", group="1")
        Torus1.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/torus2.obj", scale="5.0", handleSeams="1")
        Torus1.addObject('OglModel', name="Visual", src="@meshLoader_2", color="0.5 0.5 0.5 1.0")

        Torus2 = root.addChild('Torus2')
        Torus2.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
        Torus2.addObject('CGLinearSolver', iterations="25", tolerance="1e-5", threshold="1e-5")
        Torus2.addObject('MechanicalObject', template="Rigid3", scale="5.0", dx="-12", dy="0")
        Torus2.addObject('UniformMass', filename="BehaviorModels/torus.rigid")
        Torus2.addObject('UncoupledConstraintCorrection')

        Visu = Torus2.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/torus.obj", scale="5.0", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_3", color="0.0 0.5 0.5 1.0")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        Surf2 = Torus2.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', filename="mesh/torus_for_collision.obj", name="loader")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", scale="5.0")
        Surf2.addObject('TriangleCollisionModel', name="Torus2Triangle", group="2")
        Surf2.addObject('LineCollisionModel', name="Torus2Line", group="2")
        Surf2.addObject('PointCollisionModel', name="Torus2Point", group="2")
        Surf2.addObject('RigidMapping')

        Torus3 = root.addChild('Torus3')
        Torus3.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
        Torus3.addObject('CGLinearSolver', iterations="25", tolerance="1e-5", threshold="1e-5")
        Torus3.addObject('MechanicalObject', template="Rigid3", scale="5.0", dx="-25", dy="0")
        Torus3.addObject('UniformMass', filename="BehaviorModels/torus2.rigid")
        Torus3.addObject('UncoupledConstraintCorrection')

        Visu = Torus3.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/torus2.obj", scale="5.0", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="1.0 0.5 0.25 1.0")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        Surf2 = Torus3.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', filename="mesh/torus2_for_collision.obj", name="loader")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", scale="5.0")
        Surf2.addObject('TriangleCollisionModel', name="Torus3Triangle", group="3")
        Surf2.addObject('LineCollisionModel', name="Torus3Line", group="3")
        Surf2.addObject('PointCollisionModel', name="Torus3Point", group="3")
        Surf2.addObject('RigidMapping')

        Torus4 = root.addChild('Torus4')
        Torus4.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
        Torus4.addObject('CGLinearSolver', iterations="25", tolerance="1e-5", threshold="1e-5")
        Torus4.addObject('MechanicalObject', template="Rigid3", scale="5.0", dx="-38", dy="0")
        Torus4.addObject('UniformMass', filename="BehaviorModels/torus.rigid")
        Torus4.addObject('UncoupledConstraintCorrection')

        Visu = Torus4.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", scale="5.0", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="0.0 0.5 0.5 1.0")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        Surf2 = Torus4.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', filename="mesh/torus_for_collision.obj", name="loader")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", scale="5.0")
        Surf2.addObject('TriangleCollisionModel', name="Torus4Triangle", group="4")
        Surf2.addObject('LineCollisionModel', name="Torus4Line", group="4")
        Surf2.addObject('PointCollisionModel', name="Torus4Point", group="4")
        Surf2.addObject('RigidMapping')
    ```

