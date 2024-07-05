# PlaneProjectiveConstraint

Attach given particles to their initial positions


__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.Component.Constraint.Projective`

__namespace__: `#!c++ sofa::component::constraint::projective`

__parents__: 

- `#!c++ ProjectiveConstraintSet`

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
		<td>indices</td>
		<td>
Indices of the fixed points
</td>
		<td></td>
	</tr>
	<tr>
		<td>origin</td>
		<td>
A point in the plane
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>normal</td>
		<td>
Normal vector to the plane
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawSize</td>
		<td>
Size of the rendered particles (0 -&gt; point based rendering, &gt;0 -&gt; radius of spheres)
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
|mechanicalStates|List of mechanical states to which this component is associated|
|mstate|MechanicalState used by this component|
|topology|link to the topology container|



__Templates__:

- `#!c++ Vec2d`

__Target__: `Sofa.Component.Constraint.Projective`

__namespace__: `#!c++ sofa::component::constraint::projective`

__parents__: 

- `#!c++ ProjectiveConstraintSet`

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
		<td>indices</td>
		<td>
Indices of the fixed points
</td>
		<td></td>
	</tr>
	<tr>
		<td>origin</td>
		<td>
A point in the plane
</td>
		<td>0 0</td>
	</tr>
	<tr>
		<td>normal</td>
		<td>
Normal vector to the plane
</td>
		<td>0 0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawSize</td>
		<td>
Size of the rendered particles (0 -&gt; point based rendering, &gt;0 -&gt; radius of spheres)
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
|mechanicalStates|List of mechanical states to which this component is associated|
|mstate|MechanicalState used by this component|
|topology|link to the topology container|



## Examples

Component/Constraint/Projective/PlaneProjectiveConstraint.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node 	name="root" gravity="0 0 0" dt="0.05"  >
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint PlaneProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [TrianglePressureForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping Tetra2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <VisualStyle displayFlags="hideVisualModels showBehavior" />
        
        <DefaultAnimationLoop />
        
        <RegularGridTopology name="grid" nx="3" ny="3" nz="3" xmin="0" xmax="1" ymin="0" ymax="1" zmin="0" zmax="1" />
        
        <Node 	name="Square"  >
            <EulerImplicitSolver name="Euler Implicit" rayleighStiffness="0.5"  rayleighMass="0.5"  />
            <CGLinearSolver template="GraphScattered" name="CG Solver" iterations="40" tolerance="1e-06" threshold="1e-10" />
            
            <MechanicalObject template="Vec3" name="mObject1"  position="@../grid.position" />
            
            <TetrahedronSetTopologyContainer name="Container" />
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            
            <Hexa2TetraTopologicalMapping name="Mapping"  input="@../grid"  output="@Container" />
            
            <TetrahedronFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.3" youngModulus="500" />
            <UniformMass totalMass="1" />
            <BoxConstraint box="-0.05 -0.05 -0.05    0.05 0.05 0.05" drawBoxes="0"  />
            <BoxROI box="-0.05 -0.05 -0.05    0.05 1.05 1.05" drawBoxes="1" name="ProjectToPlane"/>
            <PlaneProjectiveConstraint normal="1 0 0" indices="@[-1].indices" drawSize="0.03" />
            <Node 	name="Boundary Edges"  >
                <TriangleSetTopologyContainer name="Container" />
                <TriangleSetTopologyModifier name="Modifier" />
                <TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo"  drawTriangles="1" />
                <Tetra2TriangleTopologicalMapping name="Mapping"  input="@../Container"  output="@Container" />
                <BoxROI box="0.95 -0.05 -0.05    1.05 1.05 1.05" drawBoxes="1" position="@../mObject1.rest_position" drawTriangles="0" triangles="@Container.triangles" name="pressureBox" />
                <TrianglePressureForceField template="Vec3" showForces="1" pressure="10 10 0" triangleList="@pressureBox.triangleIndices"/>
            </Node>
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
        root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="hideVisualModels showBehavior")
        root.addObject('DefaultAnimationLoop')
        root.addObject('RegularGridTopology', name="grid", nx="3", ny="3", nz="3", xmin="0", xmax="1", ymin="0", ymax="1", zmin="0", zmax="1")

        Square = root.addChild('Square')
        Square.addObject('EulerImplicitSolver', name="Euler Implicit", rayleighStiffness="0.5", rayleighMass="0.5")
        Square.addObject('CGLinearSolver', template="GraphScattered", name="CG Solver", iterations="40", tolerance="1e-06", threshold="1e-10")
        Square.addObject('MechanicalObject', template="Vec3", name="mObject1", position="@../grid.position")
        Square.addObject('TetrahedronSetTopologyContainer', name="Container")
        Square.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        Square.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        Square.addObject('Hexa2TetraTopologicalMapping', name="Mapping", input="@../grid", output="@Container")
        Square.addObject('TetrahedronFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.3", youngModulus="500")
        Square.addObject('UniformMass', totalMass="1")
        Square.addObject('BoxConstraint', box="-0.05 -0.05 -0.05    0.05 0.05 0.05", drawBoxes="0")
        Square.addObject('BoxROI', box="-0.05 -0.05 -0.05    0.05 1.05 1.05", drawBoxes="1", name="ProjectToPlane")
        Square.addObject('PlaneProjectiveConstraint', normal="1 0 0", indices="@[-1].indices", drawSize="0.03")

        Boundary Edges = Square.addChild('Boundary Edges')
        Boundary Edges.addObject('TriangleSetTopologyContainer', name="Container")
        Boundary Edges.addObject('TriangleSetTopologyModifier', name="Modifier")
        Boundary Edges.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo", drawTriangles="1")
        Boundary Edges.addObject('Tetra2TriangleTopologicalMapping', name="Mapping", input="@../Container", output="@Container")
        Boundary Edges.addObject('BoxROI', box="0.95 -0.05 -0.05    1.05 1.05 1.05", drawBoxes="1", position="@../mObject1.rest_position", drawTriangles="0", triangles="@Container.triangles", name="pressureBox")
        Boundary Edges.addObject('TrianglePressureForceField', template="Vec3", showForces="1", pressure="10 10 0", triangleList="@pressureBox.triangleIndices")
    ```

