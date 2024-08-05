# TetrahedronDiffusionFEMForceField

Isotropic or anisotropic diffusion on Tetrahedral Meshes


__Templates__:

- `#!c++ Vec1d`
- `#!c++ Vec2d`
- `#!c++ Vec3d`

__Target__: `Sofa.Component.Diffusion`

__namespace__: `#!c++ sofa::component::diffusion`

__parents__: 

- `#!c++ ForceField`

__categories__: 

- ForceField

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
Anisotropy ratio (r²&gt;1).
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

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|mechanicalStates|List of mechanical states to which this component is associated|
|mstate|MechanicalState used by this component|
|topology|link to the topology container|



## Examples

Component/Diffusion/TetrahedronDiffusionFEMForceField.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.00001" gravity="0 0 0" >
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [LinearMovementProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Diffusion"/> <!-- Needed to use components [TetrahedronDiffusionFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader MeshVTKLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [MeshMatrixMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Engine"/> <!-- Needed to use components [TextureInterpolation] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <VisualStyle displayFlags="showBehaviorModels"/>
    
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
            <TetrahedronDiffusionFEMForceField template="Vec1" name="DiffusionForceField" topology="@../topo" constantDiffusionCoefficient="1500" printLog="0" drawConduc="0" tagMechanics="mechanics" tags="heat"/>
            <MeshMatrixMass name="Mass" template="Vec1,Vec3" lumping="0" massDensity="1.0" printLog="0" tags="heat" topology="@../topo" geometryState="@../raptorDOFs"/>
    
            <LinearMovementProjectiveConstraint template="Vec1" keyTimes="0 0.005 0.006" movements="0 0 1" indices="@../box-cold.indices" />
            <LinearMovementProjectiveConstraint template="Vec1" keyTimes="0.001 0.002 0.004 0.005 0.006" movements="0 1 0.5 1 0" indices="@../box-hot.indices" />
    
            <Node name="Visu">
                <TextureInterpolation template="Vec1" name="EngineInterpolation"  input_states="@../gridTemperature.position"  input_coordinates="@../../raptorDOFs.position"  min_value="0.0"  max_value="1.0"  manual_scale="1"  drawPotentiels="0"  showIndicesScale="5e-05" />
                <OglModel template="Vec3" name="oglPotentiel" texcoords="@EngineInterpolation.output_coordinates" handleDynamicTopology="0" texturename="textures/heatColor.bmp" scale3d="1 1 1"  material="Default Diffuse 1 1 1 1 0.5 Ambient 1 1 1 1 0.3 Specular 0 0.5 0.5 0.5 1 Emissive 0 0.5 0.5 0.5 1 Shininess 0 45 No texture linked to the material No bump texture linked to the material "/>
                <IdentityMapping input="@../../raptorDOFs" output="@oglPotentiel" />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.00001", gravity="0 0 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Diffusion")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Engine")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels")
        root.addObject('MeshVTKLoader', name="meshLoader", filename="mesh/raptorTetra_8418.vtu")
        root.addObject('MeshOBJLoader', name="potentialLoader", filename="mesh/raptorTemperature.obj")
        root.addObject('TetrahedronSetTopologyContainer', name="topo", src="@meshLoader", tags="mechanics")
        root.addObject('MechanicalObject', template="Vec3", name="raptorDOFs", src="@meshLoader", tags="mechanics")
        root.addObject('TetrahedronSetTopologyModifier', name="Modifier", tags="mechanics")
        root.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo", tags="mechanics")
        root.addObject('BoxROI', name="box-hot", box="-3 4 4 3 8 8", drawBoxes="1", position="@raptorDOFs.position")
        root.addObject('BoxROI', name="box-cold", box="-3 4 -4 3 8 -10", drawBoxes="1", position="@raptorDOFs.position")
        root.addObject('DefaultAnimationLoop')

        Temperature = root.addChild('Temperature', gravity="0 0 0")
        Temperature.addObject('EulerImplicitSolver', name="EulerExplicitSolver", firstOrder="1", tags="heat", rayleighStiffness="0.1", rayleighMass="0.1")
        Temperature.addObject('CGLinearSolver', name="CG", iterations="1000", tolerance="1.0e-10", threshold="1.0e-30", tags="heat")
        Temperature.addObject('MechanicalObject', template="Vec1", position="@../potentialLoader.position", name="gridTemperature", bbox="0 0 0 0 0 0", tags="heat")
        Temperature.addObject('TetrahedronDiffusionFEMForceField', template="Vec1", name="DiffusionForceField", topology="@../topo", constantDiffusionCoefficient="1500", printLog="0", drawConduc="0", tagMechanics="mechanics", tags="heat")
        Temperature.addObject('MeshMatrixMass', name="Mass", template="Vec1,Vec3", lumping="0", massDensity="1.0", printLog="0", tags="heat", topology="@../topo", geometryState="@../raptorDOFs")
        Temperature.addObject('LinearMovementProjectiveConstraint', template="Vec1", keyTimes="0 0.005 0.006", movements="0 0 1", indices="@../box-cold.indices")
        Temperature.addObject('LinearMovementProjectiveConstraint', template="Vec1", keyTimes="0.001 0.002 0.004 0.005 0.006", movements="0 1 0.5 1 0", indices="@../box-hot.indices")

        Visu = Temperature.addChild('Visu')
        Visu.addObject('TextureInterpolation', template="Vec1", name="EngineInterpolation", input_states="@../gridTemperature.position", input_coordinates="@../../raptorDOFs.position", min_value="0.0", max_value="1.0", manual_scale="1", drawPotentiels="0", showIndicesScale="5e-05")
        Visu.addObject('OglModel', template="Vec3", name="oglPotentiel", texcoords="@EngineInterpolation.output_coordinates", handleDynamicTopology="0", texturename="textures/heatColor.bmp", scale3d="1 1 1", material="Default Diffuse 1 1 1 1 0.5 Ambient 1 1 1 1 0.3 Specular 0 0.5 0.5 0.5 1 Emissive 0 0.5 0.5 0.5 1 Shininess 0 45 No texture linked to the material No bump texture linked to the material ")
        Visu.addObject('IdentityMapping', input="@../../raptorDOFs", output="@oglPotentiel")
    ```

