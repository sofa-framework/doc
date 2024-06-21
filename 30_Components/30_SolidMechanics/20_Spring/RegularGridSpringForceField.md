# RegularGridSpringForceField

Spring acting on the edges and faces of a regular grid


__Templates__:

- `#!c++ Vec1d`
- `#!c++ Vec2d`
- `#!c++ Vec3d`
- `#!c++ Vec6d`

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
		<td>linesStiffness</td>
		<td>
Lines Stiffness
</td>
		<td>100</td>
	</tr>
	<tr>
		<td>linesDamping</td>
		<td>
Lines Damping
</td>
		<td>5</td>
	</tr>
	<tr>
		<td>quadsStiffness</td>
		<td>
Quads Stiffness
</td>
		<td>100</td>
	</tr>
	<tr>
		<td>quadsDamping</td>
		<td>
Quads Damping
</td>
		<td>5</td>
	</tr>
	<tr>
		<td>cubesStiffness</td>
		<td>
Cubes Stiffness
</td>
		<td>100</td>
	</tr>
	<tr>
		<td>cubesDamping</td>
		<td>
Cubes Damping
</td>
		<td>5</td>
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



## Examples

Component/SolidMechanics/Spring/RegularGridSpringForceField.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [NewProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [RegularGridSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <NewProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <DefaultAnimationLoop/>
        
        <Node name="Chain">
            <Node name="TorusFixed">
                <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <MeshOBJLoader name="meshLoader_3" filename="mesh/torus2.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_3" color="gray" />
            </Node>
            <Node name="TorusFFD1">
                <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MechanicalObject translation="2.5 0 0" />
                <UniformMass totalMass="5" />
                <RegularGridTopology nx="6" ny="2" nz="5" xmin="-2.5" xmax="2.5" ymin="-0.5" ymax="0.5" zmin="-2" zmax="2" />
                <RegularGridSpringForceField name="Springs" stiffness="200" damping="2" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_4" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_4" dx="2.5" color="yellow" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" translation="2.5 0 0" />
                    <TriangleCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFFD2">
                <EulerImplicitSolver name="cg_odesolver" printLog="false" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MechanicalObject dx="5" />
                <UniformMass totalMass="5" />
                <RegularGridTopology nx="6" ny="5" nz="2" xmin="-2.5" xmax="2.5" ymin="-2" ymax="2" zmin="-0.5" zmax="0.5" />
                <RegularGridSpringForceField name="Springs" stiffness="200" damping="2" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_1" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_1" dx="5" color="yellow" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="5" />
                    <TriangleCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFFD3">
                <EulerImplicitSolver name="cg_odesolver" printLog="false" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MechanicalObject dx="7.5" />
                <UniformMass totalMass="5" />
                <RegularGridTopology nx="6" ny="2" nz="5" xmin="-2.5" xmax="2.5" ymin="-0.5" ymax="0.5" zmin="-2" zmax="2" />
                <RegularGridSpringForceField name="Springs" stiffness="200" damping="2" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_2" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_2" dx="7.5" color="yellow" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="7.5" />
                    <TriangleCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFFD4">
                <EulerImplicitSolver name="cg_odesolver" printLog="false" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MechanicalObject dx="10" />
                <UniformMass totalMass="5" />
                <RegularGridTopology nx="6" ny="5" nz="2" xmin="-2.5" xmax="2.5" ymin="-2" ymax="2" zmin="-0.5" zmax="0.5" />
                <RegularGridSpringForceField name="Springs" stiffness="200" damping="2" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_0" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_0" dx="10" color="yellow" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="10" />
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

        root = rootNode.addChild('root', dt="0.02")
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
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('NewProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
        root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")
        root.addObject('DefaultAnimationLoop')

        Chain = root.addChild('Chain')

        TorusFixed = Chain.addChild('TorusFixed')
        TorusFixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        TorusFixed.addObject('MeshTopology', src="@loader")
        TorusFixed.addObject('MechanicalObject', src="@loader")
        TorusFixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
        TorusFixed.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/torus2.obj", handleSeams="1")
        TorusFixed.addObject('OglModel', name="Visual", src="@meshLoader_3", color="gray")

        TorusFFD1 = Chain.addChild('TorusFFD1')
        TorusFFD1.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        TorusFFD1.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TorusFFD1.addObject('MechanicalObject', translation="2.5 0 0")
        TorusFFD1.addObject('UniformMass', totalMass="5")
        TorusFFD1.addObject('RegularGridTopology', nx="6", ny="2", nz="5", xmin="-2.5", xmax="2.5", ymin="-0.5", ymax="0.5", zmin="-2", zmax="2")
        TorusFFD1.addObject('RegularGridSpringForceField', name="Springs", stiffness="200", damping="2")

        Visu = TorusFFD1.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_4", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_4", dx="2.5", color="yellow")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFFD1.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", translation="2.5 0 0")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusFFD2 = Chain.addChild('TorusFFD2')
        TorusFFD2.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        TorusFFD2.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TorusFFD2.addObject('MechanicalObject', dx="5")
        TorusFFD2.addObject('UniformMass', totalMass="5")
        TorusFFD2.addObject('RegularGridTopology', nx="6", ny="5", nz="2", xmin="-2.5", xmax="2.5", ymin="-2", ymax="2", zmin="-0.5", zmax="0.5")
        TorusFFD2.addObject('RegularGridSpringForceField', name="Springs", stiffness="200", damping="2")

        Visu = TorusFFD2.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/torus2.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_1", dx="5", color="yellow")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFFD2.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="5")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusFFD3 = Chain.addChild('TorusFFD3')
        TorusFFD3.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        TorusFFD3.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TorusFFD3.addObject('MechanicalObject', dx="7.5")
        TorusFFD3.addObject('UniformMass', totalMass="5")
        TorusFFD3.addObject('RegularGridTopology', nx="6", ny="2", nz="5", xmin="-2.5", xmax="2.5", ymin="-0.5", ymax="0.5", zmin="-2", zmax="2")
        TorusFFD3.addObject('RegularGridSpringForceField', name="Springs", stiffness="200", damping="2")

        Visu = TorusFFD3.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_2", dx="7.5", color="yellow")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFFD3.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="7.5")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusFFD4 = Chain.addChild('TorusFFD4')
        TorusFFD4.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        TorusFFD4.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TorusFFD4.addObject('MechanicalObject', dx="10")
        TorusFFD4.addObject('UniformMass', totalMass="5")
        TorusFFD4.addObject('RegularGridTopology', nx="6", ny="5", nz="2", xmin="-2.5", xmax="2.5", ymin="-2", ymax="2", zmin="-0.5", zmax="0.5")
        TorusFFD4.addObject('RegularGridSpringForceField', name="Springs", stiffness="200", damping="2")

        Visu = TorusFFD4.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus2.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_0", dx="10", color="yellow")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFFD4.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="10")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('BarycentricMapping')
    ```

