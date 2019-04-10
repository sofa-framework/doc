Integration Schemes
===================

All dynamic simulations assume to discretize the temporal evolution of the system through small time steps. This time step is usually noted *dt*. An integration scheme is the [numerical method](https://en.wikipedia.org/wiki/Numerical_methods_for_ordinary_differential_equations) describing how to find the approximate solution for ordinary differential equations (ODE).

They are usually called **ODESolver** in SOFA. 

Let's write our ordinary differential equation of a function *y* as follows:
<img class="latex" src="https://latex.codecogs.com/png.latex?$$\frac{dy}{dt}=f\left(%20t,y(t)\right)$$" title="Ordinary differential equation" />.

ODESolver defines how to go from the current time step (t) to the next (t + dt), which will structure the linear system <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}x=b$$" title="Linear system" />. The integration scheme therefore defines which forces impact the left hand side matrix <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}$$" title="System matrix" /> and which forces contribute to the right hand side vector *b*:

- explicit contributions depending on the degrees of freedom (DOFs) at the current time step <img class="latex" src="https://latex.codecogs.com/png.latex?x(t)" title="Current position"/> will contribute to the *b* vector
- while implicit contributions depending on the degrees of freedom (DOFs) at the next step <img class="latex" src="https://latex.codecogs.com/png.latex?x(t+dt)" title="Unknown position"/> (unknown) will contribute to <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}$$" title="System matrix" />. 


Two categories
--------------

Two main categories of integration schemes exist: **explicit** and **implicit** schemes. A combination of explicit and implicit methods are also possible, it is called semi-implicit or semi-explicit schemes.

### Explicit scheme

An explicit scheme means that the new time step (t + dt) is computed based on information of the previous time step (t):

<center><img class="latex" src="https://latex.codecogs.com/png.latex?y(t+dt)=y(t)+dt%20\cdot%20f(y(t))" title="Explicit scheme"/></center>

For instance, in mechanics, internal or external forces would be computed on current known positions <img class="latex" src="https://latex.codecogs.com/png.latex?x(t)" title="Current position"/>. The ordinary differential equation looks like:

<center><img class="latex" src="https://latex.codecogs.com/png.latex?x(t+dt)=x(t)+dt%20\cdot%20v(t)" title="Explicit scheme"/></center>

Explicit schemes are usually known as being fast to solve (since the created linear system is lighter) but they require very small time steps, unless they may undergo stability issues. They are known to efficiently solve non-stiff problems.

Explicit ODESolvers in SOFA:

- [EulerExplicitSolver](https://www.sofa-framework.org/community/doc/using-sofa/components/integrationscheme/eulerexplicitsolver/)
- CentralDifferenceSolver
- RungeKutta2Solver


### Implicit scheme

An implicit scheme means that the new time step (t + dt) is computed based on information of this next time step (t + dt):

<center><img class="latex" src="https://latex.codecogs.com/png.latex?y(t+dt)=y(t)+dt%20\cdot%20f(y(t+dt))" title="Implicit scheme" /></center>

For instance, in mechanics, internal or external forces would be computed on unknow positions at the next time step <img class="latex" src="https://latex.codecogs.com/png.latex?x(t+dt)" title="Unknown position"/>. The ordinary differential equation looks like:

<center><img class="latex" src="https://latex.codecogs.com/png.latex?x(t+dt)=x(t)+dt%20\cdot%20v(t+dt)" title="Implicit scheme" /></center>

Implicit schemes are known as being slower to solve (the outcoming linear system is more complex) but they are way more stable than explicit schemes. Stiff differential equations require the use of implicit schemes.

Implicit ODESolvers in SOFA:

- [EulerImplicitSolver](https://www.sofa-framework.org/community/doc/using-sofa/components/integrationscheme/eulerimplicitsolver/)
- NewmarkImplicitSolver
- VariationalSymplecticSolver


In the SOFA code
----------------

The integration scheme is described in the `solve()` function of the ODESolver. This *solve()* function is called by the [AnimationLoop](https://www.sofa-framework.org/community/doc/main-principles/animation-loop/) (through a dedicated visitor) and builds the complete linear system <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}x=b$$" title="Linear system" />.


### Specification of the scheme

The construction of the linear system changes whether the integration scheme is explicit or implicit, which is specified by:

  - for explicit cases
``` cpp
mop->setImplicit(false);
```


  - for implicit cases
``` cpp
mop->setImplicit(true);
```


### Build the linear matrix system

The left hand side matrix <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}$$" title="System matrix" /> is built using the function:
``` cpp
matrix = MechanicalMatrix(r_M, r_B, r_K);
```
where *r_M* (mass coefficient), *r_B* (damping coefficient). and *r_K* (stiffness coefficient) are Rayleigh coefficients (see section below). Depending on the scheme (explicit or implicit, see previous paragraph) and on the type of LinearSolver used (if any), the abstract function `MechanicalMatrix` will trigger different [visitors](https://www.sofa-framework.org/community/doc/main-principles/visitors/), thus different functions to compute the system matrix <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}$$" title="System matrix" />. Discover the API used for the computation of <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}$$" title="System matrix" /> in the [ForceField](https://www.sofa-framework.org/community/doc/main-principles/multi-model-representation/forcefield/) and [Mass](https://www.sofa-framework.org/community/doc/main-principles/multi-model-representation/mass/) doc pages.


The right hand side vector *b* is built through the function:
``` cpp
computeForce(b)
```

Again, Depending on the scheme (explicit or implicit, see previous paragraph), the abstract function `computeForce` will trigger different [visitors](https://www.sofa-framework.org/community/doc/main-principles/visitors/), thus different functions to accumulate the forces into the vector *b*. Discover the API used for the computation of *b* in the [ForceField](https://www.sofa-framework.org/community/doc/main-principles/multi-model-representation/forcefield/) doc page.




### State vectors in ODESolver

In order to build the linear matrix system, the ODESolver uses information contained in [state vectors](https://www.sofa-framework.org/community/doc/main-principles/mechanicalobject/#state-vectors) (like DOFs and their derivatives) within the scope of the ODESolver. The ODESolver does not access the state vectors directly. It accesses the state vectors remotely using visitors, which traverse the graph starting from the node which contains the solver. This keeps the implementation of the solver independent from the simulated objects and their types.

Each type of solver may use different auxiliary state vectors to implement their simulation method. State vectors (MultiVec) are allocated and processed in the scope of the solver in a thread-safe way using an instance of _simulation::common::VectorOperations_. For instance, a Runge-Kutta algorithms needs to save the result of previous time steps.

To create an auxiliary vector, this can be done as follows:

``` cpp
MultiVecCoord pos(&vop, core::VecCoordId::position() ); // standard position vector
MultiVecDeriv acc(&vop);                                // auxiliary vector
MultiVecCoord previousPos(&vop, previousPosID);         // additional vector
```



### Compute the solution

In most cases, the matrix system <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}x=b$$" title="Linear system" /> can then be sent to a [LinearSolver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/linear-solvers/) in charge of finally solving the system defined according to the chosen scheme. Within the function *ODESolver::solve()*, the call to the LinearSolver will appear through the function call:

``` cpp
matrix.solve(x, b);
```


Some simple matrix cases provides a diagonal matrix <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}$$" title="System matrix" />. In this specific configuration, a solution can directly be found by dividing the right hand side vector *b* by the diagonal matrix <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}$$" title="System matrix" />. This is done using the function:
``` cpp
mop.accFromF(acc, f);
```



Rayleigh damping
----------------

The Rayleigh damping is a numerical damping. This damping has therefore no physical meaning and must not be mixed up with physical damping (like _DiagonalVelocityDampingForceField_ in SOFA). The Rayleigh damping corresponds to a damping matrix that is proportional to the mass or/and stiffness matrices using ceofficients, respectively Rayleigh stiffness factor <img class="latex" src="https://latex.codecogs.com/png.latex?$$r_K$$" title="Rayleigh stiffness" /> or Rayleigh mass factor <img class="latex" src="https://latex.codecogs.com/png.latex?$$r_M$$" title="Rayleigh mass" />. This numerical damping is usually used to stabilize or ease convergence of the simulation. However, it has to be used carefully.

When Rayleigh damping is used, the matrix <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}$$" title="System matrix" /> equals <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}%20=%20\mathbf{M}%20\cdot%20r_M%20+%20\mathbf{B}%20\cdot%20+%20\mathbf{K}%20\cdot%20r_K" title="System matrix" /> where <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{M}$$" title="Mass matrix" /> is the mass matrix, <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{B}$$" title="Damping matrix" /> is the damping matrix and <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{K}$$" title="Stiffness matrix" /> is the stiffness matrix.
You can see the use of Rayleigh mass and stifness in the _solve()_ function of the _EulerImplicit_ class (see EulerImplicitSolver.cpp).
