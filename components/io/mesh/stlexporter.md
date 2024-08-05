# STLExporter

Save a topology in file


__Target__: `Sofa.Component.IO.Mesh`

__namespace__: `#!c++ sofa::component::_stlexporter_`

__parents__: 

- `#!c++ BaseSimulationExporter`

__categories__: 

- _Miscellaneous

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
		<td>binaryformat</td>
		<td>
if true, save in binary format, otherwise in ascii
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
points coordinates
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangle</td>
		<td>
triangles indices
</td>
		<td></td>
	</tr>
	<tr>
		<td>quad</td>
		<td>
quads indices
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

Component/IO/Mesh/STLExporter.scn

=== "XML"

    ```xml
    <?xml version='1.0'?>
    <Node 	name='Root' gravity='0 0 0' time='0' animate='0'   >
       <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader,STLExporter] -->
       <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
       <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
       <DefaultAnimationLoop/>
       <MechanicalObject position='0 1 2 3 4 5 6 7 8 9'/>
       <MeshOBJLoader name="loader" filename='mesh/liver-smooth.obj'/>
       <OglModel src="@loader"/>
    
       <STLExporter name='exporter1' printLog='true' filename='outFile' exportAtBegin='true' position="@loader.position" triangle="@loader.triangles"/>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        Root = rootNode.addChild('Root', gravity="0 0 0", time="0", animate="0")
        Root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        Root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        Root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        Root.addObject('DefaultAnimationLoop')
        Root.addObject('MechanicalObject', position="0 1 2 3 4 5 6 7 8 9")
        Root.addObject('MeshOBJLoader', name="loader", filename="mesh/liver-smooth.obj")
        Root.addObject('OglModel', src="@loader")
        Root.addObject('STLExporter', name="exporter1", printLog="true", filename="outFile", exportAtBegin="true", position="@loader.position", triangle="@loader.triangles")
    ```

