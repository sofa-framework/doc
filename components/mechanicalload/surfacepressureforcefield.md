<!-- generate_doc -->
# SurfacePressureForceField

Pressure applied on a generic surface (triangular or quadrangular).


## Rigid3d

Templates:

- Rigid3d

__Target__: Sofa.Component.MechanicalLoad

__namespace__: sofa::component::mechanicalload

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
		<td>pressure</td>
		<td>
Pressure force per unit area
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>min</td>
		<td>
Lower bound of the selection box
		</td>
		<td>0 0 0 0 0 0 1</td>
	</tr>
	<tr>
		<td>max</td>
		<td>
Upper bound of the selection box
		</td>
		<td>0 0 0 0 0 0 1</td>
	</tr>
	<tr>
		<td>triangleIndices</td>
		<td>
Indices of affected triangles
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quadIndices</td>
		<td>
Indices of affected quads
		</td>
		<td></td>
	</tr>
	<tr>
		<td>pulseMode</td>
		<td>
Cyclic pressure application
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>pressureLowerBound</td>
		<td>
Pressure lower bound force per unit area (active in pulse mode)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>pressureSpeed</td>
		<td>
Continuous pressure application in Pascal per second. Only active in pulse mode
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>volumeConservationMode</td>
		<td>
Pressure variation follow the inverse of the volume variation
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>useTangentStiffness</td>
		<td>
Whether (non-symmetric) stiffness matrix should be used
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>defaultVolume</td>
		<td>
Default Volume
		</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>mainDirection</td>
		<td>
Main direction for pressure application
		</td>
		<td>0 0 0 0 0 0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawForceScale</td>
		<td>
DEBUG: scale used to render force vectors
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
|topology|link to the topology container|BaseMeshTopology|

<!-- generate_doc -->
## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.MechanicalLoad

__namespace__: sofa::component::mechanicalload

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
		<td>pressure</td>
		<td>
Pressure force per unit area
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>min</td>
		<td>
Lower bound of the selection box
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>max</td>
		<td>
Upper bound of the selection box
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>triangleIndices</td>
		<td>
Indices of affected triangles
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quadIndices</td>
		<td>
Indices of affected quads
		</td>
		<td></td>
	</tr>
	<tr>
		<td>pulseMode</td>
		<td>
Cyclic pressure application
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>pressureLowerBound</td>
		<td>
Pressure lower bound force per unit area (active in pulse mode)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>pressureSpeed</td>
		<td>
Continuous pressure application in Pascal per second. Only active in pulse mode
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>volumeConservationMode</td>
		<td>
Pressure variation follow the inverse of the volume variation
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>useTangentStiffness</td>
		<td>
Whether (non-symmetric) stiffness matrix should be used
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>defaultVolume</td>
		<td>
Default Volume
		</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>mainDirection</td>
		<td>
Main direction for pressure application
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawForceScale</td>
		<td>
DEBUG: scale used to render force vectors
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
|topology|link to the topology container|BaseMeshTopology|

## Examples 

SurfacePressureForceField.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.01">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [SurfacePressureForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [MeshSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [SparseGridTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        
        <DefaultAnimationLoop/>
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" usePointPoint="1" alarmDistance="3.5" contactDistance="1.5" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="Frog">
            <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="30" tolerance="1e-5" threshold="1e-5"/>
            <SparseGridTopology n="10 5 10" fileTopology="mesh/frog.obj" />
            <MechanicalObject dx="-10.0" />
            <UniformMass vertexMass="1.0" />
            <BoxConstraint box="-18.0 2.0 -5.0 -2.0 3.0 5.0" />
            <MeshSpringForceField name="Springs" stiffness="50000" damping="4" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/frog.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_0" color="0.5 1.0 0.5 1.0" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
            <Node name="TriangleSurf">
                <MeshOBJLoader name="loader" filename="mesh/frog.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel group="1" />
                <LineCollisionModel group="1" />
                <PointCollisionModel group="1" />
                <SurfacePressureForceField pressure="50000.0" pulseMode="true" pressureSpeed="20000.0" />
                <BarycentricMapping input="@.." output="@." />
            </Node>
        </Node>
        <Node name="Frog2">
            <EulerImplicitSolver />
            <CGLinearSolver iterations="30" tolerance="1e-5" threshold="1e-5"/>
            <SparseGridTopology n="10 5 10" fileTopology="mesh/frog_quads.obj" />
            <MechanicalObject dx="10.0" />
            <UniformMass vertexMass="1.0" />
            <BoxConstraint box="2.0 2.0 -5.0 18.0 3.0 5.0" />
            <MeshSpringForceField name="Springs" stiffness="50000" damping="4" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_1" filename="mesh/frog_quads.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_1" color="1.0 0.5 0.5 1.0" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
            <Node name="QuadSurf">
                <MeshOBJLoader name="loader" filename="mesh/frog_quads.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel group="1" />
                <LineCollisionModel group="1" />
                <PointCollisionModel group="1" />
                <SurfacePressureForceField pressure="50000.0" pulseMode="true" pressureSpeed="20000.0" />
                <BarycentricMapping input="@.." output="@." />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01")

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
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('MinProximityIntersection', name="Proximity", usePointPoint="1", alarmDistance="3.5", contactDistance="1.5")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       frog = root.addChild('Frog')

       frog.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
       frog.addObject('CGLinearSolver', iterations="30", tolerance="1e-5", threshold="1e-5")
       frog.addObject('SparseGridTopology', n="10 5 10", fileTopology="mesh/frog.obj")
       frog.addObject('MechanicalObject', dx="-10.0")
       frog.addObject('UniformMass', vertexMass="1.0")
       frog.addObject('BoxConstraint', box="-18.0 2.0 -5.0 -2.0 3.0 5.0")
       frog.addObject('MeshSpringForceField', name="Springs", stiffness="50000", damping="4")

       visu = Frog.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/frog.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="0.5 1.0 0.5 1.0")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       triangle_surf = Frog.addChild('TriangleSurf')

       triangle_surf.addObject('MeshOBJLoader', name="loader", filename="mesh/frog.obj")
       triangle_surf.addObject('MeshTopology', src="@loader")
       triangle_surf.addObject('MechanicalObject', src="@loader")
       triangle_surf.addObject('TriangleCollisionModel', group="1")
       triangle_surf.addObject('LineCollisionModel', group="1")
       triangle_surf.addObject('PointCollisionModel', group="1")
       triangle_surf.addObject('SurfacePressureForceField', pressure="50000.0", pulseMode="true", pressureSpeed="20000.0")
       triangle_surf.addObject('BarycentricMapping', input="@..", output="@.")

       frog2 = root.addChild('Frog2')

       frog2.addObject('EulerImplicitSolver', )
       frog2.addObject('CGLinearSolver', iterations="30", tolerance="1e-5", threshold="1e-5")
       frog2.addObject('SparseGridTopology', n="10 5 10", fileTopology="mesh/frog_quads.obj")
       frog2.addObject('MechanicalObject', dx="10.0")
       frog2.addObject('UniformMass', vertexMass="1.0")
       frog2.addObject('BoxConstraint', box="2.0 2.0 -5.0 18.0 3.0 5.0")
       frog2.addObject('MeshSpringForceField', name="Springs", stiffness="50000", damping="4")

       visu = Frog2.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/frog_quads.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="1.0 0.5 0.5 1.0")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       quad_surf = Frog2.addChild('QuadSurf')

       quad_surf.addObject('MeshOBJLoader', name="loader", filename="mesh/frog_quads.obj")
       quad_surf.addObject('MeshTopology', src="@loader")
       quad_surf.addObject('MechanicalObject', src="@loader")
       quad_surf.addObject('TriangleCollisionModel', group="1")
       quad_surf.addObject('LineCollisionModel', group="1")
       quad_surf.addObject('PointCollisionModel', group="1")
       quad_surf.addObject('SurfacePressureForceField', pressure="50000.0", pulseMode="true", pressureSpeed="20000.0")
       quad_surf.addObject('BarycentricMapping', input="@..", output="@.")
    ```

