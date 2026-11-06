NewmarkIntegrationScheme  
=====================

This component belongs to the category of [integration schemes](../../../../simulation-principles/system-resolution/integration-scheme/). This scheme builds the system following an implicit scheme: forces are considered based on the state information at the next time step $x(t+dt)$, unknown at the current time step.

It is recommended to read the theoretical part of the [integration schemes](../../../../simulation-principles/system-resolution/integration-scheme/) page to understand the following. 

The Newmark-$\beta$ integration scheme is a parametrized integration scheme. It presents a set of two parameters $\zeta = (\beta, \gamma)$, balancing the 'implicitness' of the solver:
1. With $\zeta =(0,0.5)$, the scheme is an explicit central difference scheme
2. With $\zeta =(0.25,0.5)$ it behaves like an average constant acceleration scheme
3. With $\zeta =(1/6,0.5)$ it behaves like a linear accelerations scheme
4. If $2 \beta \geq \gamma \geq 1/2$, then the Newmark-$\beta$ method is stable regardless of the size of the time-step

It inherits from AccelerationBAsedIntegrationScheme as only the acceleration integration is implicit. Its equations are the following : 

$$
\begin{aligned}
g_{\boldsymbol{x}}^{(t,h)} &: \boldsymbol{v}, \boldsymbol{a} \mapsto \boldsymbol{x}_t + h \boldsymbol{v}_t + h^2\left[\left(\frac{1}{2} - \beta\right)\boldsymbol{a}_t + \beta \boldsymbol{a}\right] \\
g_{\boldsymbol{v}}^{(t,h)} &: \boldsymbol{a} \mapsto \boldsymbol{v}_t + h \left[(1-\gamma)\boldsymbol{a}_t + \gamma \boldsymbol{a}\right]
\end{aligned}
$$ 


#### API specialization

As explained in the [IntegrationScheme](../../../../simulation-principles/system-resolution/integration-scheme/) documentation, the specialization consist in implementing 5 methods that requires the knowledge of four terms/expressions. For Newmark-$\beta$ they are the following : 
$$
\frac{\mathrm{d} g_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{v}} = 0 
\qquad \qquad \qquad 
\frac{\mathrm{d} g_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{a}} = h^2\beta 
\qquad \qquad \qquad 
\frac{\mathrm{d} g_{\boldsymbol{v}}^{(t,h)}}{\mathrm{d} \boldsymbol{a}} = h \gamma 
$$

 

Usage  
-----  

At each simulation step and each Newton Raphson iteration, the NewmarkIntegrationScheme **requires**:

- a [LinearSolver](../../../../simulation-principles/system-resolution/linear-solver/) to solve the linear system
- and a MechanicalObject to store the state vectors.
