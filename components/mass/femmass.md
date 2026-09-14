<!-- generate_doc -->
# FEMMass

Finite-element mass (inertia and body force)


Templates:

- Vec1d,Edge
- Vec1d,QuadraticEdge

__Target__: Sofa.Component.Mass

__namespace__: sofa::component::mass

__parents__:

- Mass
- TopologyAccessor

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
		<td>separateGravity</td>
		<td>
add separately gravity to velocity computation
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>rayleighMass</td>
		<td>
Rayleigh damping - mass matrix coefficient
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>lumping</td>
		<td>
If true, the mass matrix is lumped, meaning the mass matrix is approximated to a diagonal matrix (summing all mass values of a line on the diagonal)
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec1d&gt;|
|topology|Link to a topology|BaseMeshTopology|
|nodalMassDensity|Link to nodal mass density|NodalMassDensity&lt;d&gt;|

<!-- generate_doc -->
## Vec2d,Edge...

Templates:

- Vec2d,Edge
- Vec2d,Quad
- Vec2d,QuadraticEdge
- Vec2d,QuadraticQuad
- Vec2d,QuadraticTriangle
- Vec2d,Triangle

__Target__: Sofa.Component.Mass

__namespace__: sofa::component::mass

__parents__:

- Mass
- TopologyAccessor

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
		<td>separateGravity</td>
		<td>
add separately gravity to velocity computation
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>rayleighMass</td>
		<td>
Rayleigh damping - mass matrix coefficient
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>lumping</td>
		<td>
If true, the mass matrix is lumped, meaning the mass matrix is approximated to a diagonal matrix (summing all mass values of a line on the diagonal)
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec2d&gt;|
|topology|Link to a topology|BaseMeshTopology|
|nodalMassDensity|Link to nodal mass density|NodalMassDensity&lt;d&gt;|

<!-- generate_doc -->
## Vec3d,Edge...

Templates:

- Vec3d,Edge
- Vec3d,Hexahedron
- Vec3d,Prism
- Vec3d,Pyramid
- Vec3d,Quad
- Vec3d,QuadraticEdge
- Vec3d,QuadraticHexahedron
- Vec3d,QuadraticQuad
- Vec3d,QuadraticTetrahedron
- Vec3d,QuadraticTriangle
- Vec3d,Tetrahedron
- Vec3d,Triangle

__Target__: Sofa.Component.Mass

__namespace__: sofa::component::mass

__parents__:

- Mass
- TopologyAccessor

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
		<td>separateGravity</td>
		<td>
add separately gravity to velocity computation
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>rayleighMass</td>
		<td>
Rayleigh damping - mass matrix coefficient
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>lumping</td>
		<td>
If true, the mass matrix is lumped, meaning the mass matrix is approximated to a diagonal matrix (summing all mass values of a line on the diagonal)
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
|topology|Link to a topology|BaseMeshTopology|
|nodalMassDensity|Link to nodal mass density|NodalMassDensity&lt;d&gt;|

## Examples 

FEMMass_lumping.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 -9.81 0">
    
        <Node name="plugins">
            <RequiredPlugin pluginName="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin pluginName="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
            <RequiredPlugin pluginName="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [SparseLDLSolver] -->
            <RequiredPlugin pluginName="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
            <RequiredPlugin pluginName="Sofa.Component.LinearSolver.Ordering"/> <!-- Needed to use components [NaturalOrderingMethod] -->
            <RequiredPlugin pluginName="Sofa.Component.LinearSystem"/> <!-- Needed to use components [ConstantSparsityPatternSystem] -->
            <RequiredPlugin pluginName="Sofa.Component.Mass"/> <!-- Needed to use components [MeshMatrixMass] -->
            <RequiredPlugin pluginName="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin pluginName="Sofa.Component.SolidMechanics.FEM.Elastic"/>
            <RequiredPlugin pluginName="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms,TetrahedronSetTopologyContainer,TetrahedronSetTopologyModifier] -->
            <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
            <RequiredPlugin pluginName="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping] -->
            <RequiredPlugin pluginName="Sofa.Component.Visual"/> <!-- Needed to use components [LineAxis,VisualGrid,VisualStyle] -->
            <RequiredPlugin pluginName="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglSceneFrame] -->
        </Node>
    
        <DefaultAnimationLoop parallelODESolving="true"/>
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
    
        <VisualGrid size="0.1"/>
        <LineAxis size="0.1"/>
        <OglSceneFrame/>
    
        <Node name="consistent">
            <Visual3DText text="consistent mass" position="-0.09 0.03 0" scale="0.01" color="teal"/>
            <EulerImplicitSolver name="backward_Euler" rayleighStiffness="0.1" rayleighMass="0.1" />
    
            <ConstantSparsityPatternSystem template="CompressedRowSparseMatrix" name="A" checkIndices="false"/>
            <NaturalOrderingMethod/>
            <SparseLDLSolver name="linear_solver" template="CompressedRowSparseMatrix"/>
    
            <RegularGridTopology name="grid" min="-0.03 -0.01 0" max="-0.01 0.01 0.2" n="5 5 30"/>
            <MechanicalObject template="Vec3" name="state" showObject="true"/>
    
            <NodalMassDensity property="1100"/>
            <FEMMass template="Vec3,Hexahedron" lumping="false"/>
    
            <CorotationalFEMForceField name="FEM" template="Vec3,Hexahedron"
                                       youngModulus="1e5" poissonRatio="0.45" topology="@grid"
                                       computeForceStrategy="sequenced" computeForceDerivStrategy="sequenced"/>
    
            <BoxROI template="Vec3" name="box_roi" box="-0.031 -0.011 -0.0001   -0.009 0.011 0.0001" drawBoxes="1" />
            <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
        </Node>
    
        <Node name="lumped">
            <Visual3DText text="lumped mass" position="0.01 0.03 0" scale="0.01" color="orange"/>
            <EulerImplicitSolver name="backward_Euler" rayleighStiffness="0.1" rayleighMass="0.1" />
    
            <ConstantSparsityPatternSystem template="CompressedRowSparseMatrix" name="A" checkIndices="false"/>
            <NaturalOrderingMethod/>
            <SparseLDLSolver name="linear_solver" template="CompressedRowSparseMatrix"/>
    
            <RegularGridTopology name="grid" min="0.01 -0.01 0" max="0.03 0.01 0.2" n="5 5 30"/>
            <MechanicalObject template="Vec3" name="state" showObject="true"/>
    
            <NodalMassDensity property="1100"/>
            <FEMMass template="Vec3,Hexahedron" lumping="true"/>
    
            <CorotationalFEMForceField name="FEM" template="Vec3,Hexahedron"
                                       youngModulus="1e5" poissonRatio="0.45" topology="@grid"
                                       computeForceStrategy="sequenced" computeForceDerivStrategy="sequenced"/>
    
            <BoxROI template="Vec3" name="box_roi" box="0.009 -0.011 -0.0001   0.031 0.011 0.0001" drawBoxes="1" />
            <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 -9.81 0")

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Constraint.Projective")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Engine.Select")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSolver.Direct")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSolver.Iterative")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSolver.Ordering")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSystem")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Mass")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.ODESolver.Backward")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.SolidMechanics.FEM.Elastic")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Dynamic")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Grid")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Mapping")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Visual")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.GL.Component.Rendering3D")

       root.addObject('DefaultAnimationLoop', parallelODESolving="true")
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
       root.addObject('VisualGrid', size="0.1")
       root.addObject('LineAxis', size="0.1")
       root.addObject('OglSceneFrame', )

       consistent = root.addChild('consistent')

       consistent.addObject('Visual3DText', text="consistent mass", position="-0.09 0.03 0", scale="0.01", color="teal")
       consistent.addObject('EulerImplicitSolver', name="backward_Euler", rayleighStiffness="0.1", rayleighMass="0.1")
       consistent.addObject('ConstantSparsityPatternSystem', template="CompressedRowSparseMatrix", name="A", checkIndices="false")
       consistent.addObject('NaturalOrderingMethod', )
       consistent.addObject('SparseLDLSolver', name="linear_solver", template="CompressedRowSparseMatrix")
       consistent.addObject('RegularGridTopology', name="grid", min="-0.03 -0.01 0", max="-0.01 0.01 0.2", n="5 5 30")
       consistent.addObject('MechanicalObject', template="Vec3", name="state", showObject="true")
       consistent.addObject('NodalMassDensity', property="1100")
       consistent.addObject('FEMMass', template="Vec3,Hexahedron", lumping="false")
       consistent.addObject('CorotationalFEMForceField', name="FEM", template="Vec3,Hexahedron", youngModulus="1e5", poissonRatio="0.45", topology="@grid", computeForceStrategy="sequenced", computeForceDerivStrategy="sequenced")
       consistent.addObject('BoxROI', template="Vec3", name="box_roi", box="-0.031 -0.011 -0.0001   -0.009 0.011 0.0001", drawBoxes="1")
       consistent.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")

       lumped = root.addChild('lumped')

       lumped.addObject('Visual3DText', text="lumped mass", position="0.01 0.03 0", scale="0.01", color="orange")
       lumped.addObject('EulerImplicitSolver', name="backward_Euler", rayleighStiffness="0.1", rayleighMass="0.1")
       lumped.addObject('ConstantSparsityPatternSystem', template="CompressedRowSparseMatrix", name="A", checkIndices="false")
       lumped.addObject('NaturalOrderingMethod', )
       lumped.addObject('SparseLDLSolver', name="linear_solver", template="CompressedRowSparseMatrix")
       lumped.addObject('RegularGridTopology', name="grid", min="0.01 -0.01 0", max="0.03 0.01 0.2", n="5 5 30")
       lumped.addObject('MechanicalObject', template="Vec3", name="state", showObject="true")
       lumped.addObject('NodalMassDensity', property="1100")
       lumped.addObject('FEMMass', template="Vec3,Hexahedron", lumping="true")
       lumped.addObject('CorotationalFEMForceField', name="FEM", template="Vec3,Hexahedron", youngModulus="1e5", poissonRatio="0.45", topology="@grid", computeForceStrategy="sequenced", computeForceDerivStrategy="sequenced")
       lumped.addObject('BoxROI', template="Vec3", name="box_roi", box="0.009 -0.011 -0.0001   0.031 0.011 0.0001", drawBoxes="1")
       lumped.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")
    ```

