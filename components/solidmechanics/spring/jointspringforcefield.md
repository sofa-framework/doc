<!-- generate_doc -->
# JointSpringForceField

Springs for Rigids.


## Rigid3d

Templates:

- Rigid3d

__Target__: Sofa.Component.SolidMechanics.Spring

__namespace__: sofa::component::solidmechanics::spring

__parents__:

- PairInteractionForceField

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
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping - stiffness matrix coefficient
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>outfile</td>
		<td>
output file name
		</td>
		<td></td>
	</tr>
	<tr>
		<td>infile</td>
		<td>
input file containing constant joint force
		</td>
		<td></td>
	</tr>
	<tr>
		<td>period</td>
		<td>
period between outputs
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>reinit</td>
		<td>
flag enabling reinitialization of the output file at each timestep
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>spring</td>
		<td>
pairs of indices, stiffness, damping, rest length
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showLawfulTorsion</td>
		<td>
display the lawful part of the joint rotation
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showExtraTorsion</td>
		<td>
display the illicit part of the joint rotation
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showFactorSize</td>
		<td>
modify the size of the debug information of a given factor
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
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|object1|First object associated to this component|MechanicalState&lt;Rigid3d&gt;|
|object2|Second object associated to this component|MechanicalState&lt;Rigid3d&gt;|

## Examples 

JointSpringForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -9.81 0" dt="0.01" time="0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [JointSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showVisual showBehaviorModels showForceFields showCollisionModels showMechanicalMappings" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="default41" response="PenalityContactForceField" />
        <CollisionPipeline name="default42" />
        <MinProximityIntersection name="default43" alarmDistance="1" contactDistance="0.5"/>
        <Node name="default44" gravity="0 -9.81 0">
            <EulerImplicitSolver name="cg_odesolver" printLog="0"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver template="GraphScattered" name="linear solver" iterations="25" tolerance="1e-009" threshold="1e-009" />
            <MechanicalObject template="Rigid3" name="DOFs" position="0 0 0 0 0 0 1 1 0 0 0 0 0 1 3 0 0 0 0 0 1 5 0 0 0 0 0 1 7 0 0 0 0 0 1" velocity="0 0 0 0 0 0" force="0 0 0 0 0 0" externalForce="0 0 0 0 0 0" derivX="0 0 0 0 0 0" restScale="1" />
            <UniformMass name="mass" vertexMass="1 1 [1 0 0,0 1 0,0 0 1]" />
            <FixedProjectiveConstraint template="Rigid3" name="fixOrigin" indices="0" />
            <Node name="default45" gravity="0 -9.81 0">
                <MechanicalObject template="Rigid3" name="attaches" position="0 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914" velocity="0 0 0 0 0 0" force="0 0 0 0 0 0" externalForce="0 0 0 0 0 0" derivX="0 0 0 0 0 0" restScale="1" />
                <RigidMapping template="Rigid3,Rigid3" name="default46" input="@.." output="@." rigidIndexPerPoint="1 2 2 2 2" />
                <JointSpringForceField template="Rigid3" name="joint springs" spring="BEGIN_SPRING  0 1  FREE_AXIS 0 0 0 0 1 0  KS_T 0 30000  KS_R 0 200000  KD 1  R_LIM_X -0.8 0.8  R_LIM_Y -1.57 1.57  R_LIM_Z 0 0  END_SPRING&#x0A; BEGIN_SPRING  2 3  FREE_AXIS 0 0 0 0 1 0  KS_T 0 30000  KS_R 0 200000  KD 1  R_LIM_X -0.8 0.8  R_LIM_Y -1.57 1.57  R_LIM_Z 0 0  END_SPRING&#x0A; BEGIN_SPRING  4 5  FREE_AXIS 0 0 0 0 1 0  KS_T 0 30000  KS_R 0 200000  KD 1  R_LIM_X -0.8 0.8  R_LIM_Y -1.57 1.57  R_LIM_Z 0 0  END_SPRING&#x0A; BEGIN_SPRING  6 7  FREE_AXIS 0 0 0 0 1 0  KS_T 0 30000  KS_R 0 200000  KD 1  R_LIM_X -0.8 0.8  R_LIM_Y -1.57 1.57  R_LIM_Z 0 0  END_SPRING&#x0A;" />
            </Node>
            <Node name="Visu" gravity="0 -9.81 0">
                <OglModel template="Vec3" name="Visual" position="-1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5" vertices="-1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5" triangles="3 1 0  3 2 1  3 6 2  3 7 6  7 5 6  7 4 5  4 1 5  4 0 1  5 1 2  2 6 5  4 7 3  4 3 0  11 9 8  11 10 9  11 14 10  11 15 14  15 13 14  15 12 13  12 9 13  12 8 9  13 9 10  10 14 13  12 15 11  12 11 8  19 17 16  19 18 17  19 22 18  19 23 22  23 21 22  23 20 21  20 17 21  20 16 17  21 17 18  18 22 21  20 23 19  20 19 16  27 25 24  27 26 25  27 30 26  27 31 30  31 29 30  31 28 29  28 25 29  28 24 25  29 25 26  26 30 29  28 31 27  28 27 24 " />
                <RigidMapping template="Rigid3,Vec3" name="default60" mapForces="0" mapConstraints="0" mapMasses="0" input="@.." output="@Visual" rigidIndexPerPoint="0 8 8 8 8" />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9.81 0", dt="0.01", time="0")

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
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels showForceFields showCollisionModels showMechanicalMappings")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', name="default41", response="PenalityContactForceField")
       root.addObject('CollisionPipeline', name="default42")
       root.addObject('MinProximityIntersection', name="default43", alarmDistance="1", contactDistance="0.5")

       default44 = root.addChild('default44', gravity="0 -9.81 0")

       default44.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="0", rayleighStiffness="0.1", rayleighMass="0.1")
       default44.addObject('CGLinearSolver', template="GraphScattered", name="linear solver", iterations="25", tolerance="1e-009", threshold="1e-009")
       default44.addObject('MechanicalObject', template="Rigid3", name="DOFs", position="0 0 0 0 0 0 1 1 0 0 0 0 0 1 3 0 0 0 0 0 1 5 0 0 0 0 0 1 7 0 0 0 0 0 1", velocity="0 0 0 0 0 0", force="0 0 0 0 0 0", externalForce="0 0 0 0 0 0", derivX="0 0 0 0 0 0", restScale="1")
       default44.addObject('UniformMass', name="mass", vertexMass="1 1 [1 0 0,0 1 0,0 0 1]")
       default44.addObject('FixedProjectiveConstraint', template="Rigid3", name="fixOrigin", indices="0")

       default45 = default44.addChild('default45', gravity="0 -9.81 0")

       default45.addObject('MechanicalObject', template="Rigid3", name="attaches", position="0 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914", velocity="0 0 0 0 0 0", force="0 0 0 0 0 0", externalForce="0 0 0 0 0 0", derivX="0 0 0 0 0 0", restScale="1")
       default45.addObject('RigidMapping', template="Rigid3,Rigid3", name="default46", input="@..", output="@.", rigidIndexPerPoint="1 2 2 2 2")
       default45.addObject('JointSpringForceField', template="Rigid3", name="joint springs", spring="BEGIN_SPRING  0 1  FREE_AXIS 0 0 0 0 1 0  KS_T 0 30000  KS_R 0 200000  KD 1  R_LIM_X -0.8 0.8  R_LIM_Y -1.57 1.57  R_LIM_Z 0 0  END_SPRING
 BEGIN_SPRING  2 3  FREE_AXIS 0 0 0 0 1 0  KS_T 0 30000  KS_R 0 200000  KD 1  R_LIM_X -0.8 0.8  R_LIM_Y -1.57 1.57  R_LIM_Z 0 0  END_SPRING
 BEGIN_SPRING  4 5  FREE_AXIS 0 0 0 0 1 0  KS_T 0 30000  KS_R 0 200000  KD 1  R_LIM_X -0.8 0.8  R_LIM_Y -1.57 1.57  R_LIM_Z 0 0  END_SPRING
 BEGIN_SPRING  6 7  FREE_AXIS 0 0 0 0 1 0  KS_T 0 30000  KS_R 0 200000  KD 1  R_LIM_X -0.8 0.8  R_LIM_Y -1.57 1.57  R_LIM_Z 0 0  END_SPRING
")

       visu = default44.addChild('Visu', gravity="0 -9.81 0")

       visu.addObject('OglModel', template="Vec3", name="Visual", position="-1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5", vertices="-1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5", triangles="3 1 0  3 2 1  3 6 2  3 7 6  7 5 6  7 4 5  4 1 5  4 0 1  5 1 2  2 6 5  4 7 3  4 3 0  11 9 8  11 10 9  11 14 10  11 15 14  15 13 14  15 12 13  12 9 13  12 8 9  13 9 10  10 14 13  12 15 11  12 11 8  19 17 16  19 18 17  19 22 18  19 23 22  23 21 22  23 20 21  20 17 21  20 16 17  21 17 18  18 22 21  20 23 19  20 19 16  27 25 24  27 26 25  27 30 26  27 31 30  31 29 30  31 28 29  28 25 29  28 24 25  29 25 26  26 30 29  28 31 27  28 27 24 ")
       visu.addObject('RigidMapping', template="Rigid3,Vec3", name="default60", mapForces="0", mapConstraints="0", mapMasses="0", input="@..", output="@Visual", rigidIndexPerPoint="0 8 8 8 8")
    ```

