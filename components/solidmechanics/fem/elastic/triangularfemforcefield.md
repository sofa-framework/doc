# TriangularFEMForceField

Corotational Triangular finite elements for dynamic topology


__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.Component.SolidMechanics.FEM.Elastic`

__namespace__: `#!c++ sofa::component::solidmechanics::fem::elastic`

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
		<td>poissonRatio</td>
		<td>
Poisson ratio in Hooke's law (vector)
</td>
		<td>0.3</td>
	</tr>
	<tr>
		<td>youngModulus</td>
		<td>
Young modulus in Hooke's law (vector)
</td>
		<td>1000</td>
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
Exponant in the Hosford yield criteria
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

Benchmark/TopologicalChanges/TriangularFEMForceField_RemovingMeshTest.scn

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
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -9 0", dt="0.01", bbox="-1 -1 -1 1 1 1")
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
        root.addObject('DefaultAnimationLoop')
        root.addObject('CollisionPipeline', verbose="0")
        root.addObject('BruteForceBroadPhase', name="N2")
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField")
        root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")

        SquareGravity = root.addChild('SquareGravity')
        SquareGravity.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        SquareGravity.addObject('CGLinearSolver', iterations="25", tolerance="1e-5", threshold="1e-5", name="linear solver")
        SquareGravity.addObject('MeshGmshLoader', name="loader", filename="mesh/square3.msh", createSubelements="true")
        SquareGravity.addObject('MechanicalObject', name="dofs", src="@loader", template="Vec3")
        SquareGravity.addObject('TriangleSetTopologyContainer', name="Triangle_topo", src="@loader")
        SquareGravity.addObject('TriangleSetTopologyModifier', name="Modifier")
        SquareGravity.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        SquareGravity.addObject('DiagonalMass', template="Vec3,Vec3", name="mass", massDensity="1.0")
        SquareGravity.addObject('TriangularFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.3", youngModulus="60")
        SquareGravity.addObject('TopologicalChangeProcessor', listening="1", filename="RemovingTrianglesProcess_constraint.txt")
    ```

Component/SolidMechanics/FEM/TriangularFEMForceFieldOptim.scn

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
            <CGLinearSolver verbose="0" printLog="0" iterations="25" name="linearsolver1" tolerance="1.0e-9" threshold="1.0e-9" />
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
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.05", gravity="0 10 10", showBoundingTree="0")
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
        root.addObject('DefaultAnimationLoop')
        root.addObject('MeshGmshLoader', filename="mesh/square3.msh", name="loaderSquare")

        SquareGravity1 = root.addChild('SquareGravity1')
        SquareGravity1.addObject('EulerImplicitSolver', name="odesolver1", printLog="0", rayleighStiffness="0.1", rayleighMass="0.1")
        SquareGravity1.addObject('CGLinearSolver', verbose="0", printLog="0", iterations="25", name="linearsolver1", tolerance="1.0e-9", threshold="1.0e-9")
        SquareGravity1.addObject('TriangleSetTopologyContainer', name="Container", src="@../loaderSquare")
        SquareGravity1.addObject('MechanicalObject', name="DOFs", src="@../loaderSquare", scale="100")
        SquareGravity1.addObject('TriangleSetTopologyModifier', name="Modifier")
        SquareGravity1.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
        SquareGravity1.addObject('DiagonalMass', massDensity="0.005")
        SquareGravity1.addObject('FixedProjectiveConstraint', indices="0 1 2")
        SquareGravity1.addObject('TriangularFEMForceFieldOptim', name="FEM", youngModulus="600", poissonRatio="0.3", method="large", printLog="1")

        VisuA = SquareGravity1.addChild('VisuA')
        VisuA.addObject('OglModel', name="Visual", color="yellow")
        VisuA.addObject('IdentityMapping', name="visualMapping", input="@../DOFs", output="@Visual")
    ```

Component/SolidMechanics/FEM/TriangularFEMForceField.scn

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
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.05", gravity="0 -9.8 10", showBoundingTree="0")

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
        root.addObject('DefaultAnimationLoop')

        SquareGravity = root.addChild('SquareGravity')
        SquareGravity.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        SquareGravity.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        SquareGravity.addObject('MeshGmshLoader', filename="mesh/square3.msh", name="loader")
        SquareGravity.addObject('MechanicalObject', src="@loader", name="DOFs", scale3d="100 100 0")
        SquareGravity.addObject('TriangleSetTopologyContainer', src="@loader", name="Container")
        SquareGravity.addObject('TriangleSetTopologyModifier', name="Modifier")
        SquareGravity.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
        SquareGravity.addObject('DiagonalMass', massDensity="0.005")
        SquareGravity.addObject('FixedProjectiveConstraint', indices="0 1 2")
        SquareGravity.addObject('TriangularFEMForceField', name="FEM", youngModulus="600", poissonRatio="0.3", method="large")

        VisuA = SquareGravity.addChild('VisuA')
        VisuA.addObject('OglModel', name="Visual", color="yellow")
        VisuA.addObject('IdentityMapping', template="Vec3,Vec3", name="visualMapping", input="@../DOFs", output="@Visual")
    ```

SofaCUDA/share/sofa/examples/SofaCUDA/benchmarks/TriangularFEMForceFieldOptim_tissue100x100_gpu.scn

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
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -9 -1", dt="0.01")
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
        root.addObject('DefaultAnimationLoop')
        root.addObject('DefaultVisualManagerLoop')
        root.addObject('CollisionPipeline', verbose="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField")
        root.addObject('DiscreteIntersection')
        root.addObject('RegularGridTopology', name="tissue", n="100 100 1", min="0 0 0", max="10 10 0")

        TriangularFEMForceFieldOptim-GPU-Green = root.addChild('TriangularFEMForceFieldOptim-GPU-Green')
        TriangularFEMForceFieldOptim-GPU-Green.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        TriangularFEMForceFieldOptim-GPU-Green.addObject('CGLinearSolver', iterations="20", name="linear solver", tolerance="1.0e-6", threshold="1.0e-6")
        TriangularFEMForceFieldOptim-GPU-Green.addObject('MechanicalObject', position="@../tissue.position", name="dofs", template="CudaVec3f")
        TriangularFEMForceFieldOptim-GPU-Green.addObject('TriangleSetTopologyContainer', name="Container", src="@../tissue")
        TriangularFEMForceFieldOptim-GPU-Green.addObject('TriangleSetTopologyModifier', name="Modifier")
        TriangularFEMForceFieldOptim-GPU-Green.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo", template="CudaVec3f")
        TriangularFEMForceFieldOptim-GPU-Green.addObject('DiagonalMass', massDensity="0.15", template="CudaVec3f,CudaVec3f")
        TriangularFEMForceFieldOptim-GPU-Green.addObject('FixedProjectiveConstraint', indices="9900 9901 9902 9903 9996 9997 9998 9999")
        TriangularFEMForceFieldOptim-GPU-Green.addObject('TriangularFEMForceFieldOptim', name="FEM", youngModulus="600", poissonRatio="0.3", method="large", template="CudaVec3f")

        Visu = TriangularFEMForceFieldOptim-GPU-Green.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="green")
        Visu.addObject('IdentityMapping', input="@../dofs", output="@Visual")
    ```

SofaCUDA/share/sofa/examples/SofaCUDA/benchmarks/TriangularFEMForceFieldOptim_tissue100x100_cpu.scn

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
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -9 -1", dt="0.01")
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
        root.addObject('DefaultAnimationLoop')
        root.addObject('DefaultVisualManagerLoop')
        root.addObject('CollisionPipeline', verbose="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField")
        root.addObject('DiscreteIntersection')
        root.addObject('RegularGridTopology', name="tissue", n="100 100 1", min="0 0 0", max="10 10 0")

        TriangularFEMForceFieldOptim-CPU-red = root.addChild('TriangularFEMForceFieldOptim-CPU-red')
        TriangularFEMForceFieldOptim-CPU-red.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        TriangularFEMForceFieldOptim-CPU-red.addObject('CGLinearSolver', iterations="20", name="linear solver", tolerance="1.0e-6", threshold="1.0e-6")
        TriangularFEMForceFieldOptim-CPU-red.addObject('MechanicalObject', position="@../tissue.position", name="dofs", template="Vec3")
        TriangularFEMForceFieldOptim-CPU-red.addObject('TriangleSetTopologyContainer', name="Container", src="@../tissue")
        TriangularFEMForceFieldOptim-CPU-red.addObject('TriangleSetTopologyModifier', name="Modifier")
        TriangularFEMForceFieldOptim-CPU-red.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
        TriangularFEMForceFieldOptim-CPU-red.addObject('DiagonalMass', massDensity="0.15", template="Vec3,Vec3")
        TriangularFEMForceFieldOptim-CPU-red.addObject('FixedProjectiveConstraint', indices="9900 9901 9902 9903 9996 9997 9998 9999")
        TriangularFEMForceFieldOptim-CPU-red.addObject('TriangularFEMForceFieldOptim', name="FEM", youngModulus="600", poissonRatio="0.3", method="large", template="Vec3")

        Visu = TriangularFEMForceFieldOptim-CPU-red.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="red")
        Visu.addObject('IdentityMapping', input="@../dofs", output="@Visual")
    ```
