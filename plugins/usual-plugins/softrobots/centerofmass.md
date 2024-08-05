# CenterOfMass

This class computes the center of mass of the object in its context.


__Templates__:

- `#!c++ Vec3d`

__Target__: `SoftRobots`

__namespace__: `#!c++ softrobots::engine`

__parents__: 

- `#!c++ DataEngine`

__categories__: 

- Engine

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
		<td>position</td>
		<td>
If not set by user, find the context mechanical.
</td>
		<td></td>
	</tr>
	<tr>
		<td>centerOfMass</td>
		<td>

</td>
		<td></td>
	</tr>
	<tr>
		<td>visualization</td>
		<td>
If set to true, will draw the center of mass
</td>
		<td></td>
	</tr>
	<tr>
		<td>visuSize</td>
		<td>

</td>
		<td>1</td>
	</tr>
	<tr>
		<td>visuColor</td>
		<td>

</td>
		<td>1 0 0 1</td>
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

Component/Mapping/Linear/CenterOfMassMapping.scn

=== "XML"

    ```xml
    <Node name="root" gravity="0 -9.81 0" dt="0.01" time="0" animate="0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [SphereCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [CenterOfMassMapping SkinningMapping] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [JointSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <VisualStyle displayFlags="showVisual showForceFields showCollisionModels showMechanicalMappings showWireframe" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="default1" />
        <CollisionPipeline name="default2" />
        <MinProximityIntersection name="default3" alarmDistance="1" contactDistance="0.5"/>
        <DefaultAnimationLoop/>
        
        <Node name="pendulum" gravity="0 -9.81 0" dt="0.01" time="0" animate="0" multiThreadSimulation="0">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject template="Rigid3" name="DOFs" position="0 0 0 0 0 0 1 1 0 0 0 0 0 1 3 0 0 0 0 0 1 5 0 0 0 0 0 1 7 0 0 0 0 0 1"
    						       velocity="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
    						       force="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
    						       dx="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
    						       free_position="0 0 0 0 0 0 1 1 0 0 0 0 0 1 3 0 0 0 0 0 1 5 0 0 0 0 0 1 7 0 0 0 0 0 1"
    						       free_velocity="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
    						       rest_position="0 0 0 0 0 0 1 1 0 0 0 0 0 1 3 0 0 0 0 0 1 5 0 0 0 0 0 1 7 0 0 0 0 0 1" />
            <UniformMass template="Rigid3" name="mass" vertexMass="1 1 [1 0 0,0 1 0,0 0 1]" />
            <FixedProjectiveConstraint template="Rigid3" name="fixOrigin" indices="0" />
            <Node name="segmentsNode" gravity="0 -9.81 0" dt="0.01" time="0" animate="0" multiThreadSimulation="0">
                <MechanicalObject template="Rigid3" name="attaches" position="0 0 0 0.707914 0 0 0.707914 0 0 0 0.707914 0 0 0.707914 2 0 0 0.707914 0 0 0.707914 2 0 0 0.707914 0 0 0.707914 4 0 0 0.707914 0 0 0.707914 4 0 0 0.707914 0 0 0.707914 6 0 0 0.707914 0 0 0.707914 6 0 0 0.707914 0 0 0.707914 8 0 0 0.707914 0 0 0.707914"
    							       velocity="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
    							       force="-0.204691 0.493087 -1.55393 -15.7823 -4.91695 -0.011207 0.204691 -0.493087 1.55393 15.7823 4.91695 0.011207 -0.817747 -0.565234 -0.504438 15.6267 -1.41904 0.0182122 0.817747 0.565234 0.504438 -15.6267 1.41904 -0.0182122 -0.490036 0.948643 0.849816 10.3784 20.6947 0.014016 0.490036 -0.948643 -0.849816 -10.3784 -20.6947 -0.014016 -1.16244 -0.595626 0.268606 3.22919 22.0184 -0.0357184 1.16244 0.595626 -0.268606 -3.22919 -22.0184 0.0357184 0 0 0 0 0 0"
    							       dx="0 0 0 0 0 0 -2.04691e-005 4.93087e-005 -0.000155393 -7.89115e-005 -2.45853e-005 2.00717e-007 -2.01601e-005 4.95435e-005 -5.1433e-006 -7.89115e-005 -2.45853e-005 2.00717e-007 -0.000101935 -6.97992e-006 -5.55871e-005 -8.0336e-007 -3.15395e-005 -6.3655e-005 -3.64901e-006 -8.78868e-005 -1.67401e-005 -8.0336e-007 -3.15395e-005 -6.3655e-005 -5.26526e-005 6.9775e-006 6.82415e-005 5.10966e-005 7.20224e-005 -0.000102151 6.00157e-005 0.000177406 0.000244762 5.10966e-005 7.20224e-005 -0.000102151 -5.62283e-005 0.000117843 0.000271622 6.71189e-005 0.000181679 6.29123e-005 7.75285e-006 1.00596e-005 0.000514622 6.71189e-005 0.000181679 6.29123e-005"
    							       free_position="0 0 0 0.707914 0 0 0.707914 0 0 0 0.707914 0 0 0.707914 2 0 0 0.707914 0 0 0.707914 2 0 0 0.707914 0 0 0.707914 4 0 0 0.707914 0 0 0.707914 4 0 0 0.707914 0 0 0.707914 6 0 0 0.707914 0 0 0.707914 6 0 0 0.707914 0 0 0.707914 8 0 0 0.707914 0 0 0.707914"
    							       free_velocity="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
    						               rest_position="0 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914" />
                <RigidMapping template="Rigid3,Rigid3" name="default55" initialPoints="0 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914" rigidIndexPerPoint="1 2 2 2 2" />
                <JointSpringForceField template="Rigid3" name="joint springs" spring="BEGIN_SPRING  0 1  FREE_AXIS 0 0 0 0 1 0  KS_R 0 200000  KD 1  R_LIM_X 0 0  R_LIM_Y -1.57 1.57  R_LIM_Z 0 0  END_SPRING&#x0A; BEGIN_SPRING  2 3  FREE_AXIS 0 0 0 0 1 0  KS_R 0 200000  KD 1  R_LIM_X 0 0  R_LIM_Y -1.57 1.57  R_LIM_Z 0 0  END_SPRING&#x0A; BEGIN_SPRING  4 5  FREE_AXIS 0 0 0 0 1 0  KS_R 0 200000  KD 1  R_LIM_X 0 0  R_LIM_Y -1.57 1.57  R_LIM_Z 0 0  END_SPRING&#x0A; BEGIN_SPRING  6 7  FREE_AXIS 0 0 0 0 1 0  KS_R 0 200000  KD 1  R_LIM_X 0 0  R_LIM_Y -1.57 1.57  R_LIM_Z 0 0  END_SPRING&#x0A;" />
            </Node>
            <Node name="default65" gravity="0 -9.81 0" dt="0.01" time="0" animate="0" multiThreadSimulation="0">
                <OglModel name="Visual" position="0 -0.5 -0.5 0 0.5 -0.5 0 0.5 0.5 0 -0.5 0.5 2 -0.5 -0.5 2 0.5 -0.5 2 0.5 0.5 2 -0.5 0.5 2 -0.5 -0.5 2 0.5 -0.5 2 0.5 0.5 2 -0.5 0.5 4 -0.5 -0.5 4 0.5 -0.5 4 0.5 0.5 4 -0.5 0.5 4 -0.5 -0.5 4 0.5 -0.5 4 0.5 0.5 4 -0.5 0.5 6 -0.5 -0.5 6 0.5 -0.5 6 0.5 0.5 6 -0.5 0.5 6 -0.5 -0.5 6 0.5 -0.5 6 0.5 0.5 6 -0.5 0.5 8 -0.5 -0.5 8 0.5 -0.5 8 0.5 0.5 8 -0.5 0.5"
    				    normals="-0.57735 -0.57735 -0.57735 -0.666667 0.333333 -0.666667 -0.408248 0.816497 0.408248 -0.57735 -0.57735 0.57735 0.333333 -0.666667 -0.666667 0.666667 0.666667 -0.333333 0.408248 0.408248 0.816497 0.816497 -0.408248 0.408248 -0.57735 -0.57735 -0.57735 -0.666667 0.333333 -0.666667 -0.408248 0.816497 0.408248 -0.57735 -0.57735 0.57735 0.333333 -0.666667 -0.666667 0.666667 0.666667 -0.333333 0.408248 0.408248 0.816497 0.816497 -0.408248 0.408248 -0.57735 -0.57735 -0.57735 -0.666667 0.333333 -0.666667 -0.408248 0.816497 0.408248 -0.57735 -0.57735 0.57735 0.333333 -0.666667 -0.666667 0.666667 0.666667 -0.333333 0.408248 0.408248 0.816497 0.816497 -0.408248 0.408248 -0.57735 -0.57735 -0.57735 -0.666667 0.333333 -0.666667 -0.408248 0.816497 0.408248 -0.57735 -0.57735 0.57735 0.333333 -0.666667 -0.666667 0.666667 0.666667 -0.333333 0.408248 0.408248 0.816497 0.816497 -0.408248 0.408248"
    				    triangles="3 1 0  3 2 1  3 6 2  3 7 6  7 5 6  7 4 5  4 1 5  4 0 1  5 1 2  2 6 5  4 7 3  4 3 0  11 9 8  11 10 9  11 14 10  11 15 14  15 13 14  15 12 13  12 9 13  12 8 9  13 9 10  10 14 13  12 15 11  12 11 8  19 17 16  19 18 17  19 22 18  19 23 22  23 21 22  23 20 21  20 17 21  20 16 17  21 17 18  18 22 21  20 23 19  20 19 16  27 25 24  27 26 25  27 30 26  27 31 30  31 29 30  31 28 29  28 25 29  28 24 25  29 25 26  26 30 29  28 31 27  28 27 24" />
                <SkinningMapping template="Rigid3,Vec3" name="map" input="@.." output="@Visual" />
            </Node>
            <Node name="CenterOfMass" gravity="0 -9.81 0" dt="0.01" time="0" animate="0" multiThreadSimulation="0">
                <MechanicalObject template="Vec3" name="default88" listening="0" printLog="0" restScale="1" position="3.2 0 0" velocity="0 0 0" force="0 0 0" dx="-1.87325e-005 3.16272e-005 8.66385e-005" free_position="3.2 0 0" free_velocity="0 0 0" rest_position="0 0 0"/>
                <SphereCollisionModel name="default88Sphere" active="1" moving="1" simulated="1" selfCollision="0" proximity="0" contactStiffness="10" contactFriction="0.01" color="1 0.5 0 1" radius="0.2"/>
                <CenterOfMassMapping template="Rigid3,Vec3" name="default105" />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -9.81 0", dt="0.01", time="0", animate="0")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showVisual showForceFields showCollisionModels showMechanicalMappings showWireframe")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', name="default1")
        root.addObject('CollisionPipeline', name="default2")
        root.addObject('MinProximityIntersection', name="default3", alarmDistance="1", contactDistance="0.5")
        root.addObject('DefaultAnimationLoop')

        pendulum = root.addChild('pendulum', gravity="0 -9.81 0", dt="0.01", time="0", animate="0", multiThreadSimulation="0")
        pendulum.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        pendulum.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        pendulum.addObject('MechanicalObject', template="Rigid3", name="DOFs", position="0 0 0 0 0 0 1 1 0 0 0 0 0 1 3 0 0 0 0 0 1 5 0 0 0 0 0 1 7 0 0 0 0 0 1", velocity="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0", force="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0", dx="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0", free_position="0 0 0 0 0 0 1 1 0 0 0 0 0 1 3 0 0 0 0 0 1 5 0 0 0 0 0 1 7 0 0 0 0 0 1", free_velocity="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0", rest_position="0 0 0 0 0 0 1 1 0 0 0 0 0 1 3 0 0 0 0 0 1 5 0 0 0 0 0 1 7 0 0 0 0 0 1")
        pendulum.addObject('UniformMass', template="Rigid3", name="mass", vertexMass="1 1 [1 0 0,0 1 0,0 0 1]")
        pendulum.addObject('FixedProjectiveConstraint', template="Rigid3", name="fixOrigin", indices="0")

        segmentsNode = pendulum.addChild('segmentsNode', gravity="0 -9.81 0", dt="0.01", time="0", animate="0", multiThreadSimulation="0")
        segmentsNode.addObject('MechanicalObject', template="Rigid3", name="attaches", position="0 0 0 0.707914 0 0 0.707914 0 0 0 0.707914 0 0 0.707914 2 0 0 0.707914 0 0 0.707914 2 0 0 0.707914 0 0 0.707914 4 0 0 0.707914 0 0 0.707914 4 0 0 0.707914 0 0 0.707914 6 0 0 0.707914 0 0 0.707914 6 0 0 0.707914 0 0 0.707914 8 0 0 0.707914 0 0 0.707914", velocity="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0", force="-0.204691 0.493087 -1.55393 -15.7823 -4.91695 -0.011207 0.204691 -0.493087 1.55393 15.7823 4.91695 0.011207 -0.817747 -0.565234 -0.504438 15.6267 -1.41904 0.0182122 0.817747 0.565234 0.504438 -15.6267 1.41904 -0.0182122 -0.490036 0.948643 0.849816 10.3784 20.6947 0.014016 0.490036 -0.948643 -0.849816 -10.3784 -20.6947 -0.014016 -1.16244 -0.595626 0.268606 3.22919 22.0184 -0.0357184 1.16244 0.595626 -0.268606 -3.22919 -22.0184 0.0357184 0 0 0 0 0 0", dx="0 0 0 0 0 0 -2.04691e-005 4.93087e-005 -0.000155393 -7.89115e-005 -2.45853e-005 2.00717e-007 -2.01601e-005 4.95435e-005 -5.1433e-006 -7.89115e-005 -2.45853e-005 2.00717e-007 -0.000101935 -6.97992e-006 -5.55871e-005 -8.0336e-007 -3.15395e-005 -6.3655e-005 -3.64901e-006 -8.78868e-005 -1.67401e-005 -8.0336e-007 -3.15395e-005 -6.3655e-005 -5.26526e-005 6.9775e-006 6.82415e-005 5.10966e-005 7.20224e-005 -0.000102151 6.00157e-005 0.000177406 0.000244762 5.10966e-005 7.20224e-005 -0.000102151 -5.62283e-005 0.000117843 0.000271622 6.71189e-005 0.000181679 6.29123e-005 7.75285e-006 1.00596e-005 0.000514622 6.71189e-005 0.000181679 6.29123e-005", free_position="0 0 0 0.707914 0 0 0.707914 0 0 0 0.707914 0 0 0.707914 2 0 0 0.707914 0 0 0.707914 2 0 0 0.707914 0 0 0.707914 4 0 0 0.707914 0 0 0.707914 4 0 0 0.707914 0 0 0.707914 6 0 0 0.707914 0 0 0.707914 6 0 0 0.707914 0 0 0.707914 8 0 0 0.707914 0 0 0.707914", free_velocity="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0", rest_position="0 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914")
        segmentsNode.addObject('RigidMapping', template="Rigid3,Rigid3", name="default55", initialPoints="0 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914 -1 0 0 0.707914 0 0 0.707914 1 0 0 0.707914 0 0 0.707914", rigidIndexPerPoint="1 2 2 2 2")
        segmentsNode.addObject('JointSpringForceField', template="Rigid3", name="joint springs", spring="BEGIN_SPRING  0 1  FREE_AXIS 0 0 0 0 1 0  KS_R 0 200000  KD 1  R_LIM_X 0 0  R_LIM_Y -1.57 1.57  R_LIM_Z 0 0  END_SPRING
 BEGIN_SPRING  2 3  FREE_AXIS 0 0 0 0 1 0  KS_R 0 200000  KD 1  R_LIM_X 0 0  R_LIM_Y -1.57 1.57  R_LIM_Z 0 0  END_SPRING
 BEGIN_SPRING  4 5  FREE_AXIS 0 0 0 0 1 0  KS_R 0 200000  KD 1  R_LIM_X 0 0  R_LIM_Y -1.57 1.57  R_LIM_Z 0 0  END_SPRING
 BEGIN_SPRING  6 7  FREE_AXIS 0 0 0 0 1 0  KS_R 0 200000  KD 1  R_LIM_X 0 0  R_LIM_Y -1.57 1.57  R_LIM_Z 0 0  END_SPRING
")

        default65 = pendulum.addChild('default65', gravity="0 -9.81 0", dt="0.01", time="0", animate="0", multiThreadSimulation="0")
        default65.addObject('OglModel', name="Visual", position="0 -0.5 -0.5 0 0.5 -0.5 0 0.5 0.5 0 -0.5 0.5 2 -0.5 -0.5 2 0.5 -0.5 2 0.5 0.5 2 -0.5 0.5 2 -0.5 -0.5 2 0.5 -0.5 2 0.5 0.5 2 -0.5 0.5 4 -0.5 -0.5 4 0.5 -0.5 4 0.5 0.5 4 -0.5 0.5 4 -0.5 -0.5 4 0.5 -0.5 4 0.5 0.5 4 -0.5 0.5 6 -0.5 -0.5 6 0.5 -0.5 6 0.5 0.5 6 -0.5 0.5 6 -0.5 -0.5 6 0.5 -0.5 6 0.5 0.5 6 -0.5 0.5 8 -0.5 -0.5 8 0.5 -0.5 8 0.5 0.5 8 -0.5 0.5", normals="-0.57735 -0.57735 -0.57735 -0.666667 0.333333 -0.666667 -0.408248 0.816497 0.408248 -0.57735 -0.57735 0.57735 0.333333 -0.666667 -0.666667 0.666667 0.666667 -0.333333 0.408248 0.408248 0.816497 0.816497 -0.408248 0.408248 -0.57735 -0.57735 -0.57735 -0.666667 0.333333 -0.666667 -0.408248 0.816497 0.408248 -0.57735 -0.57735 0.57735 0.333333 -0.666667 -0.666667 0.666667 0.666667 -0.333333 0.408248 0.408248 0.816497 0.816497 -0.408248 0.408248 -0.57735 -0.57735 -0.57735 -0.666667 0.333333 -0.666667 -0.408248 0.816497 0.408248 -0.57735 -0.57735 0.57735 0.333333 -0.666667 -0.666667 0.666667 0.666667 -0.333333 0.408248 0.408248 0.816497 0.816497 -0.408248 0.408248 -0.57735 -0.57735 -0.57735 -0.666667 0.333333 -0.666667 -0.408248 0.816497 0.408248 -0.57735 -0.57735 0.57735 0.333333 -0.666667 -0.666667 0.666667 0.666667 -0.333333 0.408248 0.408248 0.816497 0.816497 -0.408248 0.408248", triangles="3 1 0  3 2 1  3 6 2  3 7 6  7 5 6  7 4 5  4 1 5  4 0 1  5 1 2  2 6 5  4 7 3  4 3 0  11 9 8  11 10 9  11 14 10  11 15 14  15 13 14  15 12 13  12 9 13  12 8 9  13 9 10  10 14 13  12 15 11  12 11 8  19 17 16  19 18 17  19 22 18  19 23 22  23 21 22  23 20 21  20 17 21  20 16 17  21 17 18  18 22 21  20 23 19  20 19 16  27 25 24  27 26 25  27 30 26  27 31 30  31 29 30  31 28 29  28 25 29  28 24 25  29 25 26  26 30 29  28 31 27  28 27 24")
        default65.addObject('SkinningMapping', template="Rigid3,Vec3", name="map", input="@..", output="@Visual")

        CenterOfMass = pendulum.addChild('CenterOfMass', gravity="0 -9.81 0", dt="0.01", time="0", animate="0", multiThreadSimulation="0")
        CenterOfMass.addObject('MechanicalObject', template="Vec3", name="default88", listening="0", printLog="0", restScale="1", position="3.2 0 0", velocity="0 0 0", force="0 0 0", dx="-1.87325e-005 3.16272e-005 8.66385e-005", free_position="3.2 0 0", free_velocity="0 0 0", rest_position="0 0 0")
        CenterOfMass.addObject('SphereCollisionModel', name="default88Sphere", active="1", moving="1", simulated="1", selfCollision="0", proximity="0", contactStiffness="10", contactFriction="0.01", color="1 0.5 0 1", radius="0.2")
        CenterOfMass.addObject('CenterOfMassMapping', template="Rigid3,Vec3", name="default105")
    ```

