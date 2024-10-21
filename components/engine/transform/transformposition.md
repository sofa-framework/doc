---
title: TransformPosition
---

TransformPosition
===============

This component belongs to the category of [Engines](../../../../simulation-principles/engine/). The TransformPosition engine transforms the positions of one DataFields into new positions after applying a transformation. This transformation can be either:

-   Projection on a plane (plane defined by an origin and a normal vector)
-   Translation, rotation, scale and some combinations of translation rotation and scale
<!-- automatically generated doc START -->
<!-- generate_doc -->

Transform position of 3d points.


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.Engine.Transform

__namespace__: sofa::component::engine::transform

__parents__:

- DataEngine

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
		<td>method</td>
		<td>
transformation method either translation or scale or rotation or random or projectOnPlane
		</td>
		<td></td>
	</tr>
	<tr>
		<td>seedValue</td>
		<td>
the seed value for the random generator
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>maxRandomDisplacement</td>
		<td>
the maximum displacement around initial position for the random transformation
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>filename</td>
		<td>
filename of an affine matrix. Supported extensions are: .trm, .tfm, .xfm and .txt(read as .xfm)
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>origin</td>
		<td>
A 3d point on the plane/Center of the scale
		</td>
		<td></td>
	</tr>
	<tr>
		<td>input_position</td>
		<td>
input array of 3d points
		</td>
		<td></td>
	</tr>
	<tr>
		<td>normal</td>
		<td>
plane normal
		</td>
		<td></td>
	</tr>
	<tr>
		<td>translation</td>
		<td>
translation vector 
		</td>
		<td></td>
	</tr>
	<tr>
		<td>rotation</td>
		<td>
rotation vector 
		</td>
		<td></td>
	</tr>
	<tr>
		<td>scale</td>
		<td>
scale factor
		</td>
		<td>1 1 1</td>
	</tr>
	<tr>
		<td>matrix</td>
		<td>
4x4 affine matrix
		</td>
		<td>[1 0 0 0,0 1 0 0,0 0 1 0,0 0 0 1]</td>
	</tr>
	<tr>
		<td>fixedIndices</td>
		<td>
Indices of the entries that are not transformed
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>output_position</td>
		<td>
output array of 3d points projected on a plane
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawInput</td>
		<td>
Draw input points
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawOutput</td>
		<td>
Draw output points
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>pointSize</td>
		<td>
Point size
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

## Examples 

TransformPosition.scn

=== "XML"

    ```xml
    <Node name="root" gravity="0 0 -9.81" dt="0.05">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Engine.Transform"/> <!-- Needed to use components [TransformPosition] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [PlaneForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [SparseGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showVisual showBehaviorModels" />
        <CollisionPipeline name="DefaultCollisionPipeline" verbose="0" draw="0" depth="6" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="3" contactDistance="2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="Object" gravity="0 -9.81 0">
            <EulerImplicitSolver name="Implicit Euler Solver"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver  name="Conjugate Gradient" tolerance="1e-05" threshold="1e-05" iterations="5"/>
            <SparseGridTopology name="grid" fileTopology="mesh/dragon.obj" n="7 6 5" />
            <TransformPosition name="transfo" method="fromFile" filename="transfo.tfm" input_position="@grid.position"/>
            <MechanicalObject  name="Particles" restScale="1" position="@transfo.output_position" />
            <UniformMass  name="Mass" totalMass="1.0"/>
            <PlaneForceField  name="Plane" normal="0 0 1" d="-10" />
            <HexahedronFEMForceField  name="FEM" youngModulus="200" poissonRatio="0.45"/>
            <Node name="VisualNode" gravity="0 -9.81 0">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/dragon.obj" handleSeams="1" />
                <OglModel name="Objective" src="@meshLoader_0" />
                <BarycentricMapping  name="Visual Mapping" output="@Objective"  />
            </Node>
        </Node>
        <Node name="Floor">
            <MeshOBJLoader name="ObjLoader" filename="mesh/floor.obj" />
            <OglModel name="VisualModel" src="@./ObjLoader" translation="0 0 -9" rotation="90 0 0"/>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 0 -9.81", dt="0.05")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Transform")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels")
       root.addObject('CollisionPipeline', name="DefaultCollisionPipeline", verbose="0", draw="0", depth="6")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="3", contactDistance="2")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       object = root.addChild('Object', gravity="0 -9.81 0")

       object.addObject('EulerImplicitSolver', name="Implicit Euler Solver", rayleighStiffness="0.1", rayleighMass="0.1")
       object.addObject('CGLinearSolver', name="Conjugate Gradient", tolerance="1e-05", threshold="1e-05", iterations="5")
       object.addObject('SparseGridTopology', name="grid", fileTopology="mesh/dragon.obj", n="7 6 5")
       object.addObject('TransformPosition', name="transfo", method="fromFile", filename="transfo.tfm", input_position="@grid.position")
       object.addObject('MechanicalObject', name="Particles", restScale="1", position="@transfo.output_position")
       object.addObject('UniformMass', name="Mass", totalMass="1.0")
       object.addObject('PlaneForceField', name="Plane", normal="0 0 1", d="-10")
       object.addObject('HexahedronFEMForceField', name="FEM", youngModulus="200", poissonRatio="0.45")

       visual_node = Object.addChild('VisualNode', gravity="0 -9.81 0")

       visual_node.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/dragon.obj", handleSeams="1")
       visual_node.addObject('OglModel', name="Objective", src="@meshLoader_0")
       visual_node.addObject('BarycentricMapping', name="Visual Mapping", output="@Objective")

       floor = root.addChild('Floor')

       floor.addObject('MeshOBJLoader', name="ObjLoader", filename="mesh/floor.obj")
       floor.addObject('OglModel', name="VisualModel", src="@./ObjLoader", translation="0 0 -9", rotation="90 0 0")
    ```


<!-- automatically generated doc END -->
