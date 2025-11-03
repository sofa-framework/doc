---
title: Suported Plugins List
---

# Officially supported plugins

This page aims at summarizing all plugins that are officially supported by the SOFA consortium.
This means that the SOFA consortium commits to:

1. Including them in our continuous integration pipeline, thus assessing the compilation at every push in the SOFA master branch, at each new pull-request and at each nightly build
2. Including them in the official bi-annual SOFA binaries 
3. Providing technical support on these plugins

| Plugin Name | Description |
| ----------- | ----------- |
| [ArticulatedSystemPlugin](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/ArticulatedSystemPlugin)* | Plugin that allow the simulation of rigid kinematic chains.  |
| [BeamAdapter](https://www.github.com/sofa-framework/BeamAdapter.git) | Plugin implementing a 1-dimensional Finite Element Method (FEM) based on the Kirchhoff rod theory and allows to simulate any 1D flexible structure.  |
| [CGALPlugin](https://www.github.com/sofa-framework/CGALPlugin.git) | Plugins offering SOFA bindings to the [CGAL library](https://www.cgal.org/) for meshing purposes.  |
| [CSparseSolvers](https://www.github.com/sofa-framework/CSparseSolvers.git) | Plugin containing a collection of linear solver components that are built on top of the [CSparse library](https://people.math.sc.edu/Burkardt/c_src/csparse/csparse.html).  |
| [Geomagic](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/Geomagic)* | Plugin enabling the use of the [Touch haptic device from 3D Systems](https://www.3dsystems.com/haptics-devices/touch).  |
| [ModelOrderReduction](https://www.github.com/SofaDefrost/ModelOrderReduction.git) | Plugin containing C++ components with python utilities allowing to perform model reduction and use these reduced model easily in a SOFA scene.  |
| [MultiThreading](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/MultiThreading)* | Plugin implementing CPU-parallelized version of some SOFA components.  |
| [PluginExample](https://www.github.com/sofa-framework/PluginExample.git) | A template and a good starting point to create a new plugin from scratch.  |
| [Registration](https://www.github.com/sofa-framework/Registration.git) | Plugin offering registering tools for deformable surfaces.  |
| [STLIB](https://www.github.com/SofaDefrost/STLIB.git) | Sofa Template Library: high level reusable python objects used to write complex parts of a simulation.  |
| [SceneChecking](https://github.com/sofa-framework/sofa/tree/master/applications/projects/SceneChecking)* | Plugin developed to provide insights to user when a scene launched with runSofa uses deprecated components/datas.  |
| [Sofa.Metis](https://www.github.com/sofa-framework/Sofa.Metis.git) | Plugin adding METIS-based ordering method for SOFA's linear solvers.  |
| [Sofa.Qt](https://www.github.com/sofa-framework/Sofa.Qt.git) | Plugin containing Qt-based GUI for SOFA.  |
| [SofaCUDA](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/SofaCUDA)* | Plugin that provides a number of SOFA components that have been re-implemented using CUDA.  |
| [SofaDistanceGrid](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/SofaDistanceGrid)* | Plugin named SofaDistanceGrid. |
| [SofaGLFW](https://www.github.com/sofa-framework/SofaGLFW.git) | Project containing two plugins: a simple GUI based on GLFW and a user interface based on [Dear ImGui](https://github.com/ocornut/imgui).  |
| [SofaMatrix](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/SofaMatrix)* | Plugin containing components used to provide insights on linear system matrices by exporting them of drawing them.  |
| [SofaPhysicsAPI](https://github.com/sofa-framework/sofa/tree/master/applications/projects/SofaPhysicsAPI)* | Application named SofaPhysicsAPI. |
| [SofaPython3](https://www.github.com/sofa-framework/SofaPython3.git) | Plugin enabling to write SOFA scenes in Python that also introduce several Python modules that exposes different C++ components used in SOFA.  |
| [SofaViscoElastic](https://www.github.com/SofaDefrost/SofaViscoElastic.git) | External Plugin named SofaViscoElastic that needs to be fetched. |
| [SoftRobots](https://www.github.com/SofaDefrost/SoftRobots.git) | Plugin containing components dedicated to forward simulation of soft robots.  |
| [SoftRobots.Inverse](https://www.github.com/SofaDefrost/SoftRobots.Inverse.git) | External Plugin named SoftRobots.Inverse that needs to be fetched. |
| [VolumetricRendering](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/VolumetricRendering)* | Plugin named VolumetricRendering. |
| [runSofa](https://github.com/sofa-framework/sofa/tree/master/applications/projects/runSofa)* | Project containing the main runSofa, used to launch the scene files.  |

(*) Projects which sources are present in SOFA sources
