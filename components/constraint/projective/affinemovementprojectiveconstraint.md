# AffineMovementProjectiveConstraint

Constraint the movement by a rigid transform.


__Templates__:

- `#!c++ Rigid3d`
- `#!c++ Vec3d`

__Target__: `Sofa.Component.Constraint.Projective`

__namespace__: `#!c++ sofa::component::constraint::projective`

__parents__: 

- `#!c++ ProjectiveConstraintSet`

__categories__: 

- ProjectiveConstraintSet

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
		<td>group</td>
		<td>
ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>endTime</td>
		<td>
The constraint stops acting after the given value.
Use a negative value for infinite constraints
</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>meshIndices</td>
		<td>
Indices of the mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
Indices of the constrained points
</td>
		<td></td>
	</tr>
	<tr>
		<td>beginConstraintTime</td>
		<td>
Begin time of the bilinear constraint
</td>
		<td></td>
	</tr>
	<tr>
		<td>endConstraintTime</td>
		<td>
End time of the bilinear constraint
</td>
		<td></td>
	</tr>
	<tr>
		<td>rotation</td>
		<td>
rotation applied to border points
</td>
		<td></td>
	</tr>
	<tr>
		<td>quaternion</td>
		<td>
quaternion applied to border points
</td>
		<td></td>
	</tr>
	<tr>
		<td>translation</td>
		<td>
translation applied to border points
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawConstrainedPoints</td>
		<td>
draw constrained points
</td>
		<td></td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|mechanicalStates|List of mechanical states to which this component is associated|
|mstate|MechanicalState used by this component|
|topology|link to the topology container|



## Examples

Component/Constraint/Projective/AffineMovementProjectiveConstraint.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
        <Node 	name="root" gravity="0 0 0" dt="0.01"  >
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [AffineMovementProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI PairBoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [MeshSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <VisualStyle displayFlags="hideVisualModels showBehavior" />
        <DefaultAnimationLoop/>
        <Node 	name="Square"  >
            <EulerImplicitSolver name="Euler Implicit" rayleighStiffness="0.5"  rayleighMass="0.5"  vdamping="0" />
            <CGLinearSolver template="GraphScattered" name="CG Solver" iterations="40"  tolerance="1e-06"  threshold="1e-10"/>
            <MechanicalObject template="Vec3" name="mObject1" showObject="true" showObjectScale="3"/>
            <RegularGridTopology name ="loader" nx="5" ny="5" nz="1" xmin="0" xmax="1" ymin="0" ymax="1" zmin="0" zmax="1" position="@mObject1.position" drawHexahedra="true"/>
            <UniformMass totalMass="1"/>
            <MeshSpringForceField template="Vec3" name="forcefield" linesStiffness="10" />
            <BoxROI name="Box" box="-0.1 -0.1 0  1.1 1.1 0"/>
            <PairBoxROI name="PairBox" inclusiveBox="-0.1 -0.1 0  1.1 1.1 0" includedBox="0.1 0.1 0 0.9 0.9 0"/>
            <AffineMovementProjectiveConstraint name="bilinearConstraint" template="Vec3" indices="@PairBox.indices" meshIndices = "@Box.indices" translation="0.1 0 0" rotation="[0.7 -0.7 0,0.7 0.7 0,0 0 1]"  drawConstrainedPoints="1"/>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 0 0", dt="0.01")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="hideVisualModels showBehavior")
        root.addObject('DefaultAnimationLoop')

        Square = root.addChild('Square')
        Square.addObject('EulerImplicitSolver', name="Euler Implicit", rayleighStiffness="0.5", rayleighMass="0.5", vdamping="0")
        Square.addObject('CGLinearSolver', template="GraphScattered", name="CG Solver", iterations="40", tolerance="1e-06", threshold="1e-10")
        Square.addObject('MechanicalObject', template="Vec3", name="mObject1", showObject="true", showObjectScale="3")
        Square.addObject('RegularGridTopology', name="loader", nx="5", ny="5", nz="1", xmin="0", xmax="1", ymin="0", ymax="1", zmin="0", zmax="1", position="@mObject1.position", drawHexahedra="true")
        Square.addObject('UniformMass', totalMass="1")
        Square.addObject('MeshSpringForceField', template="Vec3", name="forcefield", linesStiffness="10")
        Square.addObject('BoxROI', name="Box", box="-0.1 -0.1 0  1.1 1.1 0")
        Square.addObject('PairBoxROI', name="PairBox", inclusiveBox="-0.1 -0.1 0  1.1 1.1 0", includedBox="0.1 0.1 0 0.9 0.9 0")
        Square.addObject('AffineMovementProjectiveConstraint', name="bilinearConstraint", template="Vec3", indices="@PairBox.indices", meshIndices="@Box.indices", translation="0.1 0 0", rotation="[0.7 -0.7 0,0.7 0.7 0,0 0 1]", drawConstrainedPoints="1")
    ```

Component/Constraint/Projective/AffineMovementProjectiveConstraint3D.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node 	name="root" gravity="0 0 0" dt="0.05"  >
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [AffineMovementProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI PairBoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <VisualStyle displayFlags="hideVisualModels showBehavior" />
        <DefaultAnimationLoop/>
    
        <Node 	name="Square"  >
            <EulerImplicitSolver name="Euler Implicit"  printLog="0"  rayleighStiffness="0.5"  rayleighMass="0.5"  vdamping="0" />
            <CGLinearSolver template="GraphScattered" name="CG Solver"  printLog="0"  iterations="40"  tolerance="1e-06"  threshold="1e-10" />
            <MechanicalObject template="Vec3" name="mObject1" showObject="true" showObjectScale="3"/>
            <RegularGridTopology name ="loader" nx="4" ny="4" nz="4" xmin="0" xmax="1" ymin="0" ymax="1" zmin="0" zmax="1" position="@mObject1.position" drawHexahedra="true"/>
            <UniformMass totalMass="1"/>
            <TetrahedronFEMForceField template="Vec3" name="forcefield" youngModulus="200" poissonRatio="0.4" method="polar" />
            <BoxROI name="Box" box="-0.1 -0.1 -0.1  1.1 1.1 1.1"/>
            <PairBoxROI name="PairBox" inclusiveBox="-0.1 -0.1 -0.1  1.1 1.1 1.1" includedBox="0.1 0.1 0.1 0.9 0.9 0.9"/>
            <AffineMovementProjectiveConstraint name="bilinearConstraint" template="Vec3" indices="@PairBox.indices" meshIndices = "@Box.indices" translation="0.1 0.1 0.1" rotation="[1 0 0,0 1 0,1 0 1]"/>
    
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 0 0", dt="0.05")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="hideVisualModels showBehavior")
        root.addObject('DefaultAnimationLoop')

        Square = root.addChild('Square')
        Square.addObject('EulerImplicitSolver', name="Euler Implicit", printLog="0", rayleighStiffness="0.5", rayleighMass="0.5", vdamping="0")
        Square.addObject('CGLinearSolver', template="GraphScattered", name="CG Solver", printLog="0", iterations="40", tolerance="1e-06", threshold="1e-10")
        Square.addObject('MechanicalObject', template="Vec3", name="mObject1", showObject="true", showObjectScale="3")
        Square.addObject('RegularGridTopology', name="loader", nx="4", ny="4", nz="4", xmin="0", xmax="1", ymin="0", ymax="1", zmin="0", zmax="1", position="@mObject1.position", drawHexahedra="true")
        Square.addObject('UniformMass', totalMass="1")
        Square.addObject('TetrahedronFEMForceField', template="Vec3", name="forcefield", youngModulus="200", poissonRatio="0.4", method="polar")
        Square.addObject('BoxROI', name="Box", box="-0.1 -0.1 -0.1  1.1 1.1 1.1")
        Square.addObject('PairBoxROI', name="PairBox", inclusiveBox="-0.1 -0.1 -0.1  1.1 1.1 1.1", includedBox="0.1 0.1 0.1 0.9 0.9 0.9")
        Square.addObject('AffineMovementProjectiveConstraint', name="bilinearConstraint", template="Vec3", indices="@PairBox.indices", meshIndices="@Box.indices", translation="0.1 0.1 0.1", rotation="[1 0 0,0 1 0,1 0 1]")
    ```

