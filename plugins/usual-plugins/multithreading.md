---
title: MultiThreading
---

# MultiThreading

SOFA has some multithreading capabilities in its core, but more features are available in the MultiThreading plugin.

## Plugin Compilation

1. Enable `PLUGIN_MULTITHREADING` in your CMake configuration. It is disabled by default.
2. Configure, generate and build.

## Parallel Collision Detection

Most SOFA scenes use a component defining the [collision pipeline](../../../components/collision/detection/algorithm/collisionpipeline/).
This pipeline requires two components for the [broad phase](../../../components/components/collision/detection/algorithm/broadphase/) and the [narrow phase](../../../components/components/collision/detection/algorithm/narrowphase) of the collision detection.
A usual choice is [BruteForceBroadPhase](../../../components/collision/detection/algorithm/bruteforcebroadphase/) for the broad phase, and [BVHNarrowPhase](../../../components/collision/detection/algorithm/bvhnarrowphase/) for the narrow phase.
Both of these components can be replaced with a parallel version from the MultiThreading plugin.

## Independent SOFA Scenes

The AnimationLoopParallelScheduler component was implemented to run the physics simulation of independent scenes in parallel.
The component looks for [BaseAnimationLoop components](../../../simulation-principles/animation-loop/) in all its child nodes and executes the `step()` function of each AnimationLoop in parallel.

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
