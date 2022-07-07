# SOFA-NG transition

## Project timeline

- GIthub project: https://github.com/sofa-framework/sofa/projects/9
- The different PRs, the description of the task and the drafts for SOFA-NG can be found here: https://github.com/sofa-framework/sofa/issues/1527


## Components
SOFA-NG introduced new libraries, or more exactly replaces the previous "modules" (e.g. SofaBaseTopology, etc.), as it was deemed difficult for the new users to find a specific component in the code. Moreover, the dependencies between the module were difficult to manage and the sorting was seemingly weird because of unholy hard-dependency in the code.

Since v22.06, a new architecture has been proposed and the SOFA team worked on a compatibility layer aiming at making the transition as smooth as possible for the community. Nevertheless, the compatibility layer might not cover some specifal cases. Do not hesitate to [report your technical issues](https://github.com/sofa-framework/sofa/discussions/new).

We need to handle either the developers of new plugins designing components and simulations; and the "normal" users which only executes simulations.
There are 3 layers to manage the compatibility: CMake configure process, at compile-time and at run-time:

 - at run-time, highlighting that a component should be loaded from the new library and not the deprecated one (user and dev)
 - in the CMake process, informing that the deprecated package should be replaced by which new library (dev only)
 - at the compilation time, to warn the user that the path for a chosen header changed in the new architecture (dev only)


### CMake
CMake packages for the deprecated modules throw warnings message at the configuration time and redirect to the new ones.
Effectively, it does :

``` cmake
find_package(new_package1)
find_package(new_package2)
...
target_link_library(oldmodule new_package1 new_package2)
```

and it creates an empty shell of a project, dedicated to route the new includes and the new library (.lib, .so) to the new packages.


### Compilation
One big package called Sofa.Component.Compat contains all the previous headers (with the previous paths), which merely redirects to the new paths and, if the case occurs, creates an alias of the component into the previous namespace.

This is the most problematic case and where the compatibility is most likely to fail:

 - C++ does not allow specialization of templated classes with aliases
 - forward declaration in dev files will fail as well, as it is not possible to declare twice a class (first created by the alias and then by the forward declaration, or vice-versa)
 - if one did not use explicitly the include of a header but was relying on the other file (e.g using `PointSetTopologyContainer` but was including `TriangleSetTopologyContainer`, which is using `PointSetTopologyContainer`), the compilation will fail.

Obviously, if the move did not imply a change of namespace, the transition is much smoother (for example, with Controller from Sofa.Component.Controller)

### Run-time
When a user loads a deprecated module in its scene (either by using `RequiredPlugin` or by manually loading it), the loading process will display a warning, advising to load the new modules, and then will load automatically the new one. This will allow the scene to still load, even if only the deprecated module was set.

### Mapping deprecated modules ↔ new libraries

#### SofaBase

+ SofaBaseTopology → Sofa.Component.Topology
+ SofaBaseLinearSolver → Sofa.Component.LinearSolver.Iterative
+ SofaBaseUtils → Sofa.Component.SceneUtility
+ SofaBaseCollision has been split into several modules →
    + Sofa.Component.Collision.Model
    + Sofa.Component.Collision.Detection.Algorithm
    + Sofa.Component.Collision.Detection.Intersection
    + Sofa.Component.Collision.Response.Mapper
    + Sofa.Component.Collision.Response.Contact
+ SofaBaseMechanics has been split into several modules →
    + Sofa.Component.Mass
    + Sofa.Component.Mapping.Linear
    + Sofa.Component.StateContainer
+ SofaBaseTopology has been split into several modules →
    + Sofa.Component.Topology.Container.Grid
    + Sofa.Component.Topology.Container.Constant
    + Sofa.Component.Topology.Container.Dynamic
+ SofaBaseVisual has been split into several modules →
    + Sofa.Component.Visual
    + Sofa.Component.Setting

#### SofaCommon

+ SofaDeformable → Sofa.Component.SolidMechanics.Spring
+ SofaEngine → Sofa.Component.Engine.Select
+ SofaExplicitOdeSolver → Sofa.Component.ODESolver.Forward
+ SofaImplicitOdeSolver → Sofa.Component.ODESolver.Backward
+ SofaLoader → Sofa.Component.IO.Mesh
+ SofaObjectInteraction → Sofa.Component.Collision.Response.Contact
+ SofaMeshCollision has been split into several modules →
    + Sofa.Component.Collision.Geometry
    + Sofa.Component.Collision.Detection.Intersection
    + Sofa.Component.Collision.Response.Mapper
    + Sofa.Component.Collision.Response.Contact
+ SofaRigid has been split into several modules →
    + Sofa.Component.Mapping
    + Sofa.Component.SolidMechanics.Spring
+ SofaSimpleFem has been split into several modules →
    + Sofa.Component.Diffusion
    + Sofa.Component.SolidMechanics.FEM.Elastic

#### SofaGeneral

+ SofaGeneralExplicitOdeSolver → Sofa.Component.ODESolver.Forward
+ SofaGeneralImplicitOdeSolver → Sofa.Component.ODESolver.Backward
+ SofaGeneralRigid → Sofa.Component.Mapping
+ SofaGeneralSimpleFem → Sofa.Component.SolidMechanics.FEM.Elastic
+ SofaGeneralVisual → Sofa.Component.Visual
+ SofaBoundaryCondition has been split into several modules →
    + Sofa.Component.Constraint.Projective
    + Sofa.Component.MechanicalLoad
+ SofaConstraint has been split into several modules →
    + Sofa.Component.Mapping.MappedMatrix
    + Sofa.Component.Constraint.Lagrangian.Model
    + Sofa.Component.Constraint.Lagrangian.Correction
    + Sofa.Component.Constraint.Lagrangian.Solver
    + Sofa.Component.AnimationLoop
    + Sofa.Component.Collision.Detection.Intersection
    + Sofa.Component.Collision.Response.Contact
    + Sofa.GUI.Component
+ SofaGeneralAnimationLoop has been split into several modules →
    + Sofa.Component.Mapping.MappedMatrix
    + Sofa.Component.AnimationLoop
+ SofaGeneralDeformable has been split into several modules →
    + Sofa.Component.SolidMechanics.Spring
    + Sofa.Component.SolidMechanics.TensorMass
+ SofaGeneralEngine has been split into several modules →
    + Sofa.Component.Engine.Analyze
    + Sofa.Component.Engine.Generate
    + Sofa.Component.Engine.Select
    + Sofa.Component.Engine.Transform
+ SofaGeneralLinearSolver has been split into several modules → 
    + Sofa.Component.LinearSolver.Iterative
    + Sofa.Component.LinearSolver.Direct
+ SofaGeneralLoader has been split into several modules →
    + Sofa.Component.IO.Mesh
    + Sofa.Component.Playback
+ SofaGeneralMeshCollision has been split into several modules →
    + Sofa.Component.Collision.Geometry
    + Sofa.Component.Collision.Detection.Algorithm 
    + Sofa.Component.Collision.Detection.Intersection
+ SofaGeneralObjectInteraction has been split into several modules →
    + Sofa.Component.SolidMechanics.Spring
    + Sofa.Component.Constraint.Projective
    + Sofa.Component.MechanicalLoad
+ SofaGeneralTopology has been split into several modules →
    + Sofa.Component.Topology.Container.Grid
    + Sofa.Component.Topology.Container.Constant
+ SofaGraphComponent has been split into several modules →
    + Sofa.Component.SceneUtility
    + Sofa.Component.Setting
    + Sofa.GUI.Component
    + the plugin SceneChecking
+ SofaUserInteraction has been split into several modules → 
    + Sofa.Component.Collision.Geometry
    + Sofa.Component.Collision.Detection.Algorithm
    + Sofa.Component.Collision.Detection.Intersection
    + Sofa.Component.Collision.Response.Contact
    + Sofa.Component.Controller
    + Sofa.GUI.Component (from Sofa.GUI)
+ SofaTopologyMapping has been split into several modules →
    + Sofa.Component.Topology.Mapping
    + Sofa.Component.Mapping

#### SofaMisc

+ SofaMiscExtra → Sofa.Component.Engine.Generate
+ SofaMiscTopology → Sofa.Component.Topology.Utility
+ SofaMiscCollision has been split into several modules → 
    + Sofa.Component.Collision.Geometry
    + Sofa.Component.Collision.Detection.Intersection
    + Sofa.Component.Collision.Response.Contact
    + the plugin CollisionOBBCapsule
+ SofaMiscEngine has been split into several modules →
    + Sofa.Component.Engine.Analyze
    + Sofa.Component.Engine.Transform
+ SofaMiscFem has been split into several modules →
    + Sofa.Component.SolidMechanics.FEM.Elastic
    + Sofa.Component.SolidMechanics.FEM.HyperElastic
    + Sofa.Component.SolidMechanics.TensorMass
+ SofaMiscForceField has been split into several modules →
    + Sofa.Component.Mass
    + Sofa.Component.SolidMechanics.Spring
+ SofaMiscSolver has been split into several modules → 
    + Sofa.Component.ODESolver.Backward
    + Sofa.Component.ODESolver.Forward

#### Plugins

+ SofaDenseSolver → Sofa.Component.LinearSolver.Direct
+ SofaExporter → Sofa.Component.IO.Mesh and Sofa.Component.Playback
+ SofaHaptics → Sofa.Component.Haptics
+ SofaValidation → Sofa.Component.Playback
+ SofaNonUniformFem has been split into several modules →
    + Sofa.Component.Topology.Container.Grid
    + Sofa.Component.Topology.Container.Dynamic
    + Sofa.Component.SolidMechanics.FEM.NonUniform
+ SofaOpenglVisual has been split into several modules → 
    + Sofa.GL.Component.Rendering2D
    + Sofa.GL.Component.Rendering3D
    + Sofa.GL.Component.Shader (from Sofa.GL)
+ SofaPreconditioner has been split into several modules →
    + Sofa.Component.LinearSolver.Iterative 
    + Sofa.Component.LinearSolver.Preconditioner
+ SofaSparseSolver has been split into several modules →
    + Sofa.Component.LinearSolver.Iterative
    + Sofa.Component.LinearSolver.Direct

#### Collection

+ SofaComponentAll → Sofa.Component


## Framework
SOFA-NG induced also a cleaning in the framework of SOFA. All parts of the framework have been renamed to reflect the same pattern started with Sofa.Component. For example, SofaSimulationGraph becomes Sofa.Simulation.Graph.

The list of the differents packages which are considered as part of the framework is:

+ SofaHelper → Sofa.Helper
+ SofaDefaulttype → Sofa.Defaulttype
+ SofaCore → Sofa.Core
+ SofaSimulationCore → Sofa.Simulation.Core
+ SofaSimulationCommon → Sofa.Simulation.Common
+ SofaSimulationGraph → Sofa.Simulation.Graph
+ Sofa.Config (new), which gathers all CMake files used in SOFA projects (macros, config, flags, etc)
+ Sofa.Type (new)
+ Sofa.LinearAlgebra (new)
+ Sofa.Geometry (new)
+ Sofa.Topology (new)


## Report technical issues
In case you face any technical difficulty in the transition, please report it using our [GitHub Discussion forum](https://github.com/sofa-framework/sofa/discussions/new).
