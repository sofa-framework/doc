# SubsetTopology

Engine used to create subset topology given box, sphere, plan, ...


__Templates__:

- `#!c++ Rigid3d`
- `#!c++ Vec3d`

__Target__: `Sofa.Component.Engine.Select`

__namespace__: `#!c++ sofa::component::engine::select`

__parents__: 

- `#!c++ DataEngine`

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
		<td>box</td>
		<td>
Box defined by xmin,ymin,zmin, xmax,ymax,zmax
</td>
		<td></td>
	</tr>
	<tr>
		<td>centers</td>
		<td>
Center(s) of the sphere(s)
</td>
		<td></td>
	</tr>
	<tr>
		<td>radii</td>
		<td>
Radius(i) of the sphere(s)
</td>
		<td></td>
	</tr>
	<tr>
		<td>direction</td>
		<td>
Edge direction(if edgeAngle &gt; 0)
</td>
		<td></td>
	</tr>
	<tr>
		<td>normal</td>
		<td>
Normal direction of the triangles (if triAngle &gt; 0)
</td>
		<td></td>
	</tr>
	<tr>
		<td>edgeAngle</td>
		<td>
Max angle between the direction of the selected edges and the specified direction
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>triAngle</td>
		<td>
Max angle between the normal of the selected triangle and the specified normal direction
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>rest_position</td>
		<td>
Rest position coordinates of the degrees of freedom
</td>
		<td></td>
	</tr>
	<tr>
		<td>edges</td>
		<td>
Edge Topology
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
Triangle Topology
</td>
		<td></td>
	</tr>
	<tr>
		<td>quads</td>
		<td>
Quad Topology
</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedra</td>
		<td>
Tetrahedron Topology
</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedra</td>
		<td>
Hexahedron Topology
</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedraInput</td>
		<td>
Indices of the tetrahedra to keep
</td>
		<td></td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
Indices of the points contained in the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>edgeIndices</td>
		<td>
Indices of the edges contained in the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangleIndices</td>
		<td>
Indices of the triangles contained in the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>quadIndices</td>
		<td>
Indices of the quads contained in the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedronIndices</td>
		<td>
Indices of the tetrahedra contained in the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedronIndices</td>
		<td>
Indices of the hexahedra contained in the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>pointsInROI</td>
		<td>
Points contained in the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>pointsOutROI</td>
		<td>
Points out of the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>edgesInROI</td>
		<td>
Edges contained in the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>edgesOutROI</td>
		<td>
Edges out of the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>trianglesInROI</td>
		<td>
Triangles contained in the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>trianglesOutROI</td>
		<td>
Triangles out of the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>quadsInROI</td>
		<td>
Quads contained in the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>quadsOutROI</td>
		<td>
Quads out of the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedraInROI</td>
		<td>
Tetrahedra contained in the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedraOutROI</td>
		<td>
Tetrahedra out of the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedraInROI</td>
		<td>
Hexahedra contained in the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedraOutROI</td>
		<td>
Hexahedra out of the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>nbrborder</td>
		<td>
If localIndices option is activated, will give the number of vertices on the border of the ROI (being the n first points of each output Topology). 
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>localIndices</td>
		<td>
If true, will compute local dof indices in topological elements
</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawROI</td>
		<td>
Draw ROI
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawPoints</td>
		<td>
Draw Points
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawEdges</td>
		<td>
Draw Edges
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawTriangle</td>
		<td>
Draw Triangles
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawTetrahedra</td>
		<td>
Draw Tetrahedra
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawSize</td>
		<td>
rendering size for box and topological elements
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



## Examples

Component/Engine/Select/SubsetTopology_subsetbehaviormodel.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="Root" gravity="0 0 0" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [SubsetTopology] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Tetra2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showVisual showWireframe" />
        <CollisionPipeline name="DefaultCollisionPipeline" verbose="0" draw="0" depth="6" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="Cylinder" gravity="0 -9.81 0">
            <EulerImplicitSolver name="cg_odesolver"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver template="GraphScattered" name="default18" iterations="100" tolerance="1e-05" threshold="1e-05"/>
            <MechanicalObject template="Rigid3" name="rigid" position="0 0 0 0 0 0 1" velocity="0 0 0 0 0 0" force="0 0 0 0 0 0" externalForce="0 0 0 0 0 0" derivX="0 0 0 0 0 0" free_position="0 0 0 0 0 0 1" free_velocity="0 0 0 0 0 0" restScale="1" />
            <UniformMass name="default0" />
            <Node name="topology" gravity="0 -9.81 0">
                <MeshGmshLoader name="loader" filename="mesh/truthcylinder1.msh" />
                <MeshTopology src="@loader" name="meshTopology" />
                <SubsetTopology template="Vec3" name="Subset" box="-5 -20 -5 5 -10 5" rest_position="@meshTopology.position" edges="@meshTopology.edges" triangles="@meshTopology.triangles" tetrahedra="@meshTopology.tetrahedra" indices="0" localIndices="1" drawROI="0" />
                <OglModel template="Vec3" name="visual" position="@meshTopology.position" useNormals="0" computeTangents="1" vertices="@meshTopology.position" triangles="@meshTopology.triangles" material="Default Diffuse 1 0.74902 0.74902 0.74902 1 Ambient 1 0.2 0.2 0.2 1 Specular 0 1 1 1 1 Emissive 0 0 0 0 0 Shininess 0 45" />
                <RigidMapping template="Rigid3,Vec3" name="default15" mapForces="0" mapConstraints="0" mapMasses="0" input="@.." output="@visual" />
            </Node>
            <Node name="InROI" gravity="0 -9.81 0">
                <MechanicalObject template="Vec3" name="mobj" position="@../topology/Subset.pointsInROI" velocity="0 0 0" force="0 0 0" externalForce="0 0 0" derivX="0 0 0" free_position="0 0 0" free_velocity="0 0 0" restScale="1" />
                <TetrahedronSetTopologyContainer name="container" position="@../topology/Subset.pointsInROI" tetrahedra="@../topology/Subset.tetrahedraInROI" />
                <TetrahedronSetTopologyModifier name="default10" />
                <TetrahedronSetGeometryAlgorithms template="Vec3" name="default12" />
                <UniformMass name="mass" vertexMass="15" />
                <TetrahedronFEMForceField template="Vec3" name="FEM" poissonRatio="0.49" youngModulus="1000" gatherPt=" " gatherBsize=" " />
                <RigidMapping template="Rigid3,Vec3" name="rigidMapping" input="@.." output="@." />
                <Node name="Surf" gravity="0 -9.81 0">
                    <VisualStyle displayFlags="hideWireframe" />
                    <TriangleSetTopologyContainer name="container" />
                    <TriangleSetGeometryAlgorithms template="Vec3" />
                    <TriangleSetTopologyModifier />
                    <Tetra2TriangleTopologicalMapping input="@../container" output="@container" />
                    <TriangleCollisionModel template="Vec3" />
                </Node>
            </Node>
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
        Root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        Root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        Root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        Root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        Root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        Root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        Root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        Root.addObject('DefaultAnimationLoop')
        Root.addObject('VisualStyle', displayFlags="showVisual showWireframe")
        Root.addObject('CollisionPipeline', name="DefaultCollisionPipeline", verbose="0", draw="0", depth="6")
        Root.addObject('BruteForceBroadPhase')
        Root.addObject('BVHNarrowPhase')
        Root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
        Root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

        Cylinder = Root.addChild('Cylinder', gravity="0 -9.81 0")
        Cylinder.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        Cylinder.addObject('CGLinearSolver', template="GraphScattered", name="default18", iterations="100", tolerance="1e-05", threshold="1e-05")
        Cylinder.addObject('MechanicalObject', template="Rigid3", name="rigid", position="0 0 0 0 0 0 1", velocity="0 0 0 0 0 0", force="0 0 0 0 0 0", externalForce="0 0 0 0 0 0", derivX="0 0 0 0 0 0", free_position="0 0 0 0 0 0 1", free_velocity="0 0 0 0 0 0", restScale="1")
        Cylinder.addObject('UniformMass', name="default0")

        topology = Cylinder.addChild('topology', gravity="0 -9.81 0")
        topology.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
        topology.addObject('MeshTopology', src="@loader", name="meshTopology")
        topology.addObject('SubsetTopology', template="Vec3", name="Subset", box="-5 -20 -5 5 -10 5", rest_position="@meshTopology.position", edges="@meshTopology.edges", triangles="@meshTopology.triangles", tetrahedra="@meshTopology.tetrahedra", indices="0", localIndices="1", drawROI="0")
        topology.addObject('OglModel', template="Vec3", name="visual", position="@meshTopology.position", useNormals="0", computeTangents="1", vertices="@meshTopology.position", triangles="@meshTopology.triangles", material="Default Diffuse 1 0.74902 0.74902 0.74902 1 Ambient 1 0.2 0.2 0.2 1 Specular 0 1 1 1 1 Emissive 0 0 0 0 0 Shininess 0 45")
        topology.addObject('RigidMapping', template="Rigid3,Vec3", name="default15", mapForces="0", mapConstraints="0", mapMasses="0", input="@..", output="@visual")

        InROI = Cylinder.addChild('InROI', gravity="0 -9.81 0")
        InROI.addObject('MechanicalObject', template="Vec3", name="mobj", position="@../topology/Subset.pointsInROI", velocity="0 0 0", force="0 0 0", externalForce="0 0 0", derivX="0 0 0", free_position="0 0 0", free_velocity="0 0 0", restScale="1")
        InROI.addObject('TetrahedronSetTopologyContainer', name="container", position="@../topology/Subset.pointsInROI", tetrahedra="@../topology/Subset.tetrahedraInROI")
        InROI.addObject('TetrahedronSetTopologyModifier', name="default10")
        InROI.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="default12")
        InROI.addObject('UniformMass', name="mass", vertexMass="15")
        InROI.addObject('TetrahedronFEMForceField', template="Vec3", name="FEM", poissonRatio="0.49", youngModulus="1000", gatherPt=" ", gatherBsize=" ")
        InROI.addObject('RigidMapping', template="Rigid3,Vec3", name="rigidMapping", input="@..", output="@.")

        Surf = InROI.addChild('Surf', gravity="0 -9.81 0")
        Surf.addObject('VisualStyle', displayFlags="hideWireframe")
        Surf.addObject('TriangleSetTopologyContainer', name="container")
        Surf.addObject('TriangleSetGeometryAlgorithms', template="Vec3")
        Surf.addObject('TriangleSetTopologyModifier')
        Surf.addObject('Tetra2TriangleTopologicalMapping', input="@../container", output="@container")
        Surf.addObject('TriangleCollisionModel', template="Vec3")
    ```

Component/Engine/Select/SubsetTopology_withtetrahedra.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.05" gravity="0 -9.81 0" showBoundingTree="0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedPlaneProjectiveConstraint FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [SubsetTopology] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [TrianglePressureForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedralCorotationalFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [TriangularBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Tetra2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showWireframe" />
        <CollisionPipeline verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
        <Node name="TT">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshGmshLoader name="loader" filename="mesh/cylinder.msh" />
            <MechanicalObject src="@loader" name="Volume" />
            <include href="Objects/TetrahedronSetTopology.xml" src="@loader" />
            <DiagonalMass massDensity="0.5" />
            <FixedPlaneProjectiveConstraint direction="0 0 1" dmin="-0.1" dmax="0.1" />
            <FixedProjectiveConstraint indices="0" />
            <TetrahedralCorotationalFEMForceField name="FEM" youngModulus="30" poissonRatio="0.3" method="large" />
            <SubsetTopology template="Vec3" box="0 0 0 0.3 0.3 0.5" tetrahedra="@Container.tetrahedra" drawTetrahedra="1" drawROI="1" rest_position="@Volume.position" name="Subset" />
            <Node name="T">
                <include href="Objects/TriangleSetTopology.xml" src="@../loader" tags=" " />
                <Tetra2TriangleTopologicalMapping input="@../Container" output="@Container" />
                <TriangularBendingSprings name="FEM-Bend" stiffness="100" damping="1.0" />
                <TrianglePressureForceField normal="0 0 1" dmin="0.9" dmax="1.1" pressure="0.4 0 0" />
                <TriangleCollisionModel />
                <Node name="Visu">
                    <OglModel template="Vec3" name="Visual" material="Default Diffuse 1 0 0 1 0.5 Ambient 1 0.2 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45" />
                    <IdentityMapping input="@../../Volume" output="@Visual" />
                </Node>
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.05", gravity="0 -9.81 0", showBoundingTree="0")
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
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showWireframe")
        root.addObject('CollisionPipeline', verbose="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField")
        root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")

        TT = root.addChild('TT')
        TT.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        TT.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TT.addObject('MeshGmshLoader', name="loader", filename="mesh/cylinder.msh")
        TT.addObject('MechanicalObject', src="@loader", name="Volume")
        TT.addObject('include', href="Objects/TetrahedronSetTopology.xml", src="@loader")
        TT.addObject('DiagonalMass', massDensity="0.5")
        TT.addObject('FixedPlaneProjectiveConstraint', direction="0 0 1", dmin="-0.1", dmax="0.1")
        TT.addObject('FixedProjectiveConstraint', indices="0")
        TT.addObject('TetrahedralCorotationalFEMForceField', name="FEM", youngModulus="30", poissonRatio="0.3", method="large")
        TT.addObject('SubsetTopology', template="Vec3", box="0 0 0 0.3 0.3 0.5", tetrahedra="@Container.tetrahedra", drawTetrahedra="1", drawROI="1", rest_position="@Volume.position", name="Subset")

        T = TT.addChild('T')
        T.addObject('include', href="Objects/TriangleSetTopology.xml", src="@../loader", tags=" ")
        T.addObject('Tetra2TriangleTopologicalMapping', input="@../Container", output="@Container")
        T.addObject('TriangularBendingSprings', name="FEM-Bend", stiffness="100", damping="1.0")
        T.addObject('TrianglePressureForceField', normal="0 0 1", dmin="0.9", dmax="1.1", pressure="0.4 0 0")
        T.addObject('TriangleCollisionModel')

        Visu = T.addChild('Visu')
        Visu.addObject('OglModel', template="Vec3", name="Visual", material="Default Diffuse 1 0 0 1 0.5 Ambient 1 0.2 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45")
        Visu.addObject('IdentityMapping', input="@../../Volume", output="@Visual")
    ```

Component/Engine/Select/SubsetTopology.scn

=== "XML"

    ```xml
    <Node name="root" gravity="0 -9.81 0" dt="0.05">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [SubsetTopology] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangularFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [TriangularBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <CollisionPipeline name="default0" verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="default1" response="PenalityContactForceField" />
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
        <Node name="SquareGravity">
            <MeshGmshLoader name="meshLoader" filename="mesh/square3.msh" />
            <EulerImplicitSolver name="cg_odesolver"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="100" tolerance="1e-05" threshold="1e-05"/>
            <SubsetTopology template="Vec3" box="0.3 0 -0.1 0.6 1 0.1" drawTriangle="0" drawROI="1" src="@meshLoader" rest_position="@meshLoader.position" name="Subset" />
            <Node name="in">
                <MechanicalObject template="Vec3" name="mecaObj2" position="@../meshLoader.position" />
                <TriangleSetTopologyContainer name="Container" position="@mecaObj2.position" triangles="@../Subset.trianglesInROI" />
                <TriangleSetTopologyModifier name="Modifier" />
                <TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                <DiagonalMass name="default5" massDensity="1.15" />
                <TriangularFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.3" youngModulus="30" />
                <TriangularBendingSprings template="Vec3" name="FEM-Bend" stiffness="300" damping="1" />
                <TriangleCollisionModel template="Vec3" name="default7" />
    
                <Node >
                  <OglModel name="Visual" color="blue" />
                  <IdentityMapping input="@.." output="@Visual" />
                </Node>        </Node>
            <Node name="Out">
                <MechanicalObject template="Vec3" name="mecaObj2" position="@../meshLoader.position" />
                <TriangleSetTopologyContainer name="Container" position="@mecaObj2.position" triangles="@../Subset.trianglesOutROI" />
                <TriangleSetTopologyModifier name="Modifier" />
                <TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                <DiagonalMass name="default5" massDensity="1.15" />
                <TriangularFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.3" youngModulus="30" />
                <TriangularBendingSprings template="Vec3" name="FEM-Bend" stiffness="300" damping="1" />
                <TriangleCollisionModel template="Vec3" name="default7" />
                <FixedProjectiveConstraint template="Vec3" name="default6" indices="0 1" />
                <Node >
                  <OglModel name="Visual" color="red" />
                  <IdentityMapping input="@.." output="@Visual" />
                </Node>
    	 </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -9.81 0", dt="0.05")
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
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')
        root.addObject('CollisionPipeline', name="default0", verbose="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', name="default1", response="PenalityContactForceField")
        root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")

        SquareGravity = root.addChild('SquareGravity')
        SquareGravity.addObject('MeshGmshLoader', name="meshLoader", filename="mesh/square3.msh")
        SquareGravity.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        SquareGravity.addObject('CGLinearSolver', iterations="100", tolerance="1e-05", threshold="1e-05")
        SquareGravity.addObject('SubsetTopology', template="Vec3", box="0.3 0 -0.1 0.6 1 0.1", drawTriangle="0", drawROI="1", src="@meshLoader", rest_position="@meshLoader.position", name="Subset")

        in = SquareGravity.addChild('in')
        in.addObject('MechanicalObject', template="Vec3", name="mecaObj2", position="@../meshLoader.position")
        in.addObject('TriangleSetTopologyContainer', name="Container", position="@mecaObj2.position", triangles="@../Subset.trianglesInROI")
        in.addObject('TriangleSetTopologyModifier', name="Modifier")
        in.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        in.addObject('DiagonalMass', name="default5", massDensity="1.15")
        in.addObject('TriangularFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.3", youngModulus="30")
        in.addObject('TriangularBendingSprings', template="Vec3", name="FEM-Bend", stiffness="300", damping="1")
        in.addObject('TriangleCollisionModel', template="Vec3", name="default7")

        in = in.addChild('in')
        in.addObject('OglModel', name="Visual", color="blue")
        in.addObject('IdentityMapping', input="@..", output="@Visual")

        Out = SquareGravity.addChild('Out')
        Out.addObject('MechanicalObject', template="Vec3", name="mecaObj2", position="@../meshLoader.position")
        Out.addObject('TriangleSetTopologyContainer', name="Container", position="@mecaObj2.position", triangles="@../Subset.trianglesOutROI")
        Out.addObject('TriangleSetTopologyModifier', name="Modifier")
        Out.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        Out.addObject('DiagonalMass', name="default5", massDensity="1.15")
        Out.addObject('TriangularFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.3", youngModulus="30")
        Out.addObject('TriangularBendingSprings', template="Vec3", name="FEM-Bend", stiffness="300", damping="1")
        Out.addObject('TriangleCollisionModel', template="Vec3", name="default7")
        Out.addObject('FixedProjectiveConstraint', template="Vec3", name="default6", indices="0 1")

        Out = Out.addChild('Out')
        Out.addObject('OglModel', name="Visual", color="red")
        Out.addObject('IdentityMapping', input="@..", output="@Visual")
    ```

Component/Engine/Select/SubsetTopology_refiningMesh.scn

=== "XML"

    ```xml
    <Node name="root" gravity="-9.81 0 0" dt="0.05">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI SubsetTopology] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [StiffSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [SparseGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Tetra2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <CollisionPipeline name="DefaultCollisionPipeline" verbose="0" draw="0" depth="6" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="3" contactDistance="2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="SquareGravity">
            <EulerImplicitSolver name="cg_odesolver"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="100" tolerance="1e-5" threshold="1e-5"/>
            <MeshGmshLoader name="meshLoader" filename="mesh/truthcylinder1.msh" />
            <SubsetTopology template="Vec3" box="-5 -20 -5 5 -10 5" drawROI="0" src="@meshLoader" rest_position="@meshLoader.position" name="Subset" localIndices="1" />
            <Node name="in">
                <MechanicalObject template="Vec3" name="mecaObj1" position="@../Subset.pointsInROI" />
                <TetrahedronSetTopologyContainer name="Container" position="@mecaObj1.position" tetrahedra="@../Subset.tetrahedraInROI" />
                <TetrahedronSetTopologyModifier name="Modifier" />
                <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" drawTetrahedra="0" />
                <UniformMass totalMass="15" />
                <TetrahedronFEMForceField name="FEM" youngModulus="300" poissonRatio="0.49" />
                <TriangleCollisionModel template="Vec3" name="default7" />
                <BoxConstraint box_roi="fixedROI" box="-5 -20 -5 5 -17.5 5" drawBoxes="1" />
                <Node>
                    <TriangleSetTopologyContainer name="ContainerTri" />
                    <TriangleSetTopologyModifier name="Modifier" />
                    <TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                    <Tetra2TriangleTopologicalMapping name="Mapping" input="@../Container" output="@ContainerTri" />
                    <OglModel name="Visual" color="red" dx="60" />
                    <IdentityMapping input="@.." output="@Visual" />
                </Node>
            </Node>
            <Node name="Out">
                <MechanicalObject template="Vec3" name="mecaObj2" />
                <SparseGridTopology n="4 7 4" position="@../Subset.pointsOutROI" name="name" drawHexahedra="0" />
                <UniformMass totalMass="15" />
                <HexahedronFEMForceField template="Vec3" name="FEM" youngModulus="50" poissonRatio="0.49" />
                <Node name="tetra">
                    <TetrahedronSetTopologyContainer name="Container" position="@../../Subset.pointsOutROI" tetrahedra="@../../Subset.tetrahedraOutROI" />
                    <TetrahedronSetTopologyModifier name="Modifier" />
                    <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" drawTetrahedra="0" />
                    <MechanicalObject name="mecaObj3" />
                    <BarycentricMapping input="@.." output="@." />
                    <Node>
                        <TriangleSetTopologyContainer name="ContainerTri" />
                        <TriangleSetTopologyModifier name="Modifier" />
                        <TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                        <Tetra2TriangleTopologicalMapping name="Mapping" input="@../Container" output="@ContainerTri" />
                        <TriangleCollisionModel template="Vec3" name="default7" />
                        <OglModel name="Visual" color="blue" dx="60" />
                        <IdentityMapping input="@.." output="@Visual" />
                    </Node>
                </Node>
            </Node>
            <StiffSpringForceField name="Spring" object1="@in/mecaObj1" object2="@Out/tetra/mecaObj3" tags="extraSpring" spring="0 0 10000 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;       1 1 10000 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;       2 2 10000 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;       3 3 10000 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;       4 4 10000 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;       5 5 10000 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;       6 6 10000 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;       7 7 10000 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;       8 8 10000 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;       9 9 10000 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;       10 10 10000 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;       11 11 10000 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;       12 12 10000 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;       13 13 10000 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;       14 14 10000 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;       15 15 10000 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;       16 16 10000 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;       17 17 10000 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;       18 18 10000 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;       19 19 10000 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;       20 20 10000 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;       21 21 10000 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;       22 22 10000 0 0" />
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="-9.81 0 0", dt="0.05")
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
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
        root.addObject('CollisionPipeline', name="DefaultCollisionPipeline", verbose="0", draw="0", depth="6")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="3", contactDistance="2")
        root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

        SquareGravity = root.addChild('SquareGravity')
        SquareGravity.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        SquareGravity.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")
        SquareGravity.addObject('MeshGmshLoader', name="meshLoader", filename="mesh/truthcylinder1.msh")
        SquareGravity.addObject('SubsetTopology', template="Vec3", box="-5 -20 -5 5 -10 5", drawROI="0", src="@meshLoader", rest_position="@meshLoader.position", name="Subset", localIndices="1")

        in = SquareGravity.addChild('in')
        in.addObject('MechanicalObject', template="Vec3", name="mecaObj1", position="@../Subset.pointsInROI")
        in.addObject('TetrahedronSetTopologyContainer', name="Container", position="@mecaObj1.position", tetrahedra="@../Subset.tetrahedraInROI")
        in.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        in.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo", drawTetrahedra="0")
        in.addObject('UniformMass', totalMass="15")
        in.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="300", poissonRatio="0.49")
        in.addObject('TriangleCollisionModel', template="Vec3", name="default7")
        in.addObject('BoxConstraint', box_roi="fixedROI", box="-5 -20 -5 5 -17.5 5", drawBoxes="1")

        in = in.addChild('in')
        in.addObject('TriangleSetTopologyContainer', name="ContainerTri")
        in.addObject('TriangleSetTopologyModifier', name="Modifier")
        in.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        in.addObject('Tetra2TriangleTopologicalMapping', name="Mapping", input="@../Container", output="@ContainerTri")
        in.addObject('OglModel', name="Visual", color="red", dx="60")
        in.addObject('IdentityMapping', input="@..", output="@Visual")

        Out = SquareGravity.addChild('Out')
        Out.addObject('MechanicalObject', template="Vec3", name="mecaObj2")
        Out.addObject('SparseGridTopology', n="4 7 4", position="@../Subset.pointsOutROI", name="name", drawHexahedra="0")
        Out.addObject('UniformMass', totalMass="15")
        Out.addObject('HexahedronFEMForceField', template="Vec3", name="FEM", youngModulus="50", poissonRatio="0.49")

        tetra = Out.addChild('tetra')
        tetra.addObject('TetrahedronSetTopologyContainer', name="Container", position="@../../Subset.pointsOutROI", tetrahedra="@../../Subset.tetrahedraOutROI")
        tetra.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        tetra.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo", drawTetrahedra="0")
        tetra.addObject('MechanicalObject', name="mecaObj3")
        tetra.addObject('BarycentricMapping', input="@..", output="@.")

        tetra = tetra.addChild('tetra')
        tetra.addObject('TriangleSetTopologyContainer', name="ContainerTri")
        tetra.addObject('TriangleSetTopologyModifier', name="Modifier")
        tetra.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        tetra.addObject('Tetra2TriangleTopologicalMapping', name="Mapping", input="@../Container", output="@ContainerTri")
        tetra.addObject('TriangleCollisionModel', template="Vec3", name="default7")
        tetra.addObject('OglModel', name="Visual", color="blue", dx="60")
        tetra.addObject('IdentityMapping', input="@..", output="@Visual")
        SquareGravity.addObject('StiffSpringForceField', name="Spring", object1="@in/mecaObj1", object2="@Out/tetra/mecaObj3", tags="extraSpring", spring="0 0 10000 0 0
					       1 1 10000 0 0
					       2 2 10000 0 0
					       3 3 10000 0 0
					       4 4 10000 0 0
					       5 5 10000 0 0
					       6 6 10000 0 0
					       7 7 10000 0 0
					       8 8 10000 0 0
					       9 9 10000 0 0
					       10 10 10000 0 0
					       11 11 10000 0 0
					       12 12 10000 0 0
					       13 13 10000 0 0
					       14 14 10000 0 0
					       15 15 10000 0 0
					       16 16 10000 0 0
					       17 17 10000 0 0
					       18 18 10000 0 0
					       19 19 10000 0 0
					       20 20 10000 0 0
					       21 21 10000 0 0
					       22 22 10000 0 0")
    ```

Component/Engine/Select/SubsetTopology_localIndicesOption.scn

=== "XML"

    ```xml
    <Node name="root" gravity="0 -9.81 0" dt="0.05">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [SubsetTopology] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangularFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [TriangularBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels" />
        <CollisionPipeline name="default0" verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="default1" response="PenalityContactForceField" />
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
        <Node name="SquareGravity">
            <EulerImplicitSolver name="cg_odesolver"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="100" tolerance="1e-5" threshold="1e-5"/>
            <MeshGmshLoader name="meshLoader" filename="mesh/square3.msh" />
            <SubsetTopology template="Vec3" box="0.3 0 -0.1 0.6 1 0.1" drawROI="1" src="@meshLoader" rest_position="@meshLoader.position" name="Subset" localIndices="1" />
            <Node name="in">
                <MechanicalObject template="Vec3" name="mecaObj2" position="@../Subset.pointsInROI" />
                <TriangleSetTopologyContainer name="Container" position="@mecaObj2.position" triangles="@../Subset.trianglesInROI" />
                <TriangleSetTopologyModifier name="Modifier" />
                <TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                <DiagonalMass name="default5" massDensity="1.15" />
                <TriangularFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.3" youngModulus="60" />
                <TriangularBendingSprings template="Vec3" name="FEM-Bend" stiffness="300" damping="1" />
                <TriangleCollisionModel template="Vec3" name="default7" />
    
                <Node >
                  <OglModel name="Visual" color="blue" />
                  <IdentityMapping input="@.." output="@Visual" />
                </Node>        </Node>
            <Node name="Out">
                <MechanicalObject template="Vec3" name="mecaObj2" position="@../Subset.pointsOutROI" />
                <TriangleSetTopologyContainer name="Container" position="@mecaObj2.position" triangles="@../Subset.trianglesOutROI" />
                <TriangleSetTopologyModifier name="Modifier" />
                <TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                <DiagonalMass name="default5" massDensity="1.15" />
                <TriangleCollisionModel template="Vec3" name="default7" />
                <TriangularFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.3" youngModulus="60" />
                <TriangularBendingSprings template="Vec3" name="FEM-Bend" stiffness="300" damping="1" />
                <FixedProjectiveConstraint template="Vec3" name="default6" indices="0 1" />
    
                <Node >
                  <OglModel name="Visual" color="red" />
                  <IdentityMapping input="@.." output="@Visual" />
                </Node>
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -9.81 0", dt="0.05")
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
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')
        root.addObject('VisualStyle', displayFlags="showBehaviorModels")
        root.addObject('CollisionPipeline', name="default0", verbose="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', name="default1", response="PenalityContactForceField")
        root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")

        SquareGravity = root.addChild('SquareGravity')
        SquareGravity.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        SquareGravity.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")
        SquareGravity.addObject('MeshGmshLoader', name="meshLoader", filename="mesh/square3.msh")
        SquareGravity.addObject('SubsetTopology', template="Vec3", box="0.3 0 -0.1 0.6 1 0.1", drawROI="1", src="@meshLoader", rest_position="@meshLoader.position", name="Subset", localIndices="1")

        in = SquareGravity.addChild('in')
        in.addObject('MechanicalObject', template="Vec3", name="mecaObj2", position="@../Subset.pointsInROI")
        in.addObject('TriangleSetTopologyContainer', name="Container", position="@mecaObj2.position", triangles="@../Subset.trianglesInROI")
        in.addObject('TriangleSetTopologyModifier', name="Modifier")
        in.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        in.addObject('DiagonalMass', name="default5", massDensity="1.15")
        in.addObject('TriangularFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.3", youngModulus="60")
        in.addObject('TriangularBendingSprings', template="Vec3", name="FEM-Bend", stiffness="300", damping="1")
        in.addObject('TriangleCollisionModel', template="Vec3", name="default7")

        in = in.addChild('in')
        in.addObject('OglModel', name="Visual", color="blue")
        in.addObject('IdentityMapping', input="@..", output="@Visual")

        Out = SquareGravity.addChild('Out')
        Out.addObject('MechanicalObject', template="Vec3", name="mecaObj2", position="@../Subset.pointsOutROI")
        Out.addObject('TriangleSetTopologyContainer', name="Container", position="@mecaObj2.position", triangles="@../Subset.trianglesOutROI")
        Out.addObject('TriangleSetTopologyModifier', name="Modifier")
        Out.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        Out.addObject('DiagonalMass', name="default5", massDensity="1.15")
        Out.addObject('TriangleCollisionModel', template="Vec3", name="default7")
        Out.addObject('TriangularFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.3", youngModulus="60")
        Out.addObject('TriangularBendingSprings', template="Vec3", name="FEM-Bend", stiffness="300", damping="1")
        Out.addObject('FixedProjectiveConstraint', template="Vec3", name="default6", indices="0 1")

        Out = Out.addChild('Out')
        Out.addObject('OglModel', name="Visual", color="red")
        Out.addObject('IdentityMapping', input="@..", output="@Visual")
    ```

