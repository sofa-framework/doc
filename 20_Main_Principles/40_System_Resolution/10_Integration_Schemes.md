Integration Schemes
===================

All dynamic simulations assume to discretize the temporal evolution of the system through small time steps. This time step is usually noted *dt*. An integration scheme is the numerical method describing how to find the solution of ordinary differential equations (ODE) at the next time step. They are usually called **ODESolver** in SOFA.

Let's write our ordinary differential equation as follows:
<img class="latex" src="https://latex.codecogs.com/png.latex?$$\frac{dx}{dt}=f(x,t)$$" title="Ordinary differential equation" />


Two categories
--------------

Two main categories of integration schemes exist:

  * **explicit scheme**: means that the new time step (t + dt) is computed based on information of the previous time step (t). For instance, in mechanics, internal or external forces would be computed on previous positions (x(t)). The ordinary differential equation looks like:
  <img class="latex" src="https://latex.codecogs.com/png.latex?x(t+dt)=x(t)+dt%20\cdot%20f(x(t),t)" title="Explicit scheme" />
  Explicit schemes are usually known as being fast to solve (since the created linear system is lighter) but they require very small time steps, unless they may undergo stability issues.

  * **implicit scheme**: means that the new time step (t + dt) is computed based on information of this next time step (t + dt). For instance, in mechanics, internal or external forces would be computed on unknow positions at the next time step (x(t + dt)). The ordinary differential equation looks like:
  <img class="latex" src="https://latex.codecogs.com/png.latex?x(t+dt)=x(t)+dt%20\cdot%20f(x(t+dt),t)" title="Implicit scheme" />
  Implicit schemes are known as being slower to solve (the outcoming linear system is more complex) but they are more way more stable than explicit schemes.

  * Semi-implicit or semi-explicit are actually a combination of two explicit and implicit schemes together for different parts of the ordinary differential equation.


In the SOFA code
----------------

The integration scheme is described in the *solve()* function of the ODESolver. This *solve()* function will build the complete linear system <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}x=b$$" title="Linear system" />
The left hand side matrix <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}$$" title="System matrix" /> is built using the function:
``` cpp
matrix = MechanicalMatrix(a,b,c);
```
with the matrix <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}$$" title="System matrix" /> equals <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}%20=%20\mathbf{M}%20\cdot%20a%20+%20\mathbf{B}%20\cdot%20b%20+%20\mathbf{K}%20\cdot%20c" title="System matrix" /> where <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{M}$$" title="Mass matrix" /> is the mass matrix, <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{B}$$" title="Damping matrix" /> is the damping matrix and <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{K}$$" title="Stiffness matrix" /> is the stiffness matrix. The right hand side vector *b* is built through the function:
``` cpp
computeForce()
```
Previous positions, new positions, forces, etc. are MultiVec, i.e. vectors stored in the MechanicalState (MechanicalObject).

This matrix system is then sent to a [LinearSolver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/linear-solvers/) in charge of finally solving the system according to the chosen scheme. Within the function *ODESolver::solve()*, the call to the LinearSolver will appear through the function call:

``` cpp
matrix.solve(x, b);
```

Rayleigh damping
----------------

The Rayleigh damping is a numerical damping. This damping has therefore no physical meaning and must not be mixed up with physical damping (like _DiagonalVelocityDampingForceField_ in SOFA). The Rayleigh damping corresponds to a damping matrix that is proportional to the mass or/and stiffness matrices using ceofficients, respectively Rayleigh stiffness factor <img class="latex" src="https://latex.codecogs.com/png.latex?$$r_K$$" title="Rayleigh stiffness" /> or Rayleigh mass factor <img class="latex" src="https://latex.codecogs.com/png.latex?$$r_M$$" title="Rayleigh mass" />. This numerical damping is usually used to stabilize or ease convergence of the simulation. However, it has to be used carefully.

You can see the use of Rayleigh mass and stifness in the _solve()_ function of the _EulerImplicit_ class (see EulerImplicitSolver.cpp).