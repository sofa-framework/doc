EulerImplicitSolver  
===================

This component belongs to the category of [integration schemes or ODE Solver](../../../../simulation-principles/system-resolution/integration-scheme/). This scheme builds the system following an implicit scheme: forces are considered based on the state information at the next time step $$x(t+dt)$$, unknown at the current time step.

Looking at continuum mechanics, the linear system $$\mathbf{A}x=b$$ arises from the dynamic equation. This dynamic is written as follows but other physics (like heat transfer) result in a similar equation:

$$\mathbf{M}\Delta v=dt\left(f(x,t)\right)$$

where $$x$$ is the degrees of freedom, $$\mathbf{M}$$ the mass matrix and $$f(x,t)$$ a function of $$x$$ (and possibly its derivatives) acting on our system. In the case of the EulerImplicitSolver, this equation can be written: 

$$\mathbf{M} \Delta v=dt \cdot f(x(t+dt))$$

by using a Taylor expansion, we get:

$$\mathbf{M} \Delta v=dt \cdot \left( f(x(t))+\cdot \frac{\partial f}{\partial x} \Delta x \right)$$

since we have: $$\Delta x=dt(v(t)+\Delta v)$$, then:

$$\mathbf{M}\Delta v=dt\cdot \left( f(x(t))+dt\cdot \frac{\partial f}{\partial x}v(t)+dt\cdot \frac{\partial f}{\partial x} \Delta v \right)$$

Finally, gathering the unknown (depending on $$\Delta v$$) in the left-hand side, we have:

$$\left( \mathbf{M}-dt^2 \cdot \frac{\partial f}{\partial x} \right) \Delta v=dt\cdot f(x(t))+dt^2\cdot \frac{\partial f}{\partial x}v(t)$$

We can notice the appearance of the stiffness matrix : $$\mathbf{K}_{ij}=\textstyle\frac{\partial f_i}{\partial x_j}$$. The stiffness matrix $$\mathbf{K}$$ is a symmetric matrix, can either be linear or non-linear regarding $$x$$.

$$\left( \mathbf{M}-dt^2 \cdot \mathbf{K} \right) \Delta v=dt\cdot f(x(t))+dt^2\cdot \mathbf{K}v(t)$$

The computation of the **right hand side** is done by the ForceFields. Just like in the explicit case (see [EulerExplicitSolver](../../forward/eulerexplicitsolver/)), the explicit contribution $$dt\left(f(x(t))\right)$$ is implemented in the same function `addForce()`. The second part $$dt^2\cdot \frac{\partial f}{\partial x}v(t)$$ is computed by the function `addDForce()`.

It is important to note that, depending on the **choice of LinearSolver** (direct or iterative), the API functions called to build the **left hand side** system matrix $$\mathbf{A}=\left( M-dt^2 \cdot \frac{\partial f}{\partial x} \right)$$ will not be the same:

  - if a direct solver is used, the mass $$\mathbf{M}$$ is computed in the `addMToMatrix()` and the stiffness part $$-dt^2 \cdot \frac{\partial f}{\partial x}$$ is computed in the function `addKToMatrix()` in ForceFields

  - if an iterative solver is used, the mass is iteratively multiplied by the unknown $$\mathbf{M} \Delta v$$ within the `addMDx()`, as the stiffness part $$-dt^2 \cdot \frac{\partial f}{\partial x} \Delta v$$ within the function `addDForce()` in ForceFields.


#### Considering viscosity


As you might have noticed, the Taylor expansion detailed above does not take into account a possible dependency of the force  $$f(x,t)$$ on the velocity. By considering it, the effect of velocity will result in a viscosity effect through the damping matrix $$\mathbf{B}$$.

Let's apply the Taylor expansion taking into account the velocity and we get:

$$\mathbf{M} \Delta v=dt \cdot \left( f(x(t), v(t))+\cdot \frac{\partial f}{\partial x} \Delta x+\cdot \frac{\partial f}{\partial v} \Delta v \right)$$

$$\left( \mathbf{M}-dt \cdot \frac{\partial f}{\partial v}-dt^2 \cdot \frac{\partial f}{\partial x} \right) \Delta v=dt\cdot f(x(t),v(t))+dt^2\cdot \frac{\partial f}{\partial x}v(t)$$

$$\left( \mathbf{M}-dt \cdot \mathbf{B}-dt^2 \cdot \mathbf{K} \right) \Delta v=dt\cdot f(x(t),v(t))+dt^2\cdot \mathbf{K}v(t)$$

Depending on the choice of LinearSolver (direct or iterative), the API functions called to build the $$\mathbf{B}$$ damping matrix on the left hand side will not be the same:

  - if a direct solver is used, the damping matrix $$\mathbf{B}$$ is computed in the `addBToMatrix()` in ForceFields

  - if an iterative solver is used, the damping is iteratively multiplied by the unknown $$\mathbf{B} \Delta v$$ within the `addDForce()` just as the stiffness part in the function `addDForce()` in ForceFields.



#### Dissipation

SOFA is a framework aiming at interactive simulations. For this purpose, dissipative schemes are very appropriate. The Euler scheme is an order 1 integration scheme (in time, since only using the current state $$x(t)$$ and no older one like $$x(t-dt)$$). It is known to be a dissipative scheme. Moreover, only one Newton step is performed in the EulerImplicit, which might harm the energy conservation.

Activating the trapezoidalScheme option of the Euler implicit scheme will make the scheme less dissipative. This is due to the fact that the [trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule) increases the order of the time integration. Moreover, higher order schemes are known to be less dissipative.
It is also known to increase robustness and stability to the time integration due to the order 2 in time of this trapezoidal scheme. The modified scheme is the following:

$$y_{n+1}-y_n=\frac{dt}{2}(f(y_{n+1})+f(y_n))$$

This results in the following linear system:

$$\left( \mathbf{M}-\frac{dt^2}{2} \frac{\partial f}{\partial x}\right) \Delta v=dt\cdot f(x(t))+\frac{dt^2}{2}\cdot \frac{\partial f}{\partial x}v(t)$$

Finally, with Rayleigh damping, the option is given to the user to add numerical damping. The description of the meaning and effect of these Rayleigh damping coefficients is given in [ODESolver](../../../../simulation-principles/system-resolution/integration-scheme/#rayleigh-damping).


Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/EulerImplicitSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/EulerImplicitSolver.png?raw=true" title="Flow diagram for the EulerImplicitSolver"/></a>




Usage  
-----  

The EulerImplicitSolver **requires**:

- a [LinearSolver](../../../../simulation-principles/system-resolution/linear-solver/) to solve the linear system
- and a MechanicalObject to store the state vectors.

