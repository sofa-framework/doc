# FastTriangularBendingSprings

Springs added to a triangular mesh to prevent bending


__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.Component.SolidMechanics.Spring`

__namespace__: `#!c++ sofa::component::solidmechanics::spring`

__parents__: 

- `#!c++ ForceField`

__categories__: 

- ForceField

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
Rayleigh damping - stiffness matrix coefficient
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>bendingStiffness</td>
		<td>
Bending stiffness of the material
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>minDistValidity</td>
		<td>
Distance under which a spring is not valid
</td>
		<td>1e-06</td>
	</tr>
	<tr>
		<td>edgeInfo</td>
		<td>
Internal edge data
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

Component/SolidMechanics/Spring/FastTriangularBendingSprings.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.01" gravity="0 0 -1">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangularFEMForceFieldOptim] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [FastTriangularBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [EdgeSetGeometryAlgorithms] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehavior hideCollision hideVisual " />
        <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
        <CGLinearSolver iterations="25" tolerance="1e-5" threshold="1e-5"/>
        <Node name="Thin shell">
            <MeshOBJLoader name="loader" filename="mesh/triangleGrid_10_10.obj" />
            <MeshTopology src="@loader" />
            <EdgeSetGeometryAlgorithms />
            <MechanicalObject name="defoDOF" template="Vec3"  src="@loader" showObject="1"/>
            <BoxROI name="box1" box="-0.5 -0.5 -0.5  100.5 0.005 0.005  " />
            <FixedProjectiveConstraint indices="@box1.indices"/>
            <TriangularFEMForceFieldOptim name="FEM1" youngModulus="20000" poissonRatio="0.3" method="large" />
            <FastTriangularBendingSprings bendingStiffness="10000" />
            <UniformMass totalMass="2500" printLog="0" />
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01", gravity="0 0 -1")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('DefaultAnimationLoop')
        root.addObject('VisualStyle', displayFlags="showBehavior hideCollision hideVisual ")
        root.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
        root.addObject('CGLinearSolver', iterations="25", tolerance="1e-5", threshold="1e-5")

        Thin shell = root.addChild('Thin shell')
        Thin shell.addObject('MeshOBJLoader', name="loader", filename="mesh/triangleGrid_10_10.obj")
        Thin shell.addObject('MeshTopology', src="@loader")
        Thin shell.addObject('EdgeSetGeometryAlgorithms')
        Thin shell.addObject('MechanicalObject', name="defoDOF", template="Vec3", src="@loader", showObject="1")
        Thin shell.addObject('BoxROI', name="box1", box="-0.5 -0.5 -0.5  100.5 0.005 0.005  ")
        Thin shell.addObject('FixedProjectiveConstraint', indices="@box1.indices")
        Thin shell.addObject('TriangularFEMForceFieldOptim', name="FEM1", youngModulus="20000", poissonRatio="0.3", method="large")
        Thin shell.addObject('FastTriangularBendingSprings', bendingStiffness="10000")
        Thin shell.addObject('UniformMass', totalMass="2500", printLog="0")
    ```

