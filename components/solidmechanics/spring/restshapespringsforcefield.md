# RestShapeSpringsForceField

Elastic springs generating forces on degrees of freedom between their current and rest shape position
Supports GPU-side computations using CUDA


__Templates__:

- `#!c++ Rigid3d`

__Target__: `Sofa.Component.SolidMechanics.Spring`

__namespace__: `#!c++ sofa::component::solidmechanics::spring`

__parents__: 

- `#!c++ ForceField`

__categories__: 

- ForceField

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
points from the external Mechancial State that define the rest shape springs
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

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|mechanicalStates|List of mechanical states to which this component is associated|
|mstate|MechanicalState used by this component|
|external_rest_shape|rest_shape can be defined by the position of an external Mechanical State|
|topology|Link to be set to the topology container in the component graph|



__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.Component.SolidMechanics.Spring`

__namespace__: `#!c++ sofa::component::solidmechanics::spring`

__parents__: 

- `#!c++ ForceField`

__categories__: 

- ForceField

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
points from the external Mechancial State that define the rest shape springs
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

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|mechanicalStates|List of mechanical states to which this component is associated|
|mstate|MechanicalState used by this component|
|external_rest_shape|rest_shape can be defined by the position of an external Mechanical State|
|topology|Link to be set to the topology container in the component graph|



__Templates__:

- `#!c++ Vec1d`

__Target__: `Sofa.Component.SolidMechanics.Spring`

__namespace__: `#!c++ sofa::component::solidmechanics::spring`

__parents__: 

- `#!c++ ForceField`

__categories__: 

- ForceField

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
points from the external Mechancial State that define the rest shape springs
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

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|mechanicalStates|List of mechanical states to which this component is associated|
|mstate|MechanicalState used by this component|
|external_rest_shape|rest_shape can be defined by the position of an external Mechanical State|
|topology|Link to be set to the topology container in the component graph|



## Examples

Component/SolidMechanics/FEM/RestShapeSpringsForceField3.scn

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
                                        activeDirections="1 0 1 1 0 1"/>
            <UniformMass totalMass="0.01" />
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="2.0e-3", gravity="0 0 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags=" showCollisionModels showForceFields")
        root.addObject('DefaultAnimationLoop')

        Object1 = root.addChild('Object1')
        Object1.addObject('MechanicalObject', name="object1MO", template="Rigid3d", position="0 0 0 0 0 0 1", showObject="true")

        Object2 = root.addChild('Object2')
        Object2.addObject('EulerImplicitSolver', rayleighMass="0", rayleighStiffness="0")
        Object2.addObject('EigenSparseLU', name="LULinearSolver", template="CompressedRowSparseMatrixMat3x3d")
        Object2.addObject('MechanicalObject', name="object2MO", template="Rigid3d", position="0.5 0.5 0 0.2705980500730985 0.2705980500730985 0 0.9238795325112867", showObject="true")
        Object2.addObject('RestShapeSpringsForceField', stiffness="11", angularStiffness="12", external_rest_shape="@../Object1/object1MO", points="0", external_points="0", drawSpring="true", springColor="1 1 1 1", activeDirections="1 0 1 1 0 1")
        Object2.addObject('UniformMass', totalMass="0.01")
    ```

Component/SolidMechanics/Spring/RestShapeSpringsForceField2.scn

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
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01", gravity="0 0 0")
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
        root.addObject('FreeMotionAnimationLoop')
        root.addObject('GenericConstraintSolver', maxIt="1000", tolerance="1e-10", printLog="false")

        Object1 = root.addChild('Object1')
        Object1.addObject('MechanicalObject', name="ms", template="Rigid3", position="0 0 0 0 0 0 0 1", showObject="false")
        Object1.addObject('SphereCollisionModel', radius="0.01", color="0 1 0 1")

        Object2 = root.addChild('Object2')
        Object2.addObject('EulerImplicitSolver', rayleighMass="0", rayleighStiffness="0")
        Object2.addObject('EigenSparseLU', template="CompressedRowSparseMatrix", name="LULinearSolver")
        Object2.addObject('MechanicalObject', name="mstate", template="Rigid3", position="0.1 0 0  0  0 0 0 1")
        Object2.addObject('SphereCollisionModel', color="1 0 0 1", radius="0.01")
        Object2.addObject('RestShapeSpringsForceField', stiffness="11", angularStiffness="11", external_rest_shape="@../Object1/ms", points="0", external_points="0", drawSpring="true", springColor="1 1 1 1")
        Object2.addObject('UniformMass', totalMass="0.01")
        Object2.addObject('SphereCollisionModel', radius="0.0005", color="1 0 0  1")
        Object2.addObject('LinearSolverConstraintCorrection', linearSolver="@LULinearSolver")
    ```

Component/SolidMechanics/Spring/RestShapeSpringsForceField.scn

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
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01")
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
        root.addObject('DefaultAnimationLoop')

        Dragon = root.addChild('Dragon')
        Dragon.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
        Dragon.addObject('CGLinearSolver', iterations="30", tolerance="1e-5", threshold="1e-5")
        Dragon.addObject('SparseGridTopology', n="10 5 10", fileTopology="mesh/dragon.obj")
        Dragon.addObject('MechanicalObject', dx="-12.0")
        Dragon.addObject('UniformMass', vertexMass="1.0")
        Dragon.addObject('RestShapeSpringsForceField', name="Springs", stiffness="50")

        Visu = Dragon.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/dragon.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_2", color="0.5 1.0 0.5 1.0")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        TriangleSurf = Dragon.addChild('TriangleSurf')
        TriangleSurf.addObject('MeshOBJLoader', name="loader", filename="mesh/dragon.obj")
        TriangleSurf.addObject('MeshTopology', src="@loader")
        TriangleSurf.addObject('MechanicalObject', src="@loader")
        TriangleSurf.addObject('TriangleCollisionModel', group="1")
        TriangleSurf.addObject('LineCollisionModel', group="1")
        TriangleSurf.addObject('PointCollisionModel', group="1")
        TriangleSurf.addObject('BarycentricMapping', input="@..", output="@.")

        Dragon with Damping = root.addChild('Dragon with Damping')
        Dragon with Damping.addObject('EulerImplicitSolver')
        Dragon with Damping.addObject('CGLinearSolver', iterations="30", tolerance="1e-5", threshold="1e-5")
        Dragon with Damping.addObject('SparseGridTopology', n="10 5 10", fileTopology="mesh/dragon.obj")
        Dragon with Damping.addObject('MechanicalObject', dx="12.0")
        Dragon with Damping.addObject('UniformMass', vertexMass="1.0")
        Dragon with Damping.addObject('RestShapeSpringsForceField', name="Springs", stiffness="50")

        Visu = Dragon with Damping.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/dragon.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="1.0 0.5 0.5 1.0")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        TriangleSurf = Dragon with Damping.addChild('TriangleSurf')
        TriangleSurf.addObject('MeshOBJLoader', name="loader", filename="mesh/dragon.obj")
        TriangleSurf.addObject('MeshTopology', src="@loader")
        TriangleSurf.addObject('MechanicalObject', src="@loader")
        TriangleSurf.addObject('TriangleCollisionModel', group="1")
        TriangleSurf.addObject('LineCollisionModel', group="1")
        TriangleSurf.addObject('PointCollisionModel', group="1")
        TriangleSurf.addObject('BarycentricMapping', input="@..", output="@.")

        CUBE = root.addChild('CUBE')
        CUBE.addObject('EulerImplicitSolver')
        CUBE.addObject('CGLinearSolver', iterations="30", tolerance="1e-5", threshold="1e-5")
        CUBE.addObject('MechanicalObject', template="Rigid3", dx="-12.0", dy="-20", rx="10")
        CUBE.addObject('UniformMass', totalMass="1.0")
        CUBE.addObject('RestShapeSpringsForceField', name="Springs", stiffness="50", angularStiffness="50")

        Visu = CUBE.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/smCube27.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_3", color="0.5 1.0 0.5 1.0")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        Surf2 = CUBE.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/smCube27.obj", triangulate="true")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader")
        Surf2.addObject('TriangleCollisionModel', group="1")
        Surf2.addObject('LineCollisionModel', group="1")
        Surf2.addObject('PointCollisionModel', group="1")
        Surf2.addObject('RigidMapping', input="@..", output="@.")

        CUBE with Damping = root.addChild('CUBE with Damping')
        CUBE with Damping.addObject('EulerImplicitSolver')
        CUBE with Damping.addObject('CGLinearSolver', iterations="30", tolerance="1e-5", threshold="1e-5")
        CUBE with Damping.addObject('MechanicalObject', template="Rigid3", dx="12.0", dy="-20", rx="10")
        CUBE with Damping.addObject('UniformMass', totalMass="1.0")
        CUBE with Damping.addObject('RestShapeSpringsForceField', name="Springs", stiffness="50", angularStiffness="50")

        Visu = CUBE with Damping.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/smCube27.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="1.0 0.5 0.5 1.0")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        Surf2 = CUBE with Damping.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/smCube27.obj", triangulate="true")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader")
        Surf2.addObject('TriangleCollisionModel', group="1")
        Surf2.addObject('LineCollisionModel', group="1")
        Surf2.addObject('PointCollisionModel', group="1")
        Surf2.addObject('RigidMapping', input="@..", output="@.")
    ```

