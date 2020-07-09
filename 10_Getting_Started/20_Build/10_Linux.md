**It is STRONGLY advised to read through this entire doc page before getting started.**

## Preconfigured Docker image

We provide preconfigured Docker images based on Ubuntu or CentOS.  
These images contain all the tools and dependencies needed to build SOFA.  
Feel free to use them and to propose your own versions on Docker Hub!

CentOS image: [https://hub.docker.com/r/sofaframework/sofabuilder_centos](https://hub.docker.com/r/sofaframework/sofabuilder_centos)

Ubuntu image: [https://hub.docker.com/r/sofaframework/sofabuilder_ubuntu](https://hub.docker.com/r/sofaframework/sofabuilder_ubuntu)

----------------------------

# Build tools

## Compiler

SOFA requires a [C++17 compatible compiler](https://en.cppreference.com/w/cpp/compiler_support#C.2B.2B17_features).  
On Linux, we officially support **GCC >= 7** and **Clang >= 5**.  

First, install the standard compilation toolkit with this command:

```bash
sudo apt install build-essential software-properties-common python-software-properties
```
    
### GCC

To know which GCC versions are available for your distribution, run this command:
```bash
apt-cache search '^gcc-[0-9.]+$'
```

Then, install the latest one with the usual command (example with gcc-7):
```bash
sudo apt install gcc-7
```

### Clang
Clang is an **alternative to GCC**. It compiles approximately two times faster !  
We recommend to install **Clang 5 or newer**.

To know which Clang versions are available for your distribution, run this command:
```bash
apt-cache search '^clang-[0-9.]+$'
```

Then, install the latest one with the usual command (example with clang-5.0):
```bash
sudo apt install clang-5.0
```


## CMake: Makefile generator

SOFA requires at least **CMake 3.12**.  
We recommend to install CMake using [the latest official installer](https://github.com/Kitware/CMake/releases/latest).


## [optional] Ninja: build system

Ninja is an alternative to Make. It has a better handling of incremental builds.

``` {.bash .optional}
sudo apt install ninja-build
```


## [optional] CCache: caching system

We advise you to use [ccache](https://ccache.dev/). It is by no means
mandatory, but it will dramatically improve the compilation time if you
make changes to SOFA.

``` {.bash .optional}
sudo apt install ccache
```


# Dependencies

## Core (required)

SOFA requires some libraries:

-   **Qt** (>= 5.12.0) with **Charts** and **WebEngine**  
    We recommend to install Qt **in your user directory** with [the unified installer](http://download.qt.io/official_releases/online_installers).  
    Make sure to enable **Charts** and **WebEngine** components.  
    ![](https://www.sofa-framework.org/wp-content/uploads/2020/04/install_qt_linux.png)

-   **Boost** (>= 1.65.1)  
    ```bash
    sudo apt install libboost-all-dev
    ```
    
-   **Python 2.7**  
    ```bash
    sudo apt install python2.7-dev python-numpy python-scipy
    ```

-   **Additional libraries**: libPNG, libJPEG, libTIFF, Glew, Zlib   
    ```bash
    sudo apt install libpng-dev libjpeg-dev libtiff-dev libglew-dev zlib1g-dev
    ```

-   SOFA v20.06 and newer also need **Eigen** (>= 3.2.10)  
    ```bash
    sudo apt install libeigen3-dev
    ```

## Plugins (optional)

SOFA **plugins** depend on libraries that are available in the official repositories.  
You probably don't need them all, but you might find it convenient to
install them all and not worry about it later.  
This list does not cover all available SOFA plugins, only the ones that are built by our continuous integration platform.

-  CGALPlugin  
   ``` {.bash .optional}
   sudo apt install libcgal-dev libcgal-qt5-dev
   ```
-  MeshSTEPLoader  
   ``` {.bash .optional}
   sudo apt install liboce-ocaf-dev
   ```
-  SofaAssimp  
   ``` {.bash .optional}
   sudo apt install libassimp-dev
   ```
-  SofaCUDA  
   ``` {.bash .optional}
   sudo apt install nvidia-cuda-toolkit
   ```
-  SofaHeadlessRecorder  
   ``` {.bash .optional}
   sudo apt install libavcodec-dev libavformat-dev libavutil-dev libswscale-dev
   ```
-  SofaPardisoSolver  
   ``` {.bash .optional}
   sudo apt install libblas-dev liblapack-dev
   ```


# Building SOFA


## Setup your source and build directories

To set up clean repositories, we recommend to arrange the SOFA directories
as follows:

```
sofa/
├── build/
│   ├── master/
│   └── v20.06/
└── src/
    └── < SOFA sources here >
```

**First**, checkout the sources from Git repository:

Get the current **stable** version on the v20.06 branch:
``` {.bash .stable}
git clone -b v20.06 https://github.com/sofa-framework/sofa.git sofa/src
```

**OR** get the development **unstable** version on the master branch:
``` {.bash .unstable}
git clone -b master https://github.com/sofa-framework/sofa.git sofa/src
```


## Generate a Makefile with CMake

0. Create build directories respecting the arrangement above.

1. Run CMake-GUI and set source folder and build folder.

2. Run **Configure**. A popup will ask you to specify the generator for the project.

   - If you installed [Ninja](#optional-ninja-build-system), select "CodeBlocks - Ninja".
   - Otherwise, select "CodeBlocks - Unix Makefile".

3. Choose "Specify native compilers" and press "Next"

4. Set the C compiler to `/usr/bin/gcc` **or** `/usr/bin/clang`  
   Set the C++ compiler to `/usr/bin/g++` **or** `/usr/bin/clang++`

5. Run **Configure**.

6. Fix eventual dependency errors by following CMake messages (see Troubleshooting section below). Do not worry about warnings.

7. (optional) Customize SOFA via CMake variables

   - choose the build type by setting CMAKE_BUILD_TYPE to "Release" or "RelWithDebInfo" (recommended) or "Debug"   
   - activate or deactivate plugins: see PLUGIN_XXX variables
   - activate or deactivate functionalities: see SOFA_XXX variables
   
   Do not forget to **Configure** again to check if your changes are valid.

8. When you are ready, run **Generate**.



## Compile

To compile, open a terminal in your build directory and run `make` or `ninja` depending on the generator you chose during CMake configuration.  
Do not forget the `-j` option to use all your CPU cores.

Time for a coffee!



## Troubleshooting CMake errors

### Qt detection error
To solve Qt detection errors, click on **Add Entry** and add
`CMAKE_PREFIX_PATH` with path `/home/YOUR_USERNAME/Qt/QT_VERSION/COMPILER` matching your
Qt architecture.  
Example: `CMAKE_PREFIX_PATH=/home/bob/Qt/5.7/gcc_64`  
**Configure** again.

A further dev warning may appear:

    CMake Warning (dev) at YOUR_QT_PATH/lib/cmake/Qt5Core/Qt5CoreMacros.cmake:224 (configure_file):
    configure_file called with unknown argument(s):

    COPY_ONLY

    Call Stack (most recent call first):
    applications/projects/Modeler/exec/CMakeLists.txt:14 (qt5_add_resources)

This is just a typo with Qt5CoreMacros.cmake file. It uses COPY\_ONLY
instead of COPYONLY. Simply edit your Qt5CoreMacros.cmake, replace
COPY\_ONLY with COPYONLY and **Configure** again.
