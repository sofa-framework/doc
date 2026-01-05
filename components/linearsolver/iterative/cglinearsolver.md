---
title: CGLinearSolver
---

CGLinearSolver  
==============

This component belongs to the category of [LinearSolver](../../../../simulation-principles/system-resolution/linear-solver/). The role of the CGLinearSolver is to solve the linear system $\mathbf{A}x=b$ without any _a priori_ on this system.

In SOFA, the CGLinearSolver follows the well-known [conjugate gradient method](https://en.wikipedia.org/wiki/Conjugate_gradient_method), which consists in iteratively solving $r=b-\mathbf{A}x^k$ where *r* is known as the residual. This residual will be used to compute mutually conjugate vectors *p* (see the sequence diagram below) which will be used as a basis to find a new approximated solution $x^{k+1}$.

**Note**: the CGLinearSolver in SOFA assumes that the right hand side (RHS) vector *b* is already computed. The computation of *b* is usually called in the [integration scheme](../../../../simulation-principles/system-resolution/integration-scheme/) through the function `computeForce()`.



Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/CGLinearSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/CGLinearSolver.png?raw=true" title="Flow diagram for the CGLinearSolver"/></a>


Usage
-----

The CGLinearSolver **requires** the use (above in the scene graph) of an integration scheme, and (below in the scene graph) of a MechanicalObject storing the state information that the CGLinearSolver will access.

When using a CGLinearSolver, make sure you carefully chose the value of the free data field iterations, tolerance and threshold. Both tolerance and threshold data must be chosen in accordance with the dimension of the degrees of freedom (DOFs). Usually, the value of these two data is close to the square of the expected error on the DOFs.

Remember that when using an iterative linear solver like the CGLinearSolver, no exact solution can be found. The accuracy of your solution will always depend on the conditioning of your system and your input data (iterations, tolerance and threshold).

<!-- automatically generated doc START -->
<!-- generate_doc -->

Linear system solver using the conjugate gradient iterative algorithm


## CompressedRowSparseMatrixMat2x2d

Templates:

- CompressedRowSparseMatrixMat2x2d

__Target__: Sofa.Component.LinearSolver.Iterative

__namespace__: sofa::component::linearsolver::iterative

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
		<td>factorizationInvalidation</td>
		<td>
Internal data for the detection of cache invalidation of the matrix factorization
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
		<td>threshold</td>
		<td>
Minimum value of the denominator (pT A p)^ in the conjugate Gradient solution
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>warmStart</td>
		<td>
Use previous solution as initial solution, which may improve the initial guess if your system is evolving smoothly
		</td>
		<td>0</td>
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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|linearSystem|The linear system to solve|TypedMatrixLinearSystem&lt;CompressedRowSparseMatrixMat2x2d&gt;|

<!-- generate_doc -->
## CompressedRowSparseMatrixMat3x3d

Templates:

- CompressedRowSparseMatrixMat3x3d

__Target__: Sofa.Component.LinearSolver.Iterative

__namespace__: sofa::component::linearsolver::iterative

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
		<td>factorizationInvalidation</td>
		<td>
Internal data for the detection of cache invalidation of the matrix factorization
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
		<td>threshold</td>
		<td>
Minimum value of the denominator (pT A p)^ in the conjugate Gradient solution
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>warmStart</td>
		<td>
Use previous solution as initial solution, which may improve the initial guess if your system is evolving smoothly
		</td>
		<td>0</td>
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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|linearSystem|The linear system to solve|TypedMatrixLinearSystem&lt;CompressedRowSparseMatrixMat3x3d&gt;|

<!-- generate_doc -->
## CompressedRowSparseMatrixMat4x4d

Templates:

- CompressedRowSparseMatrixMat4x4d

__Target__: Sofa.Component.LinearSolver.Iterative

__namespace__: sofa::component::linearsolver::iterative

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
		<td>factorizationInvalidation</td>
		<td>
Internal data for the detection of cache invalidation of the matrix factorization
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
		<td>threshold</td>
		<td>
Minimum value of the denominator (pT A p)^ in the conjugate Gradient solution
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>warmStart</td>
		<td>
Use previous solution as initial solution, which may improve the initial guess if your system is evolving smoothly
		</td>
		<td>0</td>
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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|linearSystem|The linear system to solve|TypedMatrixLinearSystem&lt;CompressedRowSparseMatrixMat4x4d&gt;|

<!-- generate_doc -->
## CompressedRowSparseMatrixMat6x6d

Templates:

- CompressedRowSparseMatrixMat6x6d

__Target__: Sofa.Component.LinearSolver.Iterative

__namespace__: sofa::component::linearsolver::iterative

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
		<td>factorizationInvalidation</td>
		<td>
Internal data for the detection of cache invalidation of the matrix factorization
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
		<td>threshold</td>
		<td>
Minimum value of the denominator (pT A p)^ in the conjugate Gradient solution
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>warmStart</td>
		<td>
Use previous solution as initial solution, which may improve the initial guess if your system is evolving smoothly
		</td>
		<td>0</td>
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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|linearSystem|The linear system to solve|TypedMatrixLinearSystem&lt;CompressedRowSparseMatrixMat6x6d&gt;|

<!-- generate_doc -->
## CompressedRowSparseMatrixMat8x8d

Templates:

- CompressedRowSparseMatrixMat8x8d

__Target__: Sofa.Component.LinearSolver.Iterative

__namespace__: sofa::component::linearsolver::iterative

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
		<td>factorizationInvalidation</td>
		<td>
Internal data for the detection of cache invalidation of the matrix factorization
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
		<td>threshold</td>
		<td>
Minimum value of the denominator (pT A p)^ in the conjugate Gradient solution
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>warmStart</td>
		<td>
Use previous solution as initial solution, which may improve the initial guess if your system is evolving smoothly
		</td>
		<td>0</td>
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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|linearSystem|The linear system to solve|TypedMatrixLinearSystem&lt;CompressedRowSparseMatrixMat8x8d&gt;|

<!-- generate_doc -->
## CompressedRowSparseMatrixd

Templates:

- CompressedRowSparseMatrixd

__Target__: Sofa.Component.LinearSolver.Iterative

__namespace__: sofa::component::linearsolver::iterative

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
		<td>factorizationInvalidation</td>
		<td>
Internal data for the detection of cache invalidation of the matrix factorization
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
		<td>threshold</td>
		<td>
Minimum value of the denominator (pT A p)^ in the conjugate Gradient solution
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>warmStart</td>
		<td>
Use previous solution as initial solution, which may improve the initial guess if your system is evolving smoothly
		</td>
		<td>0</td>
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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|linearSystem|The linear system to solve|TypedMatrixLinearSystem&lt;CompressedRowSparseMatrixd&gt;|

<!-- generate_doc -->
## FullMatrix

Templates:

- FullMatrix

__Target__: Sofa.Component.LinearSolver.Iterative

__namespace__: sofa::component::linearsolver::iterative

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
		<td>factorizationInvalidation</td>
		<td>
Internal data for the detection of cache invalidation of the matrix factorization
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
		<td>threshold</td>
		<td>
Minimum value of the denominator (pT A p)^ in the conjugate Gradient solution
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>warmStart</td>
		<td>
Use previous solution as initial solution, which may improve the initial guess if your system is evolving smoothly
		</td>
		<td>0</td>
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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|linearSystem|The linear system to solve|TypedMatrixLinearSystem&lt;FullMatrix&gt;|

<!-- generate_doc -->
## GraphScattered

Templates:

- GraphScattered

__Target__: Sofa.Component.LinearSolver.Iterative

__namespace__: sofa::component::linearsolver::iterative

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
		<td>factorizationInvalidation</td>
		<td>
Internal data for the detection of cache invalidation of the matrix factorization
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
		<td>threshold</td>
		<td>
Minimum value of the denominator (pT A p)^ in the conjugate Gradient solution
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>warmStart</td>
		<td>
Use previous solution as initial solution, which may improve the initial guess if your system is evolving smoothly
		</td>
		<td>0</td>
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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|linearSystem|The linear system to solve|TypedMatrixLinearSystem&lt;GraphScattered&gt;|

<!-- generate_doc -->
## SparseMatrix

Templates:

- SparseMatrix

__Target__: Sofa.Component.LinearSolver.Iterative

__namespace__: sofa::component::linearsolver::iterative

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
		<td>factorizationInvalidation</td>
		<td>
Internal data for the detection of cache invalidation of the matrix factorization
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
		<td>threshold</td>
		<td>
Minimum value of the denominator (pT A p)^ in the conjugate Gradient solution
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>warmStart</td>
		<td>
Use previous solution as initial solution, which may improve the initial guess if your system is evolving smoothly
		</td>
		<td>0</td>
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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|linearSystem|The linear system to solve|TypedMatrixLinearSystem&lt;SparseMatrix&gt;|

## Examples 

CGLinearSolver.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.02" gravity="0 -10 0">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <DefaultAnimationLoop/>
        
        <Node>
            <EulerImplicitSolver name="eulerimplicit_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="100" tolerance="1e-20" threshold="1e-20" warmStart="1" />
            <MechanicalObject />
            <UniformMass vertexMass="1" />
            <RegularGridTopology nx="4" ny="4" nz="4" xmin="-9" xmax="-6" ymin="0" ymax="3" zmin="0" zmax="3" />
            <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15" />
            <HexahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" method="large" />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02", gravity="0 -10 0")

       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
       root.addObject('DefaultAnimationLoop', )

       node = root.addChild('node')

       node.addObject('EulerImplicitSolver', name="eulerimplicit_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       node.addObject('CGLinearSolver', iterations="100", tolerance="1e-20", threshold="1e-20", warmStart="1")
       node.addObject('MechanicalObject', )
       node.addObject('UniformMass', vertexMass="1")
       node.addObject('RegularGridTopology', nx="4", ny="4", nz="4", xmin="-9", xmax="-6", ymin="0", ymax="3", zmin="0", zmax="3")
       node.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15")
       node.addObject('HexahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3", method="large")
    ```


<!-- automatically generated doc END -->
