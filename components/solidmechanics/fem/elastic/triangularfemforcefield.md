<!-- generate_doc -->
# TriangularFEMForceField

Corotational Triangular finite elements for dynamic topology.


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.SolidMechanics.FEM.Elastic

__namespace__: sofa::component::solidmechanics::fem::elastic

__parents__:

- BaseLinearElasticityFEMForceField

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
FEM Poisson Ratio in Hooke's law [0,0.5[
		</td>
		<td>0.45</td>
	</tr>
	<tr>
		<td>youngModulus</td>
		<td>
FEM Young's Modulus in Hooke's law
		</td>
		<td>5000</td>
	</tr>
	<tr>
		<td>triangleInfo</td>
		<td>
Internal triangle data
		</td>
		<td></td>
	</tr>
	<tr>
		<td>vertexInfo</td>
		<td>
Internal point data
		</td>
		<td></td>
	</tr>
	<tr>
		<td>method</td>
		<td>
large: large displacements, small: small displacements
		</td>
		<td>large</td>
	</tr>
	<tr>
		<td>rotatedInitialElements</td>
		<td>
Flag activating rendering of stress directions within each triangle
		</td>
		<td></td>
	</tr>
	<tr>
		<td>initialTransformation</td>
		<td>
Flag activating rendering of stress directions within each triangle
		</td>
		<td></td>
	</tr>
	<tr>
		<td>hosfordExponant</td>
		<td>
Exponent in the Hosford yield criteria
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>criteriaValue</td>
		<td>
Fracturable threshold used to draw fracturable triangles
		</td>
		<td>1e+15</td>
	</tr>
	<tr>
		<td>computePrincipalStress</td>
		<td>
Compute principal stress for each triangle
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showStressValue</td>
		<td>
Flag activating rendering of stress values as a color in each triangle
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>showStressVector</td>
		<td>
Flag activating rendering of stress directions within each triangle
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showFracturableTriangles</td>
		<td>
Flag activating rendering of triangles to fracture
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
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|
|topology|link to the topology container|BaseMeshTopology|

## Examples 

TriangularFEMForceField_RemovingMeshTest.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <!-- Automatic Triangle removal on a simple Triangle topology with FEM: Element removed are define in: ./RemovingTrianglesProcess.txt -->
    <Node name="root" gravity="0 -9 0" dt="0.01"  bbox="-1 -1 -1 1 1 1">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangularFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Utility"/> <!-- Needed to use components [TopologicalChangeProcessor] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        
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
            
            <TriangularFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.3" youngModulus="60" />
           
            <TopologicalChangeProcessor listening="1" filename="RemovingTrianglesProcess_constraint.txt" />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9 0", dt="0.01", bbox="-1 -1 -1 1 1 1")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Utility")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
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
       square_gravity.addObject('TriangularFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.3", youngModulus="60")
       square_gravity.addObject('TopologicalChangeProcessor', listening="1", filename="RemovingTrianglesProcess_constraint.txt")
    ```

TriangularFEMForceFieldOptim.scn

=== "XML"

    ```xml
    <!-- Mechanical TriangularFEMForceFieldOptim Example -->
    <Node name="root" dt="0.05" gravity="0 10 10" showBoundingTree="0">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangularFEMForceFieldOptim] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        
        <VisualStyle displayFlags="showVisual showBehaviorModels showForceFields showWireframe" />
        <DefaultAnimationLoop/>
        <!-- Activate this loader to use a square mesh with only two triangles (useful to debug base equations) -->
        <!--<MeshGmshLoader name="loaderSquare" triangles="0 1 3  1 2 3" position="0 0 0  1 0 0  1 1 0  0 1 0" />-->
        <!-- Activate this loader to load a square mesh with many triangles -->
        <MeshGmshLoader filename="mesh/square3.msh" name="loaderSquare" />
        <Node name="SquareGravity1">
            <EulerImplicitSolver name="odesolver1" printLog="0"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver printLog="0" iterations="25" name="linearsolver1" tolerance="1.0e-9" threshold="1.0e-9" />
            <TriangleSetTopologyContainer name="Container" src="@../loaderSquare" />
            <MechanicalObject name="DOFs" src="@../loaderSquare" scale="100"  />
            <TriangleSetTopologyModifier name="Modifier" />
            <TriangleSetGeometryAlgorithms name="GeomAlgo" template="Vec3" />
            <DiagonalMass massDensity="0.005" />
            <FixedProjectiveConstraint indices="0 1 2" />
            <TriangularFEMForceFieldOptim name="FEM" youngModulus="600" poissonRatio="0.3" method="large" printLog="1"/>
            <Node name="VisuA">
                <OglModel name="Visual" color="yellow" />
                <IdentityMapping name="visualMapping" input="@../DOFs" output="@Visual" />
            </Node>
        </Node>
        <!-- Activate this version to compare computed stiffness matrix (addKToMatrix) with addDForce -->
        <!--<Node name="SquareGravityTestMatrixConstruction">
            <EulerImplicitSolver name="odesolver2" printLog="0" />
            <CGLinearSolver template="SparseMatrix" verbose="0" printLog="1" iterations="25" name="linearsolver2" tolerance="1.0e-9" threshold="1.0e-9" />
            <TriangleSetTopologyContainer name="Container" src="@../loaderSquare" />
            <MechanicalObject name="DOFs" src="@../loaderSquare" scale="100"  />
            <TriangleSetTopologyModifier name="Modifier" />
            <TriangleSetGeometryAlgorithms name="GeomAlgo" template="Vec3" />
            <DiagonalMass massDensity="0.005" />
            <FixedProjectiveConstraint indices="0 1 2" />
            <TriangularFEMForceFieldOptim name="FEM" youngModulus="600" poissonRatio="0.3" method="large" printLog="1"/>
            <Node name="VisuA">
                <OglModel name="Visual" color="yellow" />
                <IdentityMapping name="visualMapping" input="@../DOFs" output="@Visual" />
            </Node>
        </Node>-->
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.05", gravity="0 10 10", showBoundingTree="0")

       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels showForceFields showWireframe")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('MeshGmshLoader', filename="mesh/square3.msh", name="loaderSquare")

       square_gravity1 = root.addChild('SquareGravity1')

       square_gravity1.addObject('EulerImplicitSolver', name="odesolver1", printLog="0", rayleighStiffness="0.1", rayleighMass="0.1")
       square_gravity1.addObject('CGLinearSolver', printLog="0", iterations="25", name="linearsolver1", tolerance="1.0e-9", threshold="1.0e-9")
       square_gravity1.addObject('TriangleSetTopologyContainer', name="Container", src="@../loaderSquare")
       square_gravity1.addObject('MechanicalObject', name="DOFs", src="@../loaderSquare", scale="100")
       square_gravity1.addObject('TriangleSetTopologyModifier', name="Modifier")
       square_gravity1.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
       square_gravity1.addObject('DiagonalMass', massDensity="0.005")
       square_gravity1.addObject('FixedProjectiveConstraint', indices="0 1 2")
       square_gravity1.addObject('TriangularFEMForceFieldOptim', name="FEM", youngModulus="600", poissonRatio="0.3", method="large", printLog="1")

       visu_a = SquareGravity1.addChild('VisuA')

       visu_a.addObject('OglModel', name="Visual", color="yellow")
       visu_a.addObject('IdentityMapping', name="visualMapping", input="@../DOFs", output="@Visual")
    ```

TriangularFEMForceField.scn

=== "XML"

    ```xml
    <!-- Mechanical TriangularFEMForceField Example -->
    <Node name="root" dt="0.05" gravity="0 -9.8 10" showBoundingTree="0">
    
        <Node name="plugins">
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
            <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangularFEMForceField] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
            <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
            <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        </Node>
    
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
        <DefaultAnimationLoop/>
        
        <Node name="SquareGravity">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshGmshLoader filename="mesh/square3.msh" name="loader" />
            <MechanicalObject src="@loader" name="DOFs" scale3d="100 100 0" />
            <TriangleSetTopologyContainer src="@loader" name="Container" />
            <TriangleSetTopologyModifier name="Modifier" />
            <TriangleSetGeometryAlgorithms name="GeomAlgo" template="Vec3" />
            <DiagonalMass massDensity="0.005" />
            <FixedProjectiveConstraint indices="0 1 2" />
            <TriangularFEMForceField name="FEM" youngModulus="600" poissonRatio="0.3" method="large" />
            <Node name="VisuA">
                <OglModel name="Visual" color="yellow" />
                <IdentityMapping template="Vec3,Vec3" name="visualMapping" input="@../DOFs" output="@Visual" />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.05", gravity="0 -9.8 10", showBoundingTree="0")

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       plugins.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")

       root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
       root.addObject('DefaultAnimationLoop', )

       square_gravity = root.addChild('SquareGravity')

       square_gravity.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       square_gravity.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       square_gravity.addObject('MeshGmshLoader', filename="mesh/square3.msh", name="loader")
       square_gravity.addObject('MechanicalObject', src="@loader", name="DOFs", scale3d="100 100 0")
       square_gravity.addObject('TriangleSetTopologyContainer', src="@loader", name="Container")
       square_gravity.addObject('TriangleSetTopologyModifier', name="Modifier")
       square_gravity.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
       square_gravity.addObject('DiagonalMass', massDensity="0.005")
       square_gravity.addObject('FixedProjectiveConstraint', indices="0 1 2")
       square_gravity.addObject('TriangularFEMForceField', name="FEM", youngModulus="600", poissonRatio="0.3", method="large")

       visu_a = SquareGravity.addChild('VisuA')

       visu_a.addObject('OglModel', name="Visual", color="yellow")
       visu_a.addObject('IdentityMapping', template="Vec3,Vec3", name="visualMapping", input="@../DOFs", output="@Visual")
    ```

TriangularFEMForceFieldOptim_tissue100x100_cpu.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -9 -1" dt="0.01">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangularFEMForceFieldOptim] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
        <DefaultAnimationLoop />
        <DefaultVisualManagerLoop />
        <CollisionPipeline verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <DiscreteIntersection/>
        
        <RegularGridTopology name="tissue" n="100 100 1" min="0 0 0" max="10 10 0" />
       
        <Node name="TriangularFEMForceFieldOptim-CPU-red">
            <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="20" name="linear solver" tolerance="1.0e-6" threshold="1.0e-6" />
            
            <MechanicalObject position="@../tissue.position" name="dofs" template="Vec3"/>
    
            <TriangleSetTopologyContainer name="Container" src="@../tissue"/>
            <TriangleSetTopologyModifier name="Modifier" />
            <TriangleSetGeometryAlgorithms name="GeomAlgo" template="Vec3" />
    
            <DiagonalMass massDensity="0.15" template="Vec3,Vec3"/>
            <FixedProjectiveConstraint indices="9900 9901 9902 9903 9996 9997 9998 9999" />
            
            <TriangularFEMForceFieldOptim name="FEM" youngModulus="600" poissonRatio="0.3" method="large" template="Vec3"/>
            <Node name="Visu">
                <OglModel name="Visual" color="red" />
                <IdentityMapping input="@../dofs" output="@Visual" />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9 -1", dt="0.01")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('DefaultVisualManagerLoop', )
       root.addObject('CollisionPipeline', verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', response="PenalityContactForceField")
       root.addObject('DiscreteIntersection', )
       root.addObject('RegularGridTopology', name="tissue", n="100 100 1", min="0 0 0", max="10 10 0")

       triangular_fem_force_field_optim__cpu_red = root.addChild('TriangularFEMForceFieldOptim-CPU-red')

       triangular_fem_force_field_optim__cpu_red.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
       triangular_fem_force_field_optim__cpu_red.addObject('CGLinearSolver', iterations="20", name="linear solver", tolerance="1.0e-6", threshold="1.0e-6")
       triangular_fem_force_field_optim__cpu_red.addObject('MechanicalObject', position="@../tissue.position", name="dofs", template="Vec3")
       triangular_fem_force_field_optim__cpu_red.addObject('TriangleSetTopologyContainer', name="Container", src="@../tissue")
       triangular_fem_force_field_optim__cpu_red.addObject('TriangleSetTopologyModifier', name="Modifier")
       triangular_fem_force_field_optim__cpu_red.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
       triangular_fem_force_field_optim__cpu_red.addObject('DiagonalMass', massDensity="0.15", template="Vec3,Vec3")
       triangular_fem_force_field_optim__cpu_red.addObject('FixedProjectiveConstraint', indices="9900 9901 9902 9903 9996 9997 9998 9999")
       triangular_fem_force_field_optim__cpu_red.addObject('TriangularFEMForceFieldOptim', name="FEM", youngModulus="600", poissonRatio="0.3", method="large", template="Vec3")

       visu = TriangularFEMForceFieldOptim-CPU-red.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="red")
       visu.addObject('IdentityMapping', input="@../dofs", output="@Visual")
    ```

TriangularFEMForceFieldOptim_tissue100x100_gpu.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -9 -1" dt="0.01">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="SofaCUDA"/> <!-- Needed to use components [DiagonalMass FixedProjectiveConstraint IdentityMapping MechanicalObject TriangleSetGeometryAlgorithms TriangularFEMForceFieldOptim] -->
    
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
    	
        <DefaultAnimationLoop />
        <DefaultVisualManagerLoop />
        <CollisionPipeline verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <DiscreteIntersection/>
        
        <RegularGridTopology name="tissue" n="100 100 1" min="0 0 0" max="10 10 0" />
        
        <Node name="TriangularFEMForceFieldOptim-GPU-Green">
            <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="20" name="linear solver" tolerance="1.0e-6" threshold="1.0e-6" />
            
            <MechanicalObject position="@../tissue.position" name="dofs" template="CudaVec3f"/>
    
            <TriangleSetTopologyContainer name="Container" src="@../tissue"/>
            <TriangleSetTopologyModifier name="Modifier" />
            <TriangleSetGeometryAlgorithms name="GeomAlgo" template="CudaVec3f" />
    
            <DiagonalMass massDensity="0.15" template="CudaVec3f,CudaVec3f"/>
            <FixedProjectiveConstraint indices="9900 9901 9902 9903 9996 9997 9998 9999" />
    
            <TriangularFEMForceFieldOptim name="FEM" youngModulus="600" poissonRatio="0.3" method="large" template="CudaVec3f"/>
            <Node name="Visu">
                <OglModel name="Visual" color="green" />
                <IdentityMapping input="@../dofs" output="@Visual" />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9 -1", dt="0.01")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('RequiredPlugin', name="SofaCUDA")
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('DefaultVisualManagerLoop', )
       root.addObject('CollisionPipeline', verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', response="PenalityContactForceField")
       root.addObject('DiscreteIntersection', )
       root.addObject('RegularGridTopology', name="tissue", n="100 100 1", min="0 0 0", max="10 10 0")

       triangular_fem_force_field_optim__gpu__green = root.addChild('TriangularFEMForceFieldOptim-GPU-Green')

       triangular_fem_force_field_optim__gpu__green.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
       triangular_fem_force_field_optim__gpu__green.addObject('CGLinearSolver', iterations="20", name="linear solver", tolerance="1.0e-6", threshold="1.0e-6")
       triangular_fem_force_field_optim__gpu__green.addObject('MechanicalObject', position="@../tissue.position", name="dofs", template="CudaVec3f")
       triangular_fem_force_field_optim__gpu__green.addObject('TriangleSetTopologyContainer', name="Container", src="@../tissue")
       triangular_fem_force_field_optim__gpu__green.addObject('TriangleSetTopologyModifier', name="Modifier")
       triangular_fem_force_field_optim__gpu__green.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo", template="CudaVec3f")
       triangular_fem_force_field_optim__gpu__green.addObject('DiagonalMass', massDensity="0.15", template="CudaVec3f,CudaVec3f")
       triangular_fem_force_field_optim__gpu__green.addObject('FixedProjectiveConstraint', indices="9900 9901 9902 9903 9996 9997 9998 9999")
       triangular_fem_force_field_optim__gpu__green.addObject('TriangularFEMForceFieldOptim', name="FEM", youngModulus="600", poissonRatio="0.3", method="large", template="CudaVec3f")

       visu = TriangularFEMForceFieldOptim-GPU-Green.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="green")
       visu.addObject('IdentityMapping', input="@../dofs", output="@Visual")
    ```

