<!-- generate_doc -->
# RotationMatrixSystem

Rotation matrix warping the main linear system.


## RotationMatrixd

Templates:

- RotationMatrixd

__Target__: Sofa.Component.LinearSolver.Preconditioner

__namespace__: sofa::component::linearsolver::preconditioner

__parents__:

- TypedMatrixLinearSystem

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
		<td>matrixSize</td>
		<td>
Size of the global matrix
		</td>
		<td></td>
	</tr>
	<tr>
		<td>enableAssembly</td>
		<td>
Allows to assemble the system matrix
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>factorizationInvalidation</td>
		<td>
Internal Data indicating a change in the matrix
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>assemblingRate</td>
		<td>
Rate of update of the preconditioner matrix
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
|mainSystem|Main assembled linear system that will be warped|BaseMatrixLinearSystem|
|rotationFinder|Link toward the rotation finder used to compute the rotation matrix|BaseRotationFinder|

