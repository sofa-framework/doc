BilateralInteractionConstraint
==============================

This component belongs to the category of [Constraint Laws](https://www.sofa-framework.org/community/doc/simulation-principles/constraint/lagrange-constraint/#constraint-laws) used for the Lagrange constraint resolution and inherits from the PairInteractionConstraint. The BilateralInteractionConstraint defines an [holonomic constraint](https://en.wikipedia.org/wiki/Holonomic_constraints) law between a pair of simulated body, i.e. the constraint defined between the pair of objects must have an equality form:

<img class="latex" src="https://latex.codecogs.com/png.latex?\Phi(x_1,x_2%20...)~=~0" title="Holonomic constraint law" />

Such a constraint is suited for attachment cases or sliding joints. For an attachment case, if the vertex _i_ of object 1 and the vertex _j_ of object 2 are attached, the holonomic constraint law can be written as <img class="latex" src="https://latex.codecogs.com/png.latex?x_1(i)-x_2(j)~=~0" title="Attachment law" />.

For a BilateralInteractionConstraint, the constraint matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{H}" title="Constraint matrix" /> (derivative of the constraint law) corresponds to:

- <img src="https://latex.codecogs.com/gif.latex?\begin{equation*}&space;&\mathbf{H}_1&space;=&space;\begin{bmatrix}&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_0&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;1&space;&&space;0&space;&&space;0\\\end{bmatrix}_i&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_{N_1}\\&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_0&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;0&space;&&space;1&space;&&space;0\\\end{bmatrix}_i&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_{N_1}\\&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_0&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;1\\\end{bmatrix}_i&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_{N_1}\\&space;\end{bmatrix}&space;\end{equation*}" title="\begin{equation*} &\mathbf{H}_1 = \begin{bmatrix} \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 & \hdots & \begin{bmatrix} 1 & 0 & 0\\\end{bmatrix}_i & \hdots & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_1}\\ \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 & \hdots & \begin{bmatrix} 0 & 1 & 0\\\end{bmatrix}_i & \hdots & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_1}\\ \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 & \hdots & \begin{bmatrix} 0 & 0 & 1\\\end{bmatrix}_i & \hdots & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_1}\\ \end{bmatrix} \end{equation*}" /> for object 1
- <img src="https://latex.codecogs.com/gif.latex?\begin{equation*}&space;&\mathbf{H}_2&space;=&space;\begin{bmatrix}&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_0&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;-1&space;&&space;0&space;&&space;0\\\end{bmatrix}_j&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_{N_2}\\&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_0&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;0&space;&&space;-1&space;&&space;0\\\end{bmatrix}_j&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_{N_2}\\&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_0&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;-1\\\end{bmatrix}_j&space;&&space;\hdots&space;&&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0\\\end{bmatrix}_{N_2}\\&space;\end{bmatrix}&space;\end{equation*}" title="\begin{equation*} &\mathbf{H}_2 = \begin{bmatrix} \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 & \hdots & \begin{bmatrix} -1 & 0 & 0\\\end{bmatrix}_j & \hdots & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_2}\\ \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 & \hdots & \begin{bmatrix} 0 & -1 & 0\\\end{bmatrix}_j & \hdots & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_2}\\ \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_0 & \hdots & \begin{bmatrix} 0 & 0 & -1\\\end{bmatrix}_j & \hdots & \begin{bmatrix} 0 & 0 & 0\\\end{bmatrix}_{N_2}\\ \end{bmatrix} \end{equation*}" /> for object 2


As all constraint laws, the BilateralInteractionConstraint will be called in the following functions and for the following steps:

- `getConstraintViolation()`: project the free velocity in the constraint space and compute the free interpenetration <img src="https://latex.codecogs.com/gif.latex?\begin{equation}&space;&\dot{\delta}_1^{free}=\mathbf{H}_1v_1^{free}&space;\end{equation}" title="\begin{equation} &\dot{\delta}_1^{free}=\mathbf{H}_1v_1^{free} \end{equation}" />
- `buildConstraintMatrix()`: build the compliance made up of <img class="latex" src="https://latex.codecogs.com/png.latex?dt\mathbf{H}_1\mathbf{A}_1^{-1}\mathbf{H}_1^T" title="Compliance of object 1" /> and <img class="latex" src="https://latex.codecogs.com/png.latex?dt\mathbf{H}_2\mathbf{A}_2^{-1}\mathbf{H}_2^T" title="Compliance of object 2" />



Data  
----

As a PairInteractionConstraint, the BilateralInteractionConstraint requires the following Data:

- **object1**: link towards the object 1 to constraint
- **object2**: link towards the object 2 to constraint
- **first_point**: index of the constraint on the first model (object 1)
- **second_point**: index of the constraint on the second model (object 2)


Usage
-----

The BilateralInteractionConstraint can only be used in the context of [Lagrange constraint](https://www.sofa-framework.org/community/doc/simulation-principles/constraint/lagrange-constraint/) resolution. The scene must therefore contain:

- a FreeMotionAnimationLoop
- a ConstraintSolver

Moreover, each constrained object must define in its node a ConstraintCorrection so that the corrective motion can be applied.


Example
-------

This component is used as follows in XML format:

``` xml
<BilateralInteractionConstraint template="Vec3d" object1="@CUBE_2/Constraints/points" object2="@CUBE_4/Constraints/points" first_point="1" second_point="0" />
```

or using SofaPython3:

``` python
node.addObject('BilateralInteractionConstraint', template='Vec3d' object1='@CUBE_2/Constraints/points' object2='@CUBE_4/Constraints/points' first_point='1' second_point='0')
```

An example scene involving a BilateralInteractionConstraint is available in [*examples/Component/Constraint/Lagrangian/BilateralLagrangianConstraint_PGS.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/Constraint/Lagrangian/BilateralLagrangianConstraint_PGS.scn)
