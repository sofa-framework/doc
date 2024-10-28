---
title: SparseLDLSolver
---

SparseLDLSolver
===============

This component belongs to the category of [LinearSolver](../../../../simulation-principles/system-resolution/linear-solver/). The role of the SparseLDLSolver is to solve the linear system $\mathbf{A}x=b$ assuming that the matrix $\mathbf{A}$ is symmetric and sparse.


To do so, the SparseLDLSolver relies on the method of [LDL decomposition](https://en.wikipedia.org/wiki/Cholesky_decomposition#LDL_decomposition_2). The system matrix will be decomposed $\mathbf{A}=\mathbf{L}\mathbf{D}\mathbf{L}^T$, where $\mathbf{L}$ is a lower triangular matrix $\mathbf{A}$ and $\mathbf{D}$ is a diagonal matrix. This decomposition is an extension of the Cholesky decomposition which reduces its numerical inaccuracy.

As a direct solver, the SparseLDLSolver computes at each simulation time step an exact solution as follows:

$$
\mathbf{L}\mathbf{D}\mathbf{L}^Tx=b
$$

Using a block forward substitution, we successively solve two triangular systems. Between those two resolutions, we need to inverse $\mathbf{D}$, which is trivial as it is a diagonal matrix that has no null value on its diagonal.

$$
\begin{cases}
\mathbf{A}x=b \\
\mathbf{A}=\mathbf{LDL^T}
\end{cases}
\Longleftrightarrow 
\begin{cases}
 \mathbf{L} z = b \\
 \mathbf{D} y = z \\
 \mathbf{L}^T x = y \\
 \end{cases}
$$

It is important to note that this decomposition considers that the system matrix $\mathbf{A}$ is symmetric.

Note that using permutation, the SparseLDLSolver will apply fill reducing permutation on the rows and the columns of $\mathbf{A}$ in order to minimize the number of non null values in $\mathbf{L}$ . Instead of solving $\mathbf{A}x=b$, we will solve $\mathbf{(PAQ) (Q^{-1}}x) = Pb$. Moreover, $\mathbf{A}$ is symmetric, so we will use the same permutation on the rows and on the columns with $\mathbf{Q}=\mathbf{P}^T=\mathbf{P}^{-1}$. We will factorize $\tilde{\mathbf{A}} =\mathbf{PAP^T} $ and then we will solve

$$
\begin{cases} 
\tilde{\mathbf{A}} y = Pb \\
\mathbf{Q}^{-1} x = y
 \end{cases}
$$

As the impact of the use of fill reducing permutations on the performances is highly influenced by the repartition of the nodes used to model an object, we advise the users to test which type of permutation is the best suited for their simulations.



Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/SparseLDLSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/SparseLDLSolver.png?raw=true" title="Flow diagram for the SparseLDLSolver"/></a>


Usage
-----

The SparseLDLSolver **requires** the use (above in the scene graph) of an integration scheme, and (below in the scene graph) of a MechanicalObject storing the state information that the SparseLDLSolver will access.

As a direct solver, the SparseLDLSolver might be extremely time consuming for large system. However, it will always give you an exact solution, **making the assumption that the system matrix $\mathbf{A}$ is symmetric**.

<!-- automatically generated doc START -->
<!-- generate_doc -->

Direct linear solver using a Sparse LDL^T factorization.


## CompressedRowSparseMatrixMat3x3d

Templates:

- CompressedRowSparseMatrixMat3x3d

__Target__: Sofa.Component.LinearSolver.Direct

__namespace__: sofa::component::linearsolver::direct

__parents__:

- SparseLDLSolverImpl

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
		<td>precomputeSymbolicDecomposition</td>
		<td>
If true, the solver will reuse the precomputed symbolic decomposition, meaning that it will store the shape of [factor matrix] on the first step, or when its shape changes, and then it will only update its coefficients. When the shape of the matrix changes, a new factorization is computed.If false, the solver will compute the entire decomposition at each step
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>L_nnz</td>
		<td>
Number of non-zero values in the lower triangular matrix of the factorization. The lower, the faster the system is solved.
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
|linearSystem|The linear system to solve|TypedMatrixLinearSystem&lt;CompressedRowSparseMatrixMat3x3d&gt;|
|orderingMethod|Ordering method used by this component|BaseOrderingMethod|

<!-- generate_doc -->
## CompressedRowSparseMatrixd

Templates:

- CompressedRowSparseMatrixd

__Target__: Sofa.Component.LinearSolver.Direct

__namespace__: sofa::component::linearsolver::direct

__parents__:

- SparseLDLSolverImpl

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
		<td>precomputeSymbolicDecomposition</td>
		<td>
If true, the solver will reuse the precomputed symbolic decomposition, meaning that it will store the shape of [factor matrix] on the first step, or when its shape changes, and then it will only update its coefficients. When the shape of the matrix changes, a new factorization is computed.If false, the solver will compute the entire decomposition at each step
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>L_nnz</td>
		<td>
Number of non-zero values in the lower triangular matrix of the factorization. The lower, the faster the system is solved.
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
|orderingMethod|Ordering method used by this component|BaseOrderingMethod|


<!-- automatically generated doc END -->
