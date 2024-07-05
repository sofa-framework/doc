---
title: EulerImplicitSolver
---

EulerImplicitSolver  
===================

This component belongs to the category of [integration schemes or ODE Solver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/integration-schemes/). This scheme builds the system following an implicit scheme: forces are considered based on the state information at the next time step <img class="latex" src="https://latex.codecogs.com/png.latex?x(t+dt)" title="Unknown state"/>, unknown at the current time step.

Looking at continuum mechanics, the linear system <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="Linear system" /> arises from the dynamic equation. This dynamic is written as follows but other physics (like heat transfer) result in a similar equation:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}\Delta%20v=dt\left(f(x,t)\right)" title="Dynamic system" />

where <img class="latex" src="https://latex.codecogs.com/png.latex?x" title="DOF at next time step system" /> is the degrees of freedom, <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}" title="Mass matrix" /> the mass matrix and <img class="latex" src="https://latex.codecogs.com/png.latex?f(x,t)" title="Forces" /> a function of <img class="latex" src="https://latex.codecogs.com/png.latex?x" title="DOF" /> (and possibly its derivatives) acting on our system. In the case of the EulerImplicitSolver, this equation can be written: 

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}%20\Delta%20v=dt%20\cdot%20f(x(t+dt))" title="Implicit dynamic system" />

by using a Taylor expansion, we get:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}%20\Delta%20v=dt%20\cdot%20\left(%20f(x(t))+\cdot%20\frac{\partial%20f}{\partial%20x}%20\Delta%20x%20\right)" title="Implicit dynamic system" />

since we have: <img class="latex" src="https://latex.codecogs.com/png.latex?\Delta%20x=dt(v(t)+\Delta%20v)" title="Implicit scheme" />, then:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}\Delta%20v=dt\cdot%20\left(%20f(x(t))+dt\cdot%20\frac{\partial%20f}{\partial%20x}v(t)+dt\cdot%20\frac{\partial%20f}{\partial%20x}%20\Delta%20v%20\right)" title="Implicit dynamic system" />

Finally, gathering the unknown (depending on <img class="latex" src="https://latex.codecogs.com/png.latex?\Delta%20v" title="Unknown delta of velocity" />) in the left hand side, we have:

<img class="latex" src="https://latex.codecogs.com/png.latex?\left(%20\mathbf{M}-dt^2%20\cdot%20\frac{\partial%20f}{\partial%20x}%20\right)%20\Delta%20v=dt\cdot%20f(x(t))+dt^2\cdot%20\frac{\partial%20f}{\partial%20x}v(t)" title="Implicit dynamic system" />

We can notice the appearance of the stiffness matrix : <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{K}_{ij}=\textstyle\frac{\partial%20f_i}{\partial%20x_j}" title="Implicit contribution" />. The stiffness matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{K}" title="Stiffness matrix" /> is a symmetric matrix, can either be linear or non-linear regarding <img class="latex" src="https://latex.codecogs.com/png.latex?x" title="DOF" />.

<img class="latex" src="https://latex.codecogs.com/png.latex?\left(%20\mathbf{M}-dt^2%20\cdot%20\mathbf{K}%20\right)%20\Delta%20v=dt\cdot%20f(x(t))+dt^2\cdot%20\mathbf{K}v(t)" title="Implicit dynamic system" />

The computation of the **right hand side** is done by the ForceFields. Just like in the explicit case (see [EulerExplicitSolver](https://www.sofa-framework.org/community/doc/using-sofa/components/odesolver/eulerexplicitsolver/)), the explicit contribution <img class="latex" src="https://latex.codecogs.com/png.latex?dt\left(f(x(t))\right)" title="Explicit contribution" /> is implemented in the same function `addForce()`. The second part <img class="latex" src="https://latex.codecogs.com/png.latex?dt^2\cdot%20\frac{\partial%20f}{\partial%20x}v(t)" title="Known stiffness" /> is computed by the function `addDForce()`.

It is important to note that, depending on the **choice of LinearSolver** (direct or iterative), the API functions called to build the **left hand side** system matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}=\left(%20M-dt^2%20\cdot%20\frac{\partial%20f}{\partial%20x}%20\right)" title="System matrix" /> will not be the same:

  - if a direct solver is used, the mass <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}" title="Mass matrix" /> is computed in the `addMToMatrix()` and the stiffness part <img class="latex" src="https://latex.codecogs.com/png.latex?-dt^2%20\cdot%20\frac{\partial%20f}{\partial%20x}" title="Stiffness matrix" /> is computed in the function `addKToMatrix()` in ForceFields

  - if an iterative solver is used, the mass is iteratively multiplied by the unknown <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}%20\Delta%20v" title="Mass matrix" /> within the `addMDx()`, as the stiffness part <img class="latex" src="https://latex.codecogs.com/png.latex?-dt^2%20\cdot%20\frac{\partial%20f}{\partial%20x}%20\Delta%20v" title="Stiffness matrix" /> within the function `addDForce()` in ForceFields.


#### Considering viscosity


As you might have notice, the Taylor expansion detailed above does not take into account a possible dependency of the force  <img class="latex" src="https://latex.codecogs.com/png.latex?f(x,t)" title="Forces" /> on the velocity. By considering it, the effect of velocity will result in a viscosity effect through the damping matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{B}" title="Damping matrix" />.

Let's apply the Taylor expansion taking into account the velocity and we get:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}%20\Delta%20v=dt%20\cdot%20\left(%20f(x(t), v(t))+\cdot%20\frac{\partial%20f}{\partial%20x}%20\Delta%20x+\cdot%20\frac{\partial%20f}{\partial%20v}%20\Delta%20v%20\right)" title="Implicit dynamic system with damping" />

<img class="latex" src="https://latex.codecogs.com/png.latex?\left(%20\mathbf{M}-dt%20\cdot%20\frac{\partial%20f}{\partial%20v}-dt^2%20\cdot%20\frac{\partial%20f}{\partial%20x}%20\right)%20\Delta%20v=dt\cdot%20f(x(t),v(t))+dt^2\cdot%20\frac{\partial%20f}{\partial%20x}v(t)" title="Implicit dynamic system with damping" />

<img class="latex" src="https://latex.codecogs.com/png.latex?\left(%20\mathbf{M}-dt%20\cdot%20\mathbf{B}-dt^2%20\cdot%20\mathbf{K}%20\right)%20\Delta%20v=dt\cdot%20f(x(t),v(t))+dt^2\cdot%20\mathbf{K}v(t)" title="Implicit dynamic system with damping" />

Depending on the choice of LinearSolver (direct or iterative), the API functions called to build the <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{B}" title="Damping matrix" /> damping matrix on the left hand side will not be the same:

  - if a direct solver is used, the damping matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{B}" title="Damping matrix" /> is computed in the `addBToMatrix()` in ForceFields

  - if an iterative solver is used, the damping is iteratively multiplied by the unknown <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{B}%20\Delta%20v" title="Damping matrix" /> within the `addDForce()` just as the stiffness part in the function `addDForce()` in ForceFields.



#### Dissipation

SOFA is a framework aiming at interactive simulations. For this purpose, dissipative schemes are very appropriate. The Euler scheme is an order 1 integration scheme (in time, since only using the current state <img class="latex" src="https://latex.codecogs.com/png.latex?x(t)" title="Current DOF" /> and no older one like <img class="latex" src="https://latex.codecogs.com/png.latex?x(t-dt)" title="Older DOF" />). It is known to be a dissipative scheme. Moreover, only one Newton step is performed in the EulerImplicit, which might harm the energy conservation.

Activating the trapezoidalScheme option of the Euler implicit scheme will make the scheme less dissipative. This is due to the fact that the trapezoidal rule increases the order of the time integration. Moreover, higher order schemes are known to be less dissipative.



Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/EulerImplicitSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/EulerImplicitSolver.png?raw=true" title="Flow diagram for the EulerImplicitSolver"/></a>


Data  
----

The data **trapezoidalScheme** modifies the EulerImplicitSolver scheme and implements the [trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule):

<img class="latex" src="https://latex.codecogs.com/png.latex?y_{n+1}-y_n=\frac{dt}{2}(f(y_{n+1})+f(y_n))" title="Trapezoidal rule" />

This results in the following linear system:

<img class="latex" src="https://latex.codecogs.com/png.latex?\left(%20\mathbf{M}-\frac{dt^2}{2}%20\frac{\partial%20f}{\partial%20x}\right)%20\Delta%20v=dt\cdot%20f(x(t))+\frac{dt^2}{2}\cdot%20\frac{\partial%20f}{\partial%20x}v(t)" title="Linear trapezoidal system" />

The use of the trapezoidal rule is known to increase robustness and stability to the time integration due to the order 2 in time of this trapezoidal scheme.

The option is given to the user to add numerical Rayleigh damping using the data **rayleighStiffness** and **rayleighMass**. The description of the meaning and effect of these Rayleigh damping coefficients is given in [ODESolver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/integration-schemes/#rayleigh-damping).

The data **firstOrder** enables to use the EulerImplicitSolver at the order 1, which means that only the first derivative of the DOFs (state) x appears in the equation. Higher derivatives are absent. This option is for instance well suited for heat diffusion equation using only the first derivative of the temperature field:

<img class="latex" src="https://latex.codecogs.com/png.latex?M\frac{\partial%20T}{\partial%20t}=\Delta%20T" title="Heat diffusion" />.



Usage  
-----  

The EulerImplicitSolver **requires**:

- a [LinearSolver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/linear-solvers/) to solve the linear system
- and a MechanicalObject to store the state vectors.


 
Example  
-------  
 
This component is used as follows in XML format:  
 
``` xml  
<EulerImplicitSolver name="ODEsolver" rayleighStiffness="0.1" rayleighMass="0.1" />
```  
 
or using SofaPython3:  
 
``` python  
node.addObject('EulerImplicitSolver', name='ODEsolver', rayleighStiffness='0.1' rayleighMass='0.1')  
```  
 
An example scene involving a StaticSolver is available in [*examples/Component/ODESolver/Backward/EulerImplicitSolver.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/ODESolver/Backward/EulerImplicitSolver.scn)
<!-- automatically generated doc START -->
__Target__: `Sofa.Component.ODESolver.Backward`

__namespace__: `#!c++ sofa::component::odesolver::backward`

__parents__: 

- `#!c++ OdeSolver`
- `#!c++ LinearSolverAccessor`

Data: 

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
list of the subsets the objet belongs to
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
Rayleigh damping coefficient related to stiffness, &gt; 0
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>rayleighMass</td>
		<td>
Rayleigh damping coefficient related to mass, &gt; 0
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

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|linearSolver|Linear solver used by this component|



## Examples

Component/ODESolver/Backward/EulerImplicitSolver-comparison.scn

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
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="-1.8 0 100", dt="0.1")
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
        root.addObject('DefaultAnimationLoop')

        Reference = root.addChild('Reference')
        Reference.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/truthcylinder1-bent.obj", scale="0.95", handleSeams="1")
        Reference.addObject('OglModel', src="@meshLoader_3", dx="0", dy="-1", dz="0", color="green")

        Springs = root.addChild('Springs')
        Springs.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        Springs.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")
        Springs.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
        Springs.addObject('MeshTopology', src="@loader")
        Springs.addObject('MechanicalObject', src="@loader", dx="15")
        Springs.addObject('UniformMass', totalMass="15")
        Springs.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345")
        Springs.addObject('MeshSpringForceField', name="Spring", tetrasStiffness="1870", tetrasDamping="0")

        Springs = Springs.addChild('Springs')
        Springs.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/truthcylinder1.obj", handleSeams="1")
        Springs.addObject('OglModel', name="Visual", src="@meshLoader_0", color="yellow", dx="15")
        Springs.addObject('BarycentricMapping', input="@..", output="@Visual")

        CoFEM = root.addChild('CoFEM')
        CoFEM.addObject('EulerImplicitSolver', name="cg_odesolver")
        CoFEM.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")
        CoFEM.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
        CoFEM.addObject('MeshTopology', src="@loader")
        CoFEM.addObject('MechanicalObject', src="@loader", dx="30")
        CoFEM.addObject('UniformMass', totalMass="15")
        CoFEM.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345")
        CoFEM.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1116", poissonRatio="0.49", method="polar")

        CoFEM = CoFEM.addChild('CoFEM')
        CoFEM.addObject('MeshOBJLoader', name="meshLoader_4", filename="mesh/truthcylinder1.obj", handleSeams="1")
        CoFEM.addObject('OglModel', name="Visual", src="@meshLoader_4", color="cyan", dx="30")
        CoFEM.addObject('BarycentricMapping', input="@..", output="@Visual")

        CoFEM_firstOrder = root.addChild('CoFEM_firstOrder')
        CoFEM_firstOrder.addObject('EulerImplicitSolver', name="cg_odesolver", firstOrder="1")
        CoFEM_firstOrder.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")
        CoFEM_firstOrder.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
        CoFEM_firstOrder.addObject('MeshTopology', src="@loader")
        CoFEM_firstOrder.addObject('MechanicalObject', src="@loader", dx="45")
        CoFEM_firstOrder.addObject('UniformMass', totalMass="15")
        CoFEM_firstOrder.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345")
        CoFEM_firstOrder.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1116", poissonRatio="0.49", method="polar")

        CoFEM_firstOrder = CoFEM_firstOrder.addChild('CoFEM_firstOrder')
        CoFEM_firstOrder.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/truthcylinder1.obj", handleSeams="1")
        CoFEM_firstOrder.addObject('OglModel', name="Visual", src="@meshLoader_1", color="blue", dx="45")
        CoFEM_firstOrder.addObject('BarycentricMapping', input="@..", output="@Visual")

        LinearFEM = root.addChild('LinearFEM')
        LinearFEM.addObject('EulerImplicitSolver', name="cg_odesolver")
        LinearFEM.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")
        LinearFEM.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
        LinearFEM.addObject('MeshTopology', src="@loader")
        LinearFEM.addObject('MechanicalObject', src="@loader", dx="60")
        LinearFEM.addObject('UniformMass', totalMass="15")
        LinearFEM.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345")
        LinearFEM.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1116", poissonRatio="0.49", method="small")

        LinearFEM = LinearFEM.addChild('LinearFEM')
        LinearFEM.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/truthcylinder1.obj", handleSeams="1")
        LinearFEM.addObject('OglModel', name="Visual", src="@meshLoader_2", color="red", dx="60")
        LinearFEM.addObject('BarycentricMapping', input="@..", output="@Visual")
    ```

Component/ODESolver/Backward/EulerImplicitSolver.scn

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
    
            <EulerImplicitSolver name="odeImplicitSolver" />
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
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="-1.8 0 100", dt="0.0001")
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
        root.addObject('DefaultAnimationLoop')

        DeformableObject = root.addChild('DeformableObject')
        DeformableObject.addObject('EulerImplicitSolver', name="odeImplicitSolver")
        DeformableObject.addObject('CGLinearSolver', iterations="1000", tolerance="1e-9", threshold="1e-9")
        DeformableObject.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
        DeformableObject.addObject('TetrahedronSetTopologyContainer', src="@loader", name="topologyContainer")
        DeformableObject.addObject('TetrahedronSetGeometryAlgorithms', name="geomAlgo")
        DeformableObject.addObject('MechanicalObject', src="@loader", dx="60")
        DeformableObject.addObject('MeshMatrixMass', totalMass="15", topology="@topologyContainer")
        DeformableObject.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 
							11 12 13 14 15 16 17 18 19 20 
							21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 
							41 42 43 44 45 46 47 268 269 270 271 343 345")
        DeformableObject.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.49", method="small")

        DeformableObject = DeformableObject.addChild('DeformableObject')
        DeformableObject.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/truthcylinder1.obj", handleSeams="1")
        DeformableObject.addObject('OglModel', name="Visual", src="@meshLoader_0", color="red", dx="60")
        DeformableObject.addObject('BarycentricMapping', input="@..", output="@Visual")
    ```


<!-- automatically generated doc END -->
