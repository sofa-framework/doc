# ParallelBruteForceBroadPhase

This component is a parallel implementation of [BruteForceBroadPhase](../../../../components/collision/detection/algorithm/bruteforcebroadphase/) using a global thread pool.
It means the result of a simulation with [BruteForceBroadPhase](../../../../components/collision/detection/algorithm/bruteforcebroadphase/) or with ParallelBruteForceBroadPhase is expected to be equal.
ParallelBruteForceBroadPhase is the most efficient compared to [BruteForceBroadPhase](../../../../components/collision/detection/algorithm/bruteforcebroadphase/) when there is a lot of objects in the scene.
