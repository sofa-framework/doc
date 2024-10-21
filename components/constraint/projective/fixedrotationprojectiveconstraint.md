<!-- generate_doc -->
# FixedRotationProjectiveConstraint

Prevents rotation around x or/and y or/and z axis


## Rigid3d

Templates:

- Rigid3d

__Target__: Sofa.Component.Constraint.Projective

__namespace__: sofa::component::constraint::projective

__parents__:

- ProjectiveConstraintSet

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
		<td>FixedXRotation</td>
		<td>
Prevent Rotation around X axis
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>FixedYRotation</td>
		<td>
Prevent Rotation around Y axis
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>FixedZRotation</td>
		<td>
Prevent Rotation around Z axis
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
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Rigid3d&gt;|

## Examples 

FixedRotationProjectiveConstraint.scn

=== "XML"

    ```xml
    <Node name="Root" gravity="0 -9.81 0" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint FixedRotationProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [JointSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showVisual showBehaviorModels showForceFields showCollision showMapping" />
        <CollisionPipeline name="DefaultCollisionPipeline" verbose="0" draw="0" depth="6" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="scene" gravity="0 -9.81 0">
            <EulerImplicitSolver name="cg_odesolver" printLog="0"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver template="GraphScattered" name="linear solver" iterations="25" tolerance="1e-12" threshold="1e-09" />
            <Node name="Rotation around Z axis not authorized" gravity="0 -9.81 0">
                <MechanicalObject template="Rigid3" name="default0" translation="0 0 0" rotation="0 0 0" restScale="1" position="0 0 0 0 0 0 1 1 0 0 0 0 0 1" />
                <FixedProjectiveConstraint template="Rigid3" name="default1" indices="0" />
                <FixedRotationProjectiveConstraint template="Rigid3" name="default2" FixedXRotation="0" FixedYRotation="0" FixedZRotation="1" />
                <UniformMass name="default3" showAxisSizeFactor="1" totalMass="1.0"/>
                <Node name="spring" gravity="0 -9.81 0">
                    <MechanicalObject template="Rigid3" name="default4" translation="0 0 0" rotation="0 0 0" restScale="1" position="0 0 0 0 0 0 1 -1 0 0 0 0 0 1" />
                    <UniformMass name="default54" showAxisSizeFactor="1" totalMass="1.0"/>
                    <RigidMapping template="Rigid3,Rigid3" name="default1" rigidIndexPerPoint="1 1" axisLength="0.001" />
                    <JointSpringForceField template="Rigid3" name="default5" spring="BEGIN_SPRING  0 1  KS_T 1e+06 100000  KS_R 0 1000  KS_B 100  END_SPRING&#x0A;" />
                </Node>
            </Node>
            <Node name="Rotation around Z axis is free" gravity="0 -9.81 0">
                <MechanicalObject template="Rigid3" name="default6" translation="0 0 0" rotation="0 0 0" restScale="1" position="3 0 0 0 0 0 1 4 0 0 0 0 0 1" />
                <FixedProjectiveConstraint template="Rigid3" name="default7" indices="0" />
                <UniformMass name="default54" showAxisSizeFactor="1" totalMass="1.0"/>
                <Node name="spring" gravity="0 -9.81 0">
                    <MechanicalObject template="Rigid3" name="default9" translation="0 0 0" rotation="0 0 0" restScale="1" position="0 0 0 0 0 0 1 -1 0 0 0 0 0 1" />
                    <UniformMass name="default10" showAxisSizeFactor="1" totalMass="1.0"/>
                    <RigidMapping template="Rigid3,Rigid3" name="default11" rigidIndexPerPoint="1 1" axisLength="0.001" />
                    <JointSpringForceField template="Rigid3" name="default12" spring="BEGIN_SPRING  0 1  END_SPRING&#x0A;" />
                </Node>
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('Root', gravity="0 -9.81 0", dt="0.02")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels showForceFields showCollision showMapping")
       root.addObject('CollisionPipeline', name="DefaultCollisionPipeline", verbose="0", draw="0", depth="6")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       scene = Root.addChild('scene', gravity="0 -9.81 0")

       scene.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="0", rayleighStiffness="0.1", rayleighMass="0.1")
       scene.addObject('CGLinearSolver', template="GraphScattered", name="linear solver", iterations="25", tolerance="1e-12", threshold="1e-09")

       rotation_around__z_axis_not_authorized = scene.addChild('Rotation around Z axis not authorized', gravity="0 -9.81 0")

       rotation_around__z_axis_not_authorized.addObject('MechanicalObject', template="Rigid3", name="default0", translation="0 0 0", rotation="0 0 0", restScale="1", position="0 0 0 0 0 0 1 1 0 0 0 0 0 1")
       rotation_around__z_axis_not_authorized.addObject('FixedProjectiveConstraint', template="Rigid3", name="default1", indices="0")
       rotation_around__z_axis_not_authorized.addObject('FixedRotationProjectiveConstraint', template="Rigid3", name="default2", FixedXRotation="0", FixedYRotation="0", FixedZRotation="1")
       rotation_around__z_axis_not_authorized.addObject('UniformMass', name="default3", showAxisSizeFactor="1", totalMass="1.0")

       spring = Rotation around Z axis not authorized.addChild('spring', gravity="0 -9.81 0")

       spring.addObject('MechanicalObject', template="Rigid3", name="default4", translation="0 0 0", rotation="0 0 0", restScale="1", position="0 0 0 0 0 0 1 -1 0 0 0 0 0 1")
       spring.addObject('UniformMass', name="default54", showAxisSizeFactor="1", totalMass="1.0")
       spring.addObject('RigidMapping', template="Rigid3,Rigid3", name="default1", rigidIndexPerPoint="1 1", axisLength="0.001")
       spring.addObject('JointSpringForceField', template="Rigid3", name="default5", spring="BEGIN_SPRING  0 1  KS_T 1e+06 100000  KS_R 0 1000  KS_B 100  END_SPRING
")

       rotation_around__z_axis_is_free = scene.addChild('Rotation around Z axis is free', gravity="0 -9.81 0")

       rotation_around__z_axis_is_free.addObject('MechanicalObject', template="Rigid3", name="default6", translation="0 0 0", rotation="0 0 0", restScale="1", position="3 0 0 0 0 0 1 4 0 0 0 0 0 1")
       rotation_around__z_axis_is_free.addObject('FixedProjectiveConstraint', template="Rigid3", name="default7", indices="0")
       rotation_around__z_axis_is_free.addObject('UniformMass', name="default54", showAxisSizeFactor="1", totalMass="1.0")

       spring = Rotation around Z axis is free.addChild('spring', gravity="0 -9.81 0")

       spring.addObject('MechanicalObject', template="Rigid3", name="default9", translation="0 0 0", rotation="0 0 0", restScale="1", position="0 0 0 0 0 0 1 -1 0 0 0 0 0 1")
       spring.addObject('UniformMass', name="default10", showAxisSizeFactor="1", totalMass="1.0")
       spring.addObject('RigidMapping', template="Rigid3,Rigid3", name="default11", rigidIndexPerPoint="1 1", axisLength="0.001")
       spring.addObject('JointSpringForceField', template="Rigid3", name="default12", spring="BEGIN_SPRING  0 1  END_SPRING
")
    ```

