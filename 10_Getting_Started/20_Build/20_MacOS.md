**It is STRONGLY advised to read through this entire doc page before getting started.**

## Preconfigured Docker image

Unfortunately, no Docker image has been created yet for MacOS.  
This may come in a near future, to be continued...

----------------------------

# Build tools

## Compiler

SOFA requires a [C++17 compatible compiler](https://en.cppreference.com/w/cpp/compiler_support#C.2B.2B17_features).  
On MacOS, we officially support **MacOS >= 10.13.2 (High Sierra)** and **AppleClang >= 9.1.0**.  

Check your MacOS version with `system_profiler SPSoftwareDataType`  
Check your AppleClang version with `clang --version`

If your MacOS version is too low, update your Mac from the App Store.

If your AppleClang version is too low:

1. Download and install the highest possible Xcode compatible with your MacOS.  
   Compatibility list (taken from [Wikipedia](https://en.wikipedia.org/wiki/Xcode#Xcode_7.0_-_12.x_%28since_Free_On-Device_Development%29)):  
   ```
   MacOS >= 10.15.2 : Xcode 11.4   (with AppleClang 11.0.3, based on clang 9)
   MacOS >= 10.14.4 : Xcode 11.3.1 (with AppleClang 11.0.0, based on clang 8)
   MacOS >= 10.14.3 : Xcode 10.3   (with AppleClang 10.0.1, based on clang 7)
   MacOS >= 10.13.6 : Xcode 10.1   (with AppleClang 10.0.0, based on clang 6)
   MacOS >= 10.13.2 : Xcode 9.4.1  (with AppleClang 9.1.0,  based on clang 5)
   ```  
   To download any version, go to https://developer.apple.com/download/more/ and search "Xcode".

2. Open Xcode to automatically finalize installation

3. In Xcode, navigate to "Xcode > Preferences > Locations" and set Command Line Tools to your Xcode version

4. Verify Command Line Tools path: `xcode-select -p`  
   If it is not pointing to your Xcode, change it: `xcode-select --switch /Applications/Xcode.app`

5. Reboot


## CMake: Makefile generator

SOFA requires at least **CMake 3.12**.  
We recommend to install CMake using [the latest official installer](https://github.com/Kitware/CMake/releases/latest).


## [optional] Ninja: build system

Ninja is an alternative to Make. It has a better handling of incremental builds.

``` {.bash .optional}
brew install ninja
```


## [optional] CCache: caching system

We advise you to use [ccache](https://ccache.dev/). It is by no means
mandatory, but it will dramatically improve the compilation time if you
make changes to SOFA.

``` {.bash .optional}
brew install ccache
```


# Dependencies

## Core (required)

SOFA requires some libraries:

-   **Qt** (>= 5.12.0) with **Charts** and **WebEngine**    
    We recommend to install Qt **in your user directory** with [the unified installer](http://download.qt.io/official_releases/online_installers).  
    Make sure to enable **Charts** and **WebEngine** components.  
    ![](https://www.sofa-framework.org/wp-content/uploads/2020/04/install_qt_macos.png)

-   **Boost** (>= 1.65.1)  
    ```bash
    brew install boost
    ```

-   **Additional libraries**: libPNG, libJPEG, libTIFF, Glew   
    ```bash
    brew install libpng libjpeg libtiff glew
    ```

-   SOFA v20.06 and newer also need **Eigen** (>= 3.2.10)  
    ```bash
    brew install eigen
    ```

## Plugins (optional)

SOFA **plugins** depend on libraries that are available in the official repositories.  
You probably don't need them all, but you might find it convenient to
install them all and not worry about it later.  
This list does not cover all available SOFA plugins, only the ones that are built by our continuous integration platform.

-  CGALPlugin  
   ``` {.bash .optional}
   brew install cgal
   ```
-  MeshSTEPLoader  
   ``` {.bash .optional}
   brew install opencascade
   ```
-  SofaAssimp  
   ``` {.bash .optional}
   brew install assimp
   ```    
-  SofaCUDA  
   ``` {.bash .optional}
   brew install homebrew/cask-drivers/nvidia-cuda
   ```
-  SofaPardisoSolver  
   ``` {.bash .optional}
   brew install lapack
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

1. Run CMake.app and set source folder and build folder.

2. Run **Configure**. A popup will ask you to specify the generator for the project.

   - If you installed [Ninja](#optional-ninja-build-system) (recommended), select "CodeBlocks - Ninja".
   - Otherwise, select "CodeBlocks - Unix Makefile".

3. Keep "Use default native compilers" and press "Done".

4. Fix eventual dependency errors by following CMake messages (see Troubleshooting section below). Do not worry about warnings.

5. (optional) Customize SOFA via CMake variables

   - choose the build type by setting CMAKE_BUILD_TYPE to "Release" or "RelWithDebInfo" (recommended) or "Debug"
   - activate or deactivate plugins: see PLUGIN_XXX variables
   - activate or deactivate functionalities: see SOFA_XXX variables
   
   Do not forget to **Configure** again to check if your changes are valid.

6. When you are ready, run **Generate**.


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
