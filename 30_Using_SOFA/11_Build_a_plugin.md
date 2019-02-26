This page presents how to build an external plugin,
i.e. a plugin which is not provided in the source code of SOFA.

Preferred file architecture
---------------------------

If you use the source code of SOFA, you want compile and use one or more
external plugins it is preferred to create one specific repository
outside SOFA where you can checkout all these external plugins.
This structure is preferred since it will allow a clean organization
of external plugins in one single repository.
Let's note the path to this repository */ext_plugin_repo/*.

In this directory, the structure is:

- ext_plugin_repo/
    - plugin1/
    - plugin2/
    - ...


CMakeList of the repository
---------------------------

In order to handle this repository as one single set of external plugins,
you need to write a short CMakeList.txt file as follows:

```
cmake_minimum_required(VERSION 2.8.12)

find_package(SofaFramework)

sofa_add_plugin(plugin1/  name_of_project_plugin1)
sofa_add_plugin(plugin2/  name_of_project_plugin2)
```

CMake option in SOFA
--------------------

To compile all the external plugins located in this repository,
all you need to do is to set the path to this repository (*/ext_plugin_repo/*)
in the CMake variable: **SOFA\_EXTERNAL\_DIRECTORIES**.

This will directly configure and allow to compile all specified plugins from SOFA.