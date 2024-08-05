# GearSpringForceField

Gear springs for Rigids


__Templates__:

- `#!c++ Rigid3d`

__Target__: `Sofa.Component.SolidMechanics.Spring`

__namespace__: `#!c++ sofa::component::solidmechanics::spring`

__parents__: 

- `#!c++ PairInteractionForceField`

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
		<td>spring</td>
		<td>
pairs of indices, stiffness, damping
</td>
		<td></td>
	</tr>
	<tr>
		<td>filename</td>
		<td>
output file name
</td>
		<td></td>
	</tr>
	<tr>
		<td>period</td>
		<td>
period between outputs
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>reinit</td>
		<td>
flag enabling reinitialization of the output file at each timestep
</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showFactorSize</td>
		<td>
modify the size of the debug information of a given factor
</td>
		<td>1</td>
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

Component/SolidMechanics/Spring/GearSpringForceField.scn

=== "XML"

    ```xml
    <Node name="root" gravity="0 0 0" dt="0.01" time="0">
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [GearSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showVisual" />
        <EulerImplicitSolver name="cg_odesolver" printLog="0" rayleighStiffness="0.1" rayleighMass="0.1" />
        <CGLinearSolver name="linear solver" iterations="50" tolerance="1e-009" threshold="1e-009" />
        <MechanicalObject template="Rigid3" name="DOFs" rest_position="0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 1" position="-1.161 0 1.706 0 0.194787 0 0.980846 &#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;-6.7 4 1.706 0 0 0.707107 0.707107 &#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;1.790 0 -5.503 0 0.229019 0 0.973422&#x09;&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;-6.7 5.2 -3.5 0 0 0.707107 0.707107&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;0 0 0 0 0 0 1" restScale="1" />
        <UniformMass name="mass" vertexMass="50 50 [1 0 0,0 1 0,0 0 1]" showAxisSizeFactor="2" />
        <FixedProjectiveConstraint template="Rigid3" name="fixOrigin" indices="4" />
        <!--  	SELF SUPPORT 	 -->
        <!--
    		<GearSpringForceField template="Rigid3" name="gear1"  showFactorSize='5' spring="BEGIN_SPRING  0 0 2 2 AXIS 1 1 KS_T 2000000  KS_R 2000000 2000000 KD 1 RATIO 2 END_SPRING" />
    		<GearSpringForceField template="Rigid3" name="gear2"  showFactorSize='5' spring="BEGIN_SPRING  0 0 1 1 AXIS 1 1 KS_T 2000000  KS_R 2000000 2000000 KD 1 RATIO -1.5385 END_SPRING" />
    		<GearSpringForceField template="Rigid3" name="gear3"  showFactorSize='5' spring="BEGIN_SPRING  1 1 3 3 AXIS 1 1 KS_T 2000000  KS_R 2000000 2000000 KD 1 RATIO 2.166667 END_SPRING" />
     -->
        <!--  	EXTERNAL SUPPORT -->
        <Node name="Gear">
            <MechanicalObject template="Rigid3" name="attaches" rest_position="0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 1 -1.161 0 1.706 0 0.194787 0 0.980846 -6.7 4 1.706 0 0 0.707107 0.707107 1.790 0 -5.503 0 0.229019 0 0.973422 -6.7 5.2 -3.5 0 0 0.707107 0.707107" restScale="1" />
            <RigidMapping template="Rigid3,Rigid3" input="@.." output="@." rigidIndexPerPoint="1 1 1 1 4" />
            <GearSpringForceField template="Rigid3" name="springs" showFactorSize="5" spring="BEGIN_SPRING  4 0 6 2 AXIS 1 1 KS_T 2000000  KS_R 2000000 2000000 KD 1 RATIO 2 END_SPRING&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;  BEGIN_SPRING  4 0 5 1 AXIS 1 1 KS_T 2000000  KS_R 2000000 2000000 KD 1 RATIO -1.5385 END_SPRING&#x0A;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;&#x09;  BEGIN_SPRING  5 1 7 3 AXIS 1 1 KS_T 2000000  KS_R 2000000 2000000 KD 1 RATIO 2.166667 END_SPRING" />
        </Node>
        <Node name="0">
            <MeshOBJLoader name="MeshLoader" filename="mesh/gear0.obj" />
            <MeshTopology src="@MeshLoader" />
            <MechanicalObject name="PointSet" />
            <TriangleCollisionModel />
            <RigidMapping template="Rigid3,Vec3" index="0" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_1" filename="mesh/gear0.obj" handleSeams="1" />
                <OglModel template="Vec3" name="Visual" src="@meshLoader_1" />
                <IdentityMapping template="Vec3,Vec3" input="@.." output="@Visual" />
            </Node>
        </Node>
        <Node name="1">
            <MeshOBJLoader name="MeshLoader" filename="mesh/gear1.obj" />
            <MeshTopology src="@MeshLoader" />
            <MechanicalObject name="PointSet" />
            <TriangleCollisionModel />
            <RigidMapping template="Rigid3,Vec3" index="1" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_3" filename="mesh/gear1.obj" handleSeams="1" />
                <OglModel template="Vec3" name="Visual" src="@meshLoader_3" />
                <IdentityMapping template="Vec3,Vec3" input="@.." output="@Visual" />
            </Node>
        </Node>
        <Node name="2">
            <MeshOBJLoader name="MeshLoader" filename="mesh/gear2.obj" />
            <MeshTopology src="@MeshLoader" />
            <MechanicalObject name="PointSet" />
            <TriangleCollisionModel />
            <RigidMapping template="Rigid3,Vec3" index="2" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/gear2.obj" handleSeams="1" />
                <OglModel template="Vec3" name="Visual" src="@meshLoader_0" />
                <IdentityMapping template="Vec3,Vec3" input="@.." output="@Visual" />
            </Node>
        </Node>
        <Node name="3">
            <MeshOBJLoader name="MeshLoader" filename="mesh/gear3.obj" />
            <MeshTopology src="@MeshLoader" />
            <MechanicalObject name="PointSet" />
            <TriangleCollisionModel />
            <RigidMapping template="Rigid3,Vec3" index="3" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_2" filename="mesh/gear3.obj" handleSeams="1" />
                <OglModel template="Vec3" name="Visual" src="@meshLoader_2" />
                <IdentityMapping template="Vec3,Vec3" input="@.." output="@Visual" />
            </Node>
        </Node>
        <Node name="support">
            <MeshOBJLoader name="MeshLoader" filename="mesh/gearsupport.obj" />
            <MeshTopology src="@MeshLoader" />
            <MechanicalObject name="PointSet" />
            <TriangleCollisionModel />
            <RigidMapping template="Rigid3,Vec3" index="4" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_4" filename="mesh/gearsupport.obj" handleSeams="1" />
                <OglModel template="Vec3" name="Visual" src="@meshLoader_4" material="Default Diffuse 1 1 1 0.8 1 Ambient 1 0.2 0.2 0.2 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45" />
                <IdentityMapping template="Vec3,Vec3" input="@.." output="@Visual" />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 0 0", dt="0.01", time="0")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')
        root.addObject('VisualStyle', displayFlags="showVisual")
        root.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="0", rayleighStiffness="0.1", rayleighMass="0.1")
        root.addObject('CGLinearSolver', name="linear solver", iterations="50", tolerance="1e-009", threshold="1e-009")
        root.addObject('MechanicalObject', template="Rigid3", name="DOFs", rest_position="0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 1", position="-1.161 0 1.706 0 0.194787 0 0.980846 
																																			-6.7 4 1.706 0 0 0.707107 0.707107 
																																			1.790 0 -5.503 0 0.229019 0 0.973422	
																																			-6.7 5.2 -3.5 0 0 0.707107 0.707107
																																			0 0 0 0 0 0 1", restScale="1")
        root.addObject('UniformMass', name="mass", vertexMass="50 50 [1 0 0,0 1 0,0 0 1]", showAxisSizeFactor="2")
        root.addObject('FixedProjectiveConstraint', template="Rigid3", name="fixOrigin", indices="4")

        Gear = root.addChild('Gear')
        Gear.addObject('MechanicalObject', template="Rigid3", name="attaches", rest_position="0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 1 -1.161 0 1.706 0 0.194787 0 0.980846 -6.7 4 1.706 0 0 0.707107 0.707107 1.790 0 -5.503 0 0.229019 0 0.973422 -6.7 5.2 -3.5 0 0 0.707107 0.707107", restScale="1")
        Gear.addObject('RigidMapping', template="Rigid3,Rigid3", input="@..", output="@.", rigidIndexPerPoint="1 1 1 1 4")
        Gear.addObject('GearSpringForceField', template="Rigid3", name="springs", showFactorSize="5", spring="BEGIN_SPRING  4 0 6 2 AXIS 1 1 KS_T 2000000  KS_R 2000000 2000000 KD 1 RATIO 2 END_SPRING
																							  BEGIN_SPRING  4 0 5 1 AXIS 1 1 KS_T 2000000  KS_R 2000000 2000000 KD 1 RATIO -1.5385 END_SPRING
																							  BEGIN_SPRING  5 1 7 3 AXIS 1 1 KS_T 2000000  KS_R 2000000 2000000 KD 1 RATIO 2.166667 END_SPRING")

        0 = root.addChild('0')
        0.addObject('MeshOBJLoader', name="MeshLoader", filename="mesh/gear0.obj")
        0.addObject('MeshTopology', src="@MeshLoader")
        0.addObject('MechanicalObject', name="PointSet")
        0.addObject('TriangleCollisionModel')
        0.addObject('RigidMapping', template="Rigid3,Vec3", index="0")

        Visu = 0.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/gear0.obj", handleSeams="1")
        Visu.addObject('OglModel', template="Vec3", name="Visual", src="@meshLoader_1")
        Visu.addObject('IdentityMapping', template="Vec3,Vec3", input="@..", output="@Visual")

        1 = root.addChild('1')
        1.addObject('MeshOBJLoader', name="MeshLoader", filename="mesh/gear1.obj")
        1.addObject('MeshTopology', src="@MeshLoader")
        1.addObject('MechanicalObject', name="PointSet")
        1.addObject('TriangleCollisionModel')
        1.addObject('RigidMapping', template="Rigid3,Vec3", index="1")

        Visu = 1.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/gear1.obj", handleSeams="1")
        Visu.addObject('OglModel', template="Vec3", name="Visual", src="@meshLoader_3")
        Visu.addObject('IdentityMapping', template="Vec3,Vec3", input="@..", output="@Visual")

        2 = root.addChild('2')
        2.addObject('MeshOBJLoader', name="MeshLoader", filename="mesh/gear2.obj")
        2.addObject('MeshTopology', src="@MeshLoader")
        2.addObject('MechanicalObject', name="PointSet")
        2.addObject('TriangleCollisionModel')
        2.addObject('RigidMapping', template="Rigid3,Vec3", index="2")

        Visu = 2.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/gear2.obj", handleSeams="1")
        Visu.addObject('OglModel', template="Vec3", name="Visual", src="@meshLoader_0")
        Visu.addObject('IdentityMapping', template="Vec3,Vec3", input="@..", output="@Visual")

        3 = root.addChild('3')
        3.addObject('MeshOBJLoader', name="MeshLoader", filename="mesh/gear3.obj")
        3.addObject('MeshTopology', src="@MeshLoader")
        3.addObject('MechanicalObject', name="PointSet")
        3.addObject('TriangleCollisionModel')
        3.addObject('RigidMapping', template="Rigid3,Vec3", index="3")

        Visu = 3.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/gear3.obj", handleSeams="1")
        Visu.addObject('OglModel', template="Vec3", name="Visual", src="@meshLoader_2")
        Visu.addObject('IdentityMapping', template="Vec3,Vec3", input="@..", output="@Visual")

        support = root.addChild('support')
        support.addObject('MeshOBJLoader', name="MeshLoader", filename="mesh/gearsupport.obj")
        support.addObject('MeshTopology', src="@MeshLoader")
        support.addObject('MechanicalObject', name="PointSet")
        support.addObject('TriangleCollisionModel')
        support.addObject('RigidMapping', template="Rigid3,Vec3", index="4")

        Visu = support.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_4", filename="mesh/gearsupport.obj", handleSeams="1")
        Visu.addObject('OglModel', template="Vec3", name="Visual", src="@meshLoader_4", material="Default Diffuse 1 1 1 0.8 1 Ambient 1 0.2 0.2 0.2 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45")
        Visu.addObject('IdentityMapping', template="Vec3,Vec3", input="@..", output="@Visual")
    ```

