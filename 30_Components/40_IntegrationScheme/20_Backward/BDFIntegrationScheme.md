BDFIntegrationScheme
============

This component belongs to the category of [integration schemes](../../../../simulation-principles/system-resolution/integration-scheme/).
It is an implicit method for the numerical integration of the ODE resulting from Newton's second law of motion.

It is recommended to read the theoretical part of the [integration schemes](../../../../simulation-principles/system-resolution/integration-scheme/) page to understand the following. 

The method relies on [Backward Differentiation Formula](https://en.wikipedia.org/wiki/Backward_differentiation_formula) (BDF). This is a special case of [linear multistep method](https://en.wikipedia.org/wiki/Linear_multistep_method).  
To integrate the ODE in time, it uses information from the previous time steps to compute the next step.
It establishes a linear combination of the unknown states, the previous states and the values of the ODE function when applied on those states.

It the specific case of BDF, the coefficients of the linear combination come from the approximation of the function by a Lagrange interpolation polynomial.
The order of the BDF is the number of previous time steps required to approximate the interpolation polynomial.
The first-order BDF requires a single time step in the past to compute the next.
It corresponds to the [backward Euler method](EulerImplicitSolver.md).
The coefficients are unique for a given order, but can be influenced by a change of time step size.
The SOFA component supports any order, and any change of time step size.

In the following we are going to present the generic linear multistep method equations from which BFD derives. It has to be noted that we made the choice to only apply the linear multi step method to the position integration, not on the velocity. Using it to both decreases the stability margin of the integration scheme, leading to big instabilities in the scenes. 

The LinearMultistepIntegrationScheme inherits from VelocityBaseIntegrationScheme because its integration scheme in velocity is invertible. Its equations are the following : 

$$
\begin{aligned}
g_{\boldsymbol{x}}^{(t,h)} &: \boldsymbol{v}, \boldsymbol{a} \mapsto - \sum_{j=1}^{n} \frac{\alpha_j}{\alpha_{n+1}} \boldsymbol{x}_{t-n+j} + h \frac{\beta_{n+1}}{\alpha_{n+1}} \boldsymbol{v} + h \sum_{j=1}^{n} \frac{\beta_j}{\alpha_{n+1}} \boldsymbol{v}_{t-n+j} \\
g_{\boldsymbol{v}}^{(t,h)} &: \boldsymbol{a} \mapsto \boldsymbol{v}_{t} + h \boldsymbol{a}
\end{aligned}
$$

with $n$ the order of the integration scheme

#### API specialization

As explained in the [IntegrationScheme](../../../../simulation-principles/system-resolution/integration-scheme/) documentation, the specilization consist in implementing 4 methods that requires the knowledge of four terms/expressions. for Euler implicit they are the following : 
$$
\begin{aligned}
&\tilde{g}_{\boldsymbol{x}}^{(t,h)} \equiv g_{\boldsymbol{x}}^{(t,h)} \\
&g_{\boldsymbol{v}}^{(t,h)-1} : \boldsymbol{v} \mapsto \frac{\boldsymbol{v} - \boldsymbol{v}_t}{h}
\end{aligned}
\qquad \qquad \qquad 
\begin{aligned}
&\frac{\mathrm{d} \tilde{g}_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{v}} = h \frac{\beta_{n+1}}{\alpha_{n+1}} \\
&\frac{\mathrm{d} g_{\boldsymbol{v}}^{(t,h)-1}}{\mathrm{d} \boldsymbol{v}} = \frac{1}{h}
\end{aligned}
$$


#### BDF implementation

The generic implementation of LinearMultistepIntegrationScheme requires to overide only one virtual funciton being :

```cpp
// Method that will compute the $\alpha$ and $\beta factors$
virtual void computeFactors() = 0;
```

The the implementation of BDFIntegrationScheme only computes those terms using the previously cited Lagrange polynomial interpolation. 


-----  

The BDFIntegrationScheme **requires**:

- a [LinearSolver](../../../../simulation-principles/system-resolution/linear-solver/) to solve the linear system
- and a MechanicalObject to store the state vectors.



