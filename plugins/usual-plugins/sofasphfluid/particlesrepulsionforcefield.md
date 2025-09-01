<!-- generate_doc -->
# ParticlesRepulsionForceField

ForceField using SpatialGridContainer to compute repulsion forces in a set of spheres.


## Vec2d

Templates:

- Vec2d

__Target__: SofaSphFluid

__namespace__: sofa::component::forcefield

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
		<td>distance</td>
		<td>
Distance to maintain between particles
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>stiffness</td>
		<td>
Stiffness
		</td>
		<td>100</td>
	</tr>
	<tr>
		<td>damping</td>
		<td>
Damping
		</td>
		<td>0.1</td>
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec2d&gt;|

<!-- generate_doc -->
## Vec3d

Templates:

- Vec3d

__Target__: SofaSphFluid

__namespace__: sofa::component::forcefield

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
		<td>distance</td>
		<td>
Distance to maintain between particles
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>stiffness</td>
		<td>
Stiffness
		</td>
		<td>100</td>
	</tr>
	<tr>
		<td>damping</td>
		<td>
Damping
		</td>
		<td>0.1</td>
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

## Examples 

ParticlesRepulsionForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0.0 -2.0 0.0" dt="0.04">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [NewProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [SphereCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping SubsetMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [PlaneForceField SphereForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [MeshSpringForceField QuadBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="SofaSphFluid"/> <!-- Needed to use components [ParticlesRepulsionForceField SpatialGridContainer] -->
    
        <DefaultAnimationLoop/>
        <CollisionPipeline verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="Response" response="PenalityContactForceField"/>
        <NewProximityIntersection alarmDistance="0.002" contactDistance="0.001" />
    
        <Node name="Floor">
            <RegularGridTopology nx="2" ny="1" nz="2" xmin="20" xmax="-20" ymin="-3.05" ymax="-3.05" zmin="-20" zmax="20" />
            <MechanicalObject />
            <Node name="Visu">
                <OglModel name="Visual" color="red" />
                <IdentityMapping input="@.." output="@Visual" />
            </Node>
        </Node>
        
        <Node name="SquareCloth1">
            <EulerImplicitSolver rayleighMass="0.05"  rayleighStiffness="0.1" />
            <CGLinearSolver iterations="10" threshold="0.000001" tolerance="1e-5"/>
            <RegularGridTopology nx="100" ny="1" nz="100" xmin="12" xmax="-12" ymin="7" ymax="7" zmin="-12" zmax="12" />
            <MechanicalObject />
            <UniformMass totalMass="100" />
            <BoxConstraint box="-12 7 12 -10 7 12    10 7 12 12 7 12" />
            <MeshSpringForceField name="Springs" stiffness="1000" damping="0" />
            <QuadBendingSprings name="Bend" stiffness="2000" damping="1" />
            <SphereForceField stiffness="1000" damping="1" center="0 1 3" radius="4" />
            <PlaneForceField stiffness="1000" damping="20" normal="0 1 0" d="-3" />
            <SpatialGridContainer cellWidth="0.2" autoUpdate="false" showGrid="false" />
            <ParticlesRepulsionForceField distance="0.2" stiffness="1000" />
    
            <Node name="Visu">
                <OglModel name="Visual" color="green" />
                <IdentityMapping input="@.." output="@Visual" />
            </Node>
    
            <Node>
                <RegularGridTopology nx="4" ny="1" nz="4" xmin="12" xmax="-12" ymin="7" ymax="7" zmin="-12" zmax="12" />/
                <MechanicalObject />
                <SphereCollisionModel radius="1.0" contactStiffness="1" />
                <SubsetMapping />
            </Node>
        </Node>
    
        <Node name="Sphere">
            <MeshOBJLoader name="meshLoader_0" filename="mesh/sphere.obj" scale="3.95" handleSeams="1" />
            <OglModel name="Visual" src="@meshLoader_0" dx="0" dy="1" dz="3" color="blue" />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0.0 -2.0 0.0", dt="0.04")

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
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('RequiredPlugin', name="SofaSphFluid")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('CollisionPipeline', verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")
       root.addObject('NewProximityIntersection', alarmDistance="0.002", contactDistance="0.001")

       floor = root.addChild('Floor')

       floor.addObject('RegularGridTopology', nx="2", ny="1", nz="2", xmin="20", xmax="-20", ymin="-3.05", ymax="-3.05", zmin="-20", zmax="20")
       floor.addObject('MechanicalObject', )

       visu = Floor.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="red")
       visu.addObject('IdentityMapping', input="@..", output="@Visual")

       square_cloth1 = root.addChild('SquareCloth1')

       square_cloth1.addObject('EulerImplicitSolver', rayleighMass="0.05", rayleighStiffness="0.1")
       square_cloth1.addObject('CGLinearSolver', iterations="10", threshold="0.000001", tolerance="1e-5")
       square_cloth1.addObject('RegularGridTopology', nx="100", ny="1", nz="100", xmin="12", xmax="-12", ymin="7", ymax="7", zmin="-12", zmax="12")
       square_cloth1.addObject('MechanicalObject', )
       square_cloth1.addObject('UniformMass', totalMass="100")
       square_cloth1.addObject('BoxConstraint', box="-12 7 12 -10 7 12    10 7 12 12 7 12")
       square_cloth1.addObject('MeshSpringForceField', name="Springs", stiffness="1000", damping="0")
       square_cloth1.addObject('QuadBendingSprings', name="Bend", stiffness="2000", damping="1")
       square_cloth1.addObject('SphereForceField', stiffness="1000", damping="1", center="0 1 3", radius="4")
       square_cloth1.addObject('PlaneForceField', stiffness="1000", damping="20", normal="0 1 0", d="-3")
       square_cloth1.addObject('SpatialGridContainer', cellWidth="0.2", autoUpdate="false", showGrid="false")
       square_cloth1.addObject('ParticlesRepulsionForceField', distance="0.2", stiffness="1000")

       visu = SquareCloth1.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="green")
       visu.addObject('IdentityMapping', input="@..", output="@Visual")

       node = SquareCloth1.addChild('node')

       node.addObject('RegularGridTopology', nx="4", ny="1", nz="4", xmin="12", xmax="-12", ymin="7", ymax="7", zmin="-12", zmax="12")
       node.addObject('MechanicalObject', )
       node.addObject('SphereCollisionModel', radius="1.0", contactStiffness="1")
       node.addObject('SubsetMapping', )

       sphere = root.addChild('Sphere')

       sphere.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/sphere.obj", scale="3.95", handleSeams="1")
       sphere.addObject('OglModel', name="Visual", src="@meshLoader_0", dx="0", dy="1", dz="3", color="blue")
    ```

