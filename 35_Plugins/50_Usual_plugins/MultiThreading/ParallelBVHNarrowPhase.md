# ParallelBVHNarrowPhase

This component is a parallel implementation of [BVHNarrowPhase](../../../../components/collision/detection/algorithm/bvhnarrowphase/) using a global thread pool.
It means the result of a simulation with [BVHNarrowPhase](../../../../components/collision/detection/algorithm/bvhnarrowphase/) or with ParallelBVHNarrowPhase is expected to be equal.
