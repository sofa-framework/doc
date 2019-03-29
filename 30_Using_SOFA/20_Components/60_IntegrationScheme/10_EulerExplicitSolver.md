EulerExplicitSolver  
===================

The EulerExplicitSolver (or EulerSolver) component belongs to the category of [integration schemes or ODE Solver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/integration-schemes/). This scheme allows to solve dynamic systems explicitely: all forces will be computed based on the state information at the current time step <img class="latex" src="https://latex.codecogs.com/png.latex?x(t)" title="Current position"/>.

Looking at continuum mechanics, the linear system <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}x=b$$" title="Linear system" /> arises from the dynamic equation. This dynamic is written as follows but other physics (like heat transfer) result in a similar equation:

<img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{M}\Delta%20v=dt\left(f(x,t)\right)$$" title="Dynamic system" />

where <img class="latex" src="https://latex.codecogs.com/png.latex?$$x$$" title="DOF at next time step system" /> is the degrees of freedom, <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{M}$$" title="Mass matrix" /> the mass matrix and <img class="latex" src="https://latex.codecogs.com/png.latex?$$f(x,t)$$" title="Forces" /> a function of <img class="latex" src="https://latex.codecogs.com/png.latex?$$x$$" title="DOF" /> (and possibly its derivatives) acting on our system. In the case of the EulerExplicitSolver, this equation can be written: 

<img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{M}\Delta%20v=dt\left(f(x(t))\right)$$" title="Explicit dynamic system" />

since forces only depend on known state (at our current time step). These forces are computed by the ForceField in the `addForce()` function. The system matrix <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}$$" title="System matrix" /> is only equal to the mass matrix <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{M}$$" title="Mass matrix" />.

In SOFA, the EulerExplicitSolver only handles diagonal mass matrices, thus making the resolution of the linear system trivial. <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}$$" title="System matrix" /> being only equal to a diagonal mass matrix, the result can easily be computed:

<img class="latex" src="https://latex.codecogs.com/png.latex?$$\Delta%20v_{sol}=dt\mathbf{M}^{-1}f(x(t))$$" title="Explicit resolution" /> where <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{M}^-1$$" title="Inverse mass matrix" /> is only a vector. The division operation of <img class="latex" src="https://latex.codecogs.com/png.latex?f(x(t))" title="Explicit forces" /> by the mass, is actually directly computed by the Mass component in the `accFromF()` function. Therefore, no LinearSolver is needed to compute directly or iteratively a solution.



Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/Images/integrationscheme/EulerExplicitSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/Images/integrationscheme/EulerExplicitSolver.png?raw=true" title="Flow diagram for a EulerExplicitSolver"/></a>


Data
----

The data **symplectic** allows to modify the scheme to make is [symplectic](https://en.wikipedia.org/wiki/Semi-implicit_Euler_method), i.e. velocities are updated before the positions. This option makes the scheme more robust in time.


Usage  
-----  

The EulerExplicitSolver **requires** a MechanicalObject to store the state vectors. However, as explained above, no LinearSolver is needed and the EulerExplicitSolver is **only working using a [UniformMass](https://www.sofa-framework.org/community/doc/using-sofa/components/mass/uniformmass/) or [DiagonalMass](https://www.sofa-framework.org/community/doc/using-sofa/components/mass/diagonalmass/)**, which ensures to have a diagonal system matrix.



Example  
-------  

This component is used as follows in XML format:  
 
``` xml  
<EulerExplicitSolver name="odeExplicitSolver" />
```  
 
or using Python:  
 
``` python  
node.createObject('EulerExplicitSolver', name='odeExplicitSolver')
```  
 
An example scene involving a EulerExplicitSolver is available in [*examples/Components/solver/EulerExplicitSolver.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/solver/EulerExplicitSolver.scn)