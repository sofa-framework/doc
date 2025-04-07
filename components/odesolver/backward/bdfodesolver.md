<!-- generate_doc -->
# BDFOdeSolver

Velocity-based ODE solver using Backward Differentiation Formula (BDF), at any order, supporting variable time step size.


__Target__: Sofa.Component.ODESolver.Backward

__namespace__: sofa::component::odesolver::backward

__parents__:

- BaseLinearMultiStepMethod

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
		<td>order</td>
		<td>
Order of the numerical method
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping coefficient related to stiffness, > 0
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>rayleighMass</td>
		<td>
Rayleigh damping coefficient related to mass, > 0
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
|linearSolver|Linear solver used by this component|LinearSolver|
|newtonSolver|Link to a Newton-Raphson solver to solve the nonlinear equation produced by this numerical method|NewtonRaphsonSolver|

## Examples 

BDFOdeSolver.scn

=== "XML"

    ```xml
    <Node name="root" gravity="-1.8 0 100" dt="0.01">
    
        <Node name="plugins">
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
            <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader,MeshOBJLoader] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [EigenSimplicialLDLT] -->
            <RequiredPlugin name="Sofa.Component.LinearSystem"/> <!-- Needed to use components [ConstantSparsityPatternSystem] -->
            <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [MeshMatrixMass] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [BDFOdeSolver,NewtonRaphsonSolver] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.HyperElastic"/> <!-- Needed to use components [TetrahedronHyperelasticityFEMForceField] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms,TetrahedronSetTopologyContainer] -->
            <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
            <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        </Node>
    
        <VisualStyle displayFlags="showWireframe showVisual showBehaviorModels hideForceFields" />
        <DefaultAnimationLoop parallelODESolving="false"/>
    
        <Node name="DeformableObject">
    
            <BDFOdeSolver order="2" printLog="false" rayleighMass="0.01" rayleighStiffness="0.01"/>
            <NewtonRaphsonSolver name="newton" printLog="false"
                                 maxNbIterationsNewton="10" absoluteResidualStoppingThreshold="1e-5"
                                 maxNbIterationsLineSearch="5" lineSearchCoefficient="0.5"
                                 relativeInitialStoppingThreshold="1e-3"
                                 absoluteEstimateDifferenceThreshold="1e-5"
                                 relativeEstimateDifferenceThreshold="1e-5"/>
            <ConstantSparsityPatternSystem template="CompressedRowSparseMatrix" name="A" checkIndices="false"/>
            <PCGLinearSolver name="PCG" iterations="1000" preconditioner="@preconditioner"/>
            <AsyncSparseLDLSolver name="preconditioner"/>
    
            <MeshGmshLoader name="loader" filename="mesh/truthcylinder1.msh" />
            <TetrahedronSetTopologyContainer src="@loader" name="topologyContainer"/>
            <TetrahedronSetGeometryAlgorithms name="geomAlgo"/>
            <MechanicalObject src="@loader" />
            <MeshMatrixMass totalMass="15" topology="@topologyContainer"/>
    
            <BoxROI name="box" box="-10 -20 -10  10 -17.5 10" drawBoxes="true"/>
            <FixedProjectiveConstraint indices="@box.indices" />
            <TetrahedronHyperelasticityFEMForceField name="FEM" ParameterSet="3448.2759 31034.483" materialName="StVenantKirchhoff"/>
    
            <Node name="visual">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/truthcylinder1.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_0" color="red" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="-1.8 0 100", dt="0.01")

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSystem")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.HyperElastic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       plugins.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")

       root.addObject('VisualStyle', displayFlags="showWireframe showVisual showBehaviorModels hideForceFields")
       root.addObject('DefaultAnimationLoop', parallelODESolving="false")

       deformable_object = root.addChild('DeformableObject')

       deformable_object.addObject('BDFOdeSolver', order="2", printLog="false", rayleighMass="0.01", rayleighStiffness="0.01")
       deformable_object.addObject('NewtonRaphsonSolver', name="newton", printLog="false", maxNbIterationsNewton="10", absoluteResidualStoppingThreshold="1e-5", maxNbIterationsLineSearch="5", lineSearchCoefficient="0.5", relativeInitialStoppingThreshold="1e-3", absoluteEstimateDifferenceThreshold="1e-5", relativeEstimateDifferenceThreshold="1e-5")
       deformable_object.addObject('ConstantSparsityPatternSystem', template="CompressedRowSparseMatrix", name="A", checkIndices="false")
       deformable_object.addObject('PCGLinearSolver', name="PCG", iterations="1000", preconditioner="@preconditioner")
       deformable_object.addObject('AsyncSparseLDLSolver', name="preconditioner")
       deformable_object.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
       deformable_object.addObject('TetrahedronSetTopologyContainer', src="@loader", name="topologyContainer")
       deformable_object.addObject('TetrahedronSetGeometryAlgorithms', name="geomAlgo")
       deformable_object.addObject('MechanicalObject', src="@loader")
       deformable_object.addObject('MeshMatrixMass', totalMass="15", topology="@topologyContainer")
       deformable_object.addObject('BoxROI', name="box", box="-10 -20 -10  10 -17.5 10", drawBoxes="true")
       deformable_object.addObject('FixedProjectiveConstraint', indices="@box.indices")
       deformable_object.addObject('TetrahedronHyperelasticityFEMForceField', name="FEM", ParameterSet="3448.2759 31034.483", materialName="StVenantKirchhoff")

       visual = DeformableObject.addChild('visual')

       visual.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/truthcylinder1.obj", handleSeams="1")
       visual.addObject('OglModel', name="Visual", src="@meshLoader_0", color="red")
       visual.addObject('BarycentricMapping', input="@..", output="@Visual")
    ```

BDFOdeSolver_spring1d.scn

=== "XML"

    ```xml
    <Node name="root" gravity="-9.81 0 0" dt="0.01">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [EigenSimplicialLDLT] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [MeshMatrixMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [NewtonRaphsonSolver] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Integration"/> <!-- Needed to use components [BDF1] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [SpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglCylinderModel] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [EdgeSetTopologyContainer] -->
    
        <VisualStyle displayFlags="showWireframe showVisual showBehaviorModels showForceFields" />
        <DefaultAnimationLoop/>
        <VisualGrid size="2"/>
        <LineAxis size="2"/>
    
        <Node name="BDF-1">
    
            <BDFOdeSolver order="1" printLog="false" rayleighMass="0.01" rayleighStiffness="0.01"/>
            <NewtonRaphsonSolver name="newton" printLog="false" maxNbIterationsNewton="4" maxNbIterationsLineSearch="2" absoluteResidualStoppingThreshold="1e-6"/>
            <EigenSimplicialLDLT template="CompressedRowSparseMatrix"/>
    
            <MechanicalObject name="dofs" template="Vec1" position="1 " rest_position="0" showObject="true" showObjectScale="20"/>
            <PointSetTopologyContainer name="topologyContainer" position="1"/>
            <UniformMass totalMass="1" topology="@topologyContainer"/>
            <RestShapeSpringsForceField points="0"/>
        </Node>
    
        <Node name="BDF-2">
    
            <BDFOdeSolver order="2" printLog="false" rayleighMass="0.01" rayleighStiffness="0.01"/>
            <NewtonRaphsonSolver name="newton" printLog="false" maxNbIterationsNewton="4" maxNbIterationsLineSearch="2" absoluteResidualStoppingThreshold="1e-6"/>
            <EigenSimplicialLDLT template="CompressedRowSparseMatrix"/>
    
            <MechanicalObject name="dofs" template="Vec1" position="1 " rest_position="0" showObject="true" showObjectScale="20"/>
            <PointSetTopologyContainer name="topologyContainer" position="1"/>
            <UniformMass totalMass="1" topology="@topologyContainer"/>
            <RestShapeSpringsForceField points="0"/>
        </Node>
    
        <Node name="BDF-3">
    
            <BDFOdeSolver order="3" printLog="false" rayleighMass="0.01" rayleighStiffness="0.01"/>
            <NewtonRaphsonSolver name="newton" printLog="false" maxNbIterationsNewton="4" maxNbIterationsLineSearch="2" absoluteResidualStoppingThreshold="1e-6"/>
            <EigenSimplicialLDLT template="CompressedRowSparseMatrix"/>
    
            <MechanicalObject name="dofs" template="Vec1" position="1 " rest_position="0" showObject="true" showObjectScale="20"/>
            <PointSetTopologyContainer name="topologyContainer" position="1"/>
            <UniformMass totalMass="1" topology="@topologyContainer"/>
            <RestShapeSpringsForceField points="0"/>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="-9.81 0 0", dt="0.01")

       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Integration")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('VisualStyle', displayFlags="showWireframe showVisual showBehaviorModels showForceFields")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualGrid', size="2")
       root.addObject('LineAxis', size="2")

       bdf_1 = root.addChild('BDF-1')

       bdf_1.addObject('BDFOdeSolver', order="1", printLog="false", rayleighMass="0.01", rayleighStiffness="0.01")
       bdf_1.addObject('NewtonRaphsonSolver', name="newton", printLog="false", maxNbIterationsNewton="4", maxNbIterationsLineSearch="2", absoluteResidualStoppingThreshold="1e-6")
       bdf_1.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrix")
       bdf_1.addObject('MechanicalObject', name="dofs", template="Vec1", position="1 ", rest_position="0", showObject="true", showObjectScale="20")
       bdf_1.addObject('PointSetTopologyContainer', name="topologyContainer", position="1")
       bdf_1.addObject('UniformMass', totalMass="1", topology="@topologyContainer")
       bdf_1.addObject('RestShapeSpringsForceField', points="0")

       bdf_2 = root.addChild('BDF-2')

       bdf_2.addObject('BDFOdeSolver', order="2", printLog="false", rayleighMass="0.01", rayleighStiffness="0.01")
       bdf_2.addObject('NewtonRaphsonSolver', name="newton", printLog="false", maxNbIterationsNewton="4", maxNbIterationsLineSearch="2", absoluteResidualStoppingThreshold="1e-6")
       bdf_2.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrix")
       bdf_2.addObject('MechanicalObject', name="dofs", template="Vec1", position="1 ", rest_position="0", showObject="true", showObjectScale="20")
       bdf_2.addObject('PointSetTopologyContainer', name="topologyContainer", position="1")
       bdf_2.addObject('UniformMass', totalMass="1", topology="@topologyContainer")
       bdf_2.addObject('RestShapeSpringsForceField', points="0")

       bdf_3 = root.addChild('BDF-3')

       bdf_3.addObject('BDFOdeSolver', order="3", printLog="false", rayleighMass="0.01", rayleighStiffness="0.01")
       bdf_3.addObject('NewtonRaphsonSolver', name="newton", printLog="false", maxNbIterationsNewton="4", maxNbIterationsLineSearch="2", absoluteResidualStoppingThreshold="1e-6")
       bdf_3.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrix")
       bdf_3.addObject('MechanicalObject', name="dofs", template="Vec1", position="1 ", rest_position="0", showObject="true", showObjectScale="20")
       bdf_3.addObject('PointSetTopologyContainer', name="topologyContainer", position="1")
       bdf_3.addObject('UniformMass', totalMass="1", topology="@topologyContainer")
       bdf_3.addObject('RestShapeSpringsForceField', points="0")
    ```

BDFOdeSolver_spring3d.scn

=== "XML"

    ```xml
    <Node name="root" gravity="0 -9.81 0" dt="0.01">
    
        <Node name="plugins">
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [EigenSimplicialLDLT] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [BDFOdeSolver,NewtonRaphsonSolver] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [SpringForceField] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [EdgeSetTopologyContainer] -->
            <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [LineAxis,VisualGrid,VisualStyle] -->
        </Node>
    
        <VisualStyle displayFlags="showWireframe showVisual showBehaviorModels showForceFields" />
        <DefaultAnimationLoop/>
        <VisualGrid size="2"/>
        <LineAxis size="2"/>
    
        <Node name="BDF-1">
    
            <BDFOdeSolver order="1" printLog="false" rayleighMass="0.01" rayleighStiffness="0.01"/>
            <NewtonRaphsonSolver name="newton" printLog="false" maxNbIterationsNewton="4" maxNbIterationsLineSearch="2" absoluteResidualStoppingThreshold="1e-6"/>
            <EigenSimplicialLDLT template="CompressedRowSparseMatrix"/>
    
            <MechanicalObject name="dofs" template="Vec3" position="0 0 0  1 1 0 " showObject="true" showObjectScale="20"/>
            <EdgeSetTopologyContainer name="topologyContainer" edges="0 1" position="@dofs.position"/>
            <UniformMass totalMass="15" topology="@topologyContainer"/>
            <SpringForceField spring="0 1 1000 0 1"/>
            <FixedProjectiveConstraint indices="0" />
    
        </Node>
    
        <Node name="BDF-2">
    
            <BDFOdeSolver order="2" printLog="false" rayleighMass="0.01" rayleighStiffness="0.01"/>
            <NewtonRaphsonSolver name="newton" printLog="false" maxNbIterationsNewton="4" maxNbIterationsLineSearch="2" absoluteResidualStoppingThreshold="1e-6"/>
            <EigenSimplicialLDLT template="CompressedRowSparseMatrix"/>
    
            <MechanicalObject name="dofs" template="Vec3" position="0 0 0  1 1 0 " showObject="true" showObjectScale="20"/>
            <EdgeSetTopologyContainer name="topologyContainer" edges="0 1" position="@dofs.position"/>
            <UniformMass totalMass="15" topology="@topologyContainer"/>
            <SpringForceField spring="0 1 1000 0 1"/>
            <FixedProjectiveConstraint indices="0" />
    
        </Node>
    
        <Node name="BDF-3">
    
            <BDFOdeSolver order="3" printLog="false" rayleighMass="0.01" rayleighStiffness="0.01"/>
            <NewtonRaphsonSolver name="newton" printLog="false" maxNbIterationsNewton="4" maxNbIterationsLineSearch="2" absoluteResidualStoppingThreshold="1e-6"/>
            <EigenSimplicialLDLT template="CompressedRowSparseMatrix"/>
    
            <MechanicalObject name="dofs" template="Vec3" position="0 0 0  1 1 0 " showObject="true" showObjectScale="20"/>
            <EdgeSetTopologyContainer name="topologyContainer" edges="0 1" position="@dofs.position"/>
            <UniformMass totalMass="15" topology="@topologyContainer"/>
            <SpringForceField spring="0 1 1000 0 1"/>
            <FixedProjectiveConstraint indices="0" />
    
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9.81 0", dt="0.01")

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Visual")

       root.addObject('VisualStyle', displayFlags="showWireframe showVisual showBehaviorModels showForceFields")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualGrid', size="2")
       root.addObject('LineAxis', size="2")

       bdf_1 = root.addChild('BDF-1')

       bdf_1.addObject('BDFOdeSolver', order="1", printLog="false", rayleighMass="0.01", rayleighStiffness="0.01")
       bdf_1.addObject('NewtonRaphsonSolver', name="newton", printLog="false", maxNbIterationsNewton="4", maxNbIterationsLineSearch="2", absoluteResidualStoppingThreshold="1e-6")
       bdf_1.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrix")
       bdf_1.addObject('MechanicalObject', name="dofs", template="Vec3", position="0 0 0  1 1 0 ", showObject="true", showObjectScale="20")
       bdf_1.addObject('EdgeSetTopologyContainer', name="topologyContainer", edges="0 1", position="@dofs.position")
       bdf_1.addObject('UniformMass', totalMass="15", topology="@topologyContainer")
       bdf_1.addObject('SpringForceField', spring="0 1 1000 0 1")
       bdf_1.addObject('FixedProjectiveConstraint', indices="0")

       bdf_2 = root.addChild('BDF-2')

       bdf_2.addObject('BDFOdeSolver', order="2", printLog="false", rayleighMass="0.01", rayleighStiffness="0.01")
       bdf_2.addObject('NewtonRaphsonSolver', name="newton", printLog="false", maxNbIterationsNewton="4", maxNbIterationsLineSearch="2", absoluteResidualStoppingThreshold="1e-6")
       bdf_2.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrix")
       bdf_2.addObject('MechanicalObject', name="dofs", template="Vec3", position="0 0 0  1 1 0 ", showObject="true", showObjectScale="20")
       bdf_2.addObject('EdgeSetTopologyContainer', name="topologyContainer", edges="0 1", position="@dofs.position")
       bdf_2.addObject('UniformMass', totalMass="15", topology="@topologyContainer")
       bdf_2.addObject('SpringForceField', spring="0 1 1000 0 1")
       bdf_2.addObject('FixedProjectiveConstraint', indices="0")

       bdf_3 = root.addChild('BDF-3')

       bdf_3.addObject('BDFOdeSolver', order="3", printLog="false", rayleighMass="0.01", rayleighStiffness="0.01")
       bdf_3.addObject('NewtonRaphsonSolver', name="newton", printLog="false", maxNbIterationsNewton="4", maxNbIterationsLineSearch="2", absoluteResidualStoppingThreshold="1e-6")
       bdf_3.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrix")
       bdf_3.addObject('MechanicalObject', name="dofs", template="Vec3", position="0 0 0  1 1 0 ", showObject="true", showObjectScale="20")
       bdf_3.addObject('EdgeSetTopologyContainer', name="topologyContainer", edges="0 1", position="@dofs.position")
       bdf_3.addObject('UniformMass', totalMass="15", topology="@topologyContainer")
       bdf_3.addObject('SpringForceField', spring="0 1 1000 0 1")
       bdf_3.addObject('FixedProjectiveConstraint', indices="0")
    ```

