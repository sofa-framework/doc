# DataDisplay

Rendering of meshes colored by data


__Target__: `Sofa.GL.Component.Rendering3D`

__namespace__: `#!c++ sofa::gl::component::rendering3d`

__parents__: 

- `#!c++ VisualModel`
- `#!c++ VisualState`

__categories__: 

- VisualModel

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
		<td>enable</td>
		<td>
Display the object or not
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>maximalRange</td>
		<td>
Keep the maximal range through all timesteps
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>pointData</td>
		<td>
Data associated with nodes
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangleData</td>
		<td>
Data associated with triangles
</td>
		<td></td>
	</tr>
	<tr>
		<td>quadData</td>
		<td>
Data associated with quads
</td>
		<td></td>
	</tr>
	<tr>
		<td>pointTriangleData</td>
		<td>
Data associated with nodes per triangle
</td>
		<td></td>
	</tr>
	<tr>
		<td>pointQuadData</td>
		<td>
Data associated with nodes per quad
</td>
		<td></td>
	</tr>
	<tr>
		<td>colorNaN</td>
		<td>
Color used for NaN values (default=[0.0,0.0,0.0,1.0])
</td>
		<td>0 0 0 1</td>
	</tr>
	<tr>
		<td>userRange</td>
		<td>
Clamp to this values (if max&gt;min)
</td>
		<td>1 -1</td>
	</tr>
	<tr>
		<td>currentMin</td>
		<td>
Current min range
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>currentMax</td>
		<td>
Current max range
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>shininess</td>
		<td>
Shininess for rendering point-based data [0,128].  &lt;0 means no specularity
</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>transparency</td>
		<td>
transparency draw objects with transparency, the value varies between 0. and 1. Where 1. means no transparency and 0 full transparency
</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Vector</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Vertices coordinates
</td>
		<td></td>
	</tr>
	<tr>
		<td>restPosition</td>
		<td>
Vertices rest coordinates
</td>
		<td></td>
	</tr>
	<tr>
		<td>normal</td>
		<td>
Normals of the model
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
|topology|link to the topology container|



## Examples

Component/Visual/DataDisplay.scn

=== "XML"

    ```xml
    <!-- Use of DataDisplay to show distances from rest shape  -->
    <Node name="root" gravity="0 0 -1" dt="0.05">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangleFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [TriangleBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering2D"/> <!-- Needed to use components [OglColorMap] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [DataDisplay] -->
        <RequiredPlugin name="SofaValidation"/> <!-- Needed to use components [EvalPointsDistance] -->
        
        <VisualStyle displayFlags="showVisual hideBehavior hideCollision hideMapping" />
        <CollisionPipeline verbose="0" name="CollisionPipeline" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" name="collision response" />
        <DiscreteIntersection />
        <DefaultAnimationLoop/>
    
        <Node name="Mesh">
            <RegularGridTopology name="Grid" nx="10" ny="10" nz="1" xmin="0" xmax="9" ymin="0" ymax="9" zmin="0" zmax="1" />
            <MechanicalObject name="MO" />
        </Node>
    
        <Node name="Simulation">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <RegularGridTopology src="@/Mesh/Grid" />
            <MechanicalObject />
            <UniformMass vertexMass="0.1" />
            <FixedProjectiveConstraint indices="0 9 99" />
            <TriangleFEMForceField name="FEM3" youngModulus="5000" poissonRatio="0.3" method="large" />
            <TriangleBendingSprings name="FEM-Bend" stiffness="100" damping="0.1" />
            <TriangleCollisionModel />
    
            <EvalPointsDistance name="dist" object1="@/Mesh/MO" object2="@." listening="true" period="0.05" draw="false" />
    
            
            <Node name="Data">
                <DataDisplay pointData="@../dist.distance" />
                <OglColorMap colorScheme="Blue to Red" />
                <IdentityMapping input="@.." output="@."/>
            </Node>
    
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 0 -1", dt="0.05")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering2D")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('RequiredPlugin', name="SofaValidation")
        root.addObject('VisualStyle', displayFlags="showVisual hideBehavior hideCollision hideMapping")
        root.addObject('CollisionPipeline', verbose="0", name="CollisionPipeline")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField", name="collision response")
        root.addObject('DiscreteIntersection')
        root.addObject('DefaultAnimationLoop')

        Mesh = root.addChild('Mesh')
        Mesh.addObject('RegularGridTopology', name="Grid", nx="10", ny="10", nz="1", xmin="0", xmax="9", ymin="0", ymax="9", zmin="0", zmax="1")
        Mesh.addObject('MechanicalObject', name="MO")

        Simulation = root.addChild('Simulation')
        Simulation.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        Simulation.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        Simulation.addObject('RegularGridTopology', src="@/Mesh/Grid")
        Simulation.addObject('MechanicalObject')
        Simulation.addObject('UniformMass', vertexMass="0.1")
        Simulation.addObject('FixedProjectiveConstraint', indices="0 9 99")
        Simulation.addObject('TriangleFEMForceField', name="FEM3", youngModulus="5000", poissonRatio="0.3", method="large")
        Simulation.addObject('TriangleBendingSprings', name="FEM-Bend", stiffness="100", damping="0.1")
        Simulation.addObject('TriangleCollisionModel')
        Simulation.addObject('EvalPointsDistance', name="dist", object1="@/Mesh/MO", object2="@.", listening="true", period="0.05", draw="false")

        Data = Simulation.addChild('Data')
        Data.addObject('DataDisplay', pointData="@../dist.distance")
        Data.addObject('OglColorMap', colorScheme="Blue to Red")
        Data.addObject('IdentityMapping', input="@..", output="@.")
    ```

