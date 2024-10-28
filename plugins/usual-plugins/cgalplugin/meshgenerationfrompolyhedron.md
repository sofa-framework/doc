<!-- generate_doc -->
# MeshGenerationFromPolyhedron

Generate tetrahedral mesh from triangular mesh


## Vec3d

Templates:

- Vec3d

__Target__: CGALPlugin

__namespace__: cgal

__parents__:

- DataEngine

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
		<td>inputPoints</td>
		<td>
Rest position coordinates of the degrees of freedom
		</td>
		<td></td>
	</tr>
	<tr>
		<td>inputTriangles</td>
		<td>
List of triangles
		</td>
		<td></td>
	</tr>
	<tr>
		<td>inputQuads</td>
		<td>
List of quads (if no triangles) 
		</td>
		<td></td>
	</tr>
	<tr>
		<td>outputPoints</td>
		<td>
New Rest position coordinates from the tetrahedral generation
		</td>
		<td></td>
	</tr>
	<tr>
		<td>outputTetras</td>
		<td>
List of tetrahedra
		</td>
		<td></td>
	</tr>
	<tr>
		<td>frozen</td>
		<td>
true to prohibit recomputations of the mesh
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>facetAngle</td>
		<td>
Lower bound for the angle in degrees of the surface mesh facets
		</td>
		<td>25</td>
	</tr>
	<tr>
		<td>facetSize</td>
		<td>
Uniform upper bound for the radius of the surface Delaunay balls
		</td>
		<td>0.15</td>
	</tr>
	<tr>
		<td>facetApproximation</td>
		<td>
Upper bound for the center-center distances of the surface mesh facets
		</td>
		<td>0.008</td>
	</tr>
	<tr>
		<td>cellRatio</td>
		<td>
Upper bound for the radius-edge ratio of the tetrahedra
		</td>
		<td>4</td>
	</tr>
	<tr>
		<td>cellSize</td>
		<td>
Uniform upper bound for the circumradii of the tetrahedra in the mesh
		</td>
		<td>0.2</td>
	</tr>
	<tr>
		<td>sharpEdgeAngle</td>
		<td>
Threshold angle to detect sharp edges in input surface (activated with CGAL 3.8+ if sharpEdgeSize > 0)
		</td>
		<td>120</td>
	</tr>
	<tr>
		<td>sharpEdgeSize</td>
		<td>
Meshing size for sharp feature edges (activated with CGAL 3.8+ if sharpEdgeSize > 0)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>odt</td>
		<td>
activate odt optimization
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>lloyd</td>
		<td>
activate lloyd optimization
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>perturb</td>
		<td>
activate perturb optimization
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>exude</td>
		<td>
activate exude optimization
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>odt_max_it</td>
		<td>
odt max iteration number
		</td>
		<td>200</td>
	</tr>
	<tr>
		<td>lloyd_max_it</td>
		<td>
lloyd max iteration number
		</td>
		<td>200</td>
	</tr>
	<tr>
		<td>perturb_max_time</td>
		<td>
perturb maxtime
		</td>
		<td>20</td>
	</tr>
	<tr>
		<td>exude_max_time</td>
		<td>
exude max time
		</td>
		<td>20</td>
	</tr>
	<tr>
		<td>ordering</td>
		<td>
output points and elements ordering (0 = none, 1 = longest bbox axis)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>constantMeshProcess</td>
		<td>
deterministic choice of first point used in meshing process (true = constant output / false = variable output)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>meshingSeed</td>
		<td>
seed used when picking first point in meshing process
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawTetras</td>
		<td>
display generated tetra mesh
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawSurface</td>
		<td>
display input surface mesh
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

MeshGenerationFromPolyhedron.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.05" showBoundingTree="0" gravity="0 -9 1">
        <VisualStyle displayFlags="showVisual" />
        <RequiredPlugin pluginName="CGALPlugin"/>
    
        <MeshOBJLoader name="loader" filename="mesh/torus.obj" />	
    
        <Node name="visu_surface">
            <MechanicalObject name="dofs" position="@../loader.position"/>
            <TriangleSetTopologyContainer name="topo" triangles="@../loader.triangles"/>
            <TriangleSetTopologyModifier   name="Modifier" />
            <TriangleSetGeometryAlgorithms template="Vec3d" name="GeomAlgo" drawTriangles="1" />
        </Node>
    
        <Node name="tetra_mesh">
            <MeshGenerationFromPolyhedron name="MeshGenerator" inputPoints="@../loader.position" inputTriangles="@../loader.triangles" inputQuads="@../loader.quads"/>
            <MechanicalObject name="dofs" position="@MeshGenerator.outputPoints"/>
            <TetrahedronSetTopologyContainer name="topo" tetrahedra="@MeshGenerator.outputTetras"/>
            <TetrahedronSetGeometryAlgorithms template="Vec3d" name="GeomAlgo" drawTetrahedra="1" drawScaleTetrahedra="0.8"/>
        </Node>
        
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.05", showBoundingTree="0", gravity="0 -9 1")

       root.addObject('VisualStyle', displayFlags="showVisual")
       root.addObject('RequiredPlugin', pluginName="CGALPlugin")
       root.addObject('MeshOBJLoader', name="loader", filename="mesh/torus.obj")

       visu_surface = root.addChild('visu_surface')

       visu_surface.addObject('MechanicalObject', name="dofs", position="@../loader.position")
       visu_surface.addObject('TriangleSetTopologyContainer', name="topo", triangles="@../loader.triangles")
       visu_surface.addObject('TriangleSetTopologyModifier', name="Modifier")
       visu_surface.addObject('TriangleSetGeometryAlgorithms', template="Vec3d", name="GeomAlgo", drawTriangles="1")

       tetra_mesh = root.addChild('tetra_mesh')

       tetra_mesh.addObject('MeshGenerationFromPolyhedron', name="MeshGenerator", inputPoints="@../loader.position", inputTriangles="@../loader.triangles", inputQuads="@../loader.quads")
       tetra_mesh.addObject('MechanicalObject', name="dofs", position="@MeshGenerator.outputPoints")
       tetra_mesh.addObject('TetrahedronSetTopologyContainer', name="topo", tetrahedra="@MeshGenerator.outputTetras")
       tetra_mesh.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3d", name="GeomAlgo", drawTetrahedra="1", drawScaleTetrahedra="0.8")
    ```

