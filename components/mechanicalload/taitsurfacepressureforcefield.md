<!-- generate_doc -->
# TaitSurfacePressureForceField

This component computes the volume enclosed by a surface mesh and apply a pressure force following Tait's equation: $P = P_0 - B((V/V_0)^\gamma - 1)$.
This ForceField can be used to apply :
 * a constant pressure (set $B=0$ and use $P_0$)
 * an ideal gas pressure (set $\gamma=1$ and use $B$)
 * a pressure from water (set $\gamma=7$ and use $B$)


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
		<td>pressureTriangles</td>
		<td>
OUT: list of triangles where a pressure is applied (mesh triangles + tessellated quads)
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Controls</td>
	</tr>
	<tr>
		<td>p0</td>
		<td>
IN: Rest pressure when V = V0
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>B</td>
		<td>
IN: Bulk modulus (resistance to uniform compression)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>gamma</td>
		<td>
IN: Bulk modulus (resistance to uniform compression)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>injectedVolume</td>
		<td>
IN: Injected (or extracted) volume since the start of the simulation
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>maxInjectionRate</td>
		<td>
IN: Maximum injection rate (volume per second)
		</td>
		<td>1000</td>
	</tr>
	<tr>
		<td colspan="3">Results</td>
	</tr>
	<tr>
		<td>initialVolume</td>
		<td>
OUT: Initial volume, as computed from the surface rest position
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>currentInjectedVolume</td>
		<td>
OUT: Current injected (or extracted) volume (taking into account maxInjectionRate)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>v0</td>
		<td>
OUT: Rest volume (as computed from initialVolume + injectedVolume)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>currentVolume</td>
		<td>
OUT: Current volume, as computed from the last surface position
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>currentPressure</td>
		<td>
OUT: Current pressure, as computed from the last surface position
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>currentStiffness</td>
		<td>
OUT: dP/dV at current volume and pressure
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>volumeAfterTC</td>
		<td>
OUT: Volume after a topology change
		</td>
		<td></td>
	</tr>
	<tr>
		<td>surfaceAreaAfterTC</td>
		<td>
OUT: Surface area after a topology change
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Stats</td>
	</tr>
	<tr>
		<td>initialSurfaceArea</td>
		<td>
OUT: Initial surface area, as computed from the surface rest position
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>currentSurfaceArea</td>
		<td>
OUT: Current surface area, as computed from the last surface position
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawForceScale</td>
		<td>
DEBUG: scale used to render force vectors
		</td>
		<td>0.001</td>
	</tr>
	<tr>
		<td>drawForceColor</td>
		<td>
DEBUG: color used to render force vectors
		</td>
		<td>0 1 1 1</td>
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

TaitSurfacePressureForceField.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.02" gravity = "0 0 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [TaitSurfacePressureForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangularFEMForceFieldOptim] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [FastTriangularBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <DefaultAnimationLoop/>
        <CollisionPipeline verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <DiscreteIntersection />
        <Node name="sphere">
            <EulerImplicitSolver name="cg_odesolver" rayleighMass="0.1" rayleighStiffness="0.2" printLog="false" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshOBJLoader name="loader" filename="mesh/sphere_02b.obj" scale="0.25 0.25 0.25" rotation="-90 0 0" triangulate="1" />
            <TriangleSetTopologyContainer src="@loader" />
            <MechanicalObject src="@loader" template="Vec3" name="DOFs" />
            <TriangleSetTopologyModifier />
            <TriangleSetGeometryAlgorithms />
            <BoxConstraint box="-10 -10 -10  10 -5 10" />
            <TriangularFEMForceFieldOptim name="FEM" youngModulus="10000" poissonRatio="0.4" restScale="0.97" method="large" />
            <FastTriangularBendingSprings name="Bending" bendingStiffness="100" />
            <TaitSurfacePressureForceField name="Pressure" gamma="5" B="10000" injectedVolume="100" printLog="1" />
            <DiagonalMass name="mass" massDensity="1" printLog="0" />
            <TriangleCollisionModel name="CM" />
    
            <Node name="Visu">
                <OglModel name="VisualModel" src="@../loader" color="white" />
                <IdentityMapping />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02", gravity="0 0 0")

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
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('CollisionPipeline', verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', response="PenalityContactForceField")
       root.addObject('DiscreteIntersection', )

       sphere = root.addChild('sphere')

       sphere.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighMass="0.1", rayleighStiffness="0.2", printLog="false")
       sphere.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       sphere.addObject('MeshOBJLoader', name="loader", filename="mesh/sphere_02b.obj", scale="0.25 0.25 0.25", rotation="-90 0 0", triangulate="1")
       sphere.addObject('TriangleSetTopologyContainer', src="@loader")
       sphere.addObject('MechanicalObject', src="@loader", template="Vec3", name="DOFs")
       sphere.addObject('TriangleSetTopologyModifier', )
       sphere.addObject('TriangleSetGeometryAlgorithms', )
       sphere.addObject('BoxConstraint', box="-10 -10 -10  10 -5 10")
       sphere.addObject('TriangularFEMForceFieldOptim', name="FEM", youngModulus="10000", poissonRatio="0.4", restScale="0.97", method="large")
       sphere.addObject('FastTriangularBendingSprings', name="Bending", bendingStiffness="100")
       sphere.addObject('TaitSurfacePressureForceField', name="Pressure", gamma="5", B="10000", injectedVolume="100", printLog="1")
       sphere.addObject('DiagonalMass', name="mass", massDensity="1", printLog="0")
       sphere.addObject('TriangleCollisionModel', name="CM")

       visu = sphere.addChild('Visu')

       visu.addObject('OglModel', name="VisualModel", src="@../loader", color="white")
       visu.addObject('IdentityMapping', )
    ```

