Animation loop
==============

All the scenes in SOFA must include an _AnimationLoop_. This components orders all steps of the simulation and the system resolution. At each time step, the animation loop triggers each event (solving the matrix system, managing the constraints, detecting the collision, etc.) through a [_Visitor_](https://www.sofa-framework.org/community/doc/main-principles/visitors/) mechanism (see below). In a scene, if no animation loop is defined, a "DefaultAnimationLoop" is automatically created.

Several _AnimationLoops_ are already available in SOFA:

* [_DefaultAnimationLoop_](https://www.sofa-framework.org/community/doc/using-sofa/components/animationloop/defaultanimationloop/):
  this is the default animation loop as the name indicates! This animation loop is included by default at the root node of the graph, if no animation loop is specified in the scene. With a _DefaultAnimationLoop_, the loop of one simulation step follows:

    1. build and solve all linear systems in the scene : collision and time integration to compute the new values of the dofs
    2. update the context (dt++)
    3. update the mappings
    4. update the bounding box (volume covering all objects of the scene)

* _MultiTagAnimationLoop_:
  this animation loops works by labelling components using different tags. With a _MultiTagAnimationLoop_, the loop of one simulation step is the same as the _DefaultAnimationLoop_, except that one tag is solved after another, given a list of tags:

    1. build and solve all linear systems in the scene
      1. for all components and nodes using the first tag
      2. then the second tag
      ... and so on
    2. update the context
    3. update the mappings
    4. update the bounding box

* [_MultiStepAnimationLoop_](https://www.sofa-framework.org/community/doc/using-sofa/components/animationloop/multistepanimationloop/):
  given one time step, this animation loop allows for running several collision (_C_) and several integration time in one step (_I_), where _C_ and _I_ can be different. If the time step is _dt=0.01_, the number of collision step _C=2_ and the number of integration step is _I=4_, the loop of one simulation step follows:
  
    1. compute _C=4_ times the collision pipeline (4 collision steps)
      * for each collision step, solve _I=4_ times the linear system due to integration. The integration time step is therefore _dt' = dt / (C.I) = 0.00125_ (8 integration steps).
    2. update the context
    3. update the mappings
    4. update the bounding box : this means that the visualization is done once at each time step _dt=0.01_

* [_FreeAnimationLoop_](https://www.sofa-framework.org/community/doc/using-sofa/components/animationloop/freemotionanimationloop/):
  this animation loop is used for simulation involving constraints and collisions. With a _FreeAnimationLoop_, the loop of one simulation step follows:
  
    1. build and solve all linear systems in the scene without constraints and save the "free" values of the dofs
    2. collisions are computed
    3. constraints are finally used to correct the "free" dofs in order to take into account the collisions & constraints
    4. update the mappings
    5. update the bounding box

