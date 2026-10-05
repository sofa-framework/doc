<!-- generate_doc -->
# HexahedronFEMForceField

Hexahedral finite elements.


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.SolidMechanics.FEM.Elastic

__namespace__: sofa::component::solidmechanics::fem::elastic

__parents__:

- BaseLinearElasticityFEMForceField
- BaseRotationFinder

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
		<td>method</td>
		<td>
"large" or "polar" or "small" displacements
		</td>
		<td>large</td>
	</tr>
	<tr>
		<td>updateStiffnessMatrix</td>
		<td>

		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>gatherPt</td>
		<td>
number of dof accumulated per threads during the gather operation (Only use in GPU version)
		</td>
		<td></td>
	</tr>
	<tr>
		<td>gatherBsize</td>
		<td>
number of dof accumulated per threads during the gather operation (Only use in GPU version)
		</td>
		<td></td>
	</tr>
	<tr>
		<td>stiffnessMatrices</td>
		<td>
Stiffness matrices per element (K_i)
		</td>
		<td></td>
	</tr>
	<tr>
		<td>initialPoints</td>
		<td>
Initial Position
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawing</td>
		<td>
draw the forcefield if true
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>drawPercentageOffset</td>
		<td>
size of the hexa
		</td>
		<td>0.15</td>
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
|topology|Link to a topology|BaseMeshTopology|

## Examples 

HexahedronFEMForceFieldAndMass.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.02">
        <RequiredPlugin pluginName="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin pluginName="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin pluginName="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin pluginName="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin pluginName="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin pluginName="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin pluginName="Sofa.Component.IntegrationScheme.Backward"/> <!-- Needed to use components [EulerImplicitIntegrationScheme] -->
        <RequiredPlugin pluginName="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceFieldAndMass] -->
        <RequiredPlugin pluginName="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin pluginName="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.5" contactDistance="0.3" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="M1">
            <EulerImplicitIntegrationScheme name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject />
            <RegularGridTopology nx="4" ny="4" nz="20" xmin="-9" xmax="-6" ymin="0" ymax="3" zmin="0" zmax="19" />
            <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15" />
            <HexahedronFEMForceFieldAndMass name="FEM" youngModulus="40000" poissonRatio="0.3" method="large" density="1" />
            <TriangleCollisionModel />
            <LineCollisionModel />
            <PointCollisionModel />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02")

       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.IntegrationScheme.Backward")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Visual")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.5", contactDistance="0.3")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       m1 = root.addChild('M1')

       m1.addObject('EulerImplicitIntegrationScheme', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       m1.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       m1.addObject('MechanicalObject', )
       m1.addObject('RegularGridTopology', nx="4", ny="4", nz="20", xmin="-9", xmax="-6", ymin="0", ymax="3", zmin="0", zmax="19")
       m1.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15")
       m1.addObject('HexahedronFEMForceFieldAndMass', name="FEM", youngModulus="40000", poissonRatio="0.3", method="large", density="1")
       m1.addObject('TriangleCollisionModel', )
       m1.addObject('LineCollisionModel', )
       m1.addObject('PointCollisionModel', )
    ```

HexahedronFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.02">
        <RequiredPlugin pluginName="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin pluginName="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin pluginName="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin pluginName="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin pluginName="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin pluginName="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin pluginName="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin pluginName="Sofa.Component.IntegrationScheme.Backward"/> <!-- Needed to use components [EulerImplicitIntegrationScheme] -->
        <RequiredPlugin pluginName="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField] -->
        <RequiredPlugin pluginName="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin pluginName="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.5" contactDistance="0.3" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="M1">
            <EulerImplicitIntegrationScheme name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" template="CompressedRowSparseMatrixMat3x3"/>
            <MechanicalObject />
            <UniformMass vertexMass="1" />
            <RegularGridTopology nx="4" ny="4" nz="20" xmin="-9" xmax="-6" ymin="0" ymax="3" zmin="0" zmax="19" />
            <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15" />
            <HexahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" method="large" />
            <TriangleCollisionModel />
            <LineCollisionModel />
            <PointCollisionModel />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02")

       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.IntegrationScheme.Backward")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Visual")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.5", contactDistance="0.3")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       m1 = root.addChild('M1')

       m1.addObject('EulerImplicitIntegrationScheme', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       m1.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9", template="CompressedRowSparseMatrixMat3x3")
       m1.addObject('MechanicalObject', )
       m1.addObject('UniformMass', vertexMass="1")
       m1.addObject('RegularGridTopology', nx="4", ny="4", nz="20", xmin="-9", xmax="-6", ymin="0", ymax="3", zmin="0", zmax="19")
       m1.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15")
       m1.addObject('HexahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3", method="large")
       m1.addObject('TriangleCollisionModel', )
       m1.addObject('LineCollisionModel', )
       m1.addObject('PointCollisionModel', )
    ```

