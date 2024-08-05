# BeamLinearMapping

Set the positions and velocities of points attached to a beam using linear interpolation between DOFs
Set the positions and velocities of points attached to a beam using linear interpolation between DOFs


__Templates__:

- `#!c++ Rigid3d,CudaVec3d`
- `#!c++ Rigid3d,CudaVec3f`

__Target__: `SofaCUDA`

__namespace__: `#!c++ sofa::component::mapping::linear`

__parents__: 

- `#!c++ CRTPLinearMapping`

__categories__: 

- Mapping

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
		<td>mapForces</td>
		<td>
Are forces mapped ?
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapConstraints</td>
		<td>
Are constraints mapped ?
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapMasses</td>
		<td>
Are masses mapped ?
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapMatrices</td>
		<td>
Are matrix explicit mapped?
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>applyRestPosition</td>
		<td>
set to true to apply this mapping to restPosition at init
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>localCoord</td>
		<td>
true if initial coordinates are in the beam local coordinate system (i.e. a point at (10,0,0) is on the DOF number 10, whereas if this is false it is at whatever position on the beam where the distance from the initial DOF is 10)
</td>
		<td>1</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|input|Input object to map|
|output|Output object to map|



## Examples

MultiThreading/share/sofa/examples/MultiThreading/BeamLinearMapping_mt.scn

=== "XML"

    ```xml
    <!-- BeamFEMForceField example -->
    <Node name="root" dt="0.01">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [BTDLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [BeamFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [CubeTopology MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <VisualStyle displayFlags="showBehaviorModels showForceFields showCollisionModels" />
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.03" contactDistance="0.02" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="beam">
            <EulerImplicitSolver rayleighStiffness="0" printLog="false"  rayleighMass="0.1" />
            <BTDLinearSolver bandWidth="11" printLog="false" verbose="false" />
            <MechanicalObject template="Rigid3d" name="DOFs" position="0 0 0 0 0 0 1  1 0 0 0 0 0 1  2 0 0 0 0 0 1  3 0 0 0 0 0 1  4 0 0 0 0 0 1  5 0 0 0 0 0 1  6 0 0 0 0 0 1  7 0 0 0 0 0 1
                              8 0 0 0 0 0 1  9 0 0 0 0 0 1  10 0 0 0 0 0 1  11 0 0 0 0 0 1  12 0 0 0 0 0 1  13 0 0 0 0 0 1  14 0 0 0 0 0 1  15 0 0 0 0 0 1
                              16 0 0 0 0 0 1  17 0 0 0 0 0 1  18 0 0 0 0 0 1  19 0 0 0 0 0 1  20 0 0 0 0 0 1  21 0 0 0 0 0 1  22 0 0 0 0 0 1  23 0 0 0 0 0 1
                              24 0 0 0 0 0 1  25 0 0 0 0 0 1  26 0 0 0 0 0 1  27 0 0 0 0 0 1  28 0 0 0 0 0 1  29 0 0 0 0 0 1  30 0 0 0 0 0 1  31 0 0 0 0 0 1" />
            <MeshTopology name="lines" lines="0 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10 11 11 12 12 13 13 14 14 15 15 16 16 17 17 18 18 
                  19 19 20 20 21 21 22 22 23 23 24 24 25 25 26 26 27 27 28 28 29 29 30 30 31" />
            <!--
          <MechanicalObject template="Rigid3d" name="DOFs" position="0 0 0 0 0 0 1  1 0 0 0 0 0 1  2 0 0 0 0 0 1  3 0 0 0 0 0 1" />
          <MeshTopology name="lines" lines="0 1 1 2 2 3" />
          -->
            <!--
          <MechanicalObject template="Rigid3d" name="DOFs" position="0 0 0 0 0 -0.7071067811865475244 0.7071067811865475244  0 -1 0 0 0 -0.7071067811865475244 0.7071067811865475244" />
          <MeshTopology name="lines" lines="0 1" />
          -->
            <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="0" />
            <UniformMass vertexMass="1 1 0.01 0 0 0 0.1 0 0 0 0.1" printLog="false" />
            <BeamFEMForceField name="FEM" radius="0.1" poissonRatio="0.49" youngModulus="20000000" />
            <!--
          <Gravity value="0 0 0 0 0 0" />
          <ExternalForceField forces="10 0 0 0 0 0" indices="1" />
    -->
            <!--
          <Node name="Collision">
            <MechanicalObject/>
            <SphereCollisionModel radius=".2" position="0 0 0 0 0 0" />
            <RigidMapping index="7" />
          </Node>
    -->
            <Node name="Collision">
                <!--        <CubeTopology nx="115" ny="4" nz="4" xmin="0" xmax="7" ymin="-0.1" ymax="0.1" zmin="-0.1" zmax="0.1" /> -->
                <CubeTopology nx="256" ny="8" nz="8" min="0 -0.1 -0.1" max="31 0.1 0.1" />
                <MechanicalObject />
                <BeamLinearMapping_mt granularity="512" isMechanical="true" />
                <TriangleCollisionModel />
                <!--        <OglModel /> -->
            </Node>
        </Node>
      
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields showCollisionModels")
        root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.03", contactDistance="0.02")
        root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

        beam = root.addChild('beam')
        beam.addObject('EulerImplicitSolver', rayleighStiffness="0", printLog="false", rayleighMass="0.1")
        beam.addObject('BTDLinearSolver', bandWidth="11", printLog="false", verbose="false")
        beam.addObject('MechanicalObject', template="Rigid3d", name="DOFs", position="0 0 0 0 0 0 1  1 0 0 0 0 0 1  2 0 0 0 0 0 1  3 0 0 0 0 0 1  4 0 0 0 0 0 1  5 0 0 0 0 0 1  6 0 0 0 0 0 1  7 0 0 0 0 0 1
                          8 0 0 0 0 0 1  9 0 0 0 0 0 1  10 0 0 0 0 0 1  11 0 0 0 0 0 1  12 0 0 0 0 0 1  13 0 0 0 0 0 1  14 0 0 0 0 0 1  15 0 0 0 0 0 1
                          16 0 0 0 0 0 1  17 0 0 0 0 0 1  18 0 0 0 0 0 1  19 0 0 0 0 0 1  20 0 0 0 0 0 1  21 0 0 0 0 0 1  22 0 0 0 0 0 1  23 0 0 0 0 0 1
                          24 0 0 0 0 0 1  25 0 0 0 0 0 1  26 0 0 0 0 0 1  27 0 0 0 0 0 1  28 0 0 0 0 0 1  29 0 0 0 0 0 1  30 0 0 0 0 0 1  31 0 0 0 0 0 1")
        beam.addObject('MeshTopology', name="lines", lines="0 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10 11 11 12 12 13 13 14 14 15 15 16 16 17 17 18 18 
              19 19 20 20 21 21 22 22 23 23 24 24 25 25 26 26 27 27 28 28 29 29 30 30 31")
        beam.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="0")
        beam.addObject('UniformMass', vertexMass="1 1 0.01 0 0 0 0.1 0 0 0 0.1", printLog="false")
        beam.addObject('BeamFEMForceField', name="FEM", radius="0.1", poissonRatio="0.49", youngModulus="20000000")

        Collision = beam.addChild('Collision')
        Collision.addObject('CubeTopology', nx="256", ny="8", nz="8", min="0 -0.1 -0.1", max="31 0.1 0.1")
        Collision.addObject('MechanicalObject')
        Collision.addObject('BeamLinearMapping_mt', granularity="512", isMechanical="true")
        Collision.addObject('TriangleCollisionModel')
    ```

