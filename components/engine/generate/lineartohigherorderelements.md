<!-- generate_doc -->
# LinearToHigherOrderElements

Merge several meshes.


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.Engine.Generate

__namespace__: sofa::component::engine::generate

__parents__:

- DataEngine
- TopologyAccessor
- SingleStateAccessor

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
		<td>computeFromEdges</td>
		<td>
Use edges from the input to generate higher-order edges
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>computeFromTriangles</td>
		<td>
Use triangles from the input to generate higher-order triangles
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>computeFromQuads</td>
		<td>
Use quads from the input to generate higher-order quads
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>computeFromTetrahedra</td>
		<td>
Use tetrahedra from the input to generate higher-order tetrahedra
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>computeFromHexahedra</td>
		<td>
Use hexahedra from the input to generate higher-order hexahedra
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Output position
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quadratic_edges</td>
		<td>
List of quadratic edges
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quadratic_triangles</td>
		<td>
List of quadratic triangles
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quadratic_quads</td>
		<td>
List of quadratic quads
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quadratic_tetrahedra</td>
		<td>
List of quadratic tetrahedra
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quadratic_hexahedra</td>
		<td>
List of quadratic hexahedra
		</td>
		<td></td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseComponent|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseComponent|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|topology|Link to a topology|BaseMeshTopology|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|

## Examples 

LinearToHigherOrderElements.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="0 0 0" dt="1"  >
    
        <Node name="plugins">
            <RequiredPlugin pluginName="Sofa.Component.Engine.Generate"/> <!-- Needed to use components [LinearToHigherOrderElements] -->
            <RequiredPlugin pluginName="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshVTKLoader] -->
            <RequiredPlugin pluginName="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
            <RequiredPlugin pluginName="Sofa.Component.Visual"/> <!-- Needed to use components [VisualMesh,VisualPointCloud] -->
            <RequiredPlugin pluginName="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        </Node>
    
        <LineAxis/>
    
        <DefaultAnimationLoop/>
    
    <!--    <Node name="Volume" >-->
    <!--        <Node name="preprocessing">-->
    <!--            <MeshVTKLoader name="mesh" filename="mesh/Bunny.vtk"/>-->
    <!--            <MeshTopology src="@mesh" name="topology"/>-->
    <!--            <MechanicalObject name="state" template="Vec3"/>-->
    <!--            <LinearToHigherOrderElements name="engine"/>-->
    <!--        </Node>-->
    
    <!--        <Node name="quadratic_elements">-->
    <!--            <MeshTopology name="topology" position="@../preprocessing/engine.position" quadratic_tetrahedra="@../preprocessing/engine.quadratic_tetrahedra"/>-->
    <!--            <MechanicalObject name="state" template="Vec3" position="@../preprocessing/engine.position"/>-->
    
    <!--            <VisualPointCloud position="@state.position" drawMode="Sphere" sphereRadius="0.03" color="orange"/>-->
    <!--            <VisualMesh position="@state.position" topology="@topology"/>-->
    <!--        </Node>-->
    <!--    </Node>-->
    
    <!--    <Node name="single_tetra" >-->
    <!--        <Node name="preprocessing">-->
    <!--            <MeshTopology name="topology" tetrahedra="0 1 2 3"/>-->
    <!--            <MechanicalObject name="state" template="Vec3" position="0 0 0  1 0 0  0 1 0  0 0 1"/>-->
    <!--            <LinearToHigherOrderElements name="engine"/>-->
    <!--        </Node>-->
    
    <!--        <Node name="quadratic_elements">-->
    <!--            <MeshTopology name="topology" position="@../preprocessing/engine.position" quadratic_tetrahedra="@../preprocessing/engine.quadratic_tetrahedra"/>-->
    <!--            <MechanicalObject name="state" template="Vec3" position="@../preprocessing/engine.position"/>-->
    
    <!--            <VisualPointCloud position="@state.position" drawMode="Sphere" sphereRadius="0.1" color="lime" showIndices="true" indicesScale="2" indicesColor="black"/>-->
    <!--            <VisualMesh position="@state.position" topology="@topology"/>-->
    <!--        </Node>-->
    <!--    </Node>-->
    
        <Node name="single_hexa" >
    
            <VisualPointCloud position="2 0 0" drawMode="Sphere" sphereRadius="0.2" color="red"/>
            <VisualPointCloud position="0 2 0" drawMode="Sphere" sphereRadius="0.2" color="green"/>
            <VisualPointCloud position="0 0 2" drawMode="Sphere" sphereRadius="0.2" color="blue"/>
    
            <Node name="preprocessing">
                <MeshTopology name="topology" hexahedra="0 1 2 3 4 5 6 7"/>
                <MechanicalObject name="state" template="Vec3" position="-1 -1 -1  1 -1 -1  1 1 -1  -1 1 -1  -1 -1 1  1 -1 1  1 1 1  -1 1 1"/>
                <LinearToHigherOrderElements name="engine"/>
            </Node>
    
            <Node name="quadratic_elements">
                <MeshTopology name="topology" position="@../preprocessing/engine.position" quadratic_hexahedra="@../preprocessing/engine.quadratic_hexahedra"/>
                <MechanicalObject name="state" template="Vec3" position="@../preprocessing/engine.position"/>
    
                <VisualPointCloud position="@state.position" drawMode="Sphere" sphereRadius="0.1" color="lime" showIndices="true" indicesScale="2" indicesColor="black"/>
                <VisualMesh position="@state.position" topology="@topology"/>
            </Node>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 0 0", dt="1")

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Engine.Generate")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.IO.Mesh")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Constant")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Visual")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.GL.Component.Rendering3D")

       root.addObject('LineAxis', )
       root.addObject('DefaultAnimationLoop', )

       single_hexa = root.addChild('single_hexa')

       single_hexa.addObject('VisualPointCloud', position="2 0 0", drawMode="Sphere", sphereRadius="0.2", color="red")
       single_hexa.addObject('VisualPointCloud', position="0 2 0", drawMode="Sphere", sphereRadius="0.2", color="green")
       single_hexa.addObject('VisualPointCloud', position="0 0 2", drawMode="Sphere", sphereRadius="0.2", color="blue")

       preprocessing = single_hexa.addChild('preprocessing')

       preprocessing.addObject('MeshTopology', name="topology", hexahedra="0 1 2 3 4 5 6 7")
       preprocessing.addObject('MechanicalObject', name="state", template="Vec3", position="-1 -1 -1  1 -1 -1  1 1 -1  -1 1 -1  -1 -1 1  1 -1 1  1 1 1  -1 1 1")
       preprocessing.addObject('LinearToHigherOrderElements', name="engine")

       quadratic_elements = single_hexa.addChild('quadratic_elements')

       quadratic_elements.addObject('MeshTopology', name="topology", position="@../preprocessing/engine.position", quadratic_hexahedra="@../preprocessing/engine.quadratic_hexahedra")
       quadratic_elements.addObject('MechanicalObject', name="state", template="Vec3", position="@../preprocessing/engine.position")
       quadratic_elements.addObject('VisualPointCloud', position="@state.position", drawMode="Sphere", sphereRadius="0.1", color="lime", showIndices="true", indicesScale="2", indicesColor="black")
       quadratic_elements.addObject('VisualMesh', position="@state.position", topology="@topology")
    ```

