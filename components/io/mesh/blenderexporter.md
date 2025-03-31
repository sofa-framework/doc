<!-- generate_doc -->
# BlenderExporter

Export the simulation result as blender point cache files.


Templates:

- Rigid3d
- Vec3d

__Target__: Sofa.Component.IO.Mesh

__namespace__: sofa::component::_blenderexporter_

__parents__:

- BaseSimulationExporter

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
Path or filename where to export the data.  If missing the name of the component is used.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>exportEveryNumberOfSteps</td>
		<td>
export file only at specified number of steps (0=disable, default=0)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>exportAtBegin</td>
		<td>
export file before the simulation starts, once the simulation is initialized (default=false)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>exportAtEnd</td>
		<td>
export file when the simulation is over and cleanup is called, i.e. just before deleting the simulation (default=false)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>enable</td>
		<td>
Enable or disable the component. (default=true)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>path</td>
		<td>
output path
		</td>
		<td></td>
	</tr>
	<tr>
		<td>baseName</td>
		<td>
Base name for the output files
		</td>
		<td></td>
	</tr>
	<tr>
		<td>simulationType</td>
		<td>
simulation type (0: soft body, 1: particles, 2:cloth, 3:hair)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>step</td>
		<td>
save the  simulation result every step frames
		</td>
		<td>2</td>
	</tr>
	<tr>
		<td>nbPtsByHair</td>
		<td>
number of element by hair strand
		</td>
		<td>20</td>
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

BlenderExporter.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.01" gravity="0 -9.81 0">
    	<RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader VTKExporter] -->
    	<RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
    	<RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
    	<RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetTopologyContainer] -->
    	<DefaultAnimationLoop/>
    
        <MeshTopology name="mesh" filename="mesh/dragon.obj" />
        <MeshOBJLoader name="loader" filename="mesh/dragon.obj" />
        <MechanicalObject src="@loader" template="Vec3" name="mecha" showObject="1" />
        <TetrahedronSetTopologyContainer src="@loader" name="topo" />
        <BlenderExporter name="ExportToBlender"
            filename="example"
            listening="true" 
            exportAtBegin="1" 
            exportAtEnd="1" 
            exportEveryNumberOfSteps="3"
            printLog="1"
        />
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 -9.81 0")

       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('MeshTopology', name="mesh", filename="mesh/dragon.obj")
       root.addObject('MeshOBJLoader', name="loader", filename="mesh/dragon.obj")
       root.addObject('MechanicalObject', src="@loader", template="Vec3", name="mecha", showObject="1")
       root.addObject('TetrahedronSetTopologyContainer', src="@loader", name="topo")
       root.addObject('BlenderExporter', name="ExportToBlender", filename="example", listening="true", exportAtBegin="1", exportAtEnd="1", exportEveryNumberOfSteps="3", printLog="1")
    ```

