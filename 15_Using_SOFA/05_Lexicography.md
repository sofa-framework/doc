# Lexicography

## Library
Libraries are the central elements of SOFA. They define all SOFA framework mechanisms in [Sofa/framework](https://github.com/sofa-framework/sofa/tree/master/Sofa/framework).

Libraries do not contain Components.
Libraries are not externalizable. They are all within SOFA sources.
Some Libraries can be disabled via a CMake option.

A Library can "contain" other Libraries. Technically, it will have link dependencies on those Libraries.

From the system point of view, a Library is a dynamic library (.so or .dylib or .dll).

Examples: Sofa.Core, Sofa.Type

## Module
Modules are the elements defining all usual SOFA features with Components in [Sofa/Component](https://github.com/sofa-framework/sofa/tree/master/Sofa/Component).
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
Plugins are externalizable. Some external plugins can be [auto-fetched into SOFA sources](../plugins/fetch-plugin-code-source/).
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
Simulation corresponds to the process computing the change of state of the physical systems, given their rest and initial state.

## Scene
Scene denotes the graph structure (direct acyclic graph) describing the physical systems, their physical behavior, their properties and the numerical tools used for the computation. The Scene description starts with a root Node which then contains child Nodes (sub-Nodes). Each child Node of the root Node usually corresponds to one object (one physical system).
Read more about the [Scene graph](../simulation-principles/scene-graph/) 

## Example
Example refers to set of Scene files provided with SOFA. These Scene files illustrate most of the SOFA components in a dedicated Simulation. They can be found within the _examples/_ folder in the SOFA sources or within the _share/sofa/examples/_ folder in the SOFA binaries.


## Unit test
Scene tests correspond to C++ codes testing SOFA classes or parts of codes to assess their proper functioning.
Unit tests can be triggered on each pull-request.

## Scene test
Scene tests correspond to Scene files which are launched to check if the associated Simulations run without error.
Scene tests can be triggered on each pull-request.

## Regression test
Regression tests correspond to Scene files which Simulation result configuration was previously saved. These tests are launched to check if the Simulation remains consistent with the save Simulation result.
Regression tests can be triggered on each pull-request.


## Node
Node defines a hierarchical level of the Scene graph. The root Node is the entry point of the simulation (first Node without any parent) and it may contain several child Nodes (sub-Nodes). Each child Node of the root Node usually corresponds to one object (one physical system). Generally, a Node can have many children, and it may have several parent (except the root Node). An operation performed on a Node automatically propagates its effect to all of its child Nodes. The collection of all Nodes builds the Scene graph.

## Component
Component corresponds to C++ classes implementing specific physical models or algorithms. A Component must belong to a Node.

## Data
Data is a public attribute of a Component (C++ class) visible to the user in the SOFA user interface. For a physical model or an algorithm, a Data is a parameter available for the user (e.g. the total mass `totalMass` in a mass component). Data may be defined by the user (some are compulsory - a.k.a. required - else a warning will be sent), accessed and modified.
Read more about [Data](../simulation-principles/scene-graph/#data).

## Datafield
DataField refers to a Data

## Link
Link corresponds to connection created between Data instances of two different Components. One Data may be linked to one or several other Data (respectively called a SingleLink and a MultiLink). The network of interconnected Data objects defines a Data dependency graph, superimposed on the Scene graph.
