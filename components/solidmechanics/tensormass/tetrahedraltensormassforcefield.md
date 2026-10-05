<!-- generate_doc -->
# TetrahedralTensorMassForceField

Linear Elastic Tetrahedral Mesh


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.SolidMechanics.TensorMass

__namespace__: sofa::component::solidmechanics::tensormass

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
		<td>poissonRatio</td>
		<td>
Poisson ratio in Hooke's law
		</td>
		<td>0.3</td>
	</tr>
	<tr>
		<td>youngModulus</td>
		<td>
Young's modulus in Hooke's law
		</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>edgeInfo</td>
		<td>
Internal edge data
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|
|topology|link to the topology container|BaseMeshTopology|

## Examples 

TetrahedralTensorMassForceField.scn

=== "XML"

    ```xml
    <Node name="root">
        <Node name="plugins">
            <RequiredPlugin pluginName="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin pluginName="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
            <RequiredPlugin pluginName="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [EigenSimplicialLDLT] -->
            <RequiredPlugin pluginName="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
            <RequiredPlugin pluginName="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
            <RequiredPlugin pluginName="Sofa.Component.IntegrationScheme.Backward"/> <!-- Needed to use components [EulerImplicitIntegrationScheme] -->
            <RequiredPlugin pluginName="Sofa.Component.SolidMechanics.TensorMass"/> <!-- Needed to use components [TetrahedralTensorMassForceField] -->
            <RequiredPlugin pluginName="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [QuadSetGeometryAlgorithms QuadSetTopologyContainer QuadSetTopologyModifier TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier] -->
            <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
            <RequiredPlugin pluginName="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2QuadTopologicalMapping Hexa2TetraTopologicalMapping] -->
            <RequiredPlugin pluginName="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
            <RequiredPlugin pluginName="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        </Node>
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
    
        <DefaultAnimationLoop name="animationLoop"/>
        <DefaultVisualManagerLoop name="visualLoop"/>
    
        <EulerImplicitIntegrationScheme name="odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
        <EigenSimplicialLDLT template="CompressedRowSparseMatrixMat3x3"/>
        <MechanicalObject name="DoFs" />
        <UniformMass name="mass" totalMass="320" />
        <RegularGridTopology name="grid" nx="4" ny="4" nz="20" xmin="-9" xmax="-6" ymin="0" ymax="3" zmin="0" zmax="19" />
        <BoxROI name="box" box="-10 -1 -0.0001  -5 4 0.0001"/>
        <FixedProjectiveConstraint indices="@box.indices" />
    
        <TetrahedronSetTopologyContainer name="Tetra_topo"/>
        <TetrahedronSetTopologyModifier name="Modifier" />
        <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
        <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" swapping="true"/>
        <TetrahedralTensorMassForceField name="deformable" youngModulus="100000" poissonRatio="0.4" />
    
        <Node name="quads">
            <QuadSetTopologyContainer  name="Container" />
            <QuadSetTopologyModifier   name="Modifier" />
            <QuadSetGeometryAlgorithms name="GeomAlgo" template="Vec3" />
            <Hexa2QuadTopologicalMapping input="@../grid" output="@Container" />
            <Node name="Visu">
                <OglModel name="Visual" color="yellow" />
                <IdentityMapping input="@../../DoFs" output="@Visual" />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root')

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Constraint.Projective")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Engine.Select")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSolver.Direct")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Mapping.Linear")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Mass")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.IntegrationScheme.Backward")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.SolidMechanics.TensorMass")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Dynamic")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Grid")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Mapping")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Visual")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.GL.Component.Rendering3D")

       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
       root.addObject('DefaultAnimationLoop', name="animationLoop")
       root.addObject('DefaultVisualManagerLoop', name="visualLoop")
       root.addObject('EulerImplicitIntegrationScheme', name="odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
       root.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrixMat3x3")
       root.addObject('MechanicalObject', name="DoFs")
       root.addObject('UniformMass', name="mass", totalMass="320")
       root.addObject('RegularGridTopology', name="grid", nx="4", ny="4", nz="20", xmin="-9", xmax="-6", ymin="0", ymax="3", zmin="0", zmax="19")
       root.addObject('BoxROI', name="box", box="-10 -1 -0.0001  -5 4 0.0001")
       root.addObject('FixedProjectiveConstraint', indices="@box.indices")
       root.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
       root.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       root.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       root.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo", swapping="true")
       root.addObject('TetrahedralTensorMassForceField', name="deformable", youngModulus="100000", poissonRatio="0.4")

       quads = root.addChild('quads')

       quads.addObject('QuadSetTopologyContainer', name="Container")
       quads.addObject('QuadSetTopologyModifier', name="Modifier")
       quads.addObject('QuadSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
       quads.addObject('Hexa2QuadTopologicalMapping', input="@../grid", output="@Container")

       visu = quads.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="yellow")
       visu.addObject('IdentityMapping', input="@../../DoFs", output="@Visual")
    ```

