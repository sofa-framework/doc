Intro
=====

In order to allow building plugins separately from Sofa and building an
external application or library which depends on sofa, we provide cmake
package configurations files. Those files are what cmake looks for when
you call find\_package(Something), which is now how you find the
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

SofaFramework
-------------

-   SofaHelper
-   SofaDefaultType
-   SofaCore

SofaSimulation
--------------

-   SofaSimulationCommon
-   SofaSimulationTree
-   SofaSimulationGraph

SofaBase
--------

-   SofaBaseAnimationLoop
-   SofaBaseCollision
-   SofaBaseLinearSolver
-   SofaBaseMechanics
-   SofaBaseTopology
-   SofaBaseVisual
-   SofaComponentBase

SofaCommon
----------

-   SofaComponentCommon
-   SofaDeformable
-   SofaExplicitOdeSolver
-   SofaImplicitOdeSolver
-   SofaLoader
-   SofaMeshCollision
-   SofaObjectInteraction
-   SofaRigid
-   SofaSimpleFem

SofaGeneral
-----------

-   SofaBoundaryCondition
-   SofaComponentGeneral
-   SofaConstraint
-   SofaEngine
-   SofaExporter
-   SofaGraphComponent
-   SofaHaptics
-   SofaPreconditioner
-   SofaSparseSolver
-   SofaTopologyMapping
-   SofaUserInteraction
-   SofaValidation
-   SofaDenseSolver
-   SofaOpenglVisual
-   SofaTaucsSolver
-   SofaEigen2Solver
-   SofaPardisoSolver

SofaAdvanced
------------

-   SofaComponentAdvanced
-   SofaEulerianFluid
-   SofaNonUniformFem
-   SofaSphFluid
-   SofaVolumetricData

SofaMisc
--------

-   SofaComponentMisc
-   SofaMisc
-   SofaMiscCollision
-   SofaMiscEngine
-   SofaMiscFem
-   SofaMiscForceField
-   SofaMiscMapping
-   SofaMiscSolver
-   SofaMiscTopology

SofaGui
-------

-   SofaGuiCommon
-   SofaGuiGlut
-   SofaGuiQt
-   SofaGuiMain

Simple Plugin
=============

Minimal CMakeLists.txt
----------------------

`cmake_minimum_required(VERSION 2.8.12)`\
`project(MyPlugin)`\
\
\
`set(HEADER_FILES`\
`    MyHeaderFile1.h`\
`    MyHeaderFile2.h`\
`    MyHeaderFile3.h`\
`)`\
\
`set(SOURCE_FILES`\
`    MySourceFile1.cpp`\
`    MySourceFile2.cpp`\
`    MySourceFile3.cpp`\
`)`\
\
`find_package(SofaFramework REQUIRED)`\
\
`add_library(${PROJECT_NAME} SHARED ${HEADER_FILES} ${SOURCE_FILES})`\
`target_link_libraries(${PROJECT_NAME} SofaCore)`

Installation rules
------------------

Install the *Foo* library in <prefix>/lib, or <prefix>/bin on Windows.

`install(TARGETS Foo`\
`        RUNTIME DESTINATION bin`\
`        LIBRARY DESTINATION lib`\
`        ARCHIVE DESTINATION lib)`

Plugin usable as a library
==========================

Include directories
-------------------

### From the build directory

Use the current source directory as an include directory when linking
against MyPlugin from the build tree:

` target_include_directories(MyPlugin PUBLIC "$`<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>`")`

### From the installed location

Use <prefix>/include as an include directory when linking against the
installed MyPlugin library

` target_include_directories(MyPlugin PUBLIC "$`<INSTALL_INTERFACE:include>`")`

Installation rules
------------------

### Declare public headers

The public headers of a target are the headers that should be installed
with this target.

`set_target_properties(MyPlugin PROPERTIES PUBLIC_HEADER "${HEADER_FILES}")`

### Install headers and binaries

`install(TARGETS MyPlugin`\
`        EXPORT MyPluginTargets`\
`        RUNTIME DESTINATION bin`\
`        LIBRARY DESTINATION lib`\
`        ARCHIVE DESTINATION lib`\
`        PUBLIC_HEADER DESTINATION include/MyPlugin)`

Which is exactly what this macro does :

`sofa_install_targets(MyPlugin MyPlugin MyPlugin) # package-name target-name include-subdir-`

Create and install CMake package configuration files
----------------------------------------------------

`sofa_write_package_config_files(MyPlugin 0.1)`

This macro expects a MyPluginConfig.cmake.in template.

### Minimal MyPluginConfig.cmake.in

`@PACKAGE_INIT@`\
\
`if(NOT TARGET MyPlugin)`\
`    include("${CMAKE_CURRENT_LIST_DIR}/MyPluginTargets.cmake")`\
`endif()`\
\
`check_required_components(MyPlugin)`

External application or library which depends on Sofa
=====================================================

Introduction
------------

You have got a copy of a Sofa distribution (produced by a "make install"
in Sofa) and want to use it as a lib in your project, or run Sofa
simulation directly.

In your project
---------------

### How to build

Your application or library CMakeLists.txt should contain something
similar to:

` find_package(SofaFramework REQUIRED)`\
` add_executable(myApp ${HEADER_FILES} ${SOURCE_FILES})`\
` target_link_libraries(myApp SofaCore OtherLibs)`

To tell cmake where to find sofa cmake files

` CMAKE_MODULE_PATH=/path/to/sofa/lib/cmake cmake /path/to/myProject/src`

### How to run

To be able to run your application from its build tree, you need to tell
Sofa where it is installed using the SOFA\_ROOT environment variable.

` SOFA_ROOT=/path/to/sofa`

Sofa needs it to be access its resources such as plugin defined python
packages.

Once your application is installed in the same prefix as sofa

` /path/to/sofa/bin/myApp`

You do not need SOFA\_ROOT any more.

A sofa plugin in your project
-----------------------------

### How to build

This plugin has CMakeLists.txt similar to a plugin compiled along with
sofa. If your plugin contains python files you normally have a call to
sofa\_set\_python\_directory() macro. The config file generated by this
macro needs to be copy to the Sofa root :

` # Config files and install rules for pythons scripts`\
` sofa_set_python_directory(${PROJECT_NAME} "python")`\
` # copy the python config file to sofa install dir`\
` file(COPY "${CMAKE_BINARY_DIR}/etc/sofa/python.d/${PROJECT_NAME}" DESTINATION "${SOFA_ROOT}/etc/sofa/python.d/")`

### How to run

Sofa looks for plugins in a list of *PluginRepository*, in your
application *main* you need to setup this *PluginRepository* :

` sofa::helper::system::PluginRepository.addFirstPath(QCoreApplication::applicationDirPath().toStdString()+"/../lib"); // Your plugin compiled with your application`
