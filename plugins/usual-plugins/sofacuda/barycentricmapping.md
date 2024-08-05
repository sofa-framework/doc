# BarycentricMapping

Mapping using barycentric coordinates of the child with respect to cells of its parent
Supports GPU-side computations using CUDA
Supports GPU-side computations using CUDA
Supports GPU-side computations using CUDA
Supports GPU-side computations using CUDA
Supports GPU-side computations using CUDA


__Templates__:

- `#!c++ CudaVec3f,CudaVec3f`
- `#!c++ CudaVec3f,CudaVec3f1`
- `#!c++ CudaVec3f,Rigid3d`
- `#!c++ CudaVec3f,Vec3d`
- `#!c++ CudaVec3f1,CudaVec3f`
- `#!c++ CudaVec3f1,CudaVec3f1`
- `#!c++ CudaVec3f1,Vec3d`
- `#!c++ Vec3d,CudaVec3f`
- `#!c++ Vec3d,CudaVec3f1`

__Target__: `SofaCUDA`

__namespace__: `#!c++ sofa::component::mapping::linear`

__parents__: 

- `#!c++ CRTPLinearMapping`

__categories__: 

- Mapping

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
		<td>useRestPosition</td>
		<td>
Use the rest position of the input and output models to initialize the mapping
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
|input|Input object to map|
|output|Output object to map|
|mapper|Internal mapper created depending on the type of topology|
|input_topology|Input topology container (usually the surrounding domain).|
|output_topology|Output topology container (usually the immersed domain).|



## Examples

Component/Mapping/Linear/BarycentricMapping.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [MeshSpringForceField RegularGridSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showMappings" />
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="Chain">
            <Node name="TorusFixed">
                <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <LineCollisionModel simulated="0" moving="0" />
                <PointCollisionModel simulated="0" moving="0" />
                <MeshOBJLoader name="meshLoader_19" filename="mesh/torus2.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_19" color="gray" />
            </Node>
            <Node name="TorusFEM">
                <EulerImplicitSolver rayleighStiffness="0.01"  rayleighMass="0.1" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="2.5" />
                <UniformMass vertexMass="0.1" />
                <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.3" computeGlobalMatrix="false" method="polar" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_3" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_3" color="red" dx="2.5" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="2.5" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusSpring">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MeshGmshLoader name="loader" filename="mesh/torus2_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="5" />
                <UniformMass totalMass="5" />
                <MeshSpringForceField name="Springs" tetrasStiffness="400" tetrasDamping="4" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_8" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_8" dx="5" color="green" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="5" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFFD">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MechanicalObject dx="7.5" />
                <UniformMass totalMass="5" />
                <RegularGridTopology nx="6" ny="2" nz="5" xmin="-2.5" xmax="2.5" ymin="-0.5" ymax="0.5" zmin="-2" zmax="2" />
                <RegularGridSpringForceField name="Springs" stiffness="200" damping="2" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_13" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_13" color="yellow" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusRigid">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MechanicalObject template="Rigid3" dx="10" />
                <UniformMass filename="BehaviorModels/torus2.rigid" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_17" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_17" color="gray" />
                    <RigidMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <RigidMapping />
                </Node>
            </Node>
        </Node>
        <Node name="ChainFEM">
            <Node name="TorusFixed">
                <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dz="6" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <LineCollisionModel simulated="0" moving="0" />
                <PointCollisionModel simulated="0" moving="0" />
                <MeshOBJLoader name="meshLoader_21" filename="mesh/torus2.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_21" color="gray" dz="6" />
            </Node>
            <Node name="TorusFEM1">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="2.5" dz="6" />
                <UniformMass totalMass="5" />
                <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.3" computeGlobalMatrix="false" method="polar" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_23" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_23" color="red" dx="2.5" dz="6" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="2.5" dz="6" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFEM2">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MeshGmshLoader name="loader" filename="mesh/torus2_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="5" dz="6" />
                <UniformMass totalMass="5" />
                <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.3" computeGlobalMatrix="false" method="polar" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_1" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_1" color="red" dx="5" dz="6" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="5" dz="6" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFEM3">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="7.5" dz="6" />
                <UniformMass totalMass="5" />
                <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.3" computeGlobalMatrix="false" method="polar" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_6" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_6" color="red" dx="7.5" dz="6" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="7.5" dz="6" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFEM4">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MeshGmshLoader name="loader" filename="mesh/torus2_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="10" dz="6" />
                <UniformMass totalMass="5" />
                <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.3" computeGlobalMatrix="false" method="polar" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_10" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_10" color="red" dx="10" dz="6" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="10" dz="6" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
        </Node>
        <Node name="ChainSpring">
            <Node name="TorusFixed">
                <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dz="12" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <LineCollisionModel simulated="0" moving="0" />
                <PointCollisionModel simulated="0" moving="0" />
                <MeshOBJLoader name="meshLoader_14" filename="mesh/torus2.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_14" dz="12" color="gray" />
            </Node>
            <Node name="TorusSpring1">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="2.5" dz="12" />
                <UniformMass totalMass="5" />
                <MeshSpringForceField name="Springs" tetrasStiffness="400" tetrasDamping="4" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_18" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_18" dx="2.5" dz="12" color="green" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="2.5" dz="12" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusSpring2">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MeshGmshLoader name="loader" filename="mesh/torus2_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="5" dz="12" />
                <UniformMass totalMass="5" />
                <MeshSpringForceField name="Springs" tetrasStiffness="400" tetrasDamping="4" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_22" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_22" dx="5" dz="12" color="green" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="5" dz="12" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusSpring3">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="7.5" dz="12" />
                <UniformMass totalMass="5" />
                <MeshSpringForceField name="Springs" tetrasStiffness="400" tetrasDamping="4" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_0" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_0" dx="7.5" dz="12" color="green" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="7.5" dz="12" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusSpring4">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MeshGmshLoader name="loader" filename="mesh/torus2_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="10" dz="12" />
                <UniformMass totalMass="5" />
                <MeshSpringForceField name="Springs" tetrasStiffness="400" tetrasDamping="4" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_5" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_5" dx="10" dz="12" color="green" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="10" dz="12" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
        </Node>
        <Node name="ChainFFD">
            <Node name="TorusFixed">
                <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dz="18" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <LineCollisionModel simulated="0" moving="0" />
                <PointCollisionModel simulated="0" moving="0" />
                <MeshOBJLoader name="meshLoader_9" filename="mesh/torus2.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_9" dz="18" color="gray" />
            </Node>
            <Node name="TorusFFD1">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MechanicalObject dx="2.5" dz="18" />
                <UniformMass totalMass="5" />
                <RegularGridTopology nx="6" ny="2" nz="5" xmin="-2.5" xmax="2.5" ymin="-0.5" ymax="0.5" zmin="-2" zmax="2" />
                <RegularGridSpringForceField name="Springs" stiffness="200" damping="2" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_11" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_11" color="yellow" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFFD2">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MechanicalObject dx="5" dz="18" />
                <UniformMass totalMass="5" />
                <RegularGridTopology nx="6" ny="5" nz="2" xmin="-2.5" xmax="2.5" ymin="-2" ymax="2" zmin="-0.5" zmax="0.5" />
                <RegularGridSpringForceField name="Springs" stiffness="200" damping="2" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_15" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_15" color="yellow" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFFD3">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MechanicalObject dx="7.5" dz="18" />
                <UniformMass totalMass="5" />
                <RegularGridTopology nx="6" ny="2" nz="5" xmin="-2.5" xmax="2.5" ymin="-0.5" ymax="0.5" zmin="-2" zmax="2" />
                <RegularGridSpringForceField name="Springs" stiffness="200" damping="2" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_20" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_20" color="yellow" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFFD4">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MechanicalObject dx="10" dz="18" />
                <UniformMass totalMass="5" />
                <RegularGridTopology nx="6" ny="5" nz="2" xmin="-2.5" xmax="2.5" ymin="-2" ymax="2" zmin="-0.5" zmax="0.5" />
                <RegularGridSpringForceField name="Springs" stiffness="200" damping="2" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_24" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_24" color="yellow" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
        </Node>
        <Node name="ChainRigid">
            <Node name="TorusFixed">
                <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dz="24" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <LineCollisionModel simulated="0" moving="0" />
                <PointCollisionModel simulated="0" moving="0" />
                <MeshOBJLoader name="meshLoader_2" filename="mesh/torus2.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_2" dz="24" color="gray" />
            </Node>
            <Node name="TorusRigid1">
                <EulerImplicitSolver rayleighStiffness="0" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MechanicalObject template="Rigid3" dx="2.5" dz="24" />
                <UniformMass filename="BehaviorModels/torus.rigid" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_4" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_4" color="gray" />
                    <RigidMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <RigidMapping />
                </Node>
            </Node>
            <Node name="TorusRigid2">
                <EulerImplicitSolver rayleighStiffness="0" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MechanicalObject template="Rigid3" dx="5" dz="24" />
                <UniformMass filename="BehaviorModels/torus2.rigid" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_7" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_7" color="gray" />
                    <RigidMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <RigidMapping />
                </Node>
            </Node>
            <Node name="TorusRigid3">
                <EulerImplicitSolver rayleighStiffness="0" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MechanicalObject template="Rigid3" dx="7.5" dz="24" />
                <UniformMass filename="BehaviorModels/torus.rigid" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_12" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_12" color="gray" />
                    <RigidMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <RigidMapping />
                </Node>
            </Node>
            <Node name="TorusRigid4">
                <EulerImplicitSolver rayleighStiffness="0" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MechanicalObject template="Rigid3" dx="10" dz="24" />
                <UniformMass filename="BehaviorModels/torus2.rigid" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_16" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_16" color="gray" />
                    <RigidMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
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
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showMappings")
        root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
        root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

        Chain = root.addChild('Chain')

        TorusFixed = Chain.addChild('TorusFixed')
        TorusFixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        TorusFixed.addObject('MeshTopology', src="@loader")
        TorusFixed.addObject('MechanicalObject', src="@loader")
        TorusFixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
        TorusFixed.addObject('LineCollisionModel', simulated="0", moving="0")
        TorusFixed.addObject('PointCollisionModel', simulated="0", moving="0")
        TorusFixed.addObject('MeshOBJLoader', name="meshLoader_19", filename="mesh/torus2.obj", handleSeams="1")
        TorusFixed.addObject('OglModel', name="Visual", src="@meshLoader_19", color="gray")

        TorusFEM = Chain.addChild('TorusFEM')
        TorusFEM.addObject('EulerImplicitSolver', rayleighStiffness="0.01", rayleighMass="0.1")
        TorusFEM.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
        TorusFEM.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
        TorusFEM.addObject('MeshTopology', src="@loader")
        TorusFEM.addObject('MechanicalObject', src="@loader", dx="2.5")
        TorusFEM.addObject('UniformMass', vertexMass="0.1")
        TorusFEM.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.3", computeGlobalMatrix="false", method="polar")

        Visu = TorusFEM.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_3", color="red", dx="2.5")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFEM.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="2.5")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('LineCollisionModel')
        Surf2.addObject('PointCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusSpring = Chain.addChild('TorusSpring')
        TorusSpring.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
        TorusSpring.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
        TorusSpring.addObject('MeshGmshLoader', name="loader", filename="mesh/torus2_low_res.msh")
        TorusSpring.addObject('MeshTopology', src="@loader")
        TorusSpring.addObject('MechanicalObject', src="@loader", dx="5")
        TorusSpring.addObject('UniformMass', totalMass="5")
        TorusSpring.addObject('MeshSpringForceField', name="Springs", tetrasStiffness="400", tetrasDamping="4")

        Visu = TorusSpring.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_8", filename="mesh/torus2.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_8", dx="5", color="green")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusSpring.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="5")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('LineCollisionModel')
        Surf2.addObject('PointCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusFFD = Chain.addChild('TorusFFD')
        TorusFFD.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
        TorusFFD.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
        TorusFFD.addObject('MechanicalObject', dx="7.5")
        TorusFFD.addObject('UniformMass', totalMass="5")
        TorusFFD.addObject('RegularGridTopology', nx="6", ny="2", nz="5", xmin="-2.5", xmax="2.5", ymin="-0.5", ymax="0.5", zmin="-2", zmax="2")
        TorusFFD.addObject('RegularGridSpringForceField', name="Springs", stiffness="200", damping="2")

        Visu = TorusFFD.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_13", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_13", color="yellow")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFFD.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('LineCollisionModel')
        Surf2.addObject('PointCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusRigid = Chain.addChild('TorusRigid')
        TorusRigid.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
        TorusRigid.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
        TorusRigid.addObject('MechanicalObject', template="Rigid3", dx="10")
        TorusRigid.addObject('UniformMass', filename="BehaviorModels/torus2.rigid")

        Visu = TorusRigid.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_17", filename="mesh/torus2.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_17", color="gray")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        Surf2 = TorusRigid.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('LineCollisionModel')
        Surf2.addObject('PointCollisionModel')
        Surf2.addObject('RigidMapping')

        ChainFEM = root.addChild('ChainFEM')

        TorusFixed = ChainFEM.addChild('TorusFixed')
        TorusFixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        TorusFixed.addObject('MeshTopology', src="@loader")
        TorusFixed.addObject('MechanicalObject', src="@loader", dz="6")
        TorusFixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
        TorusFixed.addObject('LineCollisionModel', simulated="0", moving="0")
        TorusFixed.addObject('PointCollisionModel', simulated="0", moving="0")
        TorusFixed.addObject('MeshOBJLoader', name="meshLoader_21", filename="mesh/torus2.obj", handleSeams="1")
        TorusFixed.addObject('OglModel', name="Visual", src="@meshLoader_21", color="gray", dz="6")

        TorusFEM1 = ChainFEM.addChild('TorusFEM1')
        TorusFEM1.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
        TorusFEM1.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
        TorusFEM1.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
        TorusFEM1.addObject('MeshTopology', src="@loader")
        TorusFEM1.addObject('MechanicalObject', src="@loader", dx="2.5", dz="6")
        TorusFEM1.addObject('UniformMass', totalMass="5")
        TorusFEM1.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.3", computeGlobalMatrix="false", method="polar")

        Visu = TorusFEM1.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_23", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_23", color="red", dx="2.5", dz="6")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFEM1.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="2.5", dz="6")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('LineCollisionModel')
        Surf2.addObject('PointCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusFEM2 = ChainFEM.addChild('TorusFEM2')
        TorusFEM2.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
        TorusFEM2.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
        TorusFEM2.addObject('MeshGmshLoader', name="loader", filename="mesh/torus2_low_res.msh")
        TorusFEM2.addObject('MeshTopology', src="@loader")
        TorusFEM2.addObject('MechanicalObject', src="@loader", dx="5", dz="6")
        TorusFEM2.addObject('UniformMass', totalMass="5")
        TorusFEM2.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.3", computeGlobalMatrix="false", method="polar")

        Visu = TorusFEM2.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/torus2.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="red", dx="5", dz="6")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFEM2.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="5", dz="6")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('LineCollisionModel')
        Surf2.addObject('PointCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusFEM3 = ChainFEM.addChild('TorusFEM3')
        TorusFEM3.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
        TorusFEM3.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
        TorusFEM3.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
        TorusFEM3.addObject('MeshTopology', src="@loader")
        TorusFEM3.addObject('MechanicalObject', src="@loader", dx="7.5", dz="6")
        TorusFEM3.addObject('UniformMass', totalMass="5")
        TorusFEM3.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.3", computeGlobalMatrix="false", method="polar")

        Visu = TorusFEM3.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_6", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_6", color="red", dx="7.5", dz="6")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFEM3.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="7.5", dz="6")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('LineCollisionModel')
        Surf2.addObject('PointCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusFEM4 = ChainFEM.addChild('TorusFEM4')
        TorusFEM4.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
        TorusFEM4.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
        TorusFEM4.addObject('MeshGmshLoader', name="loader", filename="mesh/torus2_low_res.msh")
        TorusFEM4.addObject('MeshTopology', src="@loader")
        TorusFEM4.addObject('MechanicalObject', src="@loader", dx="10", dz="6")
        TorusFEM4.addObject('UniformMass', totalMass="5")
        TorusFEM4.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.3", computeGlobalMatrix="false", method="polar")

        Visu = TorusFEM4.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_10", filename="mesh/torus2.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_10", color="red", dx="10", dz="6")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFEM4.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="10", dz="6")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('LineCollisionModel')
        Surf2.addObject('PointCollisionModel')
        Surf2.addObject('BarycentricMapping')

        ChainSpring = root.addChild('ChainSpring')

        TorusFixed = ChainSpring.addChild('TorusFixed')
        TorusFixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        TorusFixed.addObject('MeshTopology', src="@loader")
        TorusFixed.addObject('MechanicalObject', src="@loader", dz="12")
        TorusFixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
        TorusFixed.addObject('LineCollisionModel', simulated="0", moving="0")
        TorusFixed.addObject('PointCollisionModel', simulated="0", moving="0")
        TorusFixed.addObject('MeshOBJLoader', name="meshLoader_14", filename="mesh/torus2.obj", handleSeams="1")
        TorusFixed.addObject('OglModel', name="Visual", src="@meshLoader_14", dz="12", color="gray")

        TorusSpring1 = ChainSpring.addChild('TorusSpring1')
        TorusSpring1.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
        TorusSpring1.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
        TorusSpring1.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
        TorusSpring1.addObject('MeshTopology', src="@loader")
        TorusSpring1.addObject('MechanicalObject', src="@loader", dx="2.5", dz="12")
        TorusSpring1.addObject('UniformMass', totalMass="5")
        TorusSpring1.addObject('MeshSpringForceField', name="Springs", tetrasStiffness="400", tetrasDamping="4")

        Visu = TorusSpring1.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_18", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_18", dx="2.5", dz="12", color="green")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusSpring1.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="2.5", dz="12")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('LineCollisionModel')
        Surf2.addObject('PointCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusSpring2 = ChainSpring.addChild('TorusSpring2')
        TorusSpring2.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
        TorusSpring2.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
        TorusSpring2.addObject('MeshGmshLoader', name="loader", filename="mesh/torus2_low_res.msh")
        TorusSpring2.addObject('MeshTopology', src="@loader")
        TorusSpring2.addObject('MechanicalObject', src="@loader", dx="5", dz="12")
        TorusSpring2.addObject('UniformMass', totalMass="5")
        TorusSpring2.addObject('MeshSpringForceField', name="Springs", tetrasStiffness="400", tetrasDamping="4")

        Visu = TorusSpring2.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_22", filename="mesh/torus2.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_22", dx="5", dz="12", color="green")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusSpring2.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="5", dz="12")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('LineCollisionModel')
        Surf2.addObject('PointCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusSpring3 = ChainSpring.addChild('TorusSpring3')
        TorusSpring3.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
        TorusSpring3.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
        TorusSpring3.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
        TorusSpring3.addObject('MeshTopology', src="@loader")
        TorusSpring3.addObject('MechanicalObject', src="@loader", dx="7.5", dz="12")
        TorusSpring3.addObject('UniformMass', totalMass="5")
        TorusSpring3.addObject('MeshSpringForceField', name="Springs", tetrasStiffness="400", tetrasDamping="4")

        Visu = TorusSpring3.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_0", dx="7.5", dz="12", color="green")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusSpring3.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="7.5", dz="12")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('LineCollisionModel')
        Surf2.addObject('PointCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusSpring4 = ChainSpring.addChild('TorusSpring4')
        TorusSpring4.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
        TorusSpring4.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
        TorusSpring4.addObject('MeshGmshLoader', name="loader", filename="mesh/torus2_low_res.msh")
        TorusSpring4.addObject('MeshTopology', src="@loader")
        TorusSpring4.addObject('MechanicalObject', src="@loader", dx="10", dz="12")
        TorusSpring4.addObject('UniformMass', totalMass="5")
        TorusSpring4.addObject('MeshSpringForceField', name="Springs", tetrasStiffness="400", tetrasDamping="4")

        Visu = TorusSpring4.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_5", filename="mesh/torus2.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_5", dx="10", dz="12", color="green")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusSpring4.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="10", dz="12")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('LineCollisionModel')
        Surf2.addObject('PointCollisionModel')
        Surf2.addObject('BarycentricMapping')

        ChainFFD = root.addChild('ChainFFD')

        TorusFixed = ChainFFD.addChild('TorusFixed')
        TorusFixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        TorusFixed.addObject('MeshTopology', src="@loader")
        TorusFixed.addObject('MechanicalObject', src="@loader", dz="18")
        TorusFixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
        TorusFixed.addObject('LineCollisionModel', simulated="0", moving="0")
        TorusFixed.addObject('PointCollisionModel', simulated="0", moving="0")
        TorusFixed.addObject('MeshOBJLoader', name="meshLoader_9", filename="mesh/torus2.obj", handleSeams="1")
        TorusFixed.addObject('OglModel', name="Visual", src="@meshLoader_9", dz="18", color="gray")

        TorusFFD1 = ChainFFD.addChild('TorusFFD1')
        TorusFFD1.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
        TorusFFD1.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
        TorusFFD1.addObject('MechanicalObject', dx="2.5", dz="18")
        TorusFFD1.addObject('UniformMass', totalMass="5")
        TorusFFD1.addObject('RegularGridTopology', nx="6", ny="2", nz="5", xmin="-2.5", xmax="2.5", ymin="-0.5", ymax="0.5", zmin="-2", zmax="2")
        TorusFFD1.addObject('RegularGridSpringForceField', name="Springs", stiffness="200", damping="2")

        Visu = TorusFFD1.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_11", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_11", color="yellow")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFFD1.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('LineCollisionModel')
        Surf2.addObject('PointCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusFFD2 = ChainFFD.addChild('TorusFFD2')
        TorusFFD2.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
        TorusFFD2.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
        TorusFFD2.addObject('MechanicalObject', dx="5", dz="18")
        TorusFFD2.addObject('UniformMass', totalMass="5")
        TorusFFD2.addObject('RegularGridTopology', nx="6", ny="5", nz="2", xmin="-2.5", xmax="2.5", ymin="-2", ymax="2", zmin="-0.5", zmax="0.5")
        TorusFFD2.addObject('RegularGridSpringForceField', name="Springs", stiffness="200", damping="2")

        Visu = TorusFFD2.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_15", filename="mesh/torus2.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_15", color="yellow")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFFD2.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('LineCollisionModel')
        Surf2.addObject('PointCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusFFD3 = ChainFFD.addChild('TorusFFD3')
        TorusFFD3.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
        TorusFFD3.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
        TorusFFD3.addObject('MechanicalObject', dx="7.5", dz="18")
        TorusFFD3.addObject('UniformMass', totalMass="5")
        TorusFFD3.addObject('RegularGridTopology', nx="6", ny="2", nz="5", xmin="-2.5", xmax="2.5", ymin="-0.5", ymax="0.5", zmin="-2", zmax="2")
        TorusFFD3.addObject('RegularGridSpringForceField', name="Springs", stiffness="200", damping="2")

        Visu = TorusFFD3.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_20", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_20", color="yellow")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFFD3.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('LineCollisionModel')
        Surf2.addObject('PointCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusFFD4 = ChainFFD.addChild('TorusFFD4')
        TorusFFD4.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
        TorusFFD4.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
        TorusFFD4.addObject('MechanicalObject', dx="10", dz="18")
        TorusFFD4.addObject('UniformMass', totalMass="5")
        TorusFFD4.addObject('RegularGridTopology', nx="6", ny="5", nz="2", xmin="-2.5", xmax="2.5", ymin="-2", ymax="2", zmin="-0.5", zmax="0.5")
        TorusFFD4.addObject('RegularGridSpringForceField', name="Springs", stiffness="200", damping="2")

        Visu = TorusFFD4.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_24", filename="mesh/torus2.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_24", color="yellow")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFFD4.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('LineCollisionModel')
        Surf2.addObject('PointCollisionModel')
        Surf2.addObject('BarycentricMapping')

        ChainRigid = root.addChild('ChainRigid')

        TorusFixed = ChainRigid.addChild('TorusFixed')
        TorusFixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        TorusFixed.addObject('MeshTopology', src="@loader")
        TorusFixed.addObject('MechanicalObject', src="@loader", dz="24")
        TorusFixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
        TorusFixed.addObject('LineCollisionModel', simulated="0", moving="0")
        TorusFixed.addObject('PointCollisionModel', simulated="0", moving="0")
        TorusFixed.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/torus2.obj", handleSeams="1")
        TorusFixed.addObject('OglModel', name="Visual", src="@meshLoader_2", dz="24", color="gray")

        TorusRigid1 = ChainRigid.addChild('TorusRigid1')
        TorusRigid1.addObject('EulerImplicitSolver', rayleighStiffness="0")
        TorusRigid1.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
        TorusRigid1.addObject('MechanicalObject', template="Rigid3", dx="2.5", dz="24")
        TorusRigid1.addObject('UniformMass', filename="BehaviorModels/torus.rigid")

        Visu = TorusRigid1.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_4", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_4", color="gray")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        Surf2 = TorusRigid1.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('LineCollisionModel')
        Surf2.addObject('PointCollisionModel')
        Surf2.addObject('RigidMapping')

        TorusRigid2 = ChainRigid.addChild('TorusRigid2')
        TorusRigid2.addObject('EulerImplicitSolver', rayleighStiffness="0")
        TorusRigid2.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
        TorusRigid2.addObject('MechanicalObject', template="Rigid3", dx="5", dz="24")
        TorusRigid2.addObject('UniformMass', filename="BehaviorModels/torus2.rigid")

        Visu = TorusRigid2.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_7", filename="mesh/torus2.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_7", color="gray")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        Surf2 = TorusRigid2.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('LineCollisionModel')
        Surf2.addObject('PointCollisionModel')
        Surf2.addObject('RigidMapping')

        TorusRigid3 = ChainRigid.addChild('TorusRigid3')
        TorusRigid3.addObject('EulerImplicitSolver', rayleighStiffness="0")
        TorusRigid3.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
        TorusRigid3.addObject('MechanicalObject', template="Rigid3", dx="7.5", dz="24")
        TorusRigid3.addObject('UniformMass', filename="BehaviorModels/torus.rigid")

        Visu = TorusRigid3.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_12", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_12", color="gray")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        Surf2 = TorusRigid3.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('LineCollisionModel')
        Surf2.addObject('PointCollisionModel')
        Surf2.addObject('RigidMapping')

        TorusRigid4 = ChainRigid.addChild('TorusRigid4')
        TorusRigid4.addObject('EulerImplicitSolver', rayleighStiffness="0")
        TorusRigid4.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
        TorusRigid4.addObject('MechanicalObject', template="Rigid3", dx="10", dz="24")
        TorusRigid4.addObject('UniformMass', filename="BehaviorModels/torus2.rigid")

        Visu = TorusRigid4.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_16", filename="mesh/torus2.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_16", color="gray")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        Surf2 = TorusRigid4.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('LineCollisionModel')
        Surf2.addObject('PointCollisionModel')
        Surf2.addObject('RigidMapping')
    ```

Component/Mapping/Linear/BarycentricMappingTrussBeam.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.01" showBoundingTree="0" gravity="0 0 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [LocalMinDistance] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping IdentityMapping TubularMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [ConstantForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [BeamFEMForceField TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [QuadSetGeometryAlgorithms QuadSetTopologyContainer QuadSetTopologyModifier TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Edge2QuadTopologicalMapping Tetra2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <VisualStyle displayFlags="showVisual showBehaviorModels showCollisionModels" />
        <CollisionPipeline verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <LocalMinDistance name="Proximity" alarmDistance="0.5" contactDistance="0.05" />
        <CollisionResponse response="PenalityContactForceField" />
        <DefaultAnimationLoop/>
        
        <!-- A deformable square mesh -->
        <Node name="Truss" activated="true" gravity="0 0 0">
            <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="125" tolerance="1e-16" threshold="1e-16" />
            <MeshGmshLoader name="meshLoader0" filename="mesh/truss_tetra.msh" />
            <TetrahedronSetTopologyContainer name="Container" src="@meshLoader0" />
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <MechanicalObject template="Vec3" name="TrussMO" />
            <UniformMass totalMass="0.05" />
            <BoxConstraint box="-0.001 -0.001 -0.001 0.001 0.011 0.011" />
            <TetrahedronFEMForceField name="FEM" youngModulus="300000" poissonRatio="0.45" method="large" />
            <BoxROI box="0.099 -0.001 -0.001 0.11 0.011 0.011"/>
            <ConstantForceField forces="0 -0.1 0" />
    
            <Node name="Triangle">
                <include href="Objects/TriangleSetTopology.xml" />
                <Tetra2TriangleTopologicalMapping input="@/Truss/Container" output="@Container" />
                <TriangleCollisionModel />
                <Node name="TriangleVisual">
                    <OglModel template="Vec3" name="Visual" material="Default Diffuse 1 1 0 0 1 Ambient 1 0.2 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45" />
                    <IdentityMapping template="Vec3,Vec3" name="default12" input="@.." output="@Visual" />
                </Node>
            </Node>
            <Node name="Beam">
                <MechanicalObject template="Rigid3" name="BeamMO" position="0 0 0  0 0 0 1  0.02 0 0  0 0 0 1  0.04 0 0  0 0 0 1   0.06 0 0  0 0 0 1  0.08 0 0  0 0 0 1   0.1 0 0  0 0 0 1" />
                <MeshTopology name="BeamMesh" lines="0 1 1 2 2 3 3 4 4 5" />
                <FixedProjectiveConstraint name="BeamFixedProjectiveConstraint" indices="0" />
                <UniformMass vertexMass="0.001 0.001 [0.0001 0 0 0 0.0001 0 0 0 0.0001]" />
                <BeamFEMForceField name="BeamFEM" radius="0.005" youngModulus="3000000000" poissonRatio="0.45" />
                <ConstantForceField indices="5" forces="0 0 0 -10 0 0" />
                <BarycentricMapping isMechanical="true" input="@TrussMO" output="@BeamMO" />
                <Node name="VisuThread">
                    <MechanicalObject name="Quads" />
                    <include href="Objects/QuadSetTopology.xml" />
                    <Edge2QuadTopologicalMapping nbPointsOnEachCircle="10" radius="0.005" input="@BeamMesh" output="@Container" />
                    <TubularMapping nbPointsOnEachCircle="10" radius="0.005" input="@BeamMO" output="@Quads" />
                    <Node name="VisuOgl">
                        <OglModel name="Visual" color="0.5 0.5 1.0" />
                        <IdentityMapping input="@Quads" output="@Visual" />
                    </Node>
                </Node>
            </Node>
        </Node>
    </Node>
    
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01", showBoundingTree="0", gravity="0 0 0")
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
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels showCollisionModels")
        root.addObject('CollisionPipeline', verbose="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('LocalMinDistance', name="Proximity", alarmDistance="0.5", contactDistance="0.05")
        root.addObject('CollisionResponse', response="PenalityContactForceField")
        root.addObject('DefaultAnimationLoop')

        Truss = root.addChild('Truss', activated="true", gravity="0 0 0")
        Truss.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
        Truss.addObject('CGLinearSolver', iterations="125", tolerance="1e-16", threshold="1e-16")
        Truss.addObject('MeshGmshLoader', name="meshLoader0", filename="mesh/truss_tetra.msh")
        Truss.addObject('TetrahedronSetTopologyContainer', name="Container", src="@meshLoader0")
        Truss.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        Truss.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        Truss.addObject('MechanicalObject', template="Vec3", name="TrussMO")
        Truss.addObject('UniformMass', totalMass="0.05")
        Truss.addObject('BoxConstraint', box="-0.001 -0.001 -0.001 0.001 0.011 0.011")
        Truss.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="300000", poissonRatio="0.45", method="large")
        Truss.addObject('BoxROI', box="0.099 -0.001 -0.001 0.11 0.011 0.011")
        Truss.addObject('ConstantForceField', forces="0 -0.1 0")

        Triangle = Truss.addChild('Triangle')
        Triangle.addObject('include', href="Objects/TriangleSetTopology.xml")
        Triangle.addObject('Tetra2TriangleTopologicalMapping', input="@/Truss/Container", output="@Container")
        Triangle.addObject('TriangleCollisionModel')

        TriangleVisual = Triangle.addChild('TriangleVisual')
        TriangleVisual.addObject('OglModel', template="Vec3", name="Visual", material="Default Diffuse 1 1 0 0 1 Ambient 1 0.2 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45")
        TriangleVisual.addObject('IdentityMapping', template="Vec3,Vec3", name="default12", input="@..", output="@Visual")

        Beam = Truss.addChild('Beam')
        Beam.addObject('MechanicalObject', template="Rigid3", name="BeamMO", position="0 0 0  0 0 0 1  0.02 0 0  0 0 0 1  0.04 0 0  0 0 0 1   0.06 0 0  0 0 0 1  0.08 0 0  0 0 0 1   0.1 0 0  0 0 0 1")
        Beam.addObject('MeshTopology', name="BeamMesh", lines="0 1 1 2 2 3 3 4 4 5")
        Beam.addObject('FixedProjectiveConstraint', name="BeamFixedProjectiveConstraint", indices="0")
        Beam.addObject('UniformMass', vertexMass="0.001 0.001 [0.0001 0 0 0 0.0001 0 0 0 0.0001]")
        Beam.addObject('BeamFEMForceField', name="BeamFEM", radius="0.005", youngModulus="3000000000", poissonRatio="0.45")
        Beam.addObject('ConstantForceField', indices="5", forces="0 0 0 -10 0 0")
        Beam.addObject('BarycentricMapping', isMechanical="true", input="@TrussMO", output="@BeamMO")

        VisuThread = Beam.addChild('VisuThread')
        VisuThread.addObject('MechanicalObject', name="Quads")
        VisuThread.addObject('include', href="Objects/QuadSetTopology.xml")
        VisuThread.addObject('Edge2QuadTopologicalMapping', nbPointsOnEachCircle="10", radius="0.005", input="@BeamMesh", output="@Container")
        VisuThread.addObject('TubularMapping', nbPointsOnEachCircle="10", radius="0.005", input="@BeamMO", output="@Quads")

        VisuOgl = VisuThread.addChild('VisuOgl')
        VisuOgl.addObject('OglModel', name="Visual", color="0.5 0.5 1.0")
        VisuOgl.addObject('IdentityMapping', input="@Quads", output="@Visual")
    ```

