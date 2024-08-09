<!-- generate_doc -->
# ValuesFromPositions

Assign values to primitives (vertex/edge/triangle/tetrahedron) based on a linear interpolation of values along a direction


Templates:

- Rigid3d
- Vec3d

__Target__: Sofa.Component.Engine.Select

__namespace__: sofa::component::engine::select

__parents__:

- DataEngine

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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|

## Examples 

ValuesFromPositions_vectorField.scn

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
    def createScene(root_node):

       root = root_node.addChild('Root', gravity="0 0 0", dt="0.02")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels showForceFields showCollision showMapping")
       root.addObject('CollisionPipeline', name="DefaultCollisionPipeline", verbose="0", draw="0", depth="6")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       cube = Root.addChild('Cube', gravity="0 -9.81 0")

       cube.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="0", rayleighStiffness="0.1", rayleighMass="0.1")
       cube.addObject('CGLinearSolver', template="GraphScattered", name="linear solver", iterations="25", tolerance="1e-09", threshold="1e-09")
       cube.addObject('RegularGridTopology', name="grid", n="6 6 6", min="-10 -10 -10", max="10 10 10", p0="-10 -10 -10")
       cube.addObject('MechanicalObject', template="Vec3", name="mecaObj", src="@grid")
       cube.addObject('UniformMass', name="default25", vertexMass="0.25")
       cube.addObject('TetrahedronFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.4", youngModulus="1000", computeGlobalMatrix="0")
       cube.addObject('BoxROI', template="Vec3", name="box_roi", box="-11 -11 -11 11 -9 11", indices="0", drawSize="0")
       cube.addObject('FixedProjectiveConstraint', template="Vec3", name="default27", indices="@box_roi.indices", drawSize="0")

       tetra = Cube.addChild('Tetra', gravity="0 -9.81 0")

       tetra.addObject('TetrahedronSetTopologyContainer', name="Container")
       tetra.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       tetra.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       tetra.addObject('TriangleCollisionModel', template="Vec3", name="default30")
       tetra.addObject('Hexa2TetraTopologicalMapping', name="default28", input="@../grid", output="@Container")

       interpol = Tetra.addChild('interpol', gravity="0 -9.81 0")

       interpol.addObject('ValuesFromPositions', template="Vec3", direction="1 1 0", position="@../../mecaObj.position", fieldType="Vector", drawVectors="1", drawVectorLength="5")
    ```

