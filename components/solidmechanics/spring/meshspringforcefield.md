# MeshSpringForceField

Spring force field acting along the edges of a mesh
Supports GPU-side computations using CUDA


__Templates__:

- `#!c++ Vec1d`
- `#!c++ Vec2d`
- `#!c++ Vec3d`

__Target__: `Sofa.Component.SolidMechanics.Spring`

__namespace__: `#!c++ sofa::component::solidmechanics::spring`

__parents__: 

- `#!c++ StiffSpringForceField`

__categories__: 

- ForceField
- InteractionForceField

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
		<td>linesStiffness</td>
		<td>
Stiffness for the Lines
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>linesDamping</td>
		<td>
Damping for the Lines
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>trianglesStiffness</td>
		<td>
Stiffness for the Triangles
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>trianglesDamping</td>
		<td>
Damping for the Triangles
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>quadsStiffness</td>
		<td>
Stiffness for the Quads
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>quadsDamping</td>
		<td>
Damping for the Quads
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>tetrahedraStiffness</td>
		<td>
Stiffness for the Tetrahedra
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>tetrahedraDamping</td>
		<td>
Damping for the Tetrahedra
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>cubesStiffness</td>
		<td>
Stiffness for the Cubes
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>cubesDamping</td>
		<td>
Damping for the Cubes
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>noCompression</td>
		<td>
Only consider elongation
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>localRange</td>
		<td>
optional range of local DOF indices. Any computation involving only indices outside of this range are discarded (useful for parallelization using mesh partitionning)
</td>
		<td>4294967295 4294967295</td>
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
	<tr>
		<td>drawMinElongationRange</td>
		<td>
Min range of elongation (red eongation - blue neutral - green compression)
</td>
		<td>8</td>
	</tr>
	<tr>
		<td>drawMaxElongationRange</td>
		<td>
Max range of elongation (red eongation - blue neutral - green compression)
</td>
		<td>15</td>
	</tr>
	<tr>
		<td>drawSpringSize</td>
		<td>
Size of drawed lines
</td>
		<td>8</td>
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

Component/SolidMechanics/Spring/MeshSpringForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 -9 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [NewProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [MeshSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <DefaultAnimationLoop/>
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <NewProximityIntersection name="Proximity" alarmDistance="0.5" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="ChainSpring">
            <Node name="TorusFixed">
                <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <MeshOBJLoader name="meshLoader_3" filename="mesh/torus2.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_3" color="gray" />
            </Node>
            <Node name="TorusSpring1">
                <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver iterations="100" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" translation="2.5 0 0"/>
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <UniformMass totalMass="5" />
                <MeshSpringForceField name="Springs" tetrasStiffness="1000" tetrasDamping="0" />
                <Node name="Visu1">
                    <MeshOBJLoader name="meshLoader_0" filename="mesh/torus.obj" translation="2.5 0 0" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_0" color="green"/>
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf1">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" translation="2.5 0 0"/>
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusSpring2">
                <EulerImplicitSolver name="cg_odesolver" printLog="false" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MeshGmshLoader name="loader" filename="mesh/torus2_low_res.msh" translation="5 0 0"/>
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <UniformMass totalMass="5" />
                <MeshSpringForceField name="Springs" tetrasStiffness="200" tetrasDamping="0" />
                <Node name="Visu2">
                    <MeshOBJLoader name="meshLoader_2" filename="mesh/torus2.obj" translation="5 0 0" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_2" color="blue"/>
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" translation="5 0 0"/>
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader"  />
                    <TriangleCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusSpring3">
                <EulerImplicitSolver name="cg_odesolver" printLog="false" />
                <CGLinearSolver iterations="100" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" translation="7.5 0 0"/>
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <UniformMass totalMass="0.5" />
                <MeshSpringForceField name="Springs" tetrasStiffness="400" tetrasDamping="0" />
                <Node name="Visu3">
                    <MeshOBJLoader name="meshLoader_1" filename="mesh/torus.obj" translation="7.5 0 0" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_1" color="green"/>
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf3">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" translation="7.5 0 0"/>
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader"  />
                    <TriangleCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusSpring4">
                <EulerImplicitSolver name="cg_odesolver" printLog="false" />
                <CGLinearSolver iterations="100" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MeshGmshLoader name="loader" filename="mesh/torus2_low_res.msh" translation="10 0 0"/>
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader"  />
                <UniformMass totalMass="0.5" />
                <MeshSpringForceField name="Springs" tetrasStiffness="400" tetrasDamping="0" />
                <Node name="Visu4">
                    <MeshOBJLoader name="meshLoader_4" filename="mesh/torus2.obj" translation="10 0 0" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_4" color="red"/>
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf4">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" translation="10 0 0"/>
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader"  />
                    <TriangleCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01", gravity="0 -9 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')
        root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('NewProximityIntersection', name="Proximity", alarmDistance="0.5", contactDistance="0.2")
        root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

        ChainSpring = root.addChild('ChainSpring')

        TorusFixed = ChainSpring.addChild('TorusFixed')
        TorusFixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        TorusFixed.addObject('MeshTopology', src="@loader")
        TorusFixed.addObject('MechanicalObject', src="@loader")
        TorusFixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
        TorusFixed.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/torus2.obj", handleSeams="1")
        TorusFixed.addObject('OglModel', name="Visual", src="@meshLoader_3", color="gray")

        TorusSpring1 = ChainSpring.addChild('TorusSpring1')
        TorusSpring1.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        TorusSpring1.addObject('CGLinearSolver', iterations="100", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TorusSpring1.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh", translation="2.5 0 0")
        TorusSpring1.addObject('MeshTopology', src="@loader")
        TorusSpring1.addObject('MechanicalObject', src="@loader")
        TorusSpring1.addObject('UniformMass', totalMass="5")
        TorusSpring1.addObject('MeshSpringForceField', name="Springs", tetrasStiffness="1000", tetrasDamping="0")

        Visu1 = TorusSpring1.addChild('Visu1')
        Visu1.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", translation="2.5 0 0", handleSeams="1")
        Visu1.addObject('OglModel', name="Visual", src="@meshLoader_0", color="green")
        Visu1.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf1 = TorusSpring1.addChild('Surf1')
        Surf1.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj", translation="2.5 0 0")
        Surf1.addObject('MeshTopology', src="@loader")
        Surf1.addObject('MechanicalObject', src="@loader")
        Surf1.addObject('TriangleCollisionModel')
        Surf1.addObject('BarycentricMapping')

        TorusSpring2 = ChainSpring.addChild('TorusSpring2')
        TorusSpring2.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        TorusSpring2.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TorusSpring2.addObject('MeshGmshLoader', name="loader", filename="mesh/torus2_low_res.msh", translation="5 0 0")
        TorusSpring2.addObject('MeshTopology', src="@loader")
        TorusSpring2.addObject('MechanicalObject', src="@loader")
        TorusSpring2.addObject('UniformMass', totalMass="5")
        TorusSpring2.addObject('MeshSpringForceField', name="Springs", tetrasStiffness="200", tetrasDamping="0")

        Visu2 = TorusSpring2.addChild('Visu2')
        Visu2.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/torus2.obj", translation="5 0 0", handleSeams="1")
        Visu2.addObject('OglModel', name="Visual", src="@meshLoader_2", color="blue")
        Visu2.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusSpring2.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj", translation="5 0 0")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusSpring3 = ChainSpring.addChild('TorusSpring3')
        TorusSpring3.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        TorusSpring3.addObject('CGLinearSolver', iterations="100", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TorusSpring3.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh", translation="7.5 0 0")
        TorusSpring3.addObject('MeshTopology', src="@loader")
        TorusSpring3.addObject('MechanicalObject', src="@loader")
        TorusSpring3.addObject('UniformMass', totalMass="0.5")
        TorusSpring3.addObject('MeshSpringForceField', name="Springs", tetrasStiffness="400", tetrasDamping="0")

        Visu3 = TorusSpring3.addChild('Visu3')
        Visu3.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/torus.obj", translation="7.5 0 0", handleSeams="1")
        Visu3.addObject('OglModel', name="Visual", src="@meshLoader_1", color="green")
        Visu3.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf3 = TorusSpring3.addChild('Surf3')
        Surf3.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj", translation="7.5 0 0")
        Surf3.addObject('MeshTopology', src="@loader")
        Surf3.addObject('MechanicalObject', src="@loader")
        Surf3.addObject('TriangleCollisionModel')
        Surf3.addObject('BarycentricMapping')

        TorusSpring4 = ChainSpring.addChild('TorusSpring4')
        TorusSpring4.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        TorusSpring4.addObject('CGLinearSolver', iterations="100", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TorusSpring4.addObject('MeshGmshLoader', name="loader", filename="mesh/torus2_low_res.msh", translation="10 0 0")
        TorusSpring4.addObject('MeshTopology', src="@loader")
        TorusSpring4.addObject('MechanicalObject', src="@loader")
        TorusSpring4.addObject('UniformMass', totalMass="0.5")
        TorusSpring4.addObject('MeshSpringForceField', name="Springs", tetrasStiffness="400", tetrasDamping="0")

        Visu4 = TorusSpring4.addChild('Visu4')
        Visu4.addObject('MeshOBJLoader', name="meshLoader_4", filename="mesh/torus2.obj", translation="10 0 0", handleSeams="1")
        Visu4.addObject('OglModel', name="Visual", src="@meshLoader_4", color="red")
        Visu4.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf4 = TorusSpring4.addChild('Surf4')
        Surf4.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj", translation="10 0 0")
        Surf4.addObject('MeshTopology', src="@loader")
        Surf4.addObject('MechanicalObject', src="@loader")
        Surf4.addObject('TriangleCollisionModel')
        Surf4.addObject('BarycentricMapping')
    ```

SofaCUDA/share/sofa/examples/SofaCUDA/benchmarks/MeshSpringForceField_beam10x10x40_gpu.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 -9 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="SofaCUDA"/> <!-- Needed to use components [BoxROI FixedProjectiveConstraint IdentityMapping MechanicalObject MeshSpringForceField UniformMass] -->
    
        <VisualStyle displayFlags="showBehaviorModels" />
        
        <DefaultAnimationLoop/>
    	<DefaultVisualManagerLoop/>
    	<CollisionPipeline depth="6" verbose="0" draw="0"/>
    	<BruteForceBroadPhase/>
        <BVHNarrowPhase/>
    	<MinProximityIntersection name="Proximity" alarmDistance="0.5" contactDistance="0.3" />
    	<CollisionResponse name="Response" response="PenalityContactForceField" />
        
        <Node name="Beam">
            <RegularGridTopology name="grid" n="40 10 10" min="0 6 -2" max="16 10 2" />
            <TetrahedronSetTopologyContainer name="BeamTopo" />
            <TetrahedronSetTopologyModifier name="Modifier" />
    
            <Hexa2TetraTopologicalMapping input="@grid" output="@BeamTopo" />
        </Node>
        
        <Node name="MeshSpringForceField-GPU-Green">
            <EulerImplicitSolver name="cg_odesolver"  printLog="0" />
            <CGLinearSolver name="linear solver"  iterations="20"  tolerance="1e-06"  threshold="1e-06" />
                    
            <MechanicalObject position="@../Beam/grid.position" name="Volume" template="CudaVec3f"/>
            <TetrahedronSetTopologyContainer name="Container" src="@../Beam/BeamTopo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
    		        
            <BoxROI name="ROI1" box="-0.1 5 -3 0.1 11 3" drawBoxes="1" />        
            <FixedProjectiveConstraint indices="@ROI1.indices" />
            
            <UniformMass totalMass="100" />
            <MeshSpringForceField name="Springs" tetrasStiffness="1200" tetrasDamping="0" template="CudaVec3f"/>
           
            <Node name="MeshVisu">
    			<OglModel name="Visual" topology="@../Container" position="@../Volume.position" color="green"/>
    			<IdentityMapping input="@../Volume" output="@Visual" />
    		</Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01", gravity="0 -9 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('RequiredPlugin', name="SofaCUDA")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels")
        root.addObject('DefaultAnimationLoop')
        root.addObject('DefaultVisualManagerLoop')
        root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.5", contactDistance="0.3")
        root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

        Beam = root.addChild('Beam')
        Beam.addObject('RegularGridTopology', name="grid", n="40 10 10", min="0 6 -2", max="16 10 2")
        Beam.addObject('TetrahedronSetTopologyContainer', name="BeamTopo")
        Beam.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        Beam.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@BeamTopo")

        MeshSpringForceField-GPU-Green = root.addChild('MeshSpringForceField-GPU-Green')
        MeshSpringForceField-GPU-Green.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="0")
        MeshSpringForceField-GPU-Green.addObject('CGLinearSolver', name="linear solver", iterations="20", tolerance="1e-06", threshold="1e-06")
        MeshSpringForceField-GPU-Green.addObject('MechanicalObject', position="@../Beam/grid.position", name="Volume", template="CudaVec3f")
        MeshSpringForceField-GPU-Green.addObject('TetrahedronSetTopologyContainer', name="Container", src="@../Beam/BeamTopo")
        MeshSpringForceField-GPU-Green.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        MeshSpringForceField-GPU-Green.addObject('BoxROI', name="ROI1", box="-0.1 5 -3 0.1 11 3", drawBoxes="1")
        MeshSpringForceField-GPU-Green.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")
        MeshSpringForceField-GPU-Green.addObject('UniformMass', totalMass="100")
        MeshSpringForceField-GPU-Green.addObject('MeshSpringForceField', name="Springs", tetrasStiffness="1200", tetrasDamping="0", template="CudaVec3f")

        MeshVisu = MeshSpringForceField-GPU-Green.addChild('MeshVisu')
        MeshVisu.addObject('OglModel', name="Visual", topology="@../Container", position="@../Volume.position", color="green")
        MeshVisu.addObject('IdentityMapping', input="@../Volume", output="@Visual")
    ```

SofaCUDA/share/sofa/examples/SofaCUDA/benchmarks/MeshSpringForceField_beam10x10x40_cpu.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 -9 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [MeshSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <VisualStyle displayFlags="showBehaviorModels" />
        
        <DefaultAnimationLoop/>
    	<DefaultVisualManagerLoop/>
    	<CollisionPipeline depth="6" verbose="0" draw="0"/>
    	<BruteForceBroadPhase/>
        <BVHNarrowPhase/>
    	<MinProximityIntersection name="Proximity" alarmDistance="0.5" contactDistance="0.3" />
    	<CollisionResponse name="Response" response="PenalityContactForceField" />
        
        <Node name="Beam">
            <RegularGridTopology name="grid" n="40 10 10" min="0 6 -2" max="16 10 2" />
            <TetrahedronSetTopologyContainer name="BeamTopo" />
            <TetrahedronSetTopologyModifier name="Modifier" />
    
            <Hexa2TetraTopologicalMapping input="@grid" output="@BeamTopo" />
        </Node>
    
        <Node name="MeshSpringForceField-CPU-Red">
            <EulerImplicitSolver name="cg_odesolver"  printLog="0" />
            <CGLinearSolver name="linear solver"  iterations="20"  tolerance="1e-06"  threshold="1e-06" />
                    
            <MechanicalObject position="@../Beam/grid.position" name="Volume" template="Vec3"/>
            <TetrahedronSetTopologyContainer name="Container" src="@../Beam/BeamTopo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
    		        
            <BoxROI name="ROI1" box="-0.1 5 -3 0.1 11 3" drawBoxes="1" />        
            <FixedProjectiveConstraint indices="@ROI1.indices" />
            
            <UniformMass totalMass="100" />
            
            <MeshSpringForceField name="Springs" tetrasStiffness="1200" tetrasDamping="0" template="Vec3"/>
           
            <Node name="MeshVisu">
    			<OglModel name="Visual" topology="@../Container" position="@../Volume.position" color="red"/>
    			<IdentityMapping input="@../Volume" output="@Visual" />
    		</Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01", gravity="0 -9 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels")
        root.addObject('DefaultAnimationLoop')
        root.addObject('DefaultVisualManagerLoop')
        root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.5", contactDistance="0.3")
        root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

        Beam = root.addChild('Beam')
        Beam.addObject('RegularGridTopology', name="grid", n="40 10 10", min="0 6 -2", max="16 10 2")
        Beam.addObject('TetrahedronSetTopologyContainer', name="BeamTopo")
        Beam.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        Beam.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@BeamTopo")

        MeshSpringForceField-CPU-Red = root.addChild('MeshSpringForceField-CPU-Red')
        MeshSpringForceField-CPU-Red.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="0")
        MeshSpringForceField-CPU-Red.addObject('CGLinearSolver', name="linear solver", iterations="20", tolerance="1e-06", threshold="1e-06")
        MeshSpringForceField-CPU-Red.addObject('MechanicalObject', position="@../Beam/grid.position", name="Volume", template="Vec3")
        MeshSpringForceField-CPU-Red.addObject('TetrahedronSetTopologyContainer', name="Container", src="@../Beam/BeamTopo")
        MeshSpringForceField-CPU-Red.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        MeshSpringForceField-CPU-Red.addObject('BoxROI', name="ROI1", box="-0.1 5 -3 0.1 11 3", drawBoxes="1")
        MeshSpringForceField-CPU-Red.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")
        MeshSpringForceField-CPU-Red.addObject('UniformMass', totalMass="100")
        MeshSpringForceField-CPU-Red.addObject('MeshSpringForceField', name="Springs", tetrasStiffness="1200", tetrasDamping="0", template="Vec3")

        MeshVisu = MeshSpringForceField-CPU-Red.addChild('MeshVisu')
        MeshVisu.addObject('OglModel', name="Visual", topology="@../Container", position="@../Volume.position", color="red")
        MeshVisu.addObject('IdentityMapping', input="@../Volume", output="@Visual")
    ```

