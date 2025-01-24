<!-- generate_doc -->
# Gravity

Gravity in world coordinates.


__Target__: Sofa.Component.MechanicalLoad

__namespace__: sofa::component::mechanicalload

__parents__:

- ContextObject

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
		<td>gravity</td>
		<td>
Gravity in the world coordinate system
		</td>
		<td>0 0 0</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|

## Examples 

Gravity.scn

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
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [Gravity] -->
    
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
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.03333")

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
       root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
       root.addObject('CollisionPipeline', verbose="0", depth="10", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.75", contactDistance="0.5")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")
       root.addObject('DefaultAnimationLoop', )

       torus1 = root.addChild('Torus1')

       torus1.addObject('Gravity', gravity="0 -10 0")
       torus1.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       torus1.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       torus1.addObject('MechanicalObject', dx="0", dy="20", dz="0", ry="90")
       torus1.addObject('UniformMass', totalMass="10")
       torus1.addObject('RegularGridTopology', nx="6", ny="5", nz="2", xmin="-7.5", xmax="7.5", ymin="-6", ymax="6", zmin="-1.75", zmax="1.75")
       torus1.addObject('RegularGridSpringForceField', name="Springs", stiffness="350", damping="1")

       visu = Torus1.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus2_scale3.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="blue")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf = Torus1.addChild('Surf')

       surf.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_scale3.obj")
       surf.addObject('MeshTopology', src="@loader")
       surf.addObject('MechanicalObject', src="@loader")
       surf.addObject('TriangleCollisionModel', )
       surf.addObject('LineCollisionModel', )
       surf.addObject('PointCollisionModel', )
       surf.addObject('BarycentricMapping', )

       torus2 = root.addChild('Torus2')

       torus2.addObject('Gravity', gravity="0 10 0")
       torus2.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       torus2.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       torus2.addObject('MechanicalObject', dx="0", dy="-20", dz="0")
       torus2.addObject('UniformMass', totalMass="10")
       torus2.addObject('RegularGridTopology', nx="6", ny="5", nz="2", xmin="-7.5", xmax="7.5", ymin="-6", ymax="6", zmin="-1.75", zmax="1.75")
       torus2.addObject('RegularGridSpringForceField', name="Springs", stiffness="350", damping="1")

       visu = Torus2.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/torus2_scale3.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_3", color="blue")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf = Torus2.addChild('Surf')

       surf.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_scale3.obj")
       surf.addObject('MeshTopology', src="@loader")
       surf.addObject('MechanicalObject', src="@loader")
       surf.addObject('TriangleCollisionModel', )
       surf.addObject('LineCollisionModel', )
       surf.addObject('PointCollisionModel', )
       surf.addObject('BarycentricMapping', )

       floor = root.addChild('Floor')

       floor.addObject('MeshOBJLoader', name="loader", filename="mesh/floor2b.obj")
       floor.addObject('MeshTopology', src="@loader")
       floor.addObject('MechanicalObject', src="@loader", dy="30.25", scale="0.7", rx="180")
       floor.addObject('TriangleCollisionModel', name="FloorTri1", simulated="0", moving="0")
       floor.addObject('LineCollisionModel', name="FloorLine1", simulated="0", moving="0")
       floor.addObject('PointCollisionModel', name="FloorPoint1", simulated="0", moving="0")
       floor.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/floor2b.obj", scale="0.5", handleSeams="1")
       floor.addObject('OglModel', name="FloorV", src="@meshLoader_1", texturename="textures/floor.bmp", rx="180", dy="30", material="Default 
				  Diffuse 1      0.75 0.75 0.75 0.4 
				  Ambient 1      0.2 0.2 0.2 0.4 
				  Specular 0     1 1 1 1 
				  Emissive 0     0 0 0 0 
				  Shininess 0    45")

       floor2 = root.addChild('Floor2')

       floor2.addObject('MeshOBJLoader', name="loader", filename="mesh/floor2b.obj")
       floor2.addObject('MeshTopology', src="@loader")
       floor2.addObject('MechanicalObject', src="@loader", dy="-30.25", scale="0.7")
       floor2.addObject('TriangleCollisionModel', name="FloorTri2", simulated="0", moving="0")
       floor2.addObject('LineCollisionModel', name="FloorLine2", simulated="0", moving="0")
       floor2.addObject('PointCollisionModel', name="FloorPoint2", simulated="0", moving="0")
       floor2.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/floor2b.obj", scale="0.5", handleSeams="1")
       floor2.addObject('OglModel', name="FloorV", src="@meshLoader_2", texturename="textures/floor.bmp", dy="-30", material="Default 
				  Diffuse 1      0.75 0.75 0.75 0.4 
				  Ambient 1      0.2 0.2 0.2 0.4 
				  Specular 0     1 1 1 1 
				  Emissive 0     0 0 0 0 
				  Shininess 0    45")
    ```

