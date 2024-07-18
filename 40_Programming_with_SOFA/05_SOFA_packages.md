Intro
=====

In order to allow building plugins separately from SOFA and building an
external application or library which depends on SOFA, we provide cmake
package configurations files. Those files are what cmake looks for when
you call find_package(Something), which is now how you find the
dependencies for your plugins.

The repository is divided in multiple packages: *SofaFramework* for
framework/, *SofaSimulation* for sofa/simulation, five packages for
modules (divided according to the *SofaComponent\** meta-libraries), and
*SofaGui* for GUI-related libraries.

Also, there is a package for each plugin that is expected to be used as
a library. (E.g. SofaPython, Compliant, Flexible...)

The following section lists the libraries is each package.

Packages
========

Sofa.Framework
--------------

- Sofa.Type
- Sofa.LinearAlgebra
- Sofa.Core
- Sofa.Config
- Sofa.Topology
- Sofa.Testing
- Sofa.Simulation
- Sofa.SimpleApi
- Sofa.Helper
- Sofa.Geometry
- Sofa.DefaultType


Sofa.Component
--------------

- Sofa.Component.AnimationLoop
- Sofa.Component.Collision
- Sofa.Component.Constraint
- Sofa.Component.Controller
- Sofa.Component.Diffusion
- Sofa.Component.Engine
- Sofa.Component.Haptics
- Sofa.Component.IO
- Sofa.Component.LinearSolver
- Sofa.Component.LinearSystem
- Sofa.Component.Mapping
- Sofa.Component.Mass
- Sofa.Component.MechanicalLoad
- Sofa.Component.ODESolver
- Sofa.Component.Playback
- Sofa.Component.SceneUtility
- Sofa.Component.Setting
- Sofa.Component.SolidMechanics
- Sofa.Component.StateContainer
- Sofa.Component.Topology
- Sofa.Component.Visual


Sofa.GL
--------------

- Sofa.GL
- Sofa.GL.Component.Engine
- Sofa.GL.Component.Rendering2D
- Sofa.GL.Component.Rendering3D
- Sofa.GL.Component.Shader


Sofa.GUI
--------------

- Sofa.GUI
- Sofa.GUI.Batch
- Sofa.GUI.Common
- Sofa.GUI.Component
- Sofa.GUI.HeadlessRecorder
- Sofa.GUI.Qt
