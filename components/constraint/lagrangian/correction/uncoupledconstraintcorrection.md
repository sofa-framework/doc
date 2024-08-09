<!-- generate_doc -->
# UncoupledConstraintCorrection

Component computing constraint forces within a simulated body using the compliance method.


Templates:

- Rigid3d
- Vec1d
- Vec2d
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
		<td>compliance</td>
		<td>
Compliance value on each dof. If Rigid compliance (7 values): 1st value for translations, 6 others for upper-triangular part of symmetric 3x3 rotation compliance matrix
		</td>
		<td></td>
	</tr>
	<tr>
		<td>defaultCompliance</td>
		<td>
Default compliance value for new dof or if all should have the same (in which case compliance vector should be empty)
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>verbose</td>
		<td>
Dump the constraint matrix at each iteration
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>correctionVelocityFactor</td>
		<td>
Factor applied to the constraint forces when correcting the velocities
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>correctionPositionFactor</td>
		<td>
Factor applied to the constraint forces when correcting the positions
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>useOdeSolverIntegrationFactors</td>
		<td>
Use odeSolver integration factors instead of correctionVelocityFactor and correctionPositionFactor
		</td>
		<td>1</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|constraintSolvers|Constraint solvers using this constraint correction|ConstraintSolver|
|topology|link to the topology container|BaseMeshTopology|

