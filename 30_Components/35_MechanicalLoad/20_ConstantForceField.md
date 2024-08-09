ConstantForceField
==================

This component belongs to the category of [ForceField](../../../simulation-principles/multi-model-representation/forcefield/). The ConstantForceField is a simple force field applying the same constant force on each node. This force field is not integrated over the domain of our object, but simply distributed over the number of nodes.


<a href="https://github.com/sofa-framework/doc/blob/master/images/FEM/ConstantForceField.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/FEM/ConstantForceField.png?raw=true" title="Nodal constant force over a liver mesh" style="width: 50%;text-align: center; "/></a>



Usage
-----

As a Forcefield, the ConstantForceField requires a **MechanicalObject** and the associated **solvers** (integration scheme and linear solver), as well as a **PointSetTopologyContainer**.
