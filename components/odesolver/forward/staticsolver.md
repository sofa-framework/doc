---
title: StaticSolver
---

StaticSolver  
============  

This component belongs to the category of [integration schemes or ODE Solver](../../../simulation-principles/system-resolution/integration-scheme/).  

In the field of mechanics, statics consists in finding the equilibrium taking into account the loads (internal forces, external forces and torques) acting on the physical system, that do not experience an acceleration ( $$a=0$$ ). Finding a static equilibrium means finding a solution to: $$\textstyle \sum F=0$$ where $$F$$ is the sum of all loads, one of which might be unknown.  

In a static analysis, the inertia and damping effects are ignored, i.e. the dynamic effect of the mass is ignored. It can thus be written: $$M=I \alpha=0$$. In the same way, when running a static simulation, time is not elapsing and time steps should rather be considered as convergence steps.  

In a static simulation involving elasticity, the linear system that we solve corresponds to $$K \Delta u=f$$ where $$K$$ is the stiffness matrix (derivative of elastic forces), $$\Delta u$$ is a vector describing the total increment of displacement and $$f$$ are all explicit forces. We realize here that the static solver is in fact an implicit scheme, since the $$K$$ matrix is present in the left-hand side of the equation. The solution $$\Delta u$$ is obtained iteratively. At each iteration _i_, the displacement is incremented $$\Delta u_{i+1}=\Delta u_{i}+\delta u_i$$, thus resulting in the following system to solve: $$K_i \delta u_i=f$$.  

In case of non-linear elasticity, $$K_i$$ is a linearization which must be updated with regards to the increment of displacement $$\delta u_i$$. In such cases, several iterations of Newton Raphson are required to find an appropriate approximate solution. In one step of the StaticSolver, the number of Newton Raphson iterations is ruled by the data field **newton_iterations**.

_Reminder_: the [Newton Raphson method](https://en.wikipedia.org/wiki/Newton%27s_method) is an iterative algorithm aiming at finding the solution of the system $$f(x)=0"/> where $$f(x)"/> is non-linear. At each iteration of Newton Raphson algorithm, we find a new approximate solution:

$$x^{n+1}=x^n-\frac{f(x^n)}{f'(x^n)}$$ where $$f'(x^n) = \frac{df}{dx}(x^n)"/>

In our elasticity case, the system to solve is $$K_i \delta u_i-f=0$$. At each iteration of Newton Raphson algorithm $$n$$ at simulation step $$i$$, we therefore find:

$$\delta u_i^{n+1}=\delta u_i^{n}-\frac{(K_i^n \delta u_i^n-f)}{K_i^n}$$


Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/StaticSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/StaticSolver.png?raw=true" title="Flow diagram for the StaticSolver"/></a>

 
Usage  
-----  

At each simulation step and each Newton Raphson iteration, the StaticSolver **requires**:

- a [LinearSolver](../../../simulation-principles/system-resolution/linear-solver/) to solve the linear system
- and a MechanicalObject to store the state vectors.

A StaticSolver must be used in simulations where the dynamics has no or a negligible effect on the system. A StaticSolver would also be relevant for systems with low mass. In such case, we fall into the quasi-static analysis.

In some loading configuration, applying the full forces and torques might not lead to any converging simulation. It is then relevant to go for an incremental loading, i.e. loads are applied incrementally at each simulation step  $$i$$. This incremental loading has to be done in the associated ForceField. If you want to use this solver with Newton Raphson iterations, it is in the user's hand to make sure the external forces used in the scene (pressure, traction, etc.) only get incremented at each time step, and not at each calls to addForce (which is currently the case for most force fields).
