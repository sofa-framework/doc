<!-- generate_doc -->
# TriangularQuadraticSpringsForceField

Quadratic Springs on a Triangular Mesh.


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.SolidMechanics.Spring

__namespace__: sofa::component::solidmechanics::spring

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
		<td>initialPoints</td>
		<td>
Initial Position
		</td>
		<td></td>
	</tr>
	<tr>
		<td>poissonRatio</td>
		<td>
Poisson ratio in Hooke's law
		</td>
		<td>0.3</td>
	</tr>
	<tr>
		<td>youngModulus</td>
		<td>
Young modulus in Hooke's law
		</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>dampingRatio</td>
		<td>
Ratio damping/stiffness
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>useAngularSprings</td>
		<td>
If Angular Springs should be used or not
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>triangleInfo</td>
		<td>
Internal triangle data
		</td>
		<td></td>
	</tr>
	<tr>
		<td>edgeInfo</td>
		<td>
Internal edge data
		</td>
		<td></td>
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

TriangularQuadraticSpringsForceField.scn

=== "XML"

    ```xml
    <!-- TriangularQuadraticSpringsForceField Basic Example -->
    <Node name="root" dt="0.005" showBoundingTree="0" gravity="0 -9 1">
        <RequiredPlugin pluginName="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin pluginName="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin pluginName="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin pluginName="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin pluginName="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin pluginName="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin pluginName="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin pluginName="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin pluginName="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin pluginName="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin pluginName="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [TriangularQuadraticSpringsForceField] -->
        <RequiredPlugin pluginName="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin pluginName="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin pluginName="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
        <CollisionPipeline verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
        <DefaultAnimationLoop/>
        
        <Node name="SquareGravity">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshGmshLoader name="loader" filename="mesh/square3.msh" createSubelements="true" />
            <MechanicalObject src="@loader" scale="10" />
            <include href="Objects/TriangleSetTopology.xml" src="@loader" />
            <DiagonalMass massDensity="0.015" />
            <FixedProjectiveConstraint indices="0 1" />
            <TriangularQuadraticSpringsForceField name="QS" youngModulus="15" poissonRatio="0.9" useAngularSprings="1" dampingRatio="0.00" />
            <TriangleCollisionModel />
    
            <Node >
              <OglModel name="Visual" color="yellow" />
              <IdentityMapping input="@.." output="@Visual" />
            </Node>
    
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.005", showBoundingTree="0", gravity="0 -9 1")

       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', pluginName="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
       root.addObject('CollisionPipeline', verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', response="PenalityContactForceField")
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")
       root.addObject('DefaultAnimationLoop', )

       square_gravity = root.addChild('SquareGravity')

       square_gravity.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       square_gravity.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       square_gravity.addObject('MeshGmshLoader', name="loader", filename="mesh/square3.msh", createSubelements="true")
       square_gravity.addObject('MechanicalObject', src="@loader", scale="10")
       square_gravity.addObject('include', href="Objects/TriangleSetTopology.xml", src="@loader")
       square_gravity.addObject('DiagonalMass', massDensity="0.015")
       square_gravity.addObject('FixedProjectiveConstraint', indices="0 1")
       square_gravity.addObject('TriangularQuadraticSpringsForceField', name="QS", youngModulus="15", poissonRatio="0.9", useAngularSprings="1", dampingRatio="0.00")
       square_gravity.addObject('TriangleCollisionModel', )

       node = SquareGravity.addChild('node')

       node.addObject('OglModel', name="Visual", color="yellow")
       node.addObject('IdentityMapping', input="@..", output="@Visual")
    ```

