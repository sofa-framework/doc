A simulation in SOFA is described as a scene with an intrinsic generalized hierarchy. This scene is composed of nodes organized as a tree or as a Directed Acyclic Graph (DAG). The different simulated objects are described in separate nodes, and different representations of a same object can be done in different sub-nodes.

Let's take some examples!

<div style="text-align:center;width:50%;margin: 0 25% 0;">

<img src="https://www.sofa-framework.org/wp-content/uploads/2016/05/Images-tuto.001.jpg" style="width: 65%;"/>
Fig. 1 - A graph with one single child node

</div>

#### Structure of a scene

The scene starts from a parent node, called the "Root" node. All other nodes (called child nodes) inherit from this main node. In the figure 1, a first child node "Liver" is defined and represents a first object. This "Liver" node includes components (solvers, forcefield, mass) used to build the simulation. Each of these components contains attributes. For instance, a component of mass features an attribute for mass density; an iterative linear solver needs an attribute defining a maximum of iterations. These attributes are also called Data. Two Data of a same type can be connected one with another.

<div style="text-align:center;width: 80%;margin: 0 10% 0;">

<img src="https://www.sofa-framework.org/wp-content/uploads/2016/05/Images-tuto.002.jpg" style="width: 100%;"/>
Fig. 2 - A graph with one object and its two representations (mechanics and visual)

</div>

As illustrated in figure 2, nodes can be structured serially in the graph. Such a hierarchical graph allows for having several representation of a same object. In the example, the first child node "Liver" implements the mechanical behavior of the liver (hexahedral mesh), whereas the sub-node "Visual" describes a surface model (triangular mesh) of the liver.

<div style="text-align:center;width:70%;margin: 0 15% 0;">

<img src="https://www.sofa-framework.org/wp-content/uploads/2016/05/Images-tuto.003.jpg" style="width: 100%;"/>
Fig. 3 - A graph including two different objects computed in the same simulation

</div>

The figure 3 shows a simulation involving two different objects. One node can compute the mechanical behavior of a liver whereas the second simulates the electrical behavior of a heart. These two systems rely on two different degrees of freedom, i.e. different physical phenomenon. This feature shows the ability of SOFA to easily develop advanced and coupled models.

To build a simulation in SOFA, the scene graph can be written both using:

*   XML files. Read the [associated page](https://www.sofa-framework.org/support/doc/using-sofa/write-a-scene-in-xml/) about how to write a scene in XML.
*   Python scripts. Read the [associated page](https://www.sofa-framework.org/support/doc/using-sofa/features/python-scripting/) about how to write in Python.

#### Visitors

During the different steps of the simulation (initialization, system assembly, solving, visualization), information needs to be recovered from all the graph nodes. An implicit mechanism based on visitors enables this. You can find the abstract class _Visitor.h_ in the SofaSimulation package.

For each of these steps, the operation implemented with the visitor can be described as:

*   a graph traversal,
*   abstract methods depending on the triggered action (ex: clearing an global vector, or accumulating forces),
*   and vector identificators.

Example: _accumulating the forces_.

Accumulating forces is used to compute all the forces (internal or external) applied on our object. The solver then triggers the associate visitor and the action is propagated through the graph and calls the appropriate (bottom-up) methods at each force and mapping node. All components able to compute forces will accumulate their contributions. This information is finally gathered in the MechanicalObject and the solver will use this "force" vector to solve the mathematical system.

<div style="text-align:center;width:50%;margin: 0 25% 0;">

<img src="https://www.sofa-framework.org/wp-content/uploads/2016/05/Images-tuto.0010.jpg" style="width: 90%;"/>
Fig. 4 - Traversing visitors triggered for the _accumulateForce()_ action

</div>
