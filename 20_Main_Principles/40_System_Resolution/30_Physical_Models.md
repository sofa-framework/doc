Physics in SOFA
===============

In the previous doc pages, the integration scheme describes how to compute the configuration at the next time step from the current state. The linear solver explains the step performed to compute the solution of the linear system *Ax=b*. This section explains how the physics contributes to this system.

Mass
----

The Mass of the system will contribute to the left-hand side within the matrix *A*:

* with direct solvers, the mass is included in the matrix using the function:
``` cpp
addMToMatrix()
```
* with iterative solvers, the mass is taken into account through the function:
``` cpp
addMDx()
```

There is different way of integrating the mass in the system, described below.


### UniformMass ###

This mass is independent of your modeling choices. The total mass is divided by the number of nodes, the mass matrix is diagonal and each value on the diagonal has the same value:
``` cpp
for ( unsigned int i=0; i<indices.size(); i++ )
    res[indices[i]] += dx[indices[i]] * m; // m is constant
```


### MeshMatrixMass ###

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

### DiagonalMass ###

The diagonal mass is a simplification of the MeshMatrixMass approach. It integrates the mass density within the topology based on the Finite Element Method (FEM). However, the mass is moved only on integration points (only mass on the nodes, not on edges anymore): this is a numerical lumping. The mass matrix thus becomes diagonal:
``` cpp
for (size_t i=0; i<n; i++)
{
    _res[i] += _dx[i] * masses[i]; // mass different on each node, depending on the topology
}
```



External forces
---------------

Forces can be applied on your physical object. Usually forces are sorted into external and internal forces. Let's consider a simple external force independent from the state *x* of your system. This force will contribute to the right-hand side *b*:
$$Ax=b=F_{ext}$$

In any forcefield, the vector *b* is filled in the function:
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


Physical laws
-------------

Looking at continuum mechanics, the linear system *Ax=b* becomes:
$$M \ddot{x} = K(x)$$
where *K* may depend on the state *x*. *K* can either be linear or non-linear regarding *x*. In case *K* is non-linear, the resulting *K(x)* must be recomputed at each time step. The choice of the space integration used for the physical law will determine how the matrix *K* is filled. SOFA is mainly based on the [Finite Element Method](https://en.wikipedia.org/wiki/Finite_element_method) to integrate in space the physical law, i.e. the contribution of each element of the mesh will be added to the global *K* matrix.

The contribution of the physical law in the linear system will depend on the integration scheme:

* with explicit scheme, we have *K(x) = K(x(t))* where *x(t)* is the known current state. The initial equation becomes:
$$M dv = dt \cdot K(x(t))$$
The physical law therefore only contributes to the right-hand side *b* of the linear system through the function:
``` cpp
addForce() // corresponding to the term : dt K(x(t))
```

* with the implicit scheme, we have $$K(x) = K(x(t+dt)) = K(x(t)) + \frac{dK(x(t+dt))}{dx} dx$$ where *x(t+dt)* is the unknown current state and the initial equation becomes:

$$M dv = dt \cdot (K(x(t)) + \frac{dK(x(t+dt))}{dx})$$
$$\left(M - dt \cdot \frac{dK(x(t+dt))}{dx}\right) dv= dt \cdot K(x(t))$$

Therefore, the implicit scheme implements the same *addForce()* function as presented above:
``` cpp
addForce() // corresponding to the term : dt K(x(t))
```

But an implicit scheme also requires the left-hand side contribution depending on the unknown state *x(t+dt)*:
* for **direct solvers**, this is implemented in the *addKToMatrix()* function:
``` cpp
addKToMatrix() // corresponding to the term : - dt  dK(x(t+dt))/dx dv
```
* for **iterative solvers**, this is implemented in the *addDForce()* function:
``` cpp
addDForce()    // corresponding to the term : - dt  dK(x(t+dt))/dx dv
```