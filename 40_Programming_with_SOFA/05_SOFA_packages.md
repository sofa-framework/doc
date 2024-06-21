---
title: SOFA packages
---

Intro
=====

In order to allow building plugins separately from Sofa and building an
external application or library which depends on sofa, we provide cmake
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

SofaFramework
-------------

-   SofaCore
-   SofaDefaultType
-   SofaHelper
-   SofaSimulationCore

SofaSimulation
--------------

-   SofaSimulationCommon
-   SofaSimulationGraph
-   SofaSimulationTree

SofaBase
--------

-   SofaBaseCollision
-   SofaBaseLinearSolver
-   SofaBaseMechanics
-   SofaBaseTopology
-   SofaBaseVisual
-   SofaBaseUtils

SofaCommon
----------

-   SofaDeformable
-   SofaEigen2Solver
-   SofaEngine
-   SofaExplicitOdeSolver
-   SofaImplicitOdeSolver
-   SofaLoader
-   SofaMeshCollision
-   SofaObjectInteraction
-   SofaRigid
-   SofaSimpleFem

SofaGeneral
-----------

-   SofaGeneralAnimationLoop
-   SofaGeneralDeformable
-   SofaGeneralExplicitOdeSolver
-   SofaGeneralImplicitOdeSolver
-   SofaGeneralLinearSolver
-   SofaGeneralLoader
-   SofaGeneralMeshCollision
-   SofaGeneralObjectInteraction
-   SofaGeneralRigid
-   SofaGeneralSimpleFem
-   SofaGeneralTopology
-   SofaGeneralVisual
-   SofaBoundaryCondition
-   SofaConstraint
-   SofaGeneralEngine
-   SofaGraphComponent
-   SofaTopologyMapping
-   SofaUserInteraction
-   SofaValidation

SofaAdvanced
------------

-   SofaNonUniformFem

SofaMisc
--------

-   SofaMiscExtra
-   SofaMiscEngine
-   SofaMiscFem
-   SofaMiscForceField
-   SofaMiscMapping
-   SofaMiscSolver
-   SofaMiscTopology

SofaGui
-------

-   SofaGuiCommon
-   SofaGuiQt
-   SofaGuiMain
-   SofaHeadlessRecorder
