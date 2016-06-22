This page describes how to get started writing your own SOFA components
in C++, and how to integrate them with SOFA by creating a plugin.

A SOFA plugin is mainly a collection of SOFA components, that can be
used in a scene. A plugin is actually a dynamic library that respects
some conventions, so that SOFA-based applications can load it at
runtime, and retrieve the components it provides. SOFA is based on CMake
so that you can refer to the [CMake
Documentation](https://cmake.org/documentation "CMake Documentation")
for any specific need.

The next subsection describes what a somewhat minimal plugin should
contain.

A minimal plugin: MyPlugin
==========================

As of now, the most convenient way to write a plugin is to place it
inside the source tree of SOFA, in applications/plugins/. For example,
here we create a plugin called MyPlugin, which we will place in
/applications/plugins/MyPlugin. It contains only the following files:

-   **initMyPlugin.h** and **initMyPlugin.cpp**: the plugin interface
-   the **CMakeLists.txt** file which describes how to build to plugin;

#### initMyPlugin.h

This file contains the DLL export / DLL import macro definitions which
are used on Windows to tell which symbols should be visible outside the
scope of the DLL currently built. (More about this on the MSDN website:
link [dllexport,
dllimport](http://msdn.microsoft.com/en-us/library/3y1sfaz2.aspx)). This
is also not a bad place to write the main page of the doxygen
documentation of your plugin.

``` cpp
#ifndef INITMYPLUGIN_H
#define INITMYPLUGIN_H

#include <sofa/helper/system/config.h>

#ifdef SOFA_BUILD_MYPLUGIN
#define SOFA_MyPlugin_API SOFA_EXPORT_DYNAMIC_LIBRARY
#else
#define SOFA_MyPlugin_API SOFA_IMPORT_DYNAMIC_LIBRARY
#endif

/** mainpage
This is the main page of the doxygen documentation for MyPlugin.
 */

#endif
```

#### initMyPlugin.cpp

This file contains the definition a bunch of functions with C linkage,
that SOFA will look for when it tries to load this plugin, namely:

-   initExternalModule(),
-   getModuleName(),
-   getModuleVersion(),
-   getModuleLicense(),
-   getModuleDescription()
-   and getModuleComponentList().

``` cpp
#include "initMyPlugin.h"

extern "C" {
    void initExternalModule()
    {
        // Here is the place to write initialisation code, that will be executed
        // before any component is created.
    }

    const char* getModuleName()
    {
        return "MyPlugin";
    }

    const char* getModuleVersion()
    {
        return "0.1";
    }

    const char* getModuleLicense()
    {
        return "LGPL";
    }

    const char* getModuleDescription()
    {
        return "MyPlugin provides nothing for now.";
    }

    const char* getModuleComponentList()
    {
        // Comma-separated list of the components in this plugin, empty for now
        return "";
    }
}
```

CMake configuration
===================

#### CMakeLists.txt

To integrate with the build system of SOFA, your CMakeLists.txt file
should be structured as follows:

``` {.cmake}
cmake_minimum_required(VERSION 2.8.12)
project(MyPlugin)


set(HEADER_FILES
    MyHeaderFile1.h
    MyHeaderFile2.h
    MyHeaderFile3.h
)

set(SOURCE_FILES
    MySourceFile1.cpp
    MySourceFile2.cpp
    MySourceFile3.cpp
)

find_package(SofaFramework REQUIRED)

add_library(${PROJECT_NAME} SHARED ${HEADER_FILES} ${SOURCE_FILES})
target_link_libraries(${PROJECT_NAME} SofaCore)
```

*MyPlugin* is your plugin name. The repository of your plugin should be
named MyPlugin as well. Set all the source and header files implemented
in your plugin so that they can be built.

Your plugin might have some dependencies, here with SofaFramework. Then,
the associated package need to be specified as REQUIRED.

Your plugin has to be added as a new library including the source and
header files to the project. To do so, use the *add\_library* CMake
command.

Finally, the dependencies are specified using the
*target\_link\_libraries* CMake command.

**Quick start** - you can find a skeleton of an empty plugin in the
repository of SOFA, in *applications/plugins/PluginExample*.

#### Install in CMake

To install your plugin, the following command needs to be added at the
end of your CMakeList.txt file:

``` {.cmake}
install(TARGETS MyPlugin
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)
```

And the following must be added to *applications/plugins/CMakeLists.txt*:

``` {.cmake}
sofa_add_plugin(MyPlugin MyPlugin)
```

Keep us updated!
================

When starting a new plugin, do not hesitate to let us know about it so
that we can help and advert your work. The better we know the community,
the better we can support it!
