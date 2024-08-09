SparseCholeskySolver  
====================

This component belongs to the category of [LinearSolver](../../../../simulation-principles/system-resolution/linear-solver/). The role of the SparseLUSolver is to solve the linear system $\mathbf{A}x=b$ assuming that the matrix $\mathbf{A}$ is symmetric and sparse.

The Cholesky decomposition (https://en.wikipedia.org/wiki/Cholesky_decomposition) is a numerical method that solves a linear system $mathbf{A}x=b$ by factorizing the matrix of the system as $\mathbf{LL^T}$. By doing so, we only need to solve two triangular systems to compute the solution. It is only applyable on **symetric** matrices but is roughtly twice as efficient as the LU solver. The $\mathbf{LDL^T}$ decomposition is heavily related to the Cholesky decomposition.

$$
\begin{cases}\mathbf{A}x=b \\ \mathbf{A}=\mathbf{LL^T}\end{cases}\Longleftrightarrow\begin{cases} \mathbf{L} y = b \\ \mathbf{L}^T x = y \\ \end{cases}
$$


Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/SparseCholeskySolver.png?raw=true">
<img src="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/SparseCholeskySolver.png?raw=true" title="Flow diagram for the SparseCholeskySolver"/>
</a>

The SparseCholeskySolver **requires** the use (above in the scene graph) of an integration scheme, and (below in the scene graph) of a MechanicalObject storing the state information that the SparseCholeskySolver will access.
