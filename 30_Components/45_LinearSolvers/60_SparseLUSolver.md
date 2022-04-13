This component belongs to the category of [LinearSolver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/linear-solvers/). The role of the SparseLUSolver is to solve the linear system <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="Linear system" /> assuming that the matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> is invertible and sparse.

In order to solve this system, this solver will factorize the matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="system matrix" /> into the product <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A=LU}" title="lu" /> where <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{L}" title="Lower matrix" /> is a lower triangular matrix with ones on its diagonal and <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{U}" title="upper matrix" /> is an upper triangonal matrix (https://en.wikipedia.org/wiki/LU_decomposition).

As this method relies on the Gaussian elimination, we will apply a partial pivot on the lines of <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> hence its factorization will be written as <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{PA=LU}" title="factor matrix" /> .
The LU solver is a direct solver which will compute the exact solution of the linear system by successively solving two triangular system.

<div align="center">
<img class="latex" src="https://latex.codecogs.com/png.latex?\begin{cases} \mathbf{A}x = b\\
\mathbf{PA}=\mathbf{LU}
 \end{case} \Longleftrightarrow 
\begin{cases} \mathbf{L}y=\mathbf{P}b\\ 
\mathbf{U} x = y \\
\end{case} " title="System matrix" /> 

<div align="Left">

Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/SparseLUSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/SparseLUSlover.png?raw=true" title="Flow diagram for the SparseLUSolver"/></a>

The SparseLUSolver **requires** the use (above in the scene graph) of an integration scheme, and (below in the scene graph) of a MechanicalObject storing the state information that the SparseLDLSolver will access.

Data  
----
The SparseLUSolver has only one data **typePermutation** that allows three choices :
  **-None**, we won't apply any permutation nor on the rows nor on the columns
  **-SuiteSparse**, use the SuiteSparse library as intended for a the LU decomposition and apply a fill reducing permutation on the columns only leaving the permutation on the lines available for the partial pivot
  **-METIS**, use the METIS library to compute a fill reducing permutation and apply it on both the lines and the columns. For this option we assume that the matrix is symetric and we don't apply any pivoting.

  It is not currently possible to change the the type of permutation applied during a simulation.

By applying a fill reducing permutation, we aim at minimizing the number of non-null values in the decomposition, which would reduce the time spent on solving the triangular systems.

Usage
-----

The SparseLUSolver **requires** the use (above in the scene graph) of an integration scheme, and (below in the scene graph) of a MechanicalObject storing the state information that the SparseLUSolver will access.

The SparseLUSolver is the most generic direct solver. It may be time consuming but it will be able compute the exact solution as son as <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}"> is invertible.

Example
-------

This component is used as follows in XML format:

``` xml
<SparseLUSolver  />
```

or using SofaPython3:

``` python
node.addObject('SparseLUSolver')
```

With a description of each data

An example scene involving a SparseLUSolver is available in [*examples/Components/linearsolver/FEMBAR-SparseLUSolver.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/linearsolver/FEMBAR-SparseLUSolver.scn)
