**It is STRONGLY advised to read through this entire doc page before getting started.**

----------------------------

# Build tools

## Compiler

SOFA requires a [C++17 compatible compiler](https://en.cppreference.com/w/cpp/compiler_support#C.2B.2B17_features).  
On Windows, we officially support **Microsoft Visual Studio >= 2017** (version 15.7).  
If you want to use **Visual Studio IDE**, install the complete Visual Studio solution.  
If you want to use **another IDE** (like QtCreator), install the Build Tools only.

|                       |                                            **Visual Studio 2017**                                            |                                            **Visual Studio 2019**                                            |                                            **Visual Studio 2022**                                            |
|-----------------------|:------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------:|
| **Build Tools only**  | [download](https://visualstudio.microsoft.com/fr/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15) | [download](https://visualstudio.microsoft.com/fr/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16) | [download](https://visualstudio.microsoft.com/fr/thank-you-downloading-visual-studio/?sku=BuildTools&rel=17) |
| **IDE + Build Tools** | [download](https://visualstudio.microsoft.com/fr/thank-you-downloading-visual-studio/?sku=Community&rel=15)  | [download](https://visualstudio.microsoft.com/fr/thank-you-downloading-visual-studio/?sku=Community&rel=16)  | [download](https://visualstudio.microsoft.com/fr/thank-you-downloading-visual-studio/?sku=Community&rel=17)  |


In the installer, you must enable:

1. In the main panel: the **C++ development toolkit**, called "C++ Build Tools" or "Desktop C++".
2. In the side panel: the **C++ ATL** and **C++ MFC** components.

![](https://www.sofa-framework.org/wp-content/uploads/2020/03/install_vs_ide.png)

## CMake: Makefile generator

SOFA requires at least **CMake 3.22.1**.  
Install CMake with [the latest official installer](https://github.com/Kitware/CMake/releases/latest).

**IMPORTANT**: check the option **"Add CMake to the system PATH for all users"** during the install process.

![](https://www.sofa-framework.org/wp-content/uploads/2019/03/install-cmake.png)


## [optional] Ninja: build system

We strongly advise you to use Ninja if you chose to install the Build Tools only (no IDE).

Ninja is an alternative to NMake. It has a better handling of incremental builds.  
You can download the latest release from [their GitHub repository](https://github.com/ninja-build/ninja/releases).

**IMPORTANT**: do not forget to **add ninja to your system PATH**.

# Dependencies

## Core (required)

SOFA requires some libraries:

-   **Boost** (>= 1.65.1)  
    Download and install the latest version compatible with your Visual Studio from [https://sourceforge.net/projects/boost/files/boost-binaries/](https://sourceforge.net/projects/boost/files/boost-binaries/).
    
    - **For Visual Studio 2022**: choose boost_X_X_X-msvc-14.3-64.exe
    - **For Visual Studio 2019**: choose boost_X_X_X-msvc-14.2-64.exe
    - **For Visual Studio 2017**: choose boost_X_X_X-msvc-14.1-64.exe
    
-   **Python** (= 3.10.x)  
    Download and install the latest [**Python 3.10 (amd64)**](https://www.python.org/ftp/python/3.10.10/python-3.10.10-amd64.exe).
    Then install the python dependencies. Run the following commands in cmd by replacing `path\to\Python310\ ` by the path where python was installed on your OS.
    ```
    path\to\Python310\python.exe -m pip install --upgrade pip
    path\to\Python310\python.exe -m pip install numpy scipy pybind11==2.9.1
    ```
    
-   **Additional libraries**: libPNG, libJPEG, libTIFF, Glew, Zlib, TinyXML2
    Download the [Windows dependency pack](https://www.sofa-framework.org/download/WinDepPack/VS-2017/latest).  
    You will need to unzip it directly in SOFA sources (later in this tutorial).

-   **Eigen** (>= 3.2.10)  
    Download and extract the [latest Eigen sources](https://gitlab.com/libeigen/eigen/-/releases).

## Graphical User Interfaces

-   The [Sofa.Qt](https://github.com/sofa-framework/Sofa.Qt) project relies on **Qt** (>= 5.12.0) with **Charts** and **WebEngine**.
    We recommend to install Qt **in your user directory** with [the unified installer](http://download.qt.io/official_releases/online_installers).  
    ![](https://github.com/sofa-framework/doc/blob/master/images/gettingstarted/install_qt_windows_1.png?raw=true")
    Make sure to enable **Charts** and **WebEngine** components.  
    ![](https://github.com/sofa-framework/doc/blob/master/images/gettingstarted/install_qt_windows_2.png?raw=true")


### [optional] PATH modification

You can add Boost and Qt to your PATH to ease their detection by CMake.  
**Boost**: add `your/Boost/path` and `your/Boost/path/libXX-msvc-XX`  
**Qt**: add `your/Qt/path/msvcXXXX_XX/bin` and `your/Qt/path/msvcXXXX_XX/lib`


# Building SOFA


## Setup your source and build directories

To set up clean repositories, we recommend to arrange the SOFA directories
as follows:

```
sofa/
├── build/
│   ├── master/
│   └── v25.06/
└── src/
    └── < SOFA sources here >
```

**First**, checkout the sources from Git repository:

Get the current **stable** version on the v25.06 branch:
``` {.bash .stable}
git clone -b v25.06 https://github.com/sofa-framework/sofa.git sofa/src
```

**OR** get the development **unstable** version on the master branch:
``` {.bash .unstable}
git clone -b master https://github.com/sofa-framework/sofa.git sofa/src
```

**Next**, unzip the **SOFA dependencies for Windows** (downloaded before) directly in the sources `sofa/src/`.

**Finally**, you should have something like this:

![](https://www.sofa-framework.org/wp-content/uploads/2015/11/sofa_files.png)


## Generate a VS project (.sln) or a Makefile with CMake

1. Create build directories respecting the arrangement above.

2. In Windows Start menu, search for `Native Tools Command Prompt` and run the one corresponding to your Windows architecture (x64 for 64-bit, x86 for 32-bit).  
![](https://www.sofa-framework.org/wp-content/uploads/2020/04/SearchCommandPrompt2.png)

3. In the command prompt, type `cmake-gui` and press Enter.  
   If you get the error `'cmake-gui' is not recognized as an internal or external command`, it means that your system PATH does not correctly include the path to cmake-gui. In this case, you need to provide the full path to your cmake-gui.

4. In CMake-GUI, set source folder and build folder.

5. Run **Configure**.
   
6. A popup will ask you to specify the generator for the project.

   - If you want use **Visual Studio IDE**, select "Visual Studio 15 2017 Win64" or "Visual Studio 16 2019 Win64" (or without the "Win64" if you are on Windows 32-bit).
   - If you want to use **another IDE like QtCreator**, select "CodeBlocks - Ninja" (recommended, needs [Ninja](#optional-ninja-build-system)) or "CodeBlocks - NMake".
   Keep "Use default native compilers" and press "Finish".

7. Fix eventual dependency errors by following CMake messages (see Troubleshooting section below). Do not worry about warnings.

   - e.g. define the `Eigen3_DIR` with the path where you installed Eigen

8. (optional) Customize SOFA via CMake variables

   - choose the build type by setting CMAKE_BUILD_TYPE to "Release" or "RelWithDebInfo" (recommended) or "Debug"
   - activate or deactivate plugins: see PLUGIN_XXX variables
   - activate or deactivate features: see SOFA_XXX variables
   Do not forget to **Configure** again to check if your changes are valid.
   **_NOTE_**: here is an [exhaustive list of plugins](../activate-plugins/) that can be activated for an in-tree compilation.

9. When you are ready, run **Generate**. In the build directory, this will create a Visual Studio project (.sln) or a Makefile depending on the generator you chose at step 4.


## Compile

To build SOFA in Visual Studio, simply **open the generated Sofa.sln**. Finally, **build the solution** using the Visual Studio interface as shown in the image below:

![](https://www.sofa-framework.org/wp-content/uploads/2019/03/build-visual.png)

If you chose another generator you will have to run the generator from the build directory.

Example with Ninja:

- In Windows Start menu, search for `Native Tools Command Prompt` and run the one corresponding to your Windows architecture (x64 for 64-bit, x86 for 32-bit).
- Go to the build directory with `cd`
- Run `ninja`

Time for a coffee!


## Troubleshooting CMake errors

### Qt detection error
To solve Qt detection errors, click on **Add Entry** and add
`CMAKE_PREFIX_PATH` with path to your Qt directory (navigate until msvcXXXX_XX directory).  
Example: `CMAKE_PREFIX_PATH=C:/dev/Qt/5.11.3/msvc2017_64`
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


## Setup script

To simplify the configuration of our continuous integration machines, we created a complete set of setup scripts.


These scripts install a lot of software directly in `C:\` without any prealable check.  
It is meant to be used on a **fresh Windows**. We use it on disposable virtual machines only.  

Setup script: [I am aware of the disclaimer above](https://github.com/sofa-framework/ci/blob/master/setup/)
**WARNING: USE AT YOUR OWN RISKS**

The two scripts `setup-windows_1.bat` and `setup-windows_2.bat` install the minimum set of requirements.



## Compilation tutorial

See our page presenting [video tutorial for compilation on Windows](../../video-tutorials/how-to-compile-sofa/#windows).
