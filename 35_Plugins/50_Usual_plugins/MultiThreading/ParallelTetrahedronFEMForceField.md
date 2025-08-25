# ParallelTetrahedronFEMForceField

ParallelTetrahedronFEMForceField is the multi-threaded equivalent of [TetrahedronFEMForceField](../../../../components/solidmechanics/fem/elastic/tetrahedronfemforcefield).

This implementation is the most efficient when the number of tetrahedron is large (> 1000).

The following methods are executed in parallel:
- `addDForce`
- `addKToMatrix`
