---
title: MultiStepAnimationLoop
---

MultiStepAnimationLoop
======================

This component belongs to the category of [AnimationLoop](../../../simulation-principles/animation-loop/).

The MultiStepAnimationLoop derives from the [DefaultAnimationLoop](../../../components/animationloop/defaultanimationloop/). This animation loop is different due to the fact that it allows - at each iteration - for running several collision (_collisionSteps_), and within each of these collision steps, several integration sub-steps can be computed (_integrationSteps_).

<a href="https://github.com/sofa-framework/doc/blob/master/images/animationloop/MultiStepAnimationLoop.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/animationloop/MultiStepAnimationLoop.png?raw=true" title="Flow diagram for a MultiStepAnimationLoop"/></a>


Usage
-----

The MultiStepAnimationLoop has **no pre-requisite**.

Note that this MultiStepAnimationLoop does not handle constraints solved using [Lagrange multipliers](../../../simulation-principles/constraint/lagrange-constraint/).
<!-- automatically generated doc START -->
<!-- generate_doc -->

Multi steps animation loop, multi integration steps in a single animation step are managed.


__Target__: Sofa.Component.AnimationLoop

__namespace__: sofa::component::animationloop

__parents__:

- BaseAnimationLoop

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
		<td>computeBoundingBox</td>
		<td>
If true, compute the global bounding box of the scene at each time step. Used mostly for rendering.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>collisionSteps</td>
		<td>
number of collision steps between each frame rendering
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>integrationSteps</td>
		<td>
number of integration steps between each collision detection
		</td>
		<td>1</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|targetNode|Link to the scene's node that will be processed by the loop|BaseNode|

## Examples 

MultiStepAnimationLoop.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="1.0">
        <RequiredPlugin name="Sofa.Component.AnimationLoop"/> <!-- Needed to use components [MultiStepAnimationLoop] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [NewProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <NewProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <MultiStepAnimationLoop collisionSteps="20" integrationSteps="4" />
        <Node name="ChainRigid">
            <Node name="TorusFixed">
                <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <MeshOBJLoader name="meshLoader_4" filename="mesh/torus2.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_4" color="gray" />
            </Node>
            <Node name="TorusRigid-1">
                <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver iterations="25" threshold="0.000000000001" tolerance="0.000001" />
                <MechanicalObject template="Rigid3" dx="2.5" />
                <UniformMass totalMass="1.0"/>
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_3" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_3" color="gray" />
                    <RigidMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <RigidMapping />
                </Node>
            </Node>
            <Node name="TorusRigid-2">
                <EulerImplicitSolver />
                <CGLinearSolver iterations="25" threshold="0.000000000001" tolerance="0.000001" />
                <MechanicalObject template="Rigid3" dx="5" />
                <UniformMass totalMass="1.0"/>
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_0" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_0" color="gray" />
                    <RigidMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <RigidMapping />
                </Node>
            </Node>
            <Node name="TorusRigid-3">
                <EulerImplicitSolver />
                <CGLinearSolver iterations="25" threshold="0.000000000001" tolerance="0.000001" />
                <MechanicalObject template="Rigid3" dx="7.5" />
                <UniformMass totalMass="1.0"/>
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_1" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_1" color="gray" />
                    <RigidMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <RigidMapping />
                </Node>
            </Node>
            <Node name="TorusRigid-4">
                <EulerImplicitSolver />
                <CGLinearSolver iterations="25" threshold="0.000000000001" tolerance="0.000001" />
                <MechanicalObject template="Rigid3" dx="10" />
                <UniformMass totalMass="1.0"/>
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_2" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_2" color="gray" />
                    <RigidMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <RigidMapping />
                </Node>
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="1.0")

       root.addObject('RequiredPlugin', name="Sofa.Component.AnimationLoop")
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
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('NewProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")
       root.addObject('MultiStepAnimationLoop', collisionSteps="20", integrationSteps="4")

       chain_rigid = root.addChild('ChainRigid')

       torus_fixed = ChainRigid.addChild('TorusFixed')

       torus_fixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       torus_fixed.addObject('MeshTopology', src="@loader")
       torus_fixed.addObject('MechanicalObject', src="@loader")
       torus_fixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('MeshOBJLoader', name="meshLoader_4", filename="mesh/torus2.obj", handleSeams="1")
       torus_fixed.addObject('OglModel', name="Visual", src="@meshLoader_4", color="gray")

       torus_rigid_1 = ChainRigid.addChild('TorusRigid-1')

       torus_rigid_1.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
       torus_rigid_1.addObject('CGLinearSolver', iterations="25", threshold="0.000000000001", tolerance="0.000001")
       torus_rigid_1.addObject('MechanicalObject', template="Rigid3", dx="2.5")
       torus_rigid_1.addObject('UniformMass', totalMass="1.0")

       visu = TorusRigid-1.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_3", color="gray")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       surf2 = TorusRigid-1.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('RigidMapping', )

       torus_rigid_2 = ChainRigid.addChild('TorusRigid-2')

       torus_rigid_2.addObject('EulerImplicitSolver', )
       torus_rigid_2.addObject('CGLinearSolver', iterations="25", threshold="0.000000000001", tolerance="0.000001")
       torus_rigid_2.addObject('MechanicalObject', template="Rigid3", dx="5")
       torus_rigid_2.addObject('UniformMass', totalMass="1.0")

       visu = TorusRigid-2.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus2.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="gray")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       surf2 = TorusRigid-2.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('RigidMapping', )

       torus_rigid_3 = ChainRigid.addChild('TorusRigid-3')

       torus_rigid_3.addObject('EulerImplicitSolver', )
       torus_rigid_3.addObject('CGLinearSolver', iterations="25", threshold="0.000000000001", tolerance="0.000001")
       torus_rigid_3.addObject('MechanicalObject', template="Rigid3", dx="7.5")
       torus_rigid_3.addObject('UniformMass', totalMass="1.0")

       visu = TorusRigid-3.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="gray")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       surf2 = TorusRigid-3.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('RigidMapping', )

       torus_rigid_4 = ChainRigid.addChild('TorusRigid-4')

       torus_rigid_4.addObject('EulerImplicitSolver', )
       torus_rigid_4.addObject('CGLinearSolver', iterations="25", threshold="0.000000000001", tolerance="0.000001")
       torus_rigid_4.addObject('MechanicalObject', template="Rigid3", dx="10")
       torus_rigid_4.addObject('UniformMass', totalMass="1.0")

       visu = TorusRigid-4.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/torus2.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_2", color="gray")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       surf2 = TorusRigid-4.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('RigidMapping', )
    ```


<!-- automatically generated doc END -->
