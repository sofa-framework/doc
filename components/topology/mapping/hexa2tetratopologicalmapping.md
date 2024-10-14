<!-- generate_doc -->
# Hexa2TetraTopologicalMapping

Topological mapping where HexahedronSetTopology is converted to TetrahedronSetTopology


__Target__: Sofa.Component.Topology.Mapping

__namespace__: sofa::component::topology::mapping

__parents__:

- TopologicalMapping

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
		<td>swapping</td>
		<td>
Boolean enabling to swapp hexa-edges
 in order to avoid bias effect
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
|input|Input topology to map|BaseMeshTopology|
|output|Output topology to map|BaseMeshTopology|

## Examples 

Hexa2TetraTopologicalMapping_export.scn

=== "XML"

    ```xml
    <Node name="root" gravity="0 -9.81 0" dt="0.01">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshExporter VisualModelOBJExporter] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping Tetra2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
        <CollisionPipeline name="default21" verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="default22" response="PenalityContactForceField" />
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
        <DefaultAnimationLoop/>
        <Node name="Cube" gravity="0 -9.81 0">
            <EulerImplicitSolver name="cg_odesolver" printLog="0"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver template="GraphScattered" name="linear solver" iterations="25" tolerance="1e-09" threshold="1e-09" />
            <MechanicalObject template="Vec3" name="dofs" />
            <UniformMass template="Vec3" name="default25" vertexMass="0.25" />
            <RegularGridTopology name="grid" n="6 6 6" min="-10 0 -10" max="10 20 10" />
            <TetrahedronFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.4" youngModulus="1000" assembling="0" />
            <BoxROI template="Vec3" name="box_roi" box="-11 -11 -11 11 -9 11" indices="0" drawSize="0" />
            <FixedProjectiveConstraint template="Vec3" name="default27" indices="@box_roi.indices" drawSize="0" />
            <Node name="Tetra" gravity="0 -9.81 0">
                <TetrahedronSetTopologyContainer name="Container" />
                <TetrahedronSetTopologyModifier name="Modifier" />
                <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                <Hexa2TetraTopologicalMapping name="default28" input="@../grid" output="@Container" />
                <MeshExporter filename="cube5x5x5" format="vtk" position="@../dofs.rest_position" edges="0" triangles="0" tetras="1" listening="true" exportAtBegin="true" />
                <Node name="Triangles" gravity="0 -9.81 0">
                    <TriangleSetTopologyContainer name="Container" />
                    <TriangleSetTopologyModifier name="Modifier" />
                    <TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                    <Tetra2TriangleTopologicalMapping name="default29" input="@../Container" output="@Container" />
                    <!--<MeshExporter filename="cube5x5x5-surface" position="@../../dofs.rest_position" edges="0" triangles="1" tetras="0" listening="true" exportAtBegin="true" />-->
                    <TriangleCollisionModel name="default30" />
                    <LineCollisionModel name="default31" />
                    <PointCollisionModel name="default32" />
                    <Node name="Visu" gravity="0 -9.81 0">
                        <OglModel template="Vec3" name="Visual" material="Default Diffuse 1 1 0 0 1 Ambient 1 0.2 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45" />
                        <IdentityMapping template="Vec3,Vec3" name="default33" input="@.." output="@Visual" />
                        <VisualModelOBJExporter filename="cube5x5x5-surface" exportAtBegin="true" />
                    </Node>
                </Node>
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9.81 0", dt="0.01")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
       root.addObject('CollisionPipeline', name="default21", verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', name="default22", response="PenalityContactForceField")
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")
       root.addObject('DefaultAnimationLoop', )

       cube = root.addChild('Cube', gravity="0 -9.81 0")

       cube.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="0", rayleighStiffness="0.1", rayleighMass="0.1")
       cube.addObject('CGLinearSolver', template="GraphScattered", name="linear solver", iterations="25", tolerance="1e-09", threshold="1e-09")
       cube.addObject('MechanicalObject', template="Vec3", name="dofs")
       cube.addObject('UniformMass', template="Vec3", name="default25", vertexMass="0.25")
       cube.addObject('RegularGridTopology', name="grid", n="6 6 6", min="-10 0 -10", max="10 20 10")
       cube.addObject('TetrahedronFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.4", youngModulus="1000", assembling="0")
       cube.addObject('BoxROI', template="Vec3", name="box_roi", box="-11 -11 -11 11 -9 11", indices="0", drawSize="0")
       cube.addObject('FixedProjectiveConstraint', template="Vec3", name="default27", indices="@box_roi.indices", drawSize="0")

       tetra = Cube.addChild('Tetra', gravity="0 -9.81 0")

       tetra.addObject('TetrahedronSetTopologyContainer', name="Container")
       tetra.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       tetra.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       tetra.addObject('Hexa2TetraTopologicalMapping', name="default28", input="@../grid", output="@Container")
       tetra.addObject('MeshExporter', filename="cube5x5x5", format="vtk", position="@../dofs.rest_position", edges="0", triangles="0", tetras="1", listening="true", exportAtBegin="true")

       triangles = Tetra.addChild('Triangles', gravity="0 -9.81 0")

       triangles.addObject('TriangleSetTopologyContainer', name="Container")
       triangles.addObject('TriangleSetTopologyModifier', name="Modifier")
       triangles.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       triangles.addObject('Tetra2TriangleTopologicalMapping', name="default29", input="@../Container", output="@Container")
       triangles.addObject('TriangleCollisionModel', name="default30")
       triangles.addObject('LineCollisionModel', name="default31")
       triangles.addObject('PointCollisionModel', name="default32")

       visu = Triangles.addChild('Visu', gravity="0 -9.81 0")

       visu.addObject('OglModel', template="Vec3", name="Visual", material="Default Diffuse 1 1 0 0 1 Ambient 1 0.2 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45")
       visu.addObject('IdentityMapping', template="Vec3,Vec3", name="default33", input="@..", output="@Visual")
       visu.addObject('VisualModelOBJExporter', filename="cube5x5x5-surface", exportAtBegin="true")
    ```

Hexa2TetraTopologicalMapping.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="0 -9.81 0" dt="0.01">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping Tetra2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
        <CollisionPipeline name="default21" verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="default22" response="PenalityContactForceField" />
        <DefaultAnimationLoop/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
        <Node name="Cube" gravity="0 -9.81 0">
            <EulerImplicitSolver name="cg_odesolver" printLog="0"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver template="GraphScattered" name="linear solver" iterations="25" tolerance="1e-09" threshold="1e-09" />
            <RegularGridTopology name="grid" n="6 6 6" min="-10 -10 -10" max="10 10 10" p0="-10 -10 -10" />
            <MechanicalObject template="Vec3" name="default24" />
            <UniformMass template="Vec3" name="default25" vertexMass="0.25" />
            <TetrahedronFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.4" youngModulus="1000" assembling="0" />
            <BoxROI template="Vec3" name="box_roi" box="-11 -11 -11 11 -9 11" indices="0" drawSize="0" />
            <FixedProjectiveConstraint template="Vec3" name="default27" indices="@box_roi.indices" drawSize="0" />
            <Node name="Tetra" gravity="0 -9.81 0">
                <TetrahedronSetTopologyContainer name="Container" />
                <TetrahedronSetTopologyModifier name="Modifier" />
                <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                <Hexa2TetraTopologicalMapping name="default28" input="@../grid" output="@Container" />
                <Node name="Triangles" gravity="0 -9.81 0">
                    <TriangleSetTopologyContainer name="Container" />
                    <TriangleSetTopologyModifier name="Modifier" />
                    <TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                    <Tetra2TriangleTopologicalMapping name="default29" input="@../Container" output="@Container" />
                    <TriangleCollisionModel name="default30" />
                    <LineCollisionModel name="default31" />
                    <PointCollisionModel name="default32" />
                    <Node name="Visu" gravity="0 -9.81 0">
                        <OglModel template="Vec3" name="Visual" material="Default Diffuse 1 1 0 0 1 Ambient 1 0.2 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45" />
                        <IdentityMapping template="Vec3,Vec3" name="default33" input="@.." output="@Visual" />
                    </Node>
                </Node>
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9.81 0", dt="0.01")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
       root.addObject('CollisionPipeline', name="default21", verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', name="default22", response="PenalityContactForceField")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")

       cube = root.addChild('Cube', gravity="0 -9.81 0")

       cube.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="0", rayleighStiffness="0.1", rayleighMass="0.1")
       cube.addObject('CGLinearSolver', template="GraphScattered", name="linear solver", iterations="25", tolerance="1e-09", threshold="1e-09")
       cube.addObject('RegularGridTopology', name="grid", n="6 6 6", min="-10 -10 -10", max="10 10 10", p0="-10 -10 -10")
       cube.addObject('MechanicalObject', template="Vec3", name="default24")
       cube.addObject('UniformMass', template="Vec3", name="default25", vertexMass="0.25")
       cube.addObject('TetrahedronFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.4", youngModulus="1000", assembling="0")
       cube.addObject('BoxROI', template="Vec3", name="box_roi", box="-11 -11 -11 11 -9 11", indices="0", drawSize="0")
       cube.addObject('FixedProjectiveConstraint', template="Vec3", name="default27", indices="@box_roi.indices", drawSize="0")

       tetra = Cube.addChild('Tetra', gravity="0 -9.81 0")

       tetra.addObject('TetrahedronSetTopologyContainer', name="Container")
       tetra.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       tetra.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       tetra.addObject('Hexa2TetraTopologicalMapping', name="default28", input="@../grid", output="@Container")

       triangles = Tetra.addChild('Triangles', gravity="0 -9.81 0")

       triangles.addObject('TriangleSetTopologyContainer', name="Container")
       triangles.addObject('TriangleSetTopologyModifier', name="Modifier")
       triangles.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       triangles.addObject('Tetra2TriangleTopologicalMapping', name="default29", input="@../Container", output="@Container")
       triangles.addObject('TriangleCollisionModel', name="default30")
       triangles.addObject('LineCollisionModel', name="default31")
       triangles.addObject('PointCollisionModel', name="default32")

       visu = Triangles.addChild('Visu', gravity="0 -9.81 0")

       visu.addObject('OglModel', template="Vec3", name="Visual", material="Default Diffuse 1 1 0 0 1 Ambient 1 0.2 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45")
       visu.addObject('IdentityMapping', template="Vec3,Vec3", name="default33", input="@..", output="@Visual")
    ```

