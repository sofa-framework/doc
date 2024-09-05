<!-- generate_doc -->
# MechanicalStateController

Provides a Mouse & Keyboard user control on a Mechanical State.


Templates:

- Rigid3d
- Vec1d

__Target__: Sofa.Component.Controller

__namespace__: sofa::component::controller

__parents__:

- Controller

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
		<td>handleEventTriggersUpdate</td>
		<td>
Event handling frequency controls the controller update frequency
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>index</td>
		<td>
Index of the controlled DOF
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>onlyTranslation</td>
		<td>
Controlling the DOF only in translation
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>buttonDeviceState</td>
		<td>
state of ths device button
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>mainDirection</td>
		<td>
Main direction and orientation of the controlled DOF
		</td>
		<td>0 0 -1</td>
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

MechanicalStateController.scn

=== "XML"

    ```xml
    <!-- MechanicalStateController example -->
    <Node name="root" dt="0.005" gravity="0 -10 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [LocalMinDistance] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Controller"/> <!-- Needed to use components [MechanicalStateController] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [BTDLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [BeamFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [EdgeSetGeometryAlgorithms EdgeSetTopologyContainer EdgeSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showForceFields showCollisionModels" />
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <LocalMinDistance name="Proximity" alarmDistance="1.0" contactDistance="0.5" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="InstrumentEdgeSet">
            <EulerImplicitSolver rayleighStiffness="0" printLog="false"  rayleighMass="0.1" />
            <BTDLinearSolver template="BTDMatrix6d" printLog="false" verbose="false" />
            <MeshGmshLoader name="loader" filename="mesh/edgeSet.msh" />
            <MechanicalObject src="@loader" name="MechanicalDOFs" template="Rigid3" position="0 0 0 0 0 0 1  1 0 0 0 0 0 1  2 0 0 0 0 0 1" showObject="1"/>
            <include href="Objects/EdgeSetTopology.xml" src="@loader" template="Rigid3" />
            <MechanicalStateController template="Rigid3" listening="true" mainDirection="-1.0 0.0 0.0" handleEventTriggersUpdate="true" />
            <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="0" />
            <UniformMass vertexMass="1 1 0.1 0 0 0 0.1 0 0 0 0.1" printLog="false" /> 
    
            <BeamFEMForceField name="FEM" radius="0.1" youngModulus="50000000" poissonRatio=".49"/>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.005", gravity="0 -10 0")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Controller")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showForceFields showCollisionModels")
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('LocalMinDistance', name="Proximity", alarmDistance="1.0", contactDistance="0.5")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       instrument_edge_set = root.addChild('InstrumentEdgeSet')

       instrument_edge_set.addObject('EulerImplicitSolver', rayleighStiffness="0", printLog="false", rayleighMass="0.1")
       instrument_edge_set.addObject('BTDLinearSolver', template="BTDMatrix6d", printLog="false", verbose="false")
       instrument_edge_set.addObject('MeshGmshLoader', name="loader", filename="mesh/edgeSet.msh")
       instrument_edge_set.addObject('MechanicalObject', src="@loader", name="MechanicalDOFs", template="Rigid3", position="0 0 0 0 0 0 1  1 0 0 0 0 0 1  2 0 0 0 0 0 1", showObject="1")
       instrument_edge_set.addObject('include', href="Objects/EdgeSetTopology.xml", src="@loader", template="Rigid3")
       instrument_edge_set.addObject('MechanicalStateController', template="Rigid3", listening="true", mainDirection="-1.0 0.0 0.0", handleEventTriggersUpdate="true")
       instrument_edge_set.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="0")
       instrument_edge_set.addObject('UniformMass', vertexMass="1 1 0.1 0 0 0 0.1 0 0 0 0.1", printLog="false")
       instrument_edge_set.addObject('BeamFEMForceField', name="FEM", radius="0.1", youngModulus="50000000", poissonRatio=".49")
    ```

MechanicalStateControllerTranslation.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.005" gravity="0 -10 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [LocalMinDistance] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Controller"/> <!-- Needed to use components [MechanicalStateController] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <VisualStyle displayFlags="showForceFields showCollisionModels" />
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <LocalMinDistance name="Proximity" alarmDistance="1.0" contactDistance="0.5" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="InstrumentEdgeSet">
            <EulerImplicitSolver rayleighStiffness="0" printLog="false"  rayleighMass="0.1" />
            <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
            <MechanicalObject template="Rigid3" />
            <UniformMass totalMass="1" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/sphere.obj" scale="50" handleSeams="1" />
                <OglModel color="0.500 0.500 0.500" src="@meshLoader_0" name="Visual" />
                <RigidMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Surf2">
                <MeshOBJLoader name="loader" filename="mesh/sphere.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" scale="50" />
                <TriangleCollisionModel />
                <LineCollisionModel />
                <PointCollisionModel />
                <RigidMapping />
            </Node>
            <MechanicalStateController template="Rigid3" onlyTranslation="true" listening="true" handleEventTriggersUpdate="true" />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.005", gravity="0 -10 0")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Controller")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="showForceFields showCollisionModels")
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('LocalMinDistance', name="Proximity", alarmDistance="1.0", contactDistance="0.5")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       instrument_edge_set = root.addChild('InstrumentEdgeSet')

       instrument_edge_set.addObject('EulerImplicitSolver', rayleighStiffness="0", printLog="false", rayleighMass="0.1")
       instrument_edge_set.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
       instrument_edge_set.addObject('MechanicalObject', template="Rigid3")
       instrument_edge_set.addObject('UniformMass', totalMass="1")

       visu = InstrumentEdgeSet.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/sphere.obj", scale="50", handleSeams="1")
       visu.addObject('OglModel', color="0.500 0.500 0.500", src="@meshLoader_0", name="Visual")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       surf2 = InstrumentEdgeSet.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/sphere.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", scale="50")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('RigidMapping', )

       instrument_edge_set.addObject('MechanicalStateController', template="Rigid3", onlyTranslation="true", listening="true", handleEventTriggersUpdate="true")
    ```

