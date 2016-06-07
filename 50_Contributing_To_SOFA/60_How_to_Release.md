Steps
=====

-   create branches \[v15.12\] on sofa and sofa-dev
-   run header script GPL / LGPL (TODO where is the script? check it use
    the right header for GPL (e.g. gui) /LGPL part (warning
    about plugins))

Building packages
-----------------

### Windows

-   (config: Visual Studio 2015 / x86, zip package)
-   select CPACK\_ZIP in the CMake configuration
-   compile as usual
-   modify the package project, in the post-build step (bug of Cmake or
    I missed something):

"C:\\Program Files (x86)\\CMake\\bin\\cpack.exe" -C \$(Configuration)
--config ./CPackConfig.cmake by "C:\\Program Files
(x86)\\CMake\\bin\\cpack.exe" -C \$(Configuration) --config
./CPackConfig.cmake -G ZIP

-   build the target "package"
-   it will create the zip file in your build directory

If you have a problem with CPack not finding Git, add the path of your
git.exe into your PATH environment variable.

#### Dependencies Notes

-   VS2015 redistribuable dlls come from the official executable of
    Microsoft (https://www.microsoft.com/en-US/download/details.aspx?id=48145)
-   Qt 5.5 has been built for VS2015 in x86 (I guess Qt will propose
    VS2015 pre-built binaries for the version 5.6)
-   boost 1.59 from
    <http://sourceforge.net/projects/boost/files/boost-binaries/1.59.0/> (boost\_1\_59\_0-msvc-14.0-32.exe)

### Linux

TODO

### OS X

OS X has a special package system (bundle/.app)

If you want an Unix-like archive (with normal filetree such as bin/
lib/, etc), follow instructions for Linux. It is meaningful for people
wishing to develop.

If you want a pure Mac OS X package, you have to:

-   enable the CMake option RUNSOFA\_INSTALL\_AS\_BUNDLE
-   configure/compile as usual
-   and to package, run: ninja install && cpack -G DragNDrop
    CPackConfig.cmake

It will create a dmg (compressed archive), with an app containing
\*all\* required libraries, runSofa binary and the share directory.
