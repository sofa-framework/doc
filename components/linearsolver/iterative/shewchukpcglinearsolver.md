# ShewchukPCGLinearSolver

Linear system solver using the conjugate gradient iterative algorithm


__Templates__:

- `#!c++ GraphScattered`

__Target__: `Sofa.Component.LinearSolver.Iterative`

__namespace__: `#!c++ sofa::component::linearsolver::iterative`

__parents__: 

- `#!c++ MatrixLinearSolver`

__categories__: 

- LinearSolver

Data: 

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
		<td>use_precond</td>
		<td>
Use a preconditioner
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>update_step</td>
		<td>
Number of steps before the next refresh of precondtioners
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>build_precond</td>
		<td>
Build the preconditioners, if false build the preconditioner only at the initial step
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>graph</td>
		<td>
Graph of residuals at each iteration
</td>
		<td></td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|linearSystem|The linear system to solve|
|preconditioner|Link towards the linear solver used to precondition the conjugate gradient|



