<!-- generate_doc -->
# Tetra2TriangleTopologicalMapping

Topological mapping where TetrahedronSetTopology is converted to TriangleSetTopology


__Target__: Sofa.Component.Topology.Mapping

__namespace__: sofa::component::topology::mapping

__parents__:

- TopologicalMapping

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
		<td>flipNormals</td>
		<td>
Flip Normal ? (Inverse point order when creating triangle)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>noNewTriangles</td>
		<td>
If true no new triangles are being created
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>noInitialTriangles</td>
		<td>
If true the list of initial triangles is initially empty. Only additional triangles will be added in the list
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
|input|Input topology to map|BaseMeshTopology|
|output|Output topology to map|BaseMeshTopology|

## Examples 

Tetra2TriangleTopologicalMapping_with_TetrahedronModel.scn

=== "XML"

    ```xml
    <Node name="root" gravity="0 0 0" dt="0.05">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TetrahedronCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedPlaneProjectiveConstraint FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [TrianglePressureForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedralCorotationalFEMForceField TriangularFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [TriangularBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Tetra2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
        <CollisionPipeline name="default0" verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="default1" response="PenalityContactForceField" />
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
        <DefaultAnimationLoop/>
        <Node name="TT" gravity="0 -9.81 0">
            <EulerImplicitSolver name="cg_odesolver" printLog="0"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver template="GraphScattered" name="linear solver" iterations="25" tolerance="1e-09" threshold="1e-09" />
            <MeshGmshLoader name="loader" filename="mesh/cylinder.msh" />
            <MechanicalObject src="@loader" template="Vec3" name="Volume" restScale="1" />
            <TetrahedronSetTopologyContainer src="@loader" name="Container" />
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <DiagonalMass template="Vec3,Vec3" name="default3" massDensity="0.5" />
            <FixedPlaneProjectiveConstraint template="Vec3" name="default4" direction="0 0 1" dmin="-0.1" dmax="0.1" />
            <FixedProjectiveConstraint template="Vec3" name="default5" indices="0" />
            <TetrahedronCollisionModel />
            <TetrahedralCorotationalFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.3" youngModulus="360" assembling="0" />
            <Node name="T" gravity="0 -9.81 0">
                <TriangleSetTopologyContainer name="Container" tags="meca" />
                <TriangleSetTopologyModifier name="Modifier" tags="meca" />
                <TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo" tags="meca" />
                <Tetra2TriangleTopologicalMapping name="default6" input="@../Container" output="@Container" />
                <TriangularFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.3" youngModulus="60" />
                <TriangularBendingSprings template="Vec3" name="FEM-Bend" stiffness="300" damping="1" />
                <BoxROI name="pressureROI" position="@../Volume.position" triangles="@Container.triangles" box="0.9 -0.01 -0.01   1.1 1.01 1.01" drawBoxes="1"/>
                <TrianglePressureForceField name="PFF" triangleList="@pressureROI.triangleIndices" pressure="0.4 0 0"/>
                <Node name="Visu" gravity="0 -9.81 0">
                    <OglModel template="Vec3" name="Visual" material="Default Diffuse 1 0 0 1 1 Ambient 1 0 0 0.2 1 Specular 0 0 0 1 1 Emissive 0 0 0 1 1 Shininess 0 45" />
                    <IdentityMapping template="Vec3,Vec3" name="default9" input="@../../Volume" output="@Visual" />
                </Node>
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 0 0", dt="0.05")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
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
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
       root.addObject('CollisionPipeline', name="default0", verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', name="default1", response="PenalityContactForceField")
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")
       root.addObject('DefaultAnimationLoop', )

       tt = root.addChild('TT', gravity="0 -9.81 0")

       tt.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="0", rayleighStiffness="0.1", rayleighMass="0.1")
       tt.addObject('CGLinearSolver', template="GraphScattered", name="linear solver", iterations="25", tolerance="1e-09", threshold="1e-09")
       tt.addObject('MeshGmshLoader', name="loader", filename="mesh/cylinder.msh")
       tt.addObject('MechanicalObject', src="@loader", template="Vec3", name="Volume", restScale="1")
       tt.addObject('TetrahedronSetTopologyContainer', src="@loader", name="Container")
       tt.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       tt.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       tt.addObject('DiagonalMass', template="Vec3,Vec3", name="default3", massDensity="0.5")
       tt.addObject('FixedPlaneProjectiveConstraint', template="Vec3", name="default4", direction="0 0 1", dmin="-0.1", dmax="0.1")
       tt.addObject('FixedProjectiveConstraint', template="Vec3", name="default5", indices="0")
       tt.addObject('TetrahedronCollisionModel', )
       tt.addObject('TetrahedralCorotationalFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.3", youngModulus="360", assembling="0")

       t = TT.addChild('T', gravity="0 -9.81 0")

       t.addObject('TriangleSetTopologyContainer', name="Container", tags="meca")
       t.addObject('TriangleSetTopologyModifier', name="Modifier", tags="meca")
       t.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo", tags="meca")
       t.addObject('Tetra2TriangleTopologicalMapping', name="default6", input="@../Container", output="@Container")
       t.addObject('TriangularFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.3", youngModulus="60")
       t.addObject('TriangularBendingSprings', template="Vec3", name="FEM-Bend", stiffness="300", damping="1")
       t.addObject('BoxROI', name="pressureROI", position="@../Volume.position", triangles="@Container.triangles", box="0.9 -0.01 -0.01   1.1 1.01 1.01", drawBoxes="1")
       t.addObject('TrianglePressureForceField', name="PFF", triangleList="@pressureROI.triangleIndices", pressure="0.4 0 0")

       visu = T.addChild('Visu', gravity="0 -9.81 0")

       visu.addObject('OglModel', template="Vec3", name="Visual", material="Default Diffuse 1 0 0 1 1 Ambient 1 0 0 0.2 1 Specular 0 0 0 1 1 Emissive 0 0 0 1 1 Shininess 0 45")
       visu.addObject('IdentityMapping', template="Vec3,Vec3", name="default9", input="@../../Volume", output="@Visual")
    ```

Tetra2TriangleTopologicalMapping_NoInitialTriangle_option.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.05" showBoundingTree="0" gravity="0 0 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedPlaneProjectiveConstraint FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedralCorotationalFEMForceField TriangularFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [TriangularBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Tetra2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
        <CollisionPipeline verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
        <DefaultAnimationLoop/>
        <Node name="TT">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshGmshLoader name="loader" filename="mesh/cylinder.msh" />
            <MechanicalObject src="@loader" name="Volume" />
            <include href="Objects/TetrahedronSetTopology.xml" src="@loader" tags=" " />
            <DiagonalMass massDensity="0.5" />
            <FixedPlaneProjectiveConstraint direction="0 0 1" dmin="-0.1" dmax="0.1" />
            <FixedProjectiveConstraint indices="0" />
            <TetrahedralCorotationalFEMForceField name="FEM" youngModulus="360" poissonRatio="0.3" method="large" />
            <TriangleCollisionModel />
            <Node name="T1">
                <include href="Objects/TriangleSetTopology.xml" src="@../loader" tags=" " />
                <Tetra2TriangleTopologicalMapping input="@../Container" output="@Container" noNewTriangles="1" />
                <TriangularFEMForceField name="FEM" youngModulus="60" poissonRatio="0.3" method="large" />
                <TriangularBendingSprings name="FEM-Bend" stiffness="300" damping="1.0" />
                <Node name="Visu">
                    <OglModel name="Visual" color="blue" />
                    <IdentityMapping input="@../../Volume" output="@Visual" />
                </Node>
            </Node>
            <Node name="T2">
                <include href="Objects/TriangleSetTopology.xml" src="@../Container" tags=" " />
                <Tetra2TriangleTopologicalMapping input="@../Container" output="@Container" noInitialTriangles="1" />
                <Node name="Visu">
                    <OglModel name="Visual" color="red" />
                    <IdentityMapping input="@../../Volume" output="@Visual" />
                </Node>
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.05", showBoundingTree="0", gravity="0 0 0")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
       root.addObject('CollisionPipeline', verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', response="PenalityContactForceField")
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")
       root.addObject('DefaultAnimationLoop', )

       tt = root.addChild('TT')

       tt.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       tt.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       tt.addObject('MeshGmshLoader', name="loader", filename="mesh/cylinder.msh")
       tt.addObject('MechanicalObject', src="@loader", name="Volume")
       tt.addObject('include', href="Objects/TetrahedronSetTopology.xml", src="@loader", tags=" ")
       tt.addObject('DiagonalMass', massDensity="0.5")
       tt.addObject('FixedPlaneProjectiveConstraint', direction="0 0 1", dmin="-0.1", dmax="0.1")
       tt.addObject('FixedProjectiveConstraint', indices="0")
       tt.addObject('TetrahedralCorotationalFEMForceField', name="FEM", youngModulus="360", poissonRatio="0.3", method="large")
       tt.addObject('TriangleCollisionModel', )

       t1 = TT.addChild('T1')

       t1.addObject('include', href="Objects/TriangleSetTopology.xml", src="@../loader", tags=" ")
       t1.addObject('Tetra2TriangleTopologicalMapping', input="@../Container", output="@Container", noNewTriangles="1")
       t1.addObject('TriangularFEMForceField', name="FEM", youngModulus="60", poissonRatio="0.3", method="large")
       t1.addObject('TriangularBendingSprings', name="FEM-Bend", stiffness="300", damping="1.0")

       visu = T1.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="blue")
       visu.addObject('IdentityMapping', input="@../../Volume", output="@Visual")

       t2 = TT.addChild('T2')

       t2.addObject('include', href="Objects/TriangleSetTopology.xml", src="@../Container", tags=" ")
       t2.addObject('Tetra2TriangleTopologicalMapping', input="@../Container", output="@Container", noInitialTriangles="1")

       visu = T2.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="red")
       visu.addObject('IdentityMapping', input="@../../Volume", output="@Visual")
    ```

Tetra2TriangleTopologicalMapping.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.05" showBoundingTree="0" gravity="0 0 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedPlaneProjectiveConstraint FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [TrianglePressureForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedralCorotationalFEMForceField TriangularFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [TriangularBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Tetra2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->  
        
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
        <CollisionPipeline verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
        <DefaultAnimationLoop/>
        <Node name="TT">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshGmshLoader name="loader" filename="mesh/cylinder.msh" />
            <MechanicalObject src="@loader" name="Volume" />
            <include href="Objects/TetrahedronSetTopology.xml" src="@loader" tags=" " />
            <DiagonalMass massDensity="0.5" />
            <FixedPlaneProjectiveConstraint direction="0 0 1" dmin="-0.1" dmax="0.1" />
            <FixedProjectiveConstraint indices="0" />
            <TetrahedralCorotationalFEMForceField name="FEM" youngModulus="360" poissonRatio="0.3" method="large" />
            <Node name="T">
                <TriangleSetTopologyContainer name="Container" />
                <TriangleSetTopologyModifier/>
                <Tetra2TriangleTopologicalMapping input="@../Container" output="@Container" />
                <TriangularFEMForceField name="FEM" youngModulus="60" poissonRatio="0.3" method="large" />
                <TriangularBendingSprings name="FEM-Bend" stiffness="300" damping="1.0" />
                <BoxROI name="BoxROI" position="@../Volume.position" triangles="@Container.triangles" box="-0.5 -0.5 0.9 0.5 0.5 1.1" drawTriangles="true"/>
                <TrianglePressureForceField triangleList="@BoxROI.triangleIndices" pressure="0.4 0 0" />
                <TriangleCollisionModel />
                <Node name="Visu">
                    <OglModel name="Visual" color="blue" />
                    <IdentityMapping input="@../../Volume" output="@Visual" />
                </Node>
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.05", showBoundingTree="0", gravity="0 0 0")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
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
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
       root.addObject('CollisionPipeline', verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', response="PenalityContactForceField")
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")
       root.addObject('DefaultAnimationLoop', )

       tt = root.addChild('TT')

       tt.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       tt.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       tt.addObject('MeshGmshLoader', name="loader", filename="mesh/cylinder.msh")
       tt.addObject('MechanicalObject', src="@loader", name="Volume")
       tt.addObject('include', href="Objects/TetrahedronSetTopology.xml", src="@loader", tags=" ")
       tt.addObject('DiagonalMass', massDensity="0.5")
       tt.addObject('FixedPlaneProjectiveConstraint', direction="0 0 1", dmin="-0.1", dmax="0.1")
       tt.addObject('FixedProjectiveConstraint', indices="0")
       tt.addObject('TetrahedralCorotationalFEMForceField', name="FEM", youngModulus="360", poissonRatio="0.3", method="large")

       t = TT.addChild('T')

       t.addObject('TriangleSetTopologyContainer', name="Container")
       t.addObject('TriangleSetTopologyModifier', )
       t.addObject('Tetra2TriangleTopologicalMapping', input="@../Container", output="@Container")
       t.addObject('TriangularFEMForceField', name="FEM", youngModulus="60", poissonRatio="0.3", method="large")
       t.addObject('TriangularBendingSprings', name="FEM-Bend", stiffness="300", damping="1.0")
       t.addObject('BoxROI', name="BoxROI", position="@../Volume.position", triangles="@Container.triangles", box="-0.5 -0.5 0.9 0.5 0.5 1.1", drawTriangles="true")
       t.addObject('TrianglePressureForceField', triangleList="@BoxROI.triangleIndices", pressure="0.4 0 0")
       t.addObject('TriangleCollisionModel', )

       visu = T.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="blue")
       visu.addObject('IdentityMapping', input="@../../Volume", output="@Visual")
    ```

