Prerequisites for Windows
=========================

#### Compiler

You need to have Visual Studio 2008 or higher installed. We recommend
Visual Studio 2012 (tested on [our
Dashboard](http://www.sofa-framework.org/dash/)) or Visual Studio 2013
(to use the latest Qt5 64bit binaries). Both are available in [Visual
Studio downloads
page](https://www.visualstudio.com/fr-fr/downloads/download-visual-studio-vs.aspx).


#### CMake: Makefile generator

You need to have CMake 2.8.8 or higher installed. The easiest way to do
this is to get the installer from the [CMake download
page](https://cmake.org/download/).


#### Required dependencies

Finally, SOFA requires some specific dependencies:

-   **Qt**: you need to have Qt 4.8.3 or higher installed. We recommend to install Qt from
    [the unified Windows installer](http://download.qt.io/official_releases/online_installers/qt-unified-windows-x86-online.exe).  
    **WARNING**: Choose the Qt version matching your compiler.  
	If you choose Qt 5.5.x or upper, make sure you check all the Qt stuff after "Source Components" (Qt3D, Qt Location, ...).  
	If you choose Qt 5.4.x or lower, you will have to select an **OpenGL version** of the binary. There is not an OpenGL version for each compiler for each Qt version so this may force you to use an old Qt.  
	**Summary:**  
	MSVC2013 32-bit/64-bit, MSVC2015 32-bit/64-bit : Qt 5.6  
	MSVC2012 32-bit : Qt 5.5  
	MSVC2012 64-bit : Qt 5.2.1 (OpenGL version)
-   **Boost**: you need to have Boost installed. You will find the last
    official Boost installer for every Visual Studio version
    [here](https://sourceforge.net/projects/boost/files/boost-binaries/).
    SOFA is fully compatible with Boost 1.60.0 and older (not tested
    with newer versions). Beware of the correspondance between Visual
    Studio and MSVC versions (VS2013 = MSVC12, VS2012 = MSVC11, ...).
-   **External libraries**: some external libraries like Zlib or libXML2
    are required.
    -   Download the [SOFA dependencies for Windows using VS2013](https://gforge.inria.fr/frs/download.php/file/36036/sofa-win-dependencies-21-11-2013_VS2013.zip).
    -   or the [SOFA dependencies for Windows using VS2015](https://gforge.inria.fr/frs/download.php/file/36035/sofa-win-dependencies-06-11-2015_VS2015.zip).
    You will unzip them in your sources folder (e.g. sofa/v15.12/src/)
    after cloning SOFA (see below).



#### PATH

To complete the dependencies integration, you can add Boost and Qt to
your PATH.  
**Boost**: add `your/boost/path/libXX-msvc-XX`  
**Qt**: add `your/Qt/path/msvcXXXX_XX/bin` and `your/Qt/path/msvcXXXX_XX/lib`


Building on Windows
===================


### Setting up your source and build directories

To set up clean repositories, we propose to arrange the SOFA directories
as follows:

-   sofa/
    -   v15.12/
        -   src/
        -   build/
    -   master/
        -   src/
        -   build/

**First**, download the sources from Git repository:

Get the current **stable** version on the v15.12 branch:

``` {.bash .stable}
git clone -b v15.12 https://github.com/sofa-framework/sofa.git sofa/v15.12/src/
```

Or get the development **unstable** version on the master branch:

``` {.bash .unstable}
git clone -b master https://github.com/sofa-framework/sofa.git sofa/master/src/
```

**Next**, unzip in your sources folder (e.g. sofa/v15.12/src/) the [SOFA
dependencies for
Windows](https://gforge.inria.fr/frs/download.php/33142/sofa-win-dependencies-21-11-2013.zip)
you downloaded before.

**Finally**, you should have something like this:

![sofa_files](https://www.sofa-framework.org/wp-content/uploads/2015/11/sofa_files.png)


### Generate a Makefile with CMake

If you didn't do it yet, create a build/ folder respecting directories
arrangement.

Open CMake-GUI and set source folder with **Browse Source** and build
folder with **Browse Build**.

To avoid Qt detection errors, click on **Add Entry** and add
`CMAKE_PREFIX_PATH` with path C:/Qt/QtX.X.X/X.X/msvcXXXX matching your
Qt MSVC folder.

Next, run **Configure**. A popup window will ask you to specify the
generator for the project. Using the drop down menu, select your
preferred version of Visual Studio. If you have Visual Studio 2013 and a
64-bit system select "Visual Studio 12 2013 Win64". Keep "Use default
native compilers" selected, and press "Finish".

You need to run **Configure** twice, since SOFA requires two passes to
manage the module dependencies. You can then customize your version of
SOFA, activate or deactivate plugins and functionalities.

A further dev warning may appear:

    CMake Warning (dev) at YOUR_QT_MSVC_PATH/lib/cmake/Qt5Core/Qt5CoreMacros.cmake:224 (configure_file):
    configure_file called with unknown argument(s):

    COPY_ONLY

    Call Stack (most recent call first):
    applications/projects/Modeler/exec/CMakeLists.txt:14 (qt5_add_resources)

This is just a typo with Qt5CoreMacros.cmake file. It uses COPY\_ONLY
instead of COPYONLY. Simply edit your Qt5CoreMacros.cmake, replace
COPY\_ONLY with COPYONLY and **Configure** again.

#### Boost detection

**WARNING**: With v15.03, v15.09 and v15.12, no error shows up
concerning Boost (miniBoost is integrated with sources). But since Boost
is needed by several plugins, we decided to remove miniBoost from our
future releases. So you better learn now how to manually tell to CMake
where are Boost libraries.

In CMake-GUI, check the Advanced box (right from Search text-box) and
search for "Boost". Manually set `Boost_INCLUDE_DIR` with your Boost
root directory if it is empty. Manually set `Boost_THREAD_LIBRARY_DEBUG`
with absolute path of boost\_thread-vcXXX-mt-gd-1\_XX.lib and
`Boost_THREAD_LIBRARY_RELEASE` with absolute path of
boost\_thread-vcXXX-mt-1\_XX.lib.

Then run **Configure** twice (you should see no more red entries). Other
Boost libraries should be auto-detected.

Expected result for VS2013 64-bit build with Boost 1.59.0 installed in
C:/boost/ :

![screen_boost_cmake](https://www.sofa-framework.org/wp-content/uploads/2015/11/screen_boost_cmake.png)

When you are ready, press **Generate**. This will create your Visual
Studio solution.



### Compile

If you are using Visual Studio, building SOFA is just like any other
project building. Simply open the generated Sofa.sln and build the
solution.

Time for a coffee !

