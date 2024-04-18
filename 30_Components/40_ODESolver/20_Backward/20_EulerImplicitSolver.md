EulerImplicitSolver  
===================

This component belongs to the category of [integration schemes or ODE Solver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/integration-schemes/). This scheme builds the system following an implicit scheme: forces are considered based on the state information at the next time step <img class="latex" src="https://latex.codecogs.com/png.latex?x(t+dt)" title="Unknown state"/>, unknown at the current time step.

Looking at continuum mechanics, the linear system <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="Linear system" /> arises from the dynamic equation. This dynamic is written as follows but other physics (like heat transfer) result in a similar equation:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}\Delta%20v=dt\left(f(x,t)\right)" title="Dynamic system" />

where <img class="latex" src="https://latex.codecogs.com/png.latex?x" title="DOF at next time step system" /> is the degrees of freedom, <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}" title="Mass matrix" /> the mass matrix and <img class="latex" src="https://latex.codecogs.com/png.latex?f(x,t)" title="Forces" /> a function of <img class="latex" src="https://latex.codecogs.com/png.latex?x" title="DOF" /> (and possibly its derivatives) acting on our system. In the case of the EulerImplicitSolver, this equation can be written: 

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}%20\Delta%20v=dt%20\cdot%20f(x(t+dt))" title="Implicit dynamic system" />

by using a Taylor expansion, we get:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}%20\Delta%20v=dt%20\cdot%20\left(%20f(x(t))+\cdot%20\frac{\partial%20f}{\partial%20x}%20\Delta%20x%20\right)" title="Implicit dynamic system" />

since we have: <img class="latex" src="https://latex.codecogs.com/png.latex?\Delta%20x=dt(v(t)+\Delta%20v)" title="Implicit scheme" />, then:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}\Delta%20v=dt\cdot%20\left(%20f(x(t))+dt\cdot%20\frac{\partial%20f}{\partial%20x}v(t)+dt\cdot%20\frac{\partial%20f}{\partial%20x}%20\Delta%20v%20\right)" title="Implicit dynamic system" />

Finally, gathering the unknown (depending on <img class="latex" src="https://latex.codecogs.com/png.latex?\Delta%20v" title="Unknown delta of velocity" />) in the left hand side, we have:

<img class="latex" src="https://latex.codecogs.com/png.latex?\left(%20\mathbf{M}-dt^2%20\cdot%20\frac{\partial%20f}{\partial%20x}%20\right)%20\Delta%20v=dt\cdot%20f(x(t))+dt^2\cdot%20\frac{\partial%20f}{\partial%20x}v(t)" title="Implicit dynamic system" />

We can notice the appearance of the stiffness matrix : <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{K}_{ij}=\textstyle\frac{\partial%20f_i}{\partial%20x_j}" title="Implicit contribution" />. The stiffness matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{K}" title="Stiffness matrix" /> is a symmetric matrix, can either be linear or non-linear regarding <img class="latex" src="https://latex.codecogs.com/png.latex?x" title="DOF" />.

<img class="latex" src="https://latex.codecogs.com/png.latex?\left(%20\mathbf{M}-dt^2%20\cdot%20\mathbf{K}%20\right)%20\Delta%20v=dt\cdot%20f(x(t))+dt^2\cdot%20\mathbf{K}v(t)" title="Implicit dynamic system" />

The computation of the **right hand side** is done by the ForceFields. Just like in the explicit case (see [EulerExplicitSolver](https://www.sofa-framework.org/community/doc/using-sofa/components/odesolver/eulerexplicitsolver/)), the explicit contribution <img class="latex" src="https://latex.codecogs.com/png.latex?dt\left(f(x(t))\right)" title="Explicit contribution" /> is implemented in the same function `addForce()`. The second part <img class="latex" src="https://latex.codecogs.com/png.latex?dt^2\cdot%20\frac{\partial%20f}{\partial%20x}v(t)" title="Known stiffness" /> is computed by the function `addDForce()`.

It is important to note that, depending on the **choice of LinearSolver** (direct or iterative), the API functions called to build the **left hand side** system matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}=\left(%20M-dt^2%20\cdot%20\frac{\partial%20f}{\partial%20x}%20\right)" title="System matrix" /> will not be the same:

  - if a direct solver is used, the mass <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}" title="Mass matrix" /> is computed in the `addMToMatrix()` and the stiffness part <img class="latex" src="https://latex.codecogs.com/png.latex?-dt^2%20\cdot%20\frac{\partial%20f}{\partial%20x}" title="Stiffness matrix" /> is computed in the function `addKToMatrix()` in ForceFields

  - if an iterative solver is used, the mass is iteratively multiplied by the unknown <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}%20\Delta%20v" title="Mass matrix" /> within the `addMDx()`, as the stiffness part <img class="latex" src="https://latex.codecogs.com/png.latex?-dt^2%20\cdot%20\frac{\partial%20f}{\partial%20x}%20\Delta%20v" title="Stiffness matrix" /> within the function `addDForce()` in ForceFields.


#### Considering viscosity


As you might have notice, the Taylor expansion detailed above does not take into account a possible dependency of the force  <img class="latex" src="https://latex.codecogs.com/png.latex?f(x,t)" title="Forces" /> on the velocity. By considering it, the effect of velocity will result in a viscosity effect through the damping matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{B}" title="Damping matrix" />.

Let's apply the Taylor expansion taking into account the velocity and we get:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}%20\Delta%20v=dt%20\cdot%20\left(%20f(x(t), v(t))+\cdot%20\frac{\partial%20f}{\partial%20x}%20\Delta%20x+\cdot%20\frac{\partial%20f}{\partial%20v}%20\Delta%20v%20\right)" title="Implicit dynamic system with damping" />

<img class="latex" src="https://latex.codecogs.com/png.latex?\left(%20\mathbf{M}-dt%20\cdot%20\frac{\partial%20f}{\partial%20v}-dt^2%20\cdot%20\frac{\partial%20f}{\partial%20x}%20\right)%20\Delta%20v=dt\cdot%20f(x(t),v(t))+dt^2\cdot%20\frac{\partial%20f}{\partial%20x}v(t)" title="Implicit dynamic system with damping" />

<img class="latex" src="https://latex.codecogs.com/png.latex?\left(%20\mathbf{M}-dt%20\cdot%20\mathbf{B}-dt^2%20\cdot%20\mathbf{K}%20\right)%20\Delta%20v=dt\cdot%20f(x(t),v(t))+dt^2\cdot%20\mathbf{K}v(t)" title="Implicit dynamic system with damping" />

Depending on the choice of LinearSolver (direct or iterative), the API functions called to build the <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{B}" title="Damping matrix" /> damping matrix on the left hand side will not be the same:

  - if a direct solver is used, the damping matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{B}" title="Damping matrix" /> is computed in the `addBToMatrix()` in ForceFields

  - if an iterative solver is used, the damping is iteratively multiplied by the unknown <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{B}%20\Delta%20v" title="Damping matrix" /> within the `addDForce()` just as the stiffness part in the function `addDForce()` in ForceFields.



#### Dissipation

SOFA is a framework aiming at interactive simulations. For this purpose, dissipative schemes are very appropriate. The Euler scheme is an order 1 integration scheme (in time, since only using the current state <img class="latex" src="https://latex.codecogs.com/png.latex?x(t)" title="Current DOF" /> and no older one like <img class="latex" src="https://latex.codecogs.com/png.latex?x(t-dt)" title="Older DOF" />). It is known to be a dissipative scheme. Moreover, only one Newton step is performed in the EulerImplicit, which might harm the energy conservation.

Activating the trapezoidalScheme option of the Euler implicit scheme will make the scheme less dissipative. This is due to the fact that the trapezoidal rule increases the order of the time integration. Moreover, higher order schemes are known to be less dissipative.



Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/EulerImplicitSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/EulerImplicitSolver.png?raw=true" title="Flow diagram for the EulerImplicitSolver"/></a>


Data  
----

The data **trapezoidalScheme** modifies the EulerImplicitSolver scheme and implements the [trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule):

<img class="latex" src="https://latex.codecogs.com/png.latex?y_{n+1}-y_n=\frac{dt}{2}(f(y_{n+1})+f(y_n))" title="Trapezoidal rule" />

This results in the following linear system:

<img class="latex" src="https://latex.codecogs.com/png.latex?\left(%20\mathbf{M}-\frac{dt^2}{2}%20\frac{\partial%20f}{\partial%20x}\right)%20\Delta%20v=dt\cdot%20f(x(t))+\frac{dt^2}{2}\cdot%20\frac{\partial%20f}{\partial%20x}v(t)" title="Linear trapezoidal system" />

The use of the trapezoidal rule is known to increase robustness and stability to the time integration due to the order 2 in time of this trapezoidal scheme.

The option is given to the user to add numerical Rayleigh damping using the data **rayleighStiffness** and **rayleighMass**. The description of the meaning and effect of these Rayleigh damping coefficients is given in [ODESolver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/integration-schemes/#rayleigh-damping).

The data **firstOrder** enables to use the EulerImplicitSolver at the order 1, which means that only the first derivative of the DOFs (state) x appears in the equation. Higher derivatives are absent. This option is for instance well suited for heat diffusion equation using only the first derivative of the temperature field:

<img class="latex" src="https://latex.codecogs.com/png.latex?M\frac{\partial%20T}{\partial%20t}=\Delta%20T" title="Heat diffusion" />.



Usage  
-----  

The EulerImplicitSolver **requires**:

- a [LinearSolver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/linear-solvers/) to solve the linear system
- and a MechanicalObject to store the state vectors.


 
Example  
-------  
 
This component is used as follows in XML format:  
 
``` xml  
<EulerImplicitSolver name="ODEsolver" rayleighStiffness="0.1" rayleighMass="0.1" />
```  
 
or using SofaPython3:  
 
``` python  
node.addObject('EulerImplicitSolver', name='ODEsolver', rayleighStiffness='0.1' rayleighMass='0.1')  
```  
 
An example scene involving a StaticSolver is available in [*examples/Component/ODESolver/Backward/EulerImplicitSolver.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/ODESolver/Backward/EulerImplicitSolver.scn)
