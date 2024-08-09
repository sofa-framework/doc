<!-- generate_doc -->
# SphereROI

Find the primitives (vertex/edge/triangle/tetrahedron) inside a given sphere


Templates:

- Rigid3d
- Vec3d

__Target__: Sofa.Component.Engine.Select

__namespace__: sofa::component::engine::select

__parents__:

- BaseROI

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
		<td>computeEdges</td>
		<td>
If true, will compute edge list and index list inside the ROI.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>computeTriangles</td>
		<td>
If true, will compute triangle list and index list inside the ROI.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>computeQuads</td>
		<td>
If true, will compute quad list and index list inside the ROI.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>computeTetrahedra</td>
		<td>
If true, will compute tetrahedra list and index list inside the ROI.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>computeHexahedra</td>
		<td>
If true, will compute hexahedra list and index list inside the ROI.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>strict</td>
		<td>
If true, an element is inside the box if all of its nodes are inside. If False, only the center point of the element is checked.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>doUpdate</td>
		<td>
If true, updates the selection at the beginning of simulation steps.
		</td>
		<td>1</td>
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
Edge direction(if edgeAngle > 0)
		</td>
		<td></td>
	</tr>
	<tr>
		<td>normal</td>
		<td>
Normal direction of the triangles (if triAngle > 0)
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
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Rest position coordinates of the degrees of freedom. 
If empty the positions from a MechanicalObject then a MeshLoader are searched in the current context. 
If none are found the parent's context is searched for MechanicalObject.
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
		<td colspan="3">Outputs</td>
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
Indices of the quad contained in the ROI
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
		<td>edgesInROI</td>
		<td>
Edges contained in the ROI
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
		<td>quadsInROI</td>
		<td>
Quad contained in the ROI
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
		<td>hexahedraInROI</td>
		<td>
Hexahedra contained in the ROI
		</td>
		<td></td>
	</tr>
	<tr>
		<td>nbIndices</td>
		<td>
Number of selected indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>pointsOutROI</td>
		<td>
Points not contained in the ROI
		</td>
		<td></td>
	</tr>
	<tr>
		<td>edgesOutROI</td>
		<td>
Edges not contained in the ROI
		</td>
		<td></td>
	</tr>
	<tr>
		<td>trianglesOutROI</td>
		<td>
Triangles not contained in the ROI
		</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedraOutROI</td>
		<td>
Tetrahedra not contained in the ROI
		</td>
		<td></td>
	</tr>
	<tr>
		<td>indicesOut</td>
		<td>
Indices of the points not contained in the ROI
		</td>
		<td></td>
	</tr>
	<tr>
		<td>edgeOutIndices</td>
		<td>
Indices of the edges not contained in the ROI
		</td>
		<td></td>
	</tr>
	<tr>
		<td>triangleOutIndices</td>
		<td>
Indices of the triangles not contained in the ROI
		</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedronOutIndices</td>
		<td>
Indices of the tetrahedra not contained in the ROI
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawROI</td>
		<td>
Draw the ROI.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawPoints</td>
		<td>
Draw Points.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawEdges</td>
		<td>
Draw Edges.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawTriangles</td>
		<td>
Draw Triangles.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawQuads</td>
		<td>
Draw Quads.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawTetrahedra</td>
		<td>
Draw Tetrahedra.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawHexahedra</td>
		<td>
Draw Tetrahedra.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawSize</td>
		<td>
rendering size for ROI and topological elements
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

SphereROI.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.05" showBoundingTree="0" gravity="0 -9 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [SphereROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [TrianglePressureForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedralCorotationalFEMForceField TriangularFEMForceField] -->
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
            <SphereROI centers="0 0 0" radii="0.2" drawSphere="1" position="@Volume.rest_position" computeTriangles="0" computeTetrahedra="0" computeEdges="0" name="FixedROI" />
            <DiagonalMass massDensity="5" />
            <FixedProjectiveConstraint indices="@FixedROI.indices" />
            <TetrahedralCorotationalFEMForceField name="FEM" youngModulus="20" poissonRatio="0.4" method="large" />
            <Node name="T">
                <include href="Objects/TriangleSetTopology.xml" src="@../loader" tags=" " />
                <Tetra2TriangleTopologicalMapping input="@../Container" output="@Container" />
                <TriangularFEMForceField name="FEM" youngModulus="50" poissonRatio="0.3" method="large" />
                <TriangularBendingSprings name="FEM-Bend" stiffness="300" damping="1.0" />
                <TrianglePressureForceField normal="0 -0.2 1" dmin="0.9" dmax="1.1" pressure="0.4 0 0" />
                <TriangleCollisionModel />
                <SphereROI centers="0 0 1" radii="0.2" drawSphere="1" position="@../Volume.position" drawTriangles="1" drawTetrahedra="1" triangles="@Container.triangles" tetrahedra="@../Container.tetrahedra" name="SphereROI" />
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
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.05", showBoundingTree="0", gravity="0 -9 0")

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
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showWireframe")
       root.addObject('CollisionPipeline', verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', response="PenalityContactForceField")
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")

       tt = root.addChild('TT')

       tt.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       tt.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       tt.addObject('MeshGmshLoader', name="loader", filename="mesh/cylinder.msh")
       tt.addObject('MechanicalObject', src="@loader", name="Volume")
       tt.addObject('include', href="Objects/TetrahedronSetTopology.xml", src="@loader")
       tt.addObject('SphereROI', centers="0 0 0", radii="0.2", drawSphere="1", position="@Volume.rest_position", computeTriangles="0", computeTetrahedra="0", computeEdges="0", name="FixedROI")
       tt.addObject('DiagonalMass', massDensity="5")
       tt.addObject('FixedProjectiveConstraint', indices="@FixedROI.indices")
       tt.addObject('TetrahedralCorotationalFEMForceField', name="FEM", youngModulus="20", poissonRatio="0.4", method="large")

       t = TT.addChild('T')

       t.addObject('include', href="Objects/TriangleSetTopology.xml", src="@../loader", tags=" ")
       t.addObject('Tetra2TriangleTopologicalMapping', input="@../Container", output="@Container")
       t.addObject('TriangularFEMForceField', name="FEM", youngModulus="50", poissonRatio="0.3", method="large")
       t.addObject('TriangularBendingSprings', name="FEM-Bend", stiffness="300", damping="1.0")
       t.addObject('TrianglePressureForceField', normal="0 -0.2 1", dmin="0.9", dmax="1.1", pressure="0.4 0 0")
       t.addObject('TriangleCollisionModel', )
       t.addObject('SphereROI', centers="0 0 1", radii="0.2", drawSphere="1", position="@../Volume.position", drawTriangles="1", drawTetrahedra="1", triangles="@Container.triangles", tetrahedra="@../Container.tetrahedra", name="SphereROI")

       visu = T.addChild('Visu')

       visu.addObject('OglModel', template="Vec3", name="Visual", material="Default Diffuse 1 0 0 1 0.5 Ambient 1 0.2 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45")
       visu.addObject('IdentityMapping', input="@../../Volume", output="@Visual")
    ```

