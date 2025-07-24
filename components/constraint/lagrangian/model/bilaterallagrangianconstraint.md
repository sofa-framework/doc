---
title: BilateralLagrangianConstraint
---

BilateralLagrangianConstraint
==============================

This component belongs to the category of [Constraint Laws](../../../../../simulation-principles/constraint/lagrange-constraint/#constraint-laws) used for the Lagrange constraint resolution and inherits from the PairInteractionConstraint. The BilateralLagrangianConstraint defines an [holonomic constraint](https://en.wikipedia.org/wiki/Holonomic_constraints) law between a pair of simulated body, i.e. the constraint defined between the pair of objects must have an equality form:

$$
\Phi(x_1,x_2...)~=~0
$$

Such a constraint is suited for attachment cases or sliding joints. For an attachment case, if the vertex _i_ of object 1 and the vertex _j_ of object 2 are attached, the holonomic constraint law can be written as $x_1(i)-x_2(j)~=~0$.

For a BilateralLagrangianConstraint, the constraint matrix $\mathbf{H}$ (derivative of the constraint law) corresponds to:

- $\mathbf{H}_1 = \begin{bmatrix} \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 &  ... & \begin{bmatrix} 1 & 0 & 0\\\end{bmatrix}_i &  ... & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_1}\\ \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 &  ... & \begin{bmatrix} 0 & 1 & 0\\\end{bmatrix}_i &  ... & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_1}\\ \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 &  ... & \begin{bmatrix} 0 & 0 & 1\\\end{bmatrix}_i &  ... & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_1}\\ \end{bmatrix}$ for object 1
- $\mathbf{H}_2 = \begin{bmatrix} \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 &  ... & \begin{bmatrix} -1 & 0 & 0\\\end{bmatrix}_j &  ... & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_2}\\ \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 &  ... & \begin{bmatrix} 0 & -1 & 0\\\end{bmatrix}_j &  ... & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_2}\\ \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 &  ... & \begin{bmatrix} 0 & 0 & -1\\\end{bmatrix}_j &  ... & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_2}\\ \end{bmatrix}$ for object 2


As all constraint laws, the BilateralLagrangianConstraint will be called in the following functions and for the following steps:

- `getConstraintViolation()`: project the free velocity in the constraint space and compute the free interpenetration $\dot{\delta}_1^{free}=\mathbf{H}_1v_1^{free}$
- `buildConstraintMatrix()`: build the compliance made up of $dt\mathbf{H}_1\mathbf{A}_1^{-1}\mathbf{H}_1^T$ and $dt\mathbf{H}_2\mathbf{A}_2^{-1}\mathbf{H}_2^T$



Usage
-----

The BilateralLagrangianConstraint can only be used in the context of [Lagrange constraint](../../../../../simulation-principles/constraint/lagrange-constraint/) resolution. The scene must therefore contain:

- a FreeMotionAnimationLoop
- a ConstraintSolver

Moreover, each constrained object must define in its node a ConstraintCorrection so that the corrective motion can be applied.
<!-- automatically generated doc START -->
<!-- generate_doc -->

BilateralLagrangianConstraint defining an holonomic equality constraint (attachment).


## Rigid3d

Templates:

- Rigid3d

__Target__: Sofa.Component.Constraint.Lagrangian.Model

__namespace__: sofa::component::constraint::lagrangian::model

__parents__:

- PairInteractionConstraint

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
	<tr>
		<td>load</td>
		<td>
Apply this factor to the constraint force to enable incremental loading. This value should be in the interval [0.0, 1.0].
		</td>
		<td>1</td>
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
|object1|First object associated to this component|MechanicalState&lt;Rigid3d&gt;|
|object2|Second object associated to this component|MechanicalState&lt;Rigid3d&gt;|
|topology1|link to the first topology container|BaseMeshTopology|
|topology2|link to the second topology container|BaseMeshTopology|

<!-- generate_doc -->
## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.Constraint.Lagrangian.Model

__namespace__: sofa::component::constraint::lagrangian::model

__parents__:

- PairInteractionConstraint

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
	<tr>
		<td>load</td>
		<td>
Apply this factor to the constraint force to enable incremental loading. This value should be in the interval [0.0, 1.0].
		</td>
		<td>1</td>
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
|topology1|link to the first topology container|BaseMeshTopology|
|topology2|link to the second topology container|BaseMeshTopology|

## Examples 

BilateralLagrangianConstraint_with_regularization_solvable.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <!-- BilateralLagrangianConstraint example -->
    <Node name="root" dt="0.001" gravity="0 0 -9.81">
        <RequiredPlugin name="Sofa.Component.AnimationLoop"/> <!-- Needed to use components [FreeMotionAnimationLoop] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [LinearSolverConstraintCorrection] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Model"/> <!-- Needed to use components [BilateralLagrangianConstraint] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Solver"/> <!-- Needed to use components [GenericConstraintSolver] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [SparseLDLSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        
        <VisualStyle displayFlags="showForceFields" />
        <DefaultVisualManagerLoop />
        <FreeMotionAnimationLoop />
        <GenericConstraintSolver tolerance="0.0001" maxIterations="1000" resolutionMethod="ProjectedGaussSeidel" regularizationTerm="0.0"/>
    
    
        <Node name="TargetCube0">
            <RegularGridTopology name="grid" nx="4" ny="4" nz="2" xmin="-1" xmax="1" ymin="-1" ymax="1" zmin="-0.5" zmax="0.5" />
            <MechanicalObject name="mstate" template="Vec3"/>
            <BoxROI name="bottom" box="-1.1 -1.1 -1.1  1.1 1.1 -0.4" />
            <BoxROI name="top" box="-1.1 -1.1 0.4  1.1 1.1 1.1" />
        </Node>
    
        <Node name="DeformableCube0">
    
            <VisualStyle displayFlags="showForceFields" />
            <EulerImplicitSolver name="odesolver" printLog="false" />
            <SparseLDLSolver name="linearSolver" template="CompressedRowSparseMatrixMat3x3d" />
    
            <RegularGridTopology name="grid" nx="4" ny="4" nz="4" xmin="-1" xmax="1" ymin="-1" ymax="1" zmin="-1" zmax="1" />
            <MechanicalObject name="mstate" template="Vec3" />
            <HexahedronFEMForceField poissonRatio="0.49" youngModulus="700000"/>
            <UniformMass totalMass="10" />
            <BoxROI name="bottom" box="-1.1 -1.1 -1.1  1.1 1.1 -0.9" />
            <BoxROI name="top" box="-1.1 -1.1 0.9  1.1 1.1 1.1" />
            <LinearSolverConstraintCorrection linearSolver="@linearSolver"/>
        </Node>
    
        <BilateralLagrangianConstraint template="Vec3"
                                       object1="@DeformableCube0/mstate" first_point="@DeformableCube0/bottom.indices"
                                       object2="@TargetCube0/mstate" second_point="@TargetCube0/bottom.indices" />
    
        <BilateralLagrangianConstraint template="Vec3"
                                       object1="@DeformableCube0/mstate" first_point="@DeformableCube0/top.indices"
                                       object2="@TargetCube0/mstate" second_point="@TargetCube0/top.indices" />
    
        <!-- With regularization -->
        <Node name="TargetCube1">
            <RegularGridTopology name="grid" nx="4" ny="4" nz="2" xmin="2" xmax="4" ymin="-1" ymax="1" zmin="-0.5" zmax="0.5" />
            <MechanicalObject name="mstate" template="Vec3"/>
            <BoxROI name="bottom" box="1.9 -1.1 -1.1  4.1 1.1 -0.4" />
            <BoxROI name="top" box="1.9 -1.1 0.4  4.1 1.1 1.1" />
        </Node>
    
        <Node name="DeformableCube1">
    
            <VisualStyle displayFlags="showForceFields" />
            <EulerImplicitSolver name="odesolver" printLog="false" />
            <SparseLDLSolver name="linearSolver" template="CompressedRowSparseMatrixMat3x3d" />
    
            <RegularGridTopology name="grid" nx="4" ny="4" nz="4" xmin="2" xmax="4" ymin="-1" ymax="1" zmin="-1" zmax="1" />
            <MechanicalObject name="mstate" template="Vec3" />
            <HexahedronFEMForceField poissonRatio="0.49" youngModulus="700000"/>
            <UniformMass totalMass="10" />
            <BoxROI name="bottom" box="1.9 -1.1 -1.1  4.1 1.1 -0.9" />
            <BoxROI name="top" box="1.9 -1.1 0.9  4.1 1.1 1.1" />
            <LinearSolverConstraintCorrection linearSolver="@linearSolver" regularizationTerm="0.002"/>
        </Node>
    
        <BilateralLagrangianConstraint template="Vec3"
                                       object1="@DeformableCube1/mstate" first_point="@DeformableCube1/bottom.indices"
                                       object2="@TargetCube1/mstate" second_point="@TargetCube1/bottom.indices" />
    
        <BilateralLagrangianConstraint template="Vec3"
                                       object1="@DeformableCube1/mstate" first_point="@DeformableCube1/top.indices"
                                       object2="@TargetCube1/mstate" second_point="@TargetCube1/top.indices" />
    
        <!-- With more regularization -->
        <Node name="TargetCube2">
            <RegularGridTopology name="grid" nx="4" ny="4" nz="2" xmin="5" xmax="7" ymin="-1" ymax="1" zmin="-0.5" zmax="0.5" />
            <MechanicalObject name="mstate" template="Vec3"/>
            <BoxROI name="bottom" box="4.9 -1.1 -1.1  7.1 1.1 -0.4" />
            <BoxROI name="top" box="4.9 -1.1 0.4  7.1 1.1 1.1" />
        </Node>
    
        <Node name="DeformableCube2">
    
            <VisualStyle displayFlags="showForceFields" />
            <EulerImplicitSolver name="odesolver" printLog="false" />
            <SparseLDLSolver name="linearSolver" template="CompressedRowSparseMatrixMat3x3d" />
    
            <RegularGridTopology name="grid" nx="4" ny="4" nz="4" xmin="5" xmax="7" ymin="-1" ymax="1" zmin="-1" zmax="1" />
            <MechanicalObject name="mstate" template="Vec3" />
            <HexahedronFEMForceField poissonRatio="0.49" youngModulus="700000"/>
            <UniformMass totalMass="10" />
            <BoxROI name="bottom" box="4.9 -1.1 -1.1  7.1 1.1 -0.9" />
            <BoxROI name="top" box="4.9 -1.1 0.9  7.1 1.1 1.1" />
            <LinearSolverConstraintCorrection linearSolver="@linearSolver" regularizationTerm="0.005"/>
        </Node>
    
        <BilateralLagrangianConstraint template="Vec3"
                                       object1="@DeformableCube2/mstate" first_point="@DeformableCube2/bottom.indices"
                                       object2="@TargetCube2/mstate" second_point="@TargetCube2/bottom.indices" />
    
        <BilateralLagrangianConstraint template="Vec3"
                                       object1="@DeformableCube2/mstate" first_point="@DeformableCube2/top.indices"
                                       object2="@TargetCube2/mstate" second_point="@TargetCube2/top.indices" />
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.001", gravity="0 0 -9.81")

       root.addObject('RequiredPlugin', name="Sofa.Component.AnimationLoop")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Model")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Solver")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('VisualStyle', displayFlags="showForceFields")
       root.addObject('DefaultVisualManagerLoop', )
       root.addObject('FreeMotionAnimationLoop', )
       root.addObject('GenericConstraintSolver', tolerance="0.0001", maxIterations="1000", resolutionMethod="ProjectedGaussSeidel", regularizationTerm="0.0")

       target_cube0 = root.addChild('TargetCube0')

       target_cube0.addObject('RegularGridTopology', name="grid", nx="4", ny="4", nz="2", xmin="-1", xmax="1", ymin="-1", ymax="1", zmin="-0.5", zmax="0.5")
       target_cube0.addObject('MechanicalObject', name="mstate", template="Vec3")
       target_cube0.addObject('BoxROI', name="bottom", box="-1.1 -1.1 -1.1  1.1 1.1 -0.4")
       target_cube0.addObject('BoxROI', name="top", box="-1.1 -1.1 0.4  1.1 1.1 1.1")

       deformable_cube0 = root.addChild('DeformableCube0')

       deformable_cube0.addObject('VisualStyle', displayFlags="showForceFields")
       deformable_cube0.addObject('EulerImplicitSolver', name="odesolver", printLog="false")
       deformable_cube0.addObject('SparseLDLSolver', name="linearSolver", template="CompressedRowSparseMatrixMat3x3d")
       deformable_cube0.addObject('RegularGridTopology', name="grid", nx="4", ny="4", nz="4", xmin="-1", xmax="1", ymin="-1", ymax="1", zmin="-1", zmax="1")
       deformable_cube0.addObject('MechanicalObject', name="mstate", template="Vec3")
       deformable_cube0.addObject('HexahedronFEMForceField', poissonRatio="0.49", youngModulus="700000")
       deformable_cube0.addObject('UniformMass', totalMass="10")
       deformable_cube0.addObject('BoxROI', name="bottom", box="-1.1 -1.1 -1.1  1.1 1.1 -0.9")
       deformable_cube0.addObject('BoxROI', name="top", box="-1.1 -1.1 0.9  1.1 1.1 1.1")
       deformable_cube0.addObject('LinearSolverConstraintCorrection', linearSolver="@linearSolver")

       root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@DeformableCube0/mstate", first_point="@DeformableCube0/bottom.indices", object2="@TargetCube0/mstate", second_point="@TargetCube0/bottom.indices")
       root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@DeformableCube0/mstate", first_point="@DeformableCube0/top.indices", object2="@TargetCube0/mstate", second_point="@TargetCube0/top.indices")

       target_cube1 = root.addChild('TargetCube1')

       target_cube1.addObject('RegularGridTopology', name="grid", nx="4", ny="4", nz="2", xmin="2", xmax="4", ymin="-1", ymax="1", zmin="-0.5", zmax="0.5")
       target_cube1.addObject('MechanicalObject', name="mstate", template="Vec3")
       target_cube1.addObject('BoxROI', name="bottom", box="1.9 -1.1 -1.1  4.1 1.1 -0.4")
       target_cube1.addObject('BoxROI', name="top", box="1.9 -1.1 0.4  4.1 1.1 1.1")

       deformable_cube1 = root.addChild('DeformableCube1')

       deformable_cube1.addObject('VisualStyle', displayFlags="showForceFields")
       deformable_cube1.addObject('EulerImplicitSolver', name="odesolver", printLog="false")
       deformable_cube1.addObject('SparseLDLSolver', name="linearSolver", template="CompressedRowSparseMatrixMat3x3d")
       deformable_cube1.addObject('RegularGridTopology', name="grid", nx="4", ny="4", nz="4", xmin="2", xmax="4", ymin="-1", ymax="1", zmin="-1", zmax="1")
       deformable_cube1.addObject('MechanicalObject', name="mstate", template="Vec3")
       deformable_cube1.addObject('HexahedronFEMForceField', poissonRatio="0.49", youngModulus="700000")
       deformable_cube1.addObject('UniformMass', totalMass="10")
       deformable_cube1.addObject('BoxROI', name="bottom", box="1.9 -1.1 -1.1  4.1 1.1 -0.9")
       deformable_cube1.addObject('BoxROI', name="top", box="1.9 -1.1 0.9  4.1 1.1 1.1")
       deformable_cube1.addObject('LinearSolverConstraintCorrection', linearSolver="@linearSolver", regularizationTerm="0.002")

       root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@DeformableCube1/mstate", first_point="@DeformableCube1/bottom.indices", object2="@TargetCube1/mstate", second_point="@TargetCube1/bottom.indices")
       root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@DeformableCube1/mstate", first_point="@DeformableCube1/top.indices", object2="@TargetCube1/mstate", second_point="@TargetCube1/top.indices")

       target_cube2 = root.addChild('TargetCube2')

       target_cube2.addObject('RegularGridTopology', name="grid", nx="4", ny="4", nz="2", xmin="5", xmax="7", ymin="-1", ymax="1", zmin="-0.5", zmax="0.5")
       target_cube2.addObject('MechanicalObject', name="mstate", template="Vec3")
       target_cube2.addObject('BoxROI', name="bottom", box="4.9 -1.1 -1.1  7.1 1.1 -0.4")
       target_cube2.addObject('BoxROI', name="top", box="4.9 -1.1 0.4  7.1 1.1 1.1")

       deformable_cube2 = root.addChild('DeformableCube2')

       deformable_cube2.addObject('VisualStyle', displayFlags="showForceFields")
       deformable_cube2.addObject('EulerImplicitSolver', name="odesolver", printLog="false")
       deformable_cube2.addObject('SparseLDLSolver', name="linearSolver", template="CompressedRowSparseMatrixMat3x3d")
       deformable_cube2.addObject('RegularGridTopology', name="grid", nx="4", ny="4", nz="4", xmin="5", xmax="7", ymin="-1", ymax="1", zmin="-1", zmax="1")
       deformable_cube2.addObject('MechanicalObject', name="mstate", template="Vec3")
       deformable_cube2.addObject('HexahedronFEMForceField', poissonRatio="0.49", youngModulus="700000")
       deformable_cube2.addObject('UniformMass', totalMass="10")
       deformable_cube2.addObject('BoxROI', name="bottom", box="4.9 -1.1 -1.1  7.1 1.1 -0.9")
       deformable_cube2.addObject('BoxROI', name="top", box="4.9 -1.1 0.9  7.1 1.1 1.1")
       deformable_cube2.addObject('LinearSolverConstraintCorrection', linearSolver="@linearSolver", regularizationTerm="0.005")

       root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@DeformableCube2/mstate", first_point="@DeformableCube2/bottom.indices", object2="@TargetCube2/mstate", second_point="@TargetCube2/bottom.indices")
       root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@DeformableCube2/mstate", first_point="@DeformableCube2/top.indices", object2="@TargetCube2/mstate", second_point="@TargetCube2/top.indices")
    ```

BilateralLagrangianConstraint_UGS.scn

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
                <TriangleCollisionModel />
                <LineCollisionModel />
                <PointCollisionModel />
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
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.001", gravity="0 -981 0")

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
       root.addObject('DefaultVisualManagerLoop', )
       root.addObject('FreeMotionAnimationLoop', )
       root.addObject('GenericConstraintSolver', tolerance="0.001", maxIterations="1000", resolutionMethod="UnbuiltGaussSeidel")
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('LocalMinDistance', name="Proximity", alarmDistance="0.2", contactDistance="0.09", angleCone="0.0")
       root.addObject('CollisionResponse', name="Response", response="FrictionContactConstraint")

       cube_0 = root.addChild('CUBE_0')

       cube_0.addObject('MechanicalObject', dy="2.5")

       visu = CUBE_0.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/cube.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="1 0 0 1", dy="2.5")

       colli_cube = CUBE_0.addChild('ColliCube')

       colli_cube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj", triangulate="1")
       colli_cube.addObject('MeshTopology', src="@loader")
       colli_cube.addObject('MechanicalObject', src="@loader", template="Vec3", dy="2.5")
       colli_cube.addObject('TriangleCollisionModel', simulated="0", moving="0")
       colli_cube.addObject('LineCollisionModel', simulated="0", moving="0")
       colli_cube.addObject('PointCollisionModel', simulated="0", moving="0")

       constraints = CUBE_0.addChild('Constraints')

       constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1 1.25 1")

       cube_1 = root.addChild('CUBE_1')

       cube_1.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       cube_1.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
       cube_1.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="0", dz="0.0")
       cube_1.addObject('UniformMass', totalMass="0.1")
       cube_1.addObject('UncoupledConstraintCorrection', )

       visu = CUBE_1.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/cube.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_2", color="1 1 0 1.0")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       colli_cube = CUBE_1.addChild('ColliCube')

       colli_cube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj", triangulate="1")
       colli_cube.addObject('MeshTopology', src="@loader")
       colli_cube.addObject('MechanicalObject', src="@loader")
       colli_cube.addObject('TriangleCollisionModel', )
       colli_cube.addObject('LineCollisionModel', )
       colli_cube.addObject('PointCollisionModel', )
       colli_cube.addObject('RigidMapping', )

       constraints = CUBE_1.addChild('Constraints')

       constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1 1.25 1	-1.25 -1.25 1.25")
       constraints.addObject('RigidMapping', )

       root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_0/Constraints/points", object2="@CUBE_1/Constraints/points", first_point="0", second_point="0")

       cube_2 = root.addChild('CUBE_2')

       cube_2.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       cube_2.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
       cube_2.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="-2.5", dz="0.0")
       cube_2.addObject('UniformMass', totalMass="0.1")
       cube_2.addObject('UncoupledConstraintCorrection', )

       visu = CUBE_2.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/cube.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_3", color="0 1 0 1.0")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       colli_cube = CUBE_2.addChild('ColliCube')

       colli_cube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj")
       colli_cube.addObject('MeshTopology', src="@loader")
       colli_cube.addObject('MechanicalObject', src="@loader", scale="1.0")
       colli_cube.addObject('TriangleCollisionModel', )
       colli_cube.addObject('LineCollisionModel', )
       colli_cube.addObject('PointCollisionModel', )
       colli_cube.addObject('RigidMapping', )

       constraints = CUBE_2.addChild('Constraints')

       constraints.addObject('MechanicalObject', name="points", template="Vec3", position="-1.25 1.25 1.25	1.25 -1.25 -1.25")
       constraints.addObject('RigidMapping', )

       root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_1/Constraints/points", object2="@CUBE_2/Constraints/points", first_point="1", second_point="0")

       cube_3 = root.addChild('CUBE_3')

       cube_3.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       cube_3.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
       cube_3.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="-5.0", dz="0.0")
       cube_3.addObject('UniformMass', totalMass="0.1")
       cube_3.addObject('UncoupledConstraintCorrection', )

       visu = CUBE_3.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_4", filename="mesh/cube.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_4", color="0 1 1 1.0")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       colli_cube = CUBE_3.addChild('ColliCube')

       colli_cube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj")
       colli_cube.addObject('MeshTopology', src="@loader")
       colli_cube.addObject('MechanicalObject', src="@loader", scale="1.0")
       colli_cube.addObject('TriangleCollisionModel', )
       colli_cube.addObject('LineCollisionModel', )
       colli_cube.addObject('PointCollisionModel', )
       colli_cube.addObject('RigidMapping', )

       constraints = CUBE_3.addChild('Constraints')

       constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1.25 1.25 -1.25")
       constraints.addObject('RigidMapping', )

       root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_2/Constraints/points", object2="@CUBE_3/Constraints/points", first_point="1", second_point="0")

       cube_4 = root.addChild('CUBE_4')

       cube_4.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       cube_4.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
       cube_4.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="-2.5", dz="-2.5")
       cube_4.addObject('UniformMass', totalMass="0.1")
       cube_4.addObject('UncoupledConstraintCorrection', )

       visu = CUBE_4.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/cube.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="0 0 1 1.0")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       colli_cube = CUBE_4.addChild('ColliCube')

       colli_cube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj")
       colli_cube.addObject('MeshTopology', src="@loader")
       colli_cube.addObject('MechanicalObject', src="@loader", scale="1.0")
       colli_cube.addObject('TriangleCollisionModel', )
       colli_cube.addObject('LineCollisionModel', )
       colli_cube.addObject('PointCollisionModel', )
       colli_cube.addObject('RigidMapping', )

       constraints = CUBE_4.addChild('Constraints')

       constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1.25 -1.25 1.25	1.25 1.25 1.25")
       constraints.addObject('RigidMapping', )

       root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_2/Constraints/points", object2="@CUBE_4/Constraints/points", first_point="1", second_point="0")
    ```

BilateralLagrangianConstraint_with_regularization_unsolvable.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <!-- BilateralLagrangianConstraint example -->
    <Node name="root" dt="0.001" gravity="0 0 -9.81">
        <RequiredPlugin name="Sofa.Component.AnimationLoop"/> <!-- Needed to use components [FreeMotionAnimationLoop] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [LinearSolverConstraintCorrection] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Model"/> <!-- Needed to use components [BilateralLagrangianConstraint] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Solver"/> <!-- Needed to use components [GenericConstraintSolver] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [SparseLDLSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        
        <VisualStyle displayFlags="showForceFields" />
        <DefaultVisualManagerLoop />
        <FreeMotionAnimationLoop />
        <GenericConstraintSolver tolerance="0.0001" maxIterations="1000" resolutionMethod="ProjectedGaussSeidel" regularizationTerm="0.0"/>
    
    
        <Node name="TargetCube00">
            <RegularGridTopology name="grid" nx="4" ny="4" nz="1" xmin="-1" xmax="1" ymin="-1" ymax="1" zmin="-0.5" zmax="-0.5" />
            <MechanicalObject name="mstate" template="Vec3" showObject="true" showObjectScale="0.05" drawMode="1" showColor="1 0.2 0.5 1"/>
            <BoxROI name="bottom" box="-1.1 -1.1 -1.1  1.1 1.1 -0.4" />
        </Node>
        <Node name="TargetCube10">
            <RegularGridTopology name="grid" nx="4" ny="4" nz="1" xmin="-1" xmax="1" ymin="-1" ymax="1" zmin="-1" zmax="-1" />
            <MechanicalObject name="mstate" template="Vec3" showObject="true" showObjectScale="0.05" drawMode="1" showColor="0.2 1 0.5 1"/>
            <BoxROI name="bottom" box="-1.1 -1.1 -1.1  1.1 1.1 -0.4" />
        </Node>
    
        <Node name="DeformableCube0">
    
            <VisualStyle displayFlags="showForceFields" />
            <EulerImplicitSolver name="odesolver" printLog="false" />
            <SparseLDLSolver name="linearSolver" template="CompressedRowSparseMatrixMat3x3d" />
    
            <RegularGridTopology name="grid" nx="4" ny="4" nz="4" xmin="-1" xmax="1" ymin="-1" ymax="1" zmin="-1" zmax="1" />
            <MechanicalObject name="mstate" template="Vec3" />
            <HexahedronFEMForceField poissonRatio="0.49" youngModulus="700000"/>
            <UniformMass totalMass="10" />
            <BoxROI name="bottom" box="-1.1 -1.1 -1.1  1.1 1.1 -0.9" />
            <BoxROI name="top" box="-1.1 -1.1 0.9  1.1 1.1 1.1" />
            <LinearSolverConstraintCorrection linearSolver="@linearSolver"/>
        </Node>
    
        <BilateralLagrangianConstraint template="Vec3"
                                       object1="@DeformableCube0/mstate" first_point="@DeformableCube0/bottom.indices"
                                       object2="@TargetCube00/mstate" second_point="@TargetCube00/bottom.indices" />
    
        <BilateralLagrangianConstraint template="Vec3"
                                       object1="@DeformableCube0/mstate" first_point="@DeformableCube0/bottom.indices"
                                       object2="@TargetCube10/mstate" second_point="@TargetCube10/bottom.indices" />
    
    
        <Node name="TargetCube01">
            <RegularGridTopology name="grid" nx="4" ny="4" nz="1" xmin="2" xmax="4" ymin="-1" ymax="1" zmin="-0.5" zmax="-0.5" />
            <MechanicalObject name="mstate" template="Vec3" showObject="true" showObjectScale="0.05" drawMode="1" showColor="1 0.2 0.5 1"/>
            <BoxROI name="bottom" box="1.9 -1.1 -1.1  4.1 1.1 -0.4" />
        </Node>
        <Node name="TargetCube11">
            <RegularGridTopology name="grid" nx="4" ny="4" nz="1" xmin="2" xmax="4" ymin="-1" ymax="1" zmin="-1" zmax="-1" />
            <MechanicalObject name="mstate" template="Vec3" showObject="true" showObjectScale="0.05" drawMode="1" showColor="0.2 1 0.5 1"/>
            <BoxROI name="bottom" box="1.9 -1.1 -1.1  4.1 1.1 -0.4" />
        </Node>
    
        <Node name="DeformableCube1">
    
            <VisualStyle displayFlags="showForceFields" />
            <EulerImplicitSolver name="odesolver" printLog="false" />
            <SparseLDLSolver name="linearSolver" template="CompressedRowSparseMatrixMat3x3d" />
    
            <RegularGridTopology name="grid" nx="4" ny="4" nz="4" xmin="2" xmax="4" ymin="-1" ymax="1" zmin="-1" zmax="1" />
            <MechanicalObject name="mstate" template="Vec3" />
            <HexahedronFEMForceField poissonRatio="0.49" youngModulus="700000"/>
            <UniformMass totalMass="10" />
            <BoxROI name="bottom" box="1.9 -1.1 -1.1  4.1 1.1 -0.9" />
            <BoxROI name="top" box="1.9 -1.1 0.9  4.1 1.1 1.1" />
            <LinearSolverConstraintCorrection linearSolver="@linearSolver" regularizationTerm="0.01"/>
        </Node>
    
        <BilateralLagrangianConstraint template="Vec3"
                                       object1="@DeformableCube1/mstate" first_point="@DeformableCube1/bottom.indices"
                                       object2="@TargetCube01/mstate" second_point="@TargetCube01/bottom.indices" />
    
        <BilateralLagrangianConstraint template="Vec3"
                                       object1="@DeformableCube1/mstate" first_point="@DeformableCube1/bottom.indices"
                                       object2="@TargetCube11/mstate" second_point="@TargetCube11/bottom.indices" />
    
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.001", gravity="0 0 -9.81")

       root.addObject('RequiredPlugin', name="Sofa.Component.AnimationLoop")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Model")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Solver")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('VisualStyle', displayFlags="showForceFields")
       root.addObject('DefaultVisualManagerLoop', )
       root.addObject('FreeMotionAnimationLoop', )
       root.addObject('GenericConstraintSolver', tolerance="0.0001", maxIterations="1000", resolutionMethod="ProjectedGaussSeidel", regularizationTerm="0.0")

       target_cube00 = root.addChild('TargetCube00')

       target_cube00.addObject('RegularGridTopology', name="grid", nx="4", ny="4", nz="1", xmin="-1", xmax="1", ymin="-1", ymax="1", zmin="-0.5", zmax="-0.5")
       target_cube00.addObject('MechanicalObject', name="mstate", template="Vec3", showObject="true", showObjectScale="0.05", drawMode="1", showColor="1 0.2 0.5 1")
       target_cube00.addObject('BoxROI', name="bottom", box="-1.1 -1.1 -1.1  1.1 1.1 -0.4")

       target_cube10 = root.addChild('TargetCube10')

       target_cube10.addObject('RegularGridTopology', name="grid", nx="4", ny="4", nz="1", xmin="-1", xmax="1", ymin="-1", ymax="1", zmin="-1", zmax="-1")
       target_cube10.addObject('MechanicalObject', name="mstate", template="Vec3", showObject="true", showObjectScale="0.05", drawMode="1", showColor="0.2 1 0.5 1")
       target_cube10.addObject('BoxROI', name="bottom", box="-1.1 -1.1 -1.1  1.1 1.1 -0.4")

       deformable_cube0 = root.addChild('DeformableCube0')

       deformable_cube0.addObject('VisualStyle', displayFlags="showForceFields")
       deformable_cube0.addObject('EulerImplicitSolver', name="odesolver", printLog="false")
       deformable_cube0.addObject('SparseLDLSolver', name="linearSolver", template="CompressedRowSparseMatrixMat3x3d")
       deformable_cube0.addObject('RegularGridTopology', name="grid", nx="4", ny="4", nz="4", xmin="-1", xmax="1", ymin="-1", ymax="1", zmin="-1", zmax="1")
       deformable_cube0.addObject('MechanicalObject', name="mstate", template="Vec3")
       deformable_cube0.addObject('HexahedronFEMForceField', poissonRatio="0.49", youngModulus="700000")
       deformable_cube0.addObject('UniformMass', totalMass="10")
       deformable_cube0.addObject('BoxROI', name="bottom", box="-1.1 -1.1 -1.1  1.1 1.1 -0.9")
       deformable_cube0.addObject('BoxROI', name="top", box="-1.1 -1.1 0.9  1.1 1.1 1.1")
       deformable_cube0.addObject('LinearSolverConstraintCorrection', linearSolver="@linearSolver")

       root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@DeformableCube0/mstate", first_point="@DeformableCube0/bottom.indices", object2="@TargetCube00/mstate", second_point="@TargetCube00/bottom.indices")
       root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@DeformableCube0/mstate", first_point="@DeformableCube0/bottom.indices", object2="@TargetCube10/mstate", second_point="@TargetCube10/bottom.indices")

       target_cube01 = root.addChild('TargetCube01')

       target_cube01.addObject('RegularGridTopology', name="grid", nx="4", ny="4", nz="1", xmin="2", xmax="4", ymin="-1", ymax="1", zmin="-0.5", zmax="-0.5")
       target_cube01.addObject('MechanicalObject', name="mstate", template="Vec3", showObject="true", showObjectScale="0.05", drawMode="1", showColor="1 0.2 0.5 1")
       target_cube01.addObject('BoxROI', name="bottom", box="1.9 -1.1 -1.1  4.1 1.1 -0.4")

       target_cube11 = root.addChild('TargetCube11')

       target_cube11.addObject('RegularGridTopology', name="grid", nx="4", ny="4", nz="1", xmin="2", xmax="4", ymin="-1", ymax="1", zmin="-1", zmax="-1")
       target_cube11.addObject('MechanicalObject', name="mstate", template="Vec3", showObject="true", showObjectScale="0.05", drawMode="1", showColor="0.2 1 0.5 1")
       target_cube11.addObject('BoxROI', name="bottom", box="1.9 -1.1 -1.1  4.1 1.1 -0.4")

       deformable_cube1 = root.addChild('DeformableCube1')

       deformable_cube1.addObject('VisualStyle', displayFlags="showForceFields")
       deformable_cube1.addObject('EulerImplicitSolver', name="odesolver", printLog="false")
       deformable_cube1.addObject('SparseLDLSolver', name="linearSolver", template="CompressedRowSparseMatrixMat3x3d")
       deformable_cube1.addObject('RegularGridTopology', name="grid", nx="4", ny="4", nz="4", xmin="2", xmax="4", ymin="-1", ymax="1", zmin="-1", zmax="1")
       deformable_cube1.addObject('MechanicalObject', name="mstate", template="Vec3")
       deformable_cube1.addObject('HexahedronFEMForceField', poissonRatio="0.49", youngModulus="700000")
       deformable_cube1.addObject('UniformMass', totalMass="10")
       deformable_cube1.addObject('BoxROI', name="bottom", box="1.9 -1.1 -1.1  4.1 1.1 -0.9")
       deformable_cube1.addObject('BoxROI', name="top", box="1.9 -1.1 0.9  4.1 1.1 1.1")
       deformable_cube1.addObject('LinearSolverConstraintCorrection', linearSolver="@linearSolver", regularizationTerm="0.01")

       root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@DeformableCube1/mstate", first_point="@DeformableCube1/bottom.indices", object2="@TargetCube01/mstate", second_point="@TargetCube01/bottom.indices")
       root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@DeformableCube1/mstate", first_point="@DeformableCube1/bottom.indices", object2="@TargetCube11/mstate", second_point="@TargetCube11/bottom.indices")
    ```

BilateralLagrangianConstraint_Rigid.scn

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
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.1", gravity="0 -0.981 0")

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
       root.addObject('FreeMotionAnimationLoop', )
       root.addObject('GenericConstraintSolver', tolerance="0.001", maxIterations="1000")

       beam1 = root.addChild('Beam1')

       beam1.addObject('EulerImplicitSolver', name="odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       beam1.addObject('BTDLinearSolver', printLog="false", verbose="false")
       beam1.addObject('MechanicalObject', template="Rigid3", name="DOFs1", position="0 0 0 0 0 0 1  1 0 0 0 0 0 1  2 0 0 0 0 0 1  3 0 0 0 0 0 1  4 0 0 0 0 0 1  5 0 0 0 0 0 1  6 0 0 0 0 0 1  7 0 0 0 0 0 1")
       beam1.addObject('MeshTopology', name="lines", lines="0 1 1 2 2 3 3 4 4 5 5 6 6 7")
       beam1.addObject('UniformMass', vertexMass="1 1 0.01 0 0 0 0.1 0 0 0 0.1 0", printLog="false")
       beam1.addObject('BeamFEMForceField', name="FEM", poissonRatio="0.49", radius="0.1", youngModulus="2000000")
       beam1.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="7")
       beam1.addObject('LinearSolverConstraintCorrection', )
       beam1.addObject('SphereCollisionModel', radius="0.1", group="1")

       constraint_point = Beam1.addChild('ConstraintPoint')

       constraint_point.addObject('MechanicalObject', template="Rigid3", name="dof1", position="0 0 0 0 0 -0.707107 0.707107 ")
       constraint_point.addObject('RigidMapping', index="0")

       beam2 = root.addChild('Beam2')

       beam2.addObject('EulerImplicitSolver', name="odesolver", printLog="false")
       beam2.addObject('BTDLinearSolver', printLog="false", verbose="false")
       beam2.addObject('MechanicalObject', template="Rigid3", name="DOFs2", position="0 0 0 0 0 -0.707107 0.707107 0 -1 0 0 0-0.707107 0.707107  0 -2 0 0 0 -0.707107 0.707107  0 -3 0 0 0 -0.707107 0.707107  0 -4 0 0 0 -0.707107 0.707107  0 -5 0 0 0 -0.707107 0.707107  0 -6 0 0 0 -0.707107 0.707107  0 -7 0 0 0 -0.707107 0.707107")
       beam2.addObject('MeshTopology', name="lines", lines="0 1 1 2 2 3 3 4 4 5 5 6 6 7")
       beam2.addObject('UniformMass', vertexMass="1 1 0.01 0 0 0 0.1 0 0 0 0.1 0", printLog="false")
       beam2.addObject('BeamFEMForceField', name="FEM", poissonRatio="0.49", radius="0.1", youngModulus="20000000")
       beam2.addObject('LinearSolverConstraintCorrection', )
       beam2.addObject('SphereCollisionModel', radius="0.1", group="1")

       root.addObject('BilateralLagrangianConstraint', template="Rigid3", object1="@Beam1/ConstraintPoint/dof1", object2="@Beam2/DOFs2", first_point="0", second_point="0")
    ```

BilateralLagrangianConstraint_NNCG.scn

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
                <TriangleCollisionModel />
                <LineCollisionModel />
                <PointCollisionModel />
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
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.001", gravity="0 -981 0")

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
       root.addObject('DefaultVisualManagerLoop', )
       root.addObject('FreeMotionAnimationLoop', )
       root.addObject('GenericConstraintSolver', tolerance="0.001", maxIterations="1000", resolutionMethod="NonsmoothNonlinearConjugateGradient", newtonIterations="100")
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('LocalMinDistance', name="Proximity", alarmDistance="0.2", contactDistance="0.09", angleCone="0.0")
       root.addObject('CollisionResponse', name="Response", response="FrictionContactConstraint")

       cube_0 = root.addChild('CUBE_0')

       cube_0.addObject('MechanicalObject', dy="2.5")

       visu = CUBE_0.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/cube.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="1 0 0 1", dy="2.5")

       colli_cube = CUBE_0.addChild('ColliCube')

       colli_cube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj", triangulate="1")
       colli_cube.addObject('MeshTopology', src="@loader")
       colli_cube.addObject('MechanicalObject', src="@loader", template="Vec3", dy="2.5")
       colli_cube.addObject('TriangleCollisionModel', simulated="0", moving="0")
       colli_cube.addObject('LineCollisionModel', simulated="0", moving="0")
       colli_cube.addObject('PointCollisionModel', simulated="0", moving="0")

       constraints = CUBE_0.addChild('Constraints')

       constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1 1.25 1")

       cube_1 = root.addChild('CUBE_1')

       cube_1.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       cube_1.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
       cube_1.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="0", dz="0.0")
       cube_1.addObject('UniformMass', totalMass="0.1")
       cube_1.addObject('UncoupledConstraintCorrection', )

       visu = CUBE_1.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/cube.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_2", color="1 1 0 1.0")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       colli_cube = CUBE_1.addChild('ColliCube')

       colli_cube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj", triangulate="1")
       colli_cube.addObject('MeshTopology', src="@loader")
       colli_cube.addObject('MechanicalObject', src="@loader")
       colli_cube.addObject('TriangleCollisionModel', )
       colli_cube.addObject('LineCollisionModel', )
       colli_cube.addObject('PointCollisionModel', )
       colli_cube.addObject('RigidMapping', )

       constraints = CUBE_1.addChild('Constraints')

       constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1 1.25 1	-1.25 -1.25 1.25")
       constraints.addObject('RigidMapping', )

       root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_0/Constraints/points", object2="@CUBE_1/Constraints/points", first_point="0", second_point="0")

       cube_2 = root.addChild('CUBE_2')

       cube_2.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       cube_2.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
       cube_2.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="-2.5", dz="0.0")
       cube_2.addObject('UniformMass', totalMass="0.1")
       cube_2.addObject('UncoupledConstraintCorrection', )

       visu = CUBE_2.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/cube.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_3", color="0 1 0 1.0")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       colli_cube = CUBE_2.addChild('ColliCube')

       colli_cube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj")
       colli_cube.addObject('MeshTopology', src="@loader")
       colli_cube.addObject('MechanicalObject', src="@loader", scale="1.0")
       colli_cube.addObject('TriangleCollisionModel', )
       colli_cube.addObject('LineCollisionModel', )
       colli_cube.addObject('PointCollisionModel', )
       colli_cube.addObject('RigidMapping', )

       constraints = CUBE_2.addChild('Constraints')

       constraints.addObject('MechanicalObject', name="points", template="Vec3", position="-1.25 1.25 1.25	1.25 -1.25 -1.25")
       constraints.addObject('RigidMapping', )

       root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_1/Constraints/points", object2="@CUBE_2/Constraints/points", first_point="1", second_point="0")

       cube_3 = root.addChild('CUBE_3')

       cube_3.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       cube_3.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
       cube_3.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="-5.0", dz="0.0")
       cube_3.addObject('UniformMass', totalMass="0.1")
       cube_3.addObject('UncoupledConstraintCorrection', )

       visu = CUBE_3.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_4", filename="mesh/cube.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_4", color="0 1 1 1.0")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       colli_cube = CUBE_3.addChild('ColliCube')

       colli_cube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj")
       colli_cube.addObject('MeshTopology', src="@loader")
       colli_cube.addObject('MechanicalObject', src="@loader", scale="1.0")
       colli_cube.addObject('TriangleCollisionModel', )
       colli_cube.addObject('LineCollisionModel', )
       colli_cube.addObject('PointCollisionModel', )
       colli_cube.addObject('RigidMapping', )

       constraints = CUBE_3.addChild('Constraints')

       constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1.25 1.25 -1.25")
       constraints.addObject('RigidMapping', )

       root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_2/Constraints/points", object2="@CUBE_3/Constraints/points", first_point="1", second_point="0")

       cube_4 = root.addChild('CUBE_4')

       cube_4.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       cube_4.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
       cube_4.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="-2.5", dz="-2.5")
       cube_4.addObject('UniformMass', totalMass="0.1")
       cube_4.addObject('UncoupledConstraintCorrection', )

       visu = CUBE_4.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/cube.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="0 0 1 1.0")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       colli_cube = CUBE_4.addChild('ColliCube')

       colli_cube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj")
       colli_cube.addObject('MeshTopology', src="@loader")
       colli_cube.addObject('MechanicalObject', src="@loader", scale="1.0")
       colli_cube.addObject('TriangleCollisionModel', )
       colli_cube.addObject('LineCollisionModel', )
       colli_cube.addObject('PointCollisionModel', )
       colli_cube.addObject('RigidMapping', )

       constraints = CUBE_4.addChild('Constraints')

       constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1.25 -1.25 1.25	1.25 1.25 1.25")
       constraints.addObject('RigidMapping', )

       root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_2/Constraints/points", object2="@CUBE_4/Constraints/points", first_point="1", second_point="0")
    ```

BilateralLagrangianConstraint_Soft_Rigid_Bodies.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="0 -9.81 0" dt="0.01">
        
        <Node name="plugins" >
            <RequiredPlugin name="Sofa.Component.AnimationLoop"/> <!-- Needed to use components [FreeMotionAnimationLoop] -->
            <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
            <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
            <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [LinearSolverConstraintCorrection UncoupledConstraintCorrection] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Model"/> <!-- Needed to use components [BilateralLagrangianConstraint] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Solver"/> <!-- Needed to use components [GenericConstraintSolver] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [LinearMovementProjectiveConstraint] -->
            <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [SparseLDLSolver] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
            <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping IdentityMapping] -->
            <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [HexahedronSetTopologyContainer TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
            <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping Tetra2TriangleTopologicalMapping] -->
            <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
            <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        </Node>
    
    
        <FreeMotionAnimationLoop computeBoundingBox="0"/>
        <GenericConstraintSolver maxIterations="1000" tolerance="1e-3"/>
        
        <VisualStyle displayFlags="showBehaviorModels showVisual showForceFields" />
        <CollisionPipeline name="CollisionLoop" verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="CollisionReponse" response="FrictionContactConstraint" />
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
        
    
        <Node name="DeformableGrid" >
            <RegularGridTopology name="grid" n="6 6 6" min="-10 -10 -10" max="10 10 10" p0="-10 -10 -10" />
            <HexahedronSetTopologyContainer name="Container" src="@grid"/>
            <MechanicalObject template="Vec3d" name="gridDofs"/>
    
            <Node name="DeformableCube" bbox="-10 -10 -10 10 10 10" >
                <EulerImplicitSolver name="cg_odesolver" />
                <SparseLDLSolver name="linear solver" template="CompressedRowSparseMatrixMat3x3d" />
                <TetrahedronSetTopologyContainer name="Container" />
                <TetrahedronSetTopologyModifier name="Modifier" />
                <TetrahedronSetGeometryAlgorithms template="Vec3d" name="GeomAlgo" />
                <MechanicalObject template="Vec3d" name="DeformableDoFs" position="@../gridDofs.position"/>
                <Hexa2TetraTopologicalMapping name="ExtratTetraMapping" input="@../Container" output="@Container" />
    
                <UniformMass template="Vec3d" name="NodalMass" vertexMass="0.25" />
                <TetrahedronFEMForceField template="Vec3d" name="LinearElasticity" method="large" poissonRatio="0.4" youngModulus="500" />
                <BoxROI template="Vec3d" name="box_roi" box="-11 -11 -11 11 -9 11" indices="0" drawSize="0" />
    
                <LinearSolverConstraintCorrection />
    
                <!-- Interface (of soft body) between both bodies -->
                <Node name="MappedInterface" >
                    <MechanicalObject template="Vec3d" name="MappedDoFs" position="@../box_roi.pointsInROI" showObject="1" showObjectScale="0"/>
                    <BarycentricMapping input="@../DeformableDoFs" output="@MappedDoFs" />
                </Node>
    
                <Node name="Visualization" >
                    <TriangleSetTopologyContainer name="Container" />
                    <TriangleSetTopologyModifier name="Modifier" />
                    <TriangleSetGeometryAlgorithms name="GeomAlgo" />
                    <Tetra2TriangleTopologicalMapping name="ExtractSurfaceMapping" input="@../Container" output="@Container" />
    
                    <Node name="VisualModel" >
                        <OglModel name="VisualModel" material="Default Diffuse 1 1 0 0 0.5 Ambient 1 0.2 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45" position="@../../DeformableDoFs.position" triangles="@Container.triangles"/>
                        <IdentityMapping template="Vec3d,Vec3d" name="VisualMapping" input="@../../DeformableDoFs" output="@VisualModel" />
                    </Node>
                </Node>
            </Node>
        </Node>
    
    
        <!-- Rigid body -->
        <Node name="RigidBody" >
            <EulerImplicitSolver name="EulerImplicit" />
            <CGLinearSolver template="GraphScattered" name="CG-LinearSolver" iterations="25" tolerance="1e-09" threshold="1e-09" />
            <MechanicalObject template="Rigid3d" name="rigidDofs" position="0 -15 0 0 0 0 1" showObject="1" showObjectScale="5"/>
            <UniformMass name="NodalMass" totalMass="1" />
            <LinearMovementProjectiveConstraint template="Rigid3" name="MotionConstraint" keyTimes="0 1 2 10 15 9999" movements="0 0 0   0 0 0
                                                  0 -5 0   0 0 0
                                                  0 0 -1  0 0 0
                                                  0 0 -1  0 0 6.3
                                                  0 0 -1   0 0 0
                                                  0 0 -1   0 0 0" />
            <UncoupledConstraintCorrection />
            
            <!-- Interface (of rigid body) between both bodies -->
            <Node name="MappedRigidInterface" >
                <MechanicalObject template="Vec3d" name="MappedDoFs" position="@DeformableGrid/DeformableCube/box_roi.pointsInROI"  showObject="1" showObjectScale="10" />
                <RigidMapping input="@../rigidDofs" output="@MappedDoFs" globalToLocalCoords="1"/>
            </Node>
        </Node>
    
    
    
        <BilateralLagrangianConstraint template="Vec3d" name="Attachment" object1="@DeformableGrid/DeformableCube/MappedInterface" object2="@RigidBody/MappedRigidInterface" first_point="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35" second_point="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35" />
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9.81 0", dt="0.01")

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', name="Sofa.Component.AnimationLoop")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Model")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Solver")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       plugins.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")

       root.addObject('FreeMotionAnimationLoop', computeBoundingBox="0")
       root.addObject('GenericConstraintSolver', maxIterations="1000", tolerance="1e-3")
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual showForceFields")
       root.addObject('CollisionPipeline', name="CollisionLoop", verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', name="CollisionReponse", response="FrictionContactConstraint")
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")

       deformable_grid = root.addChild('DeformableGrid')

       deformable_grid.addObject('RegularGridTopology', name="grid", n="6 6 6", min="-10 -10 -10", max="10 10 10", p0="-10 -10 -10")
       deformable_grid.addObject('HexahedronSetTopologyContainer', name="Container", src="@grid")
       deformable_grid.addObject('MechanicalObject', template="Vec3d", name="gridDofs")

       deformable_cube = DeformableGrid.addChild('DeformableCube', bbox="-10 -10 -10 10 10 10")

       deformable_cube.addObject('EulerImplicitSolver', name="cg_odesolver")
       deformable_cube.addObject('SparseLDLSolver', name="linear solver", template="CompressedRowSparseMatrixMat3x3d")
       deformable_cube.addObject('TetrahedronSetTopologyContainer', name="Container")
       deformable_cube.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       deformable_cube.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3d", name="GeomAlgo")
       deformable_cube.addObject('MechanicalObject', template="Vec3d", name="DeformableDoFs", position="@../gridDofs.position")
       deformable_cube.addObject('Hexa2TetraTopologicalMapping', name="ExtratTetraMapping", input="@../Container", output="@Container")
       deformable_cube.addObject('UniformMass', template="Vec3d", name="NodalMass", vertexMass="0.25")
       deformable_cube.addObject('TetrahedronFEMForceField', template="Vec3d", name="LinearElasticity", method="large", poissonRatio="0.4", youngModulus="500")
       deformable_cube.addObject('BoxROI', template="Vec3d", name="box_roi", box="-11 -11 -11 11 -9 11", indices="0", drawSize="0")
       deformable_cube.addObject('LinearSolverConstraintCorrection', )

       mapped_interface = DeformableCube.addChild('MappedInterface')

       mapped_interface.addObject('MechanicalObject', template="Vec3d", name="MappedDoFs", position="@../box_roi.pointsInROI", showObject="1", showObjectScale="0")
       mapped_interface.addObject('BarycentricMapping', input="@../DeformableDoFs", output="@MappedDoFs")

       visualization = DeformableCube.addChild('Visualization')

       visualization.addObject('TriangleSetTopologyContainer', name="Container")
       visualization.addObject('TriangleSetTopologyModifier', name="Modifier")
       visualization.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo")
       visualization.addObject('Tetra2TriangleTopologicalMapping', name="ExtractSurfaceMapping", input="@../Container", output="@Container")

       visual_model = Visualization.addChild('VisualModel')

       visual_model.addObject('OglModel', name="VisualModel", material="Default Diffuse 1 1 0 0 0.5 Ambient 1 0.2 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45", position="@../../DeformableDoFs.position", triangles="@Container.triangles")
       visual_model.addObject('IdentityMapping', template="Vec3d,Vec3d", name="VisualMapping", input="@../../DeformableDoFs", output="@VisualModel")

       rigid_body = root.addChild('RigidBody')

       rigid_body.addObject('EulerImplicitSolver', name="EulerImplicit")
       rigid_body.addObject('CGLinearSolver', template="GraphScattered", name="CG-LinearSolver", iterations="25", tolerance="1e-09", threshold="1e-09")
       rigid_body.addObject('MechanicalObject', template="Rigid3d", name="rigidDofs", position="0 -15 0 0 0 0 1", showObject="1", showObjectScale="5")
       rigid_body.addObject('UniformMass', name="NodalMass", totalMass="1")
       rigid_body.addObject('LinearMovementProjectiveConstraint', template="Rigid3", name="MotionConstraint", keyTimes="0 1 2 10 15 9999", movements="0 0 0   0 0 0                                               0 -5 0   0 0 0                                               0 0 -1  0 0 0                                               0 0 -1  0 0 6.3                                               0 0 -1   0 0 0                                               0 0 -1   0 0 0")
       rigid_body.addObject('UncoupledConstraintCorrection', )

       mapped_rigid_interface = RigidBody.addChild('MappedRigidInterface')

       mapped_rigid_interface.addObject('MechanicalObject', template="Vec3d", name="MappedDoFs", position="@DeformableGrid/DeformableCube/box_roi.pointsInROI", showObject="1", showObjectScale="10")
       mapped_rigid_interface.addObject('RigidMapping', input="@../rigidDofs", output="@MappedDoFs", globalToLocalCoords="1")

       root.addObject('BilateralLagrangianConstraint', template="Vec3d", name="Attachment", object1="@DeformableGrid/DeformableCube/MappedInterface", object2="@RigidBody/MappedRigidInterface", first_point="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35", second_point="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35")
    ```

BilateralLagrangianConstraint_PGS.scn

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
                <TriangleCollisionModel />
                <LineCollisionModel />
                <PointCollisionModel />
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
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.001", gravity="0 -981 0")

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
       root.addObject('DefaultVisualManagerLoop', )
       root.addObject('FreeMotionAnimationLoop', )
       root.addObject('GenericConstraintSolver', tolerance="0.001", maxIterations="1000", resolutionMethod="ProjectedGaussSeidel")
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('LocalMinDistance', name="Proximity", alarmDistance="0.2", contactDistance="0.09", angleCone="0.0")
       root.addObject('CollisionResponse', name="Response", response="FrictionContactConstraint")

       cube_0 = root.addChild('CUBE_0')

       cube_0.addObject('MechanicalObject', dy="2.5")

       visu = CUBE_0.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/cube.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="1 0 0 1", dy="2.5")

       colli_cube = CUBE_0.addChild('ColliCube')

       colli_cube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj", triangulate="1")
       colli_cube.addObject('MeshTopology', src="@loader")
       colli_cube.addObject('MechanicalObject', src="@loader", template="Vec3", dy="2.5")
       colli_cube.addObject('TriangleCollisionModel', simulated="0", moving="0")
       colli_cube.addObject('LineCollisionModel', simulated="0", moving="0")
       colli_cube.addObject('PointCollisionModel', simulated="0", moving="0")

       constraints = CUBE_0.addChild('Constraints')

       constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1 1.25 1")

       cube_1 = root.addChild('CUBE_1')

       cube_1.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       cube_1.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
       cube_1.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="0", dz="0.0")
       cube_1.addObject('UniformMass', totalMass="0.1")
       cube_1.addObject('UncoupledConstraintCorrection', )

       visu = CUBE_1.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/cube.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_2", color="1 1 0 1.0")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       colli_cube = CUBE_1.addChild('ColliCube')

       colli_cube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj", triangulate="1")
       colli_cube.addObject('MeshTopology', src="@loader")
       colli_cube.addObject('MechanicalObject', src="@loader")
       colli_cube.addObject('TriangleCollisionModel', )
       colli_cube.addObject('LineCollisionModel', )
       colli_cube.addObject('PointCollisionModel', )
       colli_cube.addObject('RigidMapping', )

       constraints = CUBE_1.addChild('Constraints')

       constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1 1.25 1	-1.25 -1.25 1.25")
       constraints.addObject('RigidMapping', )

       root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_0/Constraints/points", object2="@CUBE_1/Constraints/points", first_point="0", second_point="0")

       cube_2 = root.addChild('CUBE_2')

       cube_2.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       cube_2.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
       cube_2.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="-2.5", dz="0.0")
       cube_2.addObject('UniformMass', totalMass="0.1")
       cube_2.addObject('UncoupledConstraintCorrection', )

       visu = CUBE_2.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/cube.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_3", color="0 1 0 1.0")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       colli_cube = CUBE_2.addChild('ColliCube')

       colli_cube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj")
       colli_cube.addObject('MeshTopology', src="@loader")
       colli_cube.addObject('MechanicalObject', src="@loader", scale="1.0")
       colli_cube.addObject('TriangleCollisionModel', )
       colli_cube.addObject('LineCollisionModel', )
       colli_cube.addObject('PointCollisionModel', )
       colli_cube.addObject('RigidMapping', )

       constraints = CUBE_2.addChild('Constraints')

       constraints.addObject('MechanicalObject', name="points", template="Vec3", position="-1.25 1.25 1.25	1.25 -1.25 -1.25")
       constraints.addObject('RigidMapping', )

       root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_1/Constraints/points", object2="@CUBE_2/Constraints/points", first_point="1", second_point="0")

       cube_3 = root.addChild('CUBE_3')

       cube_3.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       cube_3.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
       cube_3.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="-5.0", dz="0.0")
       cube_3.addObject('UniformMass', totalMass="0.1")
       cube_3.addObject('UncoupledConstraintCorrection', )

       visu = CUBE_3.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_4", filename="mesh/cube.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_4", color="0 1 1 1.0")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       colli_cube = CUBE_3.addChild('ColliCube')

       colli_cube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj")
       colli_cube.addObject('MeshTopology', src="@loader")
       colli_cube.addObject('MechanicalObject', src="@loader", scale="1.0")
       colli_cube.addObject('TriangleCollisionModel', )
       colli_cube.addObject('LineCollisionModel', )
       colli_cube.addObject('PointCollisionModel', )
       colli_cube.addObject('RigidMapping', )

       constraints = CUBE_3.addChild('Constraints')

       constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1.25 1.25 -1.25")
       constraints.addObject('RigidMapping', )

       root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_2/Constraints/points", object2="@CUBE_3/Constraints/points", first_point="1", second_point="0")

       cube_4 = root.addChild('CUBE_4')

       cube_4.addObject('EulerImplicitSolver', printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       cube_4.addObject('CGLinearSolver', iterations="25", tolerance="1.0e-9", threshold="1.0e-9")
       cube_4.addObject('MechanicalObject', template="Rigid3", scale="1.0", dx="0.0", dy="-2.5", dz="-2.5")
       cube_4.addObject('UniformMass', totalMass="0.1")
       cube_4.addObject('UncoupledConstraintCorrection', )

       visu = CUBE_4.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/cube.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="0 0 1 1.0")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       colli_cube = CUBE_4.addChild('ColliCube')

       colli_cube.addObject('MeshOBJLoader', name="loader", filename="mesh/cube.obj")
       colli_cube.addObject('MeshTopology', src="@loader")
       colli_cube.addObject('MechanicalObject', src="@loader", scale="1.0")
       colli_cube.addObject('TriangleCollisionModel', )
       colli_cube.addObject('LineCollisionModel', )
       colli_cube.addObject('PointCollisionModel', )
       colli_cube.addObject('RigidMapping', )

       constraints = CUBE_4.addChild('Constraints')

       constraints.addObject('MechanicalObject', name="points", template="Vec3", position="1.25 -1.25 1.25	1.25 1.25 1.25")
       constraints.addObject('RigidMapping', )

       root.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@CUBE_2/Constraints/points", object2="@CUBE_4/Constraints/points", first_point="1", second_point="0")
    ```


<!-- automatically generated doc END -->
