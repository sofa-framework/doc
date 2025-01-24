<!-- generate_doc -->
# MeshROI

Find the primitives (vertex/edge/triangle/tetrahedron) inside a given mesh.


Templates:

- Rigid3d
- Vec3d
- Vec6d

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
		<td>computeMeshROI</td>
		<td>
Compute with the mesh (not only bounding box)
		</td>
		<td>1</td>
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
		<td>ROIposition</td>
		<td>
ROI position coordinates of the degrees of freedom
		</td>
		<td></td>
	</tr>
	<tr>
		<td>ROIedges</td>
		<td>
ROI Edge Topology
		</td>
		<td></td>
	</tr>
	<tr>
		<td>ROItriangles</td>
		<td>
ROI Triangle Topology
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
		<td>box</td>
		<td>
Bounding box defined by xmin,ymin,zmin, xmax,ymax,zmax
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
	<tr>
		<td>drawOut</td>
		<td>
Draw the data not contained in the ROI
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawBox</td>
		<td>
Draw the Bounding box around the mesh used for the ROI
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

## Examples 

MeshROI.scn

=== "XML"

    ```xml
    <Node name="root" gravity="0 -9 1" dt="0.05">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [MeshROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader MeshVTKLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedralCorotationalFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showWireframe" />
        <CollisionPipeline />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <MinProximityIntersection  alarmDistance="0.8" contactDistance="0.5" />
        <Node >
            <EulerImplicitSolver   rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" tolerance="1e-05" threshold="1e-05" />
            <MeshVTKLoader name="loader" filename="mesh/Ossicles.vtu" />
            <MechanicalObject src="@loader"  name="mecaObj" scale3d="1 1 1" restScale="1" />
    
    
            <TetrahedronSetTopologyContainer name="Container"  src="@loader"/>
            <TriangleSetTopologyModifier name="ModifierTri" />
            <TetrahedronSetTopologyModifier name="ModifierTetra"/>
            <TetrahedronSetGeometryAlgorithms  name="GeomAlgo"/>
            <DiagonalMass  massDensity="0.15" />
        
            <TetrahedralCorotationalFEMForceField name="FEM" youngModulus="1e10" poissonRatio="0.3" method="large" />
    
            <Node name="MeshROI"  >
                <MeshOBJLoader name="ROIloader" filename="mesh/malleus.obj" scale3d="1 1 1" translation="0 0 0" rotation="0 0 0"/>
                <OglModel />
                <MeshROI name="ROIm"  drawBox="0" drawEdges="0" drawTriangles="1" drawTetrahedra="1" drawOut="0" computeMeshROI="1"  doUpdate="0"
                   position="@../mecaObj.position" tetrahedra="@../loader.tetrahedra" ROIposition="@ROIloader.position" ROItriangles="@ROIloader.triangles" />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9 1", dt="0.05")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showWireframe")
       root.addObject('CollisionPipeline', )
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', response="PenalityContactForceField")
       root.addObject('MinProximityIntersection', alarmDistance="0.8", contactDistance="0.5")

       node = root.addChild('node')

       node.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
       node.addObject('CGLinearSolver', iterations="25", tolerance="1e-05", threshold="1e-05")
       node.addObject('MeshVTKLoader', name="loader", filename="mesh/Ossicles.vtu")
       node.addObject('MechanicalObject', src="@loader", name="mecaObj", scale3d="1 1 1", restScale="1")
       node.addObject('TetrahedronSetTopologyContainer', name="Container", src="@loader")
       node.addObject('TriangleSetTopologyModifier', name="ModifierTri")
       node.addObject('TetrahedronSetTopologyModifier', name="ModifierTetra")
       node.addObject('TetrahedronSetGeometryAlgorithms', name="GeomAlgo")
       node.addObject('DiagonalMass', massDensity="0.15")
       node.addObject('TetrahedralCorotationalFEMForceField', name="FEM", youngModulus="1e10", poissonRatio="0.3", method="large")

       mesh_roi = node.addChild('MeshROI')

       mesh_roi.addObject('MeshOBJLoader', name="ROIloader", filename="mesh/malleus.obj", scale3d="1 1 1", translation="0 0 0", rotation="0 0 0")
       mesh_roi.addObject('OglModel', )
       mesh_roi.addObject('MeshROI', name="ROIm", drawBox="0", drawEdges="0", drawTriangles="1", drawTetrahedra="1", drawOut="0", computeMeshROI="1", doUpdate="0", position="@../mecaObj.position", tetrahedra="@../loader.tetrahedra", ROIposition="@ROIloader.position", ROItriangles="@ROIloader.triangles")
    ```

