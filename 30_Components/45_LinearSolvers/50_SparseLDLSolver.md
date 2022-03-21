SparseLDLSolver
===============

This component belongs to the category of [LinearSolver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/linear-solvers/). The role of the SparseLDLSolver is to solve the linear system <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="Linear system" /> assuming that the matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> is symetric and sparse.


To do so, the SparseLDLSolver relies on the method of [LDL decomposition](https://en.wikipedia.org/wiki/Cholesky_decomposition#LDL_decomposition_2). The system matrix will be decomposed <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}=\mathbf{L}\mathbf{D}\mathbf{L}^T" title="LDL decomposition" />, where <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{L}" title="Lower part of the matrix" /> is a lower triangular matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> and <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{D}" title="Diagonal of the matrix" /> is a diagonal marix. This decomposition is an extention of the Cholesky decomposition which reduces it numerical inaccuracy.

As a direct solver, the SparseLDLSolver computes at each simulation time step an exact solution as follows:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{L}\mathbf{D}\mathbf{L}^Tx=b" title="LDL system" />

Using a block forward substitution, we successively solve two triangular systems. Between those two resoltion, we need to inverse <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{D}" title="Diagonal matrix" />, which is trivial as it is a diagonal matrix that has non null value on its diagonal.

<img class="latex" src="https://latex.codecogs.com/png.latex?\begin{cases}
 \mathbf{L}^T z = b \\
 \mathbf{D} y = z \\
 \mathbf{L} x = y \\
 \end{cases} \Longleftrightarrow \mathbf{L^T D L}x=b"
title="Linear systems" />

It is important to note that this decomposition considers that the system matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> is symmetric.




Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/SparseLDLSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/SparseLDLSolver.png?raw=true" title="Flow diagram for the SparseLDLSolver"/></a>




Data  
----

There is two bolean data to change the behavoir of this solver:

-useSymbolicDecomposition

By default useSymbolicDecomposition is set to true. The solver will use a symbolic decomposition, meaning that it will store the shape of <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{L}" title="factor matrix" /> on the first step, or when it detects that this shape muste but updated, and then it will only update its coefficients. By setting this data to false, the solver will compute the entire decomposition at each step.

-applyPermutation



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
