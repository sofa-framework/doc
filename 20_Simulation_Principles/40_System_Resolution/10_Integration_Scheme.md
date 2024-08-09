Integration Schemes
===================

All dynamic simulations assume to discretize the temporal evolution of the system through small time steps. This time step is usually noted *dt*. An integration scheme is the [numerical method](https://en.wikipedia.org/wiki/Numerical_methods_for_ordinary_differential_equations) describing how to find the approximate solution for ordinary differential equations (ODE).

They are usually called **ODESolver** in SOFA. 

Let's write our ordinary differential equation of a function *y* as follows:

$$
\frac{dy}{dt}=f\left( t,y(t)\right)
$$

ODESolver defines how to go from the current time step (t) to the next (t + dt), which will structure the linear system $\mathbf{A}x=b$. The integration scheme therefore defines which forces impact the left hand side matrix $\mathbf{A}$ and which forces contribute to the right hand side vector *b*:

- explicit contributions depending on the degrees of freedom (DOFs) at the current time step $x(t)$ will contribute to the $b$ vector
- while implicit contributions depending on the degrees of freedom (DOFs) at the next step $x(t+dt)$ (unknown) will contribute to $\mathbf{A}$. 


Two categories
--------------

Two main categories of integration schemes exist: **explicit** and **implicit** schemes. A combination of explicit and implicit methods are also possible, it is called semi-implicit or semi-explicit schemes.

### Explicit scheme

An explicit scheme means that the new time step (t + dt) is computed based on information of the previous time step (t):

$$
y(t+dt)=y(t)+dt \cdot f(y(t))
$$

For instance, in mechanics, internal or external forces would be computed on current known positions $x(t)$. The ordinary differential equation looks like:

$$
x(t+dt)=x(t)+dt \cdot v(t)
$$

Explicit schemes are usually known as being fast to solve (since the created linear system is lighter) but they require very small time steps, unless they may undergo stability issues. They are known to efficiently solve non-stiff problems.

Explicit ODESolvers in SOFA:

- [EulerExplicitSolver](../../../components/odesolver/forward/eulerexplicitsolver/)
- [CentralDifferenceSolver](../../../components/odesolver/forward/centraldifferencesolver/)
- [RungeKutta2Solver](../../../components/odesolver/forward/rungekutta2solver/)


### Implicit scheme

An implicit scheme means that the new time step (t + dt) is computed based on information of this next time step (t + dt):

$$
y(t+dt)=y(t)+dt \cdot f(y(t+dt))
$$

For instance, in mechanics, internal or external forces would be computed on unknown positions at the next time step $x(t+dt)$. The ordinary differential equation looks like:

$$
x(t+dt)=x(t)+dt \cdot v(t+dt)
$$

Implicit schemes are known as being slower to solve (the outcoming linear system is more complex) but they are way more stable than explicit schemes. Stiff differential equations require the use of implicit schemes.

Implicit ODESolvers in SOFA:

- [EulerImplicitSolver](../../../components/odesolver/backward/eulerimplicitsolver/)
- [NewmarkImplicitSolver](../../../components/odesolver/backward/newmarkimplicitsolver/)
- [VariationalSymplecticSolver](../../../components/odesolver/backward/variationalsymplecticsolver/)


In the SOFA code
----------------

The integration scheme is described in the `solve()` function of the ODESolver. This *solve()* function is called by the [AnimationLoop](../../animation-loop/) (through a dedicated visitor) and builds the complete linear system $\mathbf{A}x=b$.


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

The left hand side matrix $\mathbf{A}$ is built using the function:
``` cpp
matrix = MechanicalMatrix(r_M, r_B, r_K);
```
where $r_M$ (mass coefficient), $r_B$ (damping coefficient) and $r_K$ (stiffness coefficient) are Rayleigh coefficients (see section below). Depending on the scheme (explicit or implicit, see previous paragraph) and on the type of LinearSolver used (if any), the abstract function `MechanicalMatrix` will trigger different [visitors](../../visitors/), thus different functions to compute the system matrix $\mathbf{A}$. Discover the API used for the computation of $\mathbf{A}$ in the [ForceField](../../multi-model-representation/forcefield/#forcefield-api) and [Mass](../../multi-model-representation/mass/#mass-api) doc pages.


The right hand side vector *b* is built through the function:
``` cpp
computeForce(b)
```

Again, Depending on the scheme (explicit or implicit, see previous paragraph), the abstract function `computeForce` will trigger different [visitors](../../visitors/), thus different functions to accumulate the forces into the vector $b$. Discover the API used for the computation of $b$ in the [ForceField](../../multi-model-representation/forcefield/#forcefield-api) doc page.




### State vectors in ODESolver

In order to build the linear matrix system, the ODESolver uses information contained in [state vectors](../../mechanicalobject/#state-vectors) (like DOFs and their derivatives) within the scope of the ODESolver. The ODESolver does not access the state vectors directly. It accesses the state vectors remotely using visitors, which traverse the graph starting from the node which contains the solver. This keeps the implementation of the solver independent of the simulated objects and their types.

Each type of solver may use different auxiliary state vectors to implement their simulation method. State vectors (MultiVec) are allocated and processed in the scope of the solver in a thread-safe way using an instance of _simulation::common::VectorOperations_. For instance, a Runge-Kutta algorithms needs to save the result of previous time steps.

To create an auxiliary vector, this can be done as follows:

``` cpp
MultiVecCoord pos(&vop, core::VecCoordId::position() ); // standard position vector
MultiVecDeriv acc(&vop);                                // auxiliary vector
MultiVecCoord previousPos(&vop, previousPosID);         // additional vector
```



### Compute the solution

In most cases, the matrix system $\mathbf{A}x=b$ can then be sent to a [LinearSolver](../../system-resolution/linear-solver/) in charge of finally solving the system defined according to the chosen scheme. Within the function *ODESolver::solve()*, the call to the LinearSolver will appear through the function call:

``` cpp
matrix.solve(x, b);
```

Some simple matrix cases provides a diagonal matrix $\mathbf{A}$. In this specific configuration, a solution can directly be found by dividing the right hand side vector *b* by the diagonal matrix $\mathbf{A}$. This is done using the function:
``` cpp
mop.accFromF(acc, f);
```



Rayleigh damping
----------------

The Rayleigh damping is a numerical damping. This damping has therefore no physical meaning and must not be mixed up with physical damping (like _DiagonalVelocityDampingForceField_ in SOFA). The Rayleigh damping corresponds to a damping matrix that is proportional to the mass or/and stiffness matrices using coefficients, respectively Rayleigh stiffness factor $r_K$ or Rayleigh mass factor $r_M$. This numerical damping is usually used to stabilize or ease convergence of the simulation. However, it has to be used carefully.

When Rayleigh damping is used, the damping matrix becomes the sum of the physical and the numerical (Rayleigh) damping: $\mathbf{B} = \mathbf{B}_{\text{phys}} - \mathbf{M} \cdot r_M+ \mathbf{K} \cdot r_K$ where $\mathbf{B}_{\text{phys}}$ is the physical damping matrix, $\mathbf{M}$ is the mass matrix and $\mathbf{K}$ is the stiffness matrix.
The negative sign in front of $\mathbf{M}$, a positive matrix, represents the fact that viscosity opposes motion. Elasticity also opposes it, however $\mathbf{K}$ is a negative matrix. This formula therefore provides two positive coefficients $r_K$ and $r_M$.

You can see the use of Rayleigh mass and stiffness dampings in the `solve()` function of the _EulerImplicit_ class (see EulerImplicitSolver.cpp).
