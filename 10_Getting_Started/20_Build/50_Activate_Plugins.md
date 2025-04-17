# Activable plugins for in-tree compilation

Multiple extensions can be activated when building the project. They fall into three categories:
1. Applications: extensions that offer SOFA-based executable applications (e.g. a main for launching SOFA)
2. Plugins: extensions that enriche the SOFA API by adding new components or providing more support for external libraries (e.g. new constitutive laws, alternative GUIs)
3. Directories: extensions that contain multiple CMake projects that cannot be described by only one of the above type
Moreover, these projects are either present in the SOFA sources or they need to be fetched (meaning that they have their own external repository).

This page aims at summarizing those extensions in tables containing:
- the name + hyperlink to the extension sources either in the SOFA repository or in its own repository
- a short description
- activation directives

The activation directives propose two ways of activating those plugins in the build tree:
1. Through custom CMake flags that [can be added during the CMake call](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-D). All of those plugins can be activated with one or two CMake flags named using their type and name. For example, the plugin SofaPython3 can be activated by activating both flags `SOFA_FETCH_SOFAPYTHON3=ON` and `PLUGIN_SOFAPYTHON3=ON` (because its sources are in a separate repository).
2. Through preset that can be [specified during the CMake call](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html#introduction)

