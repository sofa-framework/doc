<!-- generate_doc -->
# FFDDistanceGridCollisionModel

Grid-based deformable distance field


__Target__: SofaDistanceGrid

__namespace__: sofa::component::collision

__parents__:

- CollisionModel

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
		<td>active</td>
		<td>
flag indicating if this collision model is active and should be included in default collision detections
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>moving</td>
		<td>
flag indicating if this object is changing position between iterations
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>simulated</td>
		<td>
flag indicating if this object is controlled by a simulation
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>selfCollision</td>
		<td>
flag indication if the object can self collide
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>proximity</td>
		<td>
Distance to the actual (visual) surface
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>contactStiffness</td>
		<td>
Contact stiffness
		</td>
		<td>10</td>
	</tr>
	<tr>
		<td>contactFriction</td>
		<td>
Contact friction coefficient (dry or viscous or unused depending on the contact method)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>contactRestitution</td>
		<td>
Contact coefficient of restitution
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>contactResponse</td>
		<td>
if set, indicate to the ContactManager that this model should use the given class of contacts.
Note that this is only indicative, and in particular if both collision models specify a different class it is up to the manager to choose.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>color</td>
		<td>
color used to display the collision model if requested
		</td>
		<td>1 0 0 1</td>
	</tr>
	<tr>
		<td>group</td>
		<td>
IDs of the groups containing this model. No collision can occur between collision models included in a common group (e.g. allowing the same object to have multiple collision models)
		</td>
		<td></td>
	</tr>
	<tr>
		<td>numberOfContacts</td>
		<td>
Number of collision models this collision model is currently attached to
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>filename</td>
		<td>
Load distance grid from specified file
		</td>
		<td></td>
	</tr>
	<tr>
		<td>scale</td>
		<td>
scaling factor for input file
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>sampling</td>
		<td>
if not zero: sample the surface with points approximately separated by the given sampling distance (expressed in voxels if the value is negative)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>box</td>
		<td>
Field bounding box defined by xmin,ymin,zmin, xmax,ymax,zmax
		</td>
		<td></td>
	</tr>
	<tr>
		<td>nx</td>
		<td>
number of values on X axis
		</td>
		<td>64</td>
	</tr>
	<tr>
		<td>ny</td>
		<td>
number of values on Y axis
		</td>
		<td>64</td>
	</tr>
	<tr>
		<td>nz</td>
		<td>
number of values on Z axis
		</td>
		<td>64</td>
	</tr>
	<tr>
		<td>dumpfilename</td>
		<td>
write distance grid to specified file
		</td>
		<td></td>
	</tr>
	<tr>
		<td>usePoints</td>
		<td>
use mesh vertices for collision detection
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>singleContact</td>
		<td>
keep only the deepest contact in each cell
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
|previous|Previous (coarser / upper / parent level) CollisionModel in the hierarchy.|CollisionModel|
|next|Next (finer / lower / child level) CollisionModel in the hierarchy.|CollisionModel|
|collisionElementActiver|CollisionElementActiver component that activates or deactivates collision element(s) during execution|BaseObject|

## Examples 

FFDDistanceGridCollisionModel.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.005" gravity="0.0 -9.81 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField TriangularFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [TriangularBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology SparseGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Quad2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="SofaDistanceGrid"/> <!-- Needed to use components [FFDDistanceGridCollisionModel] -->
        <CollisionPipeline name="pipeline" depth="6" verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="response" response="PenalityContactForceField" />
        <DiscreteIntersection name="proximity" />
        
        <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
        <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            
        
        <Node name="DeformableLiver">
            
            <VisualStyle displayFlags="showForceFields" />
            
            <MechanicalObject />
            <UniformMass totalMass="1000.0" />
            <SparseGridTopology n="8 6 6" fileTopology="mesh/liver-smooth.obj" />
            <BoxROI name="box1" box="-2.5 0 -2.5 7.5 3 2" />
            <FixedProjectiveConstraint indices="@box1.indices"/>
            <HexahedronFEMForceField poissonRatio="0" youngModulus="7000"/>
            <FFDDistanceGridCollisionModel  fileFFDDistanceGrid="mesh/liver-smooth.obj" scale="1.0" usePoints="0" proximity="0.1" contactStiffness="500.0" contactFriction="0.0" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/liver-smooth.obj" translation="0 0 0" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_0" color="red" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
        </Node>
        
        
        <Node name="Cloth">
            
            <VisualStyle displayFlags="hideForceFields" />
            
            <RegularGridTopology nx="50" ny="1" nz="50" xmin="-6" xmax="2" ymin="6" ymax="6" zmin="-4" zmax="4" name="Container" />
            <MechanicalObject name="dofs" />
            <UniformMass totalMass="100" />
            <Node name="T">
                <include href="Objects/TriangleSetTopology.xml" />
                <Quad2TriangleTopologicalMapping input="@../Container" output="@Container" />
                <TriangularFEMForceField name="FEM" youngModulus="60" poissonRatio="0.3" method="large" />
                <TriangularBendingSprings name="FEM-Bend" stiffness="300" damping="1.0" />
                <TriangleCollisionModel />
                <PointCollisionModel />
                <Node name="Visu">
                    <OglModel name="Visual" material="mat1 Diffuse 1 0.5 1.0 0.75 0.8 Ambient 1 0.2 0.2 0.2 1 Specular 1 0.6 0.6 0.6 0.6  Emissive 0 0 0 0 0 Shininess 0 45" />
                    <IdentityMapping input="@../../dofs" output="@Visual" />
                </Node>
            </Node>
        </Node>
        
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.005", gravity="0.0 -9.81 0")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('RequiredPlugin', name="SofaDistanceGrid")
       root.addObject('CollisionPipeline', name="pipeline", depth="6", verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', name="response", response="PenalityContactForceField")
       root.addObject('DiscreteIntersection', name="proximity")
       root.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       root.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")

       deformable_liver = root.addChild('DeformableLiver')

       deformable_liver.addObject('VisualStyle', displayFlags="showForceFields")
       deformable_liver.addObject('MechanicalObject', )
       deformable_liver.addObject('UniformMass', totalMass="1000.0")
       deformable_liver.addObject('SparseGridTopology', n="8 6 6", fileTopology="mesh/liver-smooth.obj")
       deformable_liver.addObject('BoxROI', name="box1", box="-2.5 0 -2.5 7.5 3 2")
       deformable_liver.addObject('FixedProjectiveConstraint', indices="@box1.indices")
       deformable_liver.addObject('HexahedronFEMForceField', poissonRatio="0", youngModulus="7000")
       deformable_liver.addObject('FFDDistanceGridCollisionModel', fileFFDDistanceGrid="mesh/liver-smooth.obj", scale="1.0", usePoints="0", proximity="0.1", contactStiffness="500.0", contactFriction="0.0")

       visu = DeformableLiver.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/liver-smooth.obj", translation="0 0 0", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="red")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       cloth = root.addChild('Cloth')

       cloth.addObject('VisualStyle', displayFlags="hideForceFields")
       cloth.addObject('RegularGridTopology', nx="50", ny="1", nz="50", xmin="-6", xmax="2", ymin="6", ymax="6", zmin="-4", zmax="4", name="Container")
       cloth.addObject('MechanicalObject', name="dofs")
       cloth.addObject('UniformMass', totalMass="100")

       t = Cloth.addChild('T')

       t.addObject('include', href="Objects/TriangleSetTopology.xml")
       t.addObject('Quad2TriangleTopologicalMapping', input="@../Container", output="@Container")
       t.addObject('TriangularFEMForceField', name="FEM", youngModulus="60", poissonRatio="0.3", method="large")
       t.addObject('TriangularBendingSprings', name="FEM-Bend", stiffness="300", damping="1.0")
       t.addObject('TriangleCollisionModel', )
       t.addObject('PointCollisionModel', )

       visu = T.addChild('Visu')

       visu.addObject('OglModel', name="Visual", material="mat1 Diffuse 1 0.5 1.0 0.75 0.8 Ambient 1 0.2 0.2 0.2 1 Specular 1 0.6 0.6 0.6 0.6  Emissive 0 0 0 0 0 Shininess 0 45")
       visu.addObject('IdentityMapping', input="@../../dofs", output="@Visual")
    ```

