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
-D flag. For example, if you know that the **PLUGIN\_SOFAPYTHON**
option enables the compilation of the SofaPython plugin, you can enable
it like so:

```
cmake -DPLUGIN_SOFAPYTHON=ON <build-directory>
```


Configuration options
---------------------

### Good to know

CMake option fields can be either a boolean, a file path,
a directory path or a basic string. For instance, you can find in SOFA:

-   The **PLUGIN\_\*** options correspond to the directories in
    applications/plugins/
-   The **APPLICATION\_\*** options correspond to the directories
    in applications/projects/
-   The **TUTORIAL\_\*** options correspond to the directories in
    applications/tutorials/

For example, the SofaPython plugin (applications/plugins/SofaPython) is
enabled by the option PLUGIN\_SOFAPYTHON, and the runSofa
(applications/projects/runSofa) is enabled by the option
APPLICATION\_RUNSOFA.


### SOFA CMake options

-   **CMAKE\_BUILD\_TYPE** : the typical values for that field are **Release** and **Debug** (even if
there are other options like **ReleaseDebInfo**, there are not really
used by SOFA internal developers and thus, not really tested). Like the
value is indicating, **Release** value indicates to compile in
**Release** mode, with optimizations for speed, size of binaries.
**Debug** value makes it compile with the debugging symbol activated and
no code optimization.


- **SOFA\_EXTERNAL\_DIRECTORIES**: path to external directories, this can be especially useful
to build external plugins with SOFA. For more informations, please read the documentation
about [Building a plugin](https://www.sofa-framework.org/community/doc/using-sofa/build-a-plugin "Building a plugin").


- **SOFA_BUILD\_TUTORIALS** : this options activates the build of
all tutorials located in *applications/tutorials*.


- **SOFA_BUILD\_TESTS** : this option activates unit tests for SOFA.
For more informations, please go to the [Tests
page](https://www.sofa-framework.org/community/doc/writing-tests "Writing Tests").


- **SOFA\_FLOATING\_POINT\_TYPE** : this option determines the type(s) (float, double or both)
used almost everywhere in SOFA when a floating point type is explicitly needed:
the **SReal** type. This option also defines which "versions" of each templated
component will be compiled (float, double or both instantiations). Note that using double
will significantly reduce compilation time, but then you will only be able to simulate
scenes that contain exclusively components using template parameters
based on double (Vec3d, Rigid3d, ...). More technically, this will respectively activate or
desactivate the macro **SOFA\_WITH\_DOUBLE** and **SOFA\_WITH\_FLOAT** in the code.


- **SOFA\_DUMP\_VISITOR\_INFO** : enabling this option allows to get more debugging informations at each
step of the simulations. For a more complete description and how to use
these informations, please go to the [Profiling
part](https://www.sofa-framework.org/community/doc/profiling "Profiling").


- **SOFA\_NO\_EXTERN\_TEMPLATE** : this option (false by default) enables the use "extern template" in the
code of SOFA. It will be always be activated for DLLs on windows. On
some platforms, it can fix RTTI issues (typeid / dynamic\_cast), and it
significantly speeds up compilation and linking on every platform. More
information here: [Shared Libraries
Mechanism](https://www.sofa-framework.org/community/doc/shared-libraries-mechanism "Shared Libraries Mechanism").


- **SOFA\_NO\_OPENGL** : this option will remove any OpenGL-related code from SOFA. This is
especially useful for people who wants to use SOFA as a library with a
different rendering system (typically DirectX with Windows)


- **SOFA\_NO\_UPDATE\_BBOX** : this optimization flag desactives the computation of the bounding box at
every timestep of the simulation.


- **SOFA\_OPENMP (*advanced*)** : this flag will allow to use OpenMP for specific computations in existing
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


- **SOFA\_USE\_MASK** : this activates an optimization done to
run simulation involving masks (a subpart of an object). However, this features is known
as sensitive when used with constraint algorithms. Set false by default.


- **SOFA\_WITH\_EXPERIMENTAL\_FEATURES** : activates some experimental work in progress.
No garantee on code quality or compilation is given.
However, this gives early-access to new functionalities in SOFA.