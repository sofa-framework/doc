SOFA policy is to support only the latest MacOS version.

# Installation with Pixi

You can download and build SOFA in only three steps without any environment installation.

## Prerequisites

- [Install Git](https://git-scm.com/install/mac)
- [Install Pixi](https://pixi.prefix.dev/latest/installation/)


## Installation steps

- Clone SOFA : `git clone https://github.com/sofa-framework/sofa` :inbox_tray: 
- Trigger the build : run `pixi run -e supported-plugins build` in the sofa source folder :desktop_computer: 
- Launch SOFA : run `pixi run -e supported-plugins runSofa` :rocket: 

⚠️ A known issue under macOS has been hotfixed in the pixi build using a patch. _You don't need to do anything while using pixi, it is applied for you_. The issue appeared through the use of Python from runSofa with SofaPython3 and caused a segmentation fault due to symbol duplication (the Python package from Conda Forge statically linked with libpython, conflicting with runSofa’s own linking). The patch (proposed in PR [#394](https://github.com/sofa-framework/SofaPython3/pull/394)) is currently used in our Conda packages.


# Manual installation (for developpers)

<details>

<summary>This installation method is advised for developers. It is STRONGLY advised to read through this entire doc page before getting started.</summary>
## Build tools

## Build tools

### Compiler

SOFA requires a [C++17 compatible compiler](https://en.cppreference.com/w/cpp/compiler_support#C.2B.2B17_features).  
On MacOS, we officially support **MacOS >= 10.13.2 (High Sierra)** and **AppleClang >= 9.1.0**.  

Check your MacOS version with `system_profiler SPSoftwareDataType`  
Check your AppleClang version with `clang --version`

If your MacOS version is too low, update your Mac from the App Store.

If your AppleClang version is too low:

1. Download and install the highest possible Xcode compatible with your MacOS.  
   Compatibility list (taken from [Wikipedia](https://en.wikipedia.org/wiki/Xcode#Version_comparison_table)):  
   ```   
   MacOS >= 11.3    : Xcode 13.2.1 (with AppleClang 13.0.0)
   MacOS >= 11.0    : Xcode 12.5.1 (with AppleClang 12.0.5)
   MacOS >= 10.15.4 : Xcode 12.4   (with AppleClang 12.0.0)   
   MacOS >= 10.15.2 : Xcode 11.7   (with AppleClang 11.0.3)
   MacOS >= 10.14.4 : Xcode 11.3.1 (with AppleClang 11.0.0)
   MacOS >= 10.14.3 : Xcode 10.3   (with AppleClang 10.0.1)
   MacOS >= 10.13.6 : Xcode 10.1   (with AppleClang 10.0.0)
   MacOS >= 10.13.2 : Xcode 9.4.1  (with AppleClang  9.1.0)
   ```  
   To download any version, go to https://developer.apple.com/download/more/ and search for "Xcode".

2. Open Xcode to automatically finalize installation

3. In Xcode, navigate to "Xcode > Preferences > Locations" and set Command Line Tools to your Xcode version

4. Verify Command Line Tools path: `xcode-select -p`  
   If it is not pointing to your Xcode, change it: `xcode-select --switch /Applications/Xcode.app`

5. Reboot


### CMake: Makefile generator

SOFA requires at least **CMake 3.22**.

``` {.bash}
brew install --cask cmake
```


### [optional] Ninja: build system

Ninja is an alternative to Make. It has a better handling of incremental builds.

``` {.bash .optional}
brew install ninja
```


### [optional] CCache: caching system

We advise you to use [ccache](https://ccache.dev/). It is by no means
mandatory, but it will dramatically improve the compilation time if you
make changes to SOFA.

``` {.bash .optional}
brew install ccache
```


## Dependencies

### Core (required)

SOFA requires some libraries:
-  **tinyXML2**
    ```bash
    brew install tinyxml2
    ```

-   **Boost** (>= 1.65.1)  
    ```bash
    brew install boost
    ```

-   **Python 3.12** + pip + numpy + scipy
    ```
    brew install python@3.12
    brew link --force python@3.10
    ```
    Python 3.12 now favor the use of venv. We highly recommend it too. To bootstrap it type `python3.12 -m venv sofa-venv` in the folder you want to keep this venv. We recommend creating it either in your home directory, in the folder containing both your sources and the build directory. Once created, you can activate it by calling `source /path/to/sofa-venv/bin/activate`. Now you can install all dependency through the following commands:
    ```
    python3.12 -m pip install --upgrade pip \
    && python3.12 -m pip install numpy scipy pybind11==2.12.0
    ```
    Now, each time you want to build or use SOFA, you first need to call `source /path/to/sofa-venv/bin/activate` to activate this virtual environment and get access to the dependencies. 

   
    
-   **Additional libraries**: libPNG, libJPEG, libTIFF, Glew   
    ```bash
    brew install libpng libjpeg libtiff glew
    ```

-   **Eigen** (>= 3.2.10)  
    ```bash
    brew install eigen
    ```


### Plugins (optional)

SOFA **plugins** depend on libraries that are available in the official repositories.  
You probably don't need them all, but you might find it convenient to
install them all and not worry about it later.  
This list does not cover all available SOFA plugins, only the ones that are built by our continuous integration platform.

-  CGALPlugin  
   ``` {.bash .optional}
   brew install cgal
   ```
-  SofaCUDA  
   ``` {.bash .optional}
   brew install homebrew/cask-drivers/nvidia-cuda
   ```


## Build SOFA


### Setup your source and build directories

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


### Generate a Makefile with CMake

0. Activate your venv `source /path/to/sofa-venv/bin/activate` and tell CMake to look there to find pybind11 `export CMAKE_PREFIX_PATH=/path/to/sofa-venv/lib/python3.12/site-packages`

1. Create build directories respecting the arrangement above.

2. Run CMake.app and set source folder and build folder.

3. Run **Configure**. A popup will ask you to specify the generator for the project.

   - If you installed [Ninja](#optional-ninja-build-system) (recommended), select "CodeBlocks - Ninja".
   - Otherwise, select "CodeBlocks - Unix Makefile".

4. Keep "Use default native compilers" and press "Done".

5. Fix eventual dependency errors by following CMake messages (see Troubleshoot section below). Do not worry about warnings.

6. Customize SOFA via CMake variables

   - choose the build type by setting CMAKE_BUILD_TYPE to "Release" or "RelWithDebInfo" (recommended) or "Debug"
   - if your Mac has a M1 processor: set CMAKE_OSX_ARCHITECTURES to "arm64"
   - activate or deactivate plugins: see PLUGIN_XXX variables
   - activate or deactivate functionalities: see SOFA_XXX variables
   Do not forget to **Configure** again to check if your changes are valid.
   **_NOTE_**: here is an [exhaustive list of plugins](../activate-plugins/) that can be activated for an in-tree compilation.

7. When you are ready, run **Generate**.


### Compile

To compile, open a terminal in your build directory and run `make` or `ninja` depending on the generator you chose during CMake configuration.  
Do not forget the `-j` option to use all your CPU cores.

Time for a coffee!

</details>



# Run SOFA

## with the SOFA GUI
To run SOFA, locate and execute the application called `runSofa`. For more detailed information on how to use the application, you can refer to the [page dedicated to runsofa](../../../using-sofa/runsofa/). This documentation will provide you with further guidance on using SOFA effectively.


## within a Python environment

To use SOFA within a Python3 environment, the section "using Python3" details how to [set up your environment on various operating systems](https://sofapython3.readthedocs.io/en/latest/content/Installation.html#using-python3).


