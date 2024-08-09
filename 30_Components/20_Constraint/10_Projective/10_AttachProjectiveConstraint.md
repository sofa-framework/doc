AttachProjectiveConstraint
================

This component belongs to the category of [Projective Constraint](../../../../simulation-principles/constraint/projective-constraint/).
The AttachProjectiveConstraint works with a pair of objects, and it projects the degrees of freedom (e.g. position) and their derivatives (e.g. velocity), so that both objects are attached.
As being a projective constraint, this projective constraints ensures a geometrical connection between both objects at the end of the time step, but it does not integrate the physics of both object (contrary to Lagrange based constraints).


Note that constraining objects using the data **twoWay** will project the constraint vertices of both _object1_ and _object2_ towards their average degrees of freedom and derivatives:
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

The AttachProjectiveConstraint **requires** two MechanicalObjects so that both degrees of freedom can be accessed and projected to the attached configuration. An integration scheme and a solver are also necessary to solve the linear system at each time step.
