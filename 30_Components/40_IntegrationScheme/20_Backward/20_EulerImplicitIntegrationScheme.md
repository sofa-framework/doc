EulerImplicitIntegrationScheme  
===================

This component belongs to the category of [integration schemes](../../../../simulation-principles/system-resolution/integration-scheme/). This scheme builds the system following an implicit scheme: forces are considered based on the state information at the next time step $x(t+dt)$, unknown at the current time step.

This is the most broadly used integration scheme thank's to its unconditional stability (for linear problems) and simplicity.  

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



Usage  
-----  

The EulerImplicitIntegrationScheme **requires**:

- a [LinearSolver](../../../../simulation-principles/system-resolution/linear-solver/) to solve the linear system
- and a MechanicalObject to store the state vectors.
