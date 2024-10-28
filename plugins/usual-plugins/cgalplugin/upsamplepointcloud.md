<!-- generate_doc -->
# UpsamplePointCloud

Generates a denser point cloud from an input point cloud


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
		<td>normals</td>
		<td>
Input point cloud normals
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>outputPosition</td>
		<td>
Output denser point cloud positions
		</td>
		<td></td>
	</tr>
	<tr>
		<td>outputNormals</td>
		<td>
Output normals of denser point cloud
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

UpsamplePointCloud.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="0 0 0" dt="1"  >
    	<RequiredPlugin pluginName="CGALPlugin"/>
      <RequiredPlugin pluginName='SofaOpenglVisual'/>
    
    	<VisualStyle displayFlags="showVisual" />
    
    	<Node name="PointCloud">
    		<MeshOBJLoader name="loader" filename="mesh/liver.obj"/>
    		<MeshTopology src="@loader"/>
    		<MechanicalObject showObject="1" showObjectScale="5" showColor="1 0 0"/>
    	</Node>
    
    	<Node name="UpsamplePointCloud">
    		<UpsamplePointCloud name="engine" src="@../PointCloud/loader"/>
    		<MeshTopology name="topology" position="@engine.outputPosition"/>
    		<MechanicalObject src="@topology" showObject="1" showObjectScale="5"/>
    	</Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 0 0", dt="1")

       root.addObject('RequiredPlugin', pluginName="CGALPlugin")
       root.addObject('RequiredPlugin', pluginName="SofaOpenglVisual")
       root.addObject('VisualStyle', displayFlags="showVisual")

       point_cloud = root.addChild('PointCloud')

       point_cloud.addObject('MeshOBJLoader', name="loader", filename="mesh/liver.obj")
       point_cloud.addObject('MeshTopology', src="@loader")
       point_cloud.addObject('MechanicalObject', showObject="1", showObjectScale="5", showColor="1 0 0")

       upsample_point_cloud = root.addChild('UpsamplePointCloud')

       upsample_point_cloud.addObject('UpsamplePointCloud', name="engine", src="@../PointCloud/loader")
       upsample_point_cloud.addObject('MeshTopology', name="topology", position="@engine.outputPosition")
       upsample_point_cloud.addObject('MechanicalObject', src="@topology", showObject="1", showObjectScale="5")
    ```

