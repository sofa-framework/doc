<!-- generate_doc -->
# LinearSolverConstraintCorrection

Component computing constraint forces within a simulated body using the compliance method.


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
		<td>wire_optimization</td>
		<td>
constraints are reordered along a wire-like topology (from tip to base)
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
|constraintSolvers|Constraint solvers using this constraint correction|ConstraintSolver|
|linearSolver|Link towards the linear solver used to compute the compliance matrix, requiring the inverse of the linear system matrix|LinearSolver|
|ODESolver|Link towards the ODE solver used to recover the integration factors|OdeSolver|

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
		<td>wire_optimization</td>
		<td>
constraints are reordered along a wire-like topology (from tip to base)
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
|constraintSolvers|Constraint solvers using this constraint correction|ConstraintSolver|
|linearSolver|Link towards the linear solver used to compute the compliance matrix, requiring the inverse of the linear system matrix|LinearSolver|
|ODESolver|Link towards the ODE solver used to recover the integration factors|OdeSolver|

<!-- generate_doc -->
## Vec2d

Templates:

- Vec2d

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
		<td>wire_optimization</td>
		<td>
constraints are reordered along a wire-like topology (from tip to base)
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
|constraintSolvers|Constraint solvers using this constraint correction|ConstraintSolver|
|linearSolver|Link towards the linear solver used to compute the compliance matrix, requiring the inverse of the linear system matrix|LinearSolver|
|ODESolver|Link towards the ODE solver used to recover the integration factors|OdeSolver|

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
		<td>wire_optimization</td>
		<td>
constraints are reordered along a wire-like topology (from tip to base)
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
|constraintSolvers|Constraint solvers using this constraint correction|ConstraintSolver|
|linearSolver|Link towards the linear solver used to compute the compliance matrix, requiring the inverse of the linear system matrix|LinearSolver|
|ODESolver|Link towards the ODE solver used to recover the integration factors|OdeSolver|

