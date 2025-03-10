<!-- generate_doc -->
# ShapeMatching

Compute target positions using shape matching deformation method by Mueller et al.


## Rigid3d

Templates:

- Rigid3d

__Target__: Sofa.Component.Engine.Analyze

__namespace__: sofa::component::engine::analyze

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
list of the subsets the object belongs to
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
		<td>iterations</td>
		<td>
Number of iterations.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>affineRatio</td>
		<td>
Blending between affine and rigid.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>fixedweight</td>
		<td>
weight of fixed particles.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>fixedPosition0</td>
		<td>
rest positions of non mechanical particles.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>fixedPosition</td>
		<td>
current (fixed) positions of non mechanical particles.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Input positions.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>cluster</td>
		<td>
Input clusters.
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>targetPosition</td>
		<td>
Computed target positions.
		</td>
		<td></td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Rigid3d&gt;|

<!-- generate_doc -->
## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.Engine.Analyze

__namespace__: sofa::component::engine::analyze

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
list of the subsets the object belongs to
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
		<td>iterations</td>
		<td>
Number of iterations.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>affineRatio</td>
		<td>
Blending between affine and rigid.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>fixedweight</td>
		<td>
weight of fixed particles.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>fixedPosition0</td>
		<td>
rest positions of non mechanical particles.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>fixedPosition</td>
		<td>
current (fixed) positions of non mechanical particles.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Input positions.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>cluster</td>
		<td>
Input clusters.
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>targetPosition</td>
		<td>
Computed target positions.
		</td>
		<td></td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|

## Examples 

ShapeMatching.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node 	name="root" gravity="0 -1 0" dt="0.05"  >
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [PositionBasedDynamicsProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Analyze"/> <!-- Needed to use components [ClusteringEngine ShapeMatching] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <CollisionPipeline verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
    	<Node 	name="dragon"  >
    		<EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
    		<CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    		<MeshOBJLoader name="loader" filename="mesh/dragon.obj" />
    		<MeshTopology name="topo" src="@loader" />
    		<MechanicalObject name="dofs" src="@loader" scale="1" dz="10" />
    		<UniformMass vertexMass="3" />
    
    		<ClusteringEngine template="Vec3" name="clustering" radius='1'  number='50' position="@topo.position"/>
    		<ShapeMatching template="Vec3" name="shapeMatching" iterations='1' position="@dofs.position" cluster="@clustering.cluster"/>
    	 	<PositionBasedDynamicsProjectiveConstraint template="Vec3" stiffness = '1' position="@shapeMatching.targetPosition"/>
    		
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_1" filename="mesh/dragon.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_1" color="red" dz="10" />
                <IdentityMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Surf">
                <MeshOBJLoader name="loader" filename="mesh/dragon.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dz="10" />
                <TriangleCollisionModel contactStiffness="1000" />
                <LineCollisionModel contactStiffness="1000" />
                <PointCollisionModel contactStiffness="1000" />
                <IdentityMapping />
            </Node>
    	</Node>
        <Node name="Floor">
            <MeshOBJLoader name="loader" filename="mesh/floor3.obj" />
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader" dy="-10" scale="1.75" />
            <TriangleCollisionModel name="FloorTriangle" simulated="0" moving="0" />
            <LineCollisionModel name="FloorLine" simulated="0" moving="0" />
            <PointCollisionModel name="FloorPoint" simulated="0" moving="0" />
            <MeshOBJLoader name="meshLoader_0" filename="mesh/floor3.obj" scale="1.75" handleSeams="1" />
            <OglModel name="FloorV" src="@meshLoader_0" texturename="textures/brushed_metal.bmp" dy="-10" />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -1 0", dt="0.05")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Analyze")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
       root.addObject('CollisionPipeline', verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       dragon = root.addChild('dragon')

       dragon.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       dragon.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       dragon.addObject('MeshOBJLoader', name="loader", filename="mesh/dragon.obj")
       dragon.addObject('MeshTopology', name="topo", src="@loader")
       dragon.addObject('MechanicalObject', name="dofs", src="@loader", scale="1", dz="10")
       dragon.addObject('UniformMass', vertexMass="3")
       dragon.addObject('ClusteringEngine', template="Vec3", name="clustering", radius="1", number="50", position="@topo.position")
       dragon.addObject('ShapeMatching', template="Vec3", name="shapeMatching", iterations="1", position="@dofs.position", cluster="@clustering.cluster")
       dragon.addObject('PositionBasedDynamicsProjectiveConstraint', template="Vec3", stiffness="1", position="@shapeMatching.targetPosition")

       visu = dragon.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/dragon.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="red", dz="10")
       visu.addObject('IdentityMapping', input="@..", output="@Visual")

       surf = dragon.addChild('Surf')

       surf.addObject('MeshOBJLoader', name="loader", filename="mesh/dragon.obj")
       surf.addObject('MeshTopology', src="@loader")
       surf.addObject('MechanicalObject', src="@loader", dz="10")
       surf.addObject('TriangleCollisionModel', contactStiffness="1000")
       surf.addObject('LineCollisionModel', contactStiffness="1000")
       surf.addObject('PointCollisionModel', contactStiffness="1000")
       surf.addObject('IdentityMapping', )

       floor = root.addChild('Floor')

       floor.addObject('MeshOBJLoader', name="loader", filename="mesh/floor3.obj")
       floor.addObject('MeshTopology', src="@loader")
       floor.addObject('MechanicalObject', src="@loader", dy="-10", scale="1.75")
       floor.addObject('TriangleCollisionModel', name="FloorTriangle", simulated="0", moving="0")
       floor.addObject('LineCollisionModel', name="FloorLine", simulated="0", moving="0")
       floor.addObject('PointCollisionModel', name="FloorPoint", simulated="0", moving="0")
       floor.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/floor3.obj", scale="1.75", handleSeams="1")
       floor.addObject('OglModel', name="FloorV", src="@meshLoader_0", texturename="textures/brushed_metal.bmp", dy="-10")
    ```

