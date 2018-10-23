Physics in SOFA
===============

In the previous doc pages, the integration scheme describes how to compute the configuration at the next time step from the current state. The linear solver explains the step performed to compute the solution of the linear system <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}x=b$$" title="Linear system" />. This section explains how the physics contributes to this system.

Mass
----

The Mass of the system will contribute to the left-hand side within the matrix <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}$$" title="System matrix" />:

* with direct solvers, the mass is included in the matrix using the function:
``` cpp
addMToMatrix()
```
* with iterative solvers, the mass is taken into account through the function:
``` cpp
addMDx()
```

There is different way of integrating the mass in the system, described below.


#### UniformMass ####

This mass is independent of your modeling choices. The total mass is divided by the number of nodes, the mass matrix is diagonal and each value on the diagonal has the same value:
``` cpp
for ( unsigned int i=0; i<indices.size(); i++ )
    res[indices[i]] += dx[indices[i]] * m; // m is constant
```


#### MeshMatrixMass ####

This mass integrates the mass density within the topology based on the Finite Element Method (FEM). Thus, the mass is spread on the nodes and edges of the topology. A large element will therefore have a higher associated mass due to its volume:
``` cpp
for (unsigned int i=0; i<dx.size(); i++)
        {
            res[i] += dx[i] * vertexMass[i] * (Real)factor;
            massTotal += vertexMass[i] * (Real)factor;
        }

        for (unsigned int j=0; j<nbEdges; ++j)
        {
            tempMass = edgeMass[j] * (Real)factor;

            v0=_topology->getEdge(j)[0];
            v1=_topology->getEdge(j)[1];

            res[v0] += dx[v1] * tempMass;
            res[v1] += dx[v0] * tempMass;

            massTotal += 2*edgeMass[j] * (Real)factor;
        }
```

#### DiagonalMass ####

The diagonal mass is a simplification of the MeshMatrixMass approach. It integrates the mass density within the topology based on the Finite Element Method (FEM). However, the mass is moved only on integration points (only mass on the nodes, not on edges anymore): this is a numerical lumping. The mass matrix thus becomes diagonal:
``` cpp
for (size_t i=0; i<n; i++)
{
    _res[i] += _dx[i] * masses[i]; // mass different on each node, depending on the topology
}
```



External forces
---------------

Forces can be applied on your physical object. Usually forces are sorted into external and internal forces. Let's consider a simple external force independent from the state <img class="latex" src="https://latex.codecogs.com/png.latex?$$x$$" title="DOF" /> of your system (i.e. purely explicit force). This force will contribute to the right-hand side <img class="latex" src="https://latex.codecogs.com/png.latex?$$b$$" title="Right-hand side vector" />: <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}x=b=f_{ext}$$" title="Right-hand side vector" />

In any forcefield, the vector <img class="latex" src="https://latex.codecogs.com/png.latex?$$b$$" title="RHS vector" /> is filled in the function:
``` cpp
addForce()
```

Taking the example of the *ConstantForceField*:
``` cpp
addForce(const core::MechanicalParams* params, DataVecDeriv& force, const DataVecCoord& position, const DataVecDeriv&)
{
    sofa::helper::WriteAccessor< core::objectmodel::Data< VecDeriv > > _force = force;
    for (unsigned int i=0; i<position.getValue().size(); i++)
        _force[i] += constantForce; // constant value filling the b vector
}
```


Physical laws (internal forces)
-------------------------------

Looking at continuum mechanics, the linear system <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}x=b$$" title="Linear system" /> arises from the dynamic equation whichis a time-varying partial differential equation which, after discretization, can be numerically solved as an ordinary differential equation. The system can then be written:

<img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{M}\ddot{x}=f_{ext}-\textstyle\frac{\partial%20E}{\partial%20x}$$" title="Dynamic mechanical system" />

where <img class="latex" src="https://latex.codecogs.com/png.latex?$$x$$" title="DOF at next time step system" /> is the degrees of freedom, <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{M}$$" title="Mass matrix" /> the mass matrix, <img class="latex" src="https://latex.codecogs.com/png.latex?$$E$$" title="Internal energy" /> a scalar function of x—yields the material internal energy, and <img class="latex" src="https://latex.codecogs.com/png.latex?$$f$$" title="Forces" /> a function of <img class="latex" src="https://latex.codecogs.com/png.latex?$$x$$" title="DOF" /> and <img class="latex" src="https://latex.codecogs.com/png.latex?$$\dot{x}$$" title="DOF derivative" />, describing other forces (constraint forces, internal damping, etc.) acting on our system. The derivative of the internal energy <img class="latex" src="https://latex.codecogs.com/png.latex?$$E$$" title="Internal energy" /> will lead to the computation of internal forces notes <img class="latex" src="https://latex.codecogs.com/png.latex?$$f=-\textstyle\frac{\partial%20E}{\partial%20x}$$" title="Internal forces" />.

The contribution of the physical law in the linear system will depend on the integration scheme. For this explanation, we will rely on the explicit (or forward) Euler and the implicit (or backward) Euler scheme:

#### Explicit case ####

In case of an explicit integration, the above system becomes:

<img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{M}\Delta%20v=dt\left(f(x(t))\right)$$" title="Explicit dynamic system" />

The physical law therefore only contributes to the right-hand side <img class="latex" src="https://latex.codecogs.com/png.latex?$$b$$" title="RHS vector" /> of the linear system through the function:

``` cpp
addForce() // corresponding to the term : dt f(x(t))
```
SOFA is mainly based on the [Finite Element Method](https://en.wikipedia.org/wiki/Finite_element_method) to integrate in space the physical law, i.e. the contribution of each element of the mesh will be added to the numerical system (here the right-hand side vector <img class="latex" src="https://latex.codecogs.com/png.latex?$$b$$" title="RHS vector" />). 


#### Implicit case ####

In case of an implicit integration, the above system becomes:

<img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{M}\Delta%20v=dt\left(f(x(t))+\textstyle\frac{\partial%20f}{\partial%20x}\Delta%20x+\textstyle\frac{\partial%20f}{\partial%20v}\Delta%20v\right)$$" title="Implicit dynamic system" />

In this equation, we can notice the same explicit contribution <img class="latex" src="https://latex.codecogs.com/png.latex?$$dt\left(f(x(t))\right)$$" title="Explicit contribution" />. Just like in the explicit case, this part is implemented in the same function _addForce()_. We can also notice the appearance of the stiffness matrix : <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{K}_{ij}=\textstyle\frac{\partial%20f_i}{\partial%20x_j}$$" title="Implicit contribution" />. The stiffness matrix <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{K}$$" title="Stiffness matrix" /> is a symetric matrix, can either be linear or non-linear regarding <img class="latex" src="https://latex.codecogs.com/png.latex?$$x$$" title="DOF" />.

The term <img class="latex" src="https://latex.codecogs.com/png.latex?$$dt\textstyle\frac{\partial%20f}{\partial%20x}\Delta%20x$$" title="Implicit forces" /> resulting from the Taylor expansion with <img class="latex" src="https://latex.codecogs.com/png.latex?$$\Delta%20x=x(t+dt)-x(t)=dt(v+\Delta%20v)$$" title="Implicit forces" /> can be decomposed into one explicit term <img class="latex" src="https://latex.codecogs.com/png.latex?$$dt^2\textstyle\frac{\partial%20f}{\partial%20x}v$$" title="Explicit stiffness" /> contributing to the right-hand side vector <img class="latex" src="https://latex.codecogs.com/png.latex?$$b$$" title="RHS vector" /> and one implicit term <img class="latex" src="https://latex.codecogs.com/png.latex?$$dt^2\textstyle\frac{\partial%20f}{\partial%20x}\Delta%20v$$" title="Implicit stiffness" /> contributing to the system matrix <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}$$" title="System matrix" /> on the left-hand side.


* for **direct solvers**, the *addKToMatrix()* function computes the implicit part of the stiffness <img class="latex" src="https://latex.codecogs.com/png.latex?$$dt^2\textstyle\frac{\partial%20f}{\partial%20x}\Delta%20v$$" title="Implicit stiffness" /> which will build a matrix <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{K}$$" title="Stiffness matrix" />. The linear system matrix <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{A}$$" title="System matrix" /> must be stored and built, since it will be inversed later on to solve the system.
``` cpp
addKToMatrix() // adding contribution in the A matrix : - dt^2  df(x(t+dt))/dx
```
The *addDForce()* function implements the explicit part of the stiffness <img class="latex" src="https://latex.codecogs.com/png.latex?$$dt^2\textstyle\frac{\partial%20f}{\partial%20x}v$$" title="Explicit stiffness" /> by adding the result of the matrix-vector multiplication directly in the right-hand side vector <img class="latex" src="https://latex.codecogs.com/png.latex?$$b$$" title="RHS vector" />:
``` cpp
addDForce()    // adding contribution in b : - dt^2  df(x(t+dt))/dx
```


* for **iterative solvers**, since the system matrix does not required to be built, both explicit and implicit contributions of the stiffness will be computed by the *addDForce()*: for the explicit part it compultes the matrix-vector multiplication between <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{K}$$" title="Stiffness matrix" /> and <img class="latex" src="https://latex.codecogs.com/png.latex?$$v$$" title="Velocity" /> the known first derivate of the degrees of freedom, while for the implicit part it computes the matrix-vector multiplication between <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{K}$$" title="Stiffness matrix" /> and the unknown <img class="latex" src="https://latex.codecogs.com/png.latex?$$\Delta%20v$$" title="Unknow state at next time step" />:
``` cpp
addDForce()    // multiplying any vector by : - dt^2  df(x(t+dt))/dx
```

#### API summary ####

In the **explicit** case, we solve the equation <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{M}\Delta%20v=dt\left(f(x(t))\right)$$" title="Explicit equation" /> using the following SOFA API:

| Linear solver | <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{M}\Delta%20v$$" title="Mass" /> | <img class="latex" src="https://latex.codecogs.com/png.latex?$$dt\left(f(x(t))\right)$$" title="Explicit forces" /> |
|:----------:|:-------------:|:--------:|
| **Iterative**  | addMDx()      | addForce() |
| **Direct**     | addMToMatrix()  | addForce() |


In the **implicit** case, we solve the equation <img class="latex" src="https://latex.codecogs.com/png.latex?$$\left(%20\mathbf{M}-dt^2%20\cdot%20\textstyle\frac{\partial%20f}{\partial%20x}\right)%20\Delta%20v=dt%20\cdot%20f(x(t))+dt^2%20\cdot%20\textstyle\frac{\partial%20f}{\partial%20x}v(t)$$" title="Implicit equation" /> using the following SOFA API:

| Linear solver | <img class="latex" src="https://latex.codecogs.com/png.latex?$$\mathbf{M}\Delta%20v$$" title="Mass" /> | <img class="latex" src="https://latex.codecogs.com/png.latex?$$-dt^2%20\cdot%20\textstyle\frac{\partial%20f}{\partial%20x}\Delta%20v$$" title="Implicit stiffness" /> | <img class="latex" src="https://latex.codecogs.com/png.latex?$$dt%20\cdot%20f(x(t))$$" title="Explicit forces" /> | <img class="latex" src="https://latex.codecogs.com/png.latex?$$dt^2\textstyle\frac{\partial%20f}{\partial%20x}v(t)$$" title="Explicit stiffness" /> |
|:-------------:|:--------------:|:--------------:|:----------:|:-----------:|
| **Iterative** | addMDx()       | addDForce()    | addForce() | addDForce() |
| **Direct**    | addMToMatrix() | addKToMatrix() | addForce() | addDForce() |