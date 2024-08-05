# MeshBarycentricMapperEngine

This class maps a set of points in a topological model and provide barycentric coordinates


__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.Component.Engine.Generate`

__namespace__: `#!c++ sofa::component::engine::generate`

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
		<td>computeLinearInterpolation</td>
		<td>
if true, computes a linear interpolation (debug)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>linearInterpolationIndices</td>
		<td>
Indices of a linear interpolation
</td>
		<td></td>
	</tr>
	<tr>
		<td>linearInterpolationValues</td>
		<td>
Values of a linear interpolation
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>inputPositions</td>
		<td>
Initial positions of the master points
</td>
		<td></td>
	</tr>
	<tr>
		<td>mappedPointPositions</td>
		<td>
Initial positions of the points to be mapped
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>barycentricPositions</td>
		<td>
Output : Barycentric positions of the mapped points
</td>
		<td></td>
	</tr>
	<tr>
		<td>tableElements</td>
		<td>
Output : Table that provides the index of the element to which each input point belongs
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
|topology|Name of the master topology|



## Examples

Component/Engine/Generate/MeshBarycentricMapperEngine.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Engine.Generate"/> <!-- Needed to use components [MeshBarycentricMapperEngine] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RegularGridTopology name="GridTopology" nx="10" ny="10" nz="10" min="-10 -10 -10" max="10 10 10" drawEdges="1"/>
    
        <DefaultAnimationLoop/>
        <Node name="Tetra-Topo">
            <TetrahedronSetTopologyContainer name="Container" checkTopology="1"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <Hexa2TetraTopologicalMapping name="default28" input="@../GridTopology" output="@Container" />
            <Node name="Liver">
                <MeshOBJLoader name="meshLoader" filename="mesh/liver.obj" />
                <MeshTopology src="@meshLoader" name="LiverTopo"  />
                <MeshBarycentricMapperEngine inputPositions="@../../GridTopology.position" mappedPointPositions="@./LiverTopo.position" topology="@../Container"/>
                <OglModel name="Visual" src="@meshLoader" color='1.0 0.0 0.0 1' />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Generate")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('RegularGridTopology', name="GridTopology", nx="10", ny="10", nz="10", min="-10 -10 -10", max="10 10 10", drawEdges="1")
        root.addObject('DefaultAnimationLoop')

        Tetra-Topo = root.addChild('Tetra-Topo')
        Tetra-Topo.addObject('TetrahedronSetTopologyContainer', name="Container", checkTopology="1")
        Tetra-Topo.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        Tetra-Topo.addObject('Hexa2TetraTopologicalMapping', name="default28", input="@../GridTopology", output="@Container")

        Liver = Tetra-Topo.addChild('Liver')
        Liver.addObject('MeshOBJLoader', name="meshLoader", filename="mesh/liver.obj")
        Liver.addObject('MeshTopology', src="@meshLoader", name="LiverTopo")
        Liver.addObject('MeshBarycentricMapperEngine', inputPositions="@../../GridTopology.position", mappedPointPositions="@./LiverTopo.position", topology="@../Container")
        Liver.addObject('OglModel', name="Visual", src="@meshLoader", color="1.0 0.0 0.0 1")
    ```

