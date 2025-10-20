<!-- generate_doc -->
# UnbuiltGaussSeidelConstraintSolver

A Constraint Solver using the Linear Complementarity Problem formulation to solve Constraint based components using an Unbuilt version of the Gauss-Seidel iterative method


__Target__: Sofa.Component.Constraint.Lagrangian.Solver

__namespace__: sofa::component::constraint::lagrangian::solver

__parents__:

- UnbuiltConstraintSolver

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
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|constraintCorrections|List of constraint corrections handled by this constraint solver|BaseConstraintCorrection|

