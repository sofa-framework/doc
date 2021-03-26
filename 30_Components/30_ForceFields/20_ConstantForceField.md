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

An example scene involving a ConstantForceField is available in [*examples/Components/forcefield/ConstantForceField.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/forcefield/ConstantForceField.scn)
