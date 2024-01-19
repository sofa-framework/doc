AttachConstraint
================

This component belongs to the category of [Projective Constraint](https://www.sofa-framework.org/community/doc/main-principles/constraint/projective-constraint/). The AttachConstraint works with a pair of objects and it projects the degrees of freedom (e.g. position) and their derivatives (e.g. velocity), so that both objects are attached. As being a projective constraint, this projective constraints ensures a geometrical connection between both objects at the end of the time step but it does not integrate the physics of both object (contrary to Lagrange based constraints).



Data 
----

The AttachConstraint can be initialized using three input data:

- **object1**: link to the first model (MechanicalModel)
- **object2**: link to the second model (MechanicalModel)
- **indices1**: corresponding to the indices of the source points on the first model
- **indices2**: corresponding to the indices of the fixed points on the second model
- **constraintFactor**: allows for the partial application of the constraint using this factor per pair of points constrained (0=the constraint is released. 1=the constraint is fully constrained)
- **twoWay**:
  - if true, this boolean projects the constraint vertices of both _object1_ and _object2_ towards their average degrees of freedom and derivatives: 
  ```cpp
  Deriv corr = (dx2-dx1)*0.5*responseFactor*getConstraintFactor(index);
        dx1 += corr;
        dx2 -= corr;
  ```
  - if false, the position of the _object1_ are projected onto the _object2_. Therefore, _object2_ only follows _object1_ without affecting the motion of _object1_
  ```cpp
  dx2 = Deriv();
  ```



Usage
-----

The AttachConstraint **requires** two MechanicalObjects so that both degrees of freedom can be accessed and projected to the attached configuration. An integration scheme and a solver are also necessary to solve the linear system at each time step.


Example
-------

This component is used as follows in XML format:

``` xml
<AttachConstraint name="AttachConstraint" object1="@M1" object2="@M2" indices1="0 1 2" indices2="10 11 12" constraintFactor="1 1 1"/>
```

or using SofaPython3:

``` python
node.addObject('AttachConstraint', object1="@M1", object2="@M2", indices1="0 1 2", indices2="10 11 12", constraintFactor="1 1 1")
```

An example scene involving a AttachConstraint is available in [*examples/Component/Constraint/Projective/AttachConstraint.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/Constraint/Projective/AttachConstraint.scn)
