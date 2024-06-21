---
title: HAPI
---

Configuring
-----------

-   Install
    [HAPI](http://www.h3dapi.org/modules/PDdownloads/viewcat.php?cid=15 "http://www.h3dapi.org/modules/PDdownloads/viewcat.php?cid=15"){.external
    .text}, using either an installer or with the source code (For
    VS2010, see below). If you use the installer and keep it in the
    default directory, it should install to C:/HAPI. If you use the
    source, it will be in the directory that you specify. From this
    point forward, we will refer to this directory
    as MyHAPIInstallation.
-   Turn on the option **SOFA-PLUGIN\_SOFAHAPI** in CMake,
    and configure.
-   Likely, CMake will report that HAPI was not found. You can manually
    set:

`HAPI_INCLUDE_DIR = MyHAPIInstallation/HAPI/include`
`HAPI_LIBRARY = MyHAPIInstallation/lib/HAPI_vc9.lib` If you are not
compiling in Visual Studio 2008, change the \_vc9.lib suffix to whatever
version is appropriate. HAPI\_DEBUG\_LIBRARY is optional. Configure
again.

-   Next, you will probably get an error that H3DUTIL was not found. You
    can manually set:

`H3DUTIL_INCLUDE_DIR = MyHAPIInstallation/H3DUtil/include`
`H3DUTIL_LIBRARY = MyHAPIInstallation/lib/H3DUtil_vc9.lib` Again,
changing the library suffix if needed. H3DUTIL\_DEBUG\_LIBRARY is
optional. Configure again.

-   Finally, you will probably get an error that PTHREAD was not found.
    You can manually set:

`PTHREAD_INCLUDE_DIR = MyHAPIInstallation/External/include/pthread`
`PTHREAD_LIBRARY = MyHAPIInstallation/External/lib/pthreadVC2.lib` Note
that pthreadVC2.lib is not in the same directory as the previous two
libraries. Configure again.

-   You should now be able to Generate and compile without problems.

HAPI for VS2010
---------------

The HAPI installer doesn't include libraries for VS2010, so you will
have to build them yourself.

-   Start by using the installer, as it will get you the source code and
    Pthread, a required library.
-   Using CMake, set the **Source Code** to
    **MyHAPIInstallation/HAPI/build**.
-   Set the **Build** to where you want to source to be built.
-   Press Configure, and choose Visual Studio 10 as the
    desired compiler.
-   Press Configure until all the red highlighted things are gone.
-   Press Generate.
-   Open the resulting Solution file in Visual Studio 2010, and compile.
-   Once everything finishes compiling, you can find
    **H3DUtil\_vc10.lib** in
    **MyHAPIInstallation/H3DUtil/build/Release** and **HAPI\_vc10.lib**
    in **MyHAPIInstallation/HAPI/build/Release**. You can either leave
    them where they are and point CMake to them when configuring, or
    copy them to**MyHAPIInstallation/lib** with the libraries for the
    other versions of Visual Studio.
-   Repeat the compilation is debug mode if desired.

