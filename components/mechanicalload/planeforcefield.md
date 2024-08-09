<!-- generate_doc -->
# PlaneForceField

Repulsion applied by a plane toward the exterior (half-space)


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
		<td>normal</td>
		<td>
plane normal. (default=[0,1,0])
		</td>
		<td></td>
	</tr>
	<tr>
		<td>d</td>
		<td>
plane d coef. (default=0)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>stiffness</td>
		<td>
force stiffness. (default=500)
		</td>
		<td>500</td>
	</tr>
	<tr>
		<td>damping</td>
		<td>
force damping. (default=5)
		</td>
		<td>5</td>
	</tr>
	<tr>
		<td>maxForce</td>
		<td>
if non-null , the max force that can be applied to the object. (default=0)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>bilateral</td>
		<td>
if true the plane force field is applied on both sides. (default=false)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>localRange</td>
		<td>
optional range of local DOF indices. Any computation involving indices outside of this range are discarded (useful for parallelization using mesh partitionning)
		</td>
		<td>-1 -1</td>
	</tr>
	<tr>
		<td>planeColor</td>
		<td>
plane color. (default=[0.0,0.5,0.2,1.0])
		</td>
		<td>0 0.5 0.2 1</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showPlane</td>
		<td>
enable/disable drawing of plane. (default=false)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showPlaneSize</td>
		<td>
plane display size if draw is enabled. (default=10)
		</td>
		<td>10</td>
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

<!-- generate_doc -->
## Vec1d

Templates:

- Vec1d

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
		<td>normal</td>
		<td>
plane normal. (default=[0,1,0])
		</td>
		<td></td>
	</tr>
	<tr>
		<td>d</td>
		<td>
plane d coef. (default=0)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>stiffness</td>
		<td>
force stiffness. (default=500)
		</td>
		<td>500</td>
	</tr>
	<tr>
		<td>damping</td>
		<td>
force damping. (default=5)
		</td>
		<td>5</td>
	</tr>
	<tr>
		<td>maxForce</td>
		<td>
if non-null , the max force that can be applied to the object. (default=0)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>bilateral</td>
		<td>
if true the plane force field is applied on both sides. (default=false)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>localRange</td>
		<td>
optional range of local DOF indices. Any computation involving indices outside of this range are discarded (useful for parallelization using mesh partitionning)
		</td>
		<td>-1 -1</td>
	</tr>
	<tr>
		<td>planeColor</td>
		<td>
plane color. (default=[0.0,0.5,0.2,1.0])
		</td>
		<td>0 0.5 0.2 1</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showPlane</td>
		<td>
enable/disable drawing of plane. (default=false)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showPlaneSize</td>
		<td>
plane display size if draw is enabled. (default=10)
		</td>
		<td>10</td>
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec1d&gt;|

<!-- generate_doc -->
## Vec2d

Templates:

- Vec2d

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
		<td>normal</td>
		<td>
plane normal. (default=[0,1,0])
		</td>
		<td></td>
	</tr>
	<tr>
		<td>d</td>
		<td>
plane d coef. (default=0)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>stiffness</td>
		<td>
force stiffness. (default=500)
		</td>
		<td>500</td>
	</tr>
	<tr>
		<td>damping</td>
		<td>
force damping. (default=5)
		</td>
		<td>5</td>
	</tr>
	<tr>
		<td>maxForce</td>
		<td>
if non-null , the max force that can be applied to the object. (default=0)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>bilateral</td>
		<td>
if true the plane force field is applied on both sides. (default=false)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>localRange</td>
		<td>
optional range of local DOF indices. Any computation involving indices outside of this range are discarded (useful for parallelization using mesh partitionning)
		</td>
		<td>-1 -1</td>
	</tr>
	<tr>
		<td>planeColor</td>
		<td>
plane color. (default=[0.0,0.5,0.2,1.0])
		</td>
		<td>0 0.5 0.2 1</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showPlane</td>
		<td>
enable/disable drawing of plane. (default=false)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showPlaneSize</td>
		<td>
plane display size if draw is enabled. (default=10)
		</td>
		<td>10</td>
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
		<td>normal</td>
		<td>
plane normal. (default=[0,1,0])
		</td>
		<td></td>
	</tr>
	<tr>
		<td>d</td>
		<td>
plane d coef. (default=0)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>stiffness</td>
		<td>
force stiffness. (default=500)
		</td>
		<td>500</td>
	</tr>
	<tr>
		<td>damping</td>
		<td>
force damping. (default=5)
		</td>
		<td>5</td>
	</tr>
	<tr>
		<td>maxForce</td>
		<td>
if non-null , the max force that can be applied to the object. (default=0)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>bilateral</td>
		<td>
if true the plane force field is applied on both sides. (default=false)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>localRange</td>
		<td>
optional range of local DOF indices. Any computation involving indices outside of this range are discarded (useful for parallelization using mesh partitionning)
		</td>
		<td>-1 -1</td>
	</tr>
	<tr>
		<td>planeColor</td>
		<td>
plane color. (default=[0.0,0.5,0.2,1.0])
		</td>
		<td>0 0.5 0.2 1</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showPlane</td>
		<td>
enable/disable drawing of plane. (default=false)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showPlaneSize</td>
		<td>
plane display size if draw is enabled. (default=10)
		</td>
		<td>10</td>
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

<!-- generate_doc -->
## Vec6d

Templates:

- Vec6d

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
		<td>normal</td>
		<td>
plane normal. (default=[0,1,0])
		</td>
		<td></td>
	</tr>
	<tr>
		<td>d</td>
		<td>
plane d coef. (default=0)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>stiffness</td>
		<td>
force stiffness. (default=500)
		</td>
		<td>500</td>
	</tr>
	<tr>
		<td>damping</td>
		<td>
force damping. (default=5)
		</td>
		<td>5</td>
	</tr>
	<tr>
		<td>maxForce</td>
		<td>
if non-null , the max force that can be applied to the object. (default=0)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>bilateral</td>
		<td>
if true the plane force field is applied on both sides. (default=false)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>localRange</td>
		<td>
optional range of local DOF indices. Any computation involving indices outside of this range are discarded (useful for parallelization using mesh partitionning)
		</td>
		<td>-1 -1</td>
	</tr>
	<tr>
		<td>planeColor</td>
		<td>
plane color. (default=[0.0,0.5,0.2,1.0])
		</td>
		<td>0 0.5 0.2 1</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showPlane</td>
		<td>
enable/disable drawing of plane. (default=false)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showPlaneSize</td>
		<td>
plane display size if draw is enabled. (default=10)
		</td>
		<td>10</td>
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec6d&gt;|

## Examples 

PlaneForceField.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.01">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [NewProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [PlaneForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [RegularGridSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <NewProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="M1">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject />
            <UniformMass totalMass="10" />
            <RegularGridTopology nx="2" ny="2" nz="2" xmin="-3.5" xmax="3.5" ymin="-3.5" ymax="3.5" zmin="-3.5" zmax="3.5" />
            <RegularGridSpringForceField name="Springs" stiffness="1000" />
            <PlaneForceField normal="0 1 0" d="-10" stiffness="100000" showPlane="1" showPlaneSize="20"/>
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/smCube125.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_0" color="blue" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Collis">
                <MeshOBJLoader name="loader" filename="mesh/smCube125.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel />
                <BarycentricMapping input="@.." output="@Collis" />
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
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('NewProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       m1 = root.addChild('M1')

       m1.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       m1.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       m1.addObject('MechanicalObject', )
       m1.addObject('UniformMass', totalMass="10")
       m1.addObject('RegularGridTopology', nx="2", ny="2", nz="2", xmin="-3.5", xmax="3.5", ymin="-3.5", ymax="3.5", zmin="-3.5", zmax="3.5")
       m1.addObject('RegularGridSpringForceField', name="Springs", stiffness="1000")
       m1.addObject('PlaneForceField', normal="0 1 0", d="-10", stiffness="100000", showPlane="1", showPlaneSize="20")

       visu = M1.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/smCube125.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="blue")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       collis = M1.addChild('Collis')

       collis.addObject('MeshOBJLoader', name="loader", filename="mesh/smCube125.obj")
       collis.addObject('MeshTopology', src="@loader")
       collis.addObject('MechanicalObject', src="@loader")
       collis.addObject('TriangleCollisionModel', )
       collis.addObject('BarycentricMapping', input="@..", output="@Collis")
    ```

