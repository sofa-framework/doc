EulerExplicitSolver  
===================

The EulerExplicitSolver component belongs to the category of [integration schemes or ODE Solver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/integration-schemes/). This scheme allows to solve dynamic systems explicitly: all forces will be computed based on the state information at the current time step <img class="latex" src="https://latex.codecogs.com/png.latex?x(t)" title="Current position"/>.

Looking at continuum mechanics, the linear system <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="Linear system" /> arises from the dynamic equation. This dynamic is written as follows but other physics (like heat transfer) result in a similar equation:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}\Delta%20v=dt\left(f(x,t)\right)" title="Dynamic system" />

where <img class="latex" src="https://latex.codecogs.com/png.latex?x" title="DOF at next time step system" /> is the degrees of freedom, <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}" title="Mass matrix" /> the mass matrix and <img class="latex" src="https://latex.codecogs.com/png.latex?f(x,t)" title="Forces" /> a function of <img class="latex" src="https://latex.codecogs.com/png.latex?x" title="DOF" /> (and possibly its derivatives) acting on our system. In the case of the EulerExplicitSolver, this equation can be written: 

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}\Delta%20v=dt\left(f(x(t))\right)" title="Explicit dynamic system" />

since forces only depend on known state (at our current time step). These forces are computed by the ForceField in the `addForce()` function. The system matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> is only equal to the mass matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}" title="Mass matrix" />.

Depending on whether the mass matrix is diagonal or not, SOFA supports two cases:

1) The mass matrix is diagonal. It makes the resolution of the linear system trivial (best performances). In this case, the system matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> equals a diagonal mass matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}" title="Mass matrix" /> which is diagonal and it can be stored as a vector <img class="latex" src="https://latex.codecogs.com/png.latex?|m|" title="Mass vector" /> . Moreover, its inverse can directly be obtained as: <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}^{-1}=|m|^{-1}=\frac{1}{|m|}" title="Inverse mass matrix" />.
   The solution <img class="latex" src="https://latex.codecogs.com/png.latex?\Delta%20v_{sol}=dt\cdot%20\mathbf{M}^{-1}f(x(t))" title="Explicit resolution" /> finally corresponds to a division operation of <img class="latex" src="https://latex.codecogs.com/png.latex?f(x(t))" title="Explicit forces" /> by the mass. This computation is actually performed by the Mass component in the `accFromF()` function. Therefore, no LinearSolver is needed to compute directly or iteratively a solution.
2) The mass matrix is not diagonal. Solving the system requires a linear solver. 

Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/EulerExplicitSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/EulerExplicitSolver.png?raw=true" title="Flow diagram for a EulerExplicitSolver"/></a>


Data
----

The data **symplectic** allows to modify the scheme to make it [symplectic](https://en.wikipedia.org/wiki/Semi-implicit_Euler_method), i.e. velocities are updated before the positions.
It allows to update the positions from the newly computed velocities, instead of velocities from the previous time step.
This option makes the scheme more robust in time.
EulerExplicitSolver is symplectic by default.

Usage  
-----  

The EulerExplicitSolver **requires** a MechanicalObject to store the state vectors. However, as explained above, no LinearSolver is needed and the EulerExplicitSolver is **only working using a [UniformMass](https://www.sofa-framework.org/community/doc/using-sofa/components/mass/uniformmass/) or [DiagonalMass](https://www.sofa-framework.org/community/doc/using-sofa/components/mass/diagonalmass/)**, which ensures to have a diagonal system matrix.



Example  
-------  

This component is used as follows in XML format:  
 
``` xml  
<EulerExplicitSolver name="odeExplicitSolver" />
```  
 
or using SofaPython3:  
 
``` python  
node.addObject('EulerExplicitSolver', name='odeExplicitSolver')
```  

Examples of scenes involving a EulerExplicitSolver are available in [*examples/Component/ODESolver/Forward/EulerExplicitSolver*](https://github.com/sofa-framework/sofa/tree/master/examples/Component/ODESolver/Forward/EulerExplicitSolver):

- [EulerExplicitSolver.scn](https://github.com/sofa-framework/sofa/blob/master/examples/Component/ODESolver/Forward/EulerExplicitSolver.scn): non-symplectic and non-diagonal mass matrix
- [EulerExplicitSolver_diagonal.scn](https://github.com/sofa-framework/sofa/blob/master/examples/Component/ODESolver/Forward/EulerExplicitSolver_diagonal.scn): non-symplectic and diagonal mass matrix
- [EulerSymplecticSolver.scn](https://github.com/sofa-framework/sofa/blob/master/examples/Component/ODESolver/Forward/EulerSymplecticSolver.scn): symplectic and non-diagonal mass matrix
- [EulerSymplecticSolver_diagonal.scn](https://github.com/sofa-framework/sofa/blob/master/examples/Component/ODESolver/Forward/EulerSymplecticSolver_diagonal.scn): symplectic and diagonal mass matrix
