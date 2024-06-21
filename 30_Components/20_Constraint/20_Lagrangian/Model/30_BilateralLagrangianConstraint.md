---
title: BilateralLagrangianConstraint
---

BilateralLagrangianConstraint
==============================

This component belongs to the category of [Constraint Laws](https://www.sofa-framework.org/community/doc/simulation-principles/constraint/lagrange-constraint/#constraint-laws) used for the Lagrange constraint resolution and inherits from the PairInteractionConstraint. The BilateralLagrangianConstraint defines an [holonomic constraint](https://en.wikipedia.org/wiki/Holonomic_constraints) law between a pair of simulated body, i.e. the constraint defined between the pair of objects must have an equality form:

<img class="latex" src="https://latex.codecogs.com/png.latex?\Phi(x_1,x_2%20...)~=~0" title="Holonomic constraint law" />

Such a constraint is suited for attachment cases or sliding joints. For an attachment case, if the vertex _i_ of object 1 and the vertex _j_ of object 2 are attached, the holonomic constraint law can be written as <img class="latex" src="https://latex.codecogs.com/png.latex?x_1(i)-x_2(j)~=~0" title="Attachment law" />.

For a BilateralLagrangianConstraint, the constraint matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{H}" title="Constraint matrix" /> (derivative of the constraint law) corresponds to:

- <img src="https://latex.codecogs.com/gif.latex?\begin{equation*}&space;&\mathbf{H}_1&space;=&space;\begin{bmatrix}&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_0&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;1&space;&&space;0&space;&&space;0\\\end{bmatrix}_i&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_{N_1}\\&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_0&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;0&space;&&space;1&space;&&space;0\\\end{bmatrix}_i&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_{N_1}\\&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_0&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;1\\\end{bmatrix}_i&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_{N_1}\\&space;\end{bmatrix}&space;\end{equation*}" title="\begin{equation*} &\mathbf{H}_1 = \begin{bmatrix} \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 & \hdots & \begin{bmatrix} 1 & 0 & 0\\\end{bmatrix}_i & \hdots & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_1}\\ \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 & \hdots & \begin{bmatrix} 0 & 1 & 0\\\end{bmatrix}_i & \hdots & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_1}\\ \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 & \hdots & \begin{bmatrix} 0 & 0 & 1\\\end{bmatrix}_i & \hdots & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_1}\\ \end{bmatrix} \end{equation*}" /> for object 1
- <img src="https://latex.codecogs.com/gif.latex?\begin{equation*}&space;&\mathbf{H}_2&space;=&space;\begin{bmatrix}&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_0&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;-1&space;&&space;0&space;&&space;0\\\end{bmatrix}_j&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_{N_2}\\&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_0&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;0&space;&&space;-1&space;&&space;0\\\end{bmatrix}_j&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_{N_2}\\&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_0&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;-1\\\end{bmatrix}_j&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_{N_2}\\&space;\end{bmatrix}&space;\end{equation*}" title="\begin{equation*} &\mathbf{H}_2 = \begin{bmatrix} \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 & \hdots & \begin{bmatrix} -1 & 0 & 0\\\end{bmatrix}_j & \hdots & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_2}\\ \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 & \hdots & \begin{bmatrix} 0 & -1 & 0\\\end{bmatrix}_j & \hdots & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_2}\\ \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 & \hdots & \begin{bmatrix} 0 & 0 & -1\\\end{bmatrix}_j & \hdots & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_2}\\ \end{bmatrix} \end{equation*}" /> for object 2


As all constraint laws, the BilateralLagrangianConstraint will be called in the following functions and for the following steps:

- `getConstraintViolation()`: project the free velocity in the constraint space and compute the free interpenetration <img src="https://latex.codecogs.com/gif.latex?\begin{equation}&space;&\dot{\delta}_1^{free}=\mathbf{H}_1v_1^{free}&space;\end{equation}" title="\begin{equation} &\dot{\delta}_1^{free}=\mathbf{H}_1v_1^{free} \end{equation}" />
- `buildConstraintMatrix()`: build the compliance made up of <img class="latex" src="https://latex.codecogs.com/png.latex?dt\mathbf{H}_1\mathbf{A}_1^{-1}\mathbf{H}_1^T" title="Compliance of object 1" /> and <img class="latex" src="https://latex.codecogs.com/png.latex?dt\mathbf{H}_2\mathbf{A}_2^{-1}\mathbf{H}_2^T" title="Compliance of object 2" />



Data  
----

As a PairInteractionConstraint, the BilateralLagrangianConstraint requires the following Data:

- **object1**: link towards the object 1 to constraint
- **object2**: link towards the object 2 to constraint
- **first_point**: index of the constraint on the first model (object 1)
- **second_point**: index of the constraint on the second model (object 2)


Usage
-----

The BilateralLagrangianConstraint can only be used in the context of [Lagrange constraint](https://www.sofa-framework.org/community/doc/simulation-principles/constraint/lagrange-constraint/) resolution. The scene must therefore contain:

- a FreeMotionAnimationLoop
- a ConstraintSolver

Moreover, each constrained object must define in its node a ConstraintCorrection so that the corrective motion can be applied.


Example
-------

This component is used as follows in XML format:

``` xml
<BilateralLagrangianConstraint template="Vec3d" object1="@CUBE_2/Constraints/points" object2="@CUBE_4/Constraints/points" first_point="1" second_point="0" />
```

or using SofaPython3:

``` python
node.addObject('BilateralLagrangianConstraint', template='Vec3d' object1='@CUBE_2/Constraints/points' object2='@CUBE_4/Constraints/points' first_point='1' second_point='0')
```

An example scene involving a BilateralLagrangianConstraint is available in [*examples/Component/Constraint/Lagrangian/BilateralLagrangianConstraint_PGS.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/Constraint/Lagrangian/BilateralLagrangianConstraint_PGS.scn)
<!-- automatically generated doc START -->
__Target__: `Sofa.Component.Constraint.Lagrangian.Model`

__namespace__: `#!c++ sofa::component::constraint::lagrangian::model`

__parents__: 

- `#!c++ PairInteractionConstraint`

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
		<td>group</td>
		<td>
ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>constraintIndex</td>
		<td>
Constraint index (first index in the right hand term resolution vector)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>endTime</td>
		<td>
The constraint stops acting after the given value.
Use a negative value for infinite constraints
</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>first_point</td>
		<td>
index of the constraint on the first model (object1)
</td>
		<td></td>
	</tr>
	<tr>
		<td>second_point</td>
		<td>
index of the constraint on the second model (object2)
</td>
		<td></td>
	</tr>
	<tr>
		<td>rest_vector</td>
		<td>
Relative position to maintain between attached points (optional)
</td>
		<td></td>
	</tr>
	<tr>
		<td>numericalTolerance</td>
		<td>
a real value specifying the tolerance during the constraint solving. (optional, default=0.0001)
</td>
		<td>0.0001</td>
	</tr>
	<tr>
		<td>activate</td>
		<td>
control constraint activation (true by default)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>keepOrientationDifference</td>
		<td>
keep the initial difference in orientation (only for rigids)
</td>
		<td>0</td>
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
|topology1|link to the first topology container|
|topology2|link to the second topology container|



## Examples

Component/Constraint/Lagrangian/BilateralLagrangianConstraint_NNCG.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <!-- BilateralInteractionLagrangianConstraint example -->
    <Node name="root" dt="0.001" gravity="0 -981 0">
        <RequiredPlugin name="Sofa.Component.AnimationLoop"/> <!-- Needed to use components [FreeMotionAnimationLoop] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [LocalMinDistance] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [UncoupledConstraintCorrection] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Model"/> <!-- Needed to use components [BilateralLagrangianConstraint] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Solver"/> <!-- Needed to use components [GenericConstraintSolver] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        
        <VisualStyle displayFlags="showForceFields" />
        <DefaultVisualManagerLoop />
        <FreeMotionAnimationLoop />
        <GenericConstraintSolver tolerance="0.001" maxIterations="1000" resolutionMethod="NonsmoothNonlinearConjugateGradient" newtonIterations="100"/>
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <LocalMinDistance name="Proximity" alarmDistance="0.2" contactDistance="0.09" angleCone="0.0" />
        <CollisionResponse name="Response" response="FrictionContactConstraint" />
    
        <Node name="CUBE_0">
            <MechanicalObject dy="2.5" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/cube.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_0" color="1 0 0 1" dy="2.5" />
            </Node>
            <Node name="ColliCube">
                <MeshOBJLoader name="loader" filename="mesh/cube.obj" triangulate="1" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" template="Vec3" dy="2.5" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <LineCollisionModel simulated="0" moving="0" />
                <PointCollisionModel simulated="0" moving="0" />
            </Node>
            <Node name="Constraints">
                <MechanicalObject name="points" template="Vec3" position="1 1.25 1" />
            </Node>
        </Node>
        <Node name="CUBE_1">
            <EulerImplicitSolver printLog="false" rayleighStiffness="0.1" rayleighMass="0.1"/>
            <CGLinearSolver iterations="25" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject template="Rigid3" scale="1.0" dx="0.0" dy="0" dz="0.0" />
            <UniformMass totalMass="0.1" />
            <UncoupledConstraintCorrection />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_2" filename="mesh/cube.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_2" color="1 1 0 1.0" />
                <RigidMapping input="@.." output="@Visual" />
            </Node>
            <Node name="ColliCube">
                <MeshOBJLoader name="loader" filename="mesh/cube.obj" triangulate="1" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel contactStiffness="10.0" />
                <LineCollisionModel contactStiffness="10.0" />
                <PointCollisionModel contactStiffness="10.0" />
                <RigidMapping />
            </Node>
            <Node name="Constraints">
                <MechanicalObject name="points" template="Vec3" position="1 1.25 1&#x09;-1.25 -1.25 1.25" />
                <RigidMapping />
            </Node>
        </Node>
        <BilateralLagrangianConstraint template="Vec3" object1="@CUBE_0/Constraints/points" object2="@CUBE_1/Constraints/points" first_point="0" second_point="0" />
        <Node name="CUBE_2">
            <EulerImplicitSolver printLog="false" rayleighStiffness="0.1" rayleighMass="0.1"/>
            <CGLinearSolver iterations="25" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject template="Rigid3" scale="1.0" dx="0.0" dy="-2.5" dz="0.0" />
            <UniformMass totalMass="0.1" />
            <UncoupledConstraintCorrection />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_3" filename="mesh/cube.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_3" color="0 1 0 1.0" />
                <RigidMapping input="@.." output="@Visual" />
            </Node>
            <Node name="ColliCube">
                <MeshOBJLoader name="loader" filename="mesh/cube.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" scale="1.0" />
                <TriangleCollisionModel />
                <LineCollisionModel />
                <PointCollisionModel />
                <RigidMapping />
            </Node>
            <Node name="Constraints">
                <MechanicalObject name="points" template="Vec3" position="-1.25 1.25 1.25&#x09;1.25 -1.25 -1.25" />
                <RigidMapping />
            </Node>
        </Node>
        <BilateralLagrangianConstraint template="Vec3" object1="@CUBE_1/Constraints/points" object2="@CUBE_2/Constraints/points" first_point="1" second_point="0" />
        <Node name="CUBE_3">
            <EulerImplicitSolver printLog="false" rayleighStiffness="0.1" rayleighMass="0.1"/>
            <CGLinearSolver iterations="25" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject template="Rigid3" scale="1.0" dx="0.0" dy="-5.0" dz="0.0" />
            <UniformMass totalMass="0.1" />
            <UncoupledConstraintCorrection />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_4" filename="mesh/cube.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_4" color="0 1 1 1.0" />
                <RigidMapping input="@.." output="@Visual" />
            </Node>
            <Node name="ColliCube">
                <MeshOBJLoader name="loader" filename="mesh/cube.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" scale="1.0" />
                <TriangleCollisionModel />
                <LineCollisionModel />
                <PointCollisionModel />
                <RigidMapping />
            </Node>
            <Node name="Constraints">
                <MechanicalObject name="points" template="Vec3" position="1.25 1.25 -1.25" />
                <RigidMapping />
            </Node>
        </Node>
        <BilateralLagrangianConstraint template="Vec3" object1="@CUBE_2/Constraints/points" object2="@CUBE_3/Constraints/points" first_point="1" second_point="0" />
        <Node name="CUBE_4">
            <EulerImplicitSolver printLog="false" rayleighStiffness="0.1" rayleighMass="0.1"/>
            <CGLinearSolver iterations="25" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject template="Rigid3" scale="1.0" dx="0.0" dy="-2.5" dz="-2.5" />
            <UniformMass totalMass="0.1" />
            <UncoupledConstraintCorrection />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_1" filename="mesh/cube.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_1" color="0 0 1 1.0" />
                <RigidMapping input="@.." output="@Visual" />
            </Node>
            <Node name="ColliCube">
                <MeshOBJLoader name="loader" filename="mesh/cube.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" scale="1.0" />
                <TriangleCollisionModel />
                <LineCollisionModel />
                <PointCollisionModel />
                <RigidMapping />
            </Node>
            <Node name="Constraints">
                <MechanicalObject name="points" template="Vec3" position="1.25 -1.25 1.25&#x09;1.25 1.25 1.25" />
                <RigidMapping />
            </Node>
        </Node>
        <BilateralLagrangianConstraint template="Vec3" object1="@CUBE_2/Constraints/points" object2="@CUBE_4/Constraints/points" first_point="1" second_point="0" />
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.001", gravity="0 -981 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.AnimationLoop")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Model")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Solver")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showForceFields")
        root.addObject('DefaultVisualManagerLoop')
        root.addObject('FreeMotionAnimationLoop')
        root.addObject('GenericConstraintSolver', tolerance="0.001", maxIterations="1000", resolutionMethod="NonsmoothNonlinearConjugateGradient", newtonIterations="100")
        root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('LocalMinDistance', name="Proximity", alarmDistance="0.2", contactDistance="0.09", angleCone="0.0")
        root.addObject('CollisionResponse', name="Response", response="FrictionContactConstraint")

        CUBE_0 = root.addChild('CUBE_0')
        CUBE_0.addObject('MechanicalObject', dy="2.5")

        Visu = CUBE_0.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/cube.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="1 0 0 1", dy="2.5")

        ColliCube = CUBE_0.addChild('ColliCube')
        ColliCube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj", triangulate="1")
        ColliCube.addObject('MeshTopology', src="@loader")
        ColliCube.addObject('MechanicalObject', src="@loader", template="Vec3", dy="2.5")
        ColliCube.addObject('TriangleCollisionModel', simulated="0", moving="0")
        ColliCube.addObject('LineCollisionModel', simulated="0", moving="0")
        ColliCube.addObject('PointCollisionModel', simulated="0", moving="0")

        Constraints = CUBE_0.addChild('Constraints')
        Constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1 1.25 1")

        CUBE_1 = root.addChild('CUBE_1')
        CUBE_1.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        CUBE_1.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
        CUBE_1.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="0", dz="0.0")
        CUBE_1.addObject('UniformMass', totalMass="0.1")
        CUBE_1.addObject('UncoupledConstraintCorrection')

        Visu = CUBE_1.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/cube.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_2", color="1 1 0 1.0")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        ColliCube = CUBE_1.addChild('ColliCube')
        ColliCube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj", triangulate="1")
        ColliCube.addObject('MeshTopology', src="@loader")
        ColliCube.addObject('MechanicalObject', src="@loader")
        ColliCube.addObject('TriangleCollisionModel', contactStiffness="10.0")
        ColliCube.addObject('LineCollisionModel', contactStiffness="10.0")
        ColliCube.addObject('PointCollisionModel', contactStiffness="10.0")
        ColliCube.addObject('RigidMapping')

        Constraints = CUBE_1.addChild('Constraints')
        Constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1 1.25 1	-1.25 -1.25 1.25")
        Constraints.addObject('RigidMapping')
        root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_0/Constraints/points", object2="@CUBE_1/Constraints/points", first_point="0", second_point="0")

        CUBE_2 = root.addChild('CUBE_2')
        CUBE_2.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        CUBE_2.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
        CUBE_2.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="-2.5", dz="0.0")
        CUBE_2.addObject('UniformMass', totalMass="0.1")
        CUBE_2.addObject('UncoupledConstraintCorrection')

        Visu = CUBE_2.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/cube.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_3", color="0 1 0 1.0")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        ColliCube = CUBE_2.addChild('ColliCube')
        ColliCube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj")
        ColliCube.addObject('MeshTopology', src="@loader")
        ColliCube.addObject('MechanicalObject', src="@loader", scale="1.0")
        ColliCube.addObject('TriangleCollisionModel')
        ColliCube.addObject('LineCollisionModel')
        ColliCube.addObject('PointCollisionModel')
        ColliCube.addObject('RigidMapping')

        Constraints = CUBE_2.addChild('Constraints')
        Constraints.addObject('MechanicalObject', name="points", template="Vec3", position="-1.25 1.25 1.25	1.25 -1.25 -1.25")
        Constraints.addObject('RigidMapping')
        root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_1/Constraints/points", object2="@CUBE_2/Constraints/points", first_point="1", second_point="0")

        CUBE_3 = root.addChild('CUBE_3')
        CUBE_3.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        CUBE_3.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
        CUBE_3.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="-5.0", dz="0.0")
        CUBE_3.addObject('UniformMass', totalMass="0.1")
        CUBE_3.addObject('UncoupledConstraintCorrection')

        Visu = CUBE_3.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_4", filename="mesh/cube.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_4", color="0 1 1 1.0")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        ColliCube = CUBE_3.addChild('ColliCube')
        ColliCube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj")
        ColliCube.addObject('MeshTopology', src="@loader")
        ColliCube.addObject('MechanicalObject', src="@loader", scale="1.0")
        ColliCube.addObject('TriangleCollisionModel')
        ColliCube.addObject('LineCollisionModel')
        ColliCube.addObject('PointCollisionModel')
        ColliCube.addObject('RigidMapping')

        Constraints = CUBE_3.addChild('Constraints')
        Constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1.25 1.25 -1.25")
        Constraints.addObject('RigidMapping')
        root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_2/Constraints/points", object2="@CUBE_3/Constraints/points", first_point="1", second_point="0")

        CUBE_4 = root.addChild('CUBE_4')
        CUBE_4.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        CUBE_4.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
        CUBE_4.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="-2.5", dz="-2.5")
        CUBE_4.addObject('UniformMass', totalMass="0.1")
        CUBE_4.addObject('UncoupledConstraintCorrection')

        Visu = CUBE_4.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/cube.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="0 0 1 1.0")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        ColliCube = CUBE_4.addChild('ColliCube')
        ColliCube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj")
        ColliCube.addObject('MeshTopology', src="@loader")
        ColliCube.addObject('MechanicalObject', src="@loader", scale="1.0")
        ColliCube.addObject('TriangleCollisionModel')
        ColliCube.addObject('LineCollisionModel')
        ColliCube.addObject('PointCollisionModel')
        ColliCube.addObject('RigidMapping')

        Constraints = CUBE_4.addChild('Constraints')
        Constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1.25 -1.25 1.25	1.25 1.25 1.25")
        Constraints.addObject('RigidMapping')
        root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_2/Constraints/points", object2="@CUBE_4/Constraints/points", first_point="1", second_point="0")
    ```

Component/Constraint/Lagrangian/BilateralLagrangianConstraint_UGS.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <!-- BilateralLagrangianConstraint example -->
    <Node name="root" dt="0.001" gravity="0 -981 0">
        <RequiredPlugin name="Sofa.Component.AnimationLoop"/> <!-- Needed to use components [FreeMotionAnimationLoop] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [LocalMinDistance] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [UncoupledConstraintCorrection] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Model"/> <!-- Needed to use components [BilateralLagrangianConstraint] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Solver"/> <!-- Needed to use components [GenericConstraintSolver] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        
        <VisualStyle displayFlags="showForceFields" />
        <DefaultVisualManagerLoop />
        <FreeMotionAnimationLoop />
        <GenericConstraintSolver tolerance="0.001" maxIterations="1000" resolutionMethod="UnbuiltGaussSeidel" />
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <LocalMinDistance name="Proximity" alarmDistance="0.2" contactDistance="0.09" angleCone="0.0" />
        <CollisionResponse name="Response" response="FrictionContactConstraint" />
    
        <Node name="CUBE_0">
            <MechanicalObject dy="2.5" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/cube.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_0" color="1 0 0 1" dy="2.5" />
            </Node>
            <Node name="ColliCube">
                <MeshOBJLoader name="loader" filename="mesh/cube.obj" triangulate="1" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" template="Vec3" dy="2.5" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <LineCollisionModel simulated="0" moving="0" />
                <PointCollisionModel simulated="0" moving="0" />
            </Node>
            <Node name="Constraints">
                <MechanicalObject name="points" template="Vec3" position="1 1.25 1" />
            </Node>
        </Node>
        <Node name="CUBE_1">
            <EulerImplicitSolver printLog="false" rayleighStiffness="0.1" rayleighMass="0.1"/>
            <CGLinearSolver iterations="25" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject template="Rigid3" scale="1.0" dx="0.0" dy="0" dz="0.0" />
            <UniformMass totalMass="0.1" />
            <UncoupledConstraintCorrection />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_2" filename="mesh/cube.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_2" color="1 1 0 1.0" />
                <RigidMapping input="@.." output="@Visual" />
            </Node>
            <Node name="ColliCube">
                <MeshOBJLoader name="loader" filename="mesh/cube.obj" triangulate="1" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel contactStiffness="10.0" />
                <LineCollisionModel contactStiffness="10.0" />
                <PointCollisionModel contactStiffness="10.0" />
                <RigidMapping />
            </Node>
            <Node name="Constraints">
                <MechanicalObject name="points" template="Vec3" position="1 1.25 1&#x09;-1.25 -1.25 1.25" />
                <RigidMapping />
            </Node>
        </Node>
        <BilateralLagrangianConstraint template="Vec3" object1="@CUBE_0/Constraints/points" object2="@CUBE_1/Constraints/points" first_point="0" second_point="0" />
        <Node name="CUBE_2">
            <EulerImplicitSolver printLog="false" rayleighStiffness="0.1" rayleighMass="0.1"/>
            <CGLinearSolver iterations="25" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject template="Rigid3" scale="1.0" dx="0.0" dy="-2.5" dz="0.0" />
            <UniformMass totalMass="0.1" />
            <UncoupledConstraintCorrection />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_3" filename="mesh/cube.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_3" color="0 1 0 1.0" />
                <RigidMapping input="@.." output="@Visual" />
            </Node>
            <Node name="ColliCube">
                <MeshOBJLoader name="loader" filename="mesh/cube.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" scale="1.0" />
                <TriangleCollisionModel />
                <LineCollisionModel />
                <PointCollisionModel />
                <RigidMapping />
            </Node>
            <Node name="Constraints">
                <MechanicalObject name="points" template="Vec3" position="-1.25 1.25 1.25&#x09;1.25 -1.25 -1.25" />
                <RigidMapping />
            </Node>
        </Node>
        <BilateralLagrangianConstraint template="Vec3" object1="@CUBE_1/Constraints/points" object2="@CUBE_2/Constraints/points" first_point="1" second_point="0" />
        <Node name="CUBE_3">
            <EulerImplicitSolver printLog="false" rayleighStiffness="0.1" rayleighMass="0.1"/>
            <CGLinearSolver iterations="25" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject template="Rigid3" scale="1.0" dx="0.0" dy="-5.0" dz="0.0" />
            <UniformMass totalMass="0.1" />
            <UncoupledConstraintCorrection />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_4" filename="mesh/cube.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_4" color="0 1 1 1.0" />
                <RigidMapping input="@.." output="@Visual" />
            </Node>
            <Node name="ColliCube">
                <MeshOBJLoader name="loader" filename="mesh/cube.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" scale="1.0" />
                <TriangleCollisionModel />
                <LineCollisionModel />
                <PointCollisionModel />
                <RigidMapping />
            </Node>
            <Node name="Constraints">
                <MechanicalObject name="points" template="Vec3" position="1.25 1.25 -1.25" />
                <RigidMapping />
            </Node>
        </Node>
        <BilateralLagrangianConstraint template="Vec3" object1="@CUBE_2/Constraints/points" object2="@CUBE_3/Constraints/points" first_point="1" second_point="0" />
        <Node name="CUBE_4">
            <EulerImplicitSolver printLog="false" rayleighStiffness="0.1" rayleighMass="0.1"/>
            <CGLinearSolver iterations="25" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject template="Rigid3" scale="1.0" dx="0.0" dy="-2.5" dz="-2.5" />
            <UniformMass totalMass="0.1" />
            <UncoupledConstraintCorrection />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_1" filename="mesh/cube.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_1" color="0 0 1 1.0" />
                <RigidMapping input="@.." output="@Visual" />
            </Node>
            <Node name="ColliCube">
                <MeshOBJLoader name="loader" filename="mesh/cube.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" scale="1.0" />
                <TriangleCollisionModel />
                <LineCollisionModel />
                <PointCollisionModel />
                <RigidMapping />
            </Node>
            <Node name="Constraints">
                <MechanicalObject name="points" template="Vec3" position="1.25 -1.25 1.25&#x09;1.25 1.25 1.25" />
                <RigidMapping />
            </Node>
        </Node>
        <BilateralLagrangianConstraint template="Vec3" object1="@CUBE_2/Constraints/points" object2="@CUBE_4/Constraints/points" first_point="1" second_point="0" />
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.001", gravity="0 -981 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.AnimationLoop")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Model")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Solver")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showForceFields")
        root.addObject('DefaultVisualManagerLoop')
        root.addObject('FreeMotionAnimationLoop')
        root.addObject('GenericConstraintSolver', tolerance="0.001", maxIterations="1000", resolutionMethod="UnbuiltGaussSeidel")
        root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('LocalMinDistance', name="Proximity", alarmDistance="0.2", contactDistance="0.09", angleCone="0.0")
        root.addObject('CollisionResponse', name="Response", response="FrictionContactConstraint")

        CUBE_0 = root.addChild('CUBE_0')
        CUBE_0.addObject('MechanicalObject', dy="2.5")

        Visu = CUBE_0.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/cube.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="1 0 0 1", dy="2.5")

        ColliCube = CUBE_0.addChild('ColliCube')
        ColliCube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj", triangulate="1")
        ColliCube.addObject('MeshTopology', src="@loader")
        ColliCube.addObject('MechanicalObject', src="@loader", template="Vec3", dy="2.5")
        ColliCube.addObject('TriangleCollisionModel', simulated="0", moving="0")
        ColliCube.addObject('LineCollisionModel', simulated="0", moving="0")
        ColliCube.addObject('PointCollisionModel', simulated="0", moving="0")

        Constraints = CUBE_0.addChild('Constraints')
        Constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1 1.25 1")

        CUBE_1 = root.addChild('CUBE_1')
        CUBE_1.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        CUBE_1.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
        CUBE_1.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="0", dz="0.0")
        CUBE_1.addObject('UniformMass', totalMass="0.1")
        CUBE_1.addObject('UncoupledConstraintCorrection')

        Visu = CUBE_1.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/cube.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_2", color="1 1 0 1.0")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        ColliCube = CUBE_1.addChild('ColliCube')
        ColliCube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj", triangulate="1")
        ColliCube.addObject('MeshTopology', src="@loader")
        ColliCube.addObject('MechanicalObject', src="@loader")
        ColliCube.addObject('TriangleCollisionModel', contactStiffness="10.0")
        ColliCube.addObject('LineCollisionModel', contactStiffness="10.0")
        ColliCube.addObject('PointCollisionModel', contactStiffness="10.0")
        ColliCube.addObject('RigidMapping')

        Constraints = CUBE_1.addChild('Constraints')
        Constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1 1.25 1	-1.25 -1.25 1.25")
        Constraints.addObject('RigidMapping')
        root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_0/Constraints/points", object2="@CUBE_1/Constraints/points", first_point="0", second_point="0")

        CUBE_2 = root.addChild('CUBE_2')
        CUBE_2.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        CUBE_2.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
        CUBE_2.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="-2.5", dz="0.0")
        CUBE_2.addObject('UniformMass', totalMass="0.1")
        CUBE_2.addObject('UncoupledConstraintCorrection')

        Visu = CUBE_2.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/cube.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_3", color="0 1 0 1.0")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        ColliCube = CUBE_2.addChild('ColliCube')
        ColliCube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj")
        ColliCube.addObject('MeshTopology', src="@loader")
        ColliCube.addObject('MechanicalObject', src="@loader", scale="1.0")
        ColliCube.addObject('TriangleCollisionModel')
        ColliCube.addObject('LineCollisionModel')
        ColliCube.addObject('PointCollisionModel')
        ColliCube.addObject('RigidMapping')

        Constraints = CUBE_2.addChild('Constraints')
        Constraints.addObject('MechanicalObject', name="points", template="Vec3", position="-1.25 1.25 1.25	1.25 -1.25 -1.25")
        Constraints.addObject('RigidMapping')
        root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_1/Constraints/points", object2="@CUBE_2/Constraints/points", first_point="1", second_point="0")

        CUBE_3 = root.addChild('CUBE_3')
        CUBE_3.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        CUBE_3.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
        CUBE_3.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="-5.0", dz="0.0")
        CUBE_3.addObject('UniformMass', totalMass="0.1")
        CUBE_3.addObject('UncoupledConstraintCorrection')

        Visu = CUBE_3.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_4", filename="mesh/cube.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_4", color="0 1 1 1.0")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        ColliCube = CUBE_3.addChild('ColliCube')
        ColliCube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj")
        ColliCube.addObject('MeshTopology', src="@loader")
        ColliCube.addObject('MechanicalObject', src="@loader", scale="1.0")
        ColliCube.addObject('TriangleCollisionModel')
        ColliCube.addObject('LineCollisionModel')
        ColliCube.addObject('PointCollisionModel')
        ColliCube.addObject('RigidMapping')

        Constraints = CUBE_3.addChild('Constraints')
        Constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1.25 1.25 -1.25")
        Constraints.addObject('RigidMapping')
        root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_2/Constraints/points", object2="@CUBE_3/Constraints/points", first_point="1", second_point="0")

        CUBE_4 = root.addChild('CUBE_4')
        CUBE_4.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        CUBE_4.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
        CUBE_4.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="-2.5", dz="-2.5")
        CUBE_4.addObject('UniformMass', totalMass="0.1")
        CUBE_4.addObject('UncoupledConstraintCorrection')

        Visu = CUBE_4.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/cube.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="0 0 1 1.0")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        ColliCube = CUBE_4.addChild('ColliCube')
        ColliCube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj")
        ColliCube.addObject('MeshTopology', src="@loader")
        ColliCube.addObject('MechanicalObject', src="@loader", scale="1.0")
        ColliCube.addObject('TriangleCollisionModel')
        ColliCube.addObject('LineCollisionModel')
        ColliCube.addObject('PointCollisionModel')
        ColliCube.addObject('RigidMapping')

        Constraints = CUBE_4.addChild('Constraints')
        Constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1.25 -1.25 1.25	1.25 1.25 1.25")
        Constraints.addObject('RigidMapping')
        root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_2/Constraints/points", object2="@CUBE_4/Constraints/points", first_point="1", second_point="0")
    ```

Component/Constraint/Lagrangian/BilateralLagrangianConstraint_PGS.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <!-- BilateralLagrangianConstraint example -->
    <Node name="root" dt="0.001" gravity="0 -981 0">
        <RequiredPlugin name="Sofa.Component.AnimationLoop"/> <!-- Needed to use components [FreeMotionAnimationLoop] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [LocalMinDistance] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [UncoupledConstraintCorrection] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Model"/> <!-- Needed to use components [BilateralLagrangianConstraint] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Solver"/> <!-- Needed to use components [GenericConstraintSolver] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        
        <VisualStyle displayFlags="showForceFields" />
        <DefaultVisualManagerLoop />
        <FreeMotionAnimationLoop />
        <GenericConstraintSolver tolerance="0.001" maxIterations="1000" resolutionMethod="ProjectedGaussSeidel"/>
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <LocalMinDistance name="Proximity" alarmDistance="0.2" contactDistance="0.09" angleCone="0.0" />
        <CollisionResponse name="Response" response="FrictionContactConstraint" />
    
        <Node name="CUBE_0">
            <MechanicalObject dy="2.5" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/cube.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_0" color="1 0 0 1" dy="2.5" />
            </Node>
            <Node name="ColliCube">
                <MeshOBJLoader name="loader" filename="mesh/cube.obj" triangulate="1" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" template="Vec3" dy="2.5" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <LineCollisionModel simulated="0" moving="0" />
                <PointCollisionModel simulated="0" moving="0" />
            </Node>
            <Node name="Constraints">
                <MechanicalObject name="points" template="Vec3" position="1 1.25 1" />
            </Node>
        </Node>
        <Node name="CUBE_1">
            <EulerImplicitSolver printLog="false" rayleighStiffness="0.1" rayleighMass="0.1"/>
            <CGLinearSolver iterations="25" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject template="Rigid3" scale="1.0" dx="0.0" dy="0" dz="0.0" />
            <UniformMass totalMass="0.1" />
            <UncoupledConstraintCorrection />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_2" filename="mesh/cube.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_2" color="1 1 0 1.0" />
                <RigidMapping input="@.." output="@Visual" />
            </Node>
            <Node name="ColliCube">
                <MeshOBJLoader name="loader" filename="mesh/cube.obj" triangulate="1" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel contactStiffness="10.0" />
                <LineCollisionModel contactStiffness="10.0" />
                <PointCollisionModel contactStiffness="10.0" />
                <RigidMapping />
            </Node>
            <Node name="Constraints">
                <MechanicalObject name="points" template="Vec3" position="1 1.25 1&#x09;-1.25 -1.25 1.25" />
                <RigidMapping />
            </Node>
        </Node>
        <BilateralLagrangianConstraint template="Vec3" object1="@CUBE_0/Constraints/points" object2="@CUBE_1/Constraints/points" first_point="0" second_point="0" />
        <Node name="CUBE_2">
            <EulerImplicitSolver printLog="false" rayleighStiffness="0.1" rayleighMass="0.1"/>
            <CGLinearSolver iterations="25" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject template="Rigid3" scale="1.0" dx="0.0" dy="-2.5" dz="0.0" />
            <UniformMass totalMass="0.1" />
            <UncoupledConstraintCorrection />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_3" filename="mesh/cube.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_3" color="0 1 0 1.0" />
                <RigidMapping input="@.." output="@Visual" />
            </Node>
            <Node name="ColliCube">
                <MeshOBJLoader name="loader" filename="mesh/cube.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" scale="1.0" />
                <TriangleCollisionModel />
                <LineCollisionModel />
                <PointCollisionModel />
                <RigidMapping />
            </Node>
            <Node name="Constraints">
                <MechanicalObject name="points" template="Vec3" position="-1.25 1.25 1.25&#x09;1.25 -1.25 -1.25" />
                <RigidMapping />
            </Node>
        </Node>
        <BilateralLagrangianConstraint template="Vec3" object1="@CUBE_1/Constraints/points" object2="@CUBE_2/Constraints/points" first_point="1" second_point="0" />
        <Node name="CUBE_3">
            <EulerImplicitSolver printLog="false" rayleighStiffness="0.1" rayleighMass="0.1"/>
            <CGLinearSolver iterations="25" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject template="Rigid3" scale="1.0" dx="0.0" dy="-5.0" dz="0.0" />
            <UniformMass totalMass="0.1" />
            <UncoupledConstraintCorrection />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_4" filename="mesh/cube.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_4" color="0 1 1 1.0" />
                <RigidMapping input="@.." output="@Visual" />
            </Node>
            <Node name="ColliCube">
                <MeshOBJLoader name="loader" filename="mesh/cube.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" scale="1.0" />
                <TriangleCollisionModel />
                <LineCollisionModel />
                <PointCollisionModel />
                <RigidMapping />
            </Node>
            <Node name="Constraints">
                <MechanicalObject name="points" template="Vec3" position="1.25 1.25 -1.25" />
                <RigidMapping />
            </Node>
        </Node>
        <BilateralLagrangianConstraint template="Vec3" object1="@CUBE_2/Constraints/points" object2="@CUBE_3/Constraints/points" first_point="1" second_point="0" />
        <Node name="CUBE_4">
            <EulerImplicitSolver printLog="false" rayleighStiffness="0.1" rayleighMass="0.1"/>
            <CGLinearSolver iterations="25" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject template="Rigid3" scale="1.0" dx="0.0" dy="-2.5" dz="-2.5" />
            <UniformMass totalMass="0.1" />
            <UncoupledConstraintCorrection />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_1" filename="mesh/cube.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_1" color="0 0 1 1.0" />
                <RigidMapping input="@.." output="@Visual" />
            </Node>
            <Node name="ColliCube">
                <MeshOBJLoader name="loader" filename="mesh/cube.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" scale="1.0" />
                <TriangleCollisionModel />
                <LineCollisionModel />
                <PointCollisionModel />
                <RigidMapping />
            </Node>
            <Node name="Constraints">
                <MechanicalObject name="points" template="Vec3" position="1.25 -1.25 1.25&#x09;1.25 1.25 1.25" />
                <RigidMapping />
            </Node>
        </Node>
        <BilateralLagrangianConstraint template="Vec3" object1="@CUBE_2/Constraints/points" object2="@CUBE_4/Constraints/points" first_point="1" second_point="0" />
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.001", gravity="0 -981 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.AnimationLoop")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Model")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Solver")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showForceFields")
        root.addObject('DefaultVisualManagerLoop')
        root.addObject('FreeMotionAnimationLoop')
        root.addObject('GenericConstraintSolver', tolerance="0.001", maxIterations="1000", resolutionMethod="ProjectedGaussSeidel")
        root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('LocalMinDistance', name="Proximity", alarmDistance="0.2", contactDistance="0.09", angleCone="0.0")
        root.addObject('CollisionResponse', name="Response", response="FrictionContactConstraint")

        CUBE_0 = root.addChild('CUBE_0')
        CUBE_0.addObject('MechanicalObject', dy="2.5")

        Visu = CUBE_0.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/cube.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="1 0 0 1", dy="2.5")

        ColliCube = CUBE_0.addChild('ColliCube')
        ColliCube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj", triangulate="1")
        ColliCube.addObject('MeshTopology', src="@loader")
        ColliCube.addObject('MechanicalObject', src="@loader", template="Vec3", dy="2.5")
        ColliCube.addObject('TriangleCollisionModel', simulated="0", moving="0")
        ColliCube.addObject('LineCollisionModel', simulated="0", moving="0")
        ColliCube.addObject('PointCollisionModel', simulated="0", moving="0")

        Constraints = CUBE_0.addChild('Constraints')
        Constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1 1.25 1")

        CUBE_1 = root.addChild('CUBE_1')
        CUBE_1.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        CUBE_1.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
        CUBE_1.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="0", dz="0.0")
        CUBE_1.addObject('UniformMass', totalMass="0.1")
        CUBE_1.addObject('UncoupledConstraintCorrection')

        Visu = CUBE_1.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/cube.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_2", color="1 1 0 1.0")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        ColliCube = CUBE_1.addChild('ColliCube')
        ColliCube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj", triangulate="1")
        ColliCube.addObject('MeshTopology', src="@loader")
        ColliCube.addObject('MechanicalObject', src="@loader")
        ColliCube.addObject('TriangleCollisionModel', contactStiffness="10.0")
        ColliCube.addObject('LineCollisionModel', contactStiffness="10.0")
        ColliCube.addObject('PointCollisionModel', contactStiffness="10.0")
        ColliCube.addObject('RigidMapping')

        Constraints = CUBE_1.addChild('Constraints')
        Constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1 1.25 1	-1.25 -1.25 1.25")
        Constraints.addObject('RigidMapping')
        root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_0/Constraints/points", object2="@CUBE_1/Constraints/points", first_point="0", second_point="0")

        CUBE_2 = root.addChild('CUBE_2')
        CUBE_2.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        CUBE_2.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
        CUBE_2.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="-2.5", dz="0.0")
        CUBE_2.addObject('UniformMass', totalMass="0.1")
        CUBE_2.addObject('UncoupledConstraintCorrection')

        Visu = CUBE_2.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/cube.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_3", color="0 1 0 1.0")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        ColliCube = CUBE_2.addChild('ColliCube')
        ColliCube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj")
        ColliCube.addObject('MeshTopology', src="@loader")
        ColliCube.addObject('MechanicalObject', src="@loader", scale="1.0")
        ColliCube.addObject('TriangleCollisionModel')
        ColliCube.addObject('LineCollisionModel')
        ColliCube.addObject('PointCollisionModel')
        ColliCube.addObject('RigidMapping')

        Constraints = CUBE_2.addChild('Constraints')
        Constraints.addObject('MechanicalObject', name="points", template="Vec3", position="-1.25 1.25 1.25	1.25 -1.25 -1.25")
        Constraints.addObject('RigidMapping')
        root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_1/Constraints/points", object2="@CUBE_2/Constraints/points", first_point="1", second_point="0")

        CUBE_3 = root.addChild('CUBE_3')
        CUBE_3.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        CUBE_3.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
        CUBE_3.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="-5.0", dz="0.0")
        CUBE_3.addObject('UniformMass', totalMass="0.1")
        CUBE_3.addObject('UncoupledConstraintCorrection')

        Visu = CUBE_3.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_4", filename="mesh/cube.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_4", color="0 1 1 1.0")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        ColliCube = CUBE_3.addChild('ColliCube')
        ColliCube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj")
        ColliCube.addObject('MeshTopology', src="@loader")
        ColliCube.addObject('MechanicalObject', src="@loader", scale="1.0")
        ColliCube.addObject('TriangleCollisionModel')
        ColliCube.addObject('LineCollisionModel')
        ColliCube.addObject('PointCollisionModel')
        ColliCube.addObject('RigidMapping')

        Constraints = CUBE_3.addChild('Constraints')
        Constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1.25 1.25 -1.25")
        Constraints.addObject('RigidMapping')
        root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_2/Constraints/points", object2="@CUBE_3/Constraints/points", first_point="1", second_point="0")

        CUBE_4 = root.addChild('CUBE_4')
        CUBE_4.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        CUBE_4.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
        CUBE_4.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="-2.5", dz="-2.5")
        CUBE_4.addObject('UniformMass', totalMass="0.1")
        CUBE_4.addObject('UncoupledConstraintCorrection')

        Visu = CUBE_4.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/cube.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="0 0 1 1.0")
        Visu.addObject('RigidMapping', input="@..", output="@Visual")

        ColliCube = CUBE_4.addChild('ColliCube')
        ColliCube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj")
        ColliCube.addObject('MeshTopology', src="@loader")
        ColliCube.addObject('MechanicalObject', src="@loader", scale="1.0")
        ColliCube.addObject('TriangleCollisionModel')
        ColliCube.addObject('LineCollisionModel')
        ColliCube.addObject('PointCollisionModel')
        ColliCube.addObject('RigidMapping')

        Constraints = CUBE_4.addChild('Constraints')
        Constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1.25 -1.25 1.25	1.25 1.25 1.25")
        Constraints.addObject('RigidMapping')
        root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_2/Constraints/points", object2="@CUBE_4/Constraints/points", first_point="1", second_point="0")
    ```

Component/Constraint/Lagrangian/BilateralLagrangianConstraint_Rigid.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <!-- BilateralLagrangianConstraint example using rigid-->
    <Node name="root" dt="0.1" gravity="0 -0.981 0">
        <RequiredPlugin name="Sofa.Component.AnimationLoop"/> <!-- Needed to use components [FreeMotionAnimationLoop] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [SphereCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [LinearSolverConstraintCorrection] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Model"/> <!-- Needed to use components [BilateralLagrangianConstraint] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Solver"/> <!-- Needed to use components [GenericConstraintSolver] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [BTDLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [BeamFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <FreeMotionAnimationLoop />
        <GenericConstraintSolver tolerance="0.001" maxIterations="1000"/>
        <Node name="Beam1">
            <EulerImplicitSolver name="odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <BTDLinearSolver printLog="false" verbose="false" />
            <MechanicalObject template="Rigid3" name="DOFs1" position="0 0 0 0 0 0 1  1 0 0 0 0 0 1  2 0 0 0 0 0 1  3 0 0 0 0 0 1  4 0 0 0 0 0 1  5 0 0 0 0 0 1  6 0 0 0 0 0 1  7 0 0 0 0 0 1" />
            <MeshTopology name="lines" lines="0 1 1 2 2 3 3 4 4 5 5 6 6 7" />
            <UniformMass vertexMass="1 1 0.01 0 0 0 0.1 0 0 0 0.1 0" printLog="false" />
            <BeamFEMForceField name="FEM" poissonRatio="0.49" radius="0.1" youngModulus="2000000" />
            <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="7" />
            <LinearSolverConstraintCorrection />
             <SphereCollisionModel radius="0.1" group="1"/>
            <Node name="ConstraintPoint">
                <MechanicalObject template="Rigid3" name="dof1" position="0 0 0 0 0 -0.707107 0.707107 " />
                <RigidMapping index="0" />
            </Node>
        </Node>
        <Node name="Beam2">
            <EulerImplicitSolver name="odesolver" printLog="false" />
            <BTDLinearSolver printLog="false" verbose="false" />
            <MechanicalObject template="Rigid3" name="DOFs2" position="0 0 0 0 0 -0.707107 0.707107 0 -1 0 0 0-0.707107 0.707107  0 -2 0 0 0 -0.707107 0.707107  0 -3 0 0 0 -0.707107 0.707107  0 -4 0 0 0 -0.707107 0.707107  0 -5 0 0 0 -0.707107 0.707107  0 -6 0 0 0 -0.707107 0.707107  0 -7 0 0 0 -0.707107 0.707107" />
            <MeshTopology name="lines" lines="0 1 1 2 2 3 3 4 4 5 5 6 6 7" />
            <UniformMass vertexMass="1 1 0.01 0 0 0 0.1 0 0 0 0.1 0" printLog="false" />
            <BeamFEMForceField name="FEM" poissonRatio="0.49" radius="0.1" youngModulus="20000000" />
            <LinearSolverConstraintCorrection />
            <SphereCollisionModel radius="0.1" group="1"/>
        </Node>
        <BilateralLagrangianConstraint template="Rigid3" object1="@Beam1/ConstraintPoint/dof1" object2="@Beam2/DOFs2" first_point="0" second_point="0" />
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.1", gravity="0 -0.981 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.AnimationLoop")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Model")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Solver")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
        root.addObject('FreeMotionAnimationLoop')
        root.addObject('GenericConstraintSolver', tolerance="0.001", maxIterations="1000")

        Beam1 = root.addChild('Beam1')
        Beam1.addObject('EulerImplicitSolver', name="odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        Beam1.addObject('BTDLinearSolver', printLog="false", verbose="false")
        Beam1.addObject('MechanicalObject', template="Rigid3", name="DOFs1", position="0 0 0 0 0 0 1  1 0 0 0 0 0 1  2 0 0 0 0 0 1  3 0 0 0 0 0 1  4 0 0 0 0 0 1  5 0 0 0 0 0 1  6 0 0 0 0 0 1  7 0 0 0 0 0 1")
        Beam1.addObject('MeshTopology', name="lines", lines="0 1 1 2 2 3 3 4 4 5 5 6 6 7")
        Beam1.addObject('UniformMass', vertexMass="1 1 0.01 0 0 0 0.1 0 0 0 0.1 0", printLog="false")
        Beam1.addObject('BeamFEMForceField', name="FEM", poissonRatio="0.49", radius="0.1", youngModulus="2000000")
        Beam1.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="7")
        Beam1.addObject('LinearSolverConstraintCorrection')
        Beam1.addObject('SphereCollisionModel', radius="0.1", group="1")

        ConstraintPoint = Beam1.addChild('ConstraintPoint')
        ConstraintPoint.addObject('MechanicalObject', template="Rigid3", name="dof1", position="0 0 0 0 0 -0.707107 0.707107 ")
        ConstraintPoint.addObject('RigidMapping', index="0")

        Beam2 = root.addChild('Beam2')
        Beam2.addObject('EulerImplicitSolver', name="odesolver", printLog="false")
        Beam2.addObject('BTDLinearSolver', printLog="false", verbose="false")
        Beam2.addObject('MechanicalObject', template="Rigid3", name="DOFs2", position="0 0 0 0 0 -0.707107 0.707107 0 -1 0 0 0-0.707107 0.707107  0 -2 0 0 0 -0.707107 0.707107  0 -3 0 0 0 -0.707107 0.707107  0 -4 0 0 0 -0.707107 0.707107  0 -5 0 0 0 -0.707107 0.707107  0 -6 0 0 0 -0.707107 0.707107  0 -7 0 0 0 -0.707107 0.707107")
        Beam2.addObject('MeshTopology', name="lines", lines="0 1 1 2 2 3 3 4 4 5 5 6 6 7")
        Beam2.addObject('UniformMass', vertexMass="1 1 0.01 0 0 0 0.1 0 0 0 0.1 0", printLog="false")
        Beam2.addObject('BeamFEMForceField', name="FEM", poissonRatio="0.49", radius="0.1", youngModulus="20000000")
        Beam2.addObject('LinearSolverConstraintCorrection')
        Beam2.addObject('SphereCollisionModel', radius="0.1", group="1")
        root.addObject('BilateralLagrangianConstraint', template="Rigid3", object1="@Beam1/ConstraintPoint/dof1", object2="@Beam2/DOFs2", first_point="0", second_point="0")
    ```


<!-- automatically generated doc END -->
