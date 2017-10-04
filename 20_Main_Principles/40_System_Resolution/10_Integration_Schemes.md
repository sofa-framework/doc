Integration Schemes
===================

All dynamic simulations assume to discretize the temporal evolution of the system through small time steps. This time step is usually noted *dt*.  An integration scheme is the numerical method describing how to find the solution of ordinary differential equations at the next time step. They are usually called **ODESolver** in SOFA.

Let's write our ODE as follows:
$$\frac{dx}{dt} = f(x,t)$$

Two categories
--------------
Two main categories of integration schemes exist:
  * explicit scheme: means that the new time step (t + dt) is computed based on information of the previous time step (t). For instance, in mechanics, internal or external forces would be computed on previous positions (x(t)). The ordinary differential equation looks like:
  $$x(t+dt) = x(t) + dt * f( x(t) , t)$$
  Explicit schemes are usually known as being fast to solve (since the created linear system is lighter) but they require very small time steps, unless they may undergo stability issues.

  * implicit scheme: means that the new time step (t + dt) is computed based on information of this next time step (t + dt). For instance, in mechanics, internal or external forces would be computed on unknow positions at the next time step (x(t + dt)). The ordinary differential equation looks like:
  $$x(t+dt) = x(t) + dt * f( x(t+dt) , t)$$
  Implicit schemes are known as being slower to solve (the outcoming linear system is more complex) but they are more way more stable than explicit schemes.

  * Semi-implicit or semi-explicit are actually a combination of two explicit and implicit schemes together for different parts of the ordinary differential equation.

In SOFA
-------
The integration scheme is described in the *solve()* function of the ODESolver. This *solve()* function will build the complete linear system $$Ax=b$$. The left hand side matrix A is build using the function:
``` cpp
matrix = MechanicalMatrix(a,b,c);
```
as $$M \times a + B \times b + K \times c$$ where M is the mass matrix, B is the damping matrix and K is the stiffness matrix. The right hand side vector b is built through the function:
``` cpp
computeForce()
```
Previous positions, new positions, forces, etc. are MultiVec, i.e. vectors stored in the MechanicalState (MechanicalObject).

This matrix system is then sent to a **LinearSolver** in charge of finally solving the system according to the chosen scheme. Within the function *ODESolver::solve()*, the call to the LinearSolver will appear through the function call:

``` cpp
matrix.solve(x, b);
```
