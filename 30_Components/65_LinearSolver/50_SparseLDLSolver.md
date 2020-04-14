SparseLDLSolver
===============

This component belongs to the category of [LinearSolver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/linear-solvers/). The role of the SparseLDLSolver is to solve the linear system <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}x=b$$" title="Linear system" /> without any _a priori_ on this system.


To do so, the SparseLDLSolver relies on the method of [LDL decomposition](https://en.wikipedia.org/wiki/Cholesky_decomposition#LDL_decomposition_2). The system matrix will be decomposed <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}=\mathbf{L}\mathbf{D}\mathbf{L}^T$$" title="LDL decomposition" />, where <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{L}$$" title="Lower part of the matrix" /> is the lower part of the matrix <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}$$" title="System matrix" /> and <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{D}$$" title="Diagonal of the matrix" /> is its diagonal.

As a direct solver, the SparseLDLSolver computes at each simulation time step an exact solution as follows:

<img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{L}\mathbf{D}\mathbf{L}^Tx=b$$" title="LDL system" />

Using a block forward substitution, we can first find the <img class="latex" src="https://latex.codecogs.com/png.latex?$$z$$" title="First intermediate solution" /> solution of: <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{L}z=b$$" title="L system" />

Next, a second solution <img class="latex" src="https://latex.codecogs.com/png.latex?$$y$$" title="Second intermediate solution" />  can be computed: <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{D}y=z$$" title="L system" />

Finally, from the relationship <img class="latex" src="https://latex.codecogs.com/png.latex?$$y=z\mathbf{D}^{-1}$$" title="Final substitution" /> where <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{D}^{-1}$$" title="Inverse of diagonal" /> is easy to compute, we can find the exact solution <img class="latex" src="https://latex.codecogs.com/png.latex?$$x$$" title="Solution" /> via backward substitution: <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{L}^Tx=y$$" title="Final resolution" />

It is important to note that this decomposition considers that the system matrix <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}$$" title="System matrix" /> is symmetric.




Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/SparseLDLSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/SparseLDLSolver.png?raw=true" title="Flow diagram for the SparseLDLSolver"/></a>




Data  
----

No important data is available for the LDL since it simply computes the direct solution.

However, an option for saving the matrix is given using the data **savingMatrixToFile**. You can thus choose the **savingFilename** and the precision of the digits saved in this file using **savingPrecision**.



Usage
-----

The SparseLDLSolver **requires** the use (above in the scene graph) of an integration scheme, and (below in the scene graph) of a MechanicalObject storing the state information that the SparseLDLSolver will access.

As a direct solver, the SparseLDLSolver might be extremely time consuming for large system. However, it will always give you an exact solution, **making the assumption that the system matrix <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}$$" title="System matrix" /> is symmetric**.




Example
-------

This component is used as follows in XML format:

``` xml
<SparseLDLSolver  />
```

or using Python:

``` python
node.createObject('SparseLDLSolver')
```

With a description of each data

An example scene involving a SparseLDLSolver is available in [*examples/Components/linearsolver/FEMBAR-SparseLDLSolver.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/linearsolver/FEMBAR-SparseLDLSolver.scn)