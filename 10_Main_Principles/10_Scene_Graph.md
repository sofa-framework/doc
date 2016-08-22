A simulation in SOFA is described as a scene with an intrinsic generalized hierarchy. This scene is composed of nodes organized as a tree or as a Directed Acyclic Graph (DAG). The different simulated objects are described in separate nodes, and different representations of a same object can be done in different sub-nodes.

Let's take some examples!

<div style="text-align:center;width:50%;margin: 0 25% 0;">

<img src="https://www.sofa-framework.org/wp-content/uploads/2016/05/Images-tuto.001.jpg" style="width: 65%;"/>
Fig. 1 - A graph with one single child node

</div>

Structure of a scene
--------------------

The scene starts from a parent node, called the "Root" node. All other nodes (called child nodes) inherit from this main node. In the figure 1, a first child node "Liver" is defined and represents a first object. Usually, one node gathers the components associated with the same object (same degrees of freedom).

This design is highly modular, since components in the scene are independent of each other. One physical model (springs with _SpringForceField_) could be simply replaced by another one (triangular FEM with _TriangleFEMForceField_) by changing one component in the graph. In the same way, an explicit integration scheme (_EulerSolver_) could be replaced by an implicit one (_EulerImplicitSolver_) by modifying one XML line in the scene file. This high modularity of the framework is induced by the scenegraph-visitor approach described below.

<div style="text-align:center;width: 80%;margin: 0 10% 0;">

<img src="https://www.sofa-framework.org/wp-content/uploads/2016/05/Images-tuto.002.jpg" style="width: 100%;"/>
Fig. 2 - A graph with one object and its two representations (mechanics and visual)

</div>

As illustrated in figure 2, nodes can be structured serially in the graph. Such a hierarchical graph allows for having several representation of a same object. In the example, the first child node "Liver" implements the mechanical behavior of the liver (hexahedral mesh), whereas the sub-node "Visual" describes a surface model (triangular mesh) of the liver.

<div style="text-align:center;width:70%;margin: 0 15% 0;">

<img src="https://www.sofa-framework.org/wp-content/uploads/2016/05/Images-tuto.003.jpg" style="width: 100%;"/>
Fig. 3 - A graph including two different objects computed in the same simulation

</div>

The figure 3 shows a simulation involving two different objects. One node can compute the mechanical behavior of a liver whereas the second simulates the electrical behavior of a heart. These two systems rely on two different degrees of freedom, i.e. different physical phenomenon. They must therefore be described in two distinct nodes. This feature shows the ability of SOFA to easily develop advanced and coupled models.

To build a simulation in SOFA, the scene graph can be written both using:

*   XML files. Read the [associated page](https://www.sofa-framework.org/support/doc/using-sofa/write-a-scene-in-xml/) about how to write a scene in XML.
*   Python scripts. Read the [associated page](https://www.sofa-framework.org/support/doc/using-sofa/features/python-scripting/) about how to write in Python.


Data
----
This "Liver" node of Fig. 1 includes components (solvers, forcefield, mass) used to build the mechanical simulation of the liver. Each of these components contains attributes. For instance, a component of mass features an attribute for mass density; an iterative linear solver needs an attribute defining a maximum of iterations. These attributes are also called **Data**. These Data are containers providing a reflective API used for serialization in XML files and automatic creation of input/output widgets in the user interface.

Two Data instances can be connected one with another to keep their value synchronized. This is only possible if they both have the same type (`float`, `vector<double>`). A mechanism of lazy evaluation is used to recursively flag Data that are not up-to-date. Then, the Data is recomputed (only if necessary). The network of interconnected Data objects defines a data dependency graph. In an XML file, one Data is connected to another when "@" is used:
```xml
<Component dataname="@path_to/component.data" />
```




Animation loop
--------------

All the scenes in SOFA must include an _AnimationLoop_. This class rules all the steps of the simulation and the system resolution, which succeed each other in a specific order. At each time step, the animation loop triggers each event (solving the matrix system, managing the constraints, detecting the collision, etc.) through a _Visitor_ mechanism (see below). In a scene, if no animation loop is defined, a "DefaultAnimationLoop" is automatically created. Otherwise, in an XLM format, it can be written:

In an XML format, this would be written as follows:
```xml
<Node name="root" dt="0.01" gravity="0 -9.81 0">
    <DefaultAnimationLoop />
</Node>
```

Several _AnimationLoops_ are already available in SOFA:

* _DefaultAnimationLoop_: default one, created if no animation loop in the scene
* _FreeAnimationLoop_: for advanced constraints and collisions
* _MultiStepAnimationLoop_: uncouples the simulation and the visualization (N steps of simulation for one step of visualization)
* _MultiTagAnimationLoop_: animate the graph one tag after another, given a list of tags


Visitors
--------

During the different steps of the simulation (initialization, system assembly, solving, visualization), information needs to be recovered from all the graph nodes. An implicit mechanism based on _Visitor_ enables this. You can find the abstract _Visitor_ class in the SofaSimulation package.

For each of these steps, the operation implemented with the visitor can be described as:

*   a graph traversal,
*   abstract methods depending on the triggered action (ex: clearing an global vector, or accumulating forces),
*   and vector identificators.

_Visitors_ traverse the scene top-down and bottom-up, and call the corresponding virtual functions at each graph node traversal. _Visitors_ are therefore used to trigger actions by calling the associated virtual functions (e.g. animating the simulation, accumulating forces). Algorithmic operations on the simulated objects are implemented by deriving the _Visitor_ class and overloading its virtual functions _topDown( )_ and _bottomUp( )_. This approach hides the scene structure (parent, children) from the components, for more implementation flexibility and a better control of the execution model. Moreover, various parallelism strategies can be applied independently of the mechanical computations performed at each node. The data structure is actually extended from strict hierarchies to directed acyclic graphs to handle more general kinematic dependencies. The top-down node traversals are pruned unless all the parents of the current node have been traversed already, so that nodes with multiple parents are traversed only once all their parents have been traversed. The bottom-up traversals are made in the reverse order.


Example: _accumulating the forces_. Accumulating forces is used to compute all the forces (internal or external) applied on our object. The solver then triggers the associate _Visitor_ and the action is propagated through the graph and calls the appropriate (bottom-up) methods at each force and mapping node. All components able to compute forces will accumulate their contributions. This information is finally gathered in the MechanicalObject and the solver will use this "force" vector to solve the mathematical system.

<div style="text-align:center;width:50%;margin: 0 25% 0;">

<img src="https://www.sofa-framework.org/wp-content/uploads/2016/05/Images-tuto.0010.jpg" style="width: 90%;"/>
Fig. 4 - Traversing _Visitors_ triggered for the _accumulateForce()_ action

</div>



Sequence diagram
----------------

Here is the usual sequence diagram of a SOFA simulation.


<div style="text-align:center;width:90%;margin: 0 5% 0;">

<img src="https://www.sofa-framework.org/wp-content/uploads/2016/08/diagram-sequence.png" style="width: 100%;"/>
Fig. 5 - Sequence diagram of a SOFA simulation
</div>

More about the _Visitors_ can be found [here](https://www.sofa-framework.org/community/doc/using-sofa/basic-components/visitors-and-solvers/).
