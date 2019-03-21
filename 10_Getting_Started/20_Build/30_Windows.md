Prerequisites for Windows
=========================


## Compiler

You need to have Visual Studio 2015 or higher installed. We recommend Visual Studio 2015 (tested on [our Dashboard](http://www.sofa-framework.org/dash/)).

Visit [Visual Studio downloads page](https://www.visualstudio.com/fr-fr/downloads/download-visual-studio-vs.aspx).

**Note**: you can also get [Build Tools for VS2015](https://www.microsoft.com/en-us/download/details.aspx?id=48159) or [Build Tools for VS2017](https://www.visualstudio.com/fr/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15) to install MSVC without all the Visual Studio package.


## CMake: Makefile generator

You need to have CMake 3.1 or higher installed.  
The easiest way to do this is to get the installer from the [CMake download page](https://cmake.org/download/).


## [optional] Ninja: build system

Ninja is an alternative to NMake. It has a better handling of incremental builds.  
You can download the latest release from [their GitHub repository](https://github.com/ninja-build/ninja/releases).

To use Ninja, do not forget to set the CMake generator to "Codeblocks - Ninja" (as explained in [Generate a Makefile with CMake](#generate-a-makefile-with-cmake)).


## Required dependencies

Finally, SOFA requires some specific dependencies:

-   **Qt** (>= 5.5.0)  
    We recommend to install Qt from [the unified installer](http://download.qt.io/official_releases/online_installers).  

-   **Boost** (>= 1.54.0)  
    Find the latest official Boost installer for your Visual Studio version
    [here](https://sourceforge.net/projects/boost/files/boost-binaries/).
    Beware of the correspondance between Visual Studio and MSVC versions (VS-2015 == MSVC-14.0, VS-2017 == MSVC-14.1).

-   **Python 2.7**  
    Get Python 2.7.x (32 or 64 bit) on [python.org download page](https://www.python.org/downloads/windows/).

-   **Additional libraries**: libPNG, libJPEG, libTIFF, Zlib, Glew
    -   VS2015 users: download the [Windows dependency pack for VS2015](https://www.sofa-framework.org/download/WinDepPack/VS-2015/latest).
    -   VS2017 users: download the [Windows dependency pack for VS2017](https://www.sofa-framework.org/download/WinDepPack/VS-2017/latest).

    You will unzip them **in SOFA source directory** (e.g. sofa/src/) after cloning SOFA (see below).


## [optional] PATH modification

To complete the dependencies integration, you may add Boost and Qt to your PATH (it will ease their detection by CMake).  
**Boost**: add `your/Boost/path` and `your/Boost/path/libXX-msvc-XX`  
**Qt**: add `your/Qt/path/msvcXXXX_XX/bin` and `your/Qt/path/msvcXXXX_XX/lib`


Building on Windows
===================


## Setting up your source and build directories

To set up clean repositories, we propose to arrange the SOFA directories
as follows:

-   sofa/
    -   src/
    -   build/
        -   v18.12/
        -   master/

**First**, download the sources from Git repository:

Get the current **stable** version on the v18.12 branch:
``` {.bash .stable}
git clone -b v18.12 https://github.com/sofa-framework/sofa.git sofa/src/
```

**OR** get the development **unstable** version on the master branch:
``` {.bash .unstable}
git clone -b master https://github.com/sofa-framework/sofa.git sofa/src/
```

**Next**, unzip in your sources folder (sofa/src/) the **SOFA
dependencies for Windows** you downloaded before.

**Finally**, you should have something like this:

![sofa_files](https://www.sofa-framework.org/wp-content/uploads/2015/11/sofa_files.png)


## Generate a Makefile with CMake

If you didn't do it yet, create a build/ folder respecting directories
arrangement.

Open CMake-GUI and set source folder with **Browse Source** and build
folder with **Browse Build**.

Next, run **Configure**. A popup window will ask you to specify the
generator for the project. If you installed Ninja, select "Codeblocks - Ninja".
Otherwise, select your version of Visual Studio. If you have Visual Studio 2015 and a
64-bit system select "Visual Studio 14 2015 Win64".
Keep "Use default native compilers" selected, and press "Finish".

You need to **run Configure twice**, since SOFA requires two passes to
manage the module dependencies. You can then customize your version of
SOFA, activate or deactivate plugins and functionalities.

If you have some errors, make absolutely sure all of your dependencies and your
compilator are targeting the same architecture. For example, if you are not sure
that the compiler is correctly set, do not hesitate to select it manually in the
cmake-gui configuration screen instead of keeping the default ("Use default native
compilers").

When you are ready, press **Generate**. This will create your Visual
Studio solution or your makefiles if you chose another generator.

### Troubleshooting

#### Qt detection errors
To solve Qt detection errors, click on **Add Entry** and add
`CMAKE_PREFIX_PATH` with path `C:/Qt/X.X/msvcXXXX` matching your
Qt MSVC folder.  
Example: `CMAKE_PREFIX_PATH=C:/Qt/5.7/msvc2015_64`  
**Configure** again.

A further dev warning may appear:

    CMake Warning (dev) at YOUR_QT_MSVC_PATH/lib/cmake/Qt5Core/Qt5CoreMacros.cmake:224 (configure_file):
    configure_file called with unknown argument(s):

    COPY_ONLY

    Call Stack (most recent call first):
    applications/projects/Modeler/exec/CMakeLists.txt:14 (qt5_add_resources)

This is just a typo with Qt5CoreMacros.cmake file. It uses COPY\_ONLY
instead of COPYONLY. Simply edit your Qt5CoreMacros.cmake, replace
COPY\_ONLY with COPYONLY and **Configure** again.

#### Boost detection errors
To solve Boost detection errors, click on **Add Entry** and add
`BOOST_ROOT` with type **PATH** and value `C:/boost/boost_1_XX_X` matching your
Boost lib folder.  
Example: `BOOST_ROOT=C:/boost/boost_1_61_0`  
**Configure** again.


## Compile

If you chose a Visual Studio generator in CMake, building SOFA is just like any other
project building. Simply open the generated Sofa.sln and build the
solution.

If you chose another generator you will have to run the generator from the build directory.
Example with Ninja: go in the build dir and run `ninja`.

Time for a coffee!

