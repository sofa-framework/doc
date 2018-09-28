Animation loop
==============

All the scenes in SOFA must include an _AnimationLoop_. This class rules all the steps of the simulation and the system resolution, which succeed each other in a specific order. At each time step, the animation loop triggers each event (solving the matrix system, managing the constraints, detecting the collision, etc.) through a _Visitor_ mechanism (see below). In a scene, if no animation loop is defined, a "DefaultAnimationLoop" is automatically created. Otherwise, in an XML format, it can be written:

In an XML format, this would be written as follows:
```xml
<Node name="root" dt="0.01" gravity="0 -9.81 0">
    <DefaultAnimationLoop />
</Node>
```

Several _AnimationLoops_ are already available in SOFA:

* **_DefaultAnimationLoop_**:
  this is the default animation loop as the name indicates! This animation loop is included by default at the root node of the graph, if no animation loop is specified in the scene. With a _DefaultAnimationLoop_, the loop of one simulation step follows:

    1. build and solve all linear systems in the scene : collision and time integration to compute the new values of the dofs
    2. update the context (dt++)
    3. update the mappings
    4. update the bounding box (volume covering all objects of the scene)

* **_MultiTagAnimationLoop_**:
  this animation loops works by labelling components using different tags. With a _MultiTagAnimationLoop_, the loop of one simulation step is the same as the _DefaultAnimationLoop_, except that one tag is solved after another, given a list of tags:

    1. build and solve all linear systems in the scene
      1. for all components and nodes using the first tag
      2. then the second tag
      ... and so on
    2. update the context
    3. update the mappings
    4. update the bounding box

* **_MultiStepAnimationLoop_**:
  given one time step, this animation loop allows for running several collision (_C_) and several integration time in one step (_I_), where _C_ and _I_ can be different. If the time step is _dt=0.01_, the number of collision step _C=2_ and the number of integration step is _I=4_, the loop of one simulation step follows:
  
    1. compute _C=4_ times the collision pipeline (4 collision steps)
      * for each collision step, solve _I=4_ times the linear system due to integration. The integration time step is therefore _dt' = dt / (C.I) = 0.00125_ (8 integration steps).
    2. update the context
    3. update the mappings
    4. update the bounding box : this means that the visualization is done once at each time step _dt=0.01_

* **_FreeAnimationLoop_**:
  this animation loop is used for simulation involving constraints and collisions. With a _FreeAnimationLoop_, the loop of one simulation step follows:
  
    1. build and solve all linear systems in the scene without constraints and save the "free" values of the dofs
    2. collisions are computed
    3. constraints are finally used to correct the "free" dofs in order to take into account the collisions & constraints
    4. update the mappings
    5. update the bounding box


Visitors
========

During the different steps of the simulation (initialization, system assembly, solving, visualization), information needs to be recovered from all the graph nodes. An implicit mechanism based on _Visitor_ enables this. You can find the abstract _Visitor_ class in the SofaSimulation package.

For each of these steps, the operation implemented with the visitor can be described as:

*   a graph traversal,
*   abstract methods depending on the triggered action (ex: clearing a global vector, or accumulating forces),
*   and vector identificators.

_Visitors_ traverse the scene top-down and bottom-up and call the corresponding virtual functions at each graph node traversal. _Visitors_ are therefore used to trigger actions by calling the associated virtual functions (e.g. animating the simulation, accumulating forces). Algorithmic operations on the simulated objects are implemented by deriving the _Visitor_ class and overloading its virtual functions _topDown( )_ and _bottomUp( )_. This approach hides the scene structure (parent, children) from the components, for more implementation flexibility and a better control of the execution model. Moreover, various parallelism strategies can be applied independently of the mechanical computations performed at each node. The data structure is actually extended from strict hierarchies to directed acyclic graphs to handle more general kinematic dependencies. The top-down node traversals are pruned unless all the parents of the current node have been traversed already, so that nodes with multiple parents are traversed only once all their parents have been traversed. The bottom-up traversals are made in the reverse order.


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
