<!-- generate_doc -->
# Hexa2PrismTopologicalMapping

Topological mapping where HexahedronSetTopology is converted to PrismSetTopology


__Target__: Sofa.Component.Topology.Mapping

__namespace__: sofa::component::topology::mapping

__parents__:

- TopologicalMapping

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

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseComponent|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseComponent|
|input|Input topology to map|BaseMeshTopology|
|output|Output topology to map|BaseMeshTopology|

## Examples 

Hexa2PrismTopologicalMapping.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 -9 0">
        <Node name="plugins">
            <RequiredPlugin pluginName="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
            <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
            <RequiredPlugin pluginName="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2PrismTopologicalMapping] -->
            <RequiredPlugin pluginName="Sofa.Component.Visual"/> <!-- Needed to use components [VisualMesh] -->
        </Node>
    
        <DefaultAnimationLoop/>
    
        <Node name="grid">
            <RegularGridTopology name="grid" min="-5 -5 0" max="5 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3" name="state" position="@grid.position"/>
    
            <Node name="prisms">
                <MeshTopology name="prism_topology"/>
                <Hexa2PrismTopologicalMapping input="@grid" output="@prism_topology" />
                <VisualMesh position="@../state.position" topology="@prism_topology" enable="true"/>
            </Node>
    
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 -9 0")

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Constant")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Grid")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Mapping")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Visual")

       root.addObject('DefaultAnimationLoop', )

       grid = root.addChild('grid')

       grid.addObject('RegularGridTopology', name="grid", min="-5 -5 0", max="5 5 40", n="5 5 20")
       grid.addObject('MechanicalObject', template="Vec3", name="state", position="@grid.position")

       prisms = grid.addChild('prisms')

       prisms.addObject('MeshTopology', name="prism_topology")
       prisms.addObject('Hexa2PrismTopologicalMapping', input="@grid", output="@prism_topology")
       prisms.addObject('VisualMesh', position="@../state.position", topology="@prism_topology", enable="true")
    ```

