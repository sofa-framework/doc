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

1. Through custom CMake flags that [can be added during the CMake call](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-D). All of those plugins can be activated with one or two CMake flags named using their type and name. For example, the plugin SofaPython3 can be activated by activating both flags `SOFA_FETCH_SOFAPYTHON3=ON` and `PLUGIN_SOFAPYTHON3=ON` (because its sources are in a separate repository, see bellow).
2. Through preset that can be [specified during the CMake call](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html#introduction)

### Note on fetched plugins

As stated before, some plugins have their own repository and thus need to be fetched to be compiled in-tree. To do so, you will need to activate the associated flag `SOFA_FETCH_XXX=ON` (while replacing `XXX` by the capitalized name of your plugin). Note that all '.' in the plugin name should be replaced by a '_', e.g. to fetch Sofa.Qt, one need to set the CMake flag `SOFA_FETCH_SOFA_QT=ON`.

The repository from which to fetch and the tag to checkout can be changed by using the respective flags `XXX_GIT_REPOSITORY` and `XXX_GIT_TAG`. The tag can be either a tag, a branch name or a commit hash. 

It should be noted that you can use a local clone of the repository, instead of relying on the fetching mechanism. This can be useful when you have a version of the plugin on your disk on which you are currently working. To do this, you'll need to specify the flag `XXX_LOCAL_DIRECTORY` with an absolute path to the local clone of the plugin. If This flag is non-empty it'll be used in priority over the fetching mechanism.

No matter what mechanism you use (fetch or local clone), you will still need to activate it by setting to ON the following CMake flag `{TYPE}_XXX` where TYPE corresponds to one of the following keywords: `{"APPLICATION", "PLUGIN", "DIRECTORY"}`.


