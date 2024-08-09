# IdentityMapping

Special case of mapping where the child points are the same as the parent points
Supports GPU-side computations using CUDA


__Templates__:

- `#!c++ Rigid2d,Rigid2d`
- `#!c++ Rigid2d,Vec2d`
- `#!c++ Rigid3d,Rigid3d`
- `#!c++ Rigid3d,Vec3d`
- `#!c++ Vec1d,Vec1d`
- `#!c++ Vec2d,Vec2d`
- `#!c++ Vec3d,Vec3d`
- `#!c++ Vec6d,Vec3d`
- `#!c++ Vec6d,Vec6d`

__Target__: `Sofa.Component.Mapping.Linear`

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

Component/Mapping/Linear/IdentityMapping.scn

=== "XML"

    ```xml
    <!-- Mechanical MassSpring Group Basic Example -->
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangleFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showMappings" />
        <CollisionPipeline verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
        <Node name="tshirt">
            <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" tolerance="1e-5" threshold="1e-5"/>
            <MeshGmshLoader name="loader" filename="mesh/tshirt_0.msh" />
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader" scale="10" />
            <include href="Objects/TriangleSetTopology.xml" src="@loader" />
            <UniformMass vertexMass="1" />
            <FixedProjectiveConstraint indices="38 39 40 41 42 43 123 124 137" />
            <TriangleFEMForceField name="FEM" youngModulus="50000" poissonRatio="0.3" method="large" />
            <TriangleCollisionModel />
            <Node name="Visu">
                <OglModel name="Visual" color="red" />
                <IdentityMapping input="@.." output="@Visual" />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showMappings")
        root.addObject('CollisionPipeline', verbose="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField")
        root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")

        tshirt = root.addChild('tshirt')
        tshirt.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
        tshirt.addObject('CGLinearSolver', iterations="25", tolerance="1e-5", threshold="1e-5")
        tshirt.addObject('MeshGmshLoader', name="loader", filename="mesh/tshirt_0.msh")
        tshirt.addObject('MeshTopology', src="@loader")
        tshirt.addObject('MechanicalObject', src="@loader", scale="10")
        tshirt.addObject('include', href="Objects/TriangleSetTopology.xml", src="@loader")
        tshirt.addObject('UniformMass', vertexMass="1")
        tshirt.addObject('FixedProjectiveConstraint', indices="38 39 40 41 42 43 123 124 137")
        tshirt.addObject('TriangleFEMForceField', name="FEM", youngModulus="50000", poissonRatio="0.3", method="large")
        tshirt.addObject('TriangleCollisionModel')

        Visu = tshirt.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="red")
        Visu.addObject('IdentityMapping', input="@..", output="@Visual")
    ```

