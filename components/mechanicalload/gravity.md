# Gravity

Gravity in world coordinates


__Target__: `Sofa.Component.MechanicalLoad`

__namespace__: `#!c++ sofa::component::mechanicalload`

__parents__: 

- `#!c++ ContextObject`

__categories__: 

- ContextObject

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
		<td>gravity</td>
		<td>
Gravity in the world coordinate system
</td>
		<td>0 0 0</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|



## Examples

Component/SceneUtility/Gravity.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.03333">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
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
        <RequiredPlugin name="SofaGraphComponent"/> <!-- Needed to use components [Gravity] -->
    
        <CollisionPipeline verbose="0" depth="10" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.75" contactDistance="0.5" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <DefaultAnimationLoop/>
        <Node name="Torus1">
            <Gravity gravity="0 -10 0" />
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject dx="0" dy="20" dz="0" ry="90" />
            <UniformMass totalMass="10" />
            <RegularGridTopology nx="6" ny="5" nz="2" xmin="-7.5" xmax="7.5" ymin="-6" ymax="6" zmin="-1.75" zmax="1.75" />
            <RegularGridSpringForceField name="Springs" stiffness="350" damping="1" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/torus2_scale3.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_0" color="blue" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Surf">
                <MeshOBJLoader name="loader" filename="mesh/torus2_scale3.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader"/>
                <TriangleCollisionModel />
                <LineCollisionModel />
                <PointCollisionModel />
                <BarycentricMapping />
            </Node>
        </Node>
        <Node name="Torus2">
            <Gravity gravity="0 10 0" />
            <EulerImplicitSolver name="cg_odesolver" printLog="false" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject dx="0" dy="-20" dz="0" />
            <UniformMass totalMass="10" />
            <RegularGridTopology nx="6" ny="5" nz="2" xmin="-7.5" xmax="7.5" ymin="-6" ymax="6" zmin="-1.75" zmax="1.75" />
            <RegularGridSpringForceField name="Springs" stiffness="350" damping="1" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_3" filename="mesh/torus2_scale3.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_3" color="blue" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Surf">
                <MeshOBJLoader name="loader" filename="mesh/torus2_scale3.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel />
                <LineCollisionModel />
                <PointCollisionModel />
                <BarycentricMapping />
            </Node>
        </Node>
        <Node name="Floor">
            <MeshOBJLoader name="loader" filename="mesh/floor2b.obj" />
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader" dy="30.25" scale="0.7" rx="180" />
            <TriangleCollisionModel name="FloorTri1" simulated="0" moving="0" />
            <LineCollisionModel name="FloorLine1" simulated="0" moving="0" />
            <PointCollisionModel name="FloorPoint1" simulated="0" moving="0" />
            <MeshOBJLoader name="meshLoader_1" filename="mesh/floor2b.obj" scale="0.5" handleSeams="1" />
            <OglModel name="FloorV" src="@meshLoader_1" texturename="textures/floor.bmp" rx="180" dy="30" material="Default &#x0A;&#x09;&#x09;&#x09;&#x09;  Diffuse 1      0.75 0.75 0.75 0.4 &#x0A;&#x09;&#x09;&#x09;&#x09;  Ambient 1      0.2 0.2 0.2 0.4 &#x0A;&#x09;&#x09;&#x09;&#x09;  Specular 0     1 1 1 1 &#x0A;&#x09;&#x09;&#x09;&#x09;  Emissive 0     0 0 0 0 &#x0A;&#x09;&#x09;&#x09;&#x09;  Shininess 0    45" />
        </Node>
        <Node name="Floor2">
            <MeshOBJLoader name="loader" filename="mesh/floor2b.obj" />
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader" dy="-30.25" scale="0.7" />
            <TriangleCollisionModel name="FloorTri2" simulated="0" moving="0" />
            <LineCollisionModel name="FloorLine2" simulated="0" moving="0" />
            <PointCollisionModel name="FloorPoint2" simulated="0" moving="0" />
            <MeshOBJLoader name="meshLoader_2" filename="mesh/floor2b.obj" scale="0.5" handleSeams="1" />
            <OglModel name="FloorV" src="@meshLoader_2" texturename="textures/floor.bmp" dy="-30" material="Default &#x0A;&#x09;&#x09;&#x09;&#x09;  Diffuse 1      0.75 0.75 0.75 0.4 &#x0A;&#x09;&#x09;&#x09;&#x09;  Ambient 1      0.2 0.2 0.2 0.4 &#x0A;&#x09;&#x09;&#x09;&#x09;  Specular 0     1 1 1 1 &#x0A;&#x09;&#x09;&#x09;&#x09;  Emissive 0     0 0 0 0 &#x0A;&#x09;&#x09;&#x09;&#x09;  Shininess 0    45" />/
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.03333")
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
        root.addObject('RequiredPlugin', name="SofaGraphComponent")
        root.addObject('CollisionPipeline', verbose="0", depth="10", draw="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.75", contactDistance="0.5")
        root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")
        root.addObject('DefaultAnimationLoop')

        Torus1 = root.addChild('Torus1')
        Torus1.addObject('Gravity', gravity="0 -10 0")
        Torus1.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        Torus1.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        Torus1.addObject('MechanicalObject', dx="0", dy="20", dz="0", ry="90")
        Torus1.addObject('UniformMass', totalMass="10")
        Torus1.addObject('RegularGridTopology', nx="6", ny="5", nz="2", xmin="-7.5", xmax="7.5", ymin="-6", ymax="6", zmin="-1.75", zmax="1.75")
        Torus1.addObject('RegularGridSpringForceField', name="Springs", stiffness="350", damping="1")

        Visu = Torus1.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus2_scale3.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="blue")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf = Torus1.addChild('Surf')
        Surf.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_scale3.obj")
        Surf.addObject('MeshTopology', src="@loader")
        Surf.addObject('MechanicalObject', src="@loader")
        Surf.addObject('TriangleCollisionModel')
        Surf.addObject('LineCollisionModel')
        Surf.addObject('PointCollisionModel')
        Surf.addObject('BarycentricMapping')

        Torus2 = root.addChild('Torus2')
        Torus2.addObject('Gravity', gravity="0 10 0")
        Torus2.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        Torus2.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        Torus2.addObject('MechanicalObject', dx="0", dy="-20", dz="0")
        Torus2.addObject('UniformMass', totalMass="10")
        Torus2.addObject('RegularGridTopology', nx="6", ny="5", nz="2", xmin="-7.5", xmax="7.5", ymin="-6", ymax="6", zmin="-1.75", zmax="1.75")
        Torus2.addObject('RegularGridSpringForceField', name="Springs", stiffness="350", damping="1")

        Visu = Torus2.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/torus2_scale3.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_3", color="blue")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf = Torus2.addChild('Surf')
        Surf.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_scale3.obj")
        Surf.addObject('MeshTopology', src="@loader")
        Surf.addObject('MechanicalObject', src="@loader")
        Surf.addObject('TriangleCollisionModel')
        Surf.addObject('LineCollisionModel')
        Surf.addObject('PointCollisionModel')
        Surf.addObject('BarycentricMapping')

        Floor = root.addChild('Floor')
        Floor.addObject('MeshOBJLoader', name="loader", filename="mesh/floor2b.obj")
        Floor.addObject('MeshTopology', src="@loader")
        Floor.addObject('MechanicalObject', src="@loader", dy="30.25", scale="0.7", rx="180")
        Floor.addObject('TriangleCollisionModel', name="FloorTri1", simulated="0", moving="0")
        Floor.addObject('LineCollisionModel', name="FloorLine1", simulated="0", moving="0")
        Floor.addObject('PointCollisionModel', name="FloorPoint1", simulated="0", moving="0")
        Floor.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/floor2b.obj", scale="0.5", handleSeams="1")
        Floor.addObject('OglModel', name="FloorV", src="@meshLoader_1", texturename="textures/floor.bmp", rx="180", dy="30", material="Default 
				  Diffuse 1      0.75 0.75 0.75 0.4 
				  Ambient 1      0.2 0.2 0.2 0.4 
				  Specular 0     1 1 1 1 
				  Emissive 0     0 0 0 0 
				  Shininess 0    45")

        Floor2 = root.addChild('Floor2')
        Floor2.addObject('MeshOBJLoader', name="loader", filename="mesh/floor2b.obj")
        Floor2.addObject('MeshTopology', src="@loader")
        Floor2.addObject('MechanicalObject', src="@loader", dy="-30.25", scale="0.7")
        Floor2.addObject('TriangleCollisionModel', name="FloorTri2", simulated="0", moving="0")
        Floor2.addObject('LineCollisionModel', name="FloorLine2", simulated="0", moving="0")
        Floor2.addObject('PointCollisionModel', name="FloorPoint2", simulated="0", moving="0")
        Floor2.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/floor2b.obj", scale="0.5", handleSeams="1")
        Floor2.addObject('OglModel', name="FloorV", src="@meshLoader_2", texturename="textures/floor.bmp", dy="-30", material="Default 
				  Diffuse 1      0.75 0.75 0.75 0.4 
				  Ambient 1      0.2 0.2 0.2 0.4 
				  Specular 0     1 1 1 1 
				  Emissive 0     0 0 0 0 
				  Shininess 0    45")
    ```

