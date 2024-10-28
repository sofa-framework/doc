<!-- generate_doc -->
# LCPConstraintSolver

A Constraint Solver using the Linear Complementarity Problem formulation to solve BaseConstraint based components.


__Target__: Sofa.Component.Constraint.Lagrangian.Solver

__namespace__: sofa::component::constraint::lagrangian::solver

__parents__:

- ConstraintSolverImpl

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
		<td>displayDebug</td>
		<td>
Display debug information.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>initial_guess</td>
		<td>
activate LCP results history to improve its resolution performances.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>build_lcp</td>
		<td>
LCP is not fully built to increase performance in some case.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>tolerance</td>
		<td>
residual error threshold for termination of the Gauss-Seidel algorithm
		</td>
		<td>0.001</td>
	</tr>
	<tr>
		<td>maxIt</td>
		<td>
maximal number of iterations of the Gauss-Seidel algorithm
		</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>mu</td>
		<td>
Friction coefficient
		</td>
		<td>0.6</td>
	</tr>
	<tr>
		<td>minW</td>
		<td>
If not zero, constraints whose self-compliance (i.e. the corresponding value on the diagonal of W) is smaller than this threshold will be ignored
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>maxF</td>
		<td>
If not zero, constraints whose response force becomes larger than this threshold will be ignored
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>multi_grid</td>
		<td>
activate multi_grid resolution (NOT STABLE YET)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>multi_grid_levels</td>
		<td>
if multi_grid is active: how many levels to create (>=2)
		</td>
		<td>2</td>
	</tr>
	<tr>
		<td>merge_method</td>
		<td>
if multi_grid is active: which method to use to merge constraints (0 = compliance-based, 1 = spatial coordinates)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>merge_spatial_step</td>
		<td>
if merge_method is 1: grid size reduction between multigrid levels
		</td>
		<td>2</td>
	</tr>
	<tr>
		<td>merge_local_levels</td>
		<td>
if merge_method is 1: up to the specified level of the multigrid, constraints are grouped locally, i.e. separately within each contact pairs, while on upper levels they are grouped globally independently of contact pairs.
		</td>
		<td>2</td>
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
		<td>group</td>
		<td>
list of ID of groups of constraints to be handled by this solver.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>graph</td>
		<td>
Graph of residuals at each iteration
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showLevels</td>
		<td>
Number of constraint levels to display
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showCellWidth</td>
		<td>
Distance between each constraint cells
		</td>
		<td></td>
	</tr>
	<tr>
		<td>showTranslation</td>
		<td>
Position of the first cell
		</td>
		<td></td>
	</tr>
	<tr>
		<td>showLevelTranslation</td>
		<td>
Translation between levels
		</td>
		<td></td>
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

