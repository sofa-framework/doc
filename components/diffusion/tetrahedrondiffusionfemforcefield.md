<!-- generate_doc -->
# TetrahedronDiffusionFEMForceField

Isotropic or anisotropic diffusion on Tetrahedral Meshes.


## Vec1d

Templates:

- Vec1d

__Target__: Sofa.Component.Diffusion

__namespace__: sofa::component::diffusion

__parents__:

- ForceField

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
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping - stiffness matrix coefficient
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>constantDiffusionCoefficient</td>
		<td>
Constant diffusion coefficient
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>tetraDiffusionCoefficient</td>
		<td>
Diffusion coefficient for each tetrahedron, by default equal to constantDiffusionCoefficient.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>anisotropyRatio</td>
		<td>
Anisotropy ratio (r²>1).
 Default is 1.0 = isotropy.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>transverseAnisotropyArray</td>
		<td>
Data to handle topology on tetrahedra
		</td>
		<td></td>
	</tr>
	<tr>
		<td>tagMechanics</td>
		<td>
Tag of the Mechanical Object.
		</td>
		<td>meca</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawConduc</td>
		<td>
To display conductivity map.
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
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec1d&gt;|
|topology|link to the topology container|BaseMeshTopology|

<!-- generate_doc -->
## Vec2d

Templates:

- Vec2d

__Target__: Sofa.Component.Diffusion

__namespace__: sofa::component::diffusion

__parents__:

- ForceField

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
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping - stiffness matrix coefficient
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>constantDiffusionCoefficient</td>
		<td>
Constant diffusion coefficient
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>tetraDiffusionCoefficient</td>
		<td>
Diffusion coefficient for each tetrahedron, by default equal to constantDiffusionCoefficient.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>anisotropyRatio</td>
		<td>
Anisotropy ratio (r²>1).
 Default is 1.0 = isotropy.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>transverseAnisotropyArray</td>
		<td>
Data to handle topology on tetrahedra
		</td>
		<td></td>
	</tr>
	<tr>
		<td>tagMechanics</td>
		<td>
Tag of the Mechanical Object.
		</td>
		<td>meca</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawConduc</td>
		<td>
To display conductivity map.
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
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec2d&gt;|
|topology|link to the topology container|BaseMeshTopology|

<!-- generate_doc -->
## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.Diffusion

__namespace__: sofa::component::diffusion

__parents__:

- ForceField

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
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping - stiffness matrix coefficient
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>constantDiffusionCoefficient</td>
		<td>
Constant diffusion coefficient
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>tetraDiffusionCoefficient</td>
		<td>
Diffusion coefficient for each tetrahedron, by default equal to constantDiffusionCoefficient.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>anisotropyRatio</td>
		<td>
Anisotropy ratio (r²>1).
 Default is 1.0 = isotropy.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>transverseAnisotropyArray</td>
		<td>
Data to handle topology on tetrahedra
		</td>
		<td></td>
	</tr>
	<tr>
		<td>tagMechanics</td>
		<td>
Tag of the Mechanical Object.
		</td>
		<td>meca</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawConduc</td>
		<td>
To display conductivity map.
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
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|
|topology|link to the topology container|BaseMeshTopology|

## Examples 

TetrahedronDiffusionFEMForceField.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.00001" gravity="0 0 0" >
        <Node name="plugins">
            <RequiredPlugin pluginName="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [LinearMovementProjectiveConstraint] -->
            <RequiredPlugin pluginName="Sofa.Component.Diffusion"/> <!-- Needed to use components [TetrahedronDiffusionFEMForceField] -->
            <RequiredPlugin pluginName="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
            <RequiredPlugin pluginName="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader MeshVTKLoader] -->
            <RequiredPlugin pluginName="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
            <RequiredPlugin pluginName="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
            <RequiredPlugin pluginName="Sofa.Component.Mass"/> <!-- Needed to use components [MeshMatrixMass] -->
            <RequiredPlugin pluginName="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin pluginName="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier] -->
            <RequiredPlugin pluginName="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
            <RequiredPlugin pluginName="Sofa.GL.Component.Engine"/> <!-- Needed to use components [TextureInterpolation] -->
            <RequiredPlugin pluginName="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        </Node>
    
        <VisualStyle displayFlags="showVisualModels"/>
    
        <MeshVTKLoader name="meshLoader" filename="mesh/raptorTetra_8418.vtu" />
        <MeshOBJLoader name="potentialLoader" filename="mesh/raptorTemperature.obj" />
        
        <TetrahedronSetTopologyContainer name="topo" src="@meshLoader" tags="mechanics"/>
        <MechanicalObject template="Vec3" name="raptorDOFs" src="@meshLoader" tags="mechanics" />
        <TetrahedronSetTopologyModifier name="Modifier" tags="mechanics"/>
        <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo"  tags="mechanics"/>
        <BoxROI name="box-hot" box="-3 4 4 3 8 8" drawBoxes="1" position="@raptorDOFs.position"/>
        <BoxROI name="box-cold" box="-3 4 -4 3 8 -10" drawBoxes="1" position="@raptorDOFs.position"/>
        <DefaultAnimationLoop/>
    
    
        <Node name="Temperature" gravity="0 0 0"  >
    
            <EulerImplicitSolver name="EulerExplicitSolver" firstOrder="1" tags="heat" rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver name="CG" iterations="1000" tolerance="1.0e-10" threshold="1.0e-30" tags="heat"/>
            <MechanicalObject template="Vec1" position="@../potentialLoader.position"  name="gridTemperature" bbox="0 0 0 0 0 0" tags="heat"/>
            <TetrahedronDiffusionFEMForceField template="Vec1" name="DiffusionForceField" topology="@../topo"
                                               constantDiffusionCoefficient="1500" printLog="0" drawConduc="0"
                                               tagMechanics="mechanics" tags="heat"/>
            <MeshMatrixMass name="Mass" template="Vec1,Vec3" lumping="0" massDensity="1.0" printLog="0" tags="heat" topology="@../topo" geometryState="@../raptorDOFs"/>
    
            <LinearMovementProjectiveConstraint template="Vec1" keyTimes="0 0.005 0.006" movements="0 0 1" indices="@../box-cold.indices" />
            <LinearMovementProjectiveConstraint template="Vec1" keyTimes="0.001 0.002 0.004 0.005 0.006" movements="0 1 0.5 1 0" indices="@../box-hot.indices" />
    
            <!-- color palette: https://coolors.co/palette/f94144-f3722c-f8961e-f9844a-f9c74f-90be6d-43aa8b-4d908e-577590-277da1 -->
            <VisualMesh position="@../raptorDOFs.position" elementSpace="0.2" lighting="true"
                        vertexValues="@gridTemperature.position"
                        colorMap="#277DA1 #577590 #4D908E #43AA8B #90BE6D #F9C74F #F9844A #F8961E #F3722C #F94144"/>
    
    <!--        <Node name="Visu">-->
    <!--            <TextureInterpolation template="Vec1" name="EngineInterpolation"  input_states="@../gridTemperature.position"  input_coordinates="@../../raptorDOFs.position"  min_value="0.0"  max_value="1.0"  manual_scale="1"  drawPotentiels="0"  showIndicesScale="5e-05" />-->
    <!--            <OglModel template="Vec3" name="oglPotentiel" texcoords="@EngineInterpolation.output_coordinates" handleDynamicTopology="0" texturename="textures/heatColor.bmp" scale3d="1 1 1"  material="Default Diffuse 1 1 1 1 0.5 Ambient 1 1 1 1 0.3 Specular 0 0.5 0.5 0.5 1 Emissive 0 0.5 0.5 0.5 1 Shininess 0 45 No texture linked to the material No bump texture linked to the material "/>-->
    <!--            <IdentityMapping input="@../../raptorDOFs" output="@oglPotentiel" />-->
    <!--        </Node>-->
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.00001", gravity="0 0 0")

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Constraint.Projective")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Diffusion")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Engine.Select")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.IO.Mesh")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSolver.Iterative")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Mapping.Linear")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Mass")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.ODESolver.Backward")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Dynamic")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Visual")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.GL.Component.Engine")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.GL.Component.Rendering3D")

       root.addObject('VisualStyle', displayFlags="showVisualModels")
       root.addObject('MeshVTKLoader', name="meshLoader", filename="mesh/raptorTetra_8418.vtu")
       root.addObject('MeshOBJLoader', name="potentialLoader", filename="mesh/raptorTemperature.obj")
       root.addObject('TetrahedronSetTopologyContainer', name="topo", src="@meshLoader", tags="mechanics")
       root.addObject('MechanicalObject', template="Vec3", name="raptorDOFs", src="@meshLoader", tags="mechanics")
       root.addObject('TetrahedronSetTopologyModifier', name="Modifier", tags="mechanics")
       root.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo", tags="mechanics")
       root.addObject('BoxROI', name="box-hot", box="-3 4 4 3 8 8", drawBoxes="1", position="@raptorDOFs.position")
       root.addObject('BoxROI', name="box-cold", box="-3 4 -4 3 8 -10", drawBoxes="1", position="@raptorDOFs.position")
       root.addObject('DefaultAnimationLoop', )

       temperature = root.addChild('Temperature', gravity="0 0 0")

       temperature.addObject('EulerImplicitSolver', name="EulerExplicitSolver", firstOrder="1", tags="heat", rayleighStiffness="0.1", rayleighMass="0.1")
       temperature.addObject('CGLinearSolver', name="CG", iterations="1000", tolerance="1.0e-10", threshold="1.0e-30", tags="heat")
       temperature.addObject('MechanicalObject', template="Vec1", position="@../potentialLoader.position", name="gridTemperature", bbox="0 0 0 0 0 0", tags="heat")
       temperature.addObject('TetrahedronDiffusionFEMForceField', template="Vec1", name="DiffusionForceField", topology="@../topo", constantDiffusionCoefficient="1500", printLog="0", drawConduc="0", tagMechanics="mechanics", tags="heat")
       temperature.addObject('MeshMatrixMass', name="Mass", template="Vec1,Vec3", lumping="0", massDensity="1.0", printLog="0", tags="heat", topology="@../topo", geometryState="@../raptorDOFs")
       temperature.addObject('LinearMovementProjectiveConstraint', template="Vec1", keyTimes="0 0.005 0.006", movements="0 0 1", indices="@../box-cold.indices")
       temperature.addObject('LinearMovementProjectiveConstraint', template="Vec1", keyTimes="0.001 0.002 0.004 0.005 0.006", movements="0 1 0.5 1 0", indices="@../box-hot.indices")
       temperature.addObject('VisualMesh', position="@../raptorDOFs.position", elementSpace="0.2", lighting="true", vertexValues="@gridTemperature.position", colorMap="#277DA1 #577590 #4D908E #43AA8B #90BE6D #F9C74F #F9844A #F8961E #F3722C #F94144")
    ```

