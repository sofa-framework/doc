---
title: Activate Plugins
---

# Activable plugins for in-tree compilation

Multiple extensions can be activated when building the project. They fall into three categories:
1. Applications: extensions that offer SOFA-based executable applications (e.g. a main for launching SOFA)
2. Plugins: extensions that enriche the SOFA API by adding new components or providing more support for external libraries (e.g. new constitutive laws, alternative GUIs)
3. Directories: extensions that contain multiple CMake projects that cannot be described by only one of the above type
Moreover, these projects are either present in the SOFA sources or they need to be fetched (meaning that they have their own external repository).

This page aims at summarizing those extensions in tables containing:
- the name + hyperlink to the extension sources either in the SOFA repository or in its own repository
- a short description
- activation directives

The activation directives propose two ways of activating those plugins in the build tree:
1. Through custom CMake flags that [can be added during the CMake call](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-D). All of those plugins can be activated with one or two CMake flags named using their type and name. For example, the plugin SofaPython3 can be activated by activating both flags `SOFA_FETCH_SOFAPYTHON3=ON` and `PLUGIN_SOFAPYTHON3=ON` (because its sources are in a separate repository).
2. Through preset that can be [specified during the CMake call](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html#introduction)

### Applications

|Name|Description|How to activate|
|---|---|---|
|[Modeler](https://github.com/sofa-framework/sofa/tree/master/applications/projects/Modeler)|Application named Modeler.|CMake flag `APPLICATION_MODELER=ON`. |
|[SceneChecking](https://github.com/sofa-framework/sofa/tree/master/applications/projects/SceneChecking)|Application named SceneChecking.|CMake flag `APPLICATION_SCENECHECKING=ON`. Activated in presets ['full', 'minimal', 'standard', 'supported-plugins']. |
|[SofaPhysicsAPI](https://github.com/sofa-framework/sofa/tree/master/applications/projects/SofaPhysicsAPI)|Application named SofaPhysicsAPI.|CMake flag `APPLICATION_SOFAPHYSICSAPI=ON`. Activated in presets ['full', 'standard', 'supported-plugins']. |
|[runSofa](https://github.com/sofa-framework/sofa/tree/master/applications/projects/runSofa)|Application named runSofa.|CMake flag `APPLICATION_RUNSOFA=ON`. Activated in presets ['full', 'minimal', 'standard', 'supported-plugins']. |
|[sofaProjectExample](https://github.com/sofa-framework/sofa/tree/master/applications/projects/sofaProjectExample)|Application named sofaProjectExample.|CMake flag `APPLICATION_SOFAPROJECTEXAMPLE=ON`. |


### Plugins

|Name|Description|How to activate|
|---|---|---|
|[ArticulatedSystemPlugin](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/ArticulatedSystemPlugin)|Plugin named ArticulatedSystemPlugin.|CMake flag `PLUGIN_ARTICULATEDSYSTEMPLUGIN=ON`. Activated in presets ['full', 'supported-plugins']. |
|[BeamAdapter](https://www.github.com/sofa-framework/BeamAdapter.git)|External Plugin named BeamAdapter that needs to be fetched.|CMake flags `SOFA_FETCH_BEAMADAPTER=ON` and `PLUGIN_BEAMADAPTER=ON`. Activated in presets ['full', 'supported-plugins']. |
|[BulletCollisionDetection](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/BulletCollisionDetection)|Plugin named BulletCollisionDetection.|CMake flag `PLUGIN_BULLETCOLLISIONDETECTION=ON`. |
|[CGALPlugin](https://www.github.com/sofa-framework/CGALPlugin.git)|External Plugin named CGALPlugin that needs to be fetched.|CMake flags `SOFA_FETCH_CGALPLUGIN=ON` and `PLUGIN_CGALPLUGIN=ON`. Activated in presets ['full', 'supported-plugins']. |
|[CImgPlugin](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/CImgPlugin)|Plugin named CImgPlugin.|CMake flag `PLUGIN_CIMGPLUGIN=ON`. Activated in presets ['full']. |
|[CSparseSolvers](https://www.github.com/sofa-framework/CSparseSolvers.git)|External Plugin named CSparseSolvers that needs to be fetched.|CMake flags `SOFA_FETCH_CSPARSESOLVERS=ON` and `PLUGIN_CSPARSESOLVERS=ON`. Activated in presets ['full', 'supported-plugins']. |
|[CollisionAlgorithm](https://forge.icube.unistra.fr/sofa/CollisionAlgorithm.git)|External Plugin named CollisionAlgorithm that needs to be fetched.|CMake flags `SOFA_FETCH_COLLISIONALGORITHM=ON` and `PLUGIN_COLLISIONALGORITHM=ON`. |
|[CollisionOBBCapsule](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/CollisionOBBCapsule)|Plugin named CollisionOBBCapsule.|CMake flag `PLUGIN_COLLISIONOBBCAPSULE=ON`. Activated in presets ['full']. |
|[ConstraintGeometry](https://forge.icube.unistra.fr/sofa/ConstraintGeometry.git)|External Plugin named ConstraintGeometry that needs to be fetched.|CMake flags `SOFA_FETCH_CONSTRAINTGEOMETRY=ON` and `PLUGIN_CONSTRAINTGEOMETRY=ON`. |
|[Cosserat](https://www.github.com/SofaDefrost/Cosserat.git)|External Plugin named Cosserat that needs to be fetched.|CMake flags `SOFA_FETCH_COSSERAT=ON` and `PLUGIN_COSSERAT=ON`. |
|[DiffusionSolver](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/DiffusionSolver)|Plugin named DiffusionSolver.|CMake flag `PLUGIN_DIFFUSIONSOLVER=ON`. Activated in presets ['full']. |
|[Geomagic](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/Geomagic)|Plugin named Geomagic.|CMake flag `PLUGIN_GEOMAGIC=ON`. Activated in presets ['full', 'supported-plugins']. |
|[Haption](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/Haption)|Plugin named Haption.|CMake flag `PLUGIN_HAPTION=ON`. |
|[HeadlessRecorder](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/HeadlessRecorder)|Plugin named HeadlessRecorder.|CMake flag `PLUGIN_HEADLESSRECORDER=ON`. |
|[LeapMotion](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/LeapMotion)|Plugin named LeapMotion.|CMake flag `PLUGIN_LEAPMOTION=ON`. |
|[ManifoldTopologies](https://www.github.com/sofa-framework/ManifoldTopologies.git)|External Plugin named ManifoldTopologies that needs to be fetched.|CMake flags `SOFA_FETCH_MANIFOLDTOPOLOGIES=ON` and `PLUGIN_MANIFOLDTOPOLOGIES=ON`. Activated in presets ['full']. |
|[MeshSTEPLoader](https://www.github.com/sofa-framework/MeshSTEPLoader.git)|External Plugin named MeshSTEPLoader that needs to be fetched.|CMake flags `SOFA_FETCH_MESHSTEPLOADER=ON` and `PLUGIN_MESHSTEPLOADER=ON`. |
|[ModelOrderReduction](https://www.github.com/SofaDefrost/ModelOrderReduction.git)|External Plugin named ModelOrderReduction that needs to be fetched.|CMake flags `SOFA_FETCH_MODELORDERREDUCTION=ON` and `PLUGIN_MODELORDERREDUCTION=ON`. Activated in presets ['full', 'supported-plugins']. |
|[MultiThreading](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/MultiThreading)|Plugin named MultiThreading.|CMake flag `PLUGIN_MULTITHREADING=ON`. Activated in presets ['conda-core', 'full', 'minimal', 'standard', 'supported-plugins']. |
|[PSL](https://www.github.com/sofa-framework/PSL.git)|External Plugin named PSL that needs to be fetched.|CMake flags `SOFA_FETCH_PSL=ON` and `PLUGIN_PSL=ON`. |
|[PersistentContact](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/PersistentContact)|Plugin named PersistentContact.|CMake flag `PLUGIN_PERSISTENTCONTACT=ON`. |
|[PluginExample](https://www.github.com/sofa-framework/PluginExample.git)|External Plugin named PluginExample that needs to be fetched.|CMake flags `SOFA_FETCH_PLUGINEXAMPLE=ON` and `PLUGIN_PLUGINEXAMPLE=ON`. Activated in presets ['full', 'supported-plugins']. |
|[Registration](https://www.github.com/sofa-framework/Registration.git)|External Plugin named Registration that needs to be fetched.|CMake flags `SOFA_FETCH_REGISTRATION=ON` and `PLUGIN_REGISTRATION=ON`. Activated in presets ['full', 'supported-plugins']. |
|[STLIB](https://www.github.com/SofaDefrost/STLIB.git)|External Plugin named STLIB that needs to be fetched.|CMake flags `SOFA_FETCH_STLIB=ON` and `PLUGIN_STLIB=ON`. Activated in presets ['full', 'supported-plugins']. |
|[Sensable](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/Sensable)|Plugin named Sensable.|CMake flag `PLUGIN_SENSABLE=ON`. Activated in presets ['full']. |
|[ShapeMatchingPlugin](https://www.github.com/sofa-framework/ShapeMatchingPlugin.git)|External Plugin named ShapeMatchingPlugin that needs to be fetched.|CMake flags `SOFA_FETCH_SHAPEMATCHINGPLUGIN=ON` and `PLUGIN_SHAPEMATCHINGPLUGIN=ON`. |
|[SixenseHydra](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/SixenseHydra)|Plugin named SixenseHydra.|CMake flag `PLUGIN_SIXENSEHYDRA=ON`. |
|[Sofa.Metis](https://www.github.com/sofa-framework/Sofa.Metis.git)|External Plugin named Sofa.Metis that needs to be fetched.|CMake flags `SOFA_FETCH_SOFA_METIS=ON` and `PLUGIN_SOFA_METIS=ON`. Activated in presets ['full', 'supported-plugins']. |
|[Sofa.Qt](https://www.github.com/sofa-framework/Sofa.Qt.git)|External Plugin named Sofa.Qt that needs to be fetched.|CMake flags `SOFA_FETCH_SOFA_QT=ON` and `PLUGIN_SOFA_QT=ON`. Activated in presets ['full', 'supported-plugins']. |
|[SofaAssimp](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/SofaAssimp)|Plugin named SofaAssimp.|CMake flag `PLUGIN_SOFAASSIMP=ON`. |
|[SofaCUDA](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/SofaCUDA)|Plugin named SofaCUDA.|CMake flag `PLUGIN_SOFACUDA=ON`. Activated in presets ['full', 'supported-plugins']. |
|[SofaCarving](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/SofaCarving)|Plugin named SofaCarving.|CMake flag `PLUGIN_SOFACARVING=ON`. Activated in presets ['full']. |
|[SofaDistanceGrid](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/SofaDistanceGrid)|Plugin named SofaDistanceGrid.|CMake flag `PLUGIN_SOFADISTANCEGRID=ON`. Activated in presets ['full']. |
|[SofaEulerianFluid](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/SofaEulerianFluid)|Plugin named SofaEulerianFluid.|CMake flag `PLUGIN_SOFAEULERIANFLUID=ON`. Activated in presets ['full']. |
|[SofaHAPI](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/SofaHAPI)|Plugin named SofaHAPI.|CMake flag `PLUGIN_SOFAHAPI=ON`. |
|[SofaImplicitField](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/SofaImplicitField)|Plugin named SofaImplicitField.|CMake flag `PLUGIN_SOFAIMPLICITFIELD=ON`. Activated in presets ['full']. |
|[SofaMatrix](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/SofaMatrix)|Plugin named SofaMatrix.|CMake flag `PLUGIN_SOFAMATRIX=ON`. Activated in presets ['full', 'supported-plugins']. |
|[SofaNewmat](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/SofaNewmat)|Plugin named SofaNewmat.|CMake flag `PLUGIN_SOFANEWMAT=ON`. |
|[SofaOpenCL](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/SofaOpenCL)|Plugin named SofaOpenCL.|CMake flag `PLUGIN_SOFAOPENCL=ON`. |
|[SofaPardisoSolver](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/SofaPardisoSolver)|Plugin named SofaPardisoSolver.|CMake flag `PLUGIN_SOFAPARDISOSOLVER=ON`. |
|[SofaSphFluid](https://www.github.com/sofa-framework/SofaSphFluid.git)|External Plugin named SofaSphFluid that needs to be fetched.|CMake flags `SOFA_FETCH_SOFASPHFLUID=ON` and `PLUGIN_SOFASPHFLUID=ON`. Activated in presets ['full']. |
|[SofaTest](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/SofaTest)|Plugin named SofaTest.|CMake flag `PLUGIN_SOFATEST=ON`. |
|[SofaValidation](https://www.github.com/sofa-framework/SofaValidation.git)|External Plugin named SofaValidation that needs to be fetched.|CMake flags `SOFA_FETCH_SOFAVALIDATION=ON` and `PLUGIN_SOFAVALIDATION=ON`. |
|[SoftRobots](https://www.github.com/SofaDefrost/SoftRobots.git)|External Plugin named SoftRobots that needs to be fetched.|CMake flags `SOFA_FETCH_SOFTROBOTS=ON` and `PLUGIN_SOFTROBOTS=ON`. Activated in presets ['full', 'supported-plugins']. |
|[VolumetricRendering](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/VolumetricRendering)|Plugin named VolumetricRendering.|CMake flag `PLUGIN_VOLUMETRICRENDERING=ON`. Activated in presets ['full', 'supported-plugins']. |
|[Xitact](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/Xitact)|Plugin named Xitact.|CMake flag `PLUGIN_XITACT=ON`. |
|[image](https://github.com/sofa-framework/sofa/tree/master/applications/plugins/image)|Plugin named image.|CMake flag `PLUGIN_IMAGE=ON`. Activated in presets ['full']. |


### Directories

|Name|Description|How to activate|
|---|---|---|
|[Regression](https://www.github.com/sofa-framework/Regression.git)|External Directory named Regression that needs to be fetched.|CMake flags `SOFA_FETCH_REGRESSION=ON` and `DIRECTORY_REGRESSION=ON`. |
|[SofaGLFW](https://www.github.com/sofa-framework/SofaGLFW.git)|External Directory named SofaGLFW that needs to be fetched.|CMake flags `SOFA_FETCH_SOFAGLFW=ON` and `DIRECTORY_SOFAGLFW=ON`. Activated in presets ['full', 'standard', 'supported-plugins']. |
|[SofaHighOrder](https://www.github.com/sofa-framework/SofaHighOrder.git)|External Directory named SofaHighOrder that needs to be fetched.|CMake flags `SOFA_FETCH_SOFAHIGHORDER=ON` and `DIRECTORY_SOFAHIGHORDER=ON`. |
|[SofaPython3](https://www.github.com/sofa-framework/SofaPython3.git)|External Directory named SofaPython3 that needs to be fetched.|CMake flags `SOFA_FETCH_SOFAPYTHON3=ON` and `DIRECTORY_SOFAPYTHON3=ON`. Activated in presets ['full', 'standard', 'supported-plugins']. |


