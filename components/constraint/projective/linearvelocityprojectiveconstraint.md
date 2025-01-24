<!-- generate_doc -->
# LinearVelocityProjectiveConstraint

Impose a velocity to given DOFs (translation and rotation).


## Rigid3d

Templates:

- Rigid3d

__Target__: Sofa.Component.Constraint.Projective

__namespace__: sofa::component::constraint::projective

__parents__:

- ProjectiveConstraintSet

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
		<td>group</td>
		<td>
ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>endTime</td>
		<td>
The constraint stops acting after the given value.
Use a negative value for infinite constraints
		</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
Indices of the constrained points
		</td>
		<td></td>
	</tr>
	<tr>
		<td>keyTimes</td>
		<td>
key times for the movements
		</td>
		<td></td>
	</tr>
	<tr>
		<td>velocities</td>
		<td>
velocities corresponding to the key times
		</td>
		<td></td>
	</tr>
	<tr>
		<td>coordinates</td>
		<td>
coordinates on which to apply velocities
		</td>
		<td></td>
	</tr>
	<tr>
		<td>continueAfterEnd</td>
		<td>
If set to true then the last velocity will still be applied after all the key events
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Rigid3d&gt;|
|topology|link to the topology container|BaseMeshTopology|

<!-- generate_doc -->
## Vec1d

Templates:

- Vec1d

__Target__: Sofa.Component.Constraint.Projective

__namespace__: sofa::component::constraint::projective

__parents__:

- ProjectiveConstraintSet

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
		<td>group</td>
		<td>
ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>endTime</td>
		<td>
The constraint stops acting after the given value.
Use a negative value for infinite constraints
		</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
Indices of the constrained points
		</td>
		<td></td>
	</tr>
	<tr>
		<td>keyTimes</td>
		<td>
key times for the movements
		</td>
		<td></td>
	</tr>
	<tr>
		<td>velocities</td>
		<td>
velocities corresponding to the key times
		</td>
		<td></td>
	</tr>
	<tr>
		<td>coordinates</td>
		<td>
coordinates on which to apply velocities
		</td>
		<td></td>
	</tr>
	<tr>
		<td>continueAfterEnd</td>
		<td>
If set to true then the last velocity will still be applied after all the key events
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec1d&gt;|
|topology|link to the topology container|BaseMeshTopology|

<!-- generate_doc -->
## Vec2d

Templates:

- Vec2d

__Target__: Sofa.Component.Constraint.Projective

__namespace__: sofa::component::constraint::projective

__parents__:

- ProjectiveConstraintSet

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
		<td>group</td>
		<td>
ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>endTime</td>
		<td>
The constraint stops acting after the given value.
Use a negative value for infinite constraints
		</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
Indices of the constrained points
		</td>
		<td></td>
	</tr>
	<tr>
		<td>keyTimes</td>
		<td>
key times for the movements
		</td>
		<td></td>
	</tr>
	<tr>
		<td>velocities</td>
		<td>
velocities corresponding to the key times
		</td>
		<td></td>
	</tr>
	<tr>
		<td>coordinates</td>
		<td>
coordinates on which to apply velocities
		</td>
		<td></td>
	</tr>
	<tr>
		<td>continueAfterEnd</td>
		<td>
If set to true then the last velocity will still be applied after all the key events
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec2d&gt;|
|topology|link to the topology container|BaseMeshTopology|

<!-- generate_doc -->
## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.Constraint.Projective

__namespace__: sofa::component::constraint::projective

__parents__:

- ProjectiveConstraintSet

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
		<td>group</td>
		<td>
ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>endTime</td>
		<td>
The constraint stops acting after the given value.
Use a negative value for infinite constraints
		</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
Indices of the constrained points
		</td>
		<td></td>
	</tr>
	<tr>
		<td>keyTimes</td>
		<td>
key times for the movements
		</td>
		<td></td>
	</tr>
	<tr>
		<td>velocities</td>
		<td>
velocities corresponding to the key times
		</td>
		<td></td>
	</tr>
	<tr>
		<td>coordinates</td>
		<td>
coordinates on which to apply velocities
		</td>
		<td></td>
	</tr>
	<tr>
		<td>continueAfterEnd</td>
		<td>
If set to true then the last velocity will still be applied after all the key events
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

<!-- generate_doc -->
## Vec6d

Templates:

- Vec6d

__Target__: Sofa.Component.Constraint.Projective

__namespace__: sofa::component::constraint::projective

__parents__:

- ProjectiveConstraintSet

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
		<td>group</td>
		<td>
ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>endTime</td>
		<td>
The constraint stops acting after the given value.
Use a negative value for infinite constraints
		</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
Indices of the constrained points
		</td>
		<td></td>
	</tr>
	<tr>
		<td>keyTimes</td>
		<td>
key times for the movements
		</td>
		<td></td>
	</tr>
	<tr>
		<td>velocities</td>
		<td>
velocities corresponding to the key times
		</td>
		<td></td>
	</tr>
	<tr>
		<td>coordinates</td>
		<td>
coordinates on which to apply velocities
		</td>
		<td></td>
	</tr>
	<tr>
		<td>continueAfterEnd</td>
		<td>
If set to true then the last velocity will still be applied after all the key events
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec6d&gt;|
|topology|link to the topology container|BaseMeshTopology|

## Examples 

LinearVelocityProjectiveConstraint.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="0 -100 0" dt="0.05"  >
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [AffineMovementProjectiveConstraint] -->
        <RequiredPlugin name="MultiThreading"/> <!-- Needed to use components [ParallelBVHNarrowPhase,ParallelBruteForceBroadPhase] -->
        <RequiredPlugin name="Sofa.Component.AnimationLoop"/> <!-- Needed to use components [FreeMotionAnimationLoop] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [NewProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel,TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [LinearSolverConstraintCorrection] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Solver"/> <!-- Needed to use components [GenericConstraintSolver] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader,MeshVTKLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [EigenSimplicialLDLT,EigenSparseLU] -->
        <RequiredPlugin name="Sofa.Component.LinearSystem"/> <!-- Needed to use components [ConstantSparsityPatternSystem] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [MeshMatrixMass,UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SceneUtility"/> <!-- Needed to use components [InfoComponent] -->
        <RequiredPlugin name="Sofa.Component.Setting"/> <!-- Needed to use components [BackgroundSetting] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetTopologyContainer,TetrahedronSetTopologyModifier,TriangleSetTopologyContainer] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
    
        <!-- # Rendering settings -->
        <VisualStyle name="RenderingOptions" displayFlags="showVisualModels" />
        <BackgroundSetting color="0.8 0.8 0.8 1" />
    
    
        <!-- # Header of the simulation -->
        <FreeMotionAnimationLoop name="FreeMotionAnimationLoop" parallelODESolving="true" parallelCollisionDetectionAndFreeMotion="true"/>
        <GenericConstraintSolver maxIterations="1000" tolerance="0.001" />
    
        <Node name="Box">
            <EulerImplicitSolver name="EulerImplicitScheme" />
            <EigenSparseLU name="LUSolver" template="CompressedRowSparseMatrixd" />
            <MechanicalObject name="mstate" template="Rigid3" position="0 0 0 0 0 0 1" />
            <LinearVelocityProjectiveConstraint indices="0" keyTimes="0 2" velocities="0 0 0 0 0 0 0 0 0 0 0 0.3 " continueAfterEnd="true" />
            <UniformMass name="Mass" totalMass="0.1" />
    
            <Node name="Collision">
                <TriangleSetTopologyContainer name="FloorTopology" position="-200 -200 15    200 -200 15   200 200 15   -200 200 15   -200 -200 -15   200 -200 -15   200 200 -15   -200 200 -15" triangles="0 2 1  0 3 2   4 6 5  4 7 6   0 1 4  5 4 1   3 6 2  3 7 6   1 2 6  1 6 5  0 4 3  3 4 7"/>
                <MechanicalObject name="CollisionDOF" template="Vec3"/>
                <TriangleCollisionModel  selfCollision="0" topology="@FloorTopology" simulated="0" group="1 2" proximity="3" />
                <RigidMapping name="MappingCollision" input="@../mstate" output="@CollisionDOF" globalToLocalCoords="true"/>
    
            </Node>
    
            <Node name="Visu">
                <OglModel name="VisualModel" color="0.5 0.5 0.5 0.2" src="@../Collision/FloorTopology" />
                <RigidMapping name="MappingCollision" input="@../mstate" output="@VisualModel" globalToLocalCoords="true"/>
            </Node>
            <LinearSolverConstraintCorrection/>
        </Node>
    
    
    
    
    
    
    </Node>
    
    
    
    
    
    

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -100 0", dt="0.05")

       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="MultiThreading")
       root.addObject('RequiredPlugin', name="Sofa.Component.AnimationLoop")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Solver")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSystem")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SceneUtility")
       root.addObject('RequiredPlugin', name="Sofa.Component.Setting")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', name="RenderingOptions", displayFlags="showVisualModels")
       root.addObject('BackgroundSetting', color="0.8 0.8 0.8 1")
       root.addObject('FreeMotionAnimationLoop', name="FreeMotionAnimationLoop", parallelODESolving="true", parallelCollisionDetectionAndFreeMotion="true")
       root.addObject('GenericConstraintSolver', maxIterations="1000", tolerance="0.001")

       box = root.addChild('Box')

       box.addObject('EulerImplicitSolver', name="EulerImplicitScheme")
       box.addObject('EigenSparseLU', name="LUSolver", template="CompressedRowSparseMatrixd")
       box.addObject('MechanicalObject', name="mstate", template="Rigid3", position="0 0 0 0 0 0 1")
       box.addObject('LinearVelocityProjectiveConstraint', indices="0", keyTimes="0 2", velocities="0 0 0 0 0 0 0 0 0 0 0 0.3 ", continueAfterEnd="true")
       box.addObject('UniformMass', name="Mass", totalMass="0.1")

       collision = Box.addChild('Collision')

       collision.addObject('TriangleSetTopologyContainer', name="FloorTopology", position="-200 -200 15    200 -200 15   200 200 15   -200 200 15   -200 -200 -15   200 -200 -15   200 200 -15   -200 200 -15", triangles="0 2 1  0 3 2   4 6 5  4 7 6   0 1 4  5 4 1   3 6 2  3 7 6   1 2 6  1 6 5  0 4 3  3 4 7")
       collision.addObject('MechanicalObject', name="CollisionDOF", template="Vec3")
       collision.addObject('TriangleCollisionModel', selfCollision="0", topology="@FloorTopology", simulated="0", group="1 2", proximity="3")
       collision.addObject('RigidMapping', name="MappingCollision", input="@../mstate", output="@CollisionDOF", globalToLocalCoords="true")

       visu = Box.addChild('Visu')

       visu.addObject('OglModel', name="VisualModel", color="0.5 0.5 0.5 0.2", src="@../Collision/FloorTopology")
       visu.addObject('RigidMapping', name="MappingCollision", input="@../mstate", output="@VisualModel", globalToLocalCoords="true")

       box.addObject('LinearSolverConstraintCorrection', )
    ```

