<!-- generate_doc -->
# MeshSpringForceField

Spring force field acting along the edges of a mesh.


## Vec1d

Templates:

- Vec1d

__Target__: Sofa.Component.SolidMechanics.Spring

__namespace__: sofa::component::solidmechanics::spring

__parents__:

- SpringForceField

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
		<td>lengths</td>
		<td>
List of lengths to create the springs. Must have the same than indices1 & indices2, or if only one element, it will be applied to all springs. If empty, 0 will be applied everywhere
		</td>
		<td></td>
	</tr>
	<tr>
		<td>elongationOnly</td>
		<td>
///< List of boolean stating on the fact that the spring should only apply forces on elongations. Must have the same than indices1 & indices2, or if only one element, it will be applied to all springs. If empty, False will be applied everywhere
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>enabled</td>
		<td>
///< List of boolean stating on the fact that the spring is enabled. Must have the same than indices1 & indices2, or if only one element, it will be applied to all springs. If empty, True will be applied everywhere
		</td>
		<td>1</td>
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
optional range of local DOF indices. Any computation involving only indices outside of this range are discarded (useful for parallelization using mesh partitioning)
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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|object1|First object associated to this component|MechanicalState&lt;Vec1d&gt;|
|object2|Second object associated to this component|MechanicalState&lt;Vec1d&gt;|
|topology|link to the topology container|BaseMeshTopology|

<!-- generate_doc -->
## Vec2d

Templates:

- Vec2d

__Target__: Sofa.Component.SolidMechanics.Spring

__namespace__: sofa::component::solidmechanics::spring

__parents__:

- SpringForceField

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
		<td>lengths</td>
		<td>
List of lengths to create the springs. Must have the same than indices1 & indices2, or if only one element, it will be applied to all springs. If empty, 0 will be applied everywhere
		</td>
		<td></td>
	</tr>
	<tr>
		<td>elongationOnly</td>
		<td>
///< List of boolean stating on the fact that the spring should only apply forces on elongations. Must have the same than indices1 & indices2, or if only one element, it will be applied to all springs. If empty, False will be applied everywhere
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>enabled</td>
		<td>
///< List of boolean stating on the fact that the spring is enabled. Must have the same than indices1 & indices2, or if only one element, it will be applied to all springs. If empty, True will be applied everywhere
		</td>
		<td>1</td>
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
optional range of local DOF indices. Any computation involving only indices outside of this range are discarded (useful for parallelization using mesh partitioning)
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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|object1|First object associated to this component|MechanicalState&lt;Vec2d&gt;|
|object2|Second object associated to this component|MechanicalState&lt;Vec2d&gt;|
|topology|link to the topology container|BaseMeshTopology|

<!-- generate_doc -->
## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.SolidMechanics.Spring

__namespace__: sofa::component::solidmechanics::spring

__parents__:

- SpringForceField

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
		<td>lengths</td>
		<td>
List of lengths to create the springs. Must have the same than indices1 & indices2, or if only one element, it will be applied to all springs. If empty, 0 will be applied everywhere
		</td>
		<td></td>
	</tr>
	<tr>
		<td>elongationOnly</td>
		<td>
///< List of boolean stating on the fact that the spring should only apply forces on elongations. Must have the same than indices1 & indices2, or if only one element, it will be applied to all springs. If empty, False will be applied everywhere
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>enabled</td>
		<td>
///< List of boolean stating on the fact that the spring is enabled. Must have the same than indices1 & indices2, or if only one element, it will be applied to all springs. If empty, True will be applied everywhere
		</td>
		<td>1</td>
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
optional range of local DOF indices. Any computation involving only indices outside of this range are discarded (useful for parallelization using mesh partitioning)
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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|object1|First object associated to this component|MechanicalState&lt;Vec3d&gt;|
|object2|Second object associated to this component|MechanicalState&lt;Vec3d&gt;|
|topology|link to the topology container|BaseMeshTopology|

## Examples 

MeshSpringForceField.scn

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
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 -9 0")

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
       root.addObject('DefaultAnimationLoop', )
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('NewProximityIntersection', name="Proximity", alarmDistance="0.5", contactDistance="0.2")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       chain_spring = root.addChild('ChainSpring')

       torus_fixed = ChainSpring.addChild('TorusFixed')

       torus_fixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       torus_fixed.addObject('MeshTopology', src="@loader")
       torus_fixed.addObject('MechanicalObject', src="@loader")
       torus_fixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/torus2.obj", handleSeams="1")
       torus_fixed.addObject('OglModel', name="Visual", src="@meshLoader_3", color="gray")

       torus_spring1 = ChainSpring.addChild('TorusSpring1')

       torus_spring1.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       torus_spring1.addObject('CGLinearSolver', iterations="100", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       torus_spring1.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh", translation="2.5 0 0")
       torus_spring1.addObject('MeshTopology', src="@loader")
       torus_spring1.addObject('MechanicalObject', src="@loader")
       torus_spring1.addObject('UniformMass', totalMass="5")
       torus_spring1.addObject('MeshSpringForceField', name="Springs", tetrasStiffness="1000", tetrasDamping="0")

       visu1 = TorusSpring1.addChild('Visu1')

       visu1.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", translation="2.5 0 0", handleSeams="1")
       visu1.addObject('OglModel', name="Visual", src="@meshLoader_0", color="green")
       visu1.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf1 = TorusSpring1.addChild('Surf1')

       surf1.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj", translation="2.5 0 0")
       surf1.addObject('MeshTopology', src="@loader")
       surf1.addObject('MechanicalObject', src="@loader")
       surf1.addObject('TriangleCollisionModel', )
       surf1.addObject('BarycentricMapping', )

       torus_spring2 = ChainSpring.addChild('TorusSpring2')

       torus_spring2.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       torus_spring2.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       torus_spring2.addObject('MeshGmshLoader', name="loader", filename="mesh/torus2_low_res.msh", translation="5 0 0")
       torus_spring2.addObject('MeshTopology', src="@loader")
       torus_spring2.addObject('MechanicalObject', src="@loader")
       torus_spring2.addObject('UniformMass', totalMass="5")
       torus_spring2.addObject('MeshSpringForceField', name="Springs", tetrasStiffness="200", tetrasDamping="0")

       visu2 = TorusSpring2.addChild('Visu2')

       visu2.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/torus2.obj", translation="5 0 0", handleSeams="1")
       visu2.addObject('OglModel', name="Visual", src="@meshLoader_2", color="blue")
       visu2.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusSpring2.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj", translation="5 0 0")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       torus_spring3 = ChainSpring.addChild('TorusSpring3')

       torus_spring3.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       torus_spring3.addObject('CGLinearSolver', iterations="100", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       torus_spring3.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh", translation="7.5 0 0")
       torus_spring3.addObject('MeshTopology', src="@loader")
       torus_spring3.addObject('MechanicalObject', src="@loader")
       torus_spring3.addObject('UniformMass', totalMass="0.5")
       torus_spring3.addObject('MeshSpringForceField', name="Springs", tetrasStiffness="400", tetrasDamping="0")

       visu3 = TorusSpring3.addChild('Visu3')

       visu3.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/torus.obj", translation="7.5 0 0", handleSeams="1")
       visu3.addObject('OglModel', name="Visual", src="@meshLoader_1", color="green")
       visu3.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf3 = TorusSpring3.addChild('Surf3')

       surf3.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj", translation="7.5 0 0")
       surf3.addObject('MeshTopology', src="@loader")
       surf3.addObject('MechanicalObject', src="@loader")
       surf3.addObject('TriangleCollisionModel', )
       surf3.addObject('BarycentricMapping', )

       torus_spring4 = ChainSpring.addChild('TorusSpring4')

       torus_spring4.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       torus_spring4.addObject('CGLinearSolver', iterations="100", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       torus_spring4.addObject('MeshGmshLoader', name="loader", filename="mesh/torus2_low_res.msh", translation="10 0 0")
       torus_spring4.addObject('MeshTopology', src="@loader")
       torus_spring4.addObject('MechanicalObject', src="@loader")
       torus_spring4.addObject('UniformMass', totalMass="0.5")
       torus_spring4.addObject('MeshSpringForceField', name="Springs", tetrasStiffness="400", tetrasDamping="0")

       visu4 = TorusSpring4.addChild('Visu4')

       visu4.addObject('MeshOBJLoader', name="meshLoader_4", filename="mesh/torus2.obj", translation="10 0 0", handleSeams="1")
       visu4.addObject('OglModel', name="Visual", src="@meshLoader_4", color="red")
       visu4.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf4 = TorusSpring4.addChild('Surf4')

       surf4.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj", translation="10 0 0")
       surf4.addObject('MeshTopology', src="@loader")
       surf4.addObject('MechanicalObject', src="@loader")
       surf4.addObject('TriangleCollisionModel', )
       surf4.addObject('BarycentricMapping', )
    ```

MeshSpringForceField_beam10x10x40_cpu.scn

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
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 -9 0")

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
       root.addObject('DefaultAnimationLoop', )
       root.addObject('DefaultVisualManagerLoop', )
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.5", contactDistance="0.3")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       beam = root.addChild('Beam')

       beam.addObject('RegularGridTopology', name="grid", n="40 10 10", min="0 6 -2", max="16 10 2")
       beam.addObject('TetrahedronSetTopologyContainer', name="BeamTopo")
       beam.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       beam.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@BeamTopo")

       mesh_spring_force_field__cpu__red = root.addChild('MeshSpringForceField-CPU-Red')

       mesh_spring_force_field__cpu__red.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="0")
       mesh_spring_force_field__cpu__red.addObject('CGLinearSolver', name="linear solver", iterations="20", tolerance="1e-06", threshold="1e-06")
       mesh_spring_force_field__cpu__red.addObject('MechanicalObject', position="@../Beam/grid.position", name="Volume", template="Vec3")
       mesh_spring_force_field__cpu__red.addObject('TetrahedronSetTopologyContainer', name="Container", src="@../Beam/BeamTopo")
       mesh_spring_force_field__cpu__red.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       mesh_spring_force_field__cpu__red.addObject('BoxROI', name="ROI1", box="-0.1 5 -3 0.1 11 3", drawBoxes="1")
       mesh_spring_force_field__cpu__red.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")
       mesh_spring_force_field__cpu__red.addObject('UniformMass', totalMass="100")
       mesh_spring_force_field__cpu__red.addObject('MeshSpringForceField', name="Springs", tetrasStiffness="1200", tetrasDamping="0", template="Vec3")

       mesh_visu = MeshSpringForceField-CPU-Red.addChild('MeshVisu')

       mesh_visu.addObject('OglModel', name="Visual", topology="@../Container", position="@../Volume.position", color="red")
       mesh_visu.addObject('IdentityMapping', input="@../Volume", output="@Visual")
    ```

MeshSpringForceField_beam10x10x40_gpu.scn

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
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 -9 0")

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
       root.addObject('DefaultAnimationLoop', )
       root.addObject('DefaultVisualManagerLoop', )
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.5", contactDistance="0.3")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       beam = root.addChild('Beam')

       beam.addObject('RegularGridTopology', name="grid", n="40 10 10", min="0 6 -2", max="16 10 2")
       beam.addObject('TetrahedronSetTopologyContainer', name="BeamTopo")
       beam.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       beam.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@BeamTopo")

       mesh_spring_force_field__gpu__green = root.addChild('MeshSpringForceField-GPU-Green')

       mesh_spring_force_field__gpu__green.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="0")
       mesh_spring_force_field__gpu__green.addObject('CGLinearSolver', name="linear solver", iterations="20", tolerance="1e-06", threshold="1e-06")
       mesh_spring_force_field__gpu__green.addObject('MechanicalObject', position="@../Beam/grid.position", name="Volume", template="CudaVec3f")
       mesh_spring_force_field__gpu__green.addObject('TetrahedronSetTopologyContainer', name="Container", src="@../Beam/BeamTopo")
       mesh_spring_force_field__gpu__green.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       mesh_spring_force_field__gpu__green.addObject('BoxROI', name="ROI1", box="-0.1 5 -3 0.1 11 3", drawBoxes="1")
       mesh_spring_force_field__gpu__green.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")
       mesh_spring_force_field__gpu__green.addObject('UniformMass', totalMass="100")
       mesh_spring_force_field__gpu__green.addObject('MeshSpringForceField', name="Springs", tetrasStiffness="1200", tetrasDamping="0", template="CudaVec3f")

       mesh_visu = MeshSpringForceField-GPU-Green.addChild('MeshVisu')

       mesh_visu.addObject('OglModel', name="Visual", topology="@../Container", position="@../Volume.position", color="green")
       mesh_visu.addObject('IdentityMapping', input="@../Volume", output="@Visual")
    ```

