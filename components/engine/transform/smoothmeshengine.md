<!-- generate_doc -->
# SmoothMeshEngine

Compute the laplacian smoothing of a mesh.


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.Engine.Transform

__namespace__: sofa::component::engine::transform

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
		<td>input_indices</td>
		<td>
Position indices that need to be smoothed, leave empty for all positions
		</td>
		<td></td>
	</tr>
	<tr>
		<td>nb_iterations</td>
		<td>
Number of iterations of laplacian smoothing
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>input_position</td>
		<td>
Input position
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>output_position</td>
		<td>
Output position
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showInput</td>
		<td>
showInput
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showOutput</td>
		<td>
showOutput
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
|topology|link to the topology container|BaseMeshTopology|

## Examples 

SmoothMeshEngine.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" >
        <RequiredPlugin name="Sofa.Component.Engine.Transform"/> <!-- Needed to use components [SmoothMeshEngine] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <Node name="origin" >
            <VisualStyle displayFlags="showWireframe" />
            <MeshOBJLoader name="loader" filename="mesh/dragon.obj" />
            <OglModel name="visual" src="@loader" color="yellow" />
        </Node>
        <Node name="smoothed" >
            <VisualStyle displayFlags="hideWireframe" />
            <MeshTopology name="topology" src="@/origin/loader"/>
            <SmoothMeshEngine template="Vec3" name="smoother" input_position="@/origin/loader.position" nb_iterations="1" showOutput="true"/>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root')

       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Transform")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('DefaultAnimationLoop', )

       origin = root.addChild('origin')

       origin.addObject('VisualStyle', displayFlags="showWireframe")
       origin.addObject('MeshOBJLoader', name="loader", filename="mesh/dragon.obj")
       origin.addObject('OglModel', name="visual", src="@loader", color="yellow")

       smoothed = root.addChild('smoothed')

       smoothed.addObject('VisualStyle', displayFlags="hideWireframe")
       smoothed.addObject('MeshTopology', name="topology", src="@/origin/loader")
       smoothed.addObject('SmoothMeshEngine', template="Vec3", name="smoother", input_position="@/origin/loader.position", nb_iterations="1", showOutput="true")
    ```

