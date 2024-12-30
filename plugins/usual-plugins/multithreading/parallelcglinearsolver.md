<!-- generate_doc -->
# ParallelCGLinearSolver

Parallel version of the linear solver using the conjugate gradient iterative algorithm.


## ParallelCompressedRowSparseMatrixMat3x3d

Templates:

- ParallelCompressedRowSparseMatrixMat3x3d

__Target__: MultiThreading

__namespace__: multithreading::component::linearsolver::iterative

__parents__:

- CGLinearSolver
- Base

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
		<td>parallelInverseProduct</td>
		<td>
Parallelize the computation of the product J*M^{-1}*J^T where M is the matrix of the linear system and J is any matrix with compatible dimensions
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>iterations</td>
		<td>
Maximum number of iterations after which the iterative descent of the Conjugate Gradient must stop
		</td>
		<td>25</td>
	</tr>
	<tr>
		<td>tolerance</td>
		<td>
Desired accuracy of the Conjugate Gradient solution evaluating: |r|²/|b|² (ratio of current residual norm over initial residual norm)
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>threshold</td>
		<td>
Minimum value of the denominator (pT A p)^ in the conjugate Gradient solution
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>warmStart</td>
		<td>
Use previous solution as initial solution, which may improve the initial guess if your system is evolving smoothly
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>graph</td>
		<td>
Graph of residuals at each iteration
		</td>
		<td></td>
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

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|linearSystem|The linear system to solve|TypedMatrixLinearSystem&lt;ParallelCompressedRowSparseMatrixMat3x3d&gt;|

<!-- generate_doc -->
## ParallelCompressedRowSparseMatrixd

Templates:

- ParallelCompressedRowSparseMatrixd

__Target__: MultiThreading

__namespace__: multithreading::component::linearsolver::iterative

__parents__:

- CGLinearSolver
- Base

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
		<td>parallelInverseProduct</td>
		<td>
Parallelize the computation of the product J*M^{-1}*J^T where M is the matrix of the linear system and J is any matrix with compatible dimensions
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>iterations</td>
		<td>
Maximum number of iterations after which the iterative descent of the Conjugate Gradient must stop
		</td>
		<td>25</td>
	</tr>
	<tr>
		<td>tolerance</td>
		<td>
Desired accuracy of the Conjugate Gradient solution evaluating: |r|²/|b|² (ratio of current residual norm over initial residual norm)
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>threshold</td>
		<td>
Minimum value of the denominator (pT A p)^ in the conjugate Gradient solution
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>warmStart</td>
		<td>
Use previous solution as initial solution, which may improve the initial guess if your system is evolving smoothly
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>graph</td>
		<td>
Graph of residuals at each iteration
		</td>
		<td></td>
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

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|linearSystem|The linear system to solve|TypedMatrixLinearSystem&lt;ParallelCompressedRowSparseMatrixd&gt;|

## Examples 

ParallelCGLinearSolver.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.02" gravity="0 -10 0">
        <Node name="plugins">
            <RequiredPlugin name="MultiThreading"/> <!-- Needed to use components [ParallelCGLinearSolver] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
            <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        </Node>
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <DefaultAnimationLoop/>
    
        <Node>
            <EulerImplicitSolver name="eulerimplicit_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <ParallelCGLinearSolver template="ParallelCompressedRowSparseMatrixMat3x3d" iterations="100" tolerance="1e-20" threshold="1e-20" warmStart="1" />
            <MechanicalObject />
            <UniformMass name="mass" totalMass="320" />
            <RegularGridTopology name="grid" nx="8" ny="8" nz="40" xmin="-9" xmax="-6" ymin="0" ymax="3" zmin="0" zmax="19" />
            <BoxROI name="box" box="-10 -1 -0.0001  -5 4 0.0001"/>
            <FixedProjectiveConstraint indices="@box.indices" />
            <ParallelHexahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" method="large" />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02", gravity="0 -10 0")

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', name="MultiThreading")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Visual")

       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
       root.addObject('DefaultAnimationLoop', )

       node = root.addChild('node')

       node.addObject('EulerImplicitSolver', name="eulerimplicit_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       node.addObject('ParallelCGLinearSolver', template="ParallelCompressedRowSparseMatrixMat3x3d", iterations="100", tolerance="1e-20", threshold="1e-20", warmStart="1")
       node.addObject('MechanicalObject', )
       node.addObject('UniformMass', name="mass", totalMass="320")
       node.addObject('RegularGridTopology', name="grid", nx="8", ny="8", nz="40", xmin="-9", xmax="-6", ymin="0", ymax="3", zmin="0", zmax="19")
       node.addObject('BoxROI', name="box", box="-10 -1 -0.0001  -5 4 0.0001")
       node.addObject('FixedProjectiveConstraint', indices="@box.indices")
       node.addObject('ParallelHexahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3", method="large")
    ```

