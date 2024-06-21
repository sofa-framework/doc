---
title: AsyncSparseLDLSolver
---

﻿AsyncSparseLDLSolver
====================

(since SOFA v22.06)

AsyncSparseLDLSolver is based on [SparseLDLSolver](https://www.sofa-framework.org/community/doc/components/linearsolvers/sparseldlsolver/).
It follows some ideas presented in:

> Courtecuisse, Hadrien, et al. "Asynchronous preconditioners for efficient solving of non-linear deformations." VRIPHYS-Virtual Reality Interaction and Physical Simulation. Eurographics Association, 2010.
https://hal.inria.fr/hal-00688865/document

## Asynchronous Factorization

The difference compared to SparseLDLSolver resides in the fact that the factorization of the matrix is performed in a different thread in order to speed up the simulation.

The synchronous version performs the following operations (synchronously):
1) Build the matrix
2) Factorize the matrix
3) Solve the system based on the factorization

In the asynchronous version, the factorization is performed asynchronously.
A consequence is that the solving process uses a factorization which may not be up to date.
In practice, the factorization is at least one time step old, but it can be an older factorization depending on the duration of the asynchronous factorization step.
Because of this, the solver computes an approximation of the solution, based on an old factorization.
It is therefore important to understand that using AsyncSparseLDLSolver changes the behavior of your simulation compared to a synchronous version.
It may also introduce instabilities.

## A Preconditioner

AsyncSparseLDLSolver can be used as a preconditioner of [ShewchukPCGLinearSolver](https://www.sofa-framework.org/community/doc/components/linearsolvers/preconditioned-cg/).

## Performances

The idea to have the factorization of the matrix in a different thread is to reduce the time taken to solve a linear system.
However, building the matrix and solving a system based on a factorization will not be reduced.
Since the factorization of a matrix is a time-consuming step of the simulation, this strategy greatly improves the performances.
This speed up is at the price of an approximation of the solution, because solving the linear system relies on a factorization of a matrix from a previous time step.

## Example

This component is used as follows in XML format:

``` xml
<AsyncSparseLDLSolver />
```

or using SofaPython3:

``` python
node.addObject('AsyncSparseLDLSolver')
```

- An example where AsyncSparseLDLSolver is used as a standalone linear solver is available in [*examples/Component/LinearSolver/Direct/FEMBAR_AsyncSparseLDLSolver.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/LinearSolver/Direct/FEMBAR_AsyncSparseLDLSolver.scn).
- The example in [*examples/Component/LinearSolver/Preconditioner/FEMBAR_PCG_AsyncSparseLDLSolver.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/LinearSolver/Preconditioner/FEMBAR_PCG_AsyncSparseLDLSolver.scn) shows how to use AsyncSparseLDLSolver as a preconditioner of ShewchukPCGLinearSolver.
- Finally, the example in [*examples/Component/LinearSolver/Preconditioner/FEMBAR_PCG_WarpedAsyncSparseLDLSolver.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/LinearSolver/Preconditioner/FEMBAR_PCG_WarpedAsyncSparseLDLSolver.scn) shows how the factorization in AsyncSparseLDLSolver can be warped using a WarpPreconditioner.
<!-- automatically generated doc START -->
__Target__: `Sofa.Component.LinearSolver.Direct`

__namespace__: `#!c++ sofa::component::linearsolver::direct`

__parents__: 

- `#!c++ SparseLDLSolver`

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

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|linearSystem|The linear system to solve|
|orderingMethod|Ordering method used by this component|




<!-- automatically generated doc END -->
