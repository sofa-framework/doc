---
title: ConstantForceField
---

ConstantForceField
==================

This component belongs to the category of [ForceField](https://www.sofa-framework.org/community/doc/simulation-principles/multi-model-representation/forcefield/). The ConstantForceField is a simple force field applying the same constant force on each node. This force field is not integrated over the domain of our object, but simply distributed over the number of nodes.


<a href="https://github.com/sofa-framework/doc/blob/master/images/FEM/ConstantForceField.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/FEM/ConstantForceField.png?raw=true" title="Nodal constant force over a liver mesh" style="width: 50%;text-align: center; "/></a>



Data  
----

- **indices**: list of node indices where the forces are applied and distributed
- **force**: single value corresponding to the constant force applied on each node
- **totalForce**: single value corresponding to total force for all points, i.e. the sum of the forces distributed uniformly over the nodes
- **forces**: vector containing the force amplitude applied at each node


Usage
-----

As a Forcefield, the ConstantForceField requires a **MechanicalObject** and the associated **solvers** (integration scheme and linear solver), as well as a **PointSetTopologyContainer**.


Example
-------

This component is used as follows in XML format:

``` xml
<ConstantForceField indices="0 1 2" forces="-1 -1 0   1 -1 0   1 1 0" />
```

or using SofaPython3:

``` python
node.addObject('ConstantForceField', indices=[0 1 2], forces=[[-1 -1 0] [1 -1 0] [1 1 0]])
```

With a description of each data

An example scene involving a ConstantForceField is available in [*examples/Component/MechanicalLoad/ConstantForceField.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/MechanicalLoad/ConstantForceField.scn)
<!-- automatically generated doc START -->
__Target__: `Sofa.Component.MechanicalLoad`

__namespace__: `#!c++ sofa::component::mechanicalload`

__parents__: 

- `#!c++ ForceField`

__categories__: 

- ForceField

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
		<td>indices</td>
		<td>
indices where the forces are applied
</td>
		<td></td>
	</tr>
	<tr>
		<td>indexFromEnd</td>
		<td>
Concerned DOFs indices are numbered from the end of the MState DOFs vector. (default=false)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Force info</td>
	</tr>
	<tr>
		<td>forces</td>
		<td>
vector containing the force amplitude applied at each node
</td>
		<td></td>
	</tr>
	<tr>
		<td>totalForce</td>
		<td>
total force for all points, will be distributed uniformly over points
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showArrowSize</td>
		<td>
Size of the drawn arrows (0-&gt;no arrows, sign-&gt;direction of drawing. (default=0)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showColor</td>
		<td>
Color for object display (default: [0.2,0.9,0.3,1.0])
</td>
		<td>0.2 0.9 0.3 1</td>
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
|mstate|MechanicalState used by this component|
|topology|link to the topology container|



## Examples

Component/MechanicalLoad/ConstantForceField.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.05" gravity="0 0 0">
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [ConstantForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangleFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [InteractiveCamera VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <!-- Constant force for a deformable -->
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <DefaultAnimationLoop computeBoundingBox="false"/>
        <InteractiveCamera position="1.27 0.48 4.5" orientation="0 0 0 1"  distance="3.86" fieldOfView="45"/>
        
        <Node name="BasicDeformableObject" >
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject position="0 0 0  1 0 0  1 1 0  0 1 0" velocity="0 0 0  0 0 0  0 0 0  0 0 0" />
            <UniformMass vertexMass="0.1" />
            <MeshTopology triangles="0 1 2  0 2 3" />
            <!--		<FixedProjectiveConstraint indices="2 3"/>-->
            <TriangleFEMForceField name="FEM0" youngModulus="100" poissonRatio="0.3" method="large" />
            <ConstantForceField indices="0 1 2 3" forces="-1 -1 0  1 -1 0  1 1 0  -1 1 0" showArrowSize="0.5" printLog="1"/>
            <Node name="Visu">
                <OglModel name="Visual" color="red" />
                <IdentityMapping input="@.." output="@Visual" />
            </Node>
        </Node>
        <Node name="TorusRigid">
            <EulerImplicitSolver rayleighStiffness="0.01" />
            <CGLinearSolver iterations="25" threshold="0.00000001" tolerance="1e-5"/>
            <MechanicalObject template="Rigid3" dx="2" dy="0" dz="0" rx="0" ry="0" rz="0" scale="1.0" />
            <UniformMass />
            <!-- forces for a rigid is composed of two parts translation of the rigid dof [x y z] and a quaternion for the rotation [x y z w] -->
            <ConstantForceField indices="0" forces="0 0.10 0     0 1 0" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/torus.obj" scale="0.3" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_0" color="gray" />
                <RigidMapping input="@.." output="@Visual" />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.05", gravity="0 0 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
        root.addObject('DefaultAnimationLoop', computeBoundingBox="false")
        root.addObject('InteractiveCamera', position="1.27 0.48 4.5", orientation="0 0 0 1", distance="3.86", fieldOfView="45")

        BasicDeformableObject = root.addChild('BasicDeformableObject')
        BasicDeformableObject.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighMass="0.1")
        BasicDeformableObject.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        BasicDeformableObject.addObject('MechanicalObject', position="0 0 0  1 0 0  1 1 0  0 1 0", velocity="0 0 0  0 0 0  0 0 0  0 0 0")
        BasicDeformableObject.addObject('UniformMass', vertexMass="0.1")
        BasicDeformableObject.addObject('MeshTopology', triangles="0 1 2  0 2 3")
        BasicDeformableObject.addObject('TriangleFEMForceField', name="FEM0", youngModulus="100", poissonRatio="0.3", method="large")
        BasicDeformableObject.addObject('ConstantForceField', indices="0 1 2 3", forces="-1 -1 0  1 -1 0  1 1 0  -1 1 0", showArrowSize="0.5", printLog="1")

        Visu = BasicDeformableObject.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="red")
        Visu.addObject('IdentityMapping', input="@..", output="@Visual")

        TorusRigid = root.addChild('TorusRigid')
        TorusRigid.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
        TorusRigid.addObject('CGLinearSolver', iterations="25", threshold="0.00000001", tolerance="1e-5")
        TorusRigid.addObject('MechanicalObject', template="Rigid3", dx="2", dy="0", dz="0", rx="0", ry="0", rz="0", scale="1.0")
        TorusRigid.addObject('UniformMass')
        TorusRigid.addObject('ConstantForceField', indices="0", forces="0 0.10 0     0 1 0")

        Visu = TorusRigid.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", scale="0.3", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="gray")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")
    ```


<!-- automatically generated doc END -->
