This component belongs to the category of [LinearSolver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/linear-solvers/). The role of the SparseLUSolver is to solve the linear system <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="Linear system" /> assuming that the matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> is symetric and sparse.

(https://en.wikipedia.org/wiki/Cholesky_decomposition)







Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/SparseCholeskySolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/SparseCholeskySolver.png?raw=true" title="Flow diagram for the SparseCholeskySolver"/></a>


Data  
----
There is one data that change the behaviour of the solver, **typePermutation**, that allows three choices :

**-None**, we won't apply any permutation nor on the rows nor on the columns

**-SuiteSparse**, use the SuiteSparse library as intended and apply a fill reducing permutaion on the columns only

**-METIS**, use the METIS library to compute a fill reducing permutation and apply it on both the lines and the columns

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
