# LineProjectiveConstraint

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
A point in the line
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>direction</td>
		<td>
Direction of the line
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
A point in the line
</td>
		<td>0 0</td>
	</tr>
	<tr>
		<td>direction</td>
		<td>
Direction of the line
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

Component/Constraint/Projective/LineProjectiveConstraint.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node 	name="root" gravity="0 0 0" dt="0.05"  >
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint LineProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [GridMeshCreator] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [EdgePressureForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangularFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [EdgeSetGeometryAlgorithms EdgeSetTopologyContainer EdgeSetTopologyModifier TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Triangle2EdgeTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <VisualStyle displayFlags="hideVisualModels showBehavior" />
        <DefaultAnimationLoop />
        <DefaultVisualManagerLoop />
    
        <Node 	name="Square"  >
            <EulerImplicitSolver name="Euler Implicit"  printLog="0"  rayleighStiffness="0.5"  rayleighMass="0.5"  vdamping="0"  />
            <CGLinearSolver template="GraphScattered" name="CG Solver"  printLog="0"  iterations="40"  tolerance="1e-06"  threshold="1e-10" />
            <GridMeshCreator name="loader" resolution="5 5" trianglePattern="1" rotation="0 0 0 " scale="1 1 0" />
            <MechanicalObject template="Vec3" name="mObject1" position="@loader.position"    showIndices="false" showIndicesScale="0.001" />
            <TriangleSetTopologyContainer name="Container"  position="@loader.position"  edges="@loader.edges"  triangles="@loader.triangles" />
            <TriangleSetTopologyModifier name="Modifier" />
            <TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <UniformMass totalMass="1"  />
            <TriangularFEMForceField template="Vec3" name="FEM"  method="large"  poissonRatio="0.3"  youngModulus="20" />
            <BoxConstraint box="-0.05 -0.05 -0.05    0.05 0.05 0.05" drawBoxes="1"  />
            <BoxROI box="-0.05 -0.05 -0.05    0.05 1.05 0.05" drawBoxes="1" name="ProjectToLine"/>
            <LineProjectiveConstraint direction="0.1 1 0" indices="@[-1].indices" drawSize="0.03" />
            <Node 	name="Boundary Edges"  >
                <EdgeSetTopologyContainer name="Container" />
                <EdgeSetTopologyModifier name="Modifier" />
                <EdgeSetGeometryAlgorithms template="Vec3" name="GeomAlgo"  drawEdges="1" />
                <Triangle2EdgeTopologicalMapping name="Mapping"  input="@../Container"  output="@Container" />
                <BoxROI box="0.95 -0.05 -0.05    1.05 1.05 0.05" drawBoxes="1" position="@../mObject1.rest_position" drawEdges="1" edges="@Container.edges" name="pressureBox" />
                <EdgePressureForceField template="Vec3" name="edgePressureFF0"  edgeIndices="@pressureBox.edgeIndices" binormal="0 0 1"  p_intensity="-10" showForces="1" arrowSizeCoef="1"/>
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
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="hideVisualModels showBehavior")
        root.addObject('DefaultAnimationLoop')
        root.addObject('DefaultVisualManagerLoop')

        Square = root.addChild('Square')
        Square.addObject('EulerImplicitSolver', name="Euler Implicit", printLog="0", rayleighStiffness="0.5", rayleighMass="0.5", vdamping="0")
        Square.addObject('CGLinearSolver', template="GraphScattered", name="CG Solver", printLog="0", iterations="40", tolerance="1e-06", threshold="1e-10")
        Square.addObject('GridMeshCreator', name="loader", resolution="5 5", trianglePattern="1", rotation="0 0 0 ", scale="1 1 0")
        Square.addObject('MechanicalObject', template="Vec3", name="mObject1", position="@loader.position", showIndices="false", showIndicesScale="0.001")
        Square.addObject('TriangleSetTopologyContainer', name="Container", position="@loader.position", edges="@loader.edges", triangles="@loader.triangles")
        Square.addObject('TriangleSetTopologyModifier', name="Modifier")
        Square.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        Square.addObject('UniformMass', totalMass="1")
        Square.addObject('TriangularFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.3", youngModulus="20")
        Square.addObject('BoxConstraint', box="-0.05 -0.05 -0.05    0.05 0.05 0.05", drawBoxes="1")
        Square.addObject('BoxROI', box="-0.05 -0.05 -0.05    0.05 1.05 0.05", drawBoxes="1", name="ProjectToLine")
        Square.addObject('LineProjectiveConstraint', direction="0.1 1 0", indices="@[-1].indices", drawSize="0.03")

        Boundary Edges = Square.addChild('Boundary Edges')
        Boundary Edges.addObject('EdgeSetTopologyContainer', name="Container")
        Boundary Edges.addObject('EdgeSetTopologyModifier', name="Modifier")
        Boundary Edges.addObject('EdgeSetGeometryAlgorithms', template="Vec3", name="GeomAlgo", drawEdges="1")
        Boundary Edges.addObject('Triangle2EdgeTopologicalMapping', name="Mapping", input="@../Container", output="@Container")
        Boundary Edges.addObject('BoxROI', box="0.95 -0.05 -0.05    1.05 1.05 0.05", drawBoxes="1", position="@../mObject1.rest_position", drawEdges="1", edges="@Container.edges", name="pressureBox")
        Boundary Edges.addObject('EdgePressureForceField', template="Vec3", name="edgePressureFF0", edgeIndices="@pressureBox.edgeIndices", binormal="0 0 1", p_intensity="-10", showForces="1", arrowSizeCoef="1")
    ```

