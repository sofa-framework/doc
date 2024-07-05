# SubsetTopologicalMapping

This class is a specific implementation of TopologicalMapping where the destination topology is a subset of the source topology. The implementation currently assumes that both topologies have been initialized correctly.


__Target__: `Sofa.Component.Topology.Mapping`

__namespace__: `#!c++ sofa::component::topology::mapping`

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
		<td>samePoints</td>
		<td>
True if the same set of points is used in both topologies
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>handleEdges</td>
		<td>
True if edges events and mapping should be handled
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>handleTriangles</td>
		<td>
True if triangles events and mapping should be handled
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>handleQuads</td>
		<td>
True if quads events and mapping should be handled
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>handleTetrahedra</td>
		<td>
True if tetrahedra events and mapping should be handled
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>handleHexahedra</td>
		<td>
True if hexahedra events and mapping should be handled
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>pointS2D</td>
		<td>
Internal source -&gt; destination topology points map
</td>
		<td></td>
	</tr>
	<tr>
		<td>pointD2S</td>
		<td>
Internal destination -&gt; source topology points map (link to SubsetMapping::indices to handle the mechanical-side of the mapping
</td>
		<td></td>
	</tr>
	<tr>
		<td>edgeS2D</td>
		<td>
Internal source -&gt; destination topology edges map
</td>
		<td></td>
	</tr>
	<tr>
		<td>edgeD2S</td>
		<td>
Internal destination -&gt; source topology edges map
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangleS2D</td>
		<td>
Internal source -&gt; destination topology triangles map
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangleD2S</td>
		<td>
Internal destination -&gt; source topology triangles map
</td>
		<td></td>
	</tr>
	<tr>
		<td>quadS2D</td>
		<td>
Internal source -&gt; destination topology quads map
</td>
		<td></td>
	</tr>
	<tr>
		<td>quadD2S</td>
		<td>
Internal destination -&gt; source topology quads map
</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedronS2D</td>
		<td>
Internal source -&gt; destination topology tetrahedra map
</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedronD2S</td>
		<td>
Internal destination -&gt; source topology tetrahedra map
</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedronS2D</td>
		<td>
Internal source -&gt; destination topology hexahedra map
</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedronD2S</td>
		<td>
Internal destination -&gt; source topology hexahedra map
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

Component/Topology/Mapping/SubsetTopologicalMapping2.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.05" showBoundingTree="0" gravity="0 0 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [TaitSurfacePressureForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangularFEMForceFieldOptim] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [FastTriangularBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [SubsetTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <VisualStyle displayFlags="showBehaviorModels showForceFields showCollisionModels showVisual" />
        <CollisionPipeline verbose="0" name="CollisionPipeline" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" name="collision response" />
        <DiscreteIntersection />
        <DefaultAnimationLoop/>
        
    <!--    <SplitAndAttachBodyButtonSetting button="Middle" stiffness="5000" arrowSize="0.2" snapDistance="2" />-->
        <Node name="FullTopology">
            <MeshOBJLoader name="loader" filename="mesh/sphere_05.obj" />
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <TriangleSetTopologyContainer name="Container1" src="@loader" />
            <TriangleSetTopologyModifier />
            <TriangleSetGeometryAlgorithms name="GeomAlgo" />
            <MechanicalObject name="dofs" />
            <BoxROI name="roi1" box="-55 -55 -55 55 55 -25" />
            <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="@roi1.indices" />
            <DiagonalMass massDensity="1" name="computed using mass density" />
            <TriangleCollisionModel group="1" printLog="1" />
            <TaitSurfacePressureForceField name="Pressure" gamma="5" B="10000" injectedVolume="0" printLog="1" />
            <Node name="SubsetTopology1">
                <BoxROI name="subsetROI" position="@../loader.position" triangles="@../loader.triangles" computeEdges="0" computeTetrahedra="0" box="-55 -55 25 55 55 55" />
                <TriangleSetTopologyContainer name="Container2" position="@../loader.position" triangles="@subsetROI.trianglesInROI" />
                <TriangleSetTopologyModifier />
                <TriangleSetGeometryAlgorithms name="GeomAlgo" />
                <SubsetTopologicalMapping input="@Container1" output="@Container2" samePoints="true" handleTriangles="true" printLog="1" />
                <MechanicalObject />
                <IdentityMapping />
                <TriangularFEMForceFieldOptim name="FEM1" youngModulus="1000" poissonRatio="0.3" />
                <FastTriangularBendingSprings name="Bending" bendingStiffness="100" />
                <!--<TriangleCollisionModel color="1 0 0 1" group="1" printLog="1" />-->
            </Node>
            <Node name="SubsetTopology2">
                <BoxROI name="subsetROI" position="@../loader.position" triangles="@../loader.triangles" computeEdges="0" computeTetrahedra="0" box="-55 -55 -55 55 55 25" />
                <TriangleSetTopologyContainer name="Container2" position="@../loader.position" triangles="@subsetROI.trianglesInROI" />
                <TriangleSetTopologyModifier />
                <TriangleSetGeometryAlgorithms name="GeomAlgo" />
                <SubsetTopologicalMapping input="@Container1" output="@Container2" samePoints="true" handleTriangles="true" printLog="1" />
                <MechanicalObject />
                <IdentityMapping />
                <TriangularFEMForceFieldOptim name="FEM2" youngModulus="10000" poissonRatio="0.4" />
                <FastTriangularBendingSprings name="Bending" bendingStiffness="1000" />
                <!--<TriangleCollisionModel group="1" printLog="1" />-->
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
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields showCollisionModels showVisual")
        root.addObject('CollisionPipeline', verbose="0", name="CollisionPipeline")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField", name="collision response")
        root.addObject('DiscreteIntersection')
        root.addObject('DefaultAnimationLoop')

        FullTopology = root.addChild('FullTopology')
        FullTopology.addObject('MeshOBJLoader', name="loader", filename="mesh/sphere_05.obj")
        FullTopology.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        FullTopology.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        FullTopology.addObject('TriangleSetTopologyContainer', name="Container1", src="@loader")
        FullTopology.addObject('TriangleSetTopologyModifier')
        FullTopology.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo")
        FullTopology.addObject('MechanicalObject', name="dofs")
        FullTopology.addObject('BoxROI', name="roi1", box="-55 -55 -55 55 55 -25")
        FullTopology.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="@roi1.indices")
        FullTopology.addObject('DiagonalMass', massDensity="1", name="computed using mass density")
        FullTopology.addObject('TriangleCollisionModel', group="1", printLog="1")
        FullTopology.addObject('TaitSurfacePressureForceField', name="Pressure", gamma="5", B="10000", injectedVolume="0", printLog="1")

        SubsetTopology1 = FullTopology.addChild('SubsetTopology1')
        SubsetTopology1.addObject('BoxROI', name="subsetROI", position="@../loader.position", triangles="@../loader.triangles", computeEdges="0", computeTetrahedra="0", box="-55 -55 25 55 55 55")
        SubsetTopology1.addObject('TriangleSetTopologyContainer', name="Container2", position="@../loader.position", triangles="@subsetROI.trianglesInROI")
        SubsetTopology1.addObject('TriangleSetTopologyModifier')
        SubsetTopology1.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo")
        SubsetTopology1.addObject('SubsetTopologicalMapping', input="@Container1", output="@Container2", samePoints="true", handleTriangles="true", printLog="1")
        SubsetTopology1.addObject('MechanicalObject')
        SubsetTopology1.addObject('IdentityMapping')
        SubsetTopology1.addObject('TriangularFEMForceFieldOptim', name="FEM1", youngModulus="1000", poissonRatio="0.3")
        SubsetTopology1.addObject('FastTriangularBendingSprings', name="Bending", bendingStiffness="100")

        SubsetTopology2 = FullTopology.addChild('SubsetTopology2')
        SubsetTopology2.addObject('BoxROI', name="subsetROI", position="@../loader.position", triangles="@../loader.triangles", computeEdges="0", computeTetrahedra="0", box="-55 -55 -55 55 55 25")
        SubsetTopology2.addObject('TriangleSetTopologyContainer', name="Container2", position="@../loader.position", triangles="@subsetROI.trianglesInROI")
        SubsetTopology2.addObject('TriangleSetTopologyModifier')
        SubsetTopology2.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo")
        SubsetTopology2.addObject('SubsetTopologicalMapping', input="@Container1", output="@Container2", samePoints="true", handleTriangles="true", printLog="1")
        SubsetTopology2.addObject('MechanicalObject')
        SubsetTopology2.addObject('IdentityMapping')
        SubsetTopology2.addObject('TriangularFEMForceFieldOptim', name="FEM2", youngModulus="10000", poissonRatio="0.4")
        SubsetTopology2.addObject('FastTriangularBendingSprings', name="Bending", bendingStiffness="1000")
    ```

Component/Topology/Mapping/SubsetTopologicalMapping.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.05" showBoundingTree="0" gravity="0 0 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangularFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [SubsetTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <VisualStyle displayFlags="showBehaviorModels showForceFields showCollisionModels showVisual" />
        <CollisionPipeline verbose="0" name="CollisionPipeline" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" name="collision response" />
        <DiscreteIntersection />
        <DefaultAnimationLoop/>
        
        <Node name="FullTopology">
            <MeshOBJLoader name="loader" filename="mesh/sphere_05.obj" />
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <TriangleSetTopologyContainer name="Container1" src="@loader" />
            <TriangleSetTopologyModifier />
            <TriangleSetGeometryAlgorithms name="GeomAlgo" />
            <MechanicalObject name="dofs" />
            <BoxROI name="roi1" box="-55 -55 -55 55 55 -25" />
            <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="@roi1.indices" />
            <DiagonalMass massDensity="1" name="computed using mass density" />
            <TriangularFEMForceField name="FEM" youngModulus="3000" poissonRatio="0.4" />
            <Node name="SubsetTopology1">
                <BoxROI name="subsetROI" position="@../loader.position" triangles="@../loader.triangles" computeEdges="0" computeTetrahedra="0" box="-55 -55 25 55 55 55" />
                <TriangleSetTopologyContainer name="Container2" position="@../loader.position" triangles="@subsetROI.trianglesInROI" />
                <TriangleSetTopologyModifier />
                <TriangleSetGeometryAlgorithms name="GeomAlgo" />
                <SubsetTopologicalMapping input="@Container1" output="@Container2" samePoints="true" />
                <MechanicalObject />
                <IdentityMapping />
                <TriangleCollisionModel color="1 0 0 1" group="1" printLog="1" />
            </Node>
            <Node name="SubsetTopology2">
                <BoxROI name="subsetROI" position="@../loader.position" triangles="@../loader.triangles" computeEdges="0" computeTetrahedra="0" box="-55 -55 -55 55 55 25" />
                <TriangleSetTopologyContainer name="Container2" position="@../loader.position" triangles="@subsetROI.trianglesInROI" />
                <TriangleSetTopologyModifier />
                <TriangleSetGeometryAlgorithms name="GeomAlgo" />
                <SubsetTopologicalMapping input="@Container1" output="@Container2" samePoints="true" />
                <MechanicalObject />
                <IdentityMapping />
                <TriangleCollisionModel group="1" printLog="1" />
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
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields showCollisionModels showVisual")
        root.addObject('CollisionPipeline', verbose="0", name="CollisionPipeline")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField", name="collision response")
        root.addObject('DiscreteIntersection')
        root.addObject('DefaultAnimationLoop')

        FullTopology = root.addChild('FullTopology')
        FullTopology.addObject('MeshOBJLoader', name="loader", filename="mesh/sphere_05.obj")
        FullTopology.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        FullTopology.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        FullTopology.addObject('TriangleSetTopologyContainer', name="Container1", src="@loader")
        FullTopology.addObject('TriangleSetTopologyModifier')
        FullTopology.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo")
        FullTopology.addObject('MechanicalObject', name="dofs")
        FullTopology.addObject('BoxROI', name="roi1", box="-55 -55 -55 55 55 -25")
        FullTopology.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="@roi1.indices")
        FullTopology.addObject('DiagonalMass', massDensity="1", name="computed using mass density")
        FullTopology.addObject('TriangularFEMForceField', name="FEM", youngModulus="3000", poissonRatio="0.4")

        SubsetTopology1 = FullTopology.addChild('SubsetTopology1')
        SubsetTopology1.addObject('BoxROI', name="subsetROI", position="@../loader.position", triangles="@../loader.triangles", computeEdges="0", computeTetrahedra="0", box="-55 -55 25 55 55 55")
        SubsetTopology1.addObject('TriangleSetTopologyContainer', name="Container2", position="@../loader.position", triangles="@subsetROI.trianglesInROI")
        SubsetTopology1.addObject('TriangleSetTopologyModifier')
        SubsetTopology1.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo")
        SubsetTopology1.addObject('SubsetTopologicalMapping', input="@Container1", output="@Container2", samePoints="true")
        SubsetTopology1.addObject('MechanicalObject')
        SubsetTopology1.addObject('IdentityMapping')
        SubsetTopology1.addObject('TriangleCollisionModel', color="1 0 0 1", group="1", printLog="1")

        SubsetTopology2 = FullTopology.addChild('SubsetTopology2')
        SubsetTopology2.addObject('BoxROI', name="subsetROI", position="@../loader.position", triangles="@../loader.triangles", computeEdges="0", computeTetrahedra="0", box="-55 -55 -55 55 55 25")
        SubsetTopology2.addObject('TriangleSetTopologyContainer', name="Container2", position="@../loader.position", triangles="@subsetROI.trianglesInROI")
        SubsetTopology2.addObject('TriangleSetTopologyModifier')
        SubsetTopology2.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo")
        SubsetTopology2.addObject('SubsetTopologicalMapping', input="@Container1", output="@Container2", samePoints="true")
        SubsetTopology2.addObject('MechanicalObject')
        SubsetTopology2.addObject('IdentityMapping')
        SubsetTopology2.addObject('TriangleCollisionModel', group="1", printLog="1")
    ```

