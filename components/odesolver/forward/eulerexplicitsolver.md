---
title: EulerExplicitSolver
---

EulerExplicitSolver  
===================

The EulerExplicitSolver component belongs to the category of [integration schemes or ODE Solver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/integration-schemes/). This scheme allows to solve dynamic systems explicitly: all forces will be computed based on the state information at the current time step <img class="latex" src="https://latex.codecogs.com/png.latex?x(t)" title="Current position"/>.

Looking at continuum mechanics, the linear system <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="Linear system" /> arises from the dynamic equation. This dynamic is written as follows but other physics (like heat transfer) result in a similar equation:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}\Delta%20v=dt\left(f(x,t)\right)" title="Dynamic system" />

where <img class="latex" src="https://latex.codecogs.com/png.latex?x" title="DOF at next time step system" /> is the degrees of freedom, <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}" title="Mass matrix" /> the mass matrix and <img class="latex" src="https://latex.codecogs.com/png.latex?f(x,t)" title="Forces" /> a function of <img class="latex" src="https://latex.codecogs.com/png.latex?x" title="DOF" /> (and possibly its derivatives) acting on our system. In the case of the EulerExplicitSolver, this equation can be written: 

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}\Delta%20v=dt\left(f(x(t))\right)" title="Explicit dynamic system" />

since forces only depend on known state (at our current time step). These forces are computed by the ForceField in the `addForce()` function. The system matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> is only equal to the mass matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}" title="Mass matrix" />.

Depending on whether the mass matrix is diagonal or not, SOFA supports two cases:

1) The mass matrix is diagonal. It makes the resolution of the linear system trivial (best performances). In this case, the system matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> equals a diagonal mass matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}" title="Mass matrix" /> which is diagonal, and it can be stored as a vector <img class="latex" src="https://latex.codecogs.com/png.latex?|m|" title="Mass vector" /> . Moreover, its inverse can directly be obtained as: <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}^{-1}=|m|^{-1}=\frac{1}{|m|}" title="Inverse mass matrix" />.
   The solution <img class="latex" src="https://latex.codecogs.com/png.latex?\Delta%20v_{sol}=dt\cdot%20\mathbf{M}^{-1}f(x(t))" title="Explicit resolution" /> finally corresponds to a division operation of <img class="latex" src="https://latex.codecogs.com/png.latex?f(x(t))" title="Explicit forces" /> by the mass. This computation is actually performed by the Mass component in the `accFromF()` function. Therefore, no LinearSolver is needed to compute directly or iteratively a solution.
2) The mass matrix is not diagonal. Solving the system requires a linear solver. 

Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/EulerExplicitSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/EulerExplicitSolver.png?raw=true" title="Flow diagram for a EulerExplicitSolver"/></a>


Data
----

The data **symplectic** allows to modify the scheme to make it [symplectic](https://en.wikipedia.org/wiki/Semi-implicit_Euler_method), i.e. velocities are updated before the positions.
It allows to update the positions from the newly computed velocities, instead of velocities from the previous time step.
This option makes the scheme more robust in time.
EulerExplicitSolver is symplectic by default.

Usage  
-----  

The EulerExplicitSolver **requires** a MechanicalObject to store the state vectors. However, as explained above, no LinearSolver is needed and the EulerExplicitSolver is **only working using a [UniformMass](https://www.sofa-framework.org/community/doc/using-sofa/components/mass/uniformmass/) or [DiagonalMass](https://www.sofa-framework.org/community/doc/using-sofa/components/mass/diagonalmass/)**, which ensures to have a diagonal system matrix.



Example  
-------  

This component is used as follows in XML format:  
 
``` xml  
<EulerExplicitSolver name="odeExplicitSolver" />
```  
 
or using SofaPython3:  
 
``` python  
node.addObject('EulerExplicitSolver', name='odeExplicitSolver')
```  

Examples of scenes involving a EulerExplicitSolver are available in [*examples/Component/ODESolver/Forward/EulerExplicitSolver*](https://github.com/sofa-framework/sofa/tree/master/examples/Component/ODESolver/Forward/EulerExplicitSolver):

- [EulerExplicitSolver.scn](https://github.com/sofa-framework/sofa/blob/master/examples/Component/ODESolver/Forward/EulerExplicitSolver.scn): non-symplectic and non-diagonal mass matrix
- [EulerExplicitSolver_diagonal.scn](https://github.com/sofa-framework/sofa/blob/master/examples/Component/ODESolver/Forward/EulerExplicitSolver_diagonal.scn): non-symplectic and diagonal mass matrix
- [EulerSymplecticSolver.scn](https://github.com/sofa-framework/sofa/blob/master/examples/Component/ODESolver/Forward/EulerSymplecticSolver.scn): symplectic and non-diagonal mass matrix
- [EulerSymplecticSolver_diagonal.scn](https://github.com/sofa-framework/sofa/blob/master/examples/Component/ODESolver/Forward/EulerSymplecticSolver_diagonal.scn): symplectic and diagonal mass matrix
<!-- automatically generated doc START -->
__Target__: `Sofa.Component.ODESolver.Forward`

__namespace__: `#!c++ sofa::component::odesolver::forward`

__parents__: 

- `#!c++ OdeSolver`

__categories__: 

- OdeSolver

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
		<td>symplectic</td>
		<td>
If true (default), the velocities are updated before the positions and the method is symplectic, more robust. If false, the positions are updated before the velocities (standard Euler, less robust).
</td>
		<td>1</td>
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

Component/ODESolver/Forward/EulerExplicitSolver.scn

=== "XML"

    ```xml
    <!--
    This scene shows an example of a forward Euler integration scheme.
    This is the variant of the component EulerExplicitSolver where the Data
    'symplectic' is set to false (true by default).
    In this example, the mass is not diagonal. Since it cannot be inverted
    trivially, it requires a linear solver, here SparseLDLSolver.
    -->
    
    <Node name="root" gravity="0 -9.81 0" dt="0.00001">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [SparseLDLSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [MeshMatrixMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Forward"/> <!-- Needed to use components [EulerExplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [MeshSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [HexahedronSetGeometryAlgorithms QuadSetTopologyContainer QuadSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2QuadTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <DefaultAnimationLoop/>
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
    
        <Node name="DeformableObject">
    
            <EulerExplicitSolver name="odeExplicitSolver" symplectic="false"/>
            <SparseLDLSolver />
    
            <MechanicalObject name="dofs"/>
    
            <RegularGridTopology name="topology" nx="4" ny="4" nz="11" xmin="-1.5" xmax="1.5" ymin="-1.5" ymax="1.5" zmin="0" zmax="10" />
            <HexahedronSetGeometryAlgorithms/>
            <MeshMatrixMass totalMass="15"/>
    
            <BoxROI box="-1.5 -1.5 0 1.5 1.5 0.0001" name="box"/>
            <FixedProjectiveConstraint indices="@box.indices" />
            <MeshSpringForceField stiffness="3E2"/>
    
            <Node name="visual">
                <QuadSetTopologyContainer  name="Container" />
                <QuadSetTopologyModifier/>
                <Hexa2QuadTopologicalMapping input="@../topology" output="@Container" />
                <OglModel name="Visual" color="yellow" quads="@Container.quads" />
                <IdentityMapping input="@../dofs" output="@Visual" />
            </Node>
    
        </Node>
    
        <Node name="floor-visual">
            <MeshOBJLoader name="meshLoader" filename="mesh/floorFlat.obj" scale3d="0.5 0.5 0.5"/>
            <OglModel src="@meshLoader" dy="-8" dz="10"/>
            <OglModel src="@meshLoader" rx="90" dy="2"/>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -9.81 0", dt="0.00001")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Forward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")

        DeformableObject = root.addChild('DeformableObject')
        DeformableObject.addObject('EulerExplicitSolver', name="odeExplicitSolver", symplectic="false")
        DeformableObject.addObject('SparseLDLSolver')
        DeformableObject.addObject('MechanicalObject', name="dofs")
        DeformableObject.addObject('RegularGridTopology', name="topology", nx="4", ny="4", nz="11", xmin="-1.5", xmax="1.5", ymin="-1.5", ymax="1.5", zmin="0", zmax="10")
        DeformableObject.addObject('HexahedronSetGeometryAlgorithms')
        DeformableObject.addObject('MeshMatrixMass', totalMass="15")
        DeformableObject.addObject('BoxROI', box="-1.5 -1.5 0 1.5 1.5 0.0001", name="box")
        DeformableObject.addObject('FixedProjectiveConstraint', indices="@box.indices")
        DeformableObject.addObject('MeshSpringForceField', stiffness="3E2")

        visual = DeformableObject.addChild('visual')
        visual.addObject('QuadSetTopologyContainer', name="Container")
        visual.addObject('QuadSetTopologyModifier')
        visual.addObject('Hexa2QuadTopologicalMapping', input="@../topology", output="@Container")
        visual.addObject('OglModel', name="Visual", color="yellow", quads="@Container.quads")
        visual.addObject('IdentityMapping', input="@../dofs", output="@Visual")

        floor-visual = root.addChild('floor-visual')
        floor-visual.addObject('MeshOBJLoader', name="meshLoader", filename="mesh/floorFlat.obj", scale3d="0.5 0.5 0.5")
        floor-visual.addObject('OglModel', src="@meshLoader", dy="-8", dz="10")
        floor-visual.addObject('OglModel', src="@meshLoader", rx="90", dy="2")
    ```

Component/ODESolver/Forward/EulerExplicitSolver_diagonal.scn

=== "XML"

    ```xml
    <!--
    This scene shows an example of a forward Euler integration scheme.
    This is the variant of the component EulerExplicitSolver where the Data
    'symplectic' is set to false (true by default).
    In this example, the mass is diagonal. Since it can be inverted
    trivially, it does not require a linear solver.
    -->
    
    <Node name="root" gravity="0 -9.81 0" dt="0.00001">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Forward"/> <!-- Needed to use components [EulerExplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [MeshSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [HexahedronSetGeometryAlgorithms QuadSetTopologyContainer QuadSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2QuadTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
    
        <Node name="DeformableObject">
    
            <!-- Matrix system is diagonal because integration is explicit and Mass is diagonal -->
            <!-- No need for a LinearSolver -->
            <EulerExplicitSolver name="odeExplicitSolver" symplectic="false"/>
    
            <MechanicalObject name="dofs"/>
    
            <RegularGridTopology name="topology" nx="4" ny="4" nz="11" xmin="-1.5" xmax="1.5" ymin="-1.5" ymax="1.5" zmin="0" zmax="10" />
            <HexahedronSetGeometryAlgorithms/>
            <UniformMass totalMass="15"/>
    
            <BoxROI box="-1.5 -1.5 0 1.5 1.5 0.0001" name="box"/>
            <FixedProjectiveConstraint indices="@box.indices" />
            <MeshSpringForceField stiffness="3E2"/>
    
            <Node name="visual">
                <QuadSetTopologyContainer  name="Container" />
                <QuadSetTopologyModifier/>
                <Hexa2QuadTopologicalMapping input="@../topology" output="@Container" />
                <OglModel name="Visual" color="yellow" quads="@Container.quads" />
                <IdentityMapping input="@../dofs" output="@Visual" />
            </Node>
    
        </Node>
    
        <Node name="floor-visual">
            <MeshOBJLoader name="meshLoader" filename="mesh/floorFlat.obj" scale3d="0.5 0.5 0.5"/>
            <OglModel src="@meshLoader" dy="-8" dz="10"/>
            <OglModel src="@meshLoader" rx="90" dy="2"/>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -9.81 0", dt="0.00001")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Forward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")

        DeformableObject = root.addChild('DeformableObject')
        DeformableObject.addObject('EulerExplicitSolver', name="odeExplicitSolver", symplectic="false")
        DeformableObject.addObject('MechanicalObject', name="dofs")
        DeformableObject.addObject('RegularGridTopology', name="topology", nx="4", ny="4", nz="11", xmin="-1.5", xmax="1.5", ymin="-1.5", ymax="1.5", zmin="0", zmax="10")
        DeformableObject.addObject('HexahedronSetGeometryAlgorithms')
        DeformableObject.addObject('UniformMass', totalMass="15")
        DeformableObject.addObject('BoxROI', box="-1.5 -1.5 0 1.5 1.5 0.0001", name="box")
        DeformableObject.addObject('FixedProjectiveConstraint', indices="@box.indices")
        DeformableObject.addObject('MeshSpringForceField', stiffness="3E2")

        visual = DeformableObject.addChild('visual')
        visual.addObject('QuadSetTopologyContainer', name="Container")
        visual.addObject('QuadSetTopologyModifier')
        visual.addObject('Hexa2QuadTopologicalMapping', input="@../topology", output="@Container")
        visual.addObject('OglModel', name="Visual", color="yellow", quads="@Container.quads")
        visual.addObject('IdentityMapping', input="@../dofs", output="@Visual")

        floor-visual = root.addChild('floor-visual')
        floor-visual.addObject('MeshOBJLoader', name="meshLoader", filename="mesh/floorFlat.obj", scale3d="0.5 0.5 0.5")
        floor-visual.addObject('OglModel', src="@meshLoader", dy="-8", dz="10")
        floor-visual.addObject('OglModel', src="@meshLoader", rx="90", dy="2")
    ```


<!-- automatically generated doc END -->
