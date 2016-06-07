Motivation
----------

A test suite for SOFA is being developed using the **googletest**
framework. Tests serve two purposes:

-   Automatically detect regressions. They are automatically run after
    each commit and their results are displayed on the dashboard. This
    way, changes which break existing features are detected as soon
    as possible.
-   Help developing. Creating the specific test at the same time as your
    new feature (test-oriented development) has significant advantages:
    -   it helps you specifying your code: what it does is what is
        tested
    -   focusing on your contribution, without being distracted by other
        stuff
    -   being sure that your contribution will not be accidentally
        broken by anyone.

In summary, test-oriented development generates **better code** and is
**easier**. Therefore, we strongly urge you to apply it. Feel free to
ask us for advice.

Activation
----------

When the **SOFA-MISC\_TESTS** option is checked in CMake, all the
modules/SofaModuleName/SofaModuleName\_test and
applications/plugins/PluginName/PluginName\_test projects are
automatically included by Cmake in the Sofa project/solution. Each test
project generates an executable, which outputs its results on the
standard output. The final output is the number of successful tests
(PASSED) and the number of fails (FAILED) if any.

Plugin **SofaTest** is the basis of all tests. It includes base classes
for creating tests in Sofa. As such, the other tests include it in their
cmake LinkerDependencies.

Several components of the sofa/modules directory are tested. It is far
from complete. Feel free to add some tests.

Other plugins provide tests, such as Compliant, Flexible and Image. Note
that the tests are generally not extensive, so they do not guaranty that
the code is bug-free.

Running the tests
-----------------

Once you build every tests you want, simply go in your build directory
and execute the following command in order to launch the whole test
suite:

` ctest --verbose`

How to create tests in your plugin
----------------------------------

Say you are creating **YourPlugin** in applications/plugins/YourPlugin.
The steps to create a test suite are:

-   create directory called
    applications/plugins/YourPlugin/**YourPlugin\_test** or some other
    name ending up with \_test, so that it is automatically included in
    the test suite.
-   in this directory, create a cmake project file for an executable,
    and set up dependencies on YourPlugin and on SofaTest. See e.g.
    applications/plugins/Compliant/Compliant\_test/**CMakeLists.txt**
-   create a number of .cpp files to test your classes. Each test or
    test suite typically derives from class **Sofa\_test** or one of the
    generic test classes derived from it: **Solver\_test**,
    **Mapping\_test**, **ForceField\_test** or
    **ProjectionConstraintSet\_test**. The test code typically includes
    checkings, such as ASSERT\_TRUE(bool). It is run by macros such as
    TEST\_F at the end of the file.

See e.g. Compliant\_test.

How to test components
----------------------

-   **Force field**: Force field tests should derive from the base class
    ForceField\_test.h available in plugin SofaTest.This base class
    creates a minimal scene with a mechanical object and a forcefield.
    Then call the function run\_test with positions, velocities and the
    corresponding expected forces. This function automatically checks
    not only the forces (function addForce), but also the stiffness
    (methods addDForce and addKToMatrix), using finite differences.

For example, see StiffSpringForceField\_test or
QuadPressureForceField\_test.

-   **Mapping**: Mapping tests should derive from the base class
    Mapping\_test.h available in plugin SofaTest.This base class creates
    a scene with two mechanical objects (parent and children nodes) and
    a mapping between them. Then it compares the actual output positions
    with the expected ones and automatically tests the methods related
    to Jacobian (applyJ, applyJT, applyDJT and getJs).

For example, RigidMapping\_test tests the mapping from local to world
coordinates.

-   **Solvers**: To test a solver, one tests its convergence to a
    static solution. For example, EulerImplicit\_test tests the
    convergence of euler implicit solver with a mass-spring system. This
    system is composed of 2 particles in gravity with one
    fixed particle. The other particle should move to a balance point.
    Then one checks two criteria:
    -   if it has converged
    -   if it has converged to the expected position

Other solver tests are available in Compliant\_test:
AssembledSolver\_test and DampedOscillator\_test.

-   **Projective constraint**: To test projective constraint, one
    creates a minimal scene with a mechanical object, a topology and the
    projective constraint. One defines the constraint parameters (points
    to project, normal of the projection...). Then one inits the scene
    and call the projectPosition() function. Finaly one checks two
    criteria:
    -   if constrained particle have the expected position.
    -   if unconstrained particle have not changed.

Some projective constraint tests are available in SofaTest\_test:
PRojectToLineConstraint and ProjectToPlaneConstraint.

-   **Engine test**: To test engine you set input values and check if
    the ouput values correspond to the expected ones. The test
    Engine\_test tests if the update method is called only if necessary.
    To test this a minimal engine TestEngine was created with a counter
    in its update method.

Test entirely written in python
-------------------------------

-   **Testing a Sofa scene**

The SofaTest plugin has a python API giving a Controller. You can write
a Sofa scene in python (with the regular SofaPython API and the
createScene function), and add a SofaTest.Controller to your scene. From
the SofaTest.Controller you can return the test result (functions
sendSuccess / sendFailure). A message can be passed in case of failure.
Warning: do not forget to call the base function
SofaTest.Controller.onLoaded if your surcharge this function in your
controller.

-   **Test a pure python function** (independent from SOFA)

You simply need to create a python script with a function "run()" return
the test result as a boolean. Your python scripts must be added to the
gtest framework with the SofaTest/Python\_test.h API to be executed
automatically Note that arguments can be given, so the same script can
be called with several parameters (accessible as argc/argv on the python
side). Have a look to SofaTest\_test for an example.

Investigating failures
----------------------

Regressions typically break a couple of tests, but not all of them. To
investigate, you generally want to run these tests only. Moreover, you
typically need to modify these, by adding some debug prints or changing
parameters. To **avoid damaging the test suite**, it is a good idea to
clone it and work on the cloned version. Assuming that you are
investigating test failures in SomePlugin/SomePlugin\_test, you can
apply the following steps:

1.  copy SomePlugin/SomePlugin\_test to SomePlugin/SomePluginTMP\_test
    or any other name ending up with \_test.
2.  move to this directory and edit CMakeLists.txt to remove all the
    test files you do not need
3.  update you Sofa project/solution by running cmake as you usually do;
    the new test directory will automatically be included in your
    project/solution if its name ends up with \_test
4.  modify the test as needed, and fix the problems
5.  update the original tests if necessary
6.  check that the original tests are successful

Feel free to add new tests to the original test suite, but think twice
before modifying an existing test: this might destroy its ability to
detect other problems.
