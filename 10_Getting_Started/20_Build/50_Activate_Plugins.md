# Activable plugins for in-tree compilation

Multiple extensions can be activated when building the project. They are differentiated in three categories:
1. Applications: extension that offers a new feature outside the SOFA API (e.g. a main for launching SOFA)
2. Plugins: extension that enriches the SOFA API by adding new components or providing more support for external libraries (e.g. new constitutive laws, Qt gui)
3. Directories: extension that contains multiple CMake projects that cannot be described by one of the above type
Moreover those project are either directly present in the SOFA sources or need to be fetched because they have their own repository

This page only purpose is to summarize those extensions in tables containing 
- The name + hyperlink to the extension sources either in the SOFA repo or in its own repo
- A quick description of what it is
- Activation directives. 

The activations directives propose two ways of activating those plugins in the build tree:
1. Through custom CMake flags that [can be added during the cmake call](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-D). All of those plugins can be activated with one or two CMake flags named using their type and name. For example, the plugin SofaPython3 can be activated by activating both flags `SOFA_FETCH_SOFAPYTHON3=ON` and `PLUGIN_SOFAPYTHON3=ON` (because its sources are in a separate repository). If points are present in the name, they are replaced by "_" in the flag.
2. Through preset that can be [specified during the cmake call](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html#introduction)

