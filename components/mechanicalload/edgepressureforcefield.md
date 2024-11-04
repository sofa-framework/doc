<!-- generate_doc -->
# EdgePressureForceField

Apply a force on edges, distributed on the edge nodes.


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.MechanicalLoad

__namespace__: sofa::component::mechanicalload

__parents__:

- ForceField

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
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping - stiffness matrix coefficient
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>edgePressureMap</td>
		<td>
map between edge indices and their pressure
		</td>
		<td></td>
	</tr>
	<tr>
		<td>pressure</td>
		<td>
Pressure force per unit area
		</td>
		<td></td>
	</tr>
	<tr>
		<td>edgeIndices</td>
		<td>
Indices of edges separated with commas where a pressure is applied
		</td>
		<td></td>
	</tr>
	<tr>
		<td>edges</td>
		<td>
List of edges where a pressure is applied
		</td>
		<td></td>
	</tr>
	<tr>
		<td>normal</td>
		<td>
Normal direction for the plane selection of edges
		</td>
		<td></td>
	</tr>
	<tr>
		<td>dmin</td>
		<td>
Minimum distance from the origin along the normal direction
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>dmax</td>
		<td>
Maximum distance from the origin along the normal direction
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>arrowSizeCoef</td>
		<td>
Size of the drawn arrows (0->no arrows, sign->direction of drawing
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>p_intensity</td>
		<td>
pressure intensity on edge normal
		</td>
		<td></td>
	</tr>
	<tr>
		<td>binormal</td>
		<td>
Binormal of the 2D plane
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showForces</td>
		<td>
draw arrows of edge pressures
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|
|topology|link to the topology container|BaseMeshTopology|

## Examples 

EdgePressureForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node 	name="root" gravity="0 0 3" dt="0.04"  >
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [EdgePressureForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangularFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [TriangularBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [EdgeSetGeometryAlgorithms EdgeSetTopologyContainer EdgeSetTopologyModifier TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Triangle2EdgeTopologicalMapping] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    	<CollisionPipeline name="defaultPipeline1"  verbose="0" />
    	<BruteForceBroadPhase/>
        <BVHNarrowPhase/>
    	<CollisionResponse name="CollisionResponse1"  response="PenalityContactForceField" />
    	<MinProximityIntersection name="Proximity"  alarmDistance="0.8"  contactDistance="0.5" />
    	<DefaultAnimationLoop/>
    
    	<Node name="SquareGravity" >
    		<EulerImplicitSolver name="Euler Implicit"  printLog="0"  rayleighStiffness="0.1"  rayleighMass="0.1"  vdamping="0"  />
    		<CGLinearSolver template="GraphScattered" name="CG Solver"  printLog="0"  iterations="100"  tolerance="1e-06"  threshold="1e-10" />
    		<MeshGmshLoader name="loader"  filename="mesh/square3.msh" createSubelements="true"/>
    		<MechanicalObject template="Vec3" name="mObject1"  position="@loader.position"  velocity="0 0 0"  force="0 0 0"  externalForce="0 0 0"  derivX="0 0 0"  restScale="1"  translation="@loader.translation"  rotation="@loader.rotation"  scale3d="@loader.scale3d" />
    		<TriangleSetTopologyContainer name="Container"  position="@loader.position"  edges="@loader.edges"  triangles="@loader.triangles" />
    		<TriangleSetTopologyModifier name="Modifier" />
    		<TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
    		<DiagonalMass name="diagonalMass1"  massDensity="0.15" />
    
    		<TriangularFEMForceField template="Vec3" name="FEM"  method="large"  poissonRatio="0.3"  youngModulus="60" />
    		<TriangularBendingSprings template="Vec3" name="FEM-Bend"  stiffness="300"  damping="1" />
    		<TriangleCollisionModel template="Vec3" name="tTriangleModel1" />
    
            <Node name="Visual">
    			<OglModel name="Visual"  material="Default Diffuse 1 1 0 0 1 Ambient 1 0.2 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45 No texture linked to the material No bump texture linked to the material " />
    			<IdentityMapping name="identityMap1"  mapForces="0"  mapConstraints="0"  mapMasses="0"  input="@.."  output="@Visual" />
            </Node>
    		<Node name="Edge Mesh" >
    			<EdgeSetTopologyContainer name="Container" />
    			<EdgeSetTopologyModifier name="Modifier" />
    			<EdgeSetGeometryAlgorithms template="Vec3" name="GeomAlgo"  drawEdges="1" />
    			<Triangle2EdgeTopologicalMapping name="Mapping"  input="@../Container"  output="@Container" />
    			<EdgePressureForceField template="Vec3" name="edgePressureFF0"  edges="@Container.edges" pressure="0 0 -0.1" normal="0 0 1"  p_intensity="1" arrowSizeCoef="10"/>
    		</Node>
    	</Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 0 3", dt="0.04")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('CollisionPipeline', name="defaultPipeline1", verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', name="CollisionResponse1", response="PenalityContactForceField")
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")
       root.addObject('DefaultAnimationLoop', )

       square_gravity = root.addChild('SquareGravity')

       square_gravity.addObject('EulerImplicitSolver', name="Euler Implicit", printLog="0", rayleighStiffness="0.1", rayleighMass="0.1", vdamping="0")
       square_gravity.addObject('CGLinearSolver', template="GraphScattered", name="CG Solver", printLog="0", iterations="100", tolerance="1e-06", threshold="1e-10")
       square_gravity.addObject('MeshGmshLoader', name="loader", filename="mesh/square3.msh", createSubelements="true")
       square_gravity.addObject('MechanicalObject', template="Vec3", name="mObject1", position="@loader.position", velocity="0 0 0", force="0 0 0", externalForce="0 0 0", derivX="0 0 0", restScale="1", translation="@loader.translation", rotation="@loader.rotation", scale3d="@loader.scale3d")
       square_gravity.addObject('TriangleSetTopologyContainer', name="Container", position="@loader.position", edges="@loader.edges", triangles="@loader.triangles")
       square_gravity.addObject('TriangleSetTopologyModifier', name="Modifier")
       square_gravity.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       square_gravity.addObject('DiagonalMass', name="diagonalMass1", massDensity="0.15")
       square_gravity.addObject('TriangularFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.3", youngModulus="60")
       square_gravity.addObject('TriangularBendingSprings', template="Vec3", name="FEM-Bend", stiffness="300", damping="1")
       square_gravity.addObject('TriangleCollisionModel', template="Vec3", name="tTriangleModel1")

       visual = SquareGravity.addChild('Visual')

       visual.addObject('OglModel', name="Visual", material="Default Diffuse 1 1 0 0 1 Ambient 1 0.2 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45 No texture linked to the material No bump texture linked to the material ")
       visual.addObject('IdentityMapping', name="identityMap1", mapForces="0", mapConstraints="0", mapMasses="0", input="@..", output="@Visual")

       edge__mesh = SquareGravity.addChild('Edge Mesh')

       edge__mesh.addObject('EdgeSetTopologyContainer', name="Container")
       edge__mesh.addObject('EdgeSetTopologyModifier', name="Modifier")
       edge__mesh.addObject('EdgeSetGeometryAlgorithms', template="Vec3", name="GeomAlgo", drawEdges="1")
       edge__mesh.addObject('Triangle2EdgeTopologicalMapping', name="Mapping", input="@../Container", output="@Container")
       edge__mesh.addObject('EdgePressureForceField', template="Vec3", name="edgePressureFF0", edges="@Container.edges", pressure="0 0 -0.1", normal="0 0 1", p_intensity="1", arrowSizeCoef="10")
    ```

