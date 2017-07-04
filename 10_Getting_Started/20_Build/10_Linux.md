Prerequisites for Linux
=======================


Before building SOFA from source, make sure your configuration meets the
following requirements.


#### Compiler

SOFA requires at least GCC 4.8 or Clang 3.4.  
Install the standard compilation toolkit (GCC + Make) with this command:

```bash
sudo apt-get install build-essential
```


#### CMake: Makefile generator

SOFA requires at least CMake 3.1. To get CMake, execute the usual
command:
```bash
sudo apt-get install cmake cmake-qt-gui
```

In case your configuration is **Ubuntu 14.04** (or similar), the associated
repositories only provide CMake 2.8.7. Fortunately, a more recent
version of CMake is available in some PPAs, such as ppa:george-edison55/cmake-3.x

```bash
sudo add-apt-repository ppa:george-edison55/cmake-3.x
sudo apt-get update
sudo apt-get install cmake cmake-qt-gui
```


#### [optional] Ninja (build system)

Ninja is an alternative to Make. It has a better handling of incremental builds.

``` {.bash .optional}
sudo apt-get install ninja-build
```

Do not forget to set CMake generator to **Codeblocks - Ninja** !


#### [optional] Clang (compiler)

Clang is an alternative to GCC. It compiles approximately **two times faster** !

``` {.bash .optional}
sudo apt-get install clang
```

To tell CMake you are using Clang use "Specify native compilers" option during first Configure/Generate, then set C compiler to `/usr/bin/clang` and C++ compiler to `/usr/bin/clang++`.

If you already configured or generated the project, simply set `CMAKE_C_COMPILER=/usr/bin/clang` and `CMAKE_CXX_COMPILER=/usr/bin/clang++` in CMake GUI.

If you prefer using the command line:

```
cmake -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ ../../src/
```

***WARNING***: Clang does not compile CUDA host code, prefer GCC for this (i.e. set CUDA\_HOST\_COMPILER=/usr/bin/gcc)


#### [optional] CCache (cache system)

If you work on Linux, we advise you to use *ccache*. It is by no means
mandatory, but it will dramatically improve the compilation time if you
make changes to SOFA. As explained on the
[ccache](http://ccache.samba.org/ "http://ccache.samba.org/"){.external
.text} website:

> "ccache is a compiler cache. It speeds up recompilation by caching
> previous compilations and detecting when the same compilation is being
> done again."

To get ccache, execute the usual command:

``` {.bash .optional}
sudo apt-get install ccache
```


#### Required dependencies

Finally, SOFA requires some libraries:

-   **Qt** (>= 4.8.3)

    We recommend to install Qt from [the unified installer](http://download.qt.io/official_releases/online_installers).  

-   **Boost** (>= 1.54.0)

    ```bash
    sudo apt-get install libboost-atomic-dev libboost-chrono-dev libboost-date-time-dev libboost-filesystem-dev libboost-locale-dev libboost-regex-dev libboost-system-dev libboost-thread-dev
    ```
    
-   **Python 2.7**

    ```bash
    sudo apt-get install python2.7-dev python-numpy python-scipy
    ```

-   Additional libraries: libPNG, Zlib, Glew and Glut

    ```bash
    sudo apt-get install libpng-dev zlib1g-dev libglew-dev freeglut3-dev
    ```

Some **plugins** depend on libraries that are available in the repositories.
You probably don't need them all, but you might find it convenient to
install them all and not worry about it later:

``` {.bash .optional}
sudo apt-get install libxml2-dev libcgal-dev libblas-dev liblapack-dev libsuitesparse-dev libassimp-dev
```


Building on Linux
=================


#### Setting up your source and build directories

To set up clean repositories, we propose to arrange the SOFA directories
as follows:

-   sofa/
    -   src/
    -   build/
        -   v17.06/
        -   master/

First, download the sources from Git repository:

Get the current **stable** version on the v17.06 branch:
``` {.bash .stable}
git clone -b v17.06 https://github.com/sofa-framework/sofa.git sofa/src/
```

**OR** get the development **unstable** version on the master branch:
``` {.bash .unstable}
git clone -b master https://github.com/sofa-framework/sofa.git sofa/src/
```

To launch CMake GUI on the project, open a terminal and type the following commands:

```bash
cd sofa
mkdir -p build/v17.06
cd build/v17.06
cmake-gui ../../src/
```


You need to run *Configure* **twice**, since SOFA requires two passes to
manage the module dependencies. You can then customize your version of
SOFA, activate or deactivate plugins and functionalities. For the 
compilation in debug mode, set the CMAKE_BUILD_TYPE to DEBUG. By default,
gcc is used but Clang can be prefered for a faster compilation (see the
paragraph below).
Once you are satisfied with the configuration you can run *Generate* and close cmake-gui.


#### Compile in the terminal

To compile in the terminal, type in the build/v17.06 directory:

```bash
make
```

You can use several cores to make the build faster. If, for example, you
want to use 4 cores, write:

```bash
make -j4
```

Time to have a coffee if you have an SSD, time to have lunch if you work
on a HDD! Once built, stay in the build folder and issue the following
commands to launch SOFA:

```bash
bin/runSofa (Release)
or
bin/runSofa_d (Debug)
```


#### Setting up QtCreator

The following instructions assume that you have set up two build
directories as explained in the previous section.

In QtCreator, open project CMakeLists.txt. Choose build-release as build
directory, then click on Finish. QtCreator is ready to compile, and the
build configuration is named "all", though it corresponds to a Release.

Click on the Project button in the left, then rename the configuration
from "all" to "Release".

Now click on add/Build to create a new configuration called "Debug".
Choose build-debug as build directory and run Cmake. If you set the -G
"CodeBlocks - Unix Makefiles" option in the cmake command line discussed
in the previous section, you do not even need to run CMake.

You can now switch between Debug and Release in QtCreator. The
compilation will be done using ccache (if installed). You can check this
by setting VERBOSE=1 as additional argument to Make in the Projects tab
on the left. Moreover, you probably want to run parallel compilations by
setting *-j10* for instance, for 10 parallel compilations, as additional
argument to Make.
