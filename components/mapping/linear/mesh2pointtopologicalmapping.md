<!-- generate_doc -->
# Mesh2PointTopologicalMapping

This class maps any mesh primitive (point, edge, triangle...) into a point using a relative position from the primitive.


__Target__: Sofa.Component.Mapping.Linear

__namespace__: sofa::component::mapping::linear

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
list of the subsets the object belongs to
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
		<td>copyEdges</td>
		<td>
Activate mapping of input edges into the output topology (requires at least one item in pointBaryCoords)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>copyTriangles</td>
		<td>
Activate mapping of input triangles into the output topology (requires at least one item in pointBaryCoords)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>copyTetrahedra</td>
		<td>
Activate mapping of input tetrahedra into the output topology (requires at least one item in pointBaryCoords)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">BaryCoords</td>
	</tr>
	<tr>
		<td>pointBaryCoords</td>
		<td>
Coordinates for the points of the output topology created from the points of the input topology
		</td>
		<td></td>
	</tr>
	<tr>
		<td>edgeBaryCoords</td>
		<td>
Coordinates for the points of the output topology created from the edges of the input topology
		</td>
		<td></td>
	</tr>
	<tr>
		<td>triangleBaryCoords</td>
		<td>
Coordinates for the points of the output topology created from the triangles of the input topology
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quadBaryCoords</td>
		<td>
Coordinates for the points of the output topology created from the quads of the input topology
		</td>
		<td></td>
	</tr>
	<tr>
		<td>tetraBaryCoords</td>
		<td>
Coordinates for the points of the output topology created from the tetra of the input topology
		</td>
		<td></td>
	</tr>
	<tr>
		<td>hexaBaryCoords</td>
		<td>
Coordinates for the points of the output topology created from the hexa of the input topology
		</td>
		<td></td>
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

Mesh2PointTopologicalMapping.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.05" showBoundingTree="0" gravity="0 0 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [SphereCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [Mesh2PointTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedralCorotationalFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [PointSetTopologyContainer TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <VisualStyle displayFlags="showBehaviorModels showForceFields showCollisionModels showVisual" />
        <CollisionPipeline verbose="0" name="CollisionPipeline" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" name="collision response" />
        <DiscreteIntersection/>
        <DefaultAnimationLoop/>
        
        <Node name="MeshTopology">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshGmshLoader name="meshLoader0" filename="mesh/liver.msh" />
            <TetrahedronSetTopologyContainer name="Container1" src="@meshLoader0" />
            <TetrahedronSetTopologyModifier />
            <TetrahedronSetGeometryAlgorithms name="GeomAlgo" />
            <MechanicalObject name="dofs" />
            <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="3 39 64" />
            <DiagonalMass massDensity="1" name="computed using mass density" />
            <TetrahedralCorotationalFEMForceField name="FEM" youngModulus="3000" poissonRatio="0.3" computeGlobalMatrix="false" method="large" />
            <Node name="PointSetTopology">
                <PointSetTopologyContainer name="Container2" />
                <!--<PointSetTopologyModifier/>-->
                <!--<Mesh2PointTopologicalMapping input="@Container1" output="@Container2" pointBaryCoords="0 0 0" tetraBaryCoords="0.25 0.25 0.25" />-->
                <Mesh2PointTopologicalMapping input="@Container1" output="@Container2" pointBaryCoords="0 0 0" edgeBaryCoords="0.5 0.5 0.0" />
                <MechanicalObject />
                <!--<Mesh2PointMechanicalMapping/>-->
                <SphereCollisionModel radius="0.25" />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.05", showBoundingTree="0", gravity="0 0 0")

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
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields showCollisionModels showVisual")
       root.addObject('CollisionPipeline', verbose="0", name="CollisionPipeline")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', response="PenalityContactForceField", name="collision response")
       root.addObject('DiscreteIntersection', )
       root.addObject('DefaultAnimationLoop', )

       mesh_topology = root.addChild('MeshTopology')

       mesh_topology.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       mesh_topology.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       mesh_topology.addObject('MeshGmshLoader', name="meshLoader0", filename="mesh/liver.msh")
       mesh_topology.addObject('TetrahedronSetTopologyContainer', name="Container1", src="@meshLoader0")
       mesh_topology.addObject('TetrahedronSetTopologyModifier', )
       mesh_topology.addObject('TetrahedronSetGeometryAlgorithms', name="GeomAlgo")
       mesh_topology.addObject('MechanicalObject', name="dofs")
       mesh_topology.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="3 39 64")
       mesh_topology.addObject('DiagonalMass', massDensity="1", name="computed using mass density")
       mesh_topology.addObject('TetrahedralCorotationalFEMForceField', name="FEM", youngModulus="3000", poissonRatio="0.3", computeGlobalMatrix="false", method="large")

       point_set_topology = MeshTopology.addChild('PointSetTopology')

       point_set_topology.addObject('PointSetTopologyContainer', name="Container2")
       point_set_topology.addObject('Mesh2PointTopologicalMapping', input="@Container1", output="@Container2", pointBaryCoords="0 0 0", edgeBaryCoords="0.5 0.5 0.0")
       point_set_topology.addObject('MechanicalObject', )
       point_set_topology.addObject('SphereCollisionModel', radius="0.25")
    ```

