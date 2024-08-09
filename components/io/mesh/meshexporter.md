<!-- generate_doc -->
# MeshExporter

Export topology and positions into file.   
Supported format are:   
- vtkxml  
- vtk  
- netgen  
- teten  
- gmsh  
- obj  



__Target__: Sofa.Component.IO.Mesh

__namespace__: sofa::component::_meshexporter_

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
		<td>format</td>
		<td>
File format to use
		</td>
		<td>ALL</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
points position (will use points from topology or mechanical state if this is empty)
		</td>
		<td></td>
	</tr>
	<tr>
		<td>edges</td>
		<td>
write edge topology
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
write triangle topology
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>quads</td>
		<td>
write quad topology
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>tetras</td>
		<td>
write tetra topology
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>hexas</td>
		<td>
write hexa topology
		</td>
		<td>1</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|

