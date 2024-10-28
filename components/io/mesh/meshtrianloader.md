<!-- generate_doc -->
# MeshTrianLoader

Specific mesh loader for trian (only triangulations) file format.


__Target__: Sofa.Component.IO.Mesh

__namespace__: sofa::component::io::mesh

__parents__:

- MeshLoader

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
		<td>filename</td>
		<td>
Filename of the object
		</td>
		<td></td>
	</tr>
	<tr>
		<td>flipNormals</td>
		<td>
Flip Normals
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>triangulate</td>
		<td>
Divide all polygons into triangles
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>createSubelements</td>
		<td>
Divide all n-D elements into their (n-1)-D boundary elements (e.g. tetrahedra to triangles)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>onlyAttachedPoints</td>
		<td>
Only keep points attached to elements of the mesh
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>translation</td>
		<td>
Translation of the DOFs
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>rotation</td>
		<td>
Rotation of the DOFs
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>scale3d</td>
		<td>
Scale of the DOFs in 3 dimensions
		</td>
		<td>1 1 1</td>
	</tr>
	<tr>
		<td>transformation</td>
		<td>
4x4 Homogeneous matrix to transform the DOFs (when present replace any)
		</td>
		<td>[1 0 0 0,0 1 0 0,0 0 1 0,0 0 0 1]</td>
	</tr>
	<tr>
		<td>trian2</td>
		<td>
Set to true if the mesh is a trian2 format.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>neighborTable</td>
		<td>
Table of neighborhood triangle indices for each triangle.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>edgesOnBorder</td>
		<td>
List of edges which are on the border of the mesh loaded.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>trianglesOnBorderList</td>
		<td>
List of triangle indices which are on the border of the mesh loaded.
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Vectors</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Vertices of the mesh loaded
		</td>
		<td></td>
	</tr>
	<tr>
		<td>polylines</td>
		<td>
Polylines of the mesh loaded
		</td>
		<td></td>
	</tr>
	<tr>
		<td>edges</td>
		<td>
Edges of the mesh loaded
		</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
Triangles of the mesh loaded
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quads</td>
		<td>
Quads of the mesh loaded
		</td>
		<td></td>
	</tr>
	<tr>
		<td>polygons</td>
		<td>
Polygons of the mesh loaded
		</td>
		<td></td>
	</tr>
	<tr>
		<td>highOrderEdgePositions</td>
		<td>
High order edge points of the mesh loaded
		</td>
		<td></td>
	</tr>
	<tr>
		<td>highOrderTrianglePositions</td>
		<td>
High order triangle points of the mesh loaded
		</td>
		<td></td>
	</tr>
	<tr>
		<td>highOrderQuadPositions</td>
		<td>
High order quad points of the mesh loaded
		</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedra</td>
		<td>
Tetrahedra of the mesh loaded
		</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedra</td>
		<td>
Hexahedra of the mesh loaded
		</td>
		<td></td>
	</tr>
	<tr>
		<td>pentahedra</td>
		<td>
Pentahedra of the mesh loaded
		</td>
		<td></td>
	</tr>
	<tr>
		<td>highOrderTetrahedronPositions</td>
		<td>
High order tetrahedron points of the mesh loaded
		</td>
		<td></td>
	</tr>
	<tr>
		<td>highOrderHexahedronPositions</td>
		<td>
High order hexahedron points of the mesh loaded
		</td>
		<td></td>
	</tr>
	<tr>
		<td>pyramids</td>
		<td>
Pyramids of the mesh loaded
		</td>
		<td></td>
	</tr>
	<tr>
		<td>normals</td>
		<td>
Normals of the mesh loaded
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Groups</td>
	</tr>
	<tr>
		<td>edgesGroups</td>
		<td>
Groups of Edges
		</td>
		<td></td>
	</tr>
	<tr>
		<td>trianglesGroups</td>
		<td>
Groups of Triangles
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quadsGroups</td>
		<td>
Groups of Quads
		</td>
		<td></td>
	</tr>
	<tr>
		<td>polygonsGroups</td>
		<td>
Groups of Polygons
		</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedraGroups</td>
		<td>
Groups of Tetrahedra
		</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedraGroups</td>
		<td>
Groups of Hexahedra
		</td>
		<td></td>
	</tr>
	<tr>
		<td>pentahedraGroups</td>
		<td>
Groups of Pentahedra
		</td>
		<td></td>
	</tr>
	<tr>
		<td>pyramidsGroups</td>
		<td>
Groups of Pyramids
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

## Examples 

MeshTrianLoader.scn

=== "XML"

    ```xml
    <!-- For more details see: https://wiki.sofa-framework.org/tdev/wiki/Notes/NewLoaderArchitecture -->
    <Node name="Root" gravity="0 -9.81 0" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshTrianLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showVisual showBehaviorModels showForceFields showCollision showMapping" />
        <CollisionPipeline name="DefaultCollisionPipeline" verbose="0" draw="0" depth="6" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="Trian file">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshTrianLoader name="TrianLoader" filename="mesh/coeur1.trian" />
            <!--	  <MeshGmshLoader name="loader" filename="mesh/square3.msh" /> -->
            <MechanicalObject name="dofs" scale="1" src="@TrianLoader" />
            <TriangleSetTopologyContainer name="topo" src="@TrianLoader" />
            <TriangleSetTopologyModifier name="modif" />
            <TriangleSetGeometryAlgorithms name="triGeo" />
            <OglModel name="VisualModel" src="@TrianLoader" color="red" />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('Root', gravity="0 -9.81 0", dt="0.02")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels showForceFields showCollision showMapping")
       root.addObject('CollisionPipeline', name="DefaultCollisionPipeline", verbose="0", draw="0", depth="6")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       trian_file = Root.addChild('Trian file')

       trian_file.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       trian_file.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       trian_file.addObject('MeshTrianLoader', name="TrianLoader", filename="mesh/coeur1.trian")
       trian_file.addObject('MechanicalObject', name="dofs", scale="1", src="@TrianLoader")
       trian_file.addObject('TriangleSetTopologyContainer', name="topo", src="@TrianLoader")
       trian_file.addObject('TriangleSetTopologyModifier', name="modif")
       trian_file.addObject('TriangleSetGeometryAlgorithms', name="triGeo")
       trian_file.addObject('OglModel', name="VisualModel", src="@TrianLoader", color="red")
    ```

