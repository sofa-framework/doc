Prerequisites for OS X
======================


Before building SOFA from source, make sure your configuration meets the
following requirements.


#### Compiler

SOFA requires at least GCC 4.8 or Clang 3.4. To make sure you have a correct version, execute the usual
commands:
```bash
gcc --version
clang --version
```


#### CMake: Makefile generator

SOFA requires at least CMake 3.1. To install CMake, use this
[Homebrew](http://brew.sh/ "Homebrew") command:

```bash
brew cask install cmake
```


#### [optional] Ninja (build system)

Ninja is an alternative to Make. It has a better handling of incremental builds.

``` {.bash .optional}
brew install ninja
```

Do not forget to set CMake generator to **Codeblocks - Ninja** !


#### About the compiler : LLVM vs. GCC

The default compiler on MacOS is now LLVM (ie. clang). SOFA is compatible with Clang but if you want to use gcc/g++ instead it is
necessary to tell cmake to use gcc/g++ instead of clang on MacOS.

You can do this by setting those environment variables: `CC=gcc` and
`CXX=g++`. These settings are stored in the cmake cache; once set, you
can re-use cmake or cmake-gui and the gcc settings won't be lost.


#### About the compiler on MacOS 10.8 Mountain Lion & MacOS 10.9 Maverick

If you are on MacOS 10.8 Mountain Lion, *gcc* is an alias of *clang*. To really
use gcc, use the following environnement varialbles:

```bash
CC="llvm-gcc" CXX="llvm-g++"
```


#### Required dependencies

To compile SOFA, you need to install several dependencies using Homebrew

-   **Qt** (>= 5.5.0)

    We recommend to install Qt from [the unified installer](http://download.qt.io/official_releases/online_installers).  

-   **Boost** (>= 1.54.0)

    ```bash
    brew install boost
    ```

-   Additional libraries: libPNG and Glew are needed

    ```bash
    brew install libpng
    brew install glew
    ```


Building on OS X
=================================================


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
git clone -b v17.06 https://github.com/sofa-framework/sofa.git sofa/src
```

**OR** get the development **unstable** version on the master branch:
``` {.bash .unstable}
git clone -b master https://github.com/sofa-framework/sofa.git sofa/src
```

To launch CMake GUI on the project, open a terminal and type the following commands:

```bash
cd sofa
mkdir -p build/v17.06
cd build/v17.06
cmake-gui ../../src/
```

**NOTE**:

-   if you installed Qt5 with brew, set `CMAKE_PREFIX_PATH=/usr/local/Cellar/qt5/5.X.Y` (replace 5.X.Y by your own Qt5 version) in CMake GUI to tell CMake were is your Qt installation  
or if you prefer running cmake by the command line:

    ```
    cmake -DCMAKE_PREFIX_PATH=/usr/local/Cellar/qt5/5.X.Y ../../src/
    ```
    
-   if you are not using the same file structure as the one described above, from your own build directory type instead:

    ```
    cmake PATH-TO-THE-SOURCE
    ```
    
-   you need to run  *Configure* **twice**, since SOFA requires two passes to manage the module dependencies. You can then customize your version of SOFA, acticate or deactivate plugins and functionalities. By default, gcc is used but Clang can be prefered for a faster compilation (see the paragraph below).


#### Compile in the terminal

To compile in the terminal, type in the v17.06/ directory:

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

