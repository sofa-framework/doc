# Refine2DMesh

Refine 2D mesh using Delaunay triangulation


__Templates__:

- `#!c++ Vec3d`

__Target__: `CGALPlugin`

__namespace__: `#!c++ cgal`

__parents__: 

- `#!c++ DataEngine`

__categories__: 

- Engine

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
		<td>inputPoints</td>
		<td>
Position coordinates (3D, z=0)
</td>
		<td></td>
	</tr>
	<tr>
		<td>inputEdges</td>
		<td>
Constraints (edges)
</td>
		<td></td>
	</tr>
	<tr>
		<td>inputEdgesData1</td>
		<td>
Data values defined on constrained edges
</td>
		<td></td>
	</tr>
	<tr>
		<td>inputEdgesData2</td>
		<td>
Data values defined on constrained edges
</td>
		<td></td>
	</tr>
	<tr>
		<td>seedPoints</td>
		<td>
Seed Points (3D, z=0)
</td>
		<td></td>
	</tr>
	<tr>
		<td>regionPoints</td>
		<td>
Region Points (3D, z=0)
</td>
		<td></td>
	</tr>
	<tr>
		<td>useInteriorPoints</td>
		<td>
should inputs points not on boundaries be input to the meshing algorithm
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>outputPoints</td>
		<td>
New Positions coordinates (3D, z=0)
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputTriangles</td>
		<td>
List of triangles
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputEdges</td>
		<td>
New constraints (edges)
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputEdgesData1</td>
		<td>
Data values defined on new constrained edges
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputEdgesData2</td>
		<td>
Data values defined on new constrained edges
</td>
		<td></td>
	</tr>
	<tr>
		<td>trianglesRegion</td>
		<td>
Region for each Triangle
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputBdPoints</td>
		<td>
Indices of points on the boundary
</td>
		<td></td>
	</tr>
	<tr>
		<td>shapeCriteria</td>
		<td>
Shape Criteria
</td>
		<td>0.125</td>
	</tr>
	<tr>
		<td>sizeCriteria</td>
		<td>
Size Criteria
</td>
		<td>0.5</td>
	</tr>
	<tr>
		<td>viewSeedPoints</td>
		<td>
Display Seed Points
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>viewRegionPoints</td>
		<td>
Display Region Points
</td>
		<td>0</td>
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

CGALPlugin/share/sofa/examples/CGALPlugin/Refine2DMesh.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.01" gravity="0 -1 0">
    	<VisualStyle displayFlags="showVisual showCollisionModels showWireframe"/>
        <RequiredPlugin pluginName="CGALPlugin"/>
        <RequiredPlugin pluginName='SofaOpenglVisual'/>
        
        <MeshVTKLoader name="meshLoader" filename="data/mesh/edges.vtk" />
    
        <Refine2DMesh template="Vec3d" name="cgalTool"
                        inputPoints="@meshLoader.position" inputEdges="@meshLoader.edges"
                        useInteriorPoints="false"
                        seedPoints="200 50 0"
                        regionPoints="50 50 0"
                        shapeCriteria="0.125"
                        sizeCriteria="10"
                        viewSeedPoints="1"
                        viewRegionPoints="1"
                        />
      
    	<Node>
            <MechanicalObject position="@../cgalTool.outputPoints" />
            <TriangleSetTopologyContainer position="@../cgalTool.outputPoints" triangles="@../cgalTool.outputTriangles" />
            <TriangleSetGeometryAlgorithms drawTriangles="true"/>        
    	</Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01", gravity="0 -1 0")
        root.addObject('VisualStyle', displayFlags="showVisual showCollisionModels showWireframe")
        root.addObject('RequiredPlugin', pluginName="CGALPlugin")
        root.addObject('RequiredPlugin', pluginName="SofaOpenglVisual")
        root.addObject('MeshVTKLoader', name="meshLoader", filename="data/mesh/edges.vtk")
        root.addObject('Refine2DMesh', template="Vec3d", name="cgalTool", inputPoints="@meshLoader.position", inputEdges="@meshLoader.edges", useInteriorPoints="false", seedPoints="200 50 0", regionPoints="50 50 0", shapeCriteria="0.125", sizeCriteria="10", viewSeedPoints="1", viewRegionPoints="1")

        root = root.addChild('root')
        root.addObject('MechanicalObject', position="@../cgalTool.outputPoints")
        root.addObject('TriangleSetTopologyContainer', position="@../cgalTool.outputPoints", triangles="@../cgalTool.outputTriangles")
        root.addObject('TriangleSetGeometryAlgorithms', drawTriangles="true")
    ```
