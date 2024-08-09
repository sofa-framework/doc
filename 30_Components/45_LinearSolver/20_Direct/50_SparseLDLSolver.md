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

