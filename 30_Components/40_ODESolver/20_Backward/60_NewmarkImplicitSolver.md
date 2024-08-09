NewmarkImplicitSolver  
=====================

This component belongs to the category of [integration schemes or ODE Solver](../../../simulation-principles/system-resolution/integration-scheme/).  

This scheme is an implicit time integrator for dynamic system using the Newmark scheme. To compute the new position or new velocity, the NewmarkImplicitSolver is based on the following equations:

$$x_{t+h}=x_t+h v_t+\frac{h^2}{2}((1-2\beta)a_t+2\beta a_{t+h})$$

$$v_{t+h}=v_t+h((1-\gamma)a_t+\gamma a_{t+h})$$


Applied to a mechanical system where $$\small Ma_t+(r_MM+r_KK)v_t+Kx_t=f_{ext}$$, we need to solve the following system:


$$\tiny Ma_{t+h}+(r_MM+r_KK)v_{t+h}+Kx_{t+h}=f_{ext}$$

$$\tiny Ma_{t+h}+(r_MM+r_KK)(v_t+h((1-\gamma)a_t+\gamma a_{t+h}))+K(x_t+hv_t+\frac{h^2}{2}((1-2\beta)a_t+2\beta a_{t+h}))=f_{ext}$$

$$\tiny (M+h\gamma(r_MM+r_KK)+h^2\beta K)a_{t+h}=f_{ext}-(r_MM+r_KK)(v_t+h(1-\gamma)a_t)-K(x_t+hv_t+\frac{h^2(1-2\beta)}{2}a_t)$$

$$\tiny ((1+h\gamma r_M)M+(h^2\beta +h\gamma r_K)K)a_{t+h}=f_{ext}-(r_MM+r_KK)v_t-Kx_t-(r_MM+r_KK)(h(1-\gamma)a_t)-K(hv_t+\frac{h^2(1-2\beta)}{2}a_t)$$

$$\tiny ((1+h\gamma r_M)M+(h^2\beta+h\gamma r_K)K)a_{t+h}=a_t-(r_MM+r_KK)(h(1-\gamma)a_t)-K(hv_t+\frac{h^2(1-2\beta)}{2}a_t)$$



Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/NewmarkImplicitSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/NewmarkImplicitSolver.png?raw=true" title="Flow diagram for the NewmarkImplicitSolver"/></a>
 

Usage  
-----  

At each simulation step and each Newton Raphson iteration, the NewmarkImplicitSolver **requires**:

- a [LinearSolver](../../../simulation-principles/system-resolution/linear-solver/) to solve the linear system
- and a MechanicalObject to store the state vectors.
