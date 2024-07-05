# RigidMapping

Set the positions and velocities of points attached to a rigid parent
Supports GPU-side computations using CUDA


__Templates__:

- `#!c++ Rigid2d,Vec2d`
- `#!c++ Rigid3d,Rigid3d`
- `#!c++ Rigid3d,Vec3d`

__Target__: `Sofa.Component.Mapping.NonLinear`

__namespace__: `#!c++ sofa::component::mapping::nonlinear`

__parents__: 

- `#!c++ Mapping`

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
		<td>geometricStiffness</td>
		<td>
Method used to compute the geometric stiffness:
-None: geometric stiffness is not computed
-Exact: the exact geometric stiffness is computed
-Stabilized: the exact geometric stiffness is approximated in order to improve stability
</td>
		<td>Stabilized</td>
	</tr>
	<tr>
		<td>initialPoints</td>
		<td>
Local Coordinates of the points
</td>
		<td></td>
	</tr>
	<tr>
		<td>index</td>
		<td>
input DOF index
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>filename</td>
		<td>
Xsp file where rigid mapping information can be loaded from.
</td>
		<td></td>
	</tr>
	<tr>
		<td>useX0</td>
		<td>
Use x0 instead of local copy of initial positions (to support topo changes)
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
		<td>rigidIndexPerPoint</td>
		<td>
For each mapped point, the index of the Rigid it is mapped from
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

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|input|Input object to map|
|output|Output object to map|



## Examples

Component/Mapping/NonLinear/RigidMapping.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [NewProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
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
                <TriangleCollisionModel contactStiffness="1000" simulated="0" moving="0" />
                <MeshOBJLoader name="meshLoader_3" filename="mesh/torus2.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_3" color="gray" texturename="textures/brushed_metal.bmp" />
            </Node>
            <Node name="TorusRigid1">
                <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver iterations="25" threshold="0.000000000001" tolerance="0.000001" />
                <MechanicalObject template="Rigid3" dx="2.5" />
                <UniformMass filename="BehaviorModels/torus.rigid" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_2" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_2" color="gray" texturename="textures/brushed_metal.bmp" />
                    <RigidMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <RigidMapping />
                </Node>
            </Node>
            <Node name="TorusRigid2">
                <EulerImplicitSolver />
                <CGLinearSolver iterations="25" threshold="0.000000000001" tolerance="0.000001" />
                <MechanicalObject template="Rigid3" dx="5" />
                <UniformMass />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_4" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_4" color="gray" texturename="textures/brushed_metal.bmp" />
                    <RigidMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <RigidMapping />
                </Node>
            </Node>
            <Node name="TorusRigid3">
                <EulerImplicitSolver />
                <CGLinearSolver iterations="25" threshold="0.000000000001" tolerance="0.000001" />
                <MechanicalObject template="Rigid3" dx="7.5" />
                <UniformMass />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_0" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_0" color="gray" texturename="textures/brushed_metal.bmp" />
                    <RigidMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <RigidMapping />
                </Node>
            </Node>
            <Node name="TorusRigid4">
                <EulerImplicitSolver />
                <CGLinearSolver iterations="25" threshold="0.000000000001" tolerance="0.000001" />
                <MechanicalObject template="Rigid3" dx="10" />
                <UniformMass />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_1" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_1" color="gray" texturename="textures/brushed_metal.bmp" />
                    <RigidMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <RigidMapping />
                </Node>
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('NewProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
        root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")
        root.addObject('DefaultAnimationLoop')

        ChainRigid = root.addChild('ChainRigid')

        TorusFixed = ChainRigid.addChild('TorusFixed')
        TorusFixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        TorusFixed.addObject('MeshTopology', src="@loader")
        TorusFixed.addObject('MechanicalObject', src="@loader")
        TorusFixed.addObject('TriangleCollisionModel', contactStiffness="1000", simulated="0", moving="0")
        TorusFixed.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/torus2.obj", handleSeams="1")
        TorusFixed.addObject('OglModel', name="Visual", src="@meshLoader_3", color="gray", texturename="textures/brushed_metal.bmp")

        TorusRigid1 = ChainRigid.addChild('TorusRigid1')
        TorusRigid1.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
        TorusRigid1.addObject('CGLinearSolver', iterations="25", threshold="0.000000000001", tolerance="0.000001")
        TorusRigid1.addObject('MechanicalObject', template="Rigid3", dx="2.5")
        TorusRigid1.addObject('UniformMass', filename="BehaviorModels/torus.rigid")

        Visu = TorusRigid1.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_2", color="gray", texturename="textures/brushed_metal.bmp")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        Surf2 = TorusRigid1.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('RigidMapping')

        TorusRigid2 = ChainRigid.addChild('TorusRigid2')
        TorusRigid2.addObject('EulerImplicitSolver')
        TorusRigid2.addObject('CGLinearSolver', iterations="25", threshold="0.000000000001", tolerance="0.000001")
        TorusRigid2.addObject('MechanicalObject', template="Rigid3", dx="5")
        TorusRigid2.addObject('UniformMass')

        Visu = TorusRigid2.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_4", filename="mesh/torus2.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_4", color="gray", texturename="textures/brushed_metal.bmp")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        Surf2 = TorusRigid2.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('RigidMapping')

        TorusRigid3 = ChainRigid.addChild('TorusRigid3')
        TorusRigid3.addObject('EulerImplicitSolver')
        TorusRigid3.addObject('CGLinearSolver', iterations="25", threshold="0.000000000001", tolerance="0.000001")
        TorusRigid3.addObject('MechanicalObject', template="Rigid3", dx="7.5")
        TorusRigid3.addObject('UniformMass')

        Visu = TorusRigid3.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="gray", texturename="textures/brushed_metal.bmp")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        Surf2 = TorusRigid3.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('RigidMapping')

        TorusRigid4 = ChainRigid.addChild('TorusRigid4')
        TorusRigid4.addObject('EulerImplicitSolver')
        TorusRigid4.addObject('CGLinearSolver', iterations="25", threshold="0.000000000001", tolerance="0.000001")
        TorusRigid4.addObject('MechanicalObject', template="Rigid3", dx="10")
        TorusRigid4.addObject('UniformMass')

        Visu = TorusRigid4.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/torus2.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="gray", texturename="textures/brushed_metal.bmp")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        Surf2 = TorusRigid4.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('RigidMapping')
    ```

Component/Mapping/NonLinear/RigidMapping2d-basic.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="Root" gravity="0 0 0" time="0" animate="0" bbox="-1 -1 -1 1 1 1">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [PartialFixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [ConstantForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [StaticSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <VisualStyle displayFlags="showBehaviorModels showMapping" />
        <DefaultAnimationLoop/>
    
        <Node name="parent node with independent DOFs">
            <!-- 		<EulerImplicitSolver name="ODE solver" printLog="0"  verbose="0" rayleighStiffness="0.0" rayleighMass="0"/> -->
            <StaticSolver name="ODE solver" printLog="0" />
            <CGLinearSolver template="GraphScattered" name="linear solver used by implicit ODE solvers" printLog="0" iterations="25" tolerance="1e-5" threshold="1e-5"/>
            <MechanicalObject template="Rigid2" />
            <PartialFixedProjectiveConstraint fixedDirections="1 1 0" />
            <UniformMass template="Rigid2" name="mass" />
            <Node name="child node with DOFs mapped from the parent">
                <MechanicalObject template="Vec2" name="endpoint coordinates" position="1 0 "  />
                <RigidMapping template="" name="angle-coord mapping" input="@.." output="@." index="0" />
                <ConstantForceField forces="1 -1" indices="0" />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        Root = rootNode.addChild('Root', gravity="0 0 0", time="0", animate="0", bbox="-1 -1 -1 1 1 1")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        Root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        Root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
        Root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        Root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        Root.addObject('VisualStyle', displayFlags="showBehaviorModels showMapping")
        Root.addObject('DefaultAnimationLoop')

        parent node with independent DOFs = Root.addChild('parent node with independent DOFs')
        parent node with independent DOFs.addObject('StaticSolver', name="ODE solver", printLog="0")
        parent node with independent DOFs.addObject('CGLinearSolver', template="GraphScattered", name="linear solver used by implicit ODE solvers", printLog="0", iterations="25", tolerance="1e-5", threshold="1e-5")
        parent node with independent DOFs.addObject('MechanicalObject', template="Rigid2")
        parent node with independent DOFs.addObject('PartialFixedProjectiveConstraint', fixedDirections="1 1 0")
        parent node with independent DOFs.addObject('UniformMass', template="Rigid2", name="mass")

        child node with DOFs mapped from the parent = parent node with independent DOFs.addChild('child node with DOFs mapped from the parent')
        child node with DOFs mapped from the parent.addObject('MechanicalObject', template="Vec2", name="endpoint coordinates", position="1 0 ")
        child node with DOFs mapped from the parent.addObject('RigidMapping', template="", name="angle-coord mapping", input="@..", output="@.", index="0")
        child node with DOFs mapped from the parent.addObject('ConstantForceField', forces="1 -1", indices="0")
    ```

Component/Mapping/NonLinear/RigidMapping-basic.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="Root" gravity="0 0 0" time="0" animate="0" bbox="-1 -1 -1 1 1 1">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [PartialFixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [ConstantForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [StaticSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <VisualStyle displayFlags="showBehaviorModels showMapping" />
        <DefaultAnimationLoop/>
    
        <Node name="parent node with independent DOFs">
            <StaticSolver name="ODE solver" printLog="0" />
            <CGLinearSolver template="GraphScattered" name="linear solver used by implicit ODE solvers" printLog="0" iterations="25" tolerance="1e-5" threshold="1e-5"/>
            <MechanicalObject template="Rigid3" />
            <PartialFixedProjectiveConstraint fixedDirections="1 1 1 0 0 0" />
            <UniformMass template="Rigid3" name="mass" />
            <Node name="child node with DOFs mapped from the parent">
                <MechanicalObject template="Vec3" name="endpoint coordinates" position="1 -0.0 0"  />
                <RigidMapping name="angle-coord mapping" input="@.." output="@." index="0" />
                <ConstantForceField forces="1 -1 0" indices="0" />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        Root = rootNode.addChild('Root', gravity="0 0 0", time="0", animate="0", bbox="-1 -1 -1 1 1 1")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        Root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        Root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
        Root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        Root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        Root.addObject('VisualStyle', displayFlags="showBehaviorModels showMapping")
        Root.addObject('DefaultAnimationLoop')

        parent node with independent DOFs = Root.addChild('parent node with independent DOFs')
        parent node with independent DOFs.addObject('StaticSolver', name="ODE solver", printLog="0")
        parent node with independent DOFs.addObject('CGLinearSolver', template="GraphScattered", name="linear solver used by implicit ODE solvers", printLog="0", iterations="25", tolerance="1e-5", threshold="1e-5")
        parent node with independent DOFs.addObject('MechanicalObject', template="Rigid3")
        parent node with independent DOFs.addObject('PartialFixedProjectiveConstraint', fixedDirections="1 1 1 0 0 0")
        parent node with independent DOFs.addObject('UniformMass', template="Rigid3", name="mass")

        child node with DOFs mapped from the parent = parent node with independent DOFs.addChild('child node with DOFs mapped from the parent')
        child node with DOFs mapped from the parent.addObject('MechanicalObject', template="Vec3", name="endpoint coordinates", position="1 -0.0 0")
        child node with DOFs mapped from the parent.addObject('RigidMapping', name="angle-coord mapping", input="@..", output="@.", index="0")
        child node with DOFs mapped from the parent.addObject('ConstantForceField', forces="1 -1 0", indices="0")
    ```

