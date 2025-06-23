<!-- generate_doc -->
# BoxROI

Engine selecting the any primitives (vertex/edge/triangle/quad/tetrahedron/hexahedron) inside given boxes.


Templates:

- Rigid3d
- Vec1d
- Vec2d
- Vec3d
- Vec6d

__Target__: Sofa.Component.Engine.Select

__namespace__: sofa::component::engine::select::boxroi

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
		<td>box</td>
		<td>
List of boxes, each defined by two 3D points : xmin,ymin,zmin, xmax,ymax,zmax
		</td>
		<td></td>
	</tr>
	<tr>
		<td>orientedBox</td>
		<td>
List of boxes defined by 3 points (p0, p1, p2) and a depth distance 
A parallelogram will be defined by (p0, p1, p2, p3 = p0 + (p2-p1)). 
The box will finaly correspond to the parallelogram extrusion of depth/2 
along its normal and depth/2 in the opposite direction. 
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

BoxROI_2d.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -9.81 1" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [MeshSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
    
        <DefaultAnimationLoop/>
        <DefaultVisualManagerLoop/>
    
        <Node name="M1">
            <EulerImplicitSolver name="odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver template="CompressedRowSparseMatrix" iterations="1000" threshold="1e-9" tolerance="1e-9"/>
            <MechanicalObject template="Vec2"/>
            <UniformMass vertexMass="1" />
            <RegularGridTopology nx="21" ny="5" nz="1" xmin="0" xmax="20" ymin="0" ymax="4" zmin="0" zmax="0"/>
            <BoxROI name="box" box="-0.1 -0.1 -1e4  0.1 4.1 1e4"/>
            <FixedProjectiveConstraint indices="@box.indices" />
            <MeshSpringForceField stiffness="10000"/>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9.81 1", dt="0.02")

       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('DefaultVisualManagerLoop', )

       m1 = root.addChild('M1')

       m1.addObject('EulerImplicitSolver', name="odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
       m1.addObject('CGLinearSolver', template="CompressedRowSparseMatrix", iterations="1000", threshold="1e-9", tolerance="1e-9")
       m1.addObject('MechanicalObject', template="Vec2")
       m1.addObject('UniformMass', vertexMass="1")
       m1.addObject('RegularGridTopology', nx="21", ny="5", nz="1", xmin="0", xmax="20", ymin="0", ymax="4", zmin="0", zmax="0")
       m1.addObject('BoxROI', name="box", box="-0.1 -0.1 -1e4  0.1 4.1 1e4")
       m1.addObject('FixedProjectiveConstraint', indices="@box.indices")
       m1.addObject('MeshSpringForceField', stiffness="10000")
    ```

BoxROI.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -9 1" dt="0.05">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
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
        <VisualStyle displayFlags="showBehaviorModels showWireframe" />
        <CollisionPipeline name="default0" verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="default1" response="PenalityContactForceField" />
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
        <Node name="SquareGravity" gravity="0 -9.81 0">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshGmshLoader name="loader" filename="mesh/square3.msh" createSubelements="true"/>
            <MechanicalObject src="@loader" template="Vec3" name="mecaObj" scale3d="10 10 10" restScale="1" />
            <TriangleSetTopologyContainer src="@loader" name="Container" />
            <TriangleSetTopologyModifier name="Modifier" />
            <TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <DiagonalMass name="default5" massDensity="0.15" />
            <BoxROI template="Vec3" box="2 9.5 -0.5 8 10.5 0.5" drawBoxes="1" position="@mecaObj.rest_position" name="FixedROI" computeTriangles="0" computeTetrahedra="0" computeEdges="0" />
            <FixedProjectiveConstraint template="Vec3" name="default6" indices="@FixedROI.indices" />
            <TriangularFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.3" youngModulus="60" />
            <TriangularBendingSprings template="Vec3" name="FEM-Bend" stiffness="300" damping="1" />
            <TriangleCollisionModel template="Vec3" name="default7" />
            <BoxROI template="Vec3" box="3 3 0 6 6 1" orientedBox="3 9 0 6 7 0 3 7 0 1   8 3 0 9 5.5 0 8 6 0 1" drawBoxes="1" position="@mecaObj.position" drawTriangles="1" triangles="@Container.triangles" name="boxROI" />
            <Node name="visu">
                <OglModel template="Vec3" name="Visual" material="Default Diffuse 1 1 0 0 0.6 Ambient 1 0.2 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45" />
                <IdentityMapping template="Vec3,Vec3" name="default8" input="@.." output="@Visual" />
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
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showWireframe")
       root.addObject('CollisionPipeline', name="default0", verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', name="default1", response="PenalityContactForceField")
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")

       square_gravity = root.addChild('SquareGravity', gravity="0 -9.81 0")

       square_gravity.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       square_gravity.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       square_gravity.addObject('MeshGmshLoader', name="loader", filename="mesh/square3.msh", createSubelements="true")
       square_gravity.addObject('MechanicalObject', src="@loader", template="Vec3", name="mecaObj", scale3d="10 10 10", restScale="1")
       square_gravity.addObject('TriangleSetTopologyContainer', src="@loader", name="Container")
       square_gravity.addObject('TriangleSetTopologyModifier', name="Modifier")
       square_gravity.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       square_gravity.addObject('DiagonalMass', name="default5", massDensity="0.15")
       square_gravity.addObject('BoxROI', template="Vec3", box="2 9.5 -0.5 8 10.5 0.5", drawBoxes="1", position="@mecaObj.rest_position", name="FixedROI", computeTriangles="0", computeTetrahedra="0", computeEdges="0")
       square_gravity.addObject('FixedProjectiveConstraint', template="Vec3", name="default6", indices="@FixedROI.indices")
       square_gravity.addObject('TriangularFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.3", youngModulus="60")
       square_gravity.addObject('TriangularBendingSprings', template="Vec3", name="FEM-Bend", stiffness="300", damping="1")
       square_gravity.addObject('TriangleCollisionModel', template="Vec3", name="default7")
       square_gravity.addObject('BoxROI', template="Vec3", box="3 3 0 6 6 1", orientedBox="3 9 0 6 7 0 3 7 0 1   8 3 0 9 5.5 0 8 6 0 1", drawBoxes="1", position="@mecaObj.position", drawTriangles="1", triangles="@Container.triangles", name="boxROI")

       visu = SquareGravity.addChild('visu')

       visu.addObject('OglModel', template="Vec3", name="Visual", material="Default Diffuse 1 1 0 0 0.6 Ambient 1 0.2 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45")
       visu.addObject('IdentityMapping', template="Vec3,Vec3", name="default8", input="@..", output="@Visual")
    ```

BoxROI_1d.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="9.81 0 0" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [MeshSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
    
        <DefaultAnimationLoop/>
        <DefaultVisualManagerLoop/>
    
        <Node name="M1">
            <EulerImplicitSolver name="odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver template="CompressedRowSparseMatrix" iterations="1000" threshold="1e-9" tolerance="1e-9"/>
            <MechanicalObject template="Vec1" showObject="true" showObjectScale="10"/>
            <UniformMass vertexMass="1" />
            <RegularGridTopology nx="21" ny="1" nz="1" xmin="0" xmax="20" ymin="0" ymax="0" zmin="0" zmax="0"/>
            <BoxROI name="box" box="-0.1 -1e4 -1e4  0.1 1e4 1e4"/>
            <FixedProjectiveConstraint indices="@box.indices" />
            <MeshSpringForceField stiffness="500"/>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="9.81 0 0", dt="0.02")

       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('DefaultVisualManagerLoop', )

       m1 = root.addChild('M1')

       m1.addObject('EulerImplicitSolver', name="odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
       m1.addObject('CGLinearSolver', template="CompressedRowSparseMatrix", iterations="1000", threshold="1e-9", tolerance="1e-9")
       m1.addObject('MechanicalObject', template="Vec1", showObject="true", showObjectScale="10")
       m1.addObject('UniformMass', vertexMass="1")
       m1.addObject('RegularGridTopology', nx="21", ny="1", nz="1", xmin="0", xmax="20", ymin="0", ymax="0", zmin="0", zmax="0")
       m1.addObject('BoxROI', name="box", box="-0.1 -1e4 -1e4  0.1 1e4 1e4")
       m1.addObject('FixedProjectiveConstraint', indices="@box.indices")
       m1.addObject('MeshSpringForceField', stiffness="500")
    ```

