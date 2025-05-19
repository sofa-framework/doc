<!-- generate_doc -->
# RigidDistanceGridCollisionModel

Grid-based distance field.


__Target__: SofaDistanceGrid

__namespace__: sofa::component::collision

__parents__:

- CollisionModel
- SingleStateAccessor

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
		<td>translation</td>
		<td>
translation to apply to input file
		</td>
		<td></td>
	</tr>
	<tr>
		<td>rotation</td>
		<td>
rotation to apply to input file
		</td>
		<td></td>
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
		<td>flipNormals</td>
		<td>
reverse surface direction, i.e. points are considered in collision if they move outside of the object instead of inside
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showMeshPoints</td>
		<td>
Enable rendering of mesh points
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>showGridPoints</td>
		<td>
Enable rendering of grid points
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showMinDist</td>
		<td>
Min distance to render gradients
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showMaxDist</td>
		<td>
Max distance to render gradients
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
|previous|Previous (coarser / upper / parent level) CollisionModel in the hierarchy.|CollisionModel|
|next|Next (finer / lower / child level) CollisionModel in the hierarchy.|CollisionModel|
|collisionElementActiver|CollisionElementActiver component that activates or deactivates collision element(s) during execution|BaseObject|
|mstate|MechanicalState used by this component|MechanicalState&lt;Rigid3d&gt;|

## Examples 

RigidDistanceGridCollisionModel_liver_DefaultAnimationLoop.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.005" gravity="0.0 -9.81 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangularFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [TriangularBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Quad2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="SofaDistanceGrid"/> <!-- Needed to use components [RigidDistanceGridCollisionModel] -->
    
        <DefaultAnimationLoop/>
    
        <CollisionPipeline name="pipeline" depth="6" verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="response" response="PenalityContactForceField" />
    
        <LocalMinDistance name="proximity" alarmDistance="0.3" contactDistance="0.1"/>
    
        <Node name="RigidLiver">
            <MeshOBJLoader name="meshLoader_0" filename="mesh/liver-smooth.obj"/>
            <!-- The state should be defined using a Rigid template for this collision model -->
            <MechanicalObject template="Rigid3d" name="dofs" position="0 0 0    0 0 0 1"/>
            <RigidDistanceGridCollisionModel
                filename="mesh/liver-smooth.obj"
                scale="1.0" 
                usePoints="0" 
                proximity="0.1" 
                contactStiffness="50" 
                contactFriction="0.0" 
            />
            <Node name="Visu">
                <OglModel name="VisualModel" src="@../meshLoader_0" color="white" />
            </Node>
        </Node>
        
        <Node name="Cloth">
            <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9"/>
            
            <RegularGridTopology 
                name="Container" 
                nx="50" ny="1" nz="50" 
                xmin="-9" xmax="5" ymin="7" ymax="7" zmin="-7" zmax="7" 
            />
            <MechanicalObject name="dofs"/>
            <UniformMass totalMass="100" />
            <Node name="T">
                <include href="Objects/TriangleSetTopology.xml" />
                <Quad2TriangleTopologicalMapping input="@../Container" output="@Container" />
                <TriangularFEMForceField name="FEM" youngModulus="60" poissonRatio="0.3" method="large" />
                <TriangularBendingSprings name="FEM-Bend" stiffness="300" damping="1.0" />
                <TriangleCollisionModel contactStiffness="20.0"/>
                <PointCollisionModel/>
                <Node name="Visu">
                    <OglModel 
                        name="Visual" 
                        material="mat1 
                            Diffuse 1 0.5 1.0 0.75 0.8 
                            Ambient 1 0.2 0.2 0.2 1 
                            Specular 1 0.6 0.6 0.6 0.6  
                            Emissive 0 0 0 0 0 
                            Shininess 0 45
                        "
                    />
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
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('RequiredPlugin', name="SofaDistanceGrid")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('CollisionPipeline', name="pipeline", depth="6", verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', name="response", response="PenalityContactForceField")
       root.addObject('LocalMinDistance', name="proximity", alarmDistance="0.3", contactDistance="0.1")

       rigid_liver = root.addChild('RigidLiver')

       rigid_liver.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/liver-smooth.obj")
       rigid_liver.addObject('MechanicalObject', template="Rigid3d", name="dofs", position="0 0 0    0 0 0 1")
       rigid_liver.addObject('RigidDistanceGridCollisionModel', filename="mesh/liver-smooth.obj", scale="1.0", usePoints="0", proximity="0.1", contactStiffness="50", contactFriction="0.0")

       visu = RigidLiver.addChild('Visu')

       visu.addObject('OglModel', name="VisualModel", src="@../meshLoader_0", color="white")

       cloth = root.addChild('Cloth')

       cloth.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
       cloth.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       cloth.addObject('RegularGridTopology', name="Container", nx="50", ny="1", nz="50", xmin="-9", xmax="5", ymin="7", ymax="7", zmin="-7", zmax="7")
       cloth.addObject('MechanicalObject', name="dofs")
       cloth.addObject('UniformMass', totalMass="100")

       t = Cloth.addChild('T')

       t.addObject('include', href="Objects/TriangleSetTopology.xml")
       t.addObject('Quad2TriangleTopologicalMapping', input="@../Container", output="@Container")
       t.addObject('TriangularFEMForceField', name="FEM", youngModulus="60", poissonRatio="0.3", method="large")
       t.addObject('TriangularBendingSprings', name="FEM-Bend", stiffness="300", damping="1.0")
       t.addObject('TriangleCollisionModel', contactStiffness="20.0")
       t.addObject('PointCollisionModel', )

       visu = T.addChild('Visu')

       visu.addObject('OglModel', name="Visual", material="mat1                          Diffuse 1 0.5 1.0 0.75 0.8                          Ambient 1 0.2 0.2 0.2 1                          Specular 1 0.6 0.6 0.6 0.6                           Emissive 0 0 0 0 0                          Shininess 0 45                     ")
       visu.addObject('IdentityMapping', input="@../../dofs", output="@Visual")
    ```

RigidDistanceGridCollisionModel_liver_FreeMotionAnimationLoop.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.005" gravity="0.0 -9.81 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangularFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [TriangularBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Quad2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="SofaDistanceGrid"/> <!-- Needed to use components [RigidDistanceGridCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.AnimationLoop"/> <!-- Needed to use components [FreeMotionAnimationLoop] -->  
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [UncoupledConstraintCorrection] -->  
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Solver"/> <!-- Needed to use components [LCPConstraintSolver] -->  
    
        <FreeMotionAnimationLoop/>
        <LCPConstraintSolver tolerance="1e-3" maxIt="1000"/>
    
        <CollisionPipeline name="pipeline" depth="6" verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="response" response="FrictionContactConstraint" />
    
        <LocalMinDistance name="proximity" alarmDistance="0.3" contactDistance="0.1"/>
    
        <Node name="RigidLiver">
            <MeshOBJLoader name="meshLoader_0" filename="mesh/liver-smooth.obj"/>
            <!-- The state should be defined using a Rigid template for this collision model -->
            <MechanicalObject template="Rigid3d" name="dofs" position="0 0 0    0 0 0 1"/>
            <RigidDistanceGridCollisionModel
                filename="mesh/liver-smooth.obj"
                scale="1.0" 
                usePoints="0" 
                proximity="0.1" 
            />
            <Node name="Visu">
                <OglModel name="VisualModel" src="@../meshLoader_0" color="white" />
            </Node>
        </Node>
        
        <Node name="Cloth">
            <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9"/>
            
            <RegularGridTopology 
                name="Container" 
                nx="50" ny="1" nz="50" 
                xmin="-9" xmax="5" ymin="7" ymax="7" zmin="-7" zmax="7" 
            />
            <MechanicalObject name="dofs"/>
            <UniformMass totalMass="500" />
            <UncoupledConstraintCorrection defaultCompliance="0.1"/>
            <Node name="T">
                <include href="Objects/TriangleSetTopology.xml" />
                <Quad2TriangleTopologicalMapping input="@../Container" output="@Container" />
                <TriangularFEMForceField name="FEM" youngModulus="60" poissonRatio="0.3" method="large" />
                <TriangularBendingSprings name="FEM-Bend" stiffness="600" damping="1.0" />
                <TriangleCollisionModel/>
                <PointCollisionModel/>
                <Node name="Visu">
                    <OglModel 
                        name="Visual" 
                        material="mat1 
                            Diffuse 1 0.5 1.0 0.75 0.8 
                            Ambient 1 0.2 0.2 0.2 1 
                            Specular 1 0.6 0.6 0.6 0.6  
                            Emissive 0 0 0 0 0 
                            Shininess 0 45
                        "
                    />
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
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('RequiredPlugin', name="SofaDistanceGrid")
       root.addObject('RequiredPlugin', name="Sofa.Component.AnimationLoop")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Solver")
       root.addObject('FreeMotionAnimationLoop', )
       root.addObject('LCPConstraintSolver', tolerance="1e-3", maxIt="1000")
       root.addObject('CollisionPipeline', name="pipeline", depth="6", verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', name="response", response="FrictionContactConstraint")
       root.addObject('LocalMinDistance', name="proximity", alarmDistance="0.3", contactDistance="0.1")

       rigid_liver = root.addChild('RigidLiver')

       rigid_liver.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/liver-smooth.obj")
       rigid_liver.addObject('MechanicalObject', template="Rigid3d", name="dofs", position="0 0 0    0 0 0 1")
       rigid_liver.addObject('RigidDistanceGridCollisionModel', filename="mesh/liver-smooth.obj", scale="1.0", usePoints="0", proximity="0.1")

       visu = RigidLiver.addChild('Visu')

       visu.addObject('OglModel', name="VisualModel", src="@../meshLoader_0", color="white")

       cloth = root.addChild('Cloth')

       cloth.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
       cloth.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       cloth.addObject('RegularGridTopology', name="Container", nx="50", ny="1", nz="50", xmin="-9", xmax="5", ymin="7", ymax="7", zmin="-7", zmax="7")
       cloth.addObject('MechanicalObject', name="dofs")
       cloth.addObject('UniformMass', totalMass="500")
       cloth.addObject('UncoupledConstraintCorrection', defaultCompliance="0.1")

       t = Cloth.addChild('T')

       t.addObject('include', href="Objects/TriangleSetTopology.xml")
       t.addObject('Quad2TriangleTopologicalMapping', input="@../Container", output="@Container")
       t.addObject('TriangularFEMForceField', name="FEM", youngModulus="60", poissonRatio="0.3", method="large")
       t.addObject('TriangularBendingSprings', name="FEM-Bend", stiffness="600", damping="1.0")
       t.addObject('TriangleCollisionModel', )
       t.addObject('PointCollisionModel', )

       visu = T.addChild('Visu')

       visu.addObject('OglModel', name="Visual", material="mat1                          Diffuse 1 0.5 1.0 0.75 0.8                          Ambient 1 0.2 0.2 0.2 1                          Specular 1 0.6 0.6 0.6 0.6                           Emissive 0 0 0 0 0                          Shininess 0 45                     ")
       visu.addObject('IdentityMapping', input="@../../dofs", output="@Visual")
    ```

