# MultiThreading

SOFA has some multithreading capabilities in its core, but more features are available in the MultiThreading plugin.

## Plugin Compilation

1. Enable `PLUGIN_MULTITHREADING` in your CMake configuration. It is disabled by default.
2. Configure, Generate and build.

## Parallel Collision Detection

Most SOFA scenes use a component defining the [collision pipeline](https://www.sofa-framework.org/community/doc/components/collisions/pipelines/collisionpipeline/).
This pipeline requires two components for the [broad phase collision detection](https://www.sofa-framework.org/community/doc/components/collisions/broadphases/broadphase/), and the [narrow phase collision detection](https://www.sofa-framework.org/community/doc/components/collisions/narrowphases/narrowphase/).
A usual choice for the broad phase is [BruteForceBroadPhase](https://www.sofa-framework.org/community/doc/components/collisions/broadphases/bruteforcebroadphase/), and [BVHNarrowPhase](https://www.sofa-framework.org/community/doc/components/collisions/narrowphases/bvhnarrowphase/) for the narrow phase.

In the MultiThreading plugin, two components can replace [BruteForceBroadPhase](https://www.sofa-framework.org/community/doc/components/collisions/broadphases/bruteforcebroadphase/) and [BVHNarrowPhase](https://www.sofa-framework.org/community/doc/components/collisions/narrowphases/bvhnarrowphase/).

### ParallelBruteForceBroadPhase

This component is a parallel implementation of [BruteForceBroadPhase](https://www.sofa-framework.org/community/doc/components/collisions/broadphases/bruteforcebroadphase/) using a global thread pool.
It means the result of a simulation with [BruteForceBroadPhase](https://www.sofa-framework.org/community/doc/components/collisions/broadphases/bruteforcebroadphase/) or with ParallelBruteForceBroadPhase is expected to be equal.
ParallelBruteForceBroadPhase is the most efficient compared to [BruteForceBroadPhase](https://www.sofa-framework.org/community/doc/components/collisions/broadphases/bruteforcebroadphase/) when there is a lot of objects in the scene.

#### Examples

Examples of ParallelBruteForceBroadPhase can be found in:

* [ParallelBruteForceBroadPhase.scn](https://github.com/sofa-framework/sofa/blob/master/applications/plugins/MultiThreading/examples/ParallelBruteForceBroadPhase.scn)
* [ParallelCollisionDetection.scn](https://github.com/sofa-framework/sofa/blob/master/applications/plugins/MultiThreading/examples/ParallelCollisionDetection.scn)
* [5DeformableCubesConstraints.scn](https://github.com/sofa-framework/sofa/blob/master/applications/plugins/MultiThreading/examples/5DeformableCubesConstraints.scn)

### ParallelBVHNarrowPhase

This component is a parallel implementation of [BVHNarrowPhase](https://www.sofa-framework.org/community/doc/components/collisions/narrowphases/bvhnarrowphase/) using a global thread pool.
It means the result of a simulation with [BVHNarrowPhase](https://www.sofa-framework.org/community/doc/components/collisions/narrowphases/bvhnarrowphase/) or with ParallelBVHNarrowPhase is expected to be equal.

#### Examples

Examples of ParallelBruteForceBroadPhase can be found in:

* [ParallelBruteForceBroadPhase.scn](https://github.com/sofa-framework/sofa/blob/master/applications/plugins/MultiThreading/examples/ParallelBruteForceBroadPhase.scn)
* [ParallelCollisionDetection.scn](https://github.com/sofa-framework/sofa/blob/master/applications/plugins/MultiThreading/examples/ParallelCollisionDetection.scn)
* [5DeformableCubesConstraints.scn](https://github.com/sofa-framework/sofa/blob/master/applications/plugins/MultiThreading/examples/5DeformableCubesConstraints.scn)

# Physics

## BeamLinearMapping_mt

This component inherits all the functionality from the BeamLinearMapping component and overrides three virtual functions that contain a `for` loop: `apply()`, `applyJ()` and `applyJT()`.
It adds only one data attribute, the granularity. This attribute sets the number of iterations of the `for` loop, corresponding to the number of points along the beam elements that must be assigned and executed for each task.
If this number is lower than the number of iterations the loop won't be parallelized, and the corresponding BeamLinearMapping function is called.
If this number is greater than the number of iterations of the loop the tasks are created, and each task executes the granularity value of iterations of the loop.

### Examples

Examples of BeamLinearMapping_mt can be found in:

* [BeamLinearMapping_mt.scn](https://github.com/sofa-framework/sofa/blob/master/applications/plugins/MultiThreading/examples/BeamLinearMapping_mt.scn)



## Independent SOFA Scenes

The AnimationLoopParallelScheduler component was implemented to run the physics simulation of independent scenes in parallel.
The component looks for [BaseAnimationLoop components](https://www.sofa-framework.org/community/doc/simulation-principles/animation-loop/) in all its child nodes and executes the `step()` function of each AnimationLoop in parallel.

The DataExchange component can manage the sharing of data between all the concurrent scenes without being bound by synchronization locks.
To avoid the use of synchronization locks, each component in different scenes must have its own copy of the same data to share, and the data synchronization is executed serially.
After the data synchronization the VisualLoop is executed in serial.
Each child node of the node where the AnimationLoopParallelScheduler is placed must be seen as an independent scene and there should be no physics interaction or collision detection between these scenes.
When all the `step()` functions return, the visual loop (graphics rendering) is executed serially throughout the scene.

The DataExchange component must be placed in the same node where the AnimationLoopParallelScheduler is, and the path links to the source and destination data to copy must be defined.
The data template of the source and destination path links must be the same.
This data synchronization is executed serially before the VisualLoop is executed.
A common use of the AnimationLoopParallelScheduler component is to place it in the root node of the scene hierarchy and add a AnimationLoop to all the child nodes you want to be executed independently.

### Tips and Limitations

To get the best performance with the AnimationLoopParallelScheduler component, the execution time of each animation loop should be manually balanced to get almost the same time length.
If in the scene an animation loop is computationally more expensive, the MultiStepAnimationLoop component can be useful not to limit the speed of execution of a potentially faster AnimationLoop step function.
This will improve the synchronization between threads, minimizing the waiting time for all animation loops completion.
The scene should be split into as many independent scenes as possible.
An independent scene is considered as a scene where the physics simulated objects are never supposed to collide with the objects of another scene during the whole simulation time length.

The main limitation using the AnimationLoopParallelScheduler is that interaction with the mouse with the objects in the scene crashes the simulation.

### Examples

Examples of AnimationLoopParallelScheduler and DataExchange can be found in:

* [TriangularForceFieldComparison.scn](https://github.com/sofa-framework/sofa/blob/master/applications/plugins/MultiThreading/examples/TriangularForceFieldComparison.scn)
* [livers.scn](https://github.com/sofa-framework/sofa/blob/master/applications/plugins/MultiThreading/examples/livers.scn)
