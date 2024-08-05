# FrontSurfaceReconstruction

Generate triangular surface mesh from point cloud


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
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Input point cloud positions
</td>
		<td></td>
	</tr>
	<tr>
		<td>radiusRatioBound</td>
		<td>
Candidates incident to surface triangles which are not in the beta-wedge are discarded, if the ratio of their radius and the radius of the surface triangle is larger than radius_ratio_bound
</td>
		<td>5</td>
	</tr>
	<tr>
		<td>beta</td>
		<td>
Half the angle of the wedge in which only the radius of triangles counts for the plausibility of candidates.
</td>
		<td>0.52</td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>outputPosition</td>
		<td>
Output position of the surface mesh
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

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|



## Examples

CGALPlugin/share/sofa/examples/CGALPlugin/FrontSurfaceReconstruction.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="0 0 0" dt="1"  >
    	<RequiredPlugin pluginName="CGALPlugin"/>
      <RequiredPlugin pluginName='SofaOpenglVisual'/>
    
    	<VisualStyle displayFlags="showVisual" />
    
    	<Node name="PointCloud">
    		<MeshOBJLoader name="loader" filename="mesh/liver2.obj"/>
    		<MeshTopology src="@loader"/>
    		<MechanicalObject showObject="1" showObjectScale="5"/>
    	</Node>
    
    	<Node name="FrontSurfaceReconstruction">
    		<FrontSurfaceReconstruction name="engine" src="@../PointCloud/loader" radiusRatioBound="5" beta="0.52"/>
    		<MeshTopology position="@engine.outputPosition" triangles="@engine.outputTriangles"/>
    		<OglModel color="1 0 0"/>
    	</Node>
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 0 0", dt="1")
        root.addObject('RequiredPlugin', pluginName="CGALPlugin")
        root.addObject('RequiredPlugin', pluginName="SofaOpenglVisual")
        root.addObject('VisualStyle', displayFlags="showVisual")

        PointCloud = root.addChild('PointCloud')
        PointCloud.addObject('MeshOBJLoader', name="loader", filename="mesh/liver2.obj")
        PointCloud.addObject('MeshTopology', src="@loader")
        PointCloud.addObject('MechanicalObject', showObject="1", showObjectScale="5")

        FrontSurfaceReconstruction = root.addChild('FrontSurfaceReconstruction')
        FrontSurfaceReconstruction.addObject('FrontSurfaceReconstruction', name="engine", src="@../PointCloud/loader", radiusRatioBound="5", beta="0.52")
        FrontSurfaceReconstruction.addObject('MeshTopology', position="@engine.outputPosition", triangles="@engine.outputTriangles")
        FrontSurfaceReconstruction.addObject('OglModel', color="1 0 0")
    ```

