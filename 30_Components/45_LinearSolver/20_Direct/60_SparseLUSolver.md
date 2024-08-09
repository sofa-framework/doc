SparseLUSolver
==============

This component belongs to the category of [LinearSolver](../../../../simulation-principles/system-resolution/linear-solver/). The role of the SparseLUSolver is to solve the linear system $\mathbf{A}x=b$ assuming that the matrix $\mathbf{A}$ is invertible and sparse.

In order to solve this system, this solver will factorize the matrix $\mathbf{A}$ into the product $\mathbf{A=LU}$ where $\mathbf{L}$ is a lower triangular matrix with ones on its diagonal and $\mathbf{U}$ is an upper triangular matrix (for more, see [LU decomposition article](https://en.wikipedia.org/wiki/LU_decomposition)).

As this method relies on the Gaussian elimination, a partial pivot is applied on the lines of $\mathbf{A}$ hence its factorization will be written as $\mathbf{PA=LU}$ .
The LU solver is a direct solver which will compute the exact solution of the linear system by successively solving two triangular systems.

$$
\begin{cases} \mathbf{A}x = b\\
\mathbf{PA}=\mathbf{LU}
 \end{case} \Longleftrightarrow 
\begin{cases} \mathbf{L}y=\mathbf{P}b\\ 
\mathbf{U} x = y \\
\end{case}
$$


Usage
-----
<a href="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/SparseLUSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/SparseLUSolver.png?raw=true" title="Flow diagram for the SparseLUSolver"/></a>

The SparseLUSolver **requires** the use (above in the scene graph) of an integration scheme, and (below in the scene graph) of a MechanicalObject storing the state information that the SparseLUSolver will access.

The SparseLUSolver is the most generic direct solver. It may be time consuming but it will be able compute the exact solution as soon as $$\mathbf{A}"> is invertible.
