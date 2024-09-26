---
title: EulerExplicitSolver
---

EulerExplicitSolver  
===================

The EulerExplicitSolver component belongs to the category of [integration schemes or ODE Solver](../../../../simulation-principles/system-resolution/integration-scheme/). This scheme allows to solve dynamic systems explicitly: all forces will be computed based on the state information at the current time step $x(t)$.

Looking at continuum mechanics, the linear system $\mathbf{A}x=b$ arises from the dynamic equation. This dynamic is written as follows but other physics (like heat transfer) result in a similar equation:

$$
\mathbf{M}\Delta v=dt\left(f(x,t)\right)
$$

where $x$ is the degrees of freedom, $\mathbf{M}$ the mass matrix and $f(x,t)$ a function of $x$ (and possibly its derivatives) acting on our system. In the case of the EulerExplicitSolver, this equation can be written: 

$$
\mathbf{M}\Delta v=dt\left(f(x(t))\right)
$$

since forces only depend on known state (at our current time step). These forces are computed by the ForceField in the `addForce()` function. The system matrix $\mathbf{A}$ is only equal to the mass matrix $\mathbf{M}$.

Depending on whether the mass matrix is diagonal or not, SOFA supports two cases:

1) The mass matrix is diagonal. It makes the resolution of the linear system trivial (best performances). In this case, the system matrix $\mathbf{A}$ equals a diagonal mass matrix $\mathbf{M}$ which is diagonal, and it can be stored as a vector $|m|$ . Moreover, its inverse can directly be obtained as: $\mathbf{M}^{-1}=|m|^{-1}=\frac{1}{|m|}$.
   The solution $\Delta v_{sol}=dt\cdot \mathbf{M}^{-1}f(x(t))$ finally corresponds to a division operation of $f(x(t))$ by the mass. This computation is actually performed by the Mass component in the `accFromF()` function. Therefore, no LinearSolver is needed to compute directly or iteratively a solution.
2) The mass matrix is not diagonal. Solving the system requires a linear solver. 

Note that the **symplectic** data allows to modify the scheme to make it [symplectic](https://en.wikipedia.org/wiki/Semi-implicit_Euler_method), i.e. velocities are updated before the positions.
It allows to update the positions from the newly computed velocities, instead of velocities from the previous time step.
This option makes the scheme more robust in time.
EulerExplicitSolver is symplectic by default.

Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/EulerExplicitSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/integrationscheme/EulerExplicitSolver.png?raw=true" title="Flow diagram for a EulerExplicitSolver"/></a>



Usage  
-----  

The EulerExplicitSolver **requires** a MechanicalObject to store the state vectors. However, as explained above, no LinearSolver is needed and the EulerExplicitSolver is **only working using a [UniformMass](../../../mass/uniformmass/) or [DiagonalMass](../../../mass/diagonalmass/)**, which ensures to have a diagonal system matrix.
<!-- automatically generated doc START -->
<!-- generate_doc -->

A simple explicit time integrator.


__Target__: Sofa.Component.ODESolver.Forward

__namespace__: sofa::component::odesolver::forward

__parents__:

- OdeSolver

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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|linearSolver|Linear solver used by this component|LinearSolver|

## Examples 

EulerExplicitSolver.scn

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
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9.81 0", dt="0.00001")

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
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")

       deformable_object = root.addChild('DeformableObject')

       deformable_object.addObject('EulerExplicitSolver', name="odeExplicitSolver", symplectic="false")
       deformable_object.addObject('SparseLDLSolver', )
       deformable_object.addObject('MechanicalObject', name="dofs")
       deformable_object.addObject('RegularGridTopology', name="topology", nx="4", ny="4", nz="11", xmin="-1.5", xmax="1.5", ymin="-1.5", ymax="1.5", zmin="0", zmax="10")
       deformable_object.addObject('HexahedronSetGeometryAlgorithms', )
       deformable_object.addObject('MeshMatrixMass', totalMass="15")
       deformable_object.addObject('BoxROI', box="-1.5 -1.5 0 1.5 1.5 0.0001", name="box")
       deformable_object.addObject('FixedProjectiveConstraint', indices="@box.indices")
       deformable_object.addObject('MeshSpringForceField', stiffness="3E2")

       visual = DeformableObject.addChild('visual')

       visual.addObject('QuadSetTopologyContainer', name="Container")
       visual.addObject('QuadSetTopologyModifier', )
       visual.addObject('Hexa2QuadTopologicalMapping', input="@../topology", output="@Container")
       visual.addObject('OglModel', name="Visual", color="yellow", quads="@Container.quads")
       visual.addObject('IdentityMapping', input="@../dofs", output="@Visual")

       floor_visual = root.addChild('floor-visual')

       floor_visual.addObject('MeshOBJLoader', name="meshLoader", filename="mesh/floorFlat.obj", scale3d="0.5 0.5 0.5")
       floor_visual.addObject('OglModel', src="@meshLoader", dy="-8", dz="10")
       floor_visual.addObject('OglModel', src="@meshLoader", rx="90", dy="2")
    ```

EulerExplicitSolver_diagonal.scn

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
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9.81 0", dt="0.00001")

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
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")

       deformable_object = root.addChild('DeformableObject')

       deformable_object.addObject('EulerExplicitSolver', name="odeExplicitSolver", symplectic="false")
       deformable_object.addObject('MechanicalObject', name="dofs")
       deformable_object.addObject('RegularGridTopology', name="topology", nx="4", ny="4", nz="11", xmin="-1.5", xmax="1.5", ymin="-1.5", ymax="1.5", zmin="0", zmax="10")
       deformable_object.addObject('HexahedronSetGeometryAlgorithms', )
       deformable_object.addObject('UniformMass', totalMass="15")
       deformable_object.addObject('BoxROI', box="-1.5 -1.5 0 1.5 1.5 0.0001", name="box")
       deformable_object.addObject('FixedProjectiveConstraint', indices="@box.indices")
       deformable_object.addObject('MeshSpringForceField', stiffness="3E2")

       visual = DeformableObject.addChild('visual')

       visual.addObject('QuadSetTopologyContainer', name="Container")
       visual.addObject('QuadSetTopologyModifier', )
       visual.addObject('Hexa2QuadTopologicalMapping', input="@../topology", output="@Container")
       visual.addObject('OglModel', name="Visual", color="yellow", quads="@Container.quads")
       visual.addObject('IdentityMapping', input="@../dofs", output="@Visual")

       floor_visual = root.addChild('floor-visual')

       floor_visual.addObject('MeshOBJLoader', name="meshLoader", filename="mesh/floorFlat.obj", scale3d="0.5 0.5 0.5")
       floor_visual.addObject('OglModel', src="@meshLoader", dy="-8", dz="10")
       floor_visual.addObject('OglModel', src="@meshLoader", rx="90", dy="2")
    ```


<!-- automatically generated doc END -->
