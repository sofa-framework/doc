---
title: ConstantForceField
---

ConstantForceField
==================

This component belongs to the category of [ForceField](../../simulation-principles/multi-model-representation/forcefield/). The ConstantForceField is a simple force field applying the same constant force on each node. This force field is not integrated over the domain of our object, but simply distributed over the number of nodes.


<a href="https://github.com/sofa-framework/doc/blob/master/images/FEM/ConstantForceField.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/FEM/ConstantForceField.png?raw=true" title="Nodal constant force over a liver mesh" style="width: 50%;text-align: center; "/></a>



Usage
-----

As a Forcefield, the ConstantForceField requires a **MechanicalObject** and the associated **solvers** (integration scheme and linear solver), as well as a **PointSetTopologyContainer**.
<!-- automatically generated doc START -->
<!-- generate_doc -->

Constant forces applied to given degrees of freedom


## Rigid2d

Templates:

- Rigid2d

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
Size of the drawn arrows (0->no arrows, sign->direction of drawing. (default=0)
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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Rigid2d&gt;|
|topology|link to the topology container|BaseMeshTopology|

<!-- generate_doc -->
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
Size of the drawn arrows (0->no arrows, sign->direction of drawing. (default=0)
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
Size of the drawn arrows (0->no arrows, sign->direction of drawing. (default=0)
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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec1d&gt;|
|topology|link to the topology container|BaseMeshTopology|

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
Size of the drawn arrows (0->no arrows, sign->direction of drawing. (default=0)
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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec2d&gt;|
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
Size of the drawn arrows (0->no arrows, sign->direction of drawing. (default=0)
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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|
|topology|link to the topology container|BaseMeshTopology|

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
Size of the drawn arrows (0->no arrows, sign->direction of drawing. (default=0)
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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec6d&gt;|
|topology|link to the topology container|BaseMeshTopology|

## Examples 

ConstantForceField.scn

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
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.05", gravity="0 0 0")

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

       basic_deformable_object = root.addChild('BasicDeformableObject')

       basic_deformable_object.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighMass="0.1")
       basic_deformable_object.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       basic_deformable_object.addObject('MechanicalObject', position="0 0 0  1 0 0  1 1 0  0 1 0", velocity="0 0 0  0 0 0  0 0 0  0 0 0")
       basic_deformable_object.addObject('UniformMass', vertexMass="0.1")
       basic_deformable_object.addObject('MeshTopology', triangles="0 1 2  0 2 3")
       basic_deformable_object.addObject('TriangleFEMForceField', name="FEM0", youngModulus="100", poissonRatio="0.3", method="large")
       basic_deformable_object.addObject('ConstantForceField', indices="0 1 2 3", forces="-1 -1 0  1 -1 0  1 1 0  -1 1 0", showArrowSize="0.5", printLog="1")

       visu = BasicDeformableObject.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="red")
       visu.addObject('IdentityMapping', input="@..", output="@Visual")

       torus_rigid = root.addChild('TorusRigid')

       torus_rigid.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
       torus_rigid.addObject('CGLinearSolver', iterations="25", threshold="0.00000001", tolerance="1e-5")
       torus_rigid.addObject('MechanicalObject', template="Rigid3", dx="2", dy="0", dz="0", rx="0", ry="0", rz="0", scale="1.0")
       torus_rigid.addObject('UniformMass', )
       torus_rigid.addObject('ConstantForceField', indices="0", forces="0 0.10 0     0 1 0")

       visu = TorusRigid.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", scale="0.3", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="gray")
       visu.addObject('RigidMapping', input="@..", output="@Visual")
    ```


<!-- automatically generated doc END -->
