---
title: StaticSolver
---

StaticSolver  
============  

This component belongs to the category of [integration schemes or ODE Solver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/integration-schemes/).  

In the field of mechanics, statics consists in finding the equilibrium taking into account the loads (internal forces, external forces and torques) acting on the physical system, that do not experience an acceleration ( <img class="latex" src="https://latex.codecogs.com/png.latex?a=0" title="Zero acceleration" /> ). Finding a static equilibrium means finding a solution to: <img class="latex" src="https://latex.codecogs.com/png.latex?\textstyle%20\sum%20F=0" title="Equilibrium" /> where <img class="latex" src="https://latex.codecogs.com/png.latex?F" title="Sum of loads" /> is the sum of all loads, one of which might be unknown.  

In a static analysis, the inertia and damping effects are ignored, i.e. the dynamic effect of the mass is ignored. It can thus be written: <img class="latex" src="https://latex.codecogs.com/png.latex?M=I%20\alpha=0" title="Mass has no effect" />. In the same way, when running a static simulation, time is not elapsing and time steps should rather be considered as convergence steps.  

In a static simulation involving elasticity, the linear system that we solve corresponds to <img class="latex" src="https://latex.codecogs.com/png.latex?K%20\Delta%20u=f" title="Static elasticity" /> where <img class="latex" src="https://latex.codecogs.com/png.latex?K" title="Stiffness matrix" /> is the stiffness matrix (derivative of elastic forces), <img class="latex" src="https://latex.codecogs.com/png.latex?\Delta%20u" title="Total increment of displacement" /> is a vector describing the total increment of displacement and <img class="latex" src="https://latex.codecogs.com/png.latex?f" title="Explicit forces" /> are all explicit forces. We realize here that the static solver is in fact an implicit scheme, since the <img class="latex" src="https://latex.codecogs.com/png.latex?K" title="Stiffness matrix" /> matrix is present in the left-hand side of the equation. The solution <img class="latex" src="https://latex.codecogs.com/png.latex?\Delta%20u" title="Total increment of displacement" /> is obtained iteratively. At each iteration _i_, the displacement is incremented <img class="latex" src="https://latex.codecogs.com/png.latex?\Delta%20u_{i+1}=\Delta%20u_{i}+\delta%20u_i" title="Incrementation of displacement" />, thus resulting in the following system to solve: <img class="latex" src="https://latex.codecogs.com/png.latex?K_i%20\delta%20u_i=f" title="Iterative linear system" />.  

In case of non-linear elasticity, <img class="latex" src="https://latex.codecogs.com/png.latex?K_i" title="Stiffness matrix" /> is a linearization which must be updated with regards to the increment of displacement <img class="latex" src="https://latex.codecogs.com/png.latex?\delta%20u_i" title="Iterative increment of displacement" />. In such cases, several iterations of Newton Raphson are required to find an appropriate approximate solution. In one step of the StaticSolver, the number of Newton Raphson iterations is ruled by the data field **newton_iterations**.

_Reminder_: the [Newton Raphson method](https://en.wikipedia.org/wiki/Newton%27s_method) is an iterative algorithm aiming at finding the solution of the system <img class="latex" src="https://latex.codecogs.com/png.latex?f(x)=0"/> where <img class="latex" src="https://latex.codecogs.com/png.latex?f(x)"/> is non-linear. At each iteration of Newton Raphson algorithm, we find a new approximate solution:

<img class="latex" src="https://latex.codecogs.com/png.latex?x^{n+1}=x^n-\frac{f(x^n)}{f'(x^n)}" title="Newton Raphson method"/> where <img class="latex" src="https://latex.codecogs.com/png.latex?f'(x^n) = \frac{df}{dx}(x^n)"/>

In our elasticity case, the system to solve is <img class="latex" src="https://latex.codecogs.com/png.latex?K_i%20\delta%20u_i-f=0" title="Iterative linear system" />. At each iteration of Newton Raphson algorithm <img class="latex" src="https://latex.codecogs.com/png.latex?n" title="Newton Raphson iteration"/> at simulation step <img class="latex" src="https://latex.codecogs.com/png.latex?i" title="Simulation time step"/>, we therefore find:

<img class="latex" src="https://latex.codecogs.com/png.latex?\delta%20u_i^{n+1}=\delta%20u_i^{n}-\frac{(K_i^n%20\delta%20u_i^n-f)}{K_i^n}" title="Newton Raphson method in static elasticity"/>


Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/StaticSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/StaticSolver.png?raw=true" title="Flow diagram for the StaticSolver"/></a>
 

Data 
----

The solver is ruled by several breaking (converging or diverging) conditions:  

- **correction_tolerance_threshold** is the value of <img class="latex" src="https://latex.codecogs.com/png.latex?|\delta%20u_i^{n}|" title="Unknown of the system"/> under which the Newton Raphson stops and considers the iteration as having converged. This data is homogeneous to the DOFs of the simulation.
- **residual_tolerance_threshold** is the value of <img class="latex" src="https://latex.codecogs.com/png.latex?|f-K_i^n%20\delta%20u_i^n|" title="Unknown of the system"/> under which the Newton Raphson stops and considers the iteration as having converged. This data is homogeneous to loads/forces.
Note that this residual tolerance threshold must be strictly positive.

Two other data fields are availabe:

- **should_diverge_when_residual_is_growing** is an option (bool) stopping the simulation - considered as diverging - as soon as the residual <img class="latex" src="https://latex.codecogs.com/png.latex?|f-K_i^n%20\delta%20u_i^n|" title="Residual"/> is growing
- **newton_iterations** limits the number of Newton Raphson iterations, as stated above.

 
Usage  
-----  

At each simulation step and each Newton Raphson iteration, the StaticSolver **requires**:

- a [LinearSolver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/linear-solvers/) to solve the linear system
- and a MechanicalObject to store the state vectors.

A StaticSolver must be used in simulations where the dynamics has no or a negligible effect on the system. A StaticSolver would also be relevant for systems with low mass. In such case, we fall into the quasi-static analysis.

In some loading configuration, applying the full forces and torques might not lead to any converging simulation. It is then relevant to go for an incremental loading, i.e. loads are applied incrementally at each simulation step  <img class="latex" src="https://latex.codecogs.com/png.latex?i" title="Simulation time step"/>. This incremental loading has to be done in the associated ForceField. If you want to use this solver with Newton Raphson iterations, it is in the user's hand to make sure the external forces used in the scene (pressure, traction, etc.) only get incremented at each time step, and not at each calls to addForce (which is currently the case for most force fields).

 
Example  
-------  
 
This component is used as follows in XML format:  
 
``` xml  
<StaticSolver newton_iterations="10" correction_tolerance_threshold="1e-4" residual_tolerance_threshold="1e-2" should_diverge_when_residual_is_growing="0" />  
```  
 
or using SofaPython3:  
 
``` python  
node.addObject('StaticSolver', newton_iterations='10', correction_tolerance_threshold='1e-4', residual_tolerance_threshold='1e-2', should_diverge_when_residual_is_growing='0')  
```  
 
An example scene involving a StaticSolver is available in [*examples/Component/ODESolver/Backward/StaticSolver.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/ODESolver/Backward/StaticSolver.scn)
