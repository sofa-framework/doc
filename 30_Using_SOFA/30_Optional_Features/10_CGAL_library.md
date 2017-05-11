CGAL is a C++ library specialized on geometric computations. CGAL is a
big project, therefore it is not included natively into SOFA extlibs'
directory. Here is the way to compile it for SOFA using **CMake**.

Install the CGAL plugin - Linux
-------------------------------

With Linux, follow the next steps to install CGAL:

-   Install
    [Boost](http://www.boost.org/users/download/ "Boost download") for
    use with Sofa. Note that Sofa with CMake requires the compiled
    libraries,
-   Install GMP and MPFR librairies,
-   Install and compile
    [CGal](http://www.cgal.org/download.html "CGAL download")
    -   To compile CGAL you basically need to run:

            cmake .
            make

-   With CMake, set the **SOFA-PLUGIN\_CGALPLUGIN** option to On,
-   Configure. Set GMP\_DIR and MPFR\_DIR to the location that you
    installed GMP and MPFR. Configure again and generate.

You can now compile CGalPlugin.

Install the CGAL plugin - Windows
---------------------------------

**Downloads** You will need to download the following:

-   [CGal](http://www.cgal.org/download.html "CGAL download"): This
    tutorial will describe how to set up CGal using the installer
    provided by CGal, which is bundled with some additional
    required libraries.
-   [Boost](http://www.boost.org/users/download/ "Boost download"): This
    is required for a number of Sofa plugins

**Installing**

-   **Boost**: To use the version of Boost you downloaded, set the
    **SOFA-EXTERNAL\_BOOST\_PATH** cmake variable to its directory, for
    example:
    `SOFA-EXTERNAL_BOOST_PATH = "C:Program Files (x86)boostboost_1_46_1"`
-   **CGAL**: Run the installer that you downloaded above. At some
    point, there will be a dialog box asking about additional libraries
    that can be installed with your CGAL installation. Be sure that
    **GMP/MPFR** is selected.

**Compiling CGAL Libraries**

-   Open the CMake Gui
-   Set Where is the source code to the location that you installed CGAL
    in (example C:Program FilesCGAL-4.1)
-   Set Where to build the libraries to the same location
-   Press Configure. You shouldn't have to make any changes to
    the configuration. Keep pressing Configure until none of the values
    show up red.
-   Press Generate.
-   Open the newly created solution file (found in the CGAL directory)
    in Visual Studio
-   If needed, set the Build Configuration to Release. Compile.

**Compiling CGalPlugin**

-   Open the CMake Gui, and point it to your Sofa source and build
-   Check the **SOFA-PLUGIN\_CGALPLUGIN** option
-   If you haven't already done so, set **SOFA-EXTERNAL\_BOOST\_PATH**
    to your Boost directory
-   Press Configure. Keep pressuring Configure until none of the values
    show up red.

**Note**: If you have used the CGAL installer to install GMP and MPFR,
it should find the directories for those libraries automatically. If for
some reason GMP\_DIR and MPFR\_DIR are not set, you can direct set them
to the appropriate directory. They are both located in your CGal
directory under auxiliary/gmp. You can now open your Sofa solution and
compile CGalPlugin.

Test your plugin on the examples
--------------------------------

You can launch one of the example scenes available from the root (source
directory):
`runSofa applications/plugins/CGALPlugin/scenes/MeshGenerationFromImage.scn`
This scene takes as input an Image representing a rectangular
parallelepiped with 3 different label in the image. The CGAL library
allows to mesh the image using different parameters (e.g. element size)
depending on the label. The middle zone (blue) has very fine elements,
the purple area has medium-size elements and finally the red area
includes coarse tetrahedra. The generated mesh can finally be exported.
\[caption id="attachment\_1717" align="aligncenter"
width="600"\][![](https://www.sofa-framework.org/wp-content/uploads/2014/11/MeshGenerationFromImage.png){.wp-image-1717
width="600"
height="401"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/MeshGenerationFromImage.png)
Screenshot from the scene MeshGenerationFromImage.scn\[/caption\]
