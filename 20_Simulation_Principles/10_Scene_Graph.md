Scene graph
===========

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

*   XML files. Read the [associated page](../../using-sofa/write-a-scene-in-xml/) about how to write a scene in XML.
*   Python scripts. Read the [associated page](../../using-sofa/features/python-scripting/) about how to write in Python.


Data
====

This "Liver" node of Fig. 1 includes components (solvers, forcefield, mass) used to build the mechanical simulation of the liver. Each of these components contains attributes. For instance, a component of mass features an attribute for mass density; an iterative linear solver needs an attribute defining a maximum of iterations. These attributes are also called **Data**. These Data are containers providing a reflective API used for serialization in XML files and automatic creation of input/output widgets in the user interface.

Two Data instances can be connected one with another to keep their value synchronized. This is only possible if they both have the same type (`float`, `vector<double>`). A mechanism of lazy evaluation is used to recursively flag Data that are not up-to-date. Then, the Data is recomputed (only if necessary). The network of interconnected Data objects defines a data dependency graph. In an XML file, one Data is connected to another when "@" is used:
```xml
<Component dataname="@path_to/component.data" />
```

Read more about data on the [Components and Data](../../programming-with-sofa/start-coding/components-api/components-and-datas/) documentation page.


Tags
----
Any component can be set with one or several "Tags". The "tags" data field is available for any SOFA component. 
A tag is useful to find a specific component in the scene, to distinguish several instances of a same class in the scene graph or to process these instances differently one from another (see next article about the _MultiTagAnimationLoop_).
