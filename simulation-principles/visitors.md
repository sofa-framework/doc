---
title: Visitors
---

Visitors
========

During the different steps of the simulation (initialization, system assembly, solving, visualization), information needs to be recovered from all graph nodes. SOFA relies on an implicit mechanism: the _Visitors_. You can find the abstract _Visitor_ class in the SofaSimulation package.

_Visitors_ traverse the scene top-down and bottom-up and call the corresponding virtual functions at each graph node traversal. _Visitors_ are therefore used to trigger actions by calling the associated virtual functions (e.g. animating the simulation, accumulating forces). Algorithmic operations on the simulated objects are implemented by deriving the _Visitor_ class and overloading its virtual functions _processNodeTopDown( )_ and _processNodeBottomUp( )_.

This approach hides the scene structure (parent, children) from the components, for more implementation flexibility and a better control of the execution model. Moreover, various parallelism strategies can be applied independently of the mechanical computations performed at each node. The data structure is actually extended from strict hierarchies to directed acyclic graphs to handle more general kinematic dependencies. The top-down node traversals are pruned unless all the parents of the current node have been traversed already, so that nodes with multiple parents are traversed only once all their parents have been traversed. The bottom-up traversals are made in the reverse order.


Examples:

  - at the level of an [AnimationLoop](https://www.sofa-framework.org/community/doc/main-principles/animation-loop/), visitors are used for instance to trigger the simulation step (_AnimateVisitor_), update the context (_UpdateSimulationContextVisitor_) and update the mappings (_UpdateMappingVisitor_).

  - at the level of the [ODESolver](https://www.sofa-framework.org/community/doc/simulation-principles/system-resolution/integration-scheme/), visitors allow to build the linear matrix system by abstract functions. For instance, the computation of the right hand side vector *b* is triggered by the _MechanicalComputeForceVisitor_, accumulating forces is used to compute all the forces (internal or external) applied on our object. The solver then triggers the associate _Visitor_ and the action is propagated through the graph and calls the appropriate (bottom-up) methods at each force and mapping node. All components able to compute forces will accumulate their contributions. This information is finally gathered in the MechanicalObject and the solver will use this "force" vector to solve the mathematical system.

<div style="text-align:center;width:50%;margin: 0 25% 0;">
<img src="https://www.sofa-framework.org/wp-content/uploads/2016/05/Images-tuto.0010.jpg" style="width: 90%;"/>
</div>



Sequence diagram
----------------

Here is the usual sequence diagram of a SOFA simulation.

<div style="text-align:center;width:90%;margin: 0 5% 0;">
<img src="https://www.sofa-framework.org/wp-content/uploads/2016/08/diagram-sequence-detailed.png" style="width: 100%;"/>
</div>