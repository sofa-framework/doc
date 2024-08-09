---
title: FreeMotionAnimationLoop
---

FreeMotionAnimationLoop
=======================

This component belongs to the category of [AnimationLoop](../../../simulation-principles/animation-loop/).

The FreeMotionAnimationLoop is the component that rules the simulation in two main steps: a free motion, then a correction step. First, the free motion computes the projective constraints, the physics, solving the resulting free linear system. Second, the correction step solves the constraints based on the Lagrange multipliers. More information on the constraint resolution can be found [here](../../../simulation-principles/constraint/lagrange-constraint/).

<a href="https://github.com/sofa-framework/doc/blob/master/images/animationloop/FreeMotionAnimationLoop.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/animationloop/FreeMotionAnimationLoop.png?raw=true" title="Flow diagram for a FreeMotionAnimationLoop"/></a>


Usage
-----

The FreeMotionAnimationLoop must be used specifically for constraint resolution based on the Lagrange multiplier. It therefore **requires**:

- a [ConstraintSolver](../../../simulation-principles/constraint/lagrange-constraint/#constraintsolver-in-sofa). If no constraint solver can be found, a LCPConstraintSolver is automatically created by default.

Note that one or multiple [ConstraintCorrection](../../../simulation-principles/constraint/lagrange-constraint/#constraintcorrection) may be required by the [ConstraintSolver](../../../simulation-principles/constraint/lagrange-constraint/#constraintsolver-in-sofa).

<!-- automatically generated doc START -->
<!-- generate_doc -->


The animation loop to use with constraints.
You must add this loop at the beginning of the scene if you are using constraints."


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
		<td>computeBoundingBox</td>
		<td>
If true, compute the global bounding box of the scene at each time step. Used mostly for rendering.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>solveVelocityConstraintFirst</td>
		<td>
solve separately velocity constraint violations before position constraint violations
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>threadSafeVisitor</td>
		<td>
If true, do not use realloc and free visitors in fwdInteractionForceField.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Multithreading</td>
	</tr>
	<tr>
		<td>parallelCollisionDetectionAndFreeMotion</td>
		<td>
If true, executes free motion step and collision detection step in parallel.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>parallelODESolving</td>
		<td>
If true, solves all the ODEs in parallel during the free motion step.
		</td>
		<td>0</td>
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
|constraintSolver|The ConstraintSolver used in this animation loop (required)|ConstraintSolver|

## Examples 

FreeMotionAnimationLoop.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <!--
    WARNING: this scene uses a PrecomputedConstraintCorrection which has a heavy initialization step. It may take some time
    to load the scene. To cache the result, set the recompute Data of PrecomputedConstraintCorrection to false.
    To speed up the collision detection, replace BVHNarrowPhase by ParallelBVHNarrowPhase located in the MultiThreading plugin.
    -->
    
    <Node name="root" dt="0.01" gravity="0 981 0">
        <RequiredPlugin name="Sofa.Component.AnimationLoop"/> <!-- Needed to use components [FreeMotionAnimationLoop] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [LocalMinDistance] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [PrecomputedConstraintCorrection UncoupledConstraintCorrection] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Solver"/> <!-- Needed to use components [LCPConstraintSolver] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <VisualStyle displayFlags="showBehaviorModels"/>
        <FreeMotionAnimationLoop parallelCollisionDetectionAndFreeMotion="true"/>
        <LCPConstraintSolver tolerance="1e-3" maxIt="1000"/>
        <CollisionPipeline depth="6" verbose="0" draw="0"/>
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <LocalMinDistance name="Proximity" alarmDistance="2.5" contactDistance="1.0" angleCone="0.0"/>
        <CollisionResponse name="Response" response="FrictionContactConstraint"/>
        <Node name="Torus1">
            <MeshOBJLoader filename="mesh/torus2_for_collision.obj" name="loader"/>
            <MeshTopology src="@loader"/>
            <MechanicalObject src="@loader" scale="5.0"/>
            <TriangleCollisionModel simulated="0" moving="0"/>
            <LineCollisionModel simulated="0" moving="0"/>
            <PointCollisionModel simulated="0" moving="0"/>
            <MeshOBJLoader name="meshLoader_0" filename="mesh/torus2.obj" scale="5.0" handleSeams="1" />
            <OglModel name="Visual" src="@meshLoader_0" color="0.5 0.5 0.5 1.0"/>
        </Node>
        <Node name="TorusFEM">
            <EulerImplicitSolver rayleighMass="0.01" rayleighStiffness="0.001"/>
            <CGLinearSolver iterations="15" threshold="1.0e-15" tolerance="1.0e-9"/>
            <!--<SparseLDLSolver />-->
            <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh"/>
            <MeshTopology src="@loader"/>
            <MechanicalObject src="@loader" dx="-12" dy="0" dz="0" rx="0" ry="0" rz="0" scale="5.0"/>
            <UniformMass totalMass="0.2"/>
            <TetrahedronFEMForceField name="FEM" youngModulus="60000" poissonRatio="0.48" computeGlobalMatrix="false" method="polar"/>
            <!--<LinearSolverConstraintCorrection />-->
            <PrecomputedConstraintCorrection rotations="true" recompute="true"/>
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_2" filename="mesh/torus.obj" scale="5.0" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_2" color="red" dx="-12" dy="0" dz="0" rx="0" ry="0" rz="0"/>
                <BarycentricMapping input="@.." output="@Visual"/>
            </Node>
            <Node name="Surf2">
                <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj"/>
                <MeshTopology src="@loader"/>
                <MechanicalObject src="@loader" dx="-12" dy="0" dz="0" rx="0" ry="0" rz="0" scale="5.0"/>
                <TriangleCollisionModel contactStiffness="0.1"/>
                <LineCollisionModel/>
                <PointCollisionModel/>
                <BarycentricMapping/>
            </Node>
        </Node>
        <Node name="Torus3">
            <EulerImplicitSolver/>
            <CGLinearSolver iterations="25" tolerance="1e-5" threshold="1e-5"/>
            <MechanicalObject template="Rigid3" scale="5.0" dx="-25" dy="0"/>
            <UniformMass filename="BehaviorModels/torus2.rigid" totalMass="0.02"/>
            <UncoupledConstraintCorrection/>
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_1" filename="mesh/torus2.obj" scale="5.0" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_1" color="1.0 0.5 0.25 1.0"/>
                <RigidMapping input="@.." output="@Visual"/>
            </Node>
            <Node name="Surf2">
                <MeshOBJLoader filename="mesh/torus2_for_collision.obj" name="loader"/>
                <MeshTopology src="@loader"/>
                <MechanicalObject src="@loader" scale="5.0"/>
                <TriangleCollisionModel/>
                <LineCollisionModel/>
                <PointCollisionModel/>
                <RigidMapping/>
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 981 0")

       root.addObject('RequiredPlugin', name="Sofa.Component.AnimationLoop")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Solver")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="showBehaviorModels")
       root.addObject('FreeMotionAnimationLoop', parallelCollisionDetectionAndFreeMotion="true")
       root.addObject('LCPConstraintSolver', tolerance="1e-3", maxIt="1000")
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('LocalMinDistance', name="Proximity", alarmDistance="2.5", contactDistance="1.0", angleCone="0.0")
       root.addObject('CollisionResponse', name="Response", response="FrictionContactConstraint")

       torus1 = root.addChild('Torus1')

       torus1.addObject('MeshOBJLoader', filename="mesh/torus2_for_collision.obj", name="loader")
       torus1.addObject('MeshTopology', src="@loader")
       torus1.addObject('MechanicalObject', src="@loader", scale="5.0")
       torus1.addObject('TriangleCollisionModel', simulated="0", moving="0")
       torus1.addObject('LineCollisionModel', simulated="0", moving="0")
       torus1.addObject('PointCollisionModel', simulated="0", moving="0")
       torus1.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus2.obj", scale="5.0", handleSeams="1")
       torus1.addObject('OglModel', name="Visual", src="@meshLoader_0", color="0.5 0.5 0.5 1.0")

       torus_fem = root.addChild('TorusFEM')

       torus_fem.addObject('EulerImplicitSolver', rayleighMass="0.01", rayleighStiffness="0.001")
       torus_fem.addObject('CGLinearSolver', iterations="15", threshold="1.0e-15", tolerance="1.0e-9")
       torus_fem.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
       torus_fem.addObject('MeshTopology', src="@loader")
       torus_fem.addObject('MechanicalObject', src="@loader", dx="-12", dy="0", dz="0", rx="0", ry="0", rz="0", scale="5.0")
       torus_fem.addObject('UniformMass', totalMass="0.2")
       torus_fem.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="60000", poissonRatio="0.48", computeGlobalMatrix="false", method="polar")
       torus_fem.addObject('PrecomputedConstraintCorrection', rotations="true", recompute="true")

       visu = TorusFEM.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/torus.obj", scale="5.0", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_2", color="red", dx="-12", dy="0", dz="0", rx="0", ry="0", rz="0")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusFEM.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="-12", dy="0", dz="0", rx="0", ry="0", rz="0", scale="5.0")
       surf2.addObject('TriangleCollisionModel', contactStiffness="0.1")
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       torus3 = root.addChild('Torus3')

       torus3.addObject('EulerImplicitSolver', )
       torus3.addObject('CGLinearSolver', iterations="25", tolerance="1e-5", threshold="1e-5")
       torus3.addObject('MechanicalObject', template="Rigid3", scale="5.0", dx="-25", dy="0")
       torus3.addObject('UniformMass', filename="BehaviorModels/torus2.rigid", totalMass="0.02")
       torus3.addObject('UncoupledConstraintCorrection', )

       visu = Torus3.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/torus2.obj", scale="5.0", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="1.0 0.5 0.25 1.0")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       surf2 = Torus3.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', filename="mesh/torus2_for_collision.obj", name="loader")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", scale="5.0")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('RigidMapping', )
    ```


<!-- automatically generated doc END -->
