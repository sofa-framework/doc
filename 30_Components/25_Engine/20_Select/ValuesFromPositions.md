# ValuesFromPositions

Assign values to primitives (vertex/edge/triangle/tetrahedron) based on a linear interpolation of values along a direction


__Templates__:

- `#!c++ Rigid3d`
- `#!c++ Vec3d`

__Target__: `Sofa.Component.Engine.Select`

__namespace__: `#!c++ sofa::component::engine::select`

__parents__: 

- `#!c++ DataEngine`

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
		<td>fieldType</td>
		<td>
field type of output elements
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>inputValues</td>
		<td>
Input values
</td>
		<td></td>
	</tr>
	<tr>
		<td>direction</td>
		<td>
Direction along which the values are interpolated
</td>
		<td>0 1 0</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Rest position coordinates of the degrees of freedom
</td>
		<td></td>
	</tr>
	<tr>
		<td>edges</td>
		<td>
Edge Topology
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
Triangle Topology
</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedra</td>
		<td>
Tetrahedron Topology
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>values</td>
		<td>
Values of the points contained in the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>edgeValues</td>
		<td>
Values of the edges contained in the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangleValues</td>
		<td>
Values of the triangles contained in the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedronValues</td>
		<td>
Values of the tetrahedra contained in the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>pointVectors</td>
		<td>
Vectors of the points contained in the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>edgeVectors</td>
		<td>
Vectors of the edges contained in the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangleVectors</td>
		<td>
Vectors of the triangles contained in the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedronVectors</td>
		<td>
Vectors of the tetrahedra contained in the ROI
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawVectors</td>
		<td>
draw vectors line
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawVectorLength</td>
		<td>
vector length visualisation. 
</td>
		<td>10</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|



## Examples

Component/Engine/Select/ValuesFromPositions_vectorField.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="Root" gravity="0 0 0" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI ValuesFromPositions] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showVisual showBehaviorModels showForceFields showCollision showMapping" />
        <CollisionPipeline name="DefaultCollisionPipeline" verbose="0" draw="0" depth="6" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="Cube" gravity="0 -9.81 0">
            <EulerImplicitSolver name="cg_odesolver" printLog="0"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver template="GraphScattered" name="linear solver" iterations="25" tolerance="1e-09" threshold="1e-09" />
            <RegularGridTopology name="grid" n="6 6 6" min="-10 -10 -10" max="10 10 10" p0="-10 -10 -10" />
            <MechanicalObject template="Vec3" name="mecaObj" src="@grid"/>
            <UniformMass name="default25" vertexMass="0.25" />
            <TetrahedronFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.4" youngModulus="1000" computeGlobalMatrix="0" />
            <BoxROI template="Vec3" name="box_roi" box="-11 -11 -11 11 -9 11" indices="0" drawSize="0" />
            <FixedProjectiveConstraint template="Vec3" name="default27" indices="@box_roi.indices" drawSize="0" />
            <Node name="Tetra" gravity="0 -9.81 0">
                <TetrahedronSetTopologyContainer name="Container" />
                <TetrahedronSetTopologyModifier name="Modifier" />
                <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                <TriangleCollisionModel template="Vec3" name="default30" />
                <Hexa2TetraTopologicalMapping name="default28" input="@../grid" output="@Container" />
                <Node name="interpol" gravity="0 -9.81 0">
                    <ValuesFromPositions template="Vec3" direction="1 1 0" position="@../../mecaObj.position" fieldType="Vector" drawVectors="1" drawVectorLength="5" />
                </Node>
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        Root = rootNode.addChild('Root', gravity="0 0 0", dt="0.02")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        Root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        Root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        Root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        Root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        Root.addObject('DefaultAnimationLoop')
        Root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels showForceFields showCollision showMapping")
        Root.addObject('CollisionPipeline', name="DefaultCollisionPipeline", verbose="0", draw="0", depth="6")
        Root.addObject('BruteForceBroadPhase')
        Root.addObject('BVHNarrowPhase')
        Root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
        Root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

        Cube = Root.addChild('Cube', gravity="0 -9.81 0")
        Cube.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="0", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube.addObject('CGLinearSolver', template="GraphScattered", name="linear solver", iterations="25", tolerance="1e-09", threshold="1e-09")
        Cube.addObject('RegularGridTopology', name="grid", n="6 6 6", min="-10 -10 -10", max="10 10 10", p0="-10 -10 -10")
        Cube.addObject('MechanicalObject', template="Vec3", name="mecaObj", src="@grid")
        Cube.addObject('UniformMass', name="default25", vertexMass="0.25")
        Cube.addObject('TetrahedronFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.4", youngModulus="1000", computeGlobalMatrix="0")
        Cube.addObject('BoxROI', template="Vec3", name="box_roi", box="-11 -11 -11 11 -9 11", indices="0", drawSize="0")
        Cube.addObject('FixedProjectiveConstraint', template="Vec3", name="default27", indices="@box_roi.indices", drawSize="0")

        Tetra = Cube.addChild('Tetra', gravity="0 -9.81 0")
        Tetra.addObject('TetrahedronSetTopologyContainer', name="Container")
        Tetra.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        Tetra.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        Tetra.addObject('TriangleCollisionModel', template="Vec3", name="default30")
        Tetra.addObject('Hexa2TetraTopologicalMapping', name="default28", input="@../grid", output="@Container")

        interpol = Tetra.addChild('interpol', gravity="0 -9.81 0")
        interpol.addObject('ValuesFromPositions', template="Vec3", direction="1 1 0", position="@../../mecaObj.position", fieldType="Vector", drawVectors="1", drawVectorLength="5")
    ```

