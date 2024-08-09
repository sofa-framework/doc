<!-- generate_doc -->
# QuadularBendingSprings

Springs added to a quad mesh to prevent bending


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.SolidMechanics.Spring

__namespace__: sofa::component::solidmechanics::spring

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
		<td>stiffness</td>
		<td>
uniform stiffness for the all springs
		</td>
		<td>100000</td>
	</tr>
	<tr>
		<td>damping</td>
		<td>
uniform damping for the all springs
		</td>
		<td>1</td>
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
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|
|topology|link to the topology container|BaseMeshTopology|

## Examples 

QuadularBendingSprings.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.005" showBoundingTree="0" gravity="0 -9.81 0">
        <Node name="plugins">
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [EigenSimplicialLDLT] -->
            <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangularFEMForceField] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [QuadularBendingSprings] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [QuadSetTopologyContainer TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
            <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Quad2TriangleTopologicalMapping] -->
            <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
            <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        </Node>
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showWireframe" />
        <Node name="QuadularSprings">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <EigenSimplicialLDLT name="linearSolver" template="CompressedRowSparseMatrixMat3x3"/>
            <RegularGridTopology min="0 0 0" max="1 0 1" nx="20" ny="1" nz="20" name="grid" />
            <MechanicalObject name="Quads" />
            <QuadSetTopologyContainer name="Container" quads="@grid.quads"/>
            <QuadularBendingSprings name="FEM-Bend" stiffness="3000" damping="1.0" topology="@Container" draw="true"/>
            <DiagonalMass massDensity="1.5" />
            <BoxROI box="-0.0001 -0.0001 -0.0001 0.0001 0.0001 0.0001  0.999 -0.0001 -0.0001 1.0001 0.0001 0.0001" name="box"/>
            <FixedProjectiveConstraint indices="@box.indices" />
            <Node name="Surf">
                <TriangleSetTopologyContainer name="Container"/>
                <TriangleSetTopologyModifier name="Modifier" />
                <Quad2TriangleTopologicalMapping input="@../Container" output="@Container" />
                <TriangularFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.3" method="large" />
            </Node>
            <Node name="Visu">
                <OglModel name="Visual" color="yellow" />
                <IdentityMapping input="@../Quads" output="@Visual" />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.005", showBoundingTree="0", gravity="0 -9.81 0")

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       plugins.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")

       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showWireframe")

       quadular_springs = root.addChild('QuadularSprings')

       quadular_springs.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       quadular_springs.addObject('EigenSimplicialLDLT', name="linearSolver", template="CompressedRowSparseMatrixMat3x3")
       quadular_springs.addObject('RegularGridTopology', min="0 0 0", max="1 0 1", nx="20", ny="1", nz="20", name="grid")
       quadular_springs.addObject('MechanicalObject', name="Quads")
       quadular_springs.addObject('QuadSetTopologyContainer', name="Container", quads="@grid.quads")
       quadular_springs.addObject('QuadularBendingSprings', name="FEM-Bend", stiffness="3000", damping="1.0", topology="@Container", draw="true")
       quadular_springs.addObject('DiagonalMass', massDensity="1.5")
       quadular_springs.addObject('BoxROI', box="-0.0001 -0.0001 -0.0001 0.0001 0.0001 0.0001  0.999 -0.0001 -0.0001 1.0001 0.0001 0.0001", name="box")
       quadular_springs.addObject('FixedProjectiveConstraint', indices="@box.indices")

       surf = QuadularSprings.addChild('Surf')

       surf.addObject('TriangleSetTopologyContainer', name="Container")
       surf.addObject('TriangleSetTopologyModifier', name="Modifier")
       surf.addObject('Quad2TriangleTopologicalMapping', input="@../Container", output="@Container")
       surf.addObject('TriangularFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.3", method="large")

       visu = QuadularSprings.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="yellow")
       visu.addObject('IdentityMapping', input="@../Quads", output="@Visual")
    ```
