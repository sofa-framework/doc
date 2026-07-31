EulerImplicitIntegrationScheme  
===================

This component belongs to the category of [integration schemes](../../../../simulation-principles/system-resolution/integration-scheme/). This scheme builds the system following an implicit scheme: forces are considered based on the state information at the next time step $x(t+dt)$, unknown at the current time step.

This is the most broadly used integration scheme thank's to its unconditional stability and simplicity.  

It is recommended to read the theoretical part of the [integration schemes](../../../../simulation-principles/system-resolution/integration-scheme/) page to understand the following. 

The EulerImplicitIntegrationScheme inherits from VelocityBaseIntegrationScheme because its integration scheme in velocity is invertible. Its equations are the following : 

$$
\begin{aligned}
g_{\boldsymbol{x}}^{(t,h)} &: \boldsymbol{v}, \boldsymbol{a} \mapsto \boldsymbol{x}_t + h \boldsymbol{v} \\
g_{\boldsymbol{v}}^{(t,h)} &: \boldsymbol{a} \mapsto \boldsymbol{v}_t + h \boldsymbol{a}
\end{aligned}
$$


#### API specialization

As explained in the [IntegrationScheme](../../../../simulation-principles/system-resolution/integration-scheme/) documentation, the specilization consist in implementing 4 methods that requires the knowledge of four terms/expressions. for Euler implicit they are the following : 
$$
\begin{aligned}
&\tilde{g}_{\boldsymbol{x}}^{(t,h)} \equiv g_{\boldsymbol{x}}^{(t,h)} \\
&g_{\boldsymbol{v}}^{(t,h)-1} : \boldsymbol{v} \mapsto \frac{1}{h}(\boldsymbol{v} - \boldsymbol{v}_t)
\end{aligned}
\qquad \qquad \qquad 
\begin{aligned}
&\frac{\mathrm{d} \tilde{g}_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{v}} = h \\
&\frac{\mathrm{d} g_{\boldsymbol{v}}^{(t,h)-1}}{\mathrm{d} \boldsymbol{v}} = \frac{1}{h}
\end{aligned}
$$


#### Trapezoidal rule

Activating the trapezoidalScheme option of the Euler implicit scheme will make the scheme less dissipative. This will apply the [trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule) to the velocity integration, and thus will increase the order of the time integration, which is known to be less dissipative.
It is also known to increase robustness and stability to the time integration due to the order 2 in time of this trapezoidal scheme. The modified scheme is the following:

$$
\begin{aligned}
g_{\boldsymbol{x}}^{(t,h)} &: \boldsymbol{v}, \boldsymbol{a} \mapsto \boldsymbol{x}_t + \frac{h}{2} \boldsymbol{v_t} + \frac{h}{2} \boldsymbol{v} \\
g_{\boldsymbol{v}}^{(t,h)} &: \boldsymbol{a} \mapsto \boldsymbol{v}_t + h \boldsymbol{a}
\end{aligned}
$$

This results in the updated term: 

$$

\frac{\mathrm{d} \tilde{g}_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{v}} = h/2 
$$

To activate this trapezoidal rule, you need to use the data `trapezoidalScheme=true`.




Usage  
-----  

The EulerImplicitIntegrationScheme **requires**:

- a [LinearSolver](../../../../simulation-principles/system-resolution/linear-solver/) to solve the linear system
- and a MechanicalObject to store the state vectors.

