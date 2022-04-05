SparseLDLSolver
===============

This component belongs to the category of [LinearSolver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/linear-solvers/). The role of the SparseLDLSolver is to solve the linear system <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="Linear system" /> assuming that the matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> is symmetric and sparse.


To do so, the SparseLDLSolver relies on the method of [LDL decomposition](https://en.wikipedia.org/wiki/Cholesky_decomposition#LDL_decomposition_2). The system matrix will be decomposed <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}=\mathbf{L}\mathbf{D}\mathbf{L}^T" title="LDL decomposition" />, where <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{L}" title="Lower part of the matrix" /> is a lower triangular matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> and <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{D}" title="Diagonal of the matrix" /> is a diagonal marix. This decomposition is an extention of the Cholesky decomposition which reduces its numerical inaccuracy.

As a direct solver, the SparseLDLSolver computes at each simulation time step an exact solution as follows:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{L}\mathbf{D}\mathbf{L}^Tx=b" title="LDL system" />

Using a block forward substitution, we successively solve two triangular systems. Between those two resolutions, we need to inverse <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{D}" title="Diagonal matrix" />, which is trivial as it is a diagonal matrix that has no null value on its diagonal.

<div align="center">
<img class="latex" src="https://latex.codecogs.com/png.latex?\begin{cases}
\mathbf{A}x=b \\
\mathbf{A}=\mathbf{LDL^T}
\end{cases}
\Longleftrightarrow 
\begin{cases}
 \mathbf{L} z = b \\
 \mathbf{D} y = z \\
 \mathbf{L}^T x = y \\
 \end{cases}"
title="Linear systems" />

<div align="Left">
It is important to note that this decomposition considers that the system matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> is symmetric.




Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/SparseLDLSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/SparseLDLSolver.png?raw=true" title="Flow diagram for the SparseLDLSolver"/></a>




Data  
----

There is two bolean data to change the behavior of this solver:

- **useSymbolicDecomposition**: by default useSymbolicDecomposition is set to true. The solver will use a symbolic decomposition, meaning that it will store the shape of <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{L}" title="factor matrix" /> on the first step, or when its shape changes, and then it will only update its coefficients. When the shape of the matrix changes, a new factorization is computed. By setting this data to false, the solver will compute the entire decomposition at each step.

- **applyPermutation**:  by default it is set to true. It will apply fill reducing permutation on the rows and the columns of <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="system matrix" /> in order to minimize the number of non null values in <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{L}" title="factor matrix" /> . Instead of solving <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="linear system" />, we will solve <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{(PAQ) (Q^{-1}}x) = Pb" title="factor matrix" />. Moreover, <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="system matrix" /> is symmetric, so we will use the same permutation on the rows and on the columns with <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{Q}=\mathbf{P}^T=\mathbf{P}^{-1}" title="system matrix" />. We will factorize <img class="latex" src="https://latex.codecogs.com/png.latex?\tilde{\mathbf{A}} =\mathbf{PAP^T} " title="system matrix" /> and then we will solve

<div align="center"><img class="latex" src="https://latex.codecogs.com/png.latex?\begin{cases} 
\tilde{\mathbf{A}} y = Pb \\
\mathbf{Q}^{-1} x = y
 \end{cases} " title="system matrix" />

<div align="Left">

Usage
-----

The SparseLDLSolver **requires** the use (above in the scene graph) of an integration scheme, and (below in the scene graph) of a MechanicalObject storing the state information that the SparseLDLSolver will access.

As a direct solver, the SparseLDLSolver might be extremely time consuming for large system. However, it will always give you an exact solution, **making the assumption that the system matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> is symmetric**.




Example
-------

This component is used as follows in XML format:

``` xml
<SparseLDLSolver  />
```

or using SofaPython3:

``` python
node.addObject('SparseLDLSolver')
```

With a description of each data

An example scene involving a SparseLDLSolver is available in [*examples/Components/linearsolver/FEMBAR-SparseLDLSolver.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/linearsolver/FEMBAR-SparseLDLSolver.scn)
