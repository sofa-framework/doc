This section explains how to modify the build configuration of SOFA and
attempts to document the available options.

Using CMake
-----------

CMake is a meta build system, that generates files for the build system
used in your tool chain (e.g. Unix Makefiles, or a Visual Studio
solution). Once you have created your build directory for SOFA,
modifying build options goes like this:

-   you modify options using cmake tools (either cmake-gui or ccmake,
    see below)
-   CMake runs the project's configuration scripts with the current
    options (a.k.a. "*Configure*" in CMake tools)
-   then CMake effectively generates the build system files (a.k.a.
    "*Generate*" in CMake tools)

### Interactive configuration

CMake comes with both a GUI tool (**cmake-gui**) and a cursed based tool
(**ccmake**) to modify the build options interactively. You can invoke
them from the command line like so:

```
 cmake-gui <build-directory>
```

or

```
 ccmake <build-directory>
```

And on Windows, simply launch **CMake GUI**, and set the build directory
field to the correct path if necessary. Using one of those tool, you can
edit the options you want to change, and run "*Configure*" to run the
configuration scripts. Note that the scripts are written to
automatically enable any required dependencies when you change an
option. If this happens, you will be warned at the end of the
configuration step that you must run "*Configure*" again. Likewise, if
any errors occurs during the configuration step, you have to run
"*Configure*" again after you fix them. The general rule with the CMake
configure part is that you have to hit "*Configure*" until no
red-highlighted part is existing. Once you are satisfied with the
options, and the configuration step succeeded without errors, run
"*Generate*" to generate and write the build files to the build
directory. You can then proceed to compile SOFA with your regular build
tool. Tips:

-   If some options were modified or added during the configuration step
    (by the scripts), they are highlighted in cmake-gui;
-   The list of options is pretty long; it may be easier to find what
    you are looking for if you check the "Grouped" checkbox;
-   Cmake stores the options in a cache (**CMakeCache.txt)** for the
    next time you run any cmake tool. If you want to start over from the
    default configuration, or choose a new generator, select *File* &gt;
    *Delete Cache*.

\[caption id="attachment\_1054" align="aligncenter"
width="543"\][![Cmake-gui typical
view](https://www.sofa-framework.org/wp-content/uploads/2014/11/CmakeExampleWindowMac1.png){.size-full
.wp-image-1054 width="543"
height="500"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/CmakeExampleWindowMac1.png)
cmake-gui typical view (on Mac OS X Yosemite)\[/caption\]

### Command-line configuration

When called directly, cmake does both the configuration and the
generation steps. If you wish to modify the configuration from the
command line (e.g. in a script), you can pass options to cmake with the
-D flag. For example, if you know that the **SOFA-PLUGIN\_SOFAPYTHON**
option enables the compilation of the SofaPython plugin, you can enable
it like so:

```
cmake -DSOFA-PLUGIN_SOFAPYTHON=ON <build-directory>
```

Configuration options
---------------------

Good to know: CMake option fields can be either a boolean, a file path,
a directory path or a basic string. Most configuration options of SOFA
are prefixed by "**SOFA**". More precisely, they follow the pattern
"**SOFA- &lt;category&gt;"** where *category* is usually
**APPLICATION**, **CUDA**, **EXTERNAL**, **LIB**, **LIB\_COMPONENT**,
**MISC**, **PLUGIN** or **TUTORIAL**. The options of type LIB,
LIB\_COMPONENT, APPLICATION, PLUGIN, and TUTORIAL type correspond to the
different parts of SOFA, that can be compiled or not. More options are
documented further down this page.

-   The **SOFA-LIB\_\*** options correspond to the directories in
    framework/sofa/
-   The **SOFA-LIB\_COMPONENT\_\*** options correspond to the
    directories in modules/
-   The **SOFA-PLUGIN\_\*** options correspond to the directories in
    applications/plugins/
-   The **SOFA-APPLICATION\_\*** options correspond to the directories
    in applications/projects/
-   The **SOFA-TUTORIAL\_\*** options correspond to the directories in
    applications/tutorials/

For example, the SofaPython plugin (applications/plugins/SofaPython) is
enabled by the option SOFA-PLUGIN\_SOFAPYTHON, and the Modeler
(applications/projects/Modeler) is enabled by the option
SOFA-APPLICATION\_MODELER.

### Standard CMake options

-   **CMAKE\_BUILD\_TYPE**

The typical values for that field are **Release** and **Debug** (even if
there are other options like **ReleaseDebInfo**, there are not really
used by SOFA internal developers and thus, not really tested). Like the
value is indicating, **Release** value indicates to compile in
**Release** mode, with optimizations for speed, size of binaries...
**Debug** value makes it compile with the debugging symbol activated and
no code optimization.

### SOFA-EXTERNAL\_\*

When a user wants to activate a new functionality, it can be enabled by
selecting the respective option and setting the path for that external
library (if it is not already included in the external/ directory of
SOFA). Example with CGoGN library. We want to the experimental topology
system based on [CGoGN](http://cgogn.unistra.fr/ "CGoGN"). Thus we check
in cmake-gui the field SOFA-EXTERNAL\_CGOGN (setting the boolean on
true). We can see that, by default, the SOFA-EXTERNAL\_CGOGN\_PATH is
pointing to the already shipped CGoGN directory in SOFA. You have the
ability to choose your own CGoGN installation if desired.

### SOFA-CUDA\_\*

See [Cuda documentation
page](https://www.sofa-framework.org/community/doc/gpu-computing-using-cuda "GPU computing using CUDA").

### SOFA-MISC\_\*

-   **SOFA-MISC\_TESTS**

This option activates unit tests for SOFA. For much more informations,
please go to the [Tests
page](https://www.sofa-framework.org/community/doc/writing-tests "Writing Tests").

-   **SOFA-MISC\_USE\_DOUBLE** and **SOFA-MISC\_USE\_FLOAT**

Those options determine two different things:

-   Firstly, they determine the type used almost everywhere in SOFA when
    a floating point type is explicitly needed, the **SReal** type:
    -   SReal is defined to be float if **SOFA-MISC\_USE\_FLOAT** is
        enabled, and double otherwise.
-   Secondly, they determine which "versions" of each templated
    component will be compiled:
    -   If **SOFA-MISC\_USE\_FLOAT** is enabled, templated components
        will be compiled only with parameters based on the float type
    -   If **SOFA-MISC\_USE\_DOUBLE** is enabled, templated components
        will be compiled only with parameters based on the double type
    -   If both are disabled (default), all the possible instantiations
        of templated components will be compiled.
    -   Finally, you must not enable both options at the same time.

Ultimately, enabling, say, **SOFA-MISC\_USE\_DOUBLE** will significantly
reduce compilation time, but then you will only be able to simulate
scenes that contain exclusively components using template parameters
based on double (Vec3d, Rigid3d, ...). More technically, if
**SOFA-MISC\_USE\_DOUBLE** is enabled, then the macro **SOFA\_DOUBLE**
will be defined, and similarly, **SOFA-MISC\_USE\_FLOAT** will cause
**SOFA\_FLOAT** to be defined. The **SOFA\_DOUBLE** and **SOFA\_FLOAT**
macros are used in the code to control the explicit instantiations of
class templates that define SOFA components.

-   **SOFA-MISC\_DOXYGEN**

Enable this option to create targets for source code documentation
generation with doxygen. (Obviously, this requires doxygen to be
installed.) This will create a doc-Foo target for each project Foo that
is enabled (a plugin, a module, an application...), as well as a doc
target to build all the documentation targets at once. With this option
enabled :

-   build the doc target to generate all the documentation. You can then
    open the main page doc/SOFA/index.html, that links to all
    the documentations.
-   build the doc-Foo target to generate only the documentation for the
    project Foo. This will run doxygen on the source directory of the
    project, after generating the documentation of the other projects
    Foo depends on. The documentation of Foo will be in doc/Foo/ (main
    page: doc/Foo/index.html).
-   build the doc-Foo/fast target to re-generate only the documentation
    of Foo, without generating again the documentation for
    its dependencies.

Note for Windows: due to the current organisation of files in modules/,
the cmake scripts use questionable workarounds to make the corresponding
documentation targets, which don't work under Windows. So modules/ won't
be documented when building the doc under Windows.

-   **SOFA-MISC\_DOXYGEN\_COMPONENT\_LIST**

Enable this option in order to add a page to the doxygen documentation
that lists all the components available in modules (like this page), and
links to their individual documentation page. This particular page is
generated using SOFA. Thus, if you enable this option, you will have to
compile SOFA in order to generate the documentation.

-   **SOFA-MISC\_CMAKE\_VERBOSE**

Make the CMake scripts output much more information during the
configuration step.

-   **SOFA-MISC\_DEV**

This option activates part of code flagged as "still in development"
code aka beta version. This code is very unstable and thus no support
can be provided.

-   **SOFA-MISC\_DUMP\_VISITOR\_INFO**

Enabling this option allows to get more debugging informations at each
step of the simulations. For a more complete description and how to use
these informations, please go to the [Profiling
part](https://www.sofa-framework.org/community/doc/profiling "Profiling").

-   **SOFA-MISC\_EXTERN\_TEMPLATE**

This option (true by default) enables the use "extern template" in the
code of SOFA. It will be always be activated for DLLs on windows. On
some platforms, it can fix RTTI issues (typeid / dynamic\_cast), and it
significantly speeds up compilation and linking on every platform. More
information here: [Shared Libraries
Mechanism](https://www.sofa-framework.org/community/doc/shared-libraries-mechanism "Shared Libraries Mechanism").

-   **SOFA-MISC\_NO\_OPENGL**

This option will remove any OpenGL-related code from SOFA. This is
especially useful for people who wants to use SOFA as a library with a
different rendering system (typically DirectX with Windows)

-   **SOFA-MISC\_NO\_UPDATE\_BBOX**

This optimization flag desactives the computation of the bounding box at
every timestep of the simulation.

-   **SOFA-MISC\_OPENMP (*advanced*)**

This flag will allow to use OpenMP for specific computations in existing
code. A few components are multithreaded with openmp pragmas. Sometimes
hyperthreading gives strange results (slowing down the simulation). To
get rid of hyperthreaded cores you have to tell openmp to run the
application only on physical cores. When compiled with gcc, the
environment variable GOMP\_CPU\_AFFINITY allows the core selection,
where you can select physical cores only. (eg in bash: export
GOMP\_CPU\_AFFINITY="0-15"). The core indices can be obtained with the
"lstopo" command (sudo apt-get install hwloc) Do not forget to limit the
max number of cores with the OMP\_NUM\_THREADS environment variable
(export OMP\_NUM\_THREADS="16")

-   **SOFA-MISC\_SMP (*advanced*)**

This setting enables new components with support for SMP (Symmetric
Multi Processing), in order to have parallel computations (parallel
collision pipeline, ...)
