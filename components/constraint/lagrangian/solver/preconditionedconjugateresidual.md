<!-- generate_doc -->
# PreconditionedConjugateResidual

A Constraint Solver using the Linear Complementarity Problem formulation to solve Constraint based components using a Projected Jacobi iterative method


__Target__: Sofa.Component.Constraint.Lagrangian.Solver

__namespace__: sofa::component::constraint::lagrangian::solver

__parents__:

- BuiltConstraintSolver

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
		<td>maxIterations</td>
		<td>
maximal number of iterations of iterative algorithm
		</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>tolerance</td>
		<td>
residual error threshold for termination of the Gauss-Seidel algorithm
		</td>
		<td>0.001</td>
	</tr>
	<tr>
		<td>sor</td>
		<td>
Successive Over Relaxation parameter (0-2)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>regularizationTerm</td>
		<td>
Add regularization factor times the identity matrix to the compliance W when solving constraints
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>scaleTolerance</td>
		<td>
Scale the error tolerance with the number of constraints
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>allVerified</td>
		<td>
All constraints must be verified (each constraint's error < tolerance)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>computeGraphs</td>
		<td>
Compute graphs of errors and forces during resolution
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>constraintForces</td>
		<td>
OUTPUT: constraint forces (stored only if computeConstraintForces=True)
		</td>
		<td></td>
	</tr>
	<tr>
		<td>computeConstraintForces</td>
		<td>
enable the storage of the constraintForces.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>nbThreads</td>
		<td>
If not yet initialized, the main task scheduler is initialized with this number of threads. 0 corresponds to the number of available cores on the CPU. -n (minus) corresponds to the number of available cores on the CPU minus the provided number.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>taskSchedulerType</td>
		<td>
Type of task scheduler to use.
		</td>
		<td>_default</td>
	</tr>
	<tr>
		<td>multithreading</td>
		<td>
Build compliances concurrently
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>useSVDForRegularization</td>
		<td>
Use SVD decomposiiton of the compliance matrix to project singular values smaller than regularization to the regularization term. Only works with built
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>svdSingularValueNullSpaceCriteriaFactor</td>
		<td>
Fraction of the highest singular value bellow which a singular value will be supposed to belong to the nullspace
		</td>
		<td>0.01</td>
	</tr>
	<tr>
		<td>svdSingularVectorNullSpaceCriteriaFactor</td>
		<td>
Absolute value bellow which a component of a normalized base vector will be considered null
		</td>
		<td>0.001</td>
	</tr>
	<tr>
		<td colspan="3">Graph</td>
	</tr>
	<tr>
		<td>graphErrors</td>
		<td>
Sum of the constraints' errors at each iteration
		</td>
		<td></td>
	</tr>
	<tr>
		<td>graphConstraints</td>
		<td>
Graph of each constraint's error at the end of the resolution
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Graph2</td>
	</tr>
	<tr>
		<td>graphForces</td>
		<td>
Graph of each constraint's force at each step of the resolution
		</td>
		<td></td>
	</tr>
	<tr>
		<td>graphViolations</td>
		<td>
Graph of each constraint's violation at each step of the resolution
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Stats</td>
	</tr>
	<tr>
		<td>currentNumConstraints</td>
		<td>
OUTPUT: current number of constraints
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>currentNumConstraintGroups</td>
		<td>
OUTPUT: current number of constraints
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>currentIterations</td>
		<td>
OUTPUT: current number of constraint groups
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>currentError</td>
		<td>
OUTPUT: current error
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
|constraintCorrections|List of constraint corrections handled by this constraint solver|BaseConstraintCorrection|

## Examples 

PreconditionedConjugateResidual.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    
    <Node name="root" dt="0.01" gravity="0 0 -0.981">
        <RequiredPlugin pluginName="Sofa.Component.AnimationLoop"/> <!-- Needed to use components [FreeMotionAnimationLoop] -->
        <RequiredPlugin pluginName="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin pluginName="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [LinearSolverConstraintCorrection] -->
        <RequiredPlugin pluginName="Sofa.Component.Constraint.Lagrangian.Model"/> <!-- Needed to use components [FixedLagrangianConstraint] -->
        <RequiredPlugin pluginName="Sofa.Component.Constraint.Lagrangian.Solver"/> <!-- Needed to use components [GenericConstraintSolver] -->
        <RequiredPlugin pluginName="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin pluginName="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [SparseLDLSolver] -->
        <RequiredPlugin pluginName="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin pluginName="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin pluginName="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin pluginName="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin pluginName="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin pluginName="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping Tetra2TriangleTopologicalMapping] -->
        <RequiredPlugin pluginName="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin pluginName="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin pluginName="Sofa.GUI.Component"/> <!-- Needed to use components [ConstraintAttachButtonSetting] -->
    
        <VisualStyle displayFlags="showForceFields"/>
        <ConstraintAttachButtonSetting /> <!-- The presence of this component sets the mouse interaction to Lagrangian-based constraints at the GUI launch -->
    
        <FreeMotionAnimationLoop />
        <PreconditionedConjugateResidual maxIterations="30" tolerance="1e-9" regularizationTerm="0"/>
    
        <!-- $$$$$$$$$$$$$$$$$$$$$$ TOPOLOGY 1 $$$$$$$$$$$$$$$$$$$$$$ -->
        <Node name="BEAMVOLUME">
            <RegularGridTopology name="HexaTop" n="25 5 5" min="0 0 0" max="0.5 0.1 0.1"/>
            <TetrahedronSetTopologyContainer name="Container" position="@HexaTop.position"/>
            <TetrahedronSetTopologyModifier name="Modifier"/>
            <Hexa2TetraTopologicalMapping input="@HexaTop" output="@Container" swapping="true"/>
        </Node>
    
        <Node name="FEM">
            <EulerImplicitSolver firstOrder="false" rayleighMass="0.1" rayleighStiffness="0.1"/>
            <SparseLDLSolver name="precond" template="CompressedRowSparseMatrixMat3x3" parallelInverseProduct="true" />
    
            <TetrahedronSetTopologyContainer name="Container" position="@../BEAMVOLUME/HexaTop.position" tetrahedra="@../BEAMVOLUME/Container.tetrahedra"/>
            <TetrahedronSetTopologyModifier name="Modifier"/>
    
            <MechanicalObject name="mstate" template="Vec3d" src="@Container"/>
            <TetrahedronFEMForceField name="forceField" listening="true" youngModulus="6e4" poissonRatio="0.40" />
            <UniformMass totalMass="1"/>
    
            <BoxROI name="box" box="-0.01 -0.01 -0.01 0.0001 0.11 0.11"/>
            <FixedLagrangianConstraint indices="@box.indices"/>
    
            <Node name="Surface">
                <TriangleSetTopologyContainer name="Container"/>
                <TriangleSetTopologyModifier name="Modifier"/>
                <Tetra2TriangleTopologicalMapping input="@../Container" output="@Container" flipNormals="false"/>
                <MechanicalObject name="dofs" rest_position="@../mstate.rest_position"/>
                <TriangleCollisionModel name="Torus8CMT" contactDistance="0.001" contactStiffness="20" color="0.94117647058824 0.93725490196078 0.89411764705882" />
                <Node name="Visual" activated="1">
                    <TriangleSetTopologyContainer name="Container" src="@../Container"/>
                    <OglModel color="1.0 0.1 0.2 1.0" name="visualModel"/>
                    <IdentityMapping name="VisualMapping"/>
                </Node>
                <IdentityMapping name="SurfaceMapping"/>
            </Node>
    
            <LinearSolverConstraintCorrection linearSolver="@precond"/>
        </Node>
    
        
    
    </Node>
    
    

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 0 -0.981")

       root.addObject('RequiredPlugin', pluginName="Sofa.Component.AnimationLoop")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Constraint.Lagrangian.Correction")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Constraint.Lagrangian.Model")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Constraint.Lagrangian.Solver")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSolver.Direct")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Mapping")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', pluginName="Sofa.GL.Component.Rendering3D")
       root.addObject('RequiredPlugin', pluginName="Sofa.GUI.Component")
       root.addObject('VisualStyle', displayFlags="showForceFields")
       root.addObject('ConstraintAttachButtonSetting', )
       root.addObject('FreeMotionAnimationLoop', )
       root.addObject('PreconditionedConjugateResidual', maxIterations="30", tolerance="1e-9", regularizationTerm="0")

       beamvolume = root.addChild('BEAMVOLUME')

       beamvolume.addObject('RegularGridTopology', name="HexaTop", n="25 5 5", min="0 0 0", max="0.5 0.1 0.1")
       beamvolume.addObject('TetrahedronSetTopologyContainer', name="Container", position="@HexaTop.position")
       beamvolume.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       beamvolume.addObject('Hexa2TetraTopologicalMapping', input="@HexaTop", output="@Container", swapping="true")

       fem = root.addChild('FEM')

       fem.addObject('EulerImplicitSolver', firstOrder="false", rayleighMass="0.1", rayleighStiffness="0.1")
       fem.addObject('SparseLDLSolver', name="precond", template="CompressedRowSparseMatrixMat3x3", parallelInverseProduct="true")
       fem.addObject('TetrahedronSetTopologyContainer', name="Container", position="@../BEAMVOLUME/HexaTop.position", tetrahedra="@../BEAMVOLUME/Container.tetrahedra")
       fem.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       fem.addObject('MechanicalObject', name="mstate", template="Vec3d", src="@Container")
       fem.addObject('TetrahedronFEMForceField', name="forceField", listening="true", youngModulus="6e4", poissonRatio="0.40")
       fem.addObject('UniformMass', totalMass="1")
       fem.addObject('BoxROI', name="box", box="-0.01 -0.01 -0.01 0.0001 0.11 0.11")
       fem.addObject('FixedLagrangianConstraint', indices="@box.indices")

       surface = FEM.addChild('Surface')

       surface.addObject('TriangleSetTopologyContainer', name="Container")
       surface.addObject('TriangleSetTopologyModifier', name="Modifier")
       surface.addObject('Tetra2TriangleTopologicalMapping', input="@../Container", output="@Container", flipNormals="false")
       surface.addObject('MechanicalObject', name="dofs", rest_position="@../mstate.rest_position")
       surface.addObject('TriangleCollisionModel', name="Torus8CMT", contactDistance="0.001", contactStiffness="20", color="0.94117647058824 0.93725490196078 0.89411764705882")

       visual = Surface.addChild('Visual', activated="1")

       visual.addObject('TriangleSetTopologyContainer', name="Container", src="@../Container")
       visual.addObject('OglModel', color="1.0 0.1 0.2 1.0", name="visualModel")
       visual.addObject('IdentityMapping', name="VisualMapping")

       surface.addObject('IdentityMapping', name="SurfaceMapping")

       fem.addObject('LinearSolverConstraintCorrection', linearSolver="@precond")
    ```

