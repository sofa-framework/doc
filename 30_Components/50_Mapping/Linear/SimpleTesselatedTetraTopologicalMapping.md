# SimpleTesselatedTetraTopologicalMapping

Special case of mapping where TetrahedronSetTopology is converted into a finer TetrahedronSetTopology


__Target__: `Sofa.Component.Mapping.Linear`

__namespace__: `#!c++ sofa::component::mapping::linear`

__parents__: 

- `#!c++ TopologicalMapping`

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
		<td>tetrahedraMappedFromTetra</td>
		<td>
Each Tetrahedron of the input topology is mapped to the 8 tetrahedrons in which it can be divided
</td>
		<td></td>
	</tr>
	<tr>
		<td>tetraSource</td>
		<td>
Which tetra from the input topology map to a given tetra in the output topology (sofa::InvalidID if none)
</td>
		<td></td>
	</tr>
	<tr>
		<td>pointMappedFromPoint</td>
		<td>
Each point of the input topology is mapped to the same point
</td>
		<td></td>
	</tr>
	<tr>
		<td>pointMappedFromEdge</td>
		<td>
Each edge of the input topology is mapped to his midpoint
</td>
		<td></td>
	</tr>
	<tr>
		<td>pointSource</td>
		<td>
Which input topology element map to a given point in the output topology : 0 -&gt; none, &gt; 0 -&gt; point index + 1, &lt; 0 , - edge index -1
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
|input|Input topology to map|
|output|Output topology to map|



## Examples

Component/Mapping/Linear/SimpleTesselatedTetraTopologicalMapping.scn

=== "XML"

    ```xml
    <!-- -->
    <Node name="root" dt="0.05" showBoundingTree="0" gravity="0 0 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [SimpleTesselatedTetraMechanicalMapping SimpleTesselatedTetraTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedralCorotationalFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <VisualStyle displayFlags="showBehaviorModels showForceFields showCollisionModels showVisual" />
        <CollisionPipeline verbose="0" name="CollisionPipeline" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" name="collision response" />
        <DiscreteIntersection/>
        <DefaultAnimationLoop/>
        
        <Node name="TetraTopology1">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshGmshLoader name="meshLoader0" filename="mesh/liver.msh" />
            <TetrahedronSetTopologyContainer name="Container1" src="@meshLoader0" />
            <TetrahedronSetTopologyModifier />
            <TetrahedronSetGeometryAlgorithms template="Vec3" drawEdges="1" drawColorEdges="0 1 0" />
            <MechanicalObject name="dofs" />
            <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="3 39 64" />
            <DiagonalMass massDensity="1" name="computed using mass density" />
            <TetrahedralCorotationalFEMForceField name="FEM" youngModulus="3000" poissonRatio="0.3" computeGlobalMatrix="false" method="large" />
            <Node name="TetraTopology2">
                <TetrahedronSetTopologyContainer name="Container2" />
                <TetrahedronSetTopologyModifier />
                <TetrahedronSetGeometryAlgorithms template="Vec3" drawTetrahedra="1" drawColorTetrahedra="1 0 0 1" />
                <SimpleTesselatedTetraTopologicalMapping input="@Container1" output="@Container2" />
                <MechanicalObject />
                <SimpleTesselatedTetraMechanicalMapping />
                <TriangleCollisionModel />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.05", showBoundingTree="0", gravity="0 0 0")
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
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField", name="collision response")
        root.addObject('DiscreteIntersection')
        root.addObject('DefaultAnimationLoop')

        TetraTopology1 = root.addChild('TetraTopology1')
        TetraTopology1.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        TetraTopology1.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TetraTopology1.addObject('MeshGmshLoader', name="meshLoader0", filename="mesh/liver.msh")
        TetraTopology1.addObject('TetrahedronSetTopologyContainer', name="Container1", src="@meshLoader0")
        TetraTopology1.addObject('TetrahedronSetTopologyModifier')
        TetraTopology1.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", drawEdges="1", drawColorEdges="0 1 0")
        TetraTopology1.addObject('MechanicalObject', name="dofs")
        TetraTopology1.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="3 39 64")
        TetraTopology1.addObject('DiagonalMass', massDensity="1", name="computed using mass density")
        TetraTopology1.addObject('TetrahedralCorotationalFEMForceField', name="FEM", youngModulus="3000", poissonRatio="0.3", computeGlobalMatrix="false", method="large")

        TetraTopology2 = TetraTopology1.addChild('TetraTopology2')
        TetraTopology2.addObject('TetrahedronSetTopologyContainer', name="Container2")
        TetraTopology2.addObject('TetrahedronSetTopologyModifier')
        TetraTopology2.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", drawTetrahedra="1", drawColorTetrahedra="1 0 0 1")
        TetraTopology2.addObject('SimpleTesselatedTetraTopologicalMapping', input="@Container1", output="@Container2")
        TetraTopology2.addObject('MechanicalObject')
        TetraTopology2.addObject('SimpleTesselatedTetraMechanicalMapping')
        TetraTopology2.addObject('TriangleCollisionModel')
    ```

