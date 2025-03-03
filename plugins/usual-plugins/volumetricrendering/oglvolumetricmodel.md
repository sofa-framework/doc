<!-- generate_doc -->
# OglVolumetricModel

Volumetric model for OpenGL display


__Target__: VolumetricRendering

__namespace__: sofa::component::visualmodel

__parents__:

- VisualModel
- VisualState

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
		<td>tetrahedra</td>
		<td>
Tetrahedra to draw
		</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedra</td>
		<td>
Hexahedra to draw
		</td>
		<td></td>
	</tr>
	<tr>
		<td>volumeScale</td>
		<td>
Scale for each volumetric primitive
		</td>
		<td>1</td>
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
	<tr>
		<td>defaultColor</td>
		<td>
Color for each volume (if the attribute a_vertexColor is not detected)
		</td>
		<td>0 0 0 0</td>
	</tr>
	<tr>
		<td colspan="3">Vector</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Vertices coordinates
		</td>
		<td></td>
	</tr>
	<tr>
		<td>restPosition</td>
		<td>
Vertices rest coordinates
		</td>
		<td></td>
	</tr>
	<tr>
		<td>normal</td>
		<td>
Normals of the model
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

OglVolumetricModel_physics.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.02">
        <RequiredPlugin name="VolumetricRendering" />
    
        <Node name="HexaRaptor" >
            <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="100" tolerance="1.0e-7" threshold="1.0e-7"/>
    
    		<SparseGridTopology name="grid" n="21 21 21" fileTopology="mesh/raptor_8kp.obj" />
    
    		<MechanicalObject name="dofs" template="Vec3d" />
    	 	<HexahedronSetTopologyContainer hexahedra="@grid.hexahedra" />
    	 	<HexahedronSetGeometryAlgorithms />
    
    	 	<HexahedronFEMForceField name="FEM" youngModulus="500" poissonRatio="0.4" method="large" />
    
    		<Node>
    	 		<OglShader geometryVerticesOut="12" geometryInputType="10" geometryOutputType="5" 
    	 			vertFilename="share/shaders/tetra.vert" geoFilename="share/shaders/tetra_triangles.geo" fragFilename="share/shaders/tetra.frag" />
    	 		<OglFloatVariable id="volumeScale" value="0.9"/>
    	 		<OglFloatVariable id="u_enableLight" value="1"/>
    	 		<OglFloat4Attribute id="a_vertexColor" value="@../grid.position"/>
    			<OglVolumetricModel printLog="false" color="1 0 1 1" />
    
    			<IdentityMapping />
    		</Node>
    	</Node>
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02")

       root.addObject('RequiredPlugin', name="VolumetricRendering")

       hexa_raptor = root.addChild('HexaRaptor')

       hexa_raptor.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
       hexa_raptor.addObject('CGLinearSolver', iterations="100", tolerance="1.0e-7", threshold="1.0e-7")
       hexa_raptor.addObject('SparseGridTopology', name="grid", n="21 21 21", fileTopology="mesh/raptor_8kp.obj")
       hexa_raptor.addObject('MechanicalObject', name="dofs", template="Vec3d")
       hexa_raptor.addObject('HexahedronSetTopologyContainer', hexahedra="@grid.hexahedra")
       hexa_raptor.addObject('HexahedronSetGeometryAlgorithms', )
       hexa_raptor.addObject('HexahedronFEMForceField', name="FEM", youngModulus="500", poissonRatio="0.4", method="large")

       node = HexaRaptor.addChild('node')

       node.addObject('OglShader', geometryVerticesOut="12", geometryInputType="10", geometryOutputType="5", vertFilename="share/shaders/tetra.vert", geoFilename="share/shaders/tetra_triangles.geo", fragFilename="share/shaders/tetra.frag")
       node.addObject('OglFloatVariable', id="volumeScale", value="0.9")
       node.addObject('OglFloatVariable', id="u_enableLight", value="1")
       node.addObject('OglFloat4Attribute', id="a_vertexColor", value="@../grid.position")
       node.addObject('OglVolumetricModel', printLog="false", color="1 0 1 1")
       node.addObject('IdentityMapping', )
    ```

OglVolumetricModel_hexa.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [HexahedronSetTopologyContainer] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [SparseGridTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Shader"/> <!-- Needed to use components [OglFloatVariable,OglShader] -->
        <RequiredPlugin name="VolumetricRendering" />
    
        <DefaultAnimationLoop/>
        <SparseGridTopology name="grid" n="51 51 51" fileTopology="mesh/raptor_8kp.obj" />
    
        <MechanicalObject template="Vec3d" />
        <HexahedronSetTopologyContainer hexahedra="@grid.hexahedra" />
    
        <Node>
            <OglShader geometryVerticesOut="12" geometryInputType="10" geometryOutputType="5"
                       fileVertexShaders="['share/shaders/tetra.vert']" fileGeometryShaders="['share/shaders/tetra_triangles.geo']" fileFragmentShaders="['share/shaders/tetra.frag']" />
            <OglFloatVariable id="volumeScale" value="0.9"/>
            <OglFloatVariable id="u_enableLight" value="1"/>
            <OglVolumetricModel printLog="false" color="1 0 1 1" />
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02")

       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Shader")
       root.addObject('RequiredPlugin', name="VolumetricRendering")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('SparseGridTopology', name="grid", n="51 51 51", fileTopology="mesh/raptor_8kp.obj")
       root.addObject('MechanicalObject', template="Vec3d")
       root.addObject('HexahedronSetTopologyContainer', hexahedra="@grid.hexahedra")

       node = root.addChild('node')

       node.addObject('OglShader', geometryVerticesOut="12", geometryInputType="10", geometryOutputType="5", fileVertexShaders="['share/shaders/tetra.vert']", fileGeometryShaders="['share/shaders/tetra_triangles.geo']", fileFragmentShaders="['share/shaders/tetra.frag']")
       node.addObject('OglFloatVariable', id="volumeScale", value="0.9")
       node.addObject('OglFloatVariable', id="u_enableLight", value="1")
       node.addObject('OglVolumetricModel', printLog="false", color="1 0 1 1")
    ```

OglVolumetricModel_tetra.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.02">
        <RequiredPlugin name="VolumetricRendering" />
    
    	<MeshVTKLoader name="loader" filename="mesh/raptorTetra_8418.vtu" />
    	<MechanicalObject src="@loader" template="Vec3d" />
     	<include href="Objects/TetrahedronSetTopology.xml" src="@loader" />
    
    	<Node>
     		<OglShader geometryVerticesOut="12" geometryInputType="10" geometryOutputType="5" 
     			vertFilename="share/shaders/tetra.vert" geoFilename="share/shaders/tetra_triangles.geo" fragFilename="share/shaders/tetra.frag" />
     		<OglFloatVariable id="volumeScale" value="0.9"/>
     		<OglFloatVariable id="u_enableLight" value="1"/>
     		<OglFloat4Attribute id="a_vertexColor" value="@../loader.position"/>
    		<OglVolumetricModel printLog="false"  />
    	</Node>
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02")

       root.addObject('RequiredPlugin', name="VolumetricRendering")
       root.addObject('MeshVTKLoader', name="loader", filename="mesh/raptorTetra_8418.vtu")
       root.addObject('MechanicalObject', src="@loader", template="Vec3d")
       root.addObject('include', href="Objects/TetrahedronSetTopology.xml", src="@loader")

       node = root.addChild('node')

       node.addObject('OglShader', geometryVerticesOut="12", geometryInputType="10", geometryOutputType="5", vertFilename="share/shaders/tetra.vert", geoFilename="share/shaders/tetra_triangles.geo", fragFilename="share/shaders/tetra.frag")
       node.addObject('OglFloatVariable', id="volumeScale", value="0.9")
       node.addObject('OglFloatVariable', id="u_enableLight", value="1")
       node.addObject('OglFloat4Attribute', id="a_vertexColor", value="@../loader.position")
       node.addObject('OglVolumetricModel', printLog="false")
    ```

OglVolumetricModel_tetra_clipped_physics.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.02">
        <RequiredPlugin name="VolumetricRendering" />
    
        <Node name="HexaRaptor" >
            <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="100" tolerance="1.0e-7" threshold="1.0e-7"/>
    
    		<MeshVTKLoader name="loader" filename="mesh/raptorTetra_8418.vtu" />
    		<MechanicalObject src="@loader" template="Vec3d" />
     		<include href="Objects/TetrahedronSetTopology.xml" src="@loader" />
    
    	 	<TetrahedronFEMForceField name="FEM" youngModulus="500" poissonRatio="0.4" method="large"
    	 		computeVonMisesStress="2"
    	 	 />
    
     		<Node>
    			<ClipPlane id="0" position="0 0 0" normal="0 0 1" />
    	 		<OglShader geometryVerticesOut="12" geometryInputType="10" geometryOutputType="5" 
    	 			vertFilename="share/shaders/tetra.vert" geoFilename="share/shaders/tetra_triangles.geo" fragFilename="share/shaders/tetra.frag" />
    	 		<OglFloatVariable id="volumeScale" value="0.9"/>
    	 		<OglFloatVariable id="u_enableLight" value="1"/>
    	 		<OglFloat4Attribute id="a_vertexColor" value="@../FEM.vonMisesStressColors"/>
    			<OglVolumetricModel printLog="false" color="1 0 1 1" />
    
    			<IdentityMapping />
    		</Node>
    	</Node>
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02")

       root.addObject('RequiredPlugin', name="VolumetricRendering")

       hexa_raptor = root.addChild('HexaRaptor')

       hexa_raptor.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
       hexa_raptor.addObject('CGLinearSolver', iterations="100", tolerance="1.0e-7", threshold="1.0e-7")
       hexa_raptor.addObject('MeshVTKLoader', name="loader", filename="mesh/raptorTetra_8418.vtu")
       hexa_raptor.addObject('MechanicalObject', src="@loader", template="Vec3d")
       hexa_raptor.addObject('include', href="Objects/TetrahedronSetTopology.xml", src="@loader")
       hexa_raptor.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="500", poissonRatio="0.4", method="large", computeVonMisesStress="2")

       node = HexaRaptor.addChild('node')

       node.addObject('ClipPlane', id="0", position="0 0 0", normal="0 0 1")
       node.addObject('OglShader', geometryVerticesOut="12", geometryInputType="10", geometryOutputType="5", vertFilename="share/shaders/tetra.vert", geoFilename="share/shaders/tetra_triangles.geo", fragFilename="share/shaders/tetra.frag")
       node.addObject('OglFloatVariable', id="volumeScale", value="0.9")
       node.addObject('OglFloatVariable', id="u_enableLight", value="1")
       node.addObject('OglFloat4Attribute', id="a_vertexColor", value="@../FEM.vonMisesStressColors")
       node.addObject('OglVolumetricModel', printLog="false", color="1 0 1 1")
       node.addObject('IdentityMapping', )
    ```

OglVolumetricModel_hexa_physics.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.02">
        <RequiredPlugin name="VolumetricRendering" />
    
        <Node name="HexaRaptor" >
            <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="100" tolerance="1.0e-7" threshold="1.0e-7"/>
    
    		<SparseGridTopology name="grid" n="21 21 21" fileTopology="mesh/raptor_8kp.obj" />
    
    		<MechanicalObject name="dofs" template="Vec3d" />
    	 	<HexahedronSetTopologyContainer hexahedra="@grid.hexahedra" />
    	 	<HexahedronSetGeometryAlgorithms />
    
    	 	<HexahedronFEMForceField name="FEM" youngModulus="500" poissonRatio="0.4" method="large" />
    
    		<Node>
    	 		<OglShader geometryVerticesOut="12" geometryInputType="10" geometryOutputType="5" 
    	 			vertFilename="share/shaders/tetra.vert" geoFilename="share/shaders/tetra_triangles.geo" fragFilename="share/shaders/tetra.frag" />
    	 		<OglFloatVariable id="volumeScale" value="0.9"/>
    	 		<OglFloatVariable id="u_enableLight" value="1"/>
    	 		<OglFloat4Attribute id="a_vertexColor" value="@../grid.position"/>
    			<OglVolumetricModel printLog="false" color="1 0 1 1" />
    
    			<IdentityMapping />
    		</Node>
    	</Node>
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02")

       root.addObject('RequiredPlugin', name="VolumetricRendering")

       hexa_raptor = root.addChild('HexaRaptor')

       hexa_raptor.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
       hexa_raptor.addObject('CGLinearSolver', iterations="100", tolerance="1.0e-7", threshold="1.0e-7")
       hexa_raptor.addObject('SparseGridTopology', name="grid", n="21 21 21", fileTopology="mesh/raptor_8kp.obj")
       hexa_raptor.addObject('MechanicalObject', name="dofs", template="Vec3d")
       hexa_raptor.addObject('HexahedronSetTopologyContainer', hexahedra="@grid.hexahedra")
       hexa_raptor.addObject('HexahedronSetGeometryAlgorithms', )
       hexa_raptor.addObject('HexahedronFEMForceField', name="FEM", youngModulus="500", poissonRatio="0.4", method="large")

       node = HexaRaptor.addChild('node')

       node.addObject('OglShader', geometryVerticesOut="12", geometryInputType="10", geometryOutputType="5", vertFilename="share/shaders/tetra.vert", geoFilename="share/shaders/tetra_triangles.geo", fragFilename="share/shaders/tetra.frag")
       node.addObject('OglFloatVariable', id="volumeScale", value="0.9")
       node.addObject('OglFloatVariable', id="u_enableLight", value="1")
       node.addObject('OglFloat4Attribute', id="a_vertexColor", value="@../grid.position")
       node.addObject('OglVolumetricModel', printLog="false", color="1 0 1 1")
       node.addObject('IdentityMapping', )
    ```

OglVolumetricModel_tetra_physics.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.02">
        <RequiredPlugin name="VolumetricRendering" />
    
        <Node name="HexaRaptor" >
            <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="100" tolerance="1.0e-7" threshold="1.0e-7"/>
    
    		<MeshVTKLoader name="loader" filename="mesh/raptorTetra_8418.vtu" />
    		<MechanicalObject src="@loader" template="Vec3d" />
     		<include href="Objects/TetrahedronSetTopology.xml" src="@loader" />
    
    	 	<TetrahedronFEMForceField name="FEM" youngModulus="500" poissonRatio="0.4" method="large"
    	 		computeVonMisesStress="2"
    	 	 />
    
    		<Node>
    	 		<OglShader geometryVerticesOut="12" geometryInputType="10" geometryOutputType="5" 
    	 			vertFilename="share/shaders/tetra.vert" geoFilename="share/shaders/tetra_triangles.geo" fragFilename="share/shaders/tetra.frag" />
    	 		<OglFloatVariable id="volumeScale" value="0.9"/>
    	 		<OglFloatVariable id="u_enableLight" value="1"/>
    	 		<OglFloat4Attribute id="a_vertexColor" value="@../FEM.vonMisesStressColors"/>
    			<OglVolumetricModel printLog="false" color="1 0 1 1" />
    
    			<IdentityMapping />
    		</Node>
    	</Node>
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02")

       root.addObject('RequiredPlugin', name="VolumetricRendering")

       hexa_raptor = root.addChild('HexaRaptor')

       hexa_raptor.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
       hexa_raptor.addObject('CGLinearSolver', iterations="100", tolerance="1.0e-7", threshold="1.0e-7")
       hexa_raptor.addObject('MeshVTKLoader', name="loader", filename="mesh/raptorTetra_8418.vtu")
       hexa_raptor.addObject('MechanicalObject', src="@loader", template="Vec3d")
       hexa_raptor.addObject('include', href="Objects/TetrahedronSetTopology.xml", src="@loader")
       hexa_raptor.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="500", poissonRatio="0.4", method="large", computeVonMisesStress="2")

       node = HexaRaptor.addChild('node')

       node.addObject('OglShader', geometryVerticesOut="12", geometryInputType="10", geometryOutputType="5", vertFilename="share/shaders/tetra.vert", geoFilename="share/shaders/tetra_triangles.geo", fragFilename="share/shaders/tetra.frag")
       node.addObject('OglFloatVariable', id="volumeScale", value="0.9")
       node.addObject('OglFloatVariable', id="u_enableLight", value="1")
       node.addObject('OglFloat4Attribute', id="a_vertexColor", value="@../FEM.vonMisesStressColors")
       node.addObject('OglVolumetricModel', printLog="false", color="1 0 1 1")
       node.addObject('IdentityMapping', )
    ```

OglVolumetricModel_hexa_link.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.02">
        <RequiredPlugin name="VolumetricRendering" />
    
        <Node name="Input">
            <SparseGridTopology name="grid" n="51 51 51" fileTopology="mesh/raptor_8kp.obj" />
    
            <MechanicalObject name="dofs" template="Vec3d" />
            <HexahedronSetTopologyContainer name="topology" hexahedra="@grid.hexahedra" />
        </Node>
    
        <Node>
            <OglShader geometryVerticesOut="12" geometryInputType="10" geometryOutputType="5"
                       fileVertexShaders="['share/shaders/tetra.vert']" fileGeometryShaders="['share/shaders/tetra_triangles.geo']" fileFragmentShaders="['share/shaders/tetra.frag']" />
            <OglFloatVariable id="volumeScale" value="0.9"/>
            <OglFloatVariable id="u_enableLight" value="1"/>
            <OglVolumetricModel position="@../Input/dofs.position" hexahedra="@../Input/topology.hexahedra" printLog="false" color="1 0 1 1" />
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02")

       root.addObject('RequiredPlugin', name="VolumetricRendering")

       input = root.addChild('Input')

       input.addObject('SparseGridTopology', name="grid", n="51 51 51", fileTopology="mesh/raptor_8kp.obj")
       input.addObject('MechanicalObject', name="dofs", template="Vec3d")
       input.addObject('HexahedronSetTopologyContainer', name="topology", hexahedra="@grid.hexahedra")

       node = root.addChild('node')

       node.addObject('OglShader', geometryVerticesOut="12", geometryInputType="10", geometryOutputType="5", fileVertexShaders="['share/shaders/tetra.vert']", fileGeometryShaders="['share/shaders/tetra_triangles.geo']", fileFragmentShaders="['share/shaders/tetra.frag']")
       node.addObject('OglFloatVariable', id="volumeScale", value="0.9")
       node.addObject('OglFloatVariable', id="u_enableLight", value="1")
       node.addObject('OglVolumetricModel', position="@../Input/dofs.position", hexahedra="@../Input/topology.hexahedra", printLog="false", color="1 0 1 1")
    ```

