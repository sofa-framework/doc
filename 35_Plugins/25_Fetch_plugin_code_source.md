# Fetch Plugin Code Source

A few number of plugins are directly shipped with the SOFA code source.
Most of them are deactivated by default, and it is up to the developer to activate the compilation in CMake through a corresponding CMake variable.

However, plugins can also be found in other repositories.
For example, here is a list of important plugins with their corresponding repository:

| Plugin              | Repository                                                                                               |
|---------------------|----------------------------------------------------------------------------------------------------------|
| SofaPython3         | [https://github.com/sofa-framework/SofaPython3](https://github.com/sofa-framework/SofaPython3)           |
| SofaGLFW            | [https://github.com/sofa-framework/SofaGLFW](https://github.com/sofa-framework/SofaGLFW)                 |
| CGALPlugin          | [https://github.com/sofa-framework/CGALPlugin](https://github.com/sofa-framework/CGALPlugin)             |
| SoftRobots          | [https://github.com/SofaDefrost/SoftRobots](https://github.com/SofaDefrost/SoftRobots)                   |
| ModelOrderReduction | [https://github.com/SofaDefrost/ModelOrderReduction](https://github.com/SofaDefrost/ModelOrderReduction) |
| Caribou             | [https://github.com/mimesis-inria/caribou](https://github.com/mimesis-inria/caribou)                               |

Some plugins from other repositories can be directly fetched from SOFA at the configuration stage with CMake.
To fetch the code source of a plugin, follow these steps:
1) In CMake, activate the variable `SOFA_FETCH_{PLUGINNAME}`.
2) Configure. After the configuration, the variable `SOFA_FETCH_{PLUGINNAME}` is automatically unchecked.
3) The CMake variable `PLUGIN_{PLUGINNAME}` becomes available. Activate it.
4) Configure and generate. The plugin will be compiled along with SOFA.

![](https://raw.githubusercontent.com/sofa-framework/doc/master/images/plugins/SOFA_FETCH.png)

Fetching the code source of a plugin uses git to clone a repository (usually the master branch) in the SOFA build directory.
It is done one time, and it is then up to the developer to update and manage the git directory.
For developing on a plugin repository, it is advised to follow [these steps](https://www.sofa-framework.org/community/doc/plugins/build-a-plugin-from-sources/) rather than fetching the code source. 
