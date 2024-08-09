---
title: TransformEngine
---

`TransformEngine
===============

This component belongs to the category of [Engines](../../../simulation-principles/engine/). The TransformEngine transforms the positions of one DataFields into new positions after applying a transformation. This transformation can be either: translation, rotation or scale.
<!-- automatically generated doc START -->
__Target__: `Sofa.Component.Engine.Transform`

__namespace__: `#!c++ sofa::component::engine::transform`

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
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>input_position</td>
		<td>
input array of 3d points
</td>
		<td></td>
	</tr>
	<tr>
		<td>translation</td>
		<td>
translation vector (x,y,z)
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>rotation</td>
		<td>
rotation vector (x,y,z)
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>quaternion</td>
		<td>
rotation quaternion (qx,qy,qz,qw)
</td>
		<td>0 0 0 1</td>
	</tr>
	<tr>
		<td>scale</td>
		<td>
scale factor
</td>
		<td>1 1 1</td>
	</tr>
	<tr>
		<td>inverse</td>
		<td>
true to apply inverse transformation
</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>output_position</td>
		<td>
output array of 3d points
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

Component/Engine/Transform/TransformEngine.scn

=== "XML"

    ```xml
    <Node name="Root" gravity="0 0 0" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Engine.Transform"/> <!-- Needed to use components [TransformEngine] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [SparseGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showVisual" />
        <CollisionPipeline name="DefaultCollisionPipeline" verbose="0" draw="0" depth="6" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <!-- Using the Transform Engine on the independent MechanicalState -->
        <Node name="TransformedState" gravity="0 -9.81 0">
            <EulerImplicitSolver name="default12" rayleighStiffness="0.01"  rayleighMass="0.1" />
            <CGLinearSolver template="GraphScattered" name="default13" iterations="25" threshold="1e-08" tolerance="1e-05"/>
            <SparseGridTopology name="default14" fileTopology="mesh/doubleBall.obj" n="6 6 6" />
            <TransformEngine name="transform" template="Vec3" translation="10 0 0" rotation="0 0 90" scale="0.5 1 2" input_position="@[-1].position" />
            <MechanicalObject template="Vec3" name="dofTransformed" position="@[-1].output_position" restScale="1" />
            <UniformMass name="default16" totalMass="5" />
            <HexahedronFEMForceField template="Vec3" name="FEM" method="polar" poissonRatio="0.3" youngModulus="5000" />
            <Node name="VisualNode" gravity="0 -9.81 0">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/doubleBall.obj" handleSeams="1" />
                <OglModel template="Vec3" name="Visual" src="@meshLoader_0" texturename="textures/board.png" material="Default Diffuse 1 1 0 0 1 Ambient 1 0.2 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45" />
                <BarycentricMapping template="Vec3,Vec3" name="default17" input="@.." output="@Visual" />
            </Node>
            <Node name="CollisionNode" gravity="0 -9.81 0">
                <MeshOBJLoader name="loader" filename="mesh/doubleBall.obj" />
                <MeshTopology src="@loader" name="default18" />
                <MechanicalObject src="@loader" template="Vec3" name="default19" restScale="1" />
                <TriangleCollisionModel name="default20" />
                <LineCollisionModel name="default21" />
                <PointCollisionModel name="default22" />
                <BarycentricMapping template="Vec3,Vec3" name="default23" />
            </Node>
        </Node>
        <Node name="VisualModel">
            <MeshOBJLoader name="ObjLoader" filename="mesh/floor3.obj" />
            <TransformEngine name="transform" template="Vec3" translation="5 0 0" rotation="0 0 -90" scale="0.1 0.3 0.1" input_position="@[-1].position" />
            <OglModel name="VisualModel" src="@./ObjLoader" position="@[-1].output_position" texturename="textures/floor.bmp" />
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        Root = rootNode.addChild('Root', gravity="0 0 0", dt="0.02")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Transform")
        Root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        Root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        Root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        Root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        Root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        Root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        Root.addObject('DefaultAnimationLoop')
        Root.addObject('VisualStyle', displayFlags="showVisual")
        Root.addObject('CollisionPipeline', name="DefaultCollisionPipeline", verbose="0", draw="0", depth="6")
        Root.addObject('BruteForceBroadPhase')
        Root.addObject('BVHNarrowPhase')
        Root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
        Root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

        TransformedState = Root.addChild('TransformedState', gravity="0 -9.81 0")
        TransformedState.addObject('EulerImplicitSolver', name="default12", rayleighStiffness="0.01", rayleighMass="0.1")
        TransformedState.addObject('CGLinearSolver', template="GraphScattered", name="default13", iterations="25", threshold="1e-08", tolerance="1e-05")
        TransformedState.addObject('SparseGridTopology', name="default14", fileTopology="mesh/doubleBall.obj", n="6 6 6")
        TransformedState.addObject('TransformEngine', name="transform", template="Vec3", translation="10 0 0", rotation="0 0 90", scale="0.5 1 2", input_position="@[-1].position")
        TransformedState.addObject('MechanicalObject', template="Vec3", name="dofTransformed", position="@[-1].output_position", restScale="1")
        TransformedState.addObject('UniformMass', name="default16", totalMass="5")
        TransformedState.addObject('HexahedronFEMForceField', template="Vec3", name="FEM", method="polar", poissonRatio="0.3", youngModulus="5000")

        VisualNode = TransformedState.addChild('VisualNode', gravity="0 -9.81 0")
        VisualNode.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/doubleBall.obj", handleSeams="1")
        VisualNode.addObject('OglModel', template="Vec3", name="Visual", src="@meshLoader_0", texturename="textures/board.png", material="Default Diffuse 1 1 0 0 1 Ambient 1 0.2 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45")
        VisualNode.addObject('BarycentricMapping', template="Vec3,Vec3", name="default17", input="@..", output="@Visual")

        CollisionNode = TransformedState.addChild('CollisionNode', gravity="0 -9.81 0")
        CollisionNode.addObject('MeshOBJLoader', name="loader", filename="mesh/doubleBall.obj")
        CollisionNode.addObject('MeshTopology', src="@loader", name="default18")
        CollisionNode.addObject('MechanicalObject', src="@loader", template="Vec3", name="default19", restScale="1")
        CollisionNode.addObject('TriangleCollisionModel', name="default20")
        CollisionNode.addObject('LineCollisionModel', name="default21")
        CollisionNode.addObject('PointCollisionModel', name="default22")
        CollisionNode.addObject('BarycentricMapping', template="Vec3,Vec3", name="default23")

        VisualModel = Root.addChild('VisualModel')
        VisualModel.addObject('MeshOBJLoader', name="ObjLoader", filename="mesh/floor3.obj")
        VisualModel.addObject('TransformEngine', name="transform", template="Vec3", translation="5 0 0", rotation="0 0 -90", scale="0.1 0.3 0.1", input_position="@[-1].position")
        VisualModel.addObject('OglModel', name="VisualModel", src="@./ObjLoader", position="@[-1].output_position", texturename="textures/floor.bmp")
    ```


<!-- automatically generated doc END -->
