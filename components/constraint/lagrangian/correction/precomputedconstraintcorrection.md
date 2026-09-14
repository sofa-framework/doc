<!-- generate_doc -->
# PrecomputedConstraintCorrection

Component precomputing constraint forces within a simulated body using the compliance method. It approximates the compliance matrix by a precomputed matrix inverse. The approximation can be updated based on the rotation of elements.


## Rigid3d

Templates:

- Rigid3d

__Target__: Sofa.Component.Constraint.Lagrangian.Correction

__namespace__: sofa::component::constraint::lagrangian::correction

__parents__:

- ConstraintCorrection

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
		<td>rotations</td>
		<td>
Project the precomputed matrix with a rotation matrix
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>restDeformations</td>
		<td>

		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>recompute</td>
		<td>
if true, always recompute the compliance
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>regularizationTerm</td>
		<td>
Add regularization factor times the identity matrix to the compliance W when solving constraints
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>debugViewFrameScale</td>
		<td>
Scale on computed node's frame
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>fileCompliance</td>
		<td>
Precomputed compliance matrix data file
		</td>
		<td></td>
	</tr>
	<tr>
		<td>fileDir</td>
		<td>
If not empty, the compliance will be saved in this repertory
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Rigid3d&gt;|
|constraintSolvers|Constraint solvers using this constraint correction|ConstraintSolver|
|ODESolver|Link towards the ODE solver used during the compliance precomputation. If unset, the first OdeSolver in the current context is used.|EulerImplicitSolver|
|linearSolver|Link towards the linear solver used during the compliance precomputation. If unset, the first LinearSolver in the current context is used.|LinearSolver|

<!-- generate_doc -->
## Vec1d

Templates:

- Vec1d

__Target__: Sofa.Component.Constraint.Lagrangian.Correction

__namespace__: sofa::component::constraint::lagrangian::correction

__parents__:

- ConstraintCorrection

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
		<td>rotations</td>
		<td>
Project the precomputed matrix with a rotation matrix
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>restDeformations</td>
		<td>

		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>recompute</td>
		<td>
if true, always recompute the compliance
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>regularizationTerm</td>
		<td>
Add regularization factor times the identity matrix to the compliance W when solving constraints
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>debugViewFrameScale</td>
		<td>
Scale on computed node's frame
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>fileCompliance</td>
		<td>
Precomputed compliance matrix data file
		</td>
		<td></td>
	</tr>
	<tr>
		<td>fileDir</td>
		<td>
If not empty, the compliance will be saved in this repertory
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
|constraintSolvers|Constraint solvers using this constraint correction|ConstraintSolver|
|ODESolver|Link towards the ODE solver used during the compliance precomputation. If unset, the first OdeSolver in the current context is used.|EulerImplicitSolver|
|linearSolver|Link towards the linear solver used during the compliance precomputation. If unset, the first LinearSolver in the current context is used.|LinearSolver|

<!-- generate_doc -->
## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.Constraint.Lagrangian.Correction

__namespace__: sofa::component::constraint::lagrangian::correction

__parents__:

- ConstraintCorrection

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
		<td>rotations</td>
		<td>
Project the precomputed matrix with a rotation matrix
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>restDeformations</td>
		<td>

		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>recompute</td>
		<td>
if true, always recompute the compliance
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>regularizationTerm</td>
		<td>
Add regularization factor times the identity matrix to the compliance W when solving constraints
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>debugViewFrameScale</td>
		<td>
Scale on computed node's frame
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>fileCompliance</td>
		<td>
Precomputed compliance matrix data file
		</td>
		<td></td>
	</tr>
	<tr>
		<td>fileDir</td>
		<td>
If not empty, the compliance will be saved in this repertory
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
|constraintSolvers|Constraint solvers using this constraint correction|ConstraintSolver|
|ODESolver|Link towards the ODE solver used during the compliance precomputation. If unset, the first OdeSolver in the current context is used.|EulerImplicitSolver|
|linearSolver|Link towards the linear solver used during the compliance precomputation. If unset, the first LinearSolver in the current context is used.|LinearSolver|

## Examples 

PrecomputedConstraintCorrection.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.010" gravity="0 -10 0">
        <Node name="RequiredPlugins">
            <RequiredPlugin pluginName="Sofa.Component.AnimationLoop"/>
            <RequiredPlugin pluginName="Sofa.Component.Collision.Detection.Algorithm"/>
            <RequiredPlugin pluginName="Sofa.Component.Collision.Detection.Intersection"/>
            <RequiredPlugin pluginName="Sofa.Component.Collision.Geometry"/>
            <RequiredPlugin pluginName="Sofa.Component.Collision.Response.Contact"/>
            <RequiredPlugin pluginName="Sofa.Component.Constraint.Lagrangian.Correction"/>
            <RequiredPlugin pluginName="Sofa.Component.Constraint.Lagrangian.Solver"/>
            <RequiredPlugin pluginName="Sofa.Component.Constraint.Projective"/>
            <RequiredPlugin pluginName="Sofa.Component.Engine.Select"/>
            <RequiredPlugin pluginName="Sofa.Component.LinearSolver.Iterative"/>
            <RequiredPlugin pluginName="Sofa.Component.Mass"/>
            <RequiredPlugin pluginName="Sofa.Component.MechanicalLoad"/>
            <RequiredPlugin pluginName="Sofa.Component.ODESolver.Backward"/>
            <RequiredPlugin pluginName="Sofa.Component.SolidMechanics.FEM.Elastic"/>
            <RequiredPlugin pluginName="Sofa.Component.StateContainer"/>
            <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Grid"/>
            <RequiredPlugin pluginName="Sofa.Component.Visual"/>
            <RequiredPlugin pluginName="Sofa.Component.LinearSolver.Preconditioner"/>
            <RequiredPlugin pluginName="Sofa.Component.LinearSystem"/>
        </Node>
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields showVisualModels showCollisionModels" />
    
        <FreeMotionAnimationLoop />
        <BlockGaussSeidelConstraintSolver tolerance="1e-6" maxIterations="1000" />
    
        <CollisionPipeline/>
        <BruteForceBroadPhase />
        <BVHNarrowPhase />
        <NewProximityIntersection name="proximity" alarmDistance="0.3" contactDistance="0.1"/>
        <CollisionResponse name="response" response="FrictionContactConstraint"/>
    
        <Node name="BeamPrecomputed">
            <Visual3DText text="PrecomputedConstraintCorrection" position="0 3 6" scale="0.4" color="0.3 0.7 1 1" />
            <EulerImplicitSolver name="odeSolver" rayleighStiffness="0.01" rayleighMass="0.01" linearSolver="@linearSolver"/>
    
            <MatrixLinearSystem name="precondSystem" template="CompressedRowSparseMatrixd"/>
            <SSORPreconditioner name="precond" linearSystem="@precondSystem"/>
    
            <PreconditionedMatrixFreeSystem name="solverSystem" preconditionerSystem="@precondSystem"/>
            <PCGLinearSolver name="linearSolver" iterations="200" tolerance="1e-6" linearSystem="@solverSystem" preconditioner="@precond"/>
    
            <RegularGridTopology name="grid" n="10 3 3" min="0 0 5" max="10 2 7" />
            <MechanicalObject name="dofs" />
    
            <NodalMassDensity name="rho" property="1"/>
            <FEMMass template="Vec3,Hexahedron" nodalMassDensity="@rho" />
            <CorotationalFEMForceField template="Vec3,Hexahedron" name="FEM" youngModulus="1e4" poissonRatio="0.3" />
    
            <BoxROI name="boxFixed" box="-0.1 -0.1 4.9  0.1 2.1 7.1" drawBoxes="true" />
            <FixedProjectiveConstraint indices="@boxFixed.indices" />
    
            <PointCollisionModel />
    
            <PrecomputedConstraintCorrection recompute="true" printLog="true" ODESolver="@odeSolver" linearSolver="@linearSolver"/>
        </Node>
    
        <Node name="BeamLinearSolver">
            <Visual3DText text="LinearSolverConstraintCorrection" position="0 3 12" scale="0.4" color="0.3 0.7 1 1" />
            <EulerImplicitSolver name="odeSolver" rayleighStiffness="0.01" rayleighMass="0.01" linearSolver="@linearSolver"/>
    
            <MatrixLinearSystem name="precondSystem" template="CompressedRowSparseMatrixd"/>
            <SSORPreconditioner name="precond" linearSystem="@precondSystem"/>
    
            <PreconditionedMatrixFreeSystem name="solverSystem" preconditionerSystem="@precondSystem"/>
            <PCGLinearSolver name="linearSolver" iterations="200" tolerance="1e-6" linearSystem="@solverSystem" preconditioner="@precond"/>
    
            <RegularGridTopology name="grid" n="10 3 3" min="0 0 9" max="10 2 11" />
            <MechanicalObject name="dofs" />
    
            <NodalMassDensity name="rho" property="1"/>
            <FEMMass template="Vec3,Hexahedron" nodalMassDensity="@rho" />
            <CorotationalFEMForceField template="Vec3,Hexahedron" name="FEM" youngModulus="1e4" poissonRatio="0.3" />
    
            <BoxROI name="boxFixed" box="-0.1 -0.1 8.9  0.1 2.1 11.1" drawBoxes="true" />
            <FixedProjectiveConstraint indices="@boxFixed.indices" />
    
            <PointCollisionModel />
    
            <LinearSolverConstraintCorrection ODESolver="@odeSolver" linearSolver="@precond"/>
        </Node>
    
        <Node name="Floor">
            <RegularGridTopology name="floor" n="5 1 5" min="5 -3 3.5" max="13 -3 11.5" />
            <MechanicalObject name="dofs" />
            <TriangleCollisionModel simulated="0" moving="0" />
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.010", gravity="0 -10 0")

       required_plugins = root.addChild('RequiredPlugins')

       required_plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.AnimationLoop")
       required_plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Detection.Algorithm")
       required_plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Detection.Intersection")
       required_plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Geometry")
       required_plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Response.Contact")
       required_plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Constraint.Lagrangian.Correction")
       required_plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Constraint.Lagrangian.Solver")
       required_plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Constraint.Projective")
       required_plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Engine.Select")
       required_plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSolver.Iterative")
       required_plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Mass")
       required_plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.MechanicalLoad")
       required_plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.ODESolver.Backward")
       required_plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.SolidMechanics.FEM.Elastic")
       required_plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.StateContainer")
       required_plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Grid")
       required_plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Visual")
       required_plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSolver.Preconditioner")
       required_plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSystem")

       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields showVisualModels showCollisionModels")
       root.addObject('FreeMotionAnimationLoop', )
       root.addObject('BlockGaussSeidelConstraintSolver', tolerance="1e-6", maxIterations="1000")
       root.addObject('CollisionPipeline', )
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('NewProximityIntersection', name="proximity", alarmDistance="0.3", contactDistance="0.1")
       root.addObject('CollisionResponse', name="response", response="FrictionContactConstraint")

       beam_precomputed = root.addChild('BeamPrecomputed')

       beam_precomputed.addObject('Visual3DText', text="PrecomputedConstraintCorrection", position="0 3 6", scale="0.4", color="0.3 0.7 1 1")
       beam_precomputed.addObject('EulerImplicitSolver', name="odeSolver", rayleighStiffness="0.01", rayleighMass="0.01", linearSolver="@linearSolver")
       beam_precomputed.addObject('MatrixLinearSystem', name="precondSystem", template="CompressedRowSparseMatrixd")
       beam_precomputed.addObject('SSORPreconditioner', name="precond", linearSystem="@precondSystem")
       beam_precomputed.addObject('PreconditionedMatrixFreeSystem', name="solverSystem", preconditionerSystem="@precondSystem")
       beam_precomputed.addObject('PCGLinearSolver', name="linearSolver", iterations="200", tolerance="1e-6", linearSystem="@solverSystem", preconditioner="@precond")
       beam_precomputed.addObject('RegularGridTopology', name="grid", n="10 3 3", min="0 0 5", max="10 2 7")
       beam_precomputed.addObject('MechanicalObject', name="dofs")
       beam_precomputed.addObject('NodalMassDensity', name="rho", property="1")
       beam_precomputed.addObject('FEMMass', template="Vec3,Hexahedron", nodalMassDensity="@rho")
       beam_precomputed.addObject('CorotationalFEMForceField', template="Vec3,Hexahedron", name="FEM", youngModulus="1e4", poissonRatio="0.3")
       beam_precomputed.addObject('BoxROI', name="boxFixed", box="-0.1 -0.1 4.9  0.1 2.1 7.1", drawBoxes="true")
       beam_precomputed.addObject('FixedProjectiveConstraint', indices="@boxFixed.indices")
       beam_precomputed.addObject('PointCollisionModel', )
       beam_precomputed.addObject('PrecomputedConstraintCorrection', recompute="true", printLog="true", ODESolver="@odeSolver", linearSolver="@linearSolver")

       beam_linear_solver = root.addChild('BeamLinearSolver')

       beam_linear_solver.addObject('Visual3DText', text="LinearSolverConstraintCorrection", position="0 3 12", scale="0.4", color="0.3 0.7 1 1")
       beam_linear_solver.addObject('EulerImplicitSolver', name="odeSolver", rayleighStiffness="0.01", rayleighMass="0.01", linearSolver="@linearSolver")
       beam_linear_solver.addObject('MatrixLinearSystem', name="precondSystem", template="CompressedRowSparseMatrixd")
       beam_linear_solver.addObject('SSORPreconditioner', name="precond", linearSystem="@precondSystem")
       beam_linear_solver.addObject('PreconditionedMatrixFreeSystem', name="solverSystem", preconditionerSystem="@precondSystem")
       beam_linear_solver.addObject('PCGLinearSolver', name="linearSolver", iterations="200", tolerance="1e-6", linearSystem="@solverSystem", preconditioner="@precond")
       beam_linear_solver.addObject('RegularGridTopology', name="grid", n="10 3 3", min="0 0 9", max="10 2 11")
       beam_linear_solver.addObject('MechanicalObject', name="dofs")
       beam_linear_solver.addObject('NodalMassDensity', name="rho", property="1")
       beam_linear_solver.addObject('FEMMass', template="Vec3,Hexahedron", nodalMassDensity="@rho")
       beam_linear_solver.addObject('CorotationalFEMForceField', template="Vec3,Hexahedron", name="FEM", youngModulus="1e4", poissonRatio="0.3")
       beam_linear_solver.addObject('BoxROI', name="boxFixed", box="-0.1 -0.1 8.9  0.1 2.1 11.1", drawBoxes="true")
       beam_linear_solver.addObject('FixedProjectiveConstraint', indices="@boxFixed.indices")
       beam_linear_solver.addObject('PointCollisionModel', )
       beam_linear_solver.addObject('LinearSolverConstraintCorrection', ODESolver="@odeSolver", linearSolver="@precond")

       floor = root.addChild('Floor')

       floor.addObject('RegularGridTopology', name="floor", n="5 1 5", min="5 -3 3.5", max="13 -3 11.5")
       floor.addObject('MechanicalObject', name="dofs")
       floor.addObject('TriangleCollisionModel', simulated="0", moving="0")
    ```

