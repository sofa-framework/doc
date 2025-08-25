# ParallelHexahedronFEMForceField

ParallelHexahedronFEMForceField is the multi-threaded equivalent of [HexahedronFEMForceField](../../../../components/solidmechanics/fem/elastic/hexahedronfemforcefield).

This implementation is the most efficient when:

1) the number of hexahedron is large (> 1000)
2) the global system matrix is not assembled. It is usually the case with a [CGLinearSolver](../../../../components/linearsolver/iterative/cglinearsolver/) templated with GraphScattered types.
3) the method is 'large'. If the method is 'polar' or 'small', `addForce` is executed sequentially, but `addDForce` in parallel.

The following methods are executed in parallel:

- `addForce` for method 'large'.
- `addDForce`

The method `addKToMatrix` is not executed in parallel.
This method is called with an assembled system, usually with a direct solver or a [CGLinearSolver](../../../../components/linearsolver/iterative/cglinearsolver/) templated with types different from GraphScattered.
In this case, the most time-consuming step is to invert the matrix. This is where efforts should be put to accelerate the simulation.
