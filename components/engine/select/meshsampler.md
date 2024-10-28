<!-- generate_doc -->
# MeshSampler

Select uniformly distributed points on a mesh based on Euclidean or Geodesic distance measure.


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.Engine.Select

__namespace__: sofa::component::engine::select

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
		<td>number</td>
		<td>
Sample number
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Input positions.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>edges</td>
		<td>
Input edges for geodesic sampling (Euclidean distances are used if not specified).
		</td>
		<td></td>
	</tr>
	<tr>
		<td>maxIter</td>
		<td>
Max number of Lloyd iterations.
		</td>
		<td>100</td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>outputIndices</td>
		<td>
Computed sample indices.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>outputPosition</td>
		<td>
Computed sample coordinates.
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

MeshSampler.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node 	name="root" gravity="0 -1 0" dt="0.05"  >
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [MeshSampler] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <VisualStyle displayFlags="showWireframe" />
        <DefaultAnimationLoop/>
    
        <Node name="using Geodesic Distances (red)" >
            <MeshOBJLoader name="meshLoader_1" filename="mesh/dragon.obj" handleSeams="1" />
            <OglModel name="Visual" src="@meshLoader_1" color="red" dz="0" />
            <MeshTopology name="topo" src="@Visual" />
            <MeshSampler name="sampler1" position="@topo.position" edges="@topo.edges"  number="10" maxIter="100" printLog="1"/>
            <MechanicalObject template="Vec3" position="@sampler1.outputPosition" showObject="1" showObjectScale="10" />
        </Node>
    
        <Node name="using Euclidean Distances (blue)" >
            <MeshOBJLoader name="meshLoader_0" filename="mesh/dragon.obj" handleSeams="1" />
            <OglModel name="Visual" src="@meshLoader_0" color="blue" dy="20" />
    
            <MeshSampler name="sampler2" position="@Visual.position"  number="10" maxIter="100" printLog="1"/>
            <MechanicalObject template="Vec3" position="@sampler2.outputPosition" showObject="1" showObjectScale="10" />
        </Node>
    
    </Node>
    

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -1 0", dt="0.05")

       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="showWireframe")
       root.addObject('DefaultAnimationLoop', )

       using__geodesic__distances_(red) = root.addChild('using Geodesic Distances (red)')

       using__geodesic__distances_(red).addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/dragon.obj", handleSeams="1")
       using__geodesic__distances_(red).addObject('OglModel', name="Visual", src="@meshLoader_1", color="red", dz="0")
       using__geodesic__distances_(red).addObject('MeshTopology', name="topo", src="@Visual")
       using__geodesic__distances_(red).addObject('MeshSampler', name="sampler1", position="@topo.position", edges="@topo.edges", number="10", maxIter="100", printLog="1")
       using__geodesic__distances_(red).addObject('MechanicalObject', template="Vec3", position="@sampler1.outputPosition", showObject="1", showObjectScale="10")

       using__euclidean__distances_(blue) = root.addChild('using Euclidean Distances (blue)')

       using__euclidean__distances_(blue).addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/dragon.obj", handleSeams="1")
       using__euclidean__distances_(blue).addObject('OglModel', name="Visual", src="@meshLoader_0", color="blue", dy="20")
       using__euclidean__distances_(blue).addObject('MeshSampler', name="sampler2", position="@Visual.position", number="10", maxIter="100", printLog="1")
       using__euclidean__distances_(blue).addObject('MechanicalObject', template="Vec3", position="@sampler2.outputPosition", showObject="1", showObjectScale="10")
    ```

