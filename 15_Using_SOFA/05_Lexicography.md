# Lexicography

## Library
Libraries are the central elements of SOFA. They define all SOFA framework mechanisms at the very core.

Libraries do not contain Components.
Libraries are not externalizable. They are all within SOFA sources.
Some Libraries can be disabled via a CMake option.

A Library can "contain" other Libraries. Technically, it will have link dependencies on those Libraries.

From the system point of view, a Library is a dynamic library (.so or .dylib or .dll).

Examples: Sofa.Core, Sofa.Type

## Module
Modules are the elements defining all usual SOFA features with Components.
Modules can be loaded in a Simulation by the Plugin Manager via the Component `RequiredPlugin` in a scene, or the runSofa parameter `-l ModuleName`, or within the `plugin_list.conf` file.

Modules contain Components.
Modules are not externalizable. They are all within SOFA sources.
Modules can be disabled via a CMake option. Most Modules are ON by default.

A Module can "contain" other Modules and Libraries. Technically, it will have link dependencies on those Modules.

From the system point of view, a Module is a dynamic library (.so or .dylib or .dll).

Examples: Sofa.Component.Collision, Sofa.Component.Engine.Analyze, Sofa.Component.SolidMechanics

## Plugin
Plugins are optional Modules adding more SOFA features.

Plugins contain Components.
Plugins are externalizable. Some external plugins can be auto-fetched from SOFA sources.
Plugins can be disabled via a CMake option. Most Plugins are OFF by default.

A Plugin can "contain" other Modules and Libraries. Technically, it will have link dependencies on those Modules.

From the system point of view, a Plugin is a dynamic library (.so or .dylib or .dll).

Examples: SofaPython3, SofaCUDA, CImgPlugin

## Collection
Collections are interfaces for sets of Modules and/or Libraries.

Collections do not contain any code.
Collections can be disabled via a CMake option.

From the system point of view, a Collection is a dynamic library (.so or .dylib or .dll).

Examples: SofaComponentAll, SofaBaseTopology, SofaGeneralMeshCollision

## Project
Projects are programs using parts of SOFA as dependency.
The goal of Projects is to create tools based on SOFA.

From the system point of view, a Project is an executable.

Examples: runSofa, SofaPhysicsAPI

## Tutorial
Tutorials are programs using parts of SOFA as dependency.
The goal of Tutorials is to show how to build a Simulation with SOFA API.

From the system point of view, a Tutorial is an executable.

Examples: chainHybrid, oneTetrahedron

## Simulation
To be completed.

## Scene
To be completed.

## Example
To be completed.


## Unit test
To be completed.

## Scene test
To be completed.

## Regression test
To be completed.


## Link
To be completed.

## Component
To be completed.

## Data
To be completed.

## DataField
To be completed.

## Link
To be completed.

## Node
To be completed.

