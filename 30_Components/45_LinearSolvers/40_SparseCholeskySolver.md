This component belongs to the category of [LinearSolver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/linear-solvers/). The role of the SparseLUSolver is to solve the linear system <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="Linear system" /> assuming that the matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> is symmetric and sparse.

The Cholesky decomposition (https://en.wikipedia.org/wiki/Cholesky_decomposition) is a numerical method that slove a linear system <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="Linear system" /> by factorizing the matrix of the system as <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{LL^T}" title="Linear system" />. By doing so, we only need to solve two triangular systems to compute the solution. It is only applyable on **symetric** matrices but is roughtly twice as efficient as the LU solver. The <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{LDL^T}" /> decomposition is heavily related to the Cholesky decomposition.

<div align="center">
<img class="latex" src="https://latex.codecogs.com/png.latex?\begin{cases}
\mathbf{A}x=b \\
\mathbf{A}=\mathbf{LL^T}
\end{cases}
\Longleftrightarrow 
\begin{cases}
 \mathbf{L} y = b \\
 \mathbf{L}^T x = y \\
 \end{cases}"
title="Linear systems" />

<div align="Left">

Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/SparseCholeskySolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/SparseCholeskySolver.png?raw=true" title="Flow diagram for the SparseCholeskySolver"/></a>

The SparseCholeskySolver **requires** the use (above in the scene graph) of an integration scheme, and (below in the scene graph) of a MechanicalObject storing the state information that the SparseCholeskySolver will access.


Data  
----
There is one data that change the behaviour of the solver, **typePermutation**, that allows three choices :
**-None**, we won't apply any permutation nor on the rows nor on the columns,
**-SuiteSparse**, use the SuiteSparse library as intended for a symetric matrix and apply a fill reducing permutaion on both the columns and the rows (those two permutations are the inverse of each other),
**-METIS**, use the METIS library to compute a fill reducing permutation and apply it on both the lines and the columns.

It is not currently possible to change the the type of permutation applied during a simulation.

By applying a fill reducing permutation, we aim at minimizing the number of non-null values in the decomposition, which would reduce the time spent on solving the triangular systems.

As the impact of the use of fill reducing permutations on the performances is higly influenced by the repartition of the nodes used to modelize an object, we advise the users to test which type of permutation is the best suited for their simulations.


Example
-------

This component is used as follows in XML format:

``` xml
<SparseCholeskySolver  />
```

or using SofaPython3:

``` python
node.addObject('SparseCholeskySolver')
```

With a description of each data

An example scene involving a SparseCholzskySolver is available in [*examples/Components/linearsolver/FEMBAR-SparseCholeskySolver.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/linearsolver/FEMBAR-SparseCholeskySolver.scn)
