<!-- generate_doc -->
# StaticEquilibriumIntegrationScheme

Time integrator finding static equilibrium.


__Target__: Sofa.Component.IntegrationScheme.Backward

__namespace__: sofa::component::integrationscheme::backward

__parents__:

- ImplicitIntegrationScheme

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
	<tr>
		<td>maxNbIterationsNewton</td>
		<td>
Maximum number of iteration for the Newton algorithm
		</td>
		<td>10</td>
	</tr>
	<tr>
		<td>maxNbIterationsLineSearch</td>
		<td>
Maximum number of iteration for the backtracking linesearch algorithm
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>newtonStepSize</td>
		<td>
Size of the first newton step before the linesearch
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>lineSearchReductionRate</td>
		<td>
Taken in [0,1[ representing the fraction of diminution of the step done in the backtracking line search (if set to 0.3, the first line search will reduce the step from 1.0 to 0.7)
		</td>
		<td>0.5</td>
	</tr>
	<tr>
		<td>lineSearchArmijoFactor</td>
		<td>
Taken in [0,1[ it represents a tolerance on the residue in term of the linear approximation. e.g., for a value of 0.01, it means we want the solution to decrease the residue as much as 0.01 times the linear approximation in the same direction.
		</td>
		<td>0.001</td>
	</tr>
	<tr>
		<td>residueThreshold</td>
		<td>
Threshold under which, the residue is considered to be sufficiently low. Newton algorithm will stop after reaching a lower value
		</td>
		<td>1e-09</td>
	</tr>
	<tr>
		<td>currentResidue</td>
		<td>
Current value of the residue
		</td>
		<td></td>
	</tr>
	<tr>
		<td>alwaysAdvanceNewton</td>
		<td>
Even if the linesearch didn't find a better solution than the current one, take the best one along the path that is not the current guess.
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
|linearSolver|Linear solver used by this component|LinearSolver|

