# Use plugin binaries

SOFA is regularly released along with several officially-supported plugins. However, many more plugins do exist. It may occur that someone shares with you the binaries of a plugin (pre-compiled plugin) which are not distributed in the SOFA releases. Make sure this third-party plugin is trustworthy.

## Compatibility check

In such a case, one must firstly check that the compilation environment of the plugin should be compatible with yours:
- check the operating system
- check the SOFA version
- check the version of the dependencies (libraries like Python, pybind11, Qt, Boost, Eigen, TinyXML2, Glew, Zlib, libPNG, libJPEG, libTIFF)


## Load in SOFA

See [What is a plugin > Plugin loading](./../what-is-a-plugin/#plugin_loading).
