BDFOdeSolver
============

This component belongs to the category of [integration schemes or ODE Solver](../../../../simulation-principles/system-resolution/integration-scheme/).
It is an implicit method for the numerical integration of the ODE resulting from Newton's second law of motion.

The method relies on [Backward Differentiation Formula](https://en.wikipedia.org/wiki/Backward_differentiation_formula) (BDF).
To integrate the ODE in time, it uses information from the previous time steps to compute the next step.
It establishes a linear combination of the unknown states, the previous states and the values of the ODE function when applied on those states.
This equation leads to a nonlinear function to solve.
That is why this component requires a [NewtonRaphsonSolver](NewtonRaphsonSolver.md), which the purpose is to solve nonlinear functions.

The coefficients of the linear combination come from the approximation of the function by a Lagrange interpolation polynomial.
The order of the BDF is the number of previous time steps required to approximate the interpolation polynomial.
The first-order BDF requires a single time step in the past to compute the next.
It corresponds to the [backward Euler method](EulerImplicitSolver.md).
The coefficients are unique for a given order, but can be influenced by a change of time step size.
The SOFA component supports any order, and any change of time step size.

Details
-------

The ODE resulting from Newton's second law of motion is:

$$
\begin{bmatrix}
\frac{d q}{d t}\\
M \frac{d \dot{q}}{d t}
\end{bmatrix}
=
\begin{bmatrix}
\dot{q}\\
F(q, \dot{q})
\end{bmatrix}
$$

where $q$ and $\dot{q}$ are respectively the position and the velocity, $M$ is the mass matrix, and $F$ is the sum of forces.

We define $y(t)=\begin{bmatrix} q \\ \dot{q} \end{bmatrix}$, and $f(t,y)=\begin{bmatrix} \dot{q} \\ M^{-1} F(q,\dot{q}) \end{bmatrix}$, such that the ODE is $y'=f(t,y)$.
We are interested in computing $y(t_{n+s})$ and we know the values of $y(t_{n+j})$ for $j \lt s$.
The Lagrange interpolation polynomial is the linear combination $L(t) = \sum_{j=0}^s y(t_n+j) l_j(t)$, where $l_j$ is the basis polynomials defined as $l_j(t)=\prod_{0 \leq m \leq s, m \neq j} \frac{t-t_{n+m}}{t_{n+j}-t{n+m}}$.
Then, we approximate $y'$ by $L'$, leading to the equation $\sum_{j=0}^s y_{n+j} l'_j(t_{n+s}) = f(t_{n+s},y_{n+s})$.
We can now define a nonlinear function $r(q, \dot{q}) = \left[\sum_{j=0}^s y_{n+j} l'_j(t_{n+s})\right] - f(t_{n+s},y_{n+s})$. 
The roots of this function corresponds to $y_{tn+s}$, i.e. the next values of the state.

To find the root of this function, we use a Newton-Raphson algorithm.
It means the derivative of the function is necessary.
At each iteration $i$ of the algorithm, we solve the following linear system:

$$
\begin{bmatrix}
l'_s(t_{n+s}) I & -dt I \\
-dt \frac{\partial F}{\partial q} & l'_s(t_{n+s}) M - dt \frac{\partial F}{\partial \dot{q}}
\end{bmatrix}
\begin{bmatrix}
q^{i+1} - q^i \\
\dot{q}^{i+1} - \dot{q}^{i}
\end{bmatrix}
= -r(q^i, \dot{q}^i)
$$

This system is solved by a block Gaussian elimination leading to the velocity-based linear system:

$$
\left(l'_s(t_{n+s}) M - dt \frac{\partial F}{\partial \dot{q}} - \frac{dt^2}{l'_s(t_{n+s})} \frac{\partial F}{\partial q} \right)
(\dot{q}^{i+1} - \dot{q}^i)
= -r_{\dot{q}}(q^i, \dot{q}^i) - \frac{dt}{l'_s(t_{n+s})} \frac{\partial F}{\partial q} r_{q}(q^i, \dot{q}^i)
$$


