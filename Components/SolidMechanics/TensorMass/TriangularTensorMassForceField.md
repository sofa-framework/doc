# TriangularTensorMassForceField

Linear Elastic Membrane on a Triangular Mesh


__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.Component.SolidMechanics.TensorMass`

__namespace__: `#!c++ sofa::component::solidmechanics::tensormass`

__parents__: 

- `#!c++ ForceField`

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
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping - stiffness matrix coefficient
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>edgeInfo</td>
		<td>
Internal edge data
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
Young's modulus in Hooke's law
</td>
		<td>1000</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|mechanicalStates|List of mechanical states to which this component is associated|
|mstate|MechanicalState used by this component|
|topology|link to the topology container|



## Examples

Component/SolidMechanics/TensorMass/TriangularTensorMassForceField.scn

=== "XML"

    ```xml
    <!-- TriangularTensorMassForceField Group Basic Example -->
    <Node name="root" dt="0.005" showBoundingTree="0" gravity="0 -9 1">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.TensorMass"/> <!-- Needed to use components [TriangularTensorMassForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
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
            <TriangularTensorMassForceField name="TM" youngModulus="15" poissonRatio="0.9" />
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
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.005", showBoundingTree="0", gravity="0 -9 1")
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
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.TensorMass")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
        root.addObject('CollisionPipeline', verbose="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField")
        root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")
        root.addObject('DefaultAnimationLoop')

        SquareGravity = root.addChild('SquareGravity')
        SquareGravity.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        SquareGravity.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        SquareGravity.addObject('MeshGmshLoader', name="loader", filename="mesh/square3.msh", createSubelements="true")
        SquareGravity.addObject('MechanicalObject', src="@loader", scale="10")
        SquareGravity.addObject('include', href="Objects/TriangleSetTopology.xml", src="@loader")
        SquareGravity.addObject('DiagonalMass', massDensity="0.015")
        SquareGravity.addObject('FixedProjectiveConstraint', indices="0 1")
        SquareGravity.addObject('TriangularTensorMassForceField', name="TM", youngModulus="15", poissonRatio="0.9")
        SquareGravity.addObject('TriangleCollisionModel')

        SquareGravity = SquareGravity.addChild('SquareGravity')
        SquareGravity.addObject('OglModel', name="Visual", color="yellow")
        SquareGravity.addObject('IdentityMapping', input="@..", output="@Visual")
    ```

