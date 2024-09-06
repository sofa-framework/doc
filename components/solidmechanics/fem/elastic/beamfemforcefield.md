<!-- generate_doc -->
# BeamFEMForceField

Beam finite elements


## Rigid3d

Templates:

- Rigid3d

__Target__: Sofa.Component.SolidMechanics.FEM.Elastic

__namespace__: sofa::component::solidmechanics::fem::elastic::_beamfemforcefield_

__parents__:

- BaseLinearElasticityFEMForceField

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
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping - stiffness matrix coefficient
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>poissonRatio</td>
		<td>
FEM Poisson Ratio in Hooke's law [0,0.5[
		</td>
		<td>0.45</td>
	</tr>
	<tr>
		<td>youngModulus</td>
		<td>
FEM Young's Modulus in Hooke's law
		</td>
		<td>5000</td>
	</tr>
	<tr>
		<td>beamsData</td>
		<td>
Internal element data
		</td>
		<td></td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
radius of the section
		</td>
		<td>0.1</td>
	</tr>
	<tr>
		<td>radiusInner</td>
		<td>
inner radius of the section for hollow beams
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>listSegment</td>
		<td>
apply the forcefield to a subset list of beam segments. If no segment defined, forcefield applies to the whole topology
		</td>
		<td></td>
	</tr>
	<tr>
		<td>useSymmetricAssembly</td>
		<td>
use symmetric assembly of the matrix K
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
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Rigid3d&gt;|
|topology|link to the topology container|BaseMeshTopology|

## Examples 

BeamFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    
    <!-- BeamFEMForceField example -->
    <Node name="root" dt="0.01">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel SphereCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [BTDLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BeamLinearMapping IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [BeamFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [CubeTopology MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels hideForceFields showCollisionModels hideVisual showInteractionForceFields" />
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
    
        <Node name="beam-withPointCollision">
            <EulerImplicitSolver rayleighStiffness="0" printLog="false"  rayleighMass="0.1" />
            <BTDLinearSolver template="BTDMatrix6d" printLog="false" verbose="false" />
            <MechanicalObject template="Rigid3" name="DOFs" position="0 0 0 0 0 0 1  1 0 0 0 0 0 1  2 0 0 0 0 0 1  3 0 0 0 0 0 1  4 0 0 0 0 0 1  5 0 0 0 0 0 1  6 0 0 0 0 0 1  7 0 0 0 0 0 1" />
            <MeshTopology name="lines" lines="0 1 1 2 2 3 3 4 4 5 5 6 6 7" />
    
            <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="0" />
            <UniformMass vertexMass="1 1 0.01 0 0 0 0.1 0 0 0 0.1" printLog="false" />
            <BeamFEMForceField name="FEM" radius="0.1" radiusInner="0" youngModulus="20000000" poissonRatio="0.49"/>
    
    
            <Node name="Collision">
                <MechanicalObject />
                <IdentityMapping  />
                <PointCollisionModel name="FloorPoint" />
            </Node>
        </Node>
    
        <Node name="beam-withTriangulatedCubeCollision">
            <EulerImplicitSolver rayleighStiffness="0" printLog="false"  rayleighMass="0.1" />
            <BTDLinearSolver template="BTDMatrix6d" printLog="false" verbose="false" />
            <MechanicalObject template="Rigid3" name="DOFs" position="0 0 -1 0 0 0 1  1 0 -1 0 0 0 1  2 0 -1 0 0 0 1  3 0 -1 0 0 0 1  4 0 -1 0 0 0 1  5 0 -1 0 0 0 1  6 0  -1 0 0 0 1  7 0 -1 0 0 0 1" />
            <MeshTopology name="lines" lines="0 1 1 2 2 3 3 4 4 5 5 6 6 7" />
            <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="0" />
            <UniformMass vertexMass="1 1 0.01 0 0 0 0.1 0 0 0 0.1" printLog="false" />
            <BeamFEMForceField name="FEM" radius="0.1" radiusInner="0" youngModulus="20000000" poissonRatio="0.49"/>
    
            <Node name="Collision">
                <CubeTopology nx="15" ny="2" nz="2" min="0 -0.1 -0.1" max="7 0.1 0.1" />
                <MechanicalObject />
                <BeamLinearMapping isMechanical="true" />
                <TriangleCollisionModel />
                <LineCollisionModel />
                <PointCollisionModel  />
            </Node>
        </Node>
    
    
        <Node name="beam-withSphereCollision">
            <EulerImplicitSolver rayleighStiffness="0" printLog="false" rayleighMass="0.1"/>
            <CGLinearSolver threshold="0.000000001" tolerance="0.0000000001" iterations="25" printLog="false" />
    
            <MechanicalObject template="Rigid3" name="DOFs" position="0 0 1 0 0 0 1  1 0 1 0 0 0 1  2 0 1 0 0 0 1  3 0 1 0 0 0 1" />
            <MeshTopology name="lines" lines="0 1 1 2 2 3" />
            <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="0" />
            <UniformMass totalMass="4" />
            <BeamFEMForceField name="FEM" radius="0.05" radiusInner="0" youngModulus="20000000" poissonRatio="0.49"/>
    
            <Node name="Collision">
                <MechanicalObject />
                <SphereCollisionModel radius="0.4" />
                <IdentityMapping />
            </Node>
        </Node>
    
    
        <Node name="Floor">
            <MeshOBJLoader name="loader" filename="mesh/floor3.obj" scale3d="0.5 0.5 0.5"/>
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader"  dy="-1"/>
            <TriangleCollisionModel name="FloorTriangle" simulated="0" moving="0" contactStiffness="100" />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels hideForceFields showCollisionModels hideVisual showInteractionForceFields")
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       beam_with_point_collision = root.addChild('beam-withPointCollision')

       beam_with_point_collision.addObject('EulerImplicitSolver', rayleighStiffness="0", printLog="false", rayleighMass="0.1")
       beam_with_point_collision.addObject('BTDLinearSolver', template="BTDMatrix6d", printLog="false", verbose="false")
       beam_with_point_collision.addObject('MechanicalObject', template="Rigid3", name="DOFs", position="0 0 0 0 0 0 1  1 0 0 0 0 0 1  2 0 0 0 0 0 1  3 0 0 0 0 0 1  4 0 0 0 0 0 1  5 0 0 0 0 0 1  6 0 0 0 0 0 1  7 0 0 0 0 0 1")
       beam_with_point_collision.addObject('MeshTopology', name="lines", lines="0 1 1 2 2 3 3 4 4 5 5 6 6 7")
       beam_with_point_collision.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="0")
       beam_with_point_collision.addObject('UniformMass', vertexMass="1 1 0.01 0 0 0 0.1 0 0 0 0.1", printLog="false")
       beam_with_point_collision.addObject('BeamFEMForceField', name="FEM", radius="0.1", radiusInner="0", youngModulus="20000000", poissonRatio="0.49")

       collision = beam-withPointCollision.addChild('Collision')

       collision.addObject('MechanicalObject', )
       collision.addObject('IdentityMapping', )
       collision.addObject('PointCollisionModel', name="FloorPoint")

       beam_with_triangulated_cube_collision = root.addChild('beam-withTriangulatedCubeCollision')

       beam_with_triangulated_cube_collision.addObject('EulerImplicitSolver', rayleighStiffness="0", printLog="false", rayleighMass="0.1")
       beam_with_triangulated_cube_collision.addObject('BTDLinearSolver', template="BTDMatrix6d", printLog="false", verbose="false")
       beam_with_triangulated_cube_collision.addObject('MechanicalObject', template="Rigid3", name="DOFs", position="0 0 -1 0 0 0 1  1 0 -1 0 0 0 1  2 0 -1 0 0 0 1  3 0 -1 0 0 0 1  4 0 -1 0 0 0 1  5 0 -1 0 0 0 1  6 0  -1 0 0 0 1  7 0 -1 0 0 0 1")
       beam_with_triangulated_cube_collision.addObject('MeshTopology', name="lines", lines="0 1 1 2 2 3 3 4 4 5 5 6 6 7")
       beam_with_triangulated_cube_collision.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="0")
       beam_with_triangulated_cube_collision.addObject('UniformMass', vertexMass="1 1 0.01 0 0 0 0.1 0 0 0 0.1", printLog="false")
       beam_with_triangulated_cube_collision.addObject('BeamFEMForceField', name="FEM", radius="0.1", radiusInner="0", youngModulus="20000000", poissonRatio="0.49")

       collision = beam-withTriangulatedCubeCollision.addChild('Collision')

       collision.addObject('CubeTopology', nx="15", ny="2", nz="2", min="0 -0.1 -0.1", max="7 0.1 0.1")
       collision.addObject('MechanicalObject', )
       collision.addObject('BeamLinearMapping', isMechanical="true")
       collision.addObject('TriangleCollisionModel', )
       collision.addObject('LineCollisionModel', )
       collision.addObject('PointCollisionModel', )

       beam_with_sphere_collision = root.addChild('beam-withSphereCollision')

       beam_with_sphere_collision.addObject('EulerImplicitSolver', rayleighStiffness="0", printLog="false", rayleighMass="0.1")
       beam_with_sphere_collision.addObject('CGLinearSolver', threshold="0.000000001", tolerance="0.0000000001", iterations="25", printLog="false")
       beam_with_sphere_collision.addObject('MechanicalObject', template="Rigid3", name="DOFs", position="0 0 1 0 0 0 1  1 0 1 0 0 0 1  2 0 1 0 0 0 1  3 0 1 0 0 0 1")
       beam_with_sphere_collision.addObject('MeshTopology', name="lines", lines="0 1 1 2 2 3")
       beam_with_sphere_collision.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="0")
       beam_with_sphere_collision.addObject('UniformMass', totalMass="4")
       beam_with_sphere_collision.addObject('BeamFEMForceField', name="FEM", radius="0.05", radiusInner="0", youngModulus="20000000", poissonRatio="0.49")

       collision = beam-withSphereCollision.addChild('Collision')

       collision.addObject('MechanicalObject', )
       collision.addObject('SphereCollisionModel', radius="0.4")
       collision.addObject('IdentityMapping', )

       floor = root.addChild('Floor')

       floor.addObject('MeshOBJLoader', name="loader", filename="mesh/floor3.obj", scale3d="0.5 0.5 0.5")
       floor.addObject('MeshTopology', src="@loader")
       floor.addObject('MechanicalObject', src="@loader", dy="-1")
       floor.addObject('TriangleCollisionModel', name="FloorTriangle", simulated="0", moving="0", contactStiffness="100")
    ```

