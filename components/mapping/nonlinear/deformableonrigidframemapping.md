<!-- generate_doc -->
# DeformableOnRigidFrameMapping

Set the positions and velocities of points attached to a rigid parent


## Vec3d,Rigid3d,Vec3d

Templates:

- Vec3d,Rigid3d,Vec3d

__Target__: Sofa.Component.Mapping.Linear

__namespace__: sofa::component::mapping::linear

__parents__:

- CRTPLinearMapping

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
		<td>mapForces</td>
		<td>
Are forces mapped ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapConstraints</td>
		<td>
Are constraints mapped ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapMasses</td>
		<td>
Are masses mapped ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapMatrices</td>
		<td>
Are matrix explicit mapped?
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>applyRestPosition</td>
		<td>
set to true to apply this mapping to restPosition at init
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>index</td>
		<td>
input DOF index
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>indexFromEnd</td>
		<td>
input DOF index starts from the end of input DOFs vector
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>repartition</td>
		<td>
number of dest dofs per entry dof
		</td>
		<td></td>
	</tr>
	<tr>
		<td>globalToLocalCoords</td>
		<td>
are the output DOFs initially expressed in global coordinates
		</td>
		<td></td>
	</tr>
	<tr>
		<td>rootAngularForceScaleFactor</td>
		<td>
Scale factor applied on the angular force accumulated on the rigid model
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>rootLinearForceScaleFactor</td>
		<td>
Scale factor applied on the linear force accumulated on the rigid model
		</td>
		<td>1</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|input1|Input Object(s) (1st Data type)|State&lt;Vec3d&gt;|
|input2|Input Object(s) (2st Data type)|State&lt;Rigid3d&gt;|
|output|Output Object(s)|State&lt;Vec3d&gt;|

## Examples 

DeformableOnRigidFrameMapping.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <!-- Mechanical DeformableOnRigidFrameMapping Example -->
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [NewProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping DeformableOnRigidFrameMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [PlaneForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [SparseGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <VisualStyle displayFlags="showBehavior showVisual" />
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <NewProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <DefaultAnimationLoop/>
        
        <Node name="ChainRigid">
            <Node name="TorusFixed">
                <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <MeshOBJLoader name="meshLoader_0" filename="mesh/torus2.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_0" color="gray" />
            </Node>
            <!-- 		<Node name="TorusRigid"> -->
            <Node name="Torus">
                <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver iterations="50" threshold="1e-15" tolerance="1e-15" verbose="0" />
                <MechanicalObject name="rigidframe" template="Rigid3" position="1 2 0 0 0 0.7 0.7" />
                <UniformMass filename="BehaviorModels/torus.rigid" />
                <!--<FixedProjectiveConstraint /> -->
                <!-- 	</Node> -->
                <Node name="TorusDeformLocal">
                    <SparseGridTopology filename="mesh/torus_for_collision.obj" n="7 2 4" />
                    <MechanicalObject />
                    <TetrahedronFEMForceField youngModulus="125" poissonRatio="0.45" />
                    <BoxConstraint box="-1 -1 -1 1 1 1" />
                    <Node name="DeformableMappedModel">
                        <SparseGridTopology filename="mesh/torus_for_collision.obj" n="7 2 4" />
                        <MechanicalObject name="deformedMO" />
                        <DeformableOnRigidFrameMapping input1="@.." input2="@../../rigidframe" output="@deformedMO" printLog="0" />
                        <Node name="TorusCollisLocal">
                            <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                            <MeshTopology src="@loader" />
                            <MechanicalObject src="@loader" />
                            <TriangleCollisionModel group="2" />
                            <BarycentricMapping />
                            <PlaneForceField name="Floor" normal="0 1 0" d="-4" stiffness="100" damping="1" />
                        </Node>
                        <Node name="Visu">
                            <MeshOBJLoader name="meshLoader_1" filename="mesh/torus.obj" handleSeams="1" />
                            <OglModel name="Visual" src="@meshLoader_1" color="gray" />
                            <BarycentricMapping input="@.." output="@Visual" />
                        </Node>
                    </Node>
                </Node>
            </Node>
        </Node>
        <!---->
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="showBehavior showVisual")
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('NewProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")
       root.addObject('DefaultAnimationLoop', )

       chain_rigid = root.addChild('ChainRigid')

       torus_fixed = ChainRigid.addChild('TorusFixed')

       torus_fixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       torus_fixed.addObject('MeshTopology', src="@loader")
       torus_fixed.addObject('MechanicalObject', src="@loader")
       torus_fixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus2.obj", handleSeams="1")
       torus_fixed.addObject('OglModel', name="Visual", src="@meshLoader_0", color="gray")

       torus = ChainRigid.addChild('Torus')

       torus.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
       torus.addObject('CGLinearSolver', iterations="50", threshold="1e-15", tolerance="1e-15", verbose="0")
       torus.addObject('MechanicalObject', name="rigidframe", template="Rigid3", position="1 2 0 0 0 0.7 0.7")
       torus.addObject('UniformMass', filename="BehaviorModels/torus.rigid")

       torus_deform_local = Torus.addChild('TorusDeformLocal')

       torus_deform_local.addObject('SparseGridTopology', filename="mesh/torus_for_collision.obj", n="7 2 4")
       torus_deform_local.addObject('MechanicalObject', )
       torus_deform_local.addObject('TetrahedronFEMForceField', youngModulus="125", poissonRatio="0.45")
       torus_deform_local.addObject('BoxConstraint', box="-1 -1 -1 1 1 1")

       deformable_mapped_model = TorusDeformLocal.addChild('DeformableMappedModel')

       deformable_mapped_model.addObject('SparseGridTopology', filename="mesh/torus_for_collision.obj", n="7 2 4")
       deformable_mapped_model.addObject('MechanicalObject', name="deformedMO")
       deformable_mapped_model.addObject('DeformableOnRigidFrameMapping', input1="@..", input2="@../../rigidframe", output="@deformedMO", printLog="0")

       torus_collis_local = DeformableMappedModel.addChild('TorusCollisLocal')

       torus_collis_local.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       torus_collis_local.addObject('MeshTopology', src="@loader")
       torus_collis_local.addObject('MechanicalObject', src="@loader")
       torus_collis_local.addObject('TriangleCollisionModel', group="2")
       torus_collis_local.addObject('BarycentricMapping', )
       torus_collis_local.addObject('PlaneForceField', name="Floor", normal="0 1 0", d="-4", stiffness="100", damping="1")

       visu = DeformableMappedModel.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="gray")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")
    ```

DeformableOnRigidFrameMappingConstraints.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.AnimationLoop"/> <!-- Needed to use components [FreeMotionAnimationLoop] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [LocalMinDistance] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [PrecomputedConstraintCorrection UncoupledConstraintCorrection] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Solver"/> <!-- Needed to use components [LCPConstraintSolver] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping DeformableOnRigidFrameMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [SparseGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <VisualStyle displayFlags="showBehavior" />
        <FreeMotionAnimationLoop />
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <LocalMinDistance name="Proximity" alarmDistance="0.3" contactDistance="0.1" />
        <CollisionResponse name="Response" response="FrictionContactConstraint" />
        <LCPConstraintSolver tolerance="0.001" maxIt="1000"/>
        <FreeMotionAnimationLoop/>
    
        <Node name="ChainRigid">
            <Node name="TorusFixed">
                <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <LineCollisionModel simulated="0" moving="0" />
                <PointCollisionModel simulated="0" moving="0" />
                <MeshOBJLoader name="meshLoader_1" filename="mesh/torus2.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_1" color="gray" />
            </Node>
            <Node name="TorusRigid">
                <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver iterations="50" threshold="1e-15" tolerance="1e-15" />
                <MechanicalObject name="rigidframe" template="Rigid3" position="1 2 0 0 0 0.7 0.7" />
                <UniformMass filename="BehaviorModels/torus.rigid" />
                <UncoupledConstraintCorrection />
            </Node>
            <Node name="TorusDeformLocal">
                <EulerImplicitSolver />
                <CGLinearSolver iterations="50" threshold="1e-15" tolerance="1e-15" />
                <SparseGridTopology filename="mesh/torus_for_collision.obj" n="7 2 4" />
                <MechanicalObject />
                <TetrahedronFEMForceField youngModulus="1e4" poissonRatio="0.45"/>
                <BoxConstraint box="-1 -1 -1 1 1 1" />
                <PrecomputedConstraintCorrection recompute="true" />
                <Node name="DeformableMappedModel">
                    <SparseGridTopology filename="mesh/torus_for_collision.obj" n="7 2 4" />
                    <MechanicalObject name="deformedMO" />
                    <DeformableOnRigidFrameMapping input1="@.." input2="@../../TorusRigid/rigidframe" output="@deformedMO" printLog="0" />
                    <Node name="TorusCollisLocal">
                        <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                        <MeshTopology src="@loader" />
                        <MechanicalObject src="@loader" />
                        <TriangleCollisionModel group="2" />
                        <LineCollisionModel group="2" />
                        <PointCollisionModel group="2" />
                        <BarycentricMapping />
                    </Node>
                    <Node name="Visu">
                        <MeshOBJLoader name="meshLoader_0" filename="mesh/torus.obj" handleSeams="1" />
                        <OglModel name="Visual" src="@meshLoader_0" color="gray" />
                        <BarycentricMapping input="@.." output="@Visual" />
                    </Node>
                </Node>
            </Node>
        </Node>
        <!---->
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02")

       root.addObject('RequiredPlugin', name="Sofa.Component.AnimationLoop")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Solver")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="showBehavior")
       root.addObject('FreeMotionAnimationLoop', )
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('LocalMinDistance', name="Proximity", alarmDistance="0.3", contactDistance="0.1")
       root.addObject('CollisionResponse', name="Response", response="FrictionContactConstraint")
       root.addObject('LCPConstraintSolver', tolerance="0.001", maxIt="1000")
       root.addObject('FreeMotionAnimationLoop', )

       chain_rigid = root.addChild('ChainRigid')

       torus_fixed = ChainRigid.addChild('TorusFixed')

       torus_fixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       torus_fixed.addObject('MeshTopology', src="@loader")
       torus_fixed.addObject('MechanicalObject', src="@loader")
       torus_fixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('LineCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('PointCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/torus2.obj", handleSeams="1")
       torus_fixed.addObject('OglModel', name="Visual", src="@meshLoader_1", color="gray")

       torus_rigid = ChainRigid.addChild('TorusRigid')

       torus_rigid.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
       torus_rigid.addObject('CGLinearSolver', iterations="50", threshold="1e-15", tolerance="1e-15")
       torus_rigid.addObject('MechanicalObject', name="rigidframe", template="Rigid3", position="1 2 0 0 0 0.7 0.7")
       torus_rigid.addObject('UniformMass', filename="BehaviorModels/torus.rigid")
       torus_rigid.addObject('UncoupledConstraintCorrection', )

       torus_deform_local = ChainRigid.addChild('TorusDeformLocal')

       torus_deform_local.addObject('EulerImplicitSolver', )
       torus_deform_local.addObject('CGLinearSolver', iterations="50", threshold="1e-15", tolerance="1e-15")
       torus_deform_local.addObject('SparseGridTopology', filename="mesh/torus_for_collision.obj", n="7 2 4")
       torus_deform_local.addObject('MechanicalObject', )
       torus_deform_local.addObject('TetrahedronFEMForceField', youngModulus="1e4", poissonRatio="0.45")
       torus_deform_local.addObject('BoxConstraint', box="-1 -1 -1 1 1 1")
       torus_deform_local.addObject('PrecomputedConstraintCorrection', recompute="true")

       deformable_mapped_model = TorusDeformLocal.addChild('DeformableMappedModel')

       deformable_mapped_model.addObject('SparseGridTopology', filename="mesh/torus_for_collision.obj", n="7 2 4")
       deformable_mapped_model.addObject('MechanicalObject', name="deformedMO")
       deformable_mapped_model.addObject('DeformableOnRigidFrameMapping', input1="@..", input2="@../../TorusRigid/rigidframe", output="@deformedMO", printLog="0")

       torus_collis_local = DeformableMappedModel.addChild('TorusCollisLocal')

       torus_collis_local.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       torus_collis_local.addObject('MeshTopology', src="@loader")
       torus_collis_local.addObject('MechanicalObject', src="@loader")
       torus_collis_local.addObject('TriangleCollisionModel', group="2")
       torus_collis_local.addObject('LineCollisionModel', group="2")
       torus_collis_local.addObject('PointCollisionModel', group="2")
       torus_collis_local.addObject('BarycentricMapping', )

       visu = DeformableMappedModel.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="gray")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")
    ```

