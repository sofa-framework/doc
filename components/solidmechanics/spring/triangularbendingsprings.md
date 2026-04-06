<!-- generate_doc -->
# TriangularBendingSprings

Springs added to a triangular mesh to prevent bending


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
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showSprings</td>
		<td>
option to draw springs
		</td>
		<td>1</td>
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

TriangularBendingSprings_RemovingMeshTest.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <!-- Automatic Triangle removal on a simple Triangle topology with FEM: Element removed are define in: ./RemovingTrianglesProcess.txt -->
    <Node name="root" gravity="0 -9 0" dt="0.01" bbox="-1 -1 -1 1 1 1">
        <RequiredPlugin pluginName="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin pluginName="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin pluginName="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin pluginName="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin pluginName="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin pluginName="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin pluginName="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin pluginName="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [TriangularBendingSprings] -->
        <RequiredPlugin pluginName="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin pluginName="Sofa.Component.Topology.Utility"/> <!-- Needed to use components [TopologicalChangeProcessor] -->
        <RequiredPlugin pluginName="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        
        <VisualStyle displayFlags="showVisual showBehaviorModels showForceFields" />
        <DefaultAnimationLoop/>
        <CollisionPipeline verbose="0" />
        <BruteForceBroadPhase name="N2" />
        <BVHNarrowPhase />
        <CollisionResponse response="PenalityContactForceField" />
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
        <Node name="SquareGravity">
            <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" tolerance="1e-5" threshold="1e-5" name="linear solver"/>
            <MeshGmshLoader name="loader" filename="mesh/square3.msh" createSubelements="true" />
            <MechanicalObject name="dofs" src="@loader" template="Vec3" />
            <TriangleSetTopologyContainer name="Triangle_topo" src="@loader"/>
            <TriangleSetTopologyModifier name="Modifier" />
            <TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <DiagonalMass template="Vec3,Vec3" name="mass" massDensity="1.0" />
            
            <TriangularBendingSprings template="Vec3" name="FEM-Bend" stiffness="300" damping="1" />
           
            <TopologicalChangeProcessor listening="1" filename="RemovingTrianglesProcess_constraint.txt" />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9 0", dt="0.01", bbox="-1 -1 -1 1 1 1")

       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Utility")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Visual")
       root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels showForceFields")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('CollisionPipeline', verbose="0")
       root.addObject('BruteForceBroadPhase', name="N2")
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', response="PenalityContactForceField")
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")

       square_gravity = root.addChild('SquareGravity')

       square_gravity.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
       square_gravity.addObject('CGLinearSolver', iterations="25", tolerance="1e-5", threshold="1e-5", name="linear solver")
       square_gravity.addObject('MeshGmshLoader', name="loader", filename="mesh/square3.msh", createSubelements="true")
       square_gravity.addObject('MechanicalObject', name="dofs", src="@loader", template="Vec3")
       square_gravity.addObject('TriangleSetTopologyContainer', name="Triangle_topo", src="@loader")
       square_gravity.addObject('TriangleSetTopologyModifier', name="Modifier")
       square_gravity.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       square_gravity.addObject('DiagonalMass', template="Vec3,Vec3", name="mass", massDensity="1.0")
       square_gravity.addObject('TriangularBendingSprings', template="Vec3", name="FEM-Bend", stiffness="300", damping="1")
       square_gravity.addObject('TopologicalChangeProcessor', listening="1", filename="RemovingTrianglesProcess_constraint.txt")
    ```

TriangularBendingSprings.scn

=== "XML"

    ```xml
    <!-- Mechanical MassSpring Group Basic Example -->
    <Node name="root" dt="0.005" showBoundingTree="0" gravity="0 -90 10">
        <Node name="plugins">
            <RequiredPlugin pluginName="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin pluginName="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
            <RequiredPlugin pluginName="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [AsyncSparseLDLSolver] -->
            <RequiredPlugin pluginName="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [PCGLinearSolver] -->
            <RequiredPlugin pluginName="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
            <RequiredPlugin pluginName="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
            <RequiredPlugin pluginName="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin pluginName="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangularFEMForceField] -->
            <RequiredPlugin pluginName="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [TriangularBendingSprings] -->
            <RequiredPlugin pluginName="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetTopologyContainer] -->
            <RequiredPlugin pluginName="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
            <RequiredPlugin pluginName="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        </Node>
        <VisualStyle displayFlags="showBehaviorModels" />
        <DefaultAnimationLoop/>
    
        <Node name="SquareGravity">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <PCGLinearSolver preconditioner="@preconditioner"/>
            <AsyncSparseLDLSolver name="preconditioner" template="CompressedRowSparseMatrixMat3x3"/>
            <MeshGmshLoader name="loader" filename="mesh/square3.msh" createSubelements="true"/>
            <MechanicalObject src="@loader" scale="10" />
            <TriangleSetTopologyContainer name="Container" triangles="@loader.triangles"/>
            <DiagonalMass massDensity="0.015" />
            <FixedProjectiveConstraint indices="0 1" />
            <TriangularFEMForceField name="FEM" youngModulus="60" poissonRatio="0.3" method="large" />
            <TriangularBendingSprings name="BS" stiffness="300" damping="1.0" />
            <Node >
                <OglModel name="Visual" color="yellow" />
                <IdentityMapping input="@.." output="@Visual" />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.005", showBoundingTree="0", gravity="0 -90 10")

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Constraint.Projective")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.IO.Mesh")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSolver.Direct")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSolver.Iterative")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Mapping.Linear")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Mass")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.ODESolver.Backward")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.SolidMechanics.FEM.Elastic")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.SolidMechanics.Spring")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Dynamic")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Visual")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.GL.Component.Rendering3D")

       root.addObject('VisualStyle', displayFlags="showBehaviorModels")
       root.addObject('DefaultAnimationLoop', )

       square_gravity = root.addChild('SquareGravity')

       square_gravity.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       square_gravity.addObject('PCGLinearSolver', preconditioner="@preconditioner")
       square_gravity.addObject('AsyncSparseLDLSolver', name="preconditioner", template="CompressedRowSparseMatrixMat3x3")
       square_gravity.addObject('MeshGmshLoader', name="loader", filename="mesh/square3.msh", createSubelements="true")
       square_gravity.addObject('MechanicalObject', src="@loader", scale="10")
       square_gravity.addObject('TriangleSetTopologyContainer', name="Container", triangles="@loader.triangles")
       square_gravity.addObject('DiagonalMass', massDensity="0.015")
       square_gravity.addObject('FixedProjectiveConstraint', indices="0 1")
       square_gravity.addObject('TriangularFEMForceField', name="FEM", youngModulus="60", poissonRatio="0.3", method="large")
       square_gravity.addObject('TriangularBendingSprings', name="BS", stiffness="300", damping="1.0")

       node = SquareGravity.addChild('node')

       node.addObject('OglModel', name="Visual", color="yellow")
       node.addObject('IdentityMapping', input="@..", output="@Visual")
    ```

