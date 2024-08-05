# TopologyBoundingTrasher

A class to remove all elements going outside from the given Bounding Box.


__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.Component.Topology.Utility`

__namespace__: `#!c++ sofa::component::topology::utility`

__parents__: 

- `#!c++ BaseObject`

__categories__: 

- _Miscellaneous

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
		<td>position</td>
		<td>
position coordinates of the topology object to interact with.
</td>
		<td></td>
	</tr>
	<tr>
		<td>box</td>
		<td>
List of boxes defined by xmin,ymin,zmin, xmax,ymax,zmax
</td>
		<td>-1000 -1000 -1000 1000 1000 1000</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawBox</td>
		<td>
Draw bounding box (default = false)
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
|topology|link to the topology container|



## Examples

Component/Topology/Utility/TopologyBoundingTrasher.scn

=== "XML"

    ```xml
    <!-- Mechanical MassSpring Group Basic Example -->
    <Node name="root" dt="0.01" showBoundingTree="0" gravity="0 -1 0">
    	<RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
    	<RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
    	<RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
    	<RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
    	<RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
    	<RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
    	<RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
    	<RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
    	<RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangularFEMForceField] -->
    	<RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [StiffSpringForceField TriangularBendingSprings] -->
    	<RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
    	<RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
    	<RequiredPlugin name="Sofa.Component.Topology.Utility"/> <!-- Needed to use components [TopologyBoundingTrasher] -->
    	<RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    	<RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
        <CollisionPipeline verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
        <DefaultAnimationLoop/>
    	
    	<Node name="SquareGravity">
    		<CGImplicit iterations="40" tolerance="1e-6" threshold="1e-10" />
    		<MeshGmshLoader name="loader" filename="mesh/square3.msh" createSubelements="true" />
    		<MechanicalObject name="Volume" src="@loader" scale="10" />
    		<TriangleSetTopologyContainer  name="Container" src="@loader" />
    		<TriangleSetTopologyModifier   name="Modifier" />
    		<TriangleSetGeometryAlgorithms name="GeomAlgo" template="Vec3" />
    		<DiagonalMass massDensity="1" />
    		<StiffSpringForceField name="FF" />
    		<TriangularFEMForceField name="FEM" youngModulus="60" poissonRatio="0.3" method="large" />
    		<TriangularBendingSprings name="FEM-Bend" stiffness="300" damping="1.0" />
    		
    		<TopologyBoundingTrasher box="-10 -10 -10 11 11 11" topology="@Container" drawBox="1" position="@Volume.position"/>
    		<Node >
    			<OglModel name="Visual" color="red" />
    			<IdentityMapping input="@.." output="@Visual" />
    		</Node>
    	</Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01", showBoundingTree="0", gravity="0 -1 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Utility")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
        root.addObject('CollisionPipeline', verbose="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField")
        root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")
        root.addObject('DefaultAnimationLoop')

        SquareGravity = root.addChild('SquareGravity')
        SquareGravity.addObject('CGImplicit', iterations="40", tolerance="1e-6", threshold="1e-10")
        SquareGravity.addObject('MeshGmshLoader', name="loader", filename="mesh/square3.msh", createSubelements="true")
        SquareGravity.addObject('MechanicalObject', name="Volume", src="@loader", scale="10")
        SquareGravity.addObject('TriangleSetTopologyContainer', name="Container", src="@loader")
        SquareGravity.addObject('TriangleSetTopologyModifier', name="Modifier")
        SquareGravity.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
        SquareGravity.addObject('DiagonalMass', massDensity="1")
        SquareGravity.addObject('StiffSpringForceField', name="FF")
        SquareGravity.addObject('TriangularFEMForceField', name="FEM", youngModulus="60", poissonRatio="0.3", method="large")
        SquareGravity.addObject('TriangularBendingSprings', name="FEM-Bend", stiffness="300", damping="1.0")
        SquareGravity.addObject('TopologyBoundingTrasher', box="-10 -10 -10 11 11 11", topology="@Container", drawBox="1", position="@Volume.position")

        SquareGravity = SquareGravity.addChild('SquareGravity')
        SquareGravity.addObject('OglModel', name="Visual", color="red")
        SquareGravity.addObject('IdentityMapping', input="@..", output="@Visual")
    ```

