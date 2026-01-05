---
title: EulerImplicitSolver
---

EulerImplicitSolver  
===================

This component belongs to the category of [integration schemes or ODE Solver](../../../../simulation-principles/system-resolution/integration-scheme/). This scheme builds the system following an implicit scheme: forces are considered based on the state information at the next time step $x(t+dt)$, unknown at the current time step.

Looking at continuum mechanics, the linear system $\mathbf{A}x=b$ arises from the dynamic equation. This dynamic is written as follows but other physics (like heat transfer) result in a similar equation:

$$
\mathbf{M}\Delta v=dt\left(f(x,t)\right)
$$

where $x$ is the degrees of freedom, $\mathbf{M}$ the mass matrix and $f(x,t)$ a function of $x$ (and possibly its derivatives) acting on our system. In the case of the EulerImplicitSolver, this equation can be written: 

$$
\mathbf{M} \Delta v=dt \cdot f(x(t+dt))
$$

by using a Taylor expansion, we get:

$$
\mathbf{M} \Delta v=dt \cdot \left( f(x(t))+\cdot \frac{\partial f}{\partial x} \Delta x \right)
$$

since we have: $\Delta x=dt(v(t)+\Delta v)$, then:

$$
\mathbf{M}\Delta v=dt\cdot \left( f(x(t))+dt\cdot \frac{\partial f}{\partial x}v(t)+dt\cdot \frac{\partial f}{\partial x} \Delta v \right)
$$

Finally, gathering the unknown (depending on $\Delta v$) in the left-hand side, we have:

$$
\left( \mathbf{M}-dt^2 \cdot \frac{\partial f}{\partial x} \right) \Delta v=dt\cdot f(x(t))+dt^2\cdot \frac{\partial f}{\partial x}v(t)
$$

We can notice the appearance of the stiffness matrix : $\mathbf{K}_{ij}=\textstyle\frac{\partial f_i}{\partial x_j}$. The stiffness matrix $\mathbf{K}$ is a symmetric matrix, can either be linear or non-linear regarding $x$.

$$
\left( \mathbf{M}-dt^2 \cdot \mathbf{K} \right) \Delta v=dt\cdot f(x(t))+dt^2\cdot \mathbf{K}v(t)
$$

The computation of the **right hand side** is done by the ForceFields. Just like in the explicit case (see [EulerExplicitSolver](../../forward/eulerexplicitsolver/)), the explicit contribution $dt\left(f(x(t))\right)$ is implemented in the same function `addForce()`. The second part $dt^2\cdot \frac{\partial f}{\partial x}v(t)$ is computed by the function `addDForce()`.

It is important to note that, depending on the **choice of LinearSolver** (direct or iterative), the API functions called to build the **left hand side** system matrix $\mathbf{A}=\left( M-dt^2 \cdot \frac{\partial f}{\partial x} \right)$ will not be the same:

  - if a direct solver is used, the mass $\mathbf{M}$ is computed in the `addMToMatrix()` and the stiffness part $-dt^2 \cdot \frac{\partial f}{\partial x}$ is computed in the function `addKToMatrix()` in ForceFields

  - if an iterative solver is used, the mass is iteratively multiplied by the unknown $\mathbf{M} \Delta v$ within the `addMDx()`, as the stiffness part $-dt^2 \cdot \frac{\partial f}{\partial x} \Delta v$ within the function `addDForce()` in ForceFields.


#### Considering viscosity


As you might have noticed, the Taylor expansion detailed above does not take into account a possible dependency of the force  $f(x,t)$ on the velocity. By considering it, the effect of velocity will result in a viscosity effect through the damping matrix $\mathbf{B}$.

Let's apply the Taylor expansion taking into account the velocity and we get:

$$
\mathbf{M} \Delta v=dt \cdot \left( f(x(t), v(t))+\cdot \frac{\partial f}{\partial x} \Delta x+\cdot \frac{\partial f}{\partial v} \Delta v \right)
$$

$$
\left( \mathbf{M}-dt \cdot \frac{\partial f}{\partial v}-dt^2 \cdot \frac{\partial f}{\partial x} \right) \Delta v=dt\cdot f(x(t),v(t))+dt^2\cdot \frac{\partial f}{\partial x}v(t)
$$

$$
\left( \mathbf{M}-dt \cdot \mathbf{B}-dt^2 \cdot \mathbf{K} \right) \Delta v=dt\cdot f(x(t),v(t))+dt^2\cdot \mathbf{K}v(t)
$$

Depending on the choice of LinearSolver (direct or iterative), the API functions called to build the $\mathbf{B}$ damping matrix on the left hand side will not be the same:

  - if a direct solver is used, the damping matrix $\mathbf{B}$ is computed in the `addBToMatrix()` in ForceFields
  - if an iterative solver is used, the damping is iteratively multiplied by the unknown $\mathbf{B} \Delta v$ within the `addDForce()` just as the stiffness part in the function `addDForce()` in ForceFields.



#### Dissipation

SOFA is a framework aiming at interactive simulations. For this purpose, dissipative schemes are very appropriate. The Euler scheme is an order 1 time integration scheme (since only using the current state $x(t)$ and no older one like $x(t-dt)$). It is known to be a dissipative scheme. Moreover, only one Newton step is performed in the EulerImplicit, which might harm the energy conservation.

#### Numerical damping

With Rayleigh damping, the option is given to the user to add numerical damping. The description of the meaning and effect of these Rayleigh damping coefficients is given in [ODESolver](../../../../simulation-principles/system-resolution/integration-scheme/#rayleigh-damping).


#### Trapezoidal rule

Activating the trapezoidalScheme option of the Euler implicit scheme will make the scheme less dissipative. This is due to the fact that the [trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule) increases the order of the time integration. Moreover, higher order schemes are known to be less dissipative.
It is also known to increase robustness and stability to the time integration due to the order 2 in time of this trapezoidal scheme. The modified scheme is the following:

$$
y_{n+1}-y_n=\frac{dt}{2}(f(y_{n+1})+f(y_n))
$$

This results in the following linear system:

$$
\left( \mathbf{M}-\frac{dt^2}{4} \frac{\partial f}{\partial x}\right) \Delta v=dt\cdot f(x(t))+\frac{dt^2}{2}\cdot \frac{\partial f}{\partial x}v(t)
$$


Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/EulerImplicitSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/EulerImplicitSolver.png?raw=true" title="Flow diagram for the EulerImplicitSolver"/></a>




Usage  
-----  

The EulerImplicitSolver **requires**:

- a [LinearSolver](../../../../simulation-principles/system-resolution/linear-solver/) to solve the linear system
- and a MechanicalObject to store the state vectors.

<!-- automatically generated doc START -->
<!-- generate_doc -->

Time integrator using implicit backward Euler scheme.


__Target__: Sofa.Component.ODESolver.Backward

__namespace__: sofa::component::odesolver::backward

__parents__:

- OdeSolver
- LinearSolverAccessor

### Data

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Default value</th>
        </tr>
    </thead>
    <tbody>
	<tr>
		<td>name</td>
		<td>
object name
		</td>
		<td>unnamed</td>
	</tr>
	<tr>
		<td>printLog</td>
		<td>
if true, emits extra messages at runtime.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>tags</td>
		<td>
list of the subsets the object belongs to
		</td>
		<td></td>
	</tr>
	<tr>
		<td>bbox</td>
		<td>
this object bounding box
		</td>
		<td></td>
	</tr>
	<tr>
		<td>componentState</td>
		<td>
The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
		</td>
		<td>Undefined</td>
	</tr>
	<tr>
		<td>listening</td>
		<td>
if true, handle the events, otherwise ignore the events
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping coefficient related to stiffness, > 0
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>rayleighMass</td>
		<td>
Rayleigh damping coefficient related to mass, > 0
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>vdamping</td>
		<td>
Velocity decay coefficient (no decay if null)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>firstOrder</td>
		<td>
Use backward Euler scheme for first order ODE system, which means that only the first derivative of the DOFs (state) appears in the equation. Higher derivatives are absent
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>trapezoidalScheme</td>
		<td>
Boolean to use the trapezoidal scheme instead of the implicit Euler scheme and get second order accuracy in time (false by default)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>solveConstraint</td>
		<td>
Apply ConstraintSolver (requires a ConstraintSolver in the same node as this solver, disabled by by default for now)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>threadSafeVisitor</td>
		<td>
If true, do not use realloc and free visitors in fwdInteractionForceField.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>computeResidual</td>
		<td>
If true, the residual is computed at the end of the solving
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>residual</td>
		<td>
Residual norm at the end of the free-motion solving
		</td>
		<td>1.79769e+308</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|linearSolver|Linear solver used by this component|LinearSolver|

## Examples 

EulerImplicitSolver-comparison.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="-1.8 0 100" dt="0.1">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [MeshSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <DefaultAnimationLoop/>
        
        <Node name="Reference">
            <MeshOBJLoader name="meshLoader_3" filename="mesh/truthcylinder1-bent.obj" scale="0.95" handleSeams="1" />
            <OglModel src="@meshLoader_3" dx="0" dy="-1" dz="0" color="green" />
        </Node>
        <Node name="Springs">
            <EulerImplicitSolver name="cg_odesolver"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="100" tolerance="1e-5" threshold="1e-5"/>
            <MeshGmshLoader name="loader" filename="mesh/truthcylinder1.msh" />
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader" dx="15" />
            <UniformMass totalMass="15" />
            <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345" />
            <MeshSpringForceField name="Spring" tetrasStiffness="1870" tetrasDamping="0" />
            <Node>
                <MeshOBJLoader name="meshLoader_0" filename="mesh/truthcylinder1.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_0" color="yellow" dx="15" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
        </Node>
        <Node name="CoFEM">
            <EulerImplicitSolver name="cg_odesolver" />
            <CGLinearSolver iterations="100" tolerance="1e-5" threshold="1e-5"/>
            <MeshGmshLoader name="loader" filename="mesh/truthcylinder1.msh" />
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader" dx="30" />
            <UniformMass totalMass="15" />
            <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1116" poissonRatio="0.49" method="polar" />
            <Node>
                <MeshOBJLoader name="meshLoader_4" filename="mesh/truthcylinder1.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_4" color="cyan" dx="30" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
        </Node>
        <Node name="CoFEM_firstOrder">
            <EulerImplicitSolver name="cg_odesolver" firstOrder="1" />
            <CGLinearSolver iterations="100" tolerance="1e-5" threshold="1e-5"/>
            <MeshGmshLoader name="loader" filename="mesh/truthcylinder1.msh" />
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader" dx="45" />
            <UniformMass totalMass="15" />
            <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1116" poissonRatio="0.49" method="polar" />
            <Node>
                <MeshOBJLoader name="meshLoader_1" filename="mesh/truthcylinder1.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_1" color="blue" dx="45" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
        </Node>
        <Node name="LinearFEM">
            <EulerImplicitSolver name="cg_odesolver" />
            <CGLinearSolver iterations="100" tolerance="1e-5" threshold="1e-5"/>
            <MeshGmshLoader name="loader" filename="mesh/truthcylinder1.msh" />
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader" dx="60" />
            <UniformMass totalMass="15" />
            <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1116" poissonRatio="0.49" method="small" />
            <Node>
                <MeshOBJLoader name="meshLoader_2" filename="mesh/truthcylinder1.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_2" color="red" dx="60" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="-1.8 0 100", dt="0.1")

       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('DefaultAnimationLoop', )

       reference = root.addChild('Reference')

       reference.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/truthcylinder1-bent.obj", scale="0.95", handleSeams="1")
       reference.addObject('OglModel', src="@meshLoader_3", dx="0", dy="-1", dz="0", color="green")

       springs = root.addChild('Springs')

       springs.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
       springs.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")
       springs.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
       springs.addObject('MeshTopology', src="@loader")
       springs.addObject('MechanicalObject', src="@loader", dx="15")
       springs.addObject('UniformMass', totalMass="15")
       springs.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345")
       springs.addObject('MeshSpringForceField', name="Spring", tetrasStiffness="1870", tetrasDamping="0")

       node = Springs.addChild('node')

       node.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/truthcylinder1.obj", handleSeams="1")
       node.addObject('OglModel', name="Visual", src="@meshLoader_0", color="yellow", dx="15")
       node.addObject('BarycentricMapping', input="@..", output="@Visual")

       co_fem = root.addChild('CoFEM')

       co_fem.addObject('EulerImplicitSolver', name="cg_odesolver")
       co_fem.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")
       co_fem.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
       co_fem.addObject('MeshTopology', src="@loader")
       co_fem.addObject('MechanicalObject', src="@loader", dx="30")
       co_fem.addObject('UniformMass', totalMass="15")
       co_fem.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345")
       co_fem.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1116", poissonRatio="0.49", method="polar")

       node = CoFEM.addChild('node')

       node.addObject('MeshOBJLoader', name="meshLoader_4", filename="mesh/truthcylinder1.obj", handleSeams="1")
       node.addObject('OglModel', name="Visual", src="@meshLoader_4", color="cyan", dx="30")
       node.addObject('BarycentricMapping', input="@..", output="@Visual")

       co_fem_first_order = root.addChild('CoFEM_firstOrder')

       co_fem_first_order.addObject('EulerImplicitSolver', name="cg_odesolver", firstOrder="1")
       co_fem_first_order.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")
       co_fem_first_order.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
       co_fem_first_order.addObject('MeshTopology', src="@loader")
       co_fem_first_order.addObject('MechanicalObject', src="@loader", dx="45")
       co_fem_first_order.addObject('UniformMass', totalMass="15")
       co_fem_first_order.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345")
       co_fem_first_order.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1116", poissonRatio="0.49", method="polar")

       node = CoFEM_firstOrder.addChild('node')

       node.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/truthcylinder1.obj", handleSeams="1")
       node.addObject('OglModel', name="Visual", src="@meshLoader_1", color="blue", dx="45")
       node.addObject('BarycentricMapping', input="@..", output="@Visual")

       linear_fem = root.addChild('LinearFEM')

       linear_fem.addObject('EulerImplicitSolver', name="cg_odesolver")
       linear_fem.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")
       linear_fem.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
       linear_fem.addObject('MeshTopology', src="@loader")
       linear_fem.addObject('MechanicalObject', src="@loader", dx="60")
       linear_fem.addObject('UniformMass', totalMass="15")
       linear_fem.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345")
       linear_fem.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1116", poissonRatio="0.49", method="small")

       node = LinearFEM.addChild('node')

       node.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/truthcylinder1.obj", handleSeams="1")
       node.addObject('OglModel', name="Visual", src="@meshLoader_2", color="red", dx="60")
       node.addObject('BarycentricMapping', input="@..", output="@Visual")
    ```

EulerImplicitSolver.scn

=== "XML"

    ```xml
    <Node name="root" gravity="-1.8 0 100" dt="0.0001">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [MeshMatrixMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <DefaultAnimationLoop/>
    
        <Node name="DeformableObject">
    
            <EulerImplicitSolver name="odeImplicitSolver" computeResidual="true"/>
            <CGLinearSolver iterations="1000" tolerance="1e-9" threshold="1e-9"/>
    
            <MeshGmshLoader name="loader" filename="mesh/truthcylinder1.msh" />
            <TetrahedronSetTopologyContainer src="@loader" name="topologyContainer"/>
            <TetrahedronSetGeometryAlgorithms name="geomAlgo"/>
            <MechanicalObject src="@loader" dx="60" />
            <MeshMatrixMass totalMass="15" topology="@topologyContainer"/>
            <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 &#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;11 12 13 14 15 16 17 18 19 20 &#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 &#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;41 42 43 44 45 46 47 268 269 270 271 343 345" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.49" method="small" />
    
            <Node>
                <MeshOBJLoader name="meshLoader_0" filename="mesh/truthcylinder1.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_0" color="red" dx="60" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="-1.8 0 100", dt="0.0001")

       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('DefaultAnimationLoop', )

       deformable_object = root.addChild('DeformableObject')

       deformable_object.addObject('EulerImplicitSolver', name="odeImplicitSolver", computeResidual="true")
       deformable_object.addObject('CGLinearSolver', iterations="1000", tolerance="1e-9", threshold="1e-9")
       deformable_object.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
       deformable_object.addObject('TetrahedronSetTopologyContainer', src="@loader", name="topologyContainer")
       deformable_object.addObject('TetrahedronSetGeometryAlgorithms', name="geomAlgo")
       deformable_object.addObject('MechanicalObject', src="@loader", dx="60")
       deformable_object.addObject('MeshMatrixMass', totalMass="15", topology="@topologyContainer")
       deformable_object.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 
							11 12 13 14 15 16 17 18 19 20 
							21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 
							41 42 43 44 45 46 47 268 269 270 271 343 345")
       deformable_object.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.49", method="small")

       node = DeformableObject.addChild('node')

       node.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/truthcylinder1.obj", handleSeams="1")
       node.addObject('OglModel', name="Visual", src="@meshLoader_0", color="red", dx="60")
       node.addObject('BarycentricMapping', input="@..", output="@Visual")
    ```


<!-- automatically generated doc END -->
