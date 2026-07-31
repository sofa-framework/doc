Integration Schemes
===================

All dynamic simulations assume to discretize the temporal evolution of the system through small time steps. This time step is usually noted *dt*. An integration scheme is the [numerical method](https://en.wikipedia.org/wiki/Numerical_methods_for_ordinary_differential_equations) describing how to linearly relate the different time derivatives in order to discretize and linearize those ODE.

They are usually called **IntegrationScheme** in SOFA. 

Let's write our ordinary differential equation of a function *y* as follows:

$$
\frac{dy}{dt}=f\left( t,y(t)\right)
$$

IntegrationScheme defines how to go from the current time step (t) to the next (t + dt), which will structure the linear system $\mathbf{A}x=b$. The integration scheme therefore defines which forces impact the left hand side matrix $\mathbf{A}$ and which forces contribute to the right hand side vector *b*:

- explicit contributions depending on the degrees of freedom (DOFs) at the current time step $x(t)$ will contribute to the $b$ vector
- while implicit contributions depending on the degrees of freedom (DOFs) at the next step $x(t+dt)$ (unknown) will contribute to $\mathbf{A}$. 


Two categories
--------------

Two main categories of integration schemes exist: **explicit** and **implicit** schemes. A combination of explicit and implicit methods are also possible, it is called semi-implicit or semi-explicit schemes.

### Explicit scheme

An explicit scheme means that the new time step (t + dt) is computed based on information of the previous time step (t):

$$
y(t+dt)=y(t)+dt \cdot f(y(t))
$$

For instance, in mechanics, internal or external forces would be computed on current known positions $x(t)$. The ordinary differential equation looks like:

$$
x(t+dt)=x(t)+dt \cdot v(t)
$$

Explicit schemes are usually known as being fast to solve (since the created linear system is lighter) but they require very small time steps, unless they may undergo stability issues. They are known to efficiently solve non-stiff problems.

Explicit IntegrationScheme in SOFA:

- [EulerExplicitIntegrationScheme](../../../components/integrationscheme/forward/eulerexplicitintegrationscheme/)
- [CentralDifferenceIntegrationScheme](../../../components/integrationscheme/forward/centraldifferenceintegrationscheme/)
- [RungeKutta2IntegrationScheme](../../../components/integrationscheme/forward/rungekutta2integrationscheme/)


### Implicit scheme

An implicit scheme means that the new time step (t + dt) is computed based on information of this next time step (t + dt):

$$
y(t+dt)=y(t)+dt \cdot f(y(t+dt))
$$

For instance, in mechanics, internal or external forces would be computed on unknown positions at the next time step $x(t+dt)$. The ordinary differential equation looks like:

$$
x(t+dt)=x(t)+dt \cdot v(t+dt)
$$

Implicit schemes are known as being slower to solve (the outcoming linear system is more complex) but they are way more stable than explicit schemes. Stiff differential equations require the use of implicit schemes.

Implicit IntegrationScheme in SOFA:

- [EulerImplicitIntegrationScheme](../../../components/integrationscheme/backward/eulerimplicitintegrationscheme/)
- [NewmarkImplicitIntegrationScheme](../../../components/integrationscheme/backward/newmarkimplicitintegrationscheme/)
- [BDFIntegrationScheme](../../../components/integrationscheme/backward/variationalsymplecticintegrationscheme/)


Solving for non linearities
----------------

As it has been seen, integrating through time boils down to building and solving a linear system. What is hidden behind this is that the mechanics needs to be linearized to be summarized in a linear system. While it has no effect for linear elasticity, it can result in pretty bad dynamics in the case of hyperelasticity. 

For explicit integration scheme, there is no strategy other than reducing the timestep to try to improve such non-linearities. But, because of the nature of implicit integration scheme, one can take advantage of using a non-linear solver to compute the integration in order to better take into account the non-linearities.

The current design of Implicit integration scheme is based on this finding to enable the use of Newton-Raphson solver at the level of the simulation to compute dynamics. But to present it let's first dive into what it takes to use a Newton-Raphson solver : we need to express the time step as a root-finding problem. 

> **Note :**\
> Currently, SOFA doesn't propose any Newton-Raphson algorithm able to solve for non-linear mechanics. It is an ongoing work that'll be release soon. But the refactoring of the ODE solver has been made in order to enable such new solver to be implemented. It is thus important to explain the design choices at the light of future development. 

### 1) From Dynamic equations to root finding problem

First let's introduce the dynamic equations we wish to solve. 

$$
\boldsymbol{M}\boldsymbol{a} = \mathcal{F}(\boldsymbol{x},\boldsymbol{v}) + \boldsymbol{F_{\text{ext}}}
\tag{1.1}
$$
With $\boldsymbol{a}$ the acceleration, $\boldsymbol{M}$ the mass matrix and $\mathcal{F}(\boldsymbol{x},\boldsymbol{v})$ being a non linear function of the position ($\boldsymbol{x}$) and velocity ($\boldsymbol{v}$).

Now let's consider that we have the solution to this equation at a time $t$. This means having the tensor $\boldsymbol{X}_t = (\boldsymbol{x}_t, \boldsymbol{v}_t, \boldsymbol{a}_t)$ that satisfy @eq:eq-dyn. In order to integrate the unknown along time and know their value at a future timestamp $t + h$, we need to introduce a relationship between the three unknown. Indeed, with only one equation but three unknown (position, velocity and acceleration), we need to introduce more equations to get a solvable system. This set of new equations is exactly the _integration scheme_ and can be defined as the following functions.

$$

\begin{aligned}
g_{\boldsymbol{x}}^{(t,h)} &: (\boldsymbol{v}_{t+h}, \boldsymbol{a}_{t+h}) &\mapsto \boldsymbol{x}_{t+h} \\
g_{\boldsymbol{v}}^{(t,h)} &: (\boldsymbol{a}_{t+h}) &\mapsto \boldsymbol{v}_{t+h}
\tag{1.2}
\end{aligned}
$$

Now one can rewrite the set of equations to be solved : 

$$
\begin{cases}
\boldsymbol{M}\boldsymbol{a}_{t+h} &= \mathcal{F}(\boldsymbol{x}_{t+h},\boldsymbol{v}_{t+h}) + \boldsymbol{F_{\text{ext}}} \\
\boldsymbol{x}_{t+h} &= g_{\boldsymbol{x}}^{(t,h)}(\boldsymbol{v}_{t+h}, \boldsymbol{a}_{t+h}) \\
\boldsymbol{v}_{t+h} &= g_{\boldsymbol{v}}^{(t,h)}(\boldsymbol{a}_{t+h})
\end{cases}
\tag{1.3}
$$
With the unknown $\boldsymbol{X}_{t+h} = (\boldsymbol{x}_{t+h}, \boldsymbol{v}_{t+h}, \boldsymbol{a}_{t+h})$.

#### 1.1) General form
Let define a function $\mathcal{G}_{t} (\boldsymbol{X}_{t+h} = (\boldsymbol{x}_{t+h}, \boldsymbol{v}_{t+h}, \boldsymbol{a}_{t+h}))$ such as its root is the solution of the set of equation (1.3):
$$
\mathcal{G}_{t}(\boldsymbol{X} = (\boldsymbol{x}, \boldsymbol{v}, \boldsymbol{a}))) =
\begin{cases}
\boldsymbol{M}\boldsymbol{a} - \mathcal{F}(\boldsymbol{x},\boldsymbol{v}) - \boldsymbol{F_{\text{ext}}} \\
\boldsymbol{x} - g_{\boldsymbol{x}}^{(t,h)}(\boldsymbol{v}, \boldsymbol{a}) \\
\boldsymbol{v} - g_{\boldsymbol{v}}^{(t,h)}(\boldsymbol{a})
\end{cases}
\tag{1.4}
$$
We will see later that using this general form ends up in solving for the difference in acceleration in one timestep. We will call the family of integration scheme using this forme the **_Velocity-based integration schemes_**.

#### 1.2) Simplified form
To simplify this set of equation, if $g_v^{(t,h)}$ is invertible, one can rewrite the set as : 
$$
\begin{cases}
\boldsymbol{M}g_{\boldsymbol{v}}^{(t,h)-1}(\boldsymbol{v}_{t+h}) &= \mathcal{F}(\boldsymbol{x}_{t+h},\boldsymbol{v}_{t+h}) + \boldsymbol{F_{\text{ext}}} \\
\boldsymbol{x}_{t+h} &= \tilde{g}_{\boldsymbol{x}}^{(t,h)}(\boldsymbol{v}_{t+h})
\end{cases}
\tag{1.5}
$$
With $\tilde{g}_{\boldsymbol{x}}^{(t,h)}(\boldsymbol{v}_{t+h}) = g_{\boldsymbol{x}}^{(t,h)}(\boldsymbol{v}_{t+h}, g_v^{(t,h)-1}(\boldsymbol{v}_{t+h}))$. We will use this simplified form for the following equations. 
Let define a function $\mathcal{G}_{t} (\tilde{\boldsymbol{X}}_{t+h} = (\boldsymbol{x}_{t+h}, \boldsymbol{v}_{t+h}))$ such as its root is still the solution of (1.3):
$$
\mathcal{G}_{t}(\tilde{\boldsymbol{X}} = (\boldsymbol{x}, \boldsymbol{v})) =
\begin{cases}
\boldsymbol{M}g_v^{(t,h)-1}(\boldsymbol{v}) - \mathcal{F}(\boldsymbol{x},\boldsymbol{v}) - \boldsymbol{F_{\text{ext}}} \\
\boldsymbol{x} - \tilde{g}_{x}^{(t,h)}(\boldsymbol{v})
\end{cases}
\tag{1.6}
$$
To find the root of such non-linear function, one way to do it is to use a non-linear root finder, the most common one is the Newton-Raphson algorithm


### 2) Newton-Raphson equations
#### 2.1) Basics on Newton-Raphson

The Newton-Raphson algorithm is an iterative algorithm which goal is to find the root of a non-linear function that is at least $\mathscr{C}^1$ and has values in $\mathbb{R}^p$. For the sake of simplicity we will consider $n = p$ for the rest of this document (the main difference lying in the invertibility of the Jacobian of the function, when $n \neq p$ or when the Jacobian is not invertible a pseudo inverse must be used).
Let consider a $\mathscr{C}^1$ non-linear function  $\mathcal{G} : \mathbb{R}^n \mapsto \mathbb{R}^n$. Given a current guess $\boldsymbol{X}^{(i)}$, the goal of the algorithm is to find $\mathrm{d}\boldsymbol{X}^{(i)}$ such as
$$
\mathcal{G}(\boldsymbol{X}^{(i+1)}) = \mathcal{G}(\boldsymbol{X}^{(i)} + \mathrm{d}\boldsymbol{X}^{(i)}) = 0
$$
To do this the function $\mathcal{G}$ is linearized at the current guess to express the previous equation as a linear equation. 
$$
\mathcal{G}(\boldsymbol{X}^{(i)} + \mathrm{d}\boldsymbol{X}^{(i)}) \approx \mathcal{G}(\boldsymbol{X}^{(i)}) + \left.\frac{\partial \mathcal{G}}{\partial \boldsymbol{X}}\right|_{\boldsymbol{X}^{(i)}} \cdot \mathrm{d}\boldsymbol{X}^{(i)} = 0
$$
$$
\mathrm{d}\boldsymbol{X}^{(i)} = - \left.\frac{\partial \mathcal{G}}{\partial \boldsymbol{X}}\right|_{\boldsymbol{X}^{(i)}}^{-1} \cdot \mathcal{G}(\boldsymbol{X}^{(i)})
\tag{2.1}
$$
With $\frac{\partial \mathcal{G}}{\partial \boldsymbol{X}}$ being the Jacobian of the function $\mathcal{G}$ :
$$
\frac{\partial \mathcal{G}}{\partial \boldsymbol{X}} = 
\begin{pmatrix}
\frac{\partial \mathcal{G}_0}{\partial \boldsymbol{X}_0} & \frac{\partial \mathcal{G}_0}{\partial \boldsymbol{X}_1} & \dots & \frac{\partial \mathcal{G}_0}{\partial \boldsymbol{X}_n} \\
\frac{\partial \mathcal{G}_1}{\partial \boldsymbol{X}_0} & \frac{\partial \mathcal{G}_1}{\partial \boldsymbol{X}_1} & \dots & \frac{\partial \mathcal{G}_1}{\partial \boldsymbol{X}_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial \mathcal{G}_n}{\partial \boldsymbol{X}_0} & \frac{\partial \mathcal{G}_n}{\partial \boldsymbol{X}_1} & \dots & \frac{\partial \mathcal{G}_n}{\partial \boldsymbol{X}_n}
\end{pmatrix}
$$
Then the current guess is updated according to 
$$
\boldsymbol{X}^{(i+1)} = \boldsymbol{X}^{(i)} + \mathrm{d}\boldsymbol{X}^{(i)}
\tag{2.2}
$$
The algorithm stops when the norm of the current residue $\|\boldsymbol{r}^{(i)}\| = \|\mathcal{G}(\boldsymbol{X}^{(i)})\|$ is under a certain threshold $\epsilon \in \mathbb{R}$


#### 2.2) Newton-Raphson for dynamic equations of motion
##### 2.2.1) Acceleration-based integration scheme
In the case of dynamic equations of motion, we have defined the function for which we want to find the root (1.4). Now we are going to write the recurrence relations resulting for the application of a Newton-Raphson algorithm to this problem. 

By applying (2.1) to (1.4) we can compute the final linear system to solve:

$$
\left.\frac{\partial \mathcal{G}_{t}}{\partial \boldsymbol{X}}\right|_{\boldsymbol{X}^{(i)}} \mathrm{d}\boldsymbol{X}^{(i)} = - \mathcal{G}_{t}(\boldsymbol{X}^{(i)})
$$

Let's take a look closer to the Jacobian.

$$
\begin{aligned}
\left.\frac{\partial \mathcal{G}_{t}}{\partial \boldsymbol{X}}\right|_{\boldsymbol{X}^{(i)}} &= 
\begin{pmatrix}
\left.\frac{\partial \mathcal{G}_{t,0}}{\partial \boldsymbol{X}_{\boldsymbol{x}}}\right|_{\boldsymbol{X}^{(i)}} & \left.\frac{\partial \mathcal{G}_{t,0}}{\partial \boldsymbol{X}_{\boldsymbol{v}}}\right|_{\boldsymbol{X}^{(i)}} & \left.\frac{\partial \mathcal{G}_{t,0}}{\partial \boldsymbol{X}_{\boldsymbol{a}}}\right|_{\boldsymbol{X}^{(i)}} \\
\left.\frac{\partial \mathcal{G}_{t,1}}{\partial \boldsymbol{X}_{\boldsymbol{x}}}\right|_{\boldsymbol{X}^{(i)}} & \left.\frac{\partial \mathcal{G}_{t,1}}{\partial \boldsymbol{X}_{\boldsymbol{v}}}\right|_{\boldsymbol{X}^{(i)}} & \left.\frac{\partial \mathcal{G}_{t,1}}{\partial \boldsymbol{X}_{\boldsymbol{a}}}\right|_{\boldsymbol{X}^{(i)}} \\
\left.\frac{\partial \mathcal{G}_{t,2}}{\partial \boldsymbol{X}_{\boldsymbol{x}}}\right|_{\boldsymbol{X}^{(i)}} & \left.\frac{\partial \mathcal{G}_{t,2}}{\partial \boldsymbol{X}_{\boldsymbol{v}}}\right|_{\boldsymbol{X}^{(i)}} & \left.\frac{\partial \mathcal{G}_{t,2}}{\partial \boldsymbol{X}_{\boldsymbol{a}}}\right|_{\boldsymbol{X}^{(i)}}
\end{pmatrix} \\
&= 
\begin{pmatrix}
-\left.\frac{\partial \mathcal{F}}{\partial \boldsymbol{x}}\right|_{\boldsymbol{X}^{(i)}} & \quad - \left.\frac{\partial \mathcal{F}}{\partial \boldsymbol{v}}\right|_{\boldsymbol{X}^{(i)}} & \quad \boldsymbol{M} \\
I & \quad -\left.\frac{\mathrm{d} g_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{v}}\right|_{\boldsymbol{X}^{(i)}} & \quad -\left.\frac{\mathrm{d} g_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{a}}\right|_{\boldsymbol{X}^{(i)}} \\
0 & \quad I & \quad -\left.\frac{\mathrm{d} g_{\boldsymbol{v}}^{(t,h)}}{\mathrm{d} \boldsymbol{a}}\right|_{\boldsymbol{X}^{(i)}}
\end{pmatrix}
\end{aligned}
$$

We can already identify two common mechanical matrices : 
$$
\begin{cases}
\boldsymbol{K}^{(i)} = \left.\frac{\partial \mathcal{F}}{\partial \boldsymbol{x}}\right|_{\boldsymbol{X}^{(i)}} \\
\boldsymbol{B}^{(i)} = \left.\frac{\partial \mathcal{F}}{\partial \boldsymbol{v}}\right|_{\boldsymbol{X}^{(i)}}
\end{cases}
$$

We are going to inverse this linear system by bloc by injecting the last equation into the second one. This is done by first inverting the last equation with respect to $\mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{v}}$.
$$
\mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{v}} = \left.\frac{\mathrm{d} g_{\boldsymbol{v}}^{(t,h)}}{\mathrm{d} \boldsymbol{a}}\right|_{\boldsymbol{X}^{(i)}} \mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{a}} - \mathcal{G}_{t}(\boldsymbol{X}^{(i)})_2
$$

Then we can inject it back to the second equation and then invert it again with respect to $\mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{x}}$
$$
\begin{aligned}
\mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{x}} &= \left.\frac{\mathrm{d} g_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{v}}\right|_{\boldsymbol{X}^{(i)}} \left(\left.\frac{\mathrm{d} g_{\boldsymbol{v}}^{(t,h)}}{\mathrm{d} \boldsymbol{a}}\right|_{\boldsymbol{X}^{(i)}} \mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{a}} - \mathcal{G}_{t}(\boldsymbol{X}^{(i)})_2\right) + \left.\frac{\mathrm{d} g_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{a}}\right|_{\boldsymbol{X}^{(i)}} \mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{a}} - \mathcal{G}_{t}(\boldsymbol{X}^{(i)})_1 \\
&= \left(\left.\frac{\mathrm{d} g_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{v}}\right|_{\boldsymbol{X}^{(i)}}\left.\frac{\mathrm{d} g_{\boldsymbol{v}}^{(t,h)}}{\mathrm{d} \boldsymbol{a}}\right|_{\boldsymbol{X}^{(i)}} + \left.\frac{\mathrm{d} g_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{a}}\right|_{\boldsymbol{X}^{(i)}}\right) \mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{a}} - \left.\frac{\mathrm{d} g_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{v}}\right|_{\boldsymbol{X}^{(i)}}\mathcal{G}_{t}(\boldsymbol{X}^{(i)})_2 - \mathcal{G}_{t}(\boldsymbol{X}^{(i)})_1
\end{aligned}
$$


Let define the following coefficients
$$
\begin{aligned}
\text{DG}^{(i)}_{\boldsymbol{v}} &= \left.\frac{\mathrm{d} g_{\boldsymbol{v}}^{(t,h)}}{\mathrm{d} \boldsymbol{a}}\right|_{\boldsymbol{X}^{(i)}} \\
\text{DG}^{(i)}_{\boldsymbol{x}} &= \left(\left.\frac{\mathrm{d} g_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{v}}\right|_{\boldsymbol{X}^{(i)}} \left.\frac{\mathrm{d} g_{\boldsymbol{v}}^{(t,h)}}{\mathrm{d} \boldsymbol{a}}\right|_{\boldsymbol{X}^{(i)}} + \left.\frac{\mathrm{d} g_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{a}}\right|_{\boldsymbol{X}^{(i)}}\right)
\end{aligned}
$$
We can inject the two expressions of $\mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{x}}$ and $\mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{v}}$ into the first equation :
$$
\begin{aligned}
&-\boldsymbol{K}^{(i)}\mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{x}} - \boldsymbol{B}^{(i)}\mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{v}} + \boldsymbol{M} \mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{a}} = -\mathcal{G}_{t}(\boldsymbol{X}^{(i)})_0 \\
\Longleftrightarrow\quad& -\boldsymbol{K}^{(i)} \left(\text{DG}^{(i)}_{\boldsymbol{x}} \mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{a}} - \left.\frac{\mathrm{d} g_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{v}}\right|_{\boldsymbol{X}^{(i)}}\mathcal{G}_{t}(\boldsymbol{X}^{(i)})_2 - \mathcal{G}_{t}(\boldsymbol{X}^{(i)})_1\right) - \boldsymbol{B}^{(i)} \left(\text{DG}^{(i)}_{\boldsymbol{v}} \mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{a}} - \mathcal{G}_{t}(\boldsymbol{X}^{(i)})_2\right) + \boldsymbol{M} \mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{a}} = -\mathcal{G}_{t}(\boldsymbol{X}^{(i)})_0 \\
\Longleftrightarrow\quad& (\boldsymbol{M} -\boldsymbol{K}^{(i)}\cdot\text{DG}^{(i)}_{\boldsymbol{x}} - \boldsymbol{B}^{(i)} \text{DG}^{(i)}_{\boldsymbol{v}})\mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{a}} = -\mathcal{G}_{t}(\boldsymbol{X}^{(i)})_0-\boldsymbol{K}^{(i)} \mathcal{G}_{t}(\boldsymbol{X}^{(i)})_1 - \left(\boldsymbol{B}^{(i)} + \boldsymbol{K}^{(i)}\left.\frac{\mathrm{d} g_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{v}}\right|_{\boldsymbol{X}^{(i)}}\right) \mathcal{G}_{t}(\boldsymbol{X}^{(i)})_2
\end{aligned}
$$

To summarize, the update strategy is as follow : 
$$
\begin{cases}
\mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{a}} &= (\boldsymbol{M} -\boldsymbol{K}^{(i)}\cdot\text{DG}^{(i)}_{\boldsymbol{x}} - \boldsymbol{B}^{(i)} \text{DG}^{(i)}_{\boldsymbol{v}})^{(-1)} \left(-\mathcal{G}_{t}(\boldsymbol{X}^{(i)})_0-\boldsymbol{K}^{(i)} \mathcal{G}_{t}(\boldsymbol{X}^{(i)})_1 - \left(\boldsymbol{B}^{(i)} + \boldsymbol{K}^{(i)}\left.\frac{\mathrm{d} g_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{v}}\right|_{\boldsymbol{X}^{(i)}}\right)\cdot \mathcal{G}_{t}(\boldsymbol{X}^{(i)})_2\right) \\
\mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{v}} &= \text{DG}^{(i)}_{\boldsymbol{v}} \mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{a}} - \mathcal{G}_{t}(\boldsymbol{X}^{(i)})_2 \\
\mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{x}} &= \left.\frac{\mathrm{d} g_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{v}}\right|_{\boldsymbol{X}^{(i)}} \mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{v}} + \left.\frac{\mathrm{d} g_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{a}}\right|_{\boldsymbol{X}^{(i)}} \mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{a}} - \mathcal{G}_{t}(\boldsymbol{X}^{(i)})_1 \\
&= \text{DG}^{(i)}_{\boldsymbol{x}} \mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{a}} - \left.\frac{\mathrm{d} g_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{v}}\right|_{\boldsymbol{X}^{(i)}}\mathcal{G}_{t}(\boldsymbol{X}^{(i)})_2 - \mathcal{G}_{t}(\boldsymbol{X}^{(i)})_1 \\
\boldsymbol{X}^{(i+1)} &= \boldsymbol{X}^{(i)} + \begin{pmatrix} \mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{x}} \\ \mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{v}} \\ \mathrm{d}\boldsymbol{X}^{(i)}_{\boldsymbol{a}} \end{pmatrix}
\end{cases}
\tag{2.3}
$$


##### 2.2.1) Velocity-based integration scheme
In the case of velocity-based equations of motion, we have defined the function for which we want to find the root (1.6). Now we are going to write the recurrence relations resulting for the application of a Newton-Raphson algorithm to this problem. 
By applying (2.1) to (1.6) we can compute the final linear system to solve:
$$
\left.\frac{\partial \mathcal{G}_{t}}{\partial \tilde{\boldsymbol{X}}}\right|_{\tilde{\boldsymbol{X}}^{(i)}} \mathrm{d}\tilde{\boldsymbol{X}}^{(i)} = - \mathcal{G}_{t}(\tilde{\boldsymbol{X}}^{(i)})
$$
Let's take a look closer to the Jacobian.
$$
\begin{aligned}
\left.\frac{\partial \mathcal{G}_{t}}{\partial \tilde{\boldsymbol{X}}}\right|_{\tilde{\boldsymbol{X}}^{(i)}} &= 
\begin{pmatrix}
\left.\frac{\partial \mathcal{G}_{t,0}}{\partial \tilde{\boldsymbol{X}}_{\boldsymbol{x}}}\right|_{\tilde{\boldsymbol{X}}^{(i)}} & \left.\frac{\partial \mathcal{G}_{t,0}}{\partial \tilde{\boldsymbol{X}}_{\boldsymbol{v}}}\right|_{\tilde{\boldsymbol{X}}^{(i)}} \\
\left.\frac{\partial \mathcal{G}_{t,1}}{\partial \tilde{\boldsymbol{X}}_{\boldsymbol{x}}}\right|_{\tilde{\boldsymbol{X}}^{(i)}} & \left.\frac{\partial \mathcal{G}_{t,1}}{\partial \tilde{\boldsymbol{X}}_{\boldsymbol{v}}}\right|_{\tilde{\boldsymbol{X}}^{(i)}}
\end{pmatrix} \\
&= 
\begin{pmatrix}
-\left.\frac{\partial \mathcal{F}}{\partial \boldsymbol{x}}\right|_{\tilde{\boldsymbol{X}}^{(i)}} & \quad \boldsymbol{M} \left.\frac{\mathrm{d} g_{\boldsymbol{v}}^{(t,h)-1}}{\mathrm{d} \boldsymbol{v}}\right|_{\tilde{\boldsymbol{X}}^{(i)}} - \left.\frac{\partial \mathcal{F}}{\partial \boldsymbol{v}}\right|_{\tilde{\boldsymbol{X}}^{(i)}} \\
I & \quad -\left.\frac{\mathrm{d} \tilde{g}_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{v}}\right|_{\tilde{\boldsymbol{X}}^{(i)}}
\end{pmatrix}
\end{aligned}
$$
We can already identify two common mechanical matrices : 
$$
\begin{cases}
\boldsymbol{K}^{(i)} = \left.\frac{\partial \mathcal{F}}{\partial \boldsymbol{x}}\right|_{\tilde{\boldsymbol{X}}^{(i)}} \\
\boldsymbol{B}^{(i)} = \left.\frac{\partial \mathcal{F}}{\partial \boldsymbol{v}}\right|_{\tilde{\boldsymbol{X}}^{(i)}}
\end{cases}
$$
This linear system by bloc can be solved using a Shur complement method. Here we have a special case where all blocks are squared. So we can do a development using the bottom left block:
$$
\mathrm{d}\tilde{\boldsymbol{X}}^{(i)}_{\boldsymbol{x}} = \left.\frac{\mathrm{d} \tilde{g}_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{v}}\right|_{\tilde{\boldsymbol{X}}^{(i)}} \cdot \mathrm{d}\tilde{\boldsymbol{X}}^{(i)}_{\boldsymbol{v}} - \mathcal{G}_{t}(\tilde{\boldsymbol{X}}^{(i)})_1
$$
And by injecting this into the first equation we get :
$$
\begin{aligned}
& -\boldsymbol{K}^{(i)} \left(\left.\frac{\mathrm{d} \tilde{g}_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{v}}\right|_{\tilde{\boldsymbol{X}}^{(i)}} \cdot \mathrm{d}\tilde{\boldsymbol{X}}^{(i)}_{\boldsymbol{v}} - \mathcal{G}_{t}(\tilde{\boldsymbol{X}}^{(i)})_1\right) + \left(\boldsymbol{M} \left.\frac{\mathrm{d} g_{\boldsymbol{v}}^{(t,h)-1}}{\mathrm{d} \boldsymbol{v}}\right|_{\tilde{\boldsymbol{X}}^{(i)}} - \boldsymbol{B}^{(i)}\right)\mathrm{d}\tilde{\boldsymbol{X}}^{(i)}_{\boldsymbol{v}} = - \mathcal{G}_{t}(\tilde{\boldsymbol{X}}^{(i)})_0 \\
\Longleftrightarrow & \left( \boldsymbol{M} \left.\frac{\mathrm{d} g_{\boldsymbol{v}}^{(t,h)-1}}{\mathrm{d} \boldsymbol{v}}\right|_{\tilde{\boldsymbol{X}}^{(i)}} - \boldsymbol{K}^{(i)} \left.\frac{\mathrm{d} \tilde{g}_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{v}}\right|_{\tilde{\boldsymbol{X}}^{(i)}} - \boldsymbol{B}^{(i)}\right) \mathrm{d}\tilde{\boldsymbol{X}}^{(i)}_{\boldsymbol{v}} = -\boldsymbol{K}^{(i)} \mathcal{G}_{t}(\tilde{\boldsymbol{X}}^{(i)})_1 - \mathcal{G}_{t}(\tilde{\boldsymbol{X}}^{(i)})_0
\end{aligned}
\tag{2.4}
$$
To summarize, the update strategy is as follow : 
$$
\begin{cases}
\mathrm{d}\tilde{\boldsymbol{X}}^{(i)}_{\boldsymbol{v}} &= \left( \boldsymbol{M} \left.\frac{\mathrm{d} g_{\boldsymbol{v}}^{(t,h)-1}}{\mathrm{d} \boldsymbol{v}}\right|_{\tilde{\boldsymbol{X}}^{(i)}} - \boldsymbol{K}^{(i)} \left.\frac{\mathrm{d} \tilde{g}_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{v}}\right|_{\tilde{\boldsymbol{X}}^{(i)}} - \boldsymbol{B}^{(i)}\right)^{-1} \left(-\boldsymbol{K}^{(i)} \mathcal{G}_{t}(\tilde{\boldsymbol{X}}^{(i)})_1 - \mathcal{G}_{t}(\tilde{\boldsymbol{X}}^{(i)})_0\right) \\
\mathrm{d}\tilde{\boldsymbol{X}}^{(i)}_{\boldsymbol{x}} &= \left.\frac{\mathrm{d} \tilde{g}_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{v}}\right|_{\tilde{\boldsymbol{X}}^{(i)}} \cdot \mathrm{d}\tilde{\boldsymbol{X}}^{(i)}_{\boldsymbol{v}} - \mathcal{G}_{t}(\tilde{\boldsymbol{X}}^{(i)})_1 \\
\tilde{\boldsymbol{X}}^{(i+1)} &= \tilde{\boldsymbol{X}}^{(i)} + \begin{pmatrix} \mathrm{d}\tilde{\boldsymbol{X}}^{(i)}_{\boldsymbol{x}} \\ \mathrm{d}\tilde{\boldsymbol{X}}^{(i)}_{\boldsymbol{v}} \end{pmatrix}
\end{cases}
\tag{2.5}
$$


The SOFA implementation
----------------

### Design choices
In the light of the presented Newton-Raphson algorithm and the associated equations, the design for implicit intergation scheme is now clearer : it needs an API that enable the computation of such iterative algorithm, meaning that we need to be able compute the right-hand-side of the linearized equation independently from the left-hand-side, and also update the solution independently. This choice has lead to the following API interface:

#### ImplicitIntegrationScheme
This base class inherits directly from the class `BaseIntegrationScheme` and proposes the virtual API taht'll be implemented by the different implicit integrations chemes. Here is the list of thoses methods :

```cpp
    //This method purpose is to enable the integration scheme to prepare internal state before beginning the solving step. (Not pure virtual)
    virtual void doSetupIntegrationStep(...) {}

    // Compute the system matrix. The boolean i shere to avoid computin zero-valued vectors after the first iteration (i.e. such as the integration scheme error which is always null after one iteration)
    virtual void computeLHS(bool firstIteration = false) = 0;

    // compute the current RHS.
    virtual void computeRHS(bool firstIteration = false) = 0;

    // Returns the evaluation of the residual
    virtual SReal evaluateResidual() = 0;

    // Solve the linear equation from a Newton iteration, i.e. it computes (x^{i+1}-x^i).
    virtual void solveLinearEquation() = 0;

    // Use the computed unknown to update state accordingly. The alpha parameter is here to implement line search
    virtual void updateStatesFromLinearSolution(SReal alpha, bool firstIteration = false) = 0;

    //This method is called after the integration step is completed. (Not pure virutal)
    virtual void finalizeIntegrationStep() {}

    // This method comes form the BaseIntegrationScheme API, it is a monolithic step integration.
    virtual void integrate(...) override;

    // This methods returns the factor to put in front of the linear system unknown accumulating it to the velocity.
    // In the case of acceleration-based integration scheme, we can see in (2.3) that this should return $DG_v$
    virtual SReal getVelocityIntegrationFactor() const = 0;

    // This methods returns the factor to put in front of the linear system unknown accumulating it to the position.
    // In the case of acceleration-based integration scheme, we can see in (2.3) that this should return $DG_x$
    virtual SReal getPositionIntegrationFactor() const = 0;

    // This method returns the order of the integration scheme in term of number of past timestep needed to compute the next timestep. For instance, if $p_{t+dt} = f(v_{t+dt}, ... , v_{t-k*dt}$, then the order is k+1
    virtual sofa::Size getIntegrationSchemeTimeOrder() const = 0;

    // Rayleigh damping coefficient related to stiffness > 0
    Data<SReal> d_rayleighStiffness; /
    // Rayleigh damping coefficient related to mass > 0
    Data<SReal> d_rayleighMass; 
```


For the two famillies a lot of this API can be implemented agnostically from the integration s cheme expression. Knowing the integration scheme expression is finally only required to compute the residual vector, and some factors of the LHS or RHS computation. Knowing this, we have proposed two specialization of this class, proposing new simplier API entries for both acceleration and velocity based integration scheme.



> **Note on Rayleigh damping :**\
> Most of the integration scheme propose to add _Rayleigh damping_ which is a numerical damping. This damping has therefore no physical meaning and must not be mixed up with physical damping (like _DiagonalVelocityDampingForceField_ in SOFA). The Rayleigh damping corresponds to a damping matrix that is proportional to the mass or/and stiffness matrices using coefficients, respectively Rayleigh stiffness factor $r_K$ or Rayleigh mass factor $r_M$. This numerical damping is usually used to stabilize or ease convergence of the simulation. However, it has to be used carefully.
> 
> When Rayleigh damping is used, the damping matrix becomes the sum of the physical and the numerical (Rayleigh) damping: $\mathbf{B} = \mathbf{B}_{\text{phys}} - \mathbf{M} \cdot r_M+ \mathbf{K} \cdot r_K$ where $\mathbf{B}_{\text{phys}}$ is the physical damping matrix, $\mathbf{M}$ is the mass matrix and $\mathbf{K}$ is the stiffness matrix.
> The negative sign in front of $\mathbf{M}$, a positive matrix, represents the fact that viscosity opposes motion. Elasticity also opposes it, however $\mathbf{K}$ is a negative matrix. This formula therefore provides two positive coefficients $r_K$ and $r_M$.
> 
> You can see the use of Rayleigh mass and stiffness dampings in the `integrate()` function of the _EulerImplicit_ class (see EulerImplicitSolver.cpp).


#### AccelerationBasedIntegrationScheme

For acceleration-based integration scheme, the only parts that are integration dependent are : 

- $\text{DG}^{(i)}_{\boldsymbol{x}} = \left.\frac{\mathrm{d} g_{\boldsymbol{v}}^{(t,h)}}{\mathrm{d} \boldsymbol{a}}\right|_{\boldsymbol{X}^{(i)}} $
- $\text{DG}^{(i)}_{\boldsymbol{v}} = \left(\left.\frac{\mathrm{d} g_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{v}}\right|_{\boldsymbol{X}^{(i)}} \left.\frac{\mathrm{d} g_{\boldsymbol{v}}^{(t,h)}}{\mathrm{d} \boldsymbol{a}}\right|_{\boldsymbol{X}^{(i)}} + \left.\frac{\mathrm{d} g_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{a}}\right|_{\boldsymbol{X}^{(i)}}\right)$
- $\mathcal{G}_{t}(\boldsymbol{X}^{(i)})_1$
- $\mathcal{G}_{t}(\boldsymbol{X}^{(i)})_2$

This enable to completely fulfill the `ImplicitIntegrationScheme` API in this new class by adding new light methods that will need to be specialized for every integration scheme : 
```cpp
// This method returns a scalar which is the value of the derivative of the position integration scheme with respect to the acceleration.
// To build the $DG_x$ and $DG_v$ factor (see equation above)
virtual SReal getPositionUpdateDerivedFromAcceleration() const = 0;

// This method returns a scalar which is the value of the derivative of the position integration scheme with respect to the velocity.
// To build the $DG_x$ and $DG_v$ factor (see equation above)
virtual SReal getPositionUpdateDerivedFromVelocity() const = 0;

// This method returns a scalar which is the value of the derivative of the velocity integration scheme with respect to the acceleration.
// To build the $DG_x$ and $DG_v$ factor (see equation above)
virtual SReal getVelocityUpdateDerivedFromAcceleration() const = 0;

// This method compute the error in term of position update given the current state, or $G_t(X)_1$
virtual void computeCurrentPositionIntegrationError(...) = 0;

// This method compute the error in term of velocity update given the current state, or $G_t(X)_2$
virtual void computeCurrentVelocityIntegrationError(...) = 0;
```

The tree first method returning only scalar values, they are the most traightforward method to implement. The two last have to deal with advanced concept of SOFA such as mechanical operation on `VecId`. For an example on how to implement this, see the Newmak implementation [here](//TODO, link to cpp file in the master branch once the PR is merged).


#### VelocityBasedIntegrationScheme


For velocity-based integration scheme, the only parts that are integration dependent are : 

- $g_{\boldsymbol{v}}^{(t,h)-1}$
- $\left.\frac{\mathrm{d} \tilde{g}_{\boldsymbol{x}}^{(t,h)}}{\mathrm{d} \boldsymbol{v}}\right|_{\tilde{\boldsymbol{X}}^{(i)}}$
- $\left.\frac{\mathrm{d} g_{\boldsymbol{v}}^{(t,h)-1}}{\mathrm{d} \boldsymbol{v}}\right|_{\tilde{\boldsymbol{X}}^{(i)}}$
- $\mathcal{G}_{t}(\boldsymbol{X}^{(i)})_1$

This enable to completely fulfill the `ImplicitIntegrationScheme` API in this new class by adding new light methods that will need to be specialized for every integration scheme :

```cpp
// This method returns a scalar which is the value of the derivative of the position integration scheme with respect to the velocity.
// To update the state
virtual SReal getPositionUpdateDerivedFromVelocity() const = 0;

// This method returns a scalar which is the value of the derivative of the position integration scheme with respect to the velocity.
// To build the RHS
virtual SReal getInverseVelocityUpdateDerivedFromVelocity() const = 0;

//This method compute the error in term of position update, or $G_t(X)_1$
virtual void computeCurrentPositionIntegrationError(...) = 0;

//This method compute the acceleration given the current velocity, or $g_v^{(t,h)-1}$
virtual void computeAccelerationFromVelocity(...) = 0;
```
Again, the two first method returning only scalar values, they are the most traightforward method to implement. The two last have to deal with advanced concept of SOFA such as mechanical operation on `VecId`. For an example on how to implement this, see the Euler implicit implementation [here](//TODO, link to cpp file in the master branch once the PR is merged).

> **Note :**\
> The velocity-base integration schemes offer a possibility to reduce the integration to a _first order_ integration, meaning the velocity is considered as null at the begining of each time step. This feature can help for quasi-static simulation or simulations where the objects dynamic is by nature subject to numerical noise such as very lightwheight objects. \
> This feature can be activated using the data `firstOrder=True`

#### Special case : StaticEquilibriumIntegrationScheme

The Static equilibrium integration scheme is a special case as it is not a real integration scheme becaus eit does not advance time linearly. 

For more details see its dedicated [documentation page](../../../components/integrationscheme/backward/staticequilibriumintegrationscheme/)

#### Some API details

For all integration scheme, as we have seen in the dynamic equations, the right-hand-side and the left-hand-side are composed of contirbutions coming from the mass and external and internal forces. This means that for building those terms, the intergation schemes will need to access the ForceFields and the Mass objects to either accumulate their _explicit_ part in the right-hand-side or their _implicit_ part in the left-hand-side.

This is performed using a mechanism of visitors that will iterate through the scene graph and call API method of those component so that they can add their contributions. For instance : 
- `addForce` method of forcefield will contribute to the right-hand-side
- `buildStiffnessMatrix` method of forcefield will build its implicit part, contributing to the left-hand-side
- `addMDx` in mass object will be used to add the gravity term in the right-hand-side

This list is not exhausitve, please refer to the [Forcefield](../../multi-model-representation/forcefield/) and [Mass](../../multi-model-representation/mass/) documentation pages.



