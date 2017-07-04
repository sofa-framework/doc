Prerequisites for Windows
=========================


#### Compiler

You need to have Visual Studio 2015 or higher installed. We recommend Visual Studio 2015 (tested on [our Dashboard](http://www.sofa-framework.org/dash/)).

Visit [Visual Studio downloads page](https://www.visualstudio.com/fr-fr/downloads/download-visual-studio-vs.aspx).

**Note**: you can also get [Build Tools for VS2015](https://www.microsoft.com/en-us/download/details.aspx?id=48159) or [Build Tools for VS2017](https://www.visualstudio.com/fr/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15) to install MSVC without all the Visual Studio package.


#### CMake: Makefile generator

You need to have CMake 3.1 or higher installed.
The easiest way to do this is to get the installer from the [CMake download page](https://cmake.org/download/).


#### Required dependencies

Finally, SOFA requires some specific dependencies:

-   **Qt** (>= 4.8.3)  
    We recommend to install Qt from [the unified installer](http://download.qt.io/official_releases/online_installers).  

-   **Boost** (>= 1.54.0)  
    Find the last official Boost installer for every Visual Studio version
    [here](https://sourceforge.net/projects/boost/files/boost-binaries/).
    Beware of the correspondance between Visual Studio and MSVC versions (VS-2015 == MSVC-14.0, VS-2017 == MSVC-14.1).

-   **Python 2.7**  
    Get Python 2.7.x (32 or 64 bit) on [python.org download page](https://www.python.org/downloads/windows/).

-   **External libraries**: libPNG, Zlib, Glew and Glut  
    -   VS2015 users: download the [Windows dependency pack for VS2015](https://www.sofa-framework.org/download/WinDepPack/VS-2015/latest).
    -   VS2017 users: download the [Windows dependency pack for VS2017](https://www.sofa-framework.org/download/WinDepPack/VS-2017/latest).

    You will unzip them in your sources folder (e.g. sofa/src/) after cloning SOFA (see below).


#### PATH

To complete the dependencies integration, you can add Boost and Qt to your PATH.  
**Boost**: add `your/boost/path/libXX-msvc-XX`  
**Qt**: add `your/Qt/path/msvcXXXX_XX/bin` and `your/Qt/path/msvcXXXX_XX/lib`


Building on Windows
===================


### Setting up your source and build directories

To set up clean repositories, we propose to arrange the SOFA directories
as follows:

-   sofa/
    -   src/
    -   build/
        -   v17.06/
        -   master/

**First**, download the sources from Git repository:

Get the current **stable** version on the v17.06 branch:
```bash
git clone -b v17.06 https://github.com/sofa-framework/sofa.git sofa/src/
```

Or get the development **unstable** version on the master branch:
```bash
git clone -b master https://github.com/sofa-framework/sofa.git sofa/src/
```

**Next**, unzip in your sources folder (sofa/src/) the **SOFA
dependencies for Windows** you downloaded before.

**Finally**, you should have something like this:

![sofa_files](https://www.sofa-framework.org/wp-content/uploads/2015/11/sofa_files.png)


### Generate a Makefile with CMake

If you didn't do it yet, create a build/ folder respecting directories
arrangement.

Open CMake-GUI and set source folder with **Browse Source** and build
folder with **Browse Build**.

Next, run *Configure*. A popup window will ask you to specify the
generator for the project. Using the drop down menu, select your
preferred version of Visual Studio. If you have Visual Studio 2013 and a
64-bit system select "Visual Studio 12 2013 Win64". Keep "Use default
native compilers" selected, and press "Finish".

You need to run *Configure* **twice**, since SOFA requires two passes to
manage the module dependencies. You can then customize your version of
SOFA, activate or deactivate plugins and functionalities.

To solve Qt detection errors, click on **Add Entry** and add
`CMAKE_PREFIX_PATH` with path C:/Qt/QtX.X.X/X.X/msvcXXXX matching your
Qt MSVC folder. *Configure* again.

To solve Boost detection errors, click on **Add Entry** and add
`BOOST_LIBRARYDIR` with path C:/boost/boost_1_XX_X/libXX-msvc-XX.X matching your
Boost lib folder. *Configure* again.

A further dev warning may appear:

    CMake Warning (dev) at YOUR_QT_MSVC_PATH/lib/cmake/Qt5Core/Qt5CoreMacros.cmake:224 (configure_file):
    configure_file called with unknown argument(s):

    COPY_ONLY

    Call Stack (most recent call first):
    applications/projects/Modeler/exec/CMakeLists.txt:14 (qt5_add_resources)

This is just a typo with Qt5CoreMacros.cmake file. It uses COPY\_ONLY
instead of COPYONLY. Simply edit your Qt5CoreMacros.cmake, replace
COPY\_ONLY with COPYONLY and *Configure* again.

When you are ready, press **Generate**. This will create your Visual
Studio solution or your makefiles if you chose another generator.


### Compile

If you are using Visual Studio, building SOFA is just like any other
project building. Simply open the generated Sofa.sln and build the
solution.

Time for a coffee !

