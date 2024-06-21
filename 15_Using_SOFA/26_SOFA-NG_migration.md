---
title: SOFA-NG migration
---

# SOFA-NG transition

## Project timeline

- Github [project for SOFA NG](https://github.com/sofa-framework/sofa/projects/9)
- A [GitHub issue was referencing](https://github.com/sofa-framework/sofa/issues/1527) all different PRs, the description of the task and the drafts for SOFA-NG


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


<table>
<tbody>
  <tr>
    <td>SofaBaseTopology</td>
    <td>Sofa.Component.Topology</td>
  </tr>
  <tr>
    <td>SofaBaseLinearSolver</td>
    <td>Sofa.Component.LinearSolver.Iterative</td>
  </tr>
  <tr>
    <td>SofaBaseUtils</td>
    <td>Sofa.Component.SceneUtility</td>
  </tr>
  <tr>
    <td rowspan="5">SofaBaseCollision</td>
    <td>Sofa.Component.Collision.Model</td>
  </tr>
  <tr>
    <td>Sofa.Component.Collision.Detection.Algorithm</td>
  </tr>
  <tr>
    <td>Sofa.Component.Collision.Detection.Intersection</td>
  </tr>
  <tr>
    <td>Sofa.Component.Collision.Response.Mapper</td>
  </tr>
  <tr>
    <td>Sofa.Component.Collision.Response.Contact</td>
  </tr>
  <tr>
    <td rowspan="3">SofaBaseMechanics</td>
    <td>Sofa.Component.Mass</td>
  </tr>
  <tr>
    <td>Sofa.Component.Mapping.Linear</td>
  </tr>
  <tr>
    <td>Sofa.Component.StateContainer</td>
  </tr>
  <tr>
    <td rowspan="3">SofaBaseTopology</td>
    <td>Sofa.Component.Topology.Container.Grid</td>
  </tr>
  <tr>
    <td>Sofa.Component.Topology.Container.Constant</td>
  </tr>
  <tr>
    <td>Sofa.Component.Topology.Container.Dynamic</td>
  </tr>
  <tr>
    <td rowspan="2">SofaBaseVisual</td>
    <td>Sofa.Component.Visual</td>
  </tr>
  <tr>
    <td>Sofa.Component.Setting</td>
  </tr>
</tbody>
</table>

#### SofaCommon

<table>
<tbody>
  <tr>
    <td>SofaDeformable</td>
    <td>Sofa.Component.SolidMechanics.Spring</td>
  </tr>
  <tr>
    <td>SofaEngine</td>
    <td>Sofa.Component.Engine.Select</td>
  </tr>
  <tr>
    <td>SofaExplicitOdeSolver</td>
    <td>Sofa.Component.ODESolver.Forward</td>
  </tr>
  <tr>
    <td>SofaImplicitOdeSolver</td>
    <td>Sofa.Component.ODESolver.Backward</td>
  </tr>
  <tr>
    <td>SofaLoader</td>
    <td>Sofa.Component.IO.Mesh</td>
  </tr>
  <tr>
    <td>SofaObjectInteraction</td>
    <td>Sofa.Component.Collision.Response.Contact</td>
  </tr>
  <tr>
    <td rowspan="4">SofaMeshCollision</td>
    <td>Sofa.Component.Collision.Geometry</td>
  </tr>
  <tr>
    <td>Sofa.Component.Collision.Detection.Intersection</td>
  </tr>
  <tr>
    <td>Sofa.Component.Collision.Response.Mapper</td>
  </tr>
  <tr>
    <td>Sofa.Component.Collision.Response.Contact</td>
  </tr>
  <tr>
    <td rowspan="2">SofaRigid</td>
    <td>Sofa.Component.Mapping</td>
  </tr>
  <tr>
    <td>Sofa.Component.SolidMechanics.Spring</td>
  </tr>
  <tr>
    <td rowspan="2">SofaSimpleFem</td>
    <td>Sofa.Component.Diffusion</td>
  </tr>
  <tr>
    <td>Sofa.Component.SolidMechanics.FEM.Elastic</td>
  </tr>
</tbody>
</table>


#### SofaGeneral

<table>
<tbody>
  <tr>
    <td>SofaGeneralExplicitOdeSolver</td>
    <td>Sofa.Component.ODESolver.Forward</td>
  </tr>
  <tr>
    <td>SofaGeneralImplicitOdeSolver</td>
    <td>Sofa.Component.ODESolver.Backward</td>
  </tr>
  <tr>
    <td>SofaGeneralRigid</td>
    <td>Sofa.Component.Mapping</td>
  </tr>
  <tr>
    <td>SofaGeneralSimpleFem</td>
    <td>Sofa.Component.SolidMechanics.FEM.Elastic</td>
  </tr>
  <tr>
    <td>SofaGeneralVisual</td>
    <td>Sofa.Component.Visual</td>
  </tr>
  <tr>
    <td rowspan="2">SofaBoundaryCondition</td>
    <td>Sofa.Component.Constraint.Projective</td>
  </tr>
  <tr>
    <td>Sofa.Component.MechanicalLoad</td>
  </tr>
  <tr>
    <td rowspan="8">SofaConstraint</td>
    <td>Sofa.Component.Mapping.MappedMatrix</td>
  </tr>
  <tr>
    <td>Sofa.Component.Constraint.Lagrangian.Model</td>
  </tr>
  <tr>
    <td>Sofa.Component.Constraint.Lagrangian.Correction</td>
  </tr>
  <tr>
    <td>Sofa.Component.Constraint.Lagrangian.Solver</td>
  </tr>
  <tr>
    <td>Sofa.Component.AnimationLoop</td>
  </tr>
  <tr>
    <td>Sofa.Component.Collision.Detection.Intersection</td>
  </tr>
  <tr>
    <td>Sofa.Component.Collision.Response.Contact</td>
  </tr>
  <tr>
    <td>Sofa.GUI.Component</td>
  </tr>
  <tr>
    <td rowspan="2">SofaGeneralAnimationLoop</td>
    <td>Sofa.Component.Mapping.MappedMatrix</td>
  </tr>
  <tr>
    <td>Sofa.Component.AnimationLoop</td>
  </tr>
  <tr>
    <td rowspan="2">SofaGeneralDeformable</td>
    <td>Sofa.Component.SolidMechanics.Spring</td>
  </tr>
  <tr>
    <td>Sofa.Component.SolidMechanics.TensorMass</td>
  </tr>
  <tr>
    <td rowspan="4">SofaGeneralEngine</td>
    <td>Sofa.Component.Engine.Analyze</td>
  </tr>
  <tr>
    <td>Sofa.Component.Engine.Generate</td>
  </tr>
  <tr>
    <td>Sofa.Component.Engine.Select</td>
  </tr>
  <tr>
    <td>Sofa.Component.Engine.Transform</td>
  </tr>
  <tr>
    <td rowspan="2">SofaGeneralLinearSolver</td>
    <td>Sofa.Component.LinearSolver.Iterative</td>
  </tr>
  <tr>
    <td>Sofa.Component.LinearSolver.Direct</td>
  </tr>
  <tr>
    <td rowspan="2">SofaGeneralLoader</td>
    <td>Sofa.Component.IO.Mesh</td>
  </tr>
  <tr>
    <td>Sofa.Component.Playback</td>
  </tr>
  <tr>
    <td rowspan="3">SofaGeneralMeshCollision</td>
    <td>Sofa.Component.Collision.Geometry</td>
  </tr>
  <tr>
    <td>Sofa.Component.Collision.Detection.Algorithm</td>
  </tr>
  <tr>
    <td>Sofa.Component.Collision.Detection.Intersection</td>
  </tr>
  <tr>
    <td rowspan="3">SofaGeneralObjectInteraction</td>
    <td>Sofa.Component.SolidMechanics.Spring</td>
  </tr>
  <tr>
    <td>Sofa.Component.Constraint.Projective</td>
  </tr>
  <tr>
    <td>Sofa.Component.MechanicalLoad</td>
  </tr>
  <tr>
    <td rowspan="2">SofaGeneralTopology</td>
    <td>Sofa.Component.Topology.Container.Grid</td>
  </tr>
  <tr>
    <td>Sofa.Component.Topology.Container.Constant</td>
  </tr>
  <tr>
    <td rowspan="4">SofaGraphComponent</td>
    <td>Sofa.Component.SceneUtility</td>
  </tr>
  <tr>
    <td>Sofa.Component.Setting</td>
  </tr>
  <tr>
    <td>Sofa.GUI.Component</td>
  </tr>
  <tr>
    <td>the plugin SceneChecking</td>
  </tr>
  <tr>
    <td rowspan="6">SofaUserInteraction</td>
    <td>Sofa.Component.Collision.Geometry</td>
  </tr>
  <tr>
    <td>Sofa.Component.Collision.Detection.Algorithm</td>
  </tr>
  <tr>
    <td>Sofa.Component.Collision.Detection.Intersection</td>
  </tr>
  <tr>
    <td>Sofa.Component.Collision.Response.Contact</td>
  </tr>
  <tr>
    <td>Sofa.Component.Controller</td>
  </tr>
  <tr>
    <td>Sofa.GUI.Component (from Sofa.GUI)</td>
  </tr>
  <tr>
    <td rowspan="2">SofaTopologyMapping</td>
    <td>Sofa.Component.Topology.Mapping</td>
  </tr>
  <tr>
    <td>Sofa.Component.Mapping</td>
  </tr>
</tbody>
</table>


#### SofaMisc

<table>
<tbody>
  <tr>
    <td>SofaMiscExtra</td>
    <td>Sofa.Component.Engine.Generate</td>
  </tr>
  <tr>
    <td>SofaMiscTopology</td>
    <td>Sofa.Component.Topology.Utility</td>
  </tr>
  <tr>
    <td rowspan="4">SofaMiscCollision</td>
    <td>Sofa.Component.Collision.Geometry</td>
  </tr>
  <tr>
    <td>Sofa.Component.Collision.Detection.Intersection</td>
  </tr>
  <tr>
    <td>Sofa.Component.Collision.Response.Contact</td>
  </tr>
  <tr>
    <td>the plugin CollisionOBBCapsule</td>
  </tr>
  <tr>
    <td rowspan="2">SofaMiscEngine</td>
    <td>Sofa.Component.Engine.Analyze</td>
  </tr>
  <tr>
    <td>Sofa.Component.Engine.Transform</td>
  </tr>
  <tr>
    <td rowspan="3">SofaMiscFem</td>
    <td>Sofa.Component.SolidMechanics.FEM.Elastic</td>
  </tr>
  <tr>
    <td>Sofa.Component.SolidMechanics.FEM.HyperElastic</td>
  </tr>
  <tr>
    <td>Sofa.Component.SolidMechanics.TensorMass</td>
  </tr>
  <tr>
    <td rowspan="2">SofaMiscForceField</td>
    <td>Sofa.Component.Mass</td>
  </tr>
  <tr>
    <td>Sofa.Component.SolidMechanics.Spring</td>
  </tr>
  <tr>
    <td rowspan="2">SofaMiscSolver</td>
    <td>Sofa.Component.ODESolver.Backward</td>
  </tr>
  <tr>
    <td>Sofa.Component.ODESolver.Forward</td>
  </tr>
</tbody>
</table>


#### Plugins

<table>
<tbody>
  <tr>
    <td>SofaDenseSolver</td>
    <td>Sofa.Component.LinearSolver.Direct</td>
  </tr>
  <tr>
    <td>SofaExporter</td>
    <td>Sofa.Component.IO.Mesh and Sofa.Component.Playback</td>
  </tr>
  <tr>
    <td>SofaHaptics</td>
    <td>Sofa.Component.Haptics</td>
  </tr>
  <tr>
    <td>SofaValidation</td>
    <td>Sofa.Component.Playback</td>
  </tr>
  <tr>
    <td rowspan="3">SofaNonUniformFem</td>
    <td>Sofa.Component.Topology.Container.Grid</td>
  </tr>
  <tr>
    <td>Sofa.Component.Topology.Container.Dynamic</td>
  </tr>
  <tr>
    <td>Sofa.Component.SolidMechanics.FEM.NonUniform</td>
  </tr>
  <tr>
    <td rowspan="3">SofaOpenglVisual</td>
    <td>Sofa.GL.Component.Rendering2D</td>
  </tr>
  <tr>
    <td>Sofa.GL.Component.Rendering3D</td>
  </tr>
  <tr>
    <td>Sofa.GL.Component.Shader (from Sofa.GL)</td>
  </tr>
  <tr>
    <td rowspan="2">SofaPreconditioner</td>
    <td>Sofa.Component.LinearSolver.Iterative</td>
  </tr>
  <tr>
    <td>Sofa.Component.LinearSolver.Preconditioner</td>
  </tr>
  <tr>
    <td rowspan="2">SofaSparseSolver</td>
    <td>Sofa.Component.LinearSolver.Iterative</td>
  </tr>
  <tr>
    <td>Sofa.Component.LinearSolver.Direct</td>
  </tr>
</tbody>
</table>


#### Collection


<table>
<tbody>
  <tr>
    <td>SofaComponentAll</td>
    <td>Sofa.Component</td>
  </tr>
</tbody>
</table>


## Framework
SOFA-NG induced also a cleaning in the framework of SOFA. All parts of the framework have been renamed to reflect the same pattern started with Sofa.Component. For example, SofaSimulationGraph becomes Sofa.Simulation.Graph.

The list of the differents packages which are considered as part of the framework is:


<table>
<tbody>
  <tr>
    <td>SofaHelper</td>
    <td>Sofa.Helper</td>
  </tr>
  <tr>
    <td>SofaDefaulttype</td>
    <td>Sofa.Defaulttype</td>
  </tr>
  <tr>
    <td>SofaCore</td>
    <td>Sofa.Core</td>
  </tr>
  <tr>
    <td>SofaSimulationCore</td>
    <td>Sofa.Simulation.Core</td>
  </tr>
  <tr>
    <td>SofaSimulationCommon</td>
    <td>Sofa.Simulation.Common</td>
  </tr>
  <tr>
    <td>SofaSimulationGraph</td>
    <td>Sofa.Simulation.Graph</td>
  </tr>
  <tr>
    <td></td>
    <td>Sofa.Config (new), which gathers all CMake files used in SOFA projects (macros, config, flags, etc)</td>
  </tr>
  <tr>
    <td></td>
    <td>Sofa.Type (new)</td>
  </tr>
  <tr>
    <td></td>
    <td>Sofa.LinearAlgebra (new)</td>
  </tr>
  <tr>
    <td></td>
    <td>Sofa.Geometry (new)</td>
  </tr>
  <tr>
    <td></td>
    <td>Sofa.Topology (new)</td>
  </tr>
</tbody>
</table>


## Report technical issues
In case you face any technical difficulty in the transition, please report it using our [GitHub Discussion forum](https://github.com/sofa-framework/sofa/discussions/new).
