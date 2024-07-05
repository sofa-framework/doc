# SlidingLagrangianConstraint

TODO-SlidingLagrangianConstraint


__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.Component.Constraint.Lagrangian.Model`

__namespace__: `#!c++ sofa::component::constraint::lagrangian::model`

__parents__: 

- `#!c++ PairInteractionConstraint`

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
		<td>constraintIndex</td>
		<td>
Constraint index (first index in the right hand term resolution vector)
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
		<td>sliding_point</td>
		<td>
index of the spliding point on the first model
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>axis_1</td>
		<td>
index of one end of the sliding axis
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>axis_2</td>
		<td>
index of the other end of the sliding axis
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>force</td>
		<td>
force (impulse) used to solve the constraint
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
|object1|First object associated to this component|
|object2|Second object associated to this component|



## Examples

Component/Constraint/Lagrangian/SlidingLagrangianConstraint.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.001" gravity="0 -9.81 0">
        <RequiredPlugin name="Sofa.Component.AnimationLoop"/> <!-- Needed to use components [FreeMotionAnimationLoop] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [LocalMinDistance] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [UncoupledConstraintCorrection] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Model"/> <!-- Needed to use components [SlidingLagrangianConstraint] -->
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
        
        <VisualStyle displayFlags="showForceFields showVisual showBehavior" />
        <FreeMotionAnimationLoop />
        <GenericConstraintSolver maxIterations="1000" tolerance="0.001"/>
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <LocalMinDistance name="Proximity" alarmDistance="0.2" contactDistance="0.09" angleCone="0.0" />
        <CollisionResponse name="Response" response="FrictionContactConstraint" />
        <Node name="SlidingPoint">
            <MechanicalObject name="points" template="Vec3" position="1 1.25 -0.2 &#x09;1 1.25 0.2" free_position="1 1.25 -0.2 &#x09;1 1.25 0.2" />
        </Node>
        <Node name="CUBE_1">
            <EulerImplicitSolver printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject template="Rigid3" scale="1.0" dx="0.0" dy="0" dz="0.0" />
            <UniformMass totalMass="10.0" />
            <UncoupledConstraintCorrection />
            <Node name="Visu">
                <MeshOBJLoader name='myLoader1' filename='mesh/cube.obj'/>  
                <OglModel name="Visual1" src='@myLoader1' color="1 1 0 1.0" />
                <RigidMapping input="@.." output="@Visual1" />
            </Node>
            <Node name="ColliCube">
                <MeshTopology filename="mesh/cube.obj" />
                <MechanicalObject scale="1.0" />
                <TriangleCollisionModel contactStiffness="0.1" />
                <LineCollisionModel contactStiffness="0.1" />
                <PointCollisionModel contactStiffness="0.1" />
                <RigidMapping />
            </Node>
            <Node name="Constraints">
                <MechanicalObject name="points" template="Vec3" position="1 1.25 1&#x09;1 1.25 -1&#x09;0 0 0" />
                <RigidMapping />
            </Node>
        </Node>
        <SlidingLagrangianConstraint name="constraint1" object1="@SlidingPoint/points" object2="@CUBE_1/Constraints/points" sliding_point="0" axis_1="0" axis_2="1" />
        <Node name="Line">
            <MechanicalObject name="points" template="Vec3" position="6 1.25 1&#x09;6 1.25 -1" free_position="6 1.25 1&#x09;6 1.25 -1" />
        </Node>
        <Node name="CUBE_2">
            <EulerImplicitSolver printLog="false" />
            <CGLinearSolver iterations="25" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject template="Rigid3" scale="1.0" dx="5.0" dy="0" dz="0.0" />
            <UniformMass totalMass="10.0" />
            <UncoupledConstraintCorrection />
            <Node name="Visu">
                <MeshOBJLoader name='myLoader2' filename='mesh/cube.obj'/>  
                <OglModel name="Visual2" src='@myLoader2' color="1 1 0 1.0" />
                <RigidMapping input="@.." output="@Visual2" />
            </Node>
            <Node name="ColliCube">
                <MeshTopology filename="mesh/cube.obj" />
                <MechanicalObject scale="1.0" />
                <TriangleCollisionModel contactStiffness="0.1" />
                <LineCollisionModel contactStiffness="0.1" />
                <PointCollisionModel contactStiffness="0.1" />
                <RigidMapping />
            </Node>
            <Node name="Constraints">
                <MechanicalObject name="points" template="Vec3" position="1 1.25 1" />
                <RigidMapping />
            </Node>
        </Node>
        <SlidingLagrangianConstraint name="constraint2" object1="@CUBE_2/Constraints/points" object2="@Line/points" sliding_point="0" axis_1="0" axis_2="1" />
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.001", gravity="0 -9.81 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.AnimationLoop")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Model")
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
        root.addObject('VisualStyle', displayFlags="showForceFields showVisual showBehavior")
        root.addObject('FreeMotionAnimationLoop')
        root.addObject('GenericConstraintSolver', maxIterations="1000", tolerance="0.001")
        root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('LocalMinDistance', name="Proximity", alarmDistance="0.2", contactDistance="0.09", angleCone="0.0")
        root.addObject('CollisionResponse', name="Response", response="FrictionContactConstraint")

        SlidingPoint = root.addChild('SlidingPoint')
        SlidingPoint.addObject('MechanicalObject', name="points", template="Vec3", position="1 1.25 -0.2 	1 1.25 0.2", free_position="1 1.25 -0.2 	1 1.25 0.2")

        CUBE_1 = root.addChild('CUBE_1')
        CUBE_1.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        CUBE_1.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
        CUBE_1.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="0", dz="0.0")
        CUBE_1.addObject('UniformMass', totalMass="10.0")
        CUBE_1.addObject('UncoupledConstraintCorrection')

        Visu = CUBE_1.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="myLoader1", filename="mesh/cube.obj")
        Visu.addObject('OglModel', name="Visual1", src="@myLoader1", color="1 1 0 1.0")
        Visu.addObject('RigidMapping', input="@..", output="@Visual1")

        ColliCube = CUBE_1.addChild('ColliCube')
        ColliCube.addObject('MeshTopology', filename="mesh/cube.obj")
        ColliCube.addObject('MechanicalObject', scale="1.0")
        ColliCube.addObject('TriangleCollisionModel', contactStiffness="0.1")
        ColliCube.addObject('LineCollisionModel', contactStiffness="0.1")
        ColliCube.addObject('PointCollisionModel', contactStiffness="0.1")
        ColliCube.addObject('RigidMapping')

        Constraints = CUBE_1.addChild('Constraints')
        Constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1 1.25 1	1 1.25 -1	0 0 0")
        Constraints.addObject('RigidMapping')
        root.addObject('SlidingLagrangianConstraint', name="constraint1", object1="@SlidingPoint/points", object2="@CUBE_1/Constraints/points", sliding_point="0", axis_1="0", axis_2="1")

        Line = root.addChild('Line')
        Line.addObject('MechanicalObject', name="points", template="Vec3", position="6 1.25 1	6 1.25 -1", free_position="6 1.25 1	6 1.25 -1")

        CUBE_2 = root.addChild('CUBE_2')
        CUBE_2.addObject('EulerImplicitSolver', printLog="false")
        CUBE_2.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
        CUBE_2.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="5.0", dy="0", dz="0.0")
        CUBE_2.addObject('UniformMass', totalMass="10.0")
        CUBE_2.addObject('UncoupledConstraintCorrection')

        Visu = CUBE_2.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="myLoader2", filename="mesh/cube.obj")
        Visu.addObject('OglModel', name="Visual2", src="@myLoader2", color="1 1 0 1.0")
        Visu.addObject('RigidMapping', input="@..", output="@Visual2")

        ColliCube = CUBE_2.addChild('ColliCube')
        ColliCube.addObject('MeshTopology', filename="mesh/cube.obj")
        ColliCube.addObject('MechanicalObject', scale="1.0")
        ColliCube.addObject('TriangleCollisionModel', contactStiffness="0.1")
        ColliCube.addObject('LineCollisionModel', contactStiffness="0.1")
        ColliCube.addObject('PointCollisionModel', contactStiffness="0.1")
        ColliCube.addObject('RigidMapping')

        Constraints = CUBE_2.addChild('Constraints')
        Constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1 1.25 1")
        Constraints.addObject('RigidMapping')
        root.addObject('SlidingLagrangianConstraint', name="constraint2", object1="@CUBE_2/Constraints/points", object2="@Line/points", sliding_point="0", axis_1="0", axis_2="1")
    ```

