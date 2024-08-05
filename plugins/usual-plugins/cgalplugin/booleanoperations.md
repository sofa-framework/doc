# BooleanOperations

Functions to corefine triangulated surface meshes and compute triangulated surface meshes of the union, difference and intersection of the bounded volumes.


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
		<td>operation</td>
		<td>
Boolean operation
</td>
		<td>union</td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>position1</td>
		<td>
Input positions of the first mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>position2</td>
		<td>
Input positions of the second mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles1</td>
		<td>
Input triangles of the first mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles2</td>
		<td>
Input triangles of the second mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>computeDistrubution</td>
		<td>
If true, computes outputIndices1 and outputIndices2
</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>outputPosition</td>
		<td>
Output positions of the surface mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputTriangles</td>
		<td>
Output triangles of the surface mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputPosition1</td>
		<td>
Output positions of transformation on the first surface mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputTriangles1</td>
		<td>
Output triangles of transformation on the first surface mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputPosition2</td>
		<td>
Output positions of transformation on the second surface mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputTriangles2</td>
		<td>
Output triangles of transformation on the second surface mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputIndices1</td>
		<td>
Indices of the surface mesh points that are on the first object
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputIndices2</td>
		<td>
Indices of the surface mesh points that are on the second object
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



## Examples

CGALPlugin/share/sofa/examples/CGALPlugin/BooleanOperations.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="0 0 0" dt="1"  >
    	<RequiredPlugin pluginName="CGALPlugin"/>
      <RequiredPlugin pluginName='SofaOpenglVisual'/>
    
    	<VisualStyle displayFlags="showWireframe showVisual" />
    
    	<Node name="Mesh1">
    		<MeshOBJLoader name="loader" filename="mesh/cube.obj" translation="50 50 50" scale="50"/>
    		<OglModel src="@loader" color="1 0 0"/>
    	</Node>
    
    	<Node name="Mesh2">
    		<MeshOBJLoader name="loader" filename="mesh/sphere_05.obj"/>
    		<OglModel src="@loader" color="0 1 0"/>
    	</Node>
    
    	<Node name="Union">
    		<BooleanOperations name="engine" position1="@../Mesh1/loader.position" triangles1="@../Mesh1/loader.triangles"
    																		 position2="@../Mesh2/loader.position" triangles2="@../Mesh2/loader.triangles"
    																		 operation="union"/>
    		<MeshTopology position="@engine.outputPosition" triangles="@engine.outputTriangles"/>
    		<OglModel color="0 0 1" translation="200 0 0"/>
    	</Node>
    
    	<Node name="Intersection">
    		<BooleanOperations name="engine" position1="@../Mesh1/loader.position" triangles1="@../Mesh1/loader.triangles"
    																		 position2="@../Mesh2/loader.position" triangles2="@../Mesh2/loader.triangles"
    																		 operation="intersection"/>
    		<MeshTopology position="@engine.outputPosition" triangles="@engine.outputTriangles"/>
    		<OglModel color="0 0 1" translation="375 0 0"/>
    	</Node>
    
    	<Node name="Difference1">
    		<BooleanOperations name="engine" position1="@../Mesh1/loader.position" triangles1="@../Mesh1/loader.triangles"
    																		 position2="@../Mesh2/loader.position" triangles2="@../Mesh2/loader.triangles"
    																		 operation="difference"/>
    		<MeshTopology position="@engine.outputPosition" triangles="@engine.outputTriangles"/>
    		<OglModel color="0 0 1" translation="500 0 0"/>
    	</Node>
    
    	<Node name="Difference2">
    		<BooleanOperations name="engine" position1="@../Mesh2/loader.position" triangles1="@../Mesh2/loader.triangles"
    																		 position2="@../Mesh1/loader.position" triangles2="@../Mesh1/loader.triangles"
    																		 operation="difference"/>
    		<MeshTopology position="@engine.outputPosition" triangles="@engine.outputTriangles"/>
    		<OglModel color="0 0 1" translation="700 0 0"/>
    	</Node>
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 0 0", dt="1")
        root.addObject('RequiredPlugin', pluginName="CGALPlugin")
        root.addObject('RequiredPlugin', pluginName="SofaOpenglVisual")
        root.addObject('VisualStyle', displayFlags="showWireframe showVisual")

        Mesh1 = root.addChild('Mesh1')
        Mesh1.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj", translation="50 50 50", scale="50")
        Mesh1.addObject('OglModel', src="@loader", color="1 0 0")

        Mesh2 = root.addChild('Mesh2')
        Mesh2.addObject('MeshOBJLoader', name="loader", filename="mesh/sphere_05.obj")
        Mesh2.addObject('OglModel', src="@loader", color="0 1 0")

        Union = root.addChild('Union')
        Union.addObject('BooleanOperations', name="engine", position1="@../Mesh1/loader.position", triangles1="@../Mesh1/loader.triangles", position2="@../Mesh2/loader.position", triangles2="@../Mesh2/loader.triangles", operation="union")
        Union.addObject('MeshTopology', position="@engine.outputPosition", triangles="@engine.outputTriangles")
        Union.addObject('OglModel', color="0 0 1", translation="200 0 0")

        Intersection = root.addChild('Intersection')
        Intersection.addObject('BooleanOperations', name="engine", position1="@../Mesh1/loader.position", triangles1="@../Mesh1/loader.triangles", position2="@../Mesh2/loader.position", triangles2="@../Mesh2/loader.triangles", operation="intersection")
        Intersection.addObject('MeshTopology', position="@engine.outputPosition", triangles="@engine.outputTriangles")
        Intersection.addObject('OglModel', color="0 0 1", translation="375 0 0")

        Difference1 = root.addChild('Difference1')
        Difference1.addObject('BooleanOperations', name="engine", position1="@../Mesh1/loader.position", triangles1="@../Mesh1/loader.triangles", position2="@../Mesh2/loader.position", triangles2="@../Mesh2/loader.triangles", operation="difference")
        Difference1.addObject('MeshTopology', position="@engine.outputPosition", triangles="@engine.outputTriangles")
        Difference1.addObject('OglModel', color="0 0 1", translation="500 0 0")

        Difference2 = root.addChild('Difference2')
        Difference2.addObject('BooleanOperations', name="engine", position1="@../Mesh2/loader.position", triangles1="@../Mesh2/loader.triangles", position2="@../Mesh1/loader.position", triangles2="@../Mesh1/loader.triangles", operation="difference")
        Difference2.addObject('MeshTopology', position="@engine.outputPosition", triangles="@engine.outputTriangles")
        Difference2.addObject('OglModel', color="0 0 1", translation="700 0 0")
    ```

