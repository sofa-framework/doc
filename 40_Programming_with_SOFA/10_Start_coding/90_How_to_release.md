# Initial steps

When you are ready for creating a release:

-   check the status of the build on the [dashboard](http://www.sofa-framework.org/dash/)
-   make sure the [changelog](https://github.com/sofa-framework/sofa/blob/master/CHANGELOG.md) is up-to-date
-   make sure your local SOFA repository is up-to-date  
    ```bash
    git checkout master  
    git stash  
    git pull -r
    ```
    
-   check the year in the files: README.md, Authors.txt, LICENCE.txt, CMakeList.txt (SOFA, SofaKernel, SofaFramework)
-   create a new branch for the release: `git checkout -b v1.1`
-   push this new branch on the remote repository: `git push -u origin v1.1`

In this new branch:  

-   run header script in scripts/licenseUpdater to change the version (for both GPL / LGPL parts):
    ```
    licenseUpdater.sh <path_to_sofa> <year> <version>
    ```
    
-   update the version in CMakeLists.txt  
    ```cmake
    #CPack install  
    SET(CPACK_PACKAGE_VERSION "17.06.00")  
    SET(CPACK_PACKAGE_VERSION_MAJOR "17")  
    SET(CPACK_PACKAGE_VERSION_MINOR "06")  
    SET(CPACK_PACKAGE_VERSION_PATCH "00")
    ```
    
-   update the version in SofaKernel/SofaFramework/CMakelists.txt
    ```cmake
    ## Version
    set(SOFAFRAMEWORK_VERSION "17.06.00")
    
    ## sofa/version.h
    set(SOFA_VERSION "170600")
    set(SOFA_VERSION_STR "\"17.06\"")
    ```
     
-   enable the CMake option `SOFA_BUILD_RELEASE_PACKAGE`

The next steps do depend on the operating system.


## Linux

-   configure + generate + compile
-   install: `make install` or `ninja install`  
-   in new install dir:
    - add license directory
    - fix wrong lib symlinks (pointing to system libs)
-   create a .zip archive of install dir


## Windows

-   configure + generate + compile
-   run `make package` or `ninja package` to build .exe installer (needs NSIS)


## OS X

OS X has a special package system (bundle/.app)

If you want an Unix-like archive (with normal filetree such as bin/
lib/, etc), follow instructions for Linux. It is meaningful for people
wishing to develop.

If you want a pure Mac OS X package, you have to:

-   configure + generate + compile
-   install: `make install` or `ninja install`
-   create .dmg package: `cpack -G DragNDrop CPackConfig.cmake`

It will create a dmg (compressed archive), with an app containing
**all** required libraries, runSofa binary and the share directory.

### Misc

Tricks while doing Qt Packaging:

- (OS X) before running, to show when dylibs are loaded:  
```bash
DYLD_PRINT_LIBRARIES=1
./runSofa
```
- Qt plugins are not loaded at runtime so to force Qt to print when plugins are loaded and used: `export QT_DEBUG_PLUGINS=1`


# Final steps

Once the binaries are generated:

-   update the link on the [download](https://www.sofa-framework.org/download/) page for the binaries (add changes in dependencies)
-   update the doc for building SOFA:
    -   for [Linux](https://www.sofa-framework.org/community/doc/getting-started/build/linux/)
    -   for [MacOS](https://www.sofa-framework.org/community/doc/getting-started/build/mac-os-x/)
    -   for [Windows](https://www.sofa-framework.org/community/doc/getting-started/build/windows/)
-   update the flag on the forum
-   create [announcement](https://www.sofa-framework.org/community/forum/section/announcements-infos/) on the forum, [twitter](https://twitter.com/SofaFramework), LinkedIn, SOFA dev, post.
-   create a [release](https://github.com/sofa-framework/sofa/releases) GitHub with a link to the changelog
