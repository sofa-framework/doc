---
title: UnilateralLagrangianConstraint
---

UnilateralLagrangianConstraint
===============================


This component belongs to the category of [Constraint Laws](https://www.sofa-framework.org/community/doc/simulation-principles/constraint/lagrange-constraint/#constraint-laws) used for the Lagrange constraint resolution and inherits from the PairInteractionConstraint. The UnilateralLagrangianConstraint defines an [non-holonomic constraint](https://en.wikipedia.org/wiki/Nonholonomic_system) law between a pair of simulated body, i.e. the constraint defined between the pair of objects must have an inequality form:

<img class="latex" src="https://latex.codecogs.com/png.latex?\Psi(x_1,x_2%20...)~\geq~0" title="Non-holonomic constraint law" />

Such a constraint are used for friction-less and friction contact modeling (it can even be used as a starting point for puncture modeling). For a UnilateralLagrangianConstraint, the constraint matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{H}" title="Constraint matrix" /> (derivative of the constraint law) corresponds to:

- <img src="https://latex.codecogs.com/gif.latex?\begin{equation}&space;&\mathbf{H}_1&space;=&space;\begin{bmatrix}&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_0&space;&&space;\hdots&space;&&space;\vec{n}_i&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_{N_1}\\&space;\end{bmatrix}&space;\end{equation}" title="\begin{equation} &\mathbf{H}_1 = \begin{bmatrix} \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 & \hdots & \vec{n}_i & \hdots & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_1}\\ \end{bmatrix} \end{equation}" /> for object 1
- <img src="https://latex.codecogs.com/gif.latex?\begin{equation}&space;&\mathbf{H}_1&space;=&space;\begin{bmatrix}&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_0&space;&&space;\hdots&space;&&space;\vec{n}_j&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_{N_2}&space;\\&space;\end{bmatrix}&space;\end{equation}" title="\begin{equation} &\mathbf{H}_1 = \begin{bmatrix} \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 & \hdots & \vec{n}_j & \hdots & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_2} \\ \end{bmatrix} \end{equation}" /> for object 2

We can see from these matrices that the UnilateralLagrangianConstraint is a transformation towards the constraint space, by building a projection of any field against the contact direction (normal here, and possibly tangential directions as well if friction is defined).


As all constraint laws, the UnilateralLagrangianConstraint will be called in the following functions and for the following steps:

- `getConstraintViolation()`: project the free velocity in the constraint space and compute the free interpenetration <img src="https://latex.codecogs.com/gif.latex?\begin{equation}&space;&\dot{\delta}_1^{free}=\mathbf{H}_1v_1^{free}&space;\end{equation}" title="\begin{equation} &\dot{\delta}_1^{free}=\mathbf{H}_1v_1^{free} \end{equation}" />
- `buildConstraintMatrix()`: build the compliance made up of <img class="latex" src="https://latex.codecogs.com/png.latex?dt\mathbf{H}_1\mathbf{A}_1^{-1}\mathbf{H}_1^T" title="Compliance of object 1" /> and <img class="latex" src="https://latex.codecogs.com/png.latex?dt\mathbf{H}_2\mathbf{A}_2^{-1}\mathbf{H}_2^T" title="Compliance of object 2" />




Data  
----

As a PairInteractionConstraint, the UnilateralLagrangianConstraint requires the following Data:

- **object1**: link towards the object 1 to constraint
- **object2**: link towards the object 2 to constraint
- **first_point**: index of the constraint on the first model (object 1)
- **second_point**: index of the constraint on the second model (object 2)


Usage
-----

The UnilateralLagrangianConstraint can only be used in the context of [Lagrange constraint](https://www.sofa-framework.org/community/doc/simulation-principles/constraint/lagrange-constraint/) resolution. The scene must therefore contain:

- a FreeMotionAnimationLoop
- a ConstraintSolver

Moreover, each constrained object must define in its node a ConstraintCorrection so that the corrective motion can be applied. Unlike other constraints, the UnilateralLagrangianConstraint is mostly used in SOFA for contact modeling. UnilateralLagrangianConstraint are therefore dynamically and automatically created within the scene graph when two objects are colliding: when the CollisionPipeline defines new DetectionOutput with ContactResponse using Lagrange multipliers, each DetectionOutput generates a new UnilateralLagrangianConstraint.


Example
-------

An example scene involving a UnilateralLagrangianConstraint is available in [*examples/Component/Constraint/Lagrangian/FrictionContact_LCP_without_friction.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/Constraint/Lagrangian/FrictionContact_LCP_without_friction.scn). Note that in this example, the UnilateralLagrangianConstraint will be created as soon as a contact point is outputed from the collision detection phase.
<!-- automatically generated doc START -->
__Target__: `Sofa.Component.Constraint.Lagrangian.Model`

__namespace__: `#!c++ sofa::component::constraint::lagrangian::model`

__parents__: 

- `#!c++ PairInteractionConstraint`

__categories__: 

- ConstraintSet

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




<!-- automatically generated doc END -->
