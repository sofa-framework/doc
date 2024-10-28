<!-- generate_doc -->
# PrecomputedWarpPreconditioner

Linear system solver based on a precomputed inverse matrix, wrapped by a per-node rotation matrix.


## CompressedRowSparseMatrixd

Templates:

- CompressedRowSparseMatrixd

__Target__: Sofa.Component.LinearSolver.Preconditioner

__namespace__: sofa::component::linearsolver::preconditioner

__parents__:

- MatrixLinearSolver

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
		<td>jmjt_twostep</td>
		<td>
Use two step algorithm to compute JMinvJt
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>use_file</td>
		<td>
Dump system matrix in a file
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>share_matrix</td>
		<td>
Share the compliance matrix in memory if they are related to the same file (WARNING: might require to reload Sofa when opening a new scene...)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>use_rotations</td>
		<td>
Use Rotations around the preconditioner
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>draw_rotations_scale</td>
		<td>
Scale rotations in draw function
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
|linearSystem|The linear system to solve|TypedMatrixLinearSystem&lt;CompressedRowSparseMatrixd&gt;|
|linearSolver|Link towards the linear solver used to precompute the first matrix|LinearSolver|

