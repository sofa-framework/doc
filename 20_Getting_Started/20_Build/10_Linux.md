Prerequisites for Linux
=======================


Before building SOFA from source, make sure your configuration meets the
following requirements.



#### Compiler meta-package

To get the meta-package required to compile SOFA, first execute:

```bash
sudo apt-get install cmake build-essential
```


#### CMake: Makefile generator

SOFA requires at least CMake 2.8.8. To get CMake, execute the usual
command:
```bash
sudo apt-get install cmake cmake-qt-gui cmake-curses-gui
```

In case your configuration is Ubuntu 12.04 (or similar), the associated
repositories only provide CMake 2.8.7. Fortunately, a more recent
version of CMake is available in some PPAs, such as ppa:kalakris/cmake,
ppa:leppa/backports or ppa:ubuntu-sdk-team/ppa:

```bash
sudo add-apt-repository ppa:kalakris/cmake
sudo apt-get update
sudo apt-get install cmake cmake-qt-gui cmake-curses-gui
```


#### Ccache: Speed-up your compilation

If you work on Linux, we advise you to use *ccache*. It is by no means
mandatory, but it will dramatically improve the compilation time if you
make changes to SOFA. As explained on the
[ccache](http://ccache.samba.org/ "http://ccache.samba.org/"){.external
.text} website:

> "ccache is a compiler cache. It speeds up recompilation by caching
> previous compilations and detecting when the same compilation is being
> done again."

To get ccache, execute the usual command:

```bash
sudo apt-get install ccache
```


#### Required dependencies

Finally, SOFA requires some libraries:

-   Qt5 libraries. The development package of Qt4 is needed:

    ```bash
    sudo apt-get install qtbase5-dev libqt5opengl5-dev
    ```

-   Boost. The development package of boost is needed:

    ```bash
    sudo apt-get install libboost-all-dev
    ```

-   Additional libraries: libPNG, libZ and libGlew are needed.

    ```bash
    sudo apt-get install libpng-dev zlib1g-dev libglew-dev
    ```

Some plugins depend on libraries that are available in the repositories.
You probably don't need them all, but you might find it convenient to
install them all and not worry about it later:

```bash
[optional] sudo apt-get install python2.7-dev libxml2-dev libcgal-dev libblas-dev liblapack-dev libsuitesparse-dev libassimp-dev freeglut3-dev
```


Building on Linux
=================


#### Setting up your source and build directories

To set up clean repositories, we propose to arrange the SOFA directories
as follows:

-   sofa/
    -   v15.12/
        -   src/
        -   build/
    -   master
        -   src/
        -   build/

First, download the sources from Git repository:

Get the current **stable** version on the v15.12 branch:
``` {.bash .stable}
git clone -b v16.08 https://github.com/sofa-framework/sofa.git sofa/v16.08/src/
```

Or get the development **unstable** version on the master branch:
``` {.bash .unstable}
git clone -b master https://github.com/sofa-framework/sofa.git sofa/master/src/
```

To compile the project, open a terminal, go to your sofa/ directory and
type the following command to run CMake:

```bash
cd v15.12
mkdir build/
cd build/
cmake-gui ../src/
```

If you are not using the same file structure as the one described above,
from your own build directory type instead:

```bash
cmake-gui PATH-TO-THE-SOURCE
```

You need to run *Configure* twice, since SOFA requires two passes to
manage the module dependencies. You can then customize your version of
SOFA, acticate or deactivate plugins and functionalities. By default,
gcc is used but Clang can be prefered for a faster compilation (see the
paragraph below).


#### Compile in the terminal

To compile in the terminal, type in the build/ directory:

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
bin/runSofad (Debug)
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
argument to Make. Ubuntu 14.04: default qtcreator cmake plugin is
bugged, but you can easily install qtcreator 3.1.1 from this
non-official repository
[\[1\]](https://launchpad.net/~alexey-ivanov/+archive/qtcreator "https://launchpad.net/~alexey-ivanov/+archive/qtcreator"){.external
.autonumber} (Warning, it is using qt4 rather than qt5).


#### Clang

Clang is a new alternative to gcc. It compiles approximately two times
faster !

-   Ubuntu 12.04: Installing
    [clang](http://llvm.org/apt/ "http://llvm.org/apt/"){.external
    .autonumber}. Note that openmp requires a [specific
    installation](http://clang-omp.github.io/ "http://clang-omp.github.io"){.external
    .autonumber}.
-   Ubuntu 14.04: clang 3.4 & 3.5 are available in the
    default repositories.

Building cmake for SOFA using clang:

```bash
CC="clang -Qunused-arguments -fcolor-diagnostics" CXX="clang++ -Qunused-arguments -fcolor-diagnostics" cmake -DCMAKE_BUILD_TYPE=Release -G "CodeBlocks - Unix Makefiles" -H/path/to/src/Sofa -B/path/to/build/dir
```

***WARNING***: clang does not compile CUDA host code, select gcc for it
(i.e. set CUDA\_HOST\_COMPILER=/usr/bin/gcc)
