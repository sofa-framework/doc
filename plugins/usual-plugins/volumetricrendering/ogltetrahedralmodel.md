<!-- generate_doc -->
# OglTetrahedralModel

Tetrahedral model for OpenGL display.


## Vec3d

Templates:

- Vec3d

__Target__: VolumetricRendering

__namespace__: volumetricrendering

__parents__:

- VisualModel

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
		<td>enable</td>
		<td>
Display the object or not
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Vertices coordinates
		</td>
		<td></td>
	</tr>
	<tr>
		<td>depthTest</td>
		<td>
Set Depth Test
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>blending</td>
		<td>
Set Blending
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

## Examples 

OglTetrahedralModel.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.02">
    
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshVTKLoader] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms,TetrahedronSetTopologyContainer,TetrahedronSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.GL.Component.Shader"/> <!-- Needed to use components [OglFloat4Variable,OglFloatVariable,OglShader] -->
        <RequiredPlugin name="VolumetricRendering"/>
    
        <DefaultAnimationLoop/>
        <MeshVTKLoader name="loader" filename="mesh/raptorTetra_8418.vtu" />
        <MechanicalObject src="@loader" template="Vec3d" />
        <include href="Objects/TetrahedronSetTopology.xml" src="@loader" />
    
        <Node>
            <OglShader geometryVerticesOut="12" geometryInputType="10" geometryOutputType="5" fileVertexShaders="['shaders/tetra.vert']" fileGeometryShaders="['shaders/tetra_triangles.geo']" fileFragmentShaders="['shaders/tetra.frag']" />
            <OglFloat4Variable id="vertexColor" value="1 1 0 1"/>
            <OglFloatVariable id="tetraScale" value="0.8"/>
            <OglFloatVariable id="u_enableLight" value="2"/>
            <OglTetrahedralModel template="Vec3d" />
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02")

       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Shader")
       root.addObject('RequiredPlugin', name="VolumetricRendering")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('MeshVTKLoader', name="loader", filename="mesh/raptorTetra_8418.vtu")
       root.addObject('MechanicalObject', src="@loader", template="Vec3d")
       root.addObject('include', href="Objects/TetrahedronSetTopology.xml", src="@loader")

       node = root.addChild('node')

       node.addObject('OglShader', geometryVerticesOut="12", geometryInputType="10", geometryOutputType="5", fileVertexShaders="['shaders/tetra.vert']", fileGeometryShaders="['shaders/tetra_triangles.geo']", fileFragmentShaders="['shaders/tetra.frag']")
       node.addObject('OglFloat4Variable', id="vertexColor", value="1 1 0 1")
       node.addObject('OglFloatVariable', id="tetraScale", value="0.8")
       node.addObject('OglFloatVariable', id="u_enableLight", value="2")
       node.addObject('OglTetrahedralModel', template="Vec3d")
    ```

