Animation loop
==============

All the scenes in SOFA must include an _AnimationLoop_. This component orders all steps of the simulation and the system resolution. At each time step, the animation loop triggers each event (solving the matrix system, managing the constraints, detecting the collision, etc.) through a [_Visitor_](./../visitors/) mechanism (see below). In a scene, if no animation loop is defined, a "DefaultAnimationLoop" is automatically created.

Several _AnimationLoops_ are already available in SOFA:

* [_DefaultAnimationLoop_](../../using-sofa/components/animationloop/defaultanimationloop/):
  this is the default animation loop as the name indicates! This animation loop is included by default at the root node of the graph, if no animation loop is specified in the scene. With a _DefaultAnimationLoop_, the loop of one simulation step follows:

    1. collision detection is triggered through the [collision pipeline](../../using-sofa/components/collision/detection/algorithm/collisionpipeline) (if any)
    2. solve the physics in the scene by triggering the integration scheme, taking the constraint, collision into account
    3. update the system (new values of the dofs), the context (dt++), the mappings and the bounding box (volume covering all objects of the scene)

* _MultiTagAnimationLoop_:
  this animation loop works by labelling components using different tags. With a _MultiTagAnimationLoop_, the loop of one simulation step is the same as the _DefaultAnimationLoop_, except that one tag is solved after another, given a list of tags:

    1. For each tag defined:
      1. collision detection is triggered through the [collision pipeline](../../using-sofa/components/collision/detection/algorithm/collisionpipeline) (if any)
      2. solve the physics in the scene by triggering the integration scheme, taking the constraint, collision into account
    2. update the system (new values of the dofs), the context (dt++), the mappings and the bounding box (volume covering all objects of the scene)

* [_MultiStepAnimationLoop_](../../using-sofa/components/animationloop/multistepanimationloop/):
  given one time step, this animation loop allows for running several collision (_C_ being the number of collision steps) and several time integrations in one step (_I_ being the number of integration time steps), where _C_ and _I_ can be different. If the global time step is noted _dt_, the time integration time is actually: _dt' = dt / (C.I)_. The loop in one animation step is:
  
    1. compute _C_ times the [collision pipeline](../../using-sofa/components/collision/detection/algorithm/collisionpipeline) within one time step _dt_
    2. For each collision step, solve _I_ times the linear system for time integration using the time step _dt'_
    3. update the context, the mappings, the bounding box (the visualization is done once at each time step _dt_)

* [_FreeMotionAnimationLoop_](../../using-sofa/components/animationloop/freemotionanimationloop/):
  this animation loop is used for simulation involving constraints and collisions. With a _FreeAnimationLoop_, the loop of one simulation step follows:
  
    1. build and solve all linear systems in the scene without constraints and save the "free" values of the dofs
    2. collision detection is computed thus generating constraints
    3. constraints are solved as one system to compute a correction term taking into account the collisions & constraints
    4. update the mappings, the bounding box

