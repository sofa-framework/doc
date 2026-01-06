**It is STRONGLY advised to read through this entire doc page before getting started.**

## Supported Linux version

SOFA policy is to support only the latest Ubuntu LTS.

----------------------------

# Build tools

## Compiler

SOFA requires a [C++17 compatible compiler](https://en.cppreference.com/w/cpp/compiler_support#C.2B.2B17_features).  
On Linux, we officially support **GCC >= 7** and **Clang >= 5**.  

First, install the standard compilation toolkit with this command:

```bash
sudo apt install build-essential software-properties-common
```
    
### GCC

To know which GCC versions are available for your distribution, run this command:
```bash
apt-cache search '^gcc-[0-9.]+$'
```

Then, install the latest one with the usual command (example with gcc-11):
```bash
sudo apt install gcc-11
```

### Clang
Clang is an **alternative to GCC**. It compiles approximately two times faster!  
We recommend to install **Clang 5 or newer**.

To know which Clang versions are available for your distribution, run this command:
```bash
apt-cache search '^clang-[0-9.]+$'
```

Then, install the latest one with the usual command (example with clang-12):
```bash
sudo apt install clang-12
```


## CMake: Makefile generator

CMake will be required to configure the SOFA project before compiling it. Note that SOFA requires at least **CMake 3.22**.
```bash
sudo apt install cmake cmake-gui
```

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

-  **tinyXML2**
    ```
    sudo apt install libtinyxml2-dev
    ```
   
-   **OpenGL**
    ```
    sudo apt install libopengl0
    ```

-   **Boost** (>= 1.65.1)  
    ```
    sudo apt install libboost-all-dev
    ```
    
-   **Python 3.12** + pip + numpy + scipy
    ```
    sudo apt install python3.12-dev python3.12-venv
    ```
    Python 3.12 now favor the use of venv. We highly recommend it too. To bootstrap it type `python3.12 -m venv sofa-venv` in the folder you want to keep this venv. We recommend creating it either in your home directory, in the folder containing both your sources and the build directory. Once created, you can activate it by calling `source /path/to/sofa-venv/bin/activate`. Now you can install all dependency through the following commands:
    ```
    python3.12 -m pip install --upgrade pip \
    && python3.12 -m pip install numpy scipy pybind11==2.12.0
    ```
    Now, each time you want to build or use SOFA, you first need to call `source /path/to/sofa-venv/bin/activate` to activate this virtual environment and get access to the dependencies. 

-   **Additional libraries**: libPNG, libJPEG, libTIFF, Glew, Zlib   
    ```
    sudo apt install libpng-dev libjpeg-dev libtiff-dev libglew-dev zlib1g-dev
    ```

-   **Eigen** (>= 3.2.10)  
    ```
    sudo apt install libeigen3-dev
    ```

## Graphical User Interfaces

-   The [SOFAGLFW](https://github.com/sofa-framework/SofaGLFW) project is based on both **GLFW** and **ImGui** libraries. It required the following dependencies to be installed:
   ``` {.bash .optional}
   sudo apt install xorg-dev libgtk-3-dev
   ```
-   The [Sofa.Qt](https://github.com/sofa-framework/Sofa.Qt) project relies on **Qt** (>= 5.12.0) with **Charts** and **WebEngine**.  
    We recommend to install Qt **in your user directory** with [the unified installer](http://download.qt.io/official_releases/online_installers).  
    Make sure to enable **Charts** and **WebEngine** components.  
    ![](https://www.sofa-framework.org/wp-content/uploads/2020/04/install_qt_linux.png)
    -   Qt Wayland:
    X11 is known as an old display protocol. Recently, some Linux distributions switched to a new display protocol/server named Wayland.
    If you are using Wayland, or to check whether you are using it:
        -   Run this command to check your protocol:
            ```bash
            echo $XDG_SESSION_TYPE
            ```
        -   If you are using Wayland, install the associated qtwayland running this command (here for Qt5):
            ```bash
            sudo apt install qtwayland5
            ```
            and set the environment variable `export QT_QPA_PLATFORM=wayland`


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
   The currently supported cuda version is 12.2
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


# Build SOFA


## Setup your source and build directories

To set up clean repositories, we recommend to arrange the SOFA directories
as follows:

```
sofa/
├── build/
│   ├── master/
│   └── v25.12/
└── src/
    └── < SOFA sources here >
```

**First**, checkout the sources from Git repository:

Get the current **stable** version on the v25.12 branch:
``` {.bash .stable}
git clone -b v25.12 https://github.com/sofa-framework/sofa.git sofa/src
```

**OR** get the development **unstable** version on the master branch:
``` {.bash .unstable}
git clone -b master https://github.com/sofa-framework/sofa.git sofa/src
```


## Generate a Makefile with CMake

0. Activate your venv `source /path/to/sofa-venv/bin/activate` and tell CMake to look there to find pybind11 `export CMAKE_PREFIX_PATH=/path/to/sofa-venv/lib/python3.12/site-packages`

1. Create build directories respecting the arrangement above.

2. Run CMake-GUI and set source folder and build folder.

3. Run **Configure**. A popup will ask you to specify the generator for the project.

   - If you installed [Ninja](#optional-ninja-build-system), select "Ninja".
   - Otherwise, select "Unix Makefile".

4. Choose "Specify native compilers" and press "Next"

5. Set the C compiler to `/usr/bin/gcc` **or** `/usr/bin/clang`  
   Set the C++ compiler to `/usr/bin/g++` **or** `/usr/bin/clang++`

6. Run **Configure**.

7. Fix eventual dependency errors by following CMake messages (see Troubleshoot section below). Do not worry about warnings.

8. (optional) Customize SOFA via CMake variables

   - choose the build type by setting CMAKE_BUILD_TYPE to "Release" or "RelWithDebInfo" (recommended) or "Debug"   
   - activate or deactivate plugins: see PLUGIN_XXX variables
   - activate or deactivate functionalities: see SOFA_XXX variables
   Do not forget to **Configure** again to check if your changes are valid.
   **_NOTE_**: here is an [exhaustive list of plugins](../activate-plugins/) that can be activated for an in-tree compilation.

9. When you are ready, run **Generate**.






## Compile

To compile, open a terminal in your build directory and run `make` or `ninja` depending on the generator you chose during CMake configuration.
If you chose "Unix Makefile" as generator, you can enable parallel compilation by specifying the number of parallel build you want by adding the `-j n` option with `n` being the number of desired parallel jobs. 
This is set automatically to the highest possible by `ninja`, but this can be modified in the same way as for `make`. 

Time for a coffee!



## Troubleshoot CMake errors

### Qt detection error
To solve Qt detection errors, click on **Add Entry** and add
`CMAKE_PREFIX_PATH` with path `/home/YOUR_USERNAME/Qt/QT_VERSION/COMPILER` matching your
Qt installation.  
Example: `CMAKE_PREFIX_PATH=/home/bob/Qt/5.15/gcc_64`.
Note that this is a list, in which you can provide multiple paths by separating them with a semicolon ';'.

Then, **Configure** again.

A further dev warning may appear:

    CMake Warning (dev) at YOUR_QT_PATH/lib/cmake/Qt5Core/Qt5CoreMacros.cmake:224 (configure_file):
    configure_file called with unknown argument(s):

    COPY_ONLY

    Call Stack (most recent call first):
    applications/projects/Modeler/exec/CMakeLists.txt:14 (qt5_add_resources)

This is just a typo with Qt5CoreMacros.cmake file. It uses COPY\_ONLY
instead of COPYONLY. Simply edit your Qt5CoreMacros.cmake, replace
COPY\_ONLY with COPYONLY and **Configure** again.



## Compilation tutorial

See our page presenting [video tutorial for compilation on Linux](../../video-tutorials/how-to-compile-sofa/#linux).



# Run SOFA

## with the SOFA GUI
To run SOFA, locate and execute the application called `runSofa`. For more detailed information on how to use the application, you can refer to the [page dedicated to runsofa](../../../using-sofa/runsofa/). This documentation will provide you with further guidance on using SOFA effectively.


## within a Python environment

To use SOFA within a Python3 environment, the section "using Python3" details how to [set up your environment on various operating systems](https://sofapython3.readthedocs.io/en/latest/content/Installation.html#using-python3).




# Alternative build methods


## Preconfigured Docker image

We provide preconfigured Docker images based on Ubuntu or Fedora.  
These images contain all the tools and dependencies needed to build SOFA.  
Feel free to use them and to propose your own versions on Docker Hub!

Ubuntu image: [https://hub.docker.com/r/sofaframework/sofabuilder_ubuntu](https://hub.docker.com/r/sofaframework/sofabuilder_ubuntu)

Fedora image: [https://hub.docker.com/r/sofaframework/sofabuilder_fedora](https://hub.docker.com/r/sofaframework/sofabuilder_fedora)


## Nix package

[Nix](https://nix.dev/) is a package manager which stores all packages into a common place called the Nix store, usually located at /nix/store. Each package is stored in a unique subdirectory in the store, and each package has its own tree structure. A Nix package for SOFA is available and can be used as follows:

- Install [Nix](https://nix.dev/install-nix), you can run `sh <(curl -L https://nixos.org/nix/install) --daemon`, restart your terminal or check the installation using `nix --version`
- From the SOFA sources, build using the command `nix build --extra-experimental-features nix-command --extra-experimental-features flakes` (for master). Note that you can point towards any commit hash: `nix build github:sofa-framework/sofa/COMMIT_HASH_HERE`
- Command `nix develop` provides a shell with an environment containing all required dependencies to build the project in the usual CMake way
- Finally, starts SOFA `nix run --impure .#nixgl --extra-experimental-features nix-command --extra-experimental-features flakes`
