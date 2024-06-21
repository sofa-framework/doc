# TriangleBendingSprings

Springs added to a traingular mesh to prevent bending
Supports GPU-side computations using CUDA


__Templates__:

- `#!c++ Vec2d`
- `#!c++ Vec3d`

__Target__: `Sofa.Component.SolidMechanics.Spring`

__namespace__: `#!c++ sofa::component::solidmechanics::spring`

__parents__: 

- `#!c++ StiffSpringForceField`

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
		<td>isCompliance</td>
		<td>
Consider the component as a compliance, else as a stiffness
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
		<td>stiffness</td>
		<td>
uniform stiffness for the all springs
</td>
		<td>100</td>
	</tr>
	<tr>
		<td>damping</td>
		<td>
uniform damping for the all springs
</td>
		<td>5</td>
	</tr>
	<tr>
		<td>spring</td>
		<td>
pairs of indices, stiffness, damping, rest length
</td>
		<td></td>
	</tr>
	<tr>
		<td>springsIndices1</td>
		<td>
List of indices in springs from the first mstate
</td>
		<td></td>
	</tr>
	<tr>
		<td>springsIndices2</td>
		<td>
List of indices in springs from the second mstate
</td>
		<td></td>
	</tr>
	<tr>
		<td>indices1</td>
		<td>
Indices of the source points on the first model
</td>
		<td></td>
	</tr>
	<tr>
		<td>indices2</td>
		<td>
Indices of the fixed points on the second model
</td>
		<td></td>
	</tr>
	<tr>
		<td>lengths</td>
		<td>
List of lengths to create the springs. Must have the same than indices1 & indices2, or if only one element, it will be applied to all springs. If empty, 0 will be applied everywhere
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showArrowSize</td>
		<td>
size of the axis
</td>
		<td>0.01</td>
	</tr>
	<tr>
		<td>drawMode</td>
		<td>
The way springs will be drawn:
- 0: Line
- 1:Cylinder
- 2: Arrow
</td>
		<td>0</td>
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
|object1|First object associated to this component|
|object2|Second object associated to this component|
|topology|link to the topology container|



## Examples

Component/SolidMechanics/Spring/TriangleBendingSprings.scn

=== "XML"

    ```xml
    <!-- Mechanical MassSpring Group Basic Example -->
    <Node name="root" gravity="0 0 1" dt="0.05">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangleFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [TriangleBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <VisualStyle displayFlags="showBehaviorModels showForceFields showCollisionModels showMappings showVisual" />
        <CollisionPipeline verbose="0" name="CollisionPipeline" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" name="collision response" />
        <DiscreteIntersection />
        <DefaultAnimationLoop/>
        
        <Node name="M1">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject />
            <UniformMass vertexMass="0.1" />
            <RegularGridTopology nx="3" ny="3" nz="1" xmin="10" xmax="19" ymin="0" ymax="9" zmin="4" zmax="5" />
            <FixedProjectiveConstraint indices="0 8" />
            <TriangleFEMForceField name="FEM1" youngModulus="5000" poissonRatio="0.3" method="large" />
            <TriangleBendingSprings name="FEM-Bend" stiffness="100" damping="0.1" />
            <TriangleCollisionModel />
            <Node name="Visu">
                <OglModel name="Visual" color="green" />
                <IdentityMapping input="@.." output="@Visual" />
            </Node>
        </Node>
        <Node name="M2">
            <EulerImplicitSolver name="cg_odesolver" printLog="false" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject />
            <UniformMass vertexMass="0.1" />
            <RegularGridTopology nx="4" ny="4" nz="1" xmin="20" xmax="29" ymin="0" ymax="9" zmin="8" zmax="9" />
            <FixedProjectiveConstraint indices="0 15" />
            <TriangleFEMForceField name="FEM2" youngModulus="5000" poissonRatio="0.3" method="large" />
            <TriangleBendingSprings name="FEM-Bend" stiffness="100" damping="0.1" />
            <TriangleCollisionModel />
            <Node name="Visu">
                <OglModel name="Visual" color="blue" />
                <IdentityMapping input="@.." output="@Visual" />
            </Node>
        </Node>
        <Node name="M3">
            <EulerImplicitSolver name="cg_odesolver" printLog="false" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject />
            <UniformMass vertexMass="0.1" />
            <RegularGridTopology nx="10" ny="10" nz="1" xmin="30" xmax="39" ymin="0" ymax="9" zmin="12" zmax="13" />
            <FixedProjectiveConstraint indices="0 9 99" />
            <TriangleFEMForceField name="FEM3" youngModulus="5000" poissonRatio="0.3" method="large" />
            <TriangleBendingSprings name="FEM-Bend" stiffness="100" damping="0.1" />
            <TriangleCollisionModel />
            <Node name="Visu">
                <OglModel name="Visual" color="yellow" />
                <IdentityMapping input="@.." output="@Visual" />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 0 1", dt="0.05")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields showCollisionModels showMappings showVisual")
        root.addObject('CollisionPipeline', verbose="0", name="CollisionPipeline")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField", name="collision response")
        root.addObject('DiscreteIntersection')
        root.addObject('DefaultAnimationLoop')

        M1 = root.addChild('M1')
        M1.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        M1.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        M1.addObject('MechanicalObject')
        M1.addObject('UniformMass', vertexMass="0.1")
        M1.addObject('RegularGridTopology', nx="3", ny="3", nz="1", xmin="10", xmax="19", ymin="0", ymax="9", zmin="4", zmax="5")
        M1.addObject('FixedProjectiveConstraint', indices="0 8")
        M1.addObject('TriangleFEMForceField', name="FEM1", youngModulus="5000", poissonRatio="0.3", method="large")
        M1.addObject('TriangleBendingSprings', name="FEM-Bend", stiffness="100", damping="0.1")
        M1.addObject('TriangleCollisionModel')

        Visu = M1.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="green")
        Visu.addObject('IdentityMapping', input="@..", output="@Visual")

        M2 = root.addChild('M2')
        M2.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        M2.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        M2.addObject('MechanicalObject')
        M2.addObject('UniformMass', vertexMass="0.1")
        M2.addObject('RegularGridTopology', nx="4", ny="4", nz="1", xmin="20", xmax="29", ymin="0", ymax="9", zmin="8", zmax="9")
        M2.addObject('FixedProjectiveConstraint', indices="0 15")
        M2.addObject('TriangleFEMForceField', name="FEM2", youngModulus="5000", poissonRatio="0.3", method="large")
        M2.addObject('TriangleBendingSprings', name="FEM-Bend", stiffness="100", damping="0.1")
        M2.addObject('TriangleCollisionModel')

        Visu = M2.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="blue")
        Visu.addObject('IdentityMapping', input="@..", output="@Visual")

        M3 = root.addChild('M3')
        M3.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        M3.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        M3.addObject('MechanicalObject')
        M3.addObject('UniformMass', vertexMass="0.1")
        M3.addObject('RegularGridTopology', nx="10", ny="10", nz="1", xmin="30", xmax="39", ymin="0", ymax="9", zmin="12", zmax="13")
        M3.addObject('FixedProjectiveConstraint', indices="0 9 99")
        M3.addObject('TriangleFEMForceField', name="FEM3", youngModulus="5000", poissonRatio="0.3", method="large")
        M3.addObject('TriangleBendingSprings', name="FEM-Bend", stiffness="100", damping="0.1")
        M3.addObject('TriangleCollisionModel')

        Visu = M3.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="yellow")
        Visu.addObject('IdentityMapping', input="@..", output="@Visual")
    ```

