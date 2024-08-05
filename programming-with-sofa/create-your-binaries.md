---
title: Create your binaries
---

## SOFA binaries

### Prepare the sources  
    
- Update SOFA version in CMakeLists.txt  
    ```cmake
    # Manually define VERSION
    set(Sofa_VERSION_MAJOR <new release major version>)
    set(Sofa_VERSION_MINOR <new release minor version>)
    set(Sofa_VERSION_PATCH <new release patch version>)
    ```
- Update External Projects versions  
  For each ExternalProject.cmake.in file in the sources, edit the line `GIT_TAG origin/<branch of the new release>`
- Set the CMake variables
    ```cmake
    SOFA_BUILD_RELEASE_PACKAGE=ON
    CPACK_GENERATOR=ZIP
    CPACK_BINARY_ZIP=ON
    ```
- If you want to generate an installer:
    - Install the latest [Qt Installer Framework (Qt IFW)](https://download.qt.io/official_releases/qt-installer-framework/)
    - Set the CMake variables  
    ```cmake
    CPACK_IFW_ROOT=<location of QtIFW (no "bin" at the end)>
    CPACK_GENERATOR=ZIP;IFW
    CPACK_BINARY_ZIP=ON
    CPACK_BINARY_IFW=ON
    ```
- [MacOS] Set CMake variable for OSX compatibility version:  
   ```
   CMAKE_OSX_DEPLOYMENT_TARGET=10.15
   ```
- [MacOS] If you want to generate a bundle (.app), set the CMake variables:  
    ```cmake
    CPACK_GENERATOR=ZIP;DragNDrop
    CPACK_BINARY_ZIP=ON
    CPACK_BINARY_DRAGNDROP=ON
    ```

### Generate the binaries

- Configure + Generate + Build
- Install: `make install` or `ninja install`  
- Make sure that `linux-postinstall-fixup.sh` or `windows-postinstall-fixup.sh` or `macos-postinstall-fixup.sh` was triggered and its output is OK
- Your binaries should be in your build directory


## Plugin binaries




## Troubleshooting

- To show how Qt plugins are loaded and used: `export QT_DEBUG_PLUGINS=1`
- [Linux][MacOS] To fix library dependency resolution: `export LD_LIBRARY_PATH=/path/to/sofa/bin:/path/to/sofa/lib:$LD_LIBRARY_PATH`
- [MacOS] To show when dylibs are loaded: `export DYLD_PRINT_LIBRARIES=1`


## Publishing a SOFA release

Once the binaries are generated:

- Create a [release](https://github.com/sofa-framework/sofa/releases) on GitHub.
- Update the link on the [download](https://www.sofa-framework.org/download/) page for the binaries (add changes in dependencies).
- Update the doc for building SOFA:
    - on [Linux](https://www.sofa-framework.org/community/doc/getting-started/build/linux/)
    - on [MacOS](https://www.sofa-framework.org/community/doc/getting-started/build/mac-os-x/)
    - on [Windows](https://www.sofa-framework.org/community/doc/getting-started/build/windows/)
- Update the flags on the forum.
- Create a post on the forum, on Twitter, on LinkedIn.
