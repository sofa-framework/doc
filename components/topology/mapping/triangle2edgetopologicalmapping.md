<!-- generate_doc -->
# Triangle2EdgeTopologicalMapping

Topological mapping where TriangleSetTopology is converted to EdgeSetTopology


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

Triangle2EdgeTopologicalMapping.scn

=== "XML"

    ```xml
    <!-- Mechanical MassSpring Group Basic Example -->
    <Node name="root" dt="0.05" showBoundingTree="0" gravity="0 -9 1">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangularFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [SpringForceField TriangularBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [EdgeSetGeometryAlgorithms EdgeSetTopologyContainer EdgeSetTopologyModifier TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Triangle2EdgeTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
        <CollisionPipeline verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
        <DefaultAnimationLoop/>
        
        <Node name="SquareGravity">
            <CGImplicit iterations="40" tolerance="1e-6" threshold="1e-10" />
            <MeshGmshLoader name="loader" filename="mesh/square3.msh" createSubelements="true" />
            <MechanicalObject src="@loader" scale="10" />
            <include href="Objects/TriangleSetTopology.xml" src="@loader" />
            <DiagonalMass massDensity="0.15" />
            <FixedProjectiveConstraint indices="0 1" />
            <SpringForceField name="FF" />
            <TriangularFEMForceField name="FEM" youngModulus="60" poissonRatio="0.3" method="large" />
            <TriangularBendingSprings name="FEM-Bend" stiffness="300" damping="1.0" />
            <TriangleCollisionModel />
            
            <Node >
              <OglModel name="Visual" color="red" />
              <IdentityMapping input="@.." output="@Visual" />
            </Node>
    
            <Node name="Edge Mesh">
                <EdgeSetTopologyContainer name="Container" />
                <EdgeSetTopologyModifier name="Modifier" />
                <EdgeSetGeometryAlgorithms template="Vec3" name="GeomAlgo" drawEdges="1" />
                <Triangle2EdgeTopologicalMapping name="Mapping" input="@../Container" output="@Container" />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.05", showBoundingTree="0", gravity="0 -9 1")

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
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
       root.addObject('CollisionPipeline', verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', response="PenalityContactForceField")
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")
       root.addObject('DefaultAnimationLoop', )

       square_gravity = root.addChild('SquareGravity')

       square_gravity.addObject('CGImplicit', iterations="40", tolerance="1e-6", threshold="1e-10")
       square_gravity.addObject('MeshGmshLoader', name="loader", filename="mesh/square3.msh", createSubelements="true")
       square_gravity.addObject('MechanicalObject', src="@loader", scale="10")
       square_gravity.addObject('include', href="Objects/TriangleSetTopology.xml", src="@loader")
       square_gravity.addObject('DiagonalMass', massDensity="0.15")
       square_gravity.addObject('FixedProjectiveConstraint', indices="0 1")
       square_gravity.addObject('SpringForceField', name="FF")
       square_gravity.addObject('TriangularFEMForceField', name="FEM", youngModulus="60", poissonRatio="0.3", method="large")
       square_gravity.addObject('TriangularBendingSprings', name="FEM-Bend", stiffness="300", damping="1.0")
       square_gravity.addObject('TriangleCollisionModel', )

       node = SquareGravity.addChild('node')

       node.addObject('OglModel', name="Visual", color="red")
       node.addObject('IdentityMapping', input="@..", output="@Visual")

       edge__mesh = SquareGravity.addChild('Edge Mesh')

       edge__mesh.addObject('EdgeSetTopologyContainer', name="Container")
       edge__mesh.addObject('EdgeSetTopologyModifier', name="Modifier")
       edge__mesh.addObject('EdgeSetGeometryAlgorithms', template="Vec3", name="GeomAlgo", drawEdges="1")
       edge__mesh.addObject('Triangle2EdgeTopologicalMapping', name="Mapping", input="@../Container", output="@Container")
    ```

