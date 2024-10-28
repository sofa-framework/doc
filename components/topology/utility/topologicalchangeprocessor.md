<!-- generate_doc -->
# TopologicalChangeProcessor

Read topological changes and process them.


__Target__: Sofa.Component.Topology.Utility

__namespace__: sofa::component::topology::utility

__parents__:

- BaseObject

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
		<td>filename</td>
		<td>
input file name for topological changes.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>listChanges</td>
		<td>
0 for adding, 1 for removing, 2 for cutting and associated indices.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>interval</td>
		<td>
time duration between 2 actions
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>shift</td>
		<td>
shift between times in the file and times when they will be read
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>loop</td>
		<td>
set to 'true' to re-read the file when reaching the end
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>useDataInputs</td>
		<td>
If true, will perform operation using Data input lists rather than text file.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>timeToRemove</td>
		<td>
If using option useDataInputs, time at which will be done the operations. Possibility to use the interval Data also.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>pointsToRemove</td>
		<td>
List of point IDs to be removed.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>edgesToRemove</td>
		<td>
List of edge IDs to be removed.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>trianglesToRemove</td>
		<td>
List of triangle IDs to be removed.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quadsToRemove</td>
		<td>
List of quad IDs to be removed.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedraToRemove</td>
		<td>
List of tetrahedron IDs to be removed.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedraToRemove</td>
		<td>
List of hexahedron IDs to be removed.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>saveIndicesAtInit</td>
		<td>
set to 'true' to save the incision to do in the init to incise even after a movement
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>epsilonSnapPath</td>
		<td>
epsilon snap path
		</td>
		<td>0.1</td>
	</tr>
	<tr>
		<td>epsilonSnapBorder</td>
		<td>
epsilon snap path
		</td>
		<td>0.25</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>draw</td>
		<td>
draw information
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
|topology|link to the topology container|BaseMeshTopology|

## Examples 

TopologicalChangeProcessor_useDataInputs_option.scn

=== "XML"

    ```xml
    <Node name="root" gravity="0 -9 0" dt="0.01">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangularFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [TriangularBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Utility"/> <!-- Needed to use components [TopologicalChangeProcessor] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <DefaultAnimationLoop/>
    
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
        <CollisionPipeline name="default0" verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="default1" response="PenalityContactForceField" />
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
        <Node name="SquareGravity" gravity="0 -9.81 0">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshGmshLoader name="loader" filename="mesh/square3.msh" createSubelements="true"/>
            <MechanicalObject name="mecaObj" src="@loader" template="Vec3" scale3d="10 10 10" restScale="1" />
            <TriangleSetTopologyContainer src="@loader" name="Container" />
            <TriangleSetTopologyModifier name="Modifier" />
            <TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <DiagonalMass name="default5" massDensity="0.15" />
            <TriangularFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.3" youngModulus="60" />
            <TriangularBendingSprings template="Vec3" name="FEM-Bend" stiffness="300" damping="1" />
            <TriangleCollisionModel name="default7" />
    
            <Node >
                <OglModel name="Visual" material="Default Diffuse 1 0 0 1 0.6 Ambient 1 0.2 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45" />
                <IdentityMapping name="default8" input="@.." output="@Visual" />
            </Node>
    
            <BoxROI template="Vec3" box="2 0 -1 8 -3 1" drawBoxes="1" position="@mecaObj.position" drawTriangles="1" triangles="@Container.triangles" name="trash" />
            <TopologicalChangeProcessor listening="1" useDataInputs="1" trianglesToRemove="@trash.triangleIndices" timeToRemove="0.1" interval="0.05" />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9 0", dt="0.01")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
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
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Utility")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
       root.addObject('CollisionPipeline', name="default0", verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', name="default1", response="PenalityContactForceField")
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")

       square_gravity = root.addChild('SquareGravity', gravity="0 -9.81 0")

       square_gravity.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       square_gravity.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       square_gravity.addObject('MeshGmshLoader', name="loader", filename="mesh/square3.msh", createSubelements="true")
       square_gravity.addObject('MechanicalObject', name="mecaObj", src="@loader", template="Vec3", scale3d="10 10 10", restScale="1")
       square_gravity.addObject('TriangleSetTopologyContainer', src="@loader", name="Container")
       square_gravity.addObject('TriangleSetTopologyModifier', name="Modifier")
       square_gravity.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       square_gravity.addObject('DiagonalMass', name="default5", massDensity="0.15")
       square_gravity.addObject('TriangularFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.3", youngModulus="60")
       square_gravity.addObject('TriangularBendingSprings', template="Vec3", name="FEM-Bend", stiffness="300", damping="1")
       square_gravity.addObject('TriangleCollisionModel', name="default7")

       node = SquareGravity.addChild('node')

       node.addObject('OglModel', name="Visual", material="Default Diffuse 1 0 0 1 0.6 Ambient 1 0.2 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45")
       node.addObject('IdentityMapping', name="default8", input="@..", output="@Visual")

       square_gravity.addObject('BoxROI', template="Vec3", box="2 0 -1 8 -3 1", drawBoxes="1", position="@mecaObj.position", drawTriangles="1", triangles="@Container.triangles", name="trash")
       square_gravity.addObject('TopologicalChangeProcessor', listening="1", useDataInputs="1", trianglesToRemove="@trash.triangleIndices", timeToRemove="0.1", interval="0.05")
    ```

