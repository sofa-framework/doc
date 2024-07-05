# OglVolumetricModel

Volumetric model for OpenGL display


__Target__: `VolumetricRendering`

__namespace__: `#!c++ sofa::component::visualmodel`

__parents__: 

- `#!c++ VisualModel`
- `#!c++ VisualState`

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

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|



## Examples

VolumetricRendering/OglVolumetricModel_hexa_link.scn

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
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02")
        root.addObject('RequiredPlugin', name="VolumetricRendering")

        Input = root.addChild('Input')
        Input.addObject('SparseGridTopology', name="grid", n="51 51 51", fileTopology="mesh/raptor_8kp.obj")
        Input.addObject('MechanicalObject', name="dofs", template="Vec3d")
        Input.addObject('HexahedronSetTopologyContainer', name="topology", hexahedra="@grid.hexahedra")

        root = root.addChild('root')
        root.addObject('OglShader', geometryVerticesOut="12", geometryInputType="10", geometryOutputType="5", fileVertexShaders="['share/shaders/tetra.vert']", fileGeometryShaders="['share/shaders/tetra_triangles.geo']", fileFragmentShaders="['share/shaders/tetra.frag']")
        root.addObject('OglFloatVariable', id="volumeScale", value="0.9")
        root.addObject('OglFloatVariable', id="u_enableLight", value="1")
        root.addObject('OglVolumetricModel', position="@../Input/dofs.position", hexahedra="@../Input/topology.hexahedra", printLog="false", color="1 0 1 1")
    ```

VolumetricRendering/OglVolumetricModel_tetra.scn

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
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02")
        root.addObject('RequiredPlugin', name="VolumetricRendering")
        root.addObject('MeshVTKLoader', name="loader", filename="mesh/raptorTetra_8418.vtu")
        root.addObject('MechanicalObject', src="@loader", template="Vec3d")
        root.addObject('include', href="Objects/TetrahedronSetTopology.xml", src="@loader")

        root = root.addChild('root')
        root.addObject('OglShader', geometryVerticesOut="12", geometryInputType="10", geometryOutputType="5", vertFilename="share/shaders/tetra.vert", geoFilename="share/shaders/tetra_triangles.geo", fragFilename="share/shaders/tetra.frag")
        root.addObject('OglFloatVariable', id="volumeScale", value="0.9")
        root.addObject('OglFloatVariable', id="u_enableLight", value="1")
        root.addObject('OglFloat4Attribute', id="a_vertexColor", value="@../loader.position")
        root.addObject('OglVolumetricModel', printLog="false")
    ```

VolumetricRendering/OglVolumetricModel_hexa.scn

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
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Shader")
        root.addObject('RequiredPlugin', name="VolumetricRendering")
        root.addObject('DefaultAnimationLoop')
        root.addObject('SparseGridTopology', name="grid", n="51 51 51", fileTopology="mesh/raptor_8kp.obj")
        root.addObject('MechanicalObject', template="Vec3d")
        root.addObject('HexahedronSetTopologyContainer', hexahedra="@grid.hexahedra")

        root = root.addChild('root')
        root.addObject('OglShader', geometryVerticesOut="12", geometryInputType="10", geometryOutputType="5", fileVertexShaders="['share/shaders/tetra.vert']", fileGeometryShaders="['share/shaders/tetra_triangles.geo']", fileFragmentShaders="['share/shaders/tetra.frag']")
        root.addObject('OglFloatVariable', id="volumeScale", value="0.9")
        root.addObject('OglFloatVariable', id="u_enableLight", value="1")
        root.addObject('OglVolumetricModel', printLog="false", color="1 0 1 1")
    ```

VolumetricRendering/OglVolumetricModel_physics.scn

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
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02")
        root.addObject('RequiredPlugin', name="VolumetricRendering")

        HexaRaptor = root.addChild('HexaRaptor')
        HexaRaptor.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
        HexaRaptor.addObject('CGLinearSolver', iterations="100", tolerance="1.0e-7", threshold="1.0e-7")
        HexaRaptor.addObject('SparseGridTopology', name="grid", n="21 21 21", fileTopology="mesh/raptor_8kp.obj")
        HexaRaptor.addObject('MechanicalObject', name="dofs", template="Vec3d")
        HexaRaptor.addObject('HexahedronSetTopologyContainer', hexahedra="@grid.hexahedra")
        HexaRaptor.addObject('HexahedronSetGeometryAlgorithms')
        HexaRaptor.addObject('HexahedronFEMForceField', name="FEM", youngModulus="500", poissonRatio="0.4", method="large")

        HexaRaptor = HexaRaptor.addChild('HexaRaptor')
        HexaRaptor.addObject('OglShader', geometryVerticesOut="12", geometryInputType="10", geometryOutputType="5", vertFilename="share/shaders/tetra.vert", geoFilename="share/shaders/tetra_triangles.geo", fragFilename="share/shaders/tetra.frag")
        HexaRaptor.addObject('OglFloatVariable', id="volumeScale", value="0.9")
        HexaRaptor.addObject('OglFloatVariable', id="u_enableLight", value="1")
        HexaRaptor.addObject('OglFloat4Attribute', id="a_vertexColor", value="@../grid.position")
        HexaRaptor.addObject('OglVolumetricModel', printLog="false", color="1 0 1 1")
        HexaRaptor.addObject('IdentityMapping')
    ```

VolumetricRendering/OglVolumetricModel_tetra_clipped_physics.scn

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
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02")
        root.addObject('RequiredPlugin', name="VolumetricRendering")

        HexaRaptor = root.addChild('HexaRaptor')
        HexaRaptor.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
        HexaRaptor.addObject('CGLinearSolver', iterations="100", tolerance="1.0e-7", threshold="1.0e-7")
        HexaRaptor.addObject('MeshVTKLoader', name="loader", filename="mesh/raptorTetra_8418.vtu")
        HexaRaptor.addObject('MechanicalObject', src="@loader", template="Vec3d")
        HexaRaptor.addObject('include', href="Objects/TetrahedronSetTopology.xml", src="@loader")
        HexaRaptor.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="500", poissonRatio="0.4", method="large", computeVonMisesStress="2")

        HexaRaptor = HexaRaptor.addChild('HexaRaptor')
        HexaRaptor.addObject('ClipPlane', id="0", position="0 0 0", normal="0 0 1")
        HexaRaptor.addObject('OglShader', geometryVerticesOut="12", geometryInputType="10", geometryOutputType="5", vertFilename="share/shaders/tetra.vert", geoFilename="share/shaders/tetra_triangles.geo", fragFilename="share/shaders/tetra.frag")
        HexaRaptor.addObject('OglFloatVariable', id="volumeScale", value="0.9")
        HexaRaptor.addObject('OglFloatVariable', id="u_enableLight", value="1")
        HexaRaptor.addObject('OglFloat4Attribute', id="a_vertexColor", value="@../FEM.vonMisesStressColors")
        HexaRaptor.addObject('OglVolumetricModel', printLog="false", color="1 0 1 1")
        HexaRaptor.addObject('IdentityMapping')
    ```

VolumetricRendering/OglVolumetricModel_hexa_physics.scn

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
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02")
        root.addObject('RequiredPlugin', name="VolumetricRendering")

        HexaRaptor = root.addChild('HexaRaptor')
        HexaRaptor.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
        HexaRaptor.addObject('CGLinearSolver', iterations="100", tolerance="1.0e-7", threshold="1.0e-7")
        HexaRaptor.addObject('SparseGridTopology', name="grid", n="21 21 21", fileTopology="mesh/raptor_8kp.obj")
        HexaRaptor.addObject('MechanicalObject', name="dofs", template="Vec3d")
        HexaRaptor.addObject('HexahedronSetTopologyContainer', hexahedra="@grid.hexahedra")
        HexaRaptor.addObject('HexahedronSetGeometryAlgorithms')
        HexaRaptor.addObject('HexahedronFEMForceField', name="FEM", youngModulus="500", poissonRatio="0.4", method="large")

        HexaRaptor = HexaRaptor.addChild('HexaRaptor')
        HexaRaptor.addObject('OglShader', geometryVerticesOut="12", geometryInputType="10", geometryOutputType="5", vertFilename="share/shaders/tetra.vert", geoFilename="share/shaders/tetra_triangles.geo", fragFilename="share/shaders/tetra.frag")
        HexaRaptor.addObject('OglFloatVariable', id="volumeScale", value="0.9")
        HexaRaptor.addObject('OglFloatVariable', id="u_enableLight", value="1")
        HexaRaptor.addObject('OglFloat4Attribute', id="a_vertexColor", value="@../grid.position")
        HexaRaptor.addObject('OglVolumetricModel', printLog="false", color="1 0 1 1")
        HexaRaptor.addObject('IdentityMapping')
    ```

VolumetricRendering/OglVolumetricModel_tetra_physics.scn

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
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02")
        root.addObject('RequiredPlugin', name="VolumetricRendering")

        HexaRaptor = root.addChild('HexaRaptor')
        HexaRaptor.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
        HexaRaptor.addObject('CGLinearSolver', iterations="100", tolerance="1.0e-7", threshold="1.0e-7")
        HexaRaptor.addObject('MeshVTKLoader', name="loader", filename="mesh/raptorTetra_8418.vtu")
        HexaRaptor.addObject('MechanicalObject', src="@loader", template="Vec3d")
        HexaRaptor.addObject('include', href="Objects/TetrahedronSetTopology.xml", src="@loader")
        HexaRaptor.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="500", poissonRatio="0.4", method="large", computeVonMisesStress="2")

        HexaRaptor = HexaRaptor.addChild('HexaRaptor')
        HexaRaptor.addObject('OglShader', geometryVerticesOut="12", geometryInputType="10", geometryOutputType="5", vertFilename="share/shaders/tetra.vert", geoFilename="share/shaders/tetra_triangles.geo", fragFilename="share/shaders/tetra.frag")
        HexaRaptor.addObject('OglFloatVariable', id="volumeScale", value="0.9")
        HexaRaptor.addObject('OglFloatVariable', id="u_enableLight", value="1")
        HexaRaptor.addObject('OglFloat4Attribute', id="a_vertexColor", value="@../FEM.vonMisesStressColors")
        HexaRaptor.addObject('OglVolumetricModel', printLog="false", color="1 0 1 1")
        HexaRaptor.addObject('IdentityMapping')
    ```

