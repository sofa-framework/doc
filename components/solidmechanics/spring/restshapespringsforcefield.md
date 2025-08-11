<!-- generate_doc -->
# RestShapeSpringsForceField

Elastic springs generating forces on degrees of freedom between their current and rest shape position.


## Rigid3d

Templates:

- Rigid3d

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
		<td>points</td>
		<td>
points controlled by the rest shape springs
		</td>
		<td></td>
	</tr>
	<tr>
		<td>stiffness</td>
		<td>
stiffness values between the actual position and the rest shape position
		</td>
		<td></td>
	</tr>
	<tr>
		<td>angularStiffness</td>
		<td>
angularStiffness assigned when controlling the rotation of the points
		</td>
		<td></td>
	</tr>
	<tr>
		<td>pivot_points</td>
		<td>
global pivot points used when translations instead of the rigid mass centers
		</td>
		<td></td>
	</tr>
	<tr>
		<td>external_points</td>
		<td>
points from the external Mechanical State that define the rest shape springs
		</td>
		<td></td>
	</tr>
	<tr>
		<td>recompute_indices</td>
		<td>
Recompute indices (should be false for BBOX)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>springColor</td>
		<td>
spring color. (default=[0.0,1.0,0.0,1.0])
		</td>
		<td>0 1 0 1</td>
	</tr>
	<tr>
		<td>activeDirections</td>
		<td>
Directions in which the spring is active (default=[1,1,1,1,1,1,1])
		</td>
		<td>1 1 1 1 1 1 1</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawSpring</td>
		<td>
draw Spring
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Rigid3d&gt;|
|external_rest_shape|rest_shape can be defined by the position of an external Mechanical State|MechanicalState&lt;Rigid3d&gt;|
|topology|Link to be set to the topology container in the component graph|BaseMeshTopology|

<!-- generate_doc -->
## Vec1d

Templates:

- Vec1d

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
		<td>points</td>
		<td>
points controlled by the rest shape springs
		</td>
		<td></td>
	</tr>
	<tr>
		<td>stiffness</td>
		<td>
stiffness values between the actual position and the rest shape position
		</td>
		<td></td>
	</tr>
	<tr>
		<td>angularStiffness</td>
		<td>
angularStiffness assigned when controlling the rotation of the points
		</td>
		<td></td>
	</tr>
	<tr>
		<td>pivot_points</td>
		<td>
global pivot points used when translations instead of the rigid mass centers
		</td>
		<td></td>
	</tr>
	<tr>
		<td>external_points</td>
		<td>
points from the external Mechanical State that define the rest shape springs
		</td>
		<td></td>
	</tr>
	<tr>
		<td>recompute_indices</td>
		<td>
Recompute indices (should be false for BBOX)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>springColor</td>
		<td>
spring color. (default=[0.0,1.0,0.0,1.0])
		</td>
		<td>0 1 0 1</td>
	</tr>
	<tr>
		<td>activeDirections</td>
		<td>
Directions in which the spring is active (default=[1])
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawSpring</td>
		<td>
draw Spring
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec1d&gt;|
|external_rest_shape|rest_shape can be defined by the position of an external Mechanical State|MechanicalState&lt;Vec1d&gt;|
|topology|Link to be set to the topology container in the component graph|BaseMeshTopology|

<!-- generate_doc -->
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
		<td>points</td>
		<td>
points controlled by the rest shape springs
		</td>
		<td></td>
	</tr>
	<tr>
		<td>stiffness</td>
		<td>
stiffness values between the actual position and the rest shape position
		</td>
		<td></td>
	</tr>
	<tr>
		<td>angularStiffness</td>
		<td>
angularStiffness assigned when controlling the rotation of the points
		</td>
		<td></td>
	</tr>
	<tr>
		<td>pivot_points</td>
		<td>
global pivot points used when translations instead of the rigid mass centers
		</td>
		<td></td>
	</tr>
	<tr>
		<td>external_points</td>
		<td>
points from the external Mechanical State that define the rest shape springs
		</td>
		<td></td>
	</tr>
	<tr>
		<td>recompute_indices</td>
		<td>
Recompute indices (should be false for BBOX)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>springColor</td>
		<td>
spring color. (default=[0.0,1.0,0.0,1.0])
		</td>
		<td>0 1 0 1</td>
	</tr>
	<tr>
		<td>activeDirections</td>
		<td>
Directions in which the spring is active (default=[1,1,1])
		</td>
		<td>1 1 1</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawSpring</td>
		<td>
draw Spring
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
|external_rest_shape|rest_shape can be defined by the position of an external Mechanical State|MechanicalState&lt;Vec3d&gt;|
|topology|Link to be set to the topology container in the component graph|BaseMeshTopology|

## Examples 

RestShapeSpringsForceField2.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    
    <Node name="root" dt="0.01" gravity="0 0 0" >
        <RequiredPlugin name="Sofa.Component.AnimationLoop"/> <!-- Needed to use components [FreeMotionAnimationLoop] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [SphereCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [LinearSolverConstraintCorrection] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Solver"/> <!-- Needed to use components [GenericConstraintSolver] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [EigenSparseLU] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [RestShapeSpringsForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <VisualStyle displayFlags=" showCollisionModels showForceFields" />
    
        <FreeMotionAnimationLoop />
        <GenericConstraintSolver maxIt="1000" tolerance="1e-10" printLog="false" />
    
        <Node name="Object1">
            <MechanicalObject name="ms" template="Rigid3" position="0 0 0 0 0 0 0 1" showObject="false"/>
            <SphereCollisionModel radius="0.01" color="0 1 0 1" />
        </Node>
    
        <Node name="Object2">
            <EulerImplicitSolver rayleighMass="0" rayleighStiffness="0"/>
            <EigenSparseLU template="CompressedRowSparseMatrix" name="LULinearSolver"/>
            <MechanicalObject name="mstate" template="Rigid3" position="0.1 0 0  0  0 0 0 1" />
            <SphereCollisionModel color="1 0 0 1" radius="0.01" />
            <RestShapeSpringsForceField stiffness="11" angularStiffness="11" external_rest_shape="@../Object1/ms" points="0" external_points="0" drawSpring="true" springColor="1 1 1 1"/>
            <UniformMass totalMass="0.01" />
            <SphereCollisionModel radius="0.0005" color="1 0 0  1" />
    
            <LinearSolverConstraintCorrection linearSolver="@LULinearSolver"/>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 0 0")

       root.addObject('RequiredPlugin', name="Sofa.Component.AnimationLoop")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Solver")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('VisualStyle', displayFlags=" showCollisionModels showForceFields")
       root.addObject('FreeMotionAnimationLoop', )
       root.addObject('GenericConstraintSolver', maxIt="1000", tolerance="1e-10", printLog="false")

       object1 = root.addChild('Object1')

       object1.addObject('MechanicalObject', name="ms", template="Rigid3", position="0 0 0 0 0 0 0 1", showObject="false")
       object1.addObject('SphereCollisionModel', radius="0.01", color="0 1 0 1")

       object2 = root.addChild('Object2')

       object2.addObject('EulerImplicitSolver', rayleighMass="0", rayleighStiffness="0")
       object2.addObject('EigenSparseLU', template="CompressedRowSparseMatrix", name="LULinearSolver")
       object2.addObject('MechanicalObject', name="mstate", template="Rigid3", position="0.1 0 0  0  0 0 0 1")
       object2.addObject('SphereCollisionModel', color="1 0 0 1", radius="0.01")
       object2.addObject('RestShapeSpringsForceField', stiffness="11", angularStiffness="11", external_rest_shape="@../Object1/ms", points="0", external_points="0", drawSpring="true", springColor="1 1 1 1")
       object2.addObject('UniformMass', totalMass="0.01")
       object2.addObject('SphereCollisionModel', radius="0.0005", color="1 0 0  1")
       object2.addObject('LinearSolverConstraintCorrection', linearSolver="@LULinearSolver")
    ```

RestShapeSpringsForceField.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.01">
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [RestShapeSpringsForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [SparseGridTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        
        <DefaultAnimationLoop/>
        <Node name="Dragon">
            <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="30" tolerance="1e-5" threshold="1e-5"/>
            <SparseGridTopology n="10 5 10" fileTopology="mesh/dragon.obj" />
            <MechanicalObject dx="-12.0" />
            <UniformMass vertexMass="1.0" />
            <RestShapeSpringsForceField name="Springs" stiffness="50"/>
    		
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_2" filename="mesh/dragon.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_2" color="0.5 1.0 0.5 1.0" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
    		
            <Node name="TriangleSurf">
                <MeshOBJLoader name="loader" filename="mesh/dragon.obj" />
                <MeshTopology src="@loader"/>
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel group="1" />
                <LineCollisionModel group="1" />
                <PointCollisionModel group="1" />
                <BarycentricMapping input="@.." output="@." />
            </Node>
        </Node>
    	<Node name="Dragon with Damping">
            <EulerImplicitSolver />
            <CGLinearSolver iterations="30" tolerance="1e-5" threshold="1e-5"/>
            <SparseGridTopology n="10 5 10" fileTopology="mesh/dragon.obj" />
            <MechanicalObject dx="12.0" />
            <UniformMass vertexMass="1.0" />
            <RestShapeSpringsForceField name="Springs" stiffness="50"/>
    		
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_1" filename="mesh/dragon.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_1" color="1.0 0.5 0.5 1.0" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
    		
            <Node name="TriangleSurf">
                <MeshOBJLoader name="loader" filename="mesh/dragon.obj" />
                <MeshTopology src="@loader"/>
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel group="1" />
                <LineCollisionModel group="1" />
                <PointCollisionModel group="1" />
                <BarycentricMapping input="@.." output="@." />
            </Node>
        </Node>
    	<Node name="CUBE">
    		<EulerImplicitSolver />
            <CGLinearSolver iterations="30" tolerance="1e-5" threshold="1e-5"/>
    		<MechanicalObject template="Rigid3" dx="-12.0" dy="-20" rx="10" />
    		<UniformMass totalMass="1.0" />
    		<RestShapeSpringsForceField name="Springs" stiffness="50" angularStiffness="50"/>
    		<Node name="Visu">
    			<MeshOBJLoader name="meshLoader_3" filename="mesh/smCube27.obj" handleSeams="1" />
    			<OglModel name="Visual" src="@meshLoader_3" color="0.5 1.0 0.5 1.0" />
    			<RigidMapping input="@.." output="@Visual" />
    		</Node>
    		<Node name="Surf2">
    			<MeshOBJLoader name="loader" filename="mesh/smCube27.obj" triangulate="true" />
    			<MeshTopology src="@loader"/>
    			<MechanicalObject src="@loader"/>
    			<TriangleCollisionModel group="1"/>
    			<LineCollisionModel group="1"/>
    			<PointCollisionModel group="1"/>
    			<RigidMapping input="@.." output="@."/>
    		</Node>
    	</Node>
    	<Node name="CUBE with Damping">
    		<EulerImplicitSolver />
            <CGLinearSolver iterations="30" tolerance="1e-5" threshold="1e-5"/>
    		<MechanicalObject template="Rigid3" dx="12.0" dy="-20" rx="10" />
    		<UniformMass totalMass="1.0" />
    		<RestShapeSpringsForceField name="Springs" stiffness="50" angularStiffness="50" />
    		<Node name="Visu">
    			<MeshOBJLoader name="meshLoader_0" filename="mesh/smCube27.obj" handleSeams="1" />
    			<OglModel name="Visual" src="@meshLoader_0" color="1.0 0.5 0.5 1.0" />
    			<RigidMapping input="@.." output="@Visual" />
    		</Node>
    		<Node name="Surf2">
    			<MeshOBJLoader name="loader" filename="mesh/smCube27.obj" triangulate="true" />
    			<MeshTopology src="@loader"/>
    			<MechanicalObject src="@loader"/>
    			<TriangleCollisionModel group="1"/>
    			<LineCollisionModel group="1"/>
    			<PointCollisionModel group="1"/>
    			<RigidMapping input="@.." output="@."/>
    		</Node>
    	</Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('DefaultAnimationLoop', )

       dragon = root.addChild('Dragon')

       dragon.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
       dragon.addObject('CGLinearSolver', iterations="30", tolerance="1e-5", threshold="1e-5")
       dragon.addObject('SparseGridTopology', n="10 5 10", fileTopology="mesh/dragon.obj")
       dragon.addObject('MechanicalObject', dx="-12.0")
       dragon.addObject('UniformMass', vertexMass="1.0")
       dragon.addObject('RestShapeSpringsForceField', name="Springs", stiffness="50")

       visu = Dragon.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/dragon.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_2", color="0.5 1.0 0.5 1.0")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       triangle_surf = Dragon.addChild('TriangleSurf')

       triangle_surf.addObject('MeshOBJLoader', name="loader", filename="mesh/dragon.obj")
       triangle_surf.addObject('MeshTopology', src="@loader")
       triangle_surf.addObject('MechanicalObject', src="@loader")
       triangle_surf.addObject('TriangleCollisionModel', group="1")
       triangle_surf.addObject('LineCollisionModel', group="1")
       triangle_surf.addObject('PointCollisionModel', group="1")
       triangle_surf.addObject('BarycentricMapping', input="@..", output="@.")

       dragon_with__damping = root.addChild('Dragon with Damping')

       dragon_with__damping.addObject('EulerImplicitSolver', )
       dragon_with__damping.addObject('CGLinearSolver', iterations="30", tolerance="1e-5", threshold="1e-5")
       dragon_with__damping.addObject('SparseGridTopology', n="10 5 10", fileTopology="mesh/dragon.obj")
       dragon_with__damping.addObject('MechanicalObject', dx="12.0")
       dragon_with__damping.addObject('UniformMass', vertexMass="1.0")
       dragon_with__damping.addObject('RestShapeSpringsForceField', name="Springs", stiffness="50")

       visu = Dragon with Damping.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/dragon.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="1.0 0.5 0.5 1.0")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       triangle_surf = Dragon with Damping.addChild('TriangleSurf')

       triangle_surf.addObject('MeshOBJLoader', name="loader", filename="mesh/dragon.obj")
       triangle_surf.addObject('MeshTopology', src="@loader")
       triangle_surf.addObject('MechanicalObject', src="@loader")
       triangle_surf.addObject('TriangleCollisionModel', group="1")
       triangle_surf.addObject('LineCollisionModel', group="1")
       triangle_surf.addObject('PointCollisionModel', group="1")
       triangle_surf.addObject('BarycentricMapping', input="@..", output="@.")

       cube = root.addChild('CUBE')

       cube.addObject('EulerImplicitSolver', )
       cube.addObject('CGLinearSolver', iterations="30", tolerance="1e-5", threshold="1e-5")
       cube.addObject('MechanicalObject', template="Rigid3", dx="-12.0", dy="-20", rx="10")
       cube.addObject('UniformMass', totalMass="1.0")
       cube.addObject('RestShapeSpringsForceField', name="Springs", stiffness="50", angularStiffness="50")

       visu = CUBE.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/smCube27.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_3", color="0.5 1.0 0.5 1.0")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       surf2 = CUBE.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/smCube27.obj", triangulate="true")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader")
       surf2.addObject('TriangleCollisionModel', group="1")
       surf2.addObject('LineCollisionModel', group="1")
       surf2.addObject('PointCollisionModel', group="1")
       surf2.addObject('RigidMapping', input="@..", output="@.")

       cube_with__damping = root.addChild('CUBE with Damping')

       cube_with__damping.addObject('EulerImplicitSolver', )
       cube_with__damping.addObject('CGLinearSolver', iterations="30", tolerance="1e-5", threshold="1e-5")
       cube_with__damping.addObject('MechanicalObject', template="Rigid3", dx="12.0", dy="-20", rx="10")
       cube_with__damping.addObject('UniformMass', totalMass="1.0")
       cube_with__damping.addObject('RestShapeSpringsForceField', name="Springs", stiffness="50", angularStiffness="50")

       visu = CUBE with Damping.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/smCube27.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="1.0 0.5 0.5 1.0")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       surf2 = CUBE with Damping.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/smCube27.obj", triangulate="true")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader")
       surf2.addObject('TriangleCollisionModel', group="1")
       surf2.addObject('LineCollisionModel', group="1")
       surf2.addObject('PointCollisionModel', group="1")
       surf2.addObject('RigidMapping', input="@..", output="@.")
    ```

RestShapeSpringsForceField3.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    
    <Node name="root" dt="2.0e-3" gravity="0 0 0" >
        <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [EigenSparseLU] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [RestShapeSpringsForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <VisualStyle displayFlags=" showCollisionModels showForceFields" />
        <DefaultAnimationLoop/>
    
        <Node name="Object1">
            <MechanicalObject name="object1MO" template="Rigid3d" position="0 0 0 0 0 0 1" showObject="true"/>
        </Node>
    
        <Node name="Object2">
            <EulerImplicitSolver rayleighMass="0" rayleighStiffness="0"/>
            <EigenSparseLU name="LULinearSolver" template="CompressedRowSparseMatrixMat3x3d"/>
            <MechanicalObject name="object2MO" template="Rigid3d" position="0.5 0.5 0 0.2705980500730985 0.2705980500730985 0 0.9238795325112867" showObject="true"/>
            <RestShapeSpringsForceField stiffness="11" angularStiffness="12"
                                        external_rest_shape="@../Object1/object1MO"
                                        points="0" external_points="0"
                                        drawSpring="true" springColor="1 1 1 1"
                                        activeDirections="1 0 1 1 0 1 1"/>
            <UniformMass totalMass="0.01" />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="2.0e-3", gravity="0 0 0")

       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('VisualStyle', displayFlags=" showCollisionModels showForceFields")
       root.addObject('DefaultAnimationLoop', )

       object1 = root.addChild('Object1')

       object1.addObject('MechanicalObject', name="object1MO", template="Rigid3d", position="0 0 0 0 0 0 1", showObject="true")

       object2 = root.addChild('Object2')

       object2.addObject('EulerImplicitSolver', rayleighMass="0", rayleighStiffness="0")
       object2.addObject('EigenSparseLU', name="LULinearSolver", template="CompressedRowSparseMatrixMat3x3d")
       object2.addObject('MechanicalObject', name="object2MO", template="Rigid3d", position="0.5 0.5 0 0.2705980500730985 0.2705980500730985 0 0.9238795325112867", showObject="true")
       object2.addObject('RestShapeSpringsForceField', stiffness="11", angularStiffness="12", external_rest_shape="@../Object1/object1MO", points="0", external_points="0", drawSpring="true", springColor="1 1 1 1", activeDirections="1 0 1 1 0 1 1")
       object2.addObject('UniformMass', totalMass="0.01")
    ```

