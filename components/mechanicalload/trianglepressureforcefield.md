<!-- generate_doc -->
# TrianglePressureForceField

Pressure applied on a triangular geometry.


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
		<td>pressure</td>
		<td>
Pressure force per unit area
		</td>
		<td></td>
	</tr>
	<tr>
		<td>cauchyStress</td>
		<td>
Cauchy Stress applied on the normal of each triangle
		</td>
		<td>[ 0 0 0 , 0 0 0 , 0 0 0]</td>
	</tr>
	<tr>
		<td>triangleList</td>
		<td>
Indices of triangles separated with commas where a pressure is applied
		</td>
		<td></td>
	</tr>
	<tr>
		<td>useConstantForce</td>
		<td>
applied force is computed as the pressure vector times the area at rest
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>trianglePressureMap</td>
		<td>
Map between triangle indices and their pressure
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showForces</td>
		<td>
draw triangles which have a given pressure
		</td>
		<td>0</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseComponent|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseComponent|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|
|topology|link to the topology container|BaseMeshTopology|

## Examples 

TrianglePressureForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <!-- TrianglePressureForceField example scene -->
    <Node name="root" dt="0.05" showBoundingTree="0" gravity="0 0 0">
        <RequiredPlugin pluginName="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin pluginName="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin pluginName="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin pluginName="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin pluginName="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin pluginName="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin pluginName="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin pluginName="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin pluginName="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin pluginName="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin pluginName="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [TrianglePressureForceField] -->
        <RequiredPlugin pluginName="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin pluginName="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin pluginName="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin pluginName="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Tetra2TriangleTopologicalMapping] -->
        <RequiredPlugin pluginName="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin pluginName="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
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
            <include href="Objects/TetrahedronSetTopology.xml" src="@loader" />
            <DiagonalMass massDensity="0.5" />
            <FixedProjectiveConstraint indices="0-50" />
            <TetrahedronFEMForceField name="FEM" youngModulus="60" poissonRatio="0.3" computeGlobalMatrix="false" method="large" />
            <Node name="T">
                <include href="Objects/TriangleSetTopology.xml" src="@../Container"/>
                <Tetra2TriangleTopologicalMapping input="@../Container" output="@Container" />
                <BoxROI name="Roi" position="@../Volume.position" triangles="@Container.triangles" box="-0.5 -0.5 0.9   0.5 0.5 1.1"/>
                <TrianglePressureForceField name="PFF" triangleList="@Roi.triangleIndices" pressure="0 10 10" showForces="1"/>
                <TriangleCollisionModel />
                <Node name="Visu">
                    <OglModel name="Visual" color="yellow" />
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

       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.MechanicalLoad")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Mapping")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', pluginName="Sofa.GL.Component.Rendering3D")
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
       tt.addObject('include', href="Objects/TetrahedronSetTopology.xml", src="@loader")
       tt.addObject('DiagonalMass', massDensity="0.5")
       tt.addObject('FixedProjectiveConstraint', indices="0-50")
       tt.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="60", poissonRatio="0.3", computeGlobalMatrix="false", method="large")

       t = TT.addChild('T')

       t.addObject('include', href="Objects/TriangleSetTopology.xml", src="@../Container")
       t.addObject('Tetra2TriangleTopologicalMapping', input="@../Container", output="@Container")
       t.addObject('BoxROI', name="Roi", position="@../Volume.position", triangles="@Container.triangles", box="-0.5 -0.5 0.9   0.5 0.5 1.1")
       t.addObject('TrianglePressureForceField', name="PFF", triangleList="@Roi.triangleIndices", pressure="0 10 10", showForces="1")
       t.addObject('TriangleCollisionModel', )

       visu = T.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="yellow")
       visu.addObject('IdentityMapping', input="@../../Volume", output="@Visual")
    ```

