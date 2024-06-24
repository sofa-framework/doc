SOFA provides pre-compiled binaries, eliminating the need to compile the software from its source code. This simplifies the process for users to get started with SOFA. Below are detailed instructions on how to download, install, and execute SOFA:

## Download

To download SOFA, visit the official SOFA website at [https://www.sofa-framework.org/download/](https://www.sofa-framework.org/download/). On this page, you will find the latest version of SOFA. There are two types of files available, download one or the other:

- Installer Files: these files are designed for easy installation of SOFA, including all the necessary binaries, on your operating system.
- Zip Files: these files contain a folder with the SOFA application and its associated binaries.  

If you choose the zip file option, extract its contents to access the SOFA application and binaries.

If you require a specific version of SOFA, you can also find previous releases on the official SOFA GitHub repository at [https://github.com/sofa-framework/sofa/releases](https://github.com/sofa-framework/sofa/releases).

## Install

If you downloaded an installer file, simply run the file, and follow the installation process as you would for any other software application. This will ensure that SOFA is properly installed on your system.

## Execute

To run SOFA, locate and execute the application called `runSofa`. For more detailed information on how to use the application, you can refer to the official documentation on the SOFA website at [https://www.sofa-framework.org/community/doc/using-sofa/runsofa/](https://www.sofa-framework.org/community/doc/using-sofa/runsofa/). This documentation will provide you with further guidance on using SOFA effectively.

### Notes for macOS Users

Unfortunately, macOS binaries of SOFA are not code-signed. It means that macOS adds a quarantine flag to the binaries when a user downloads them. The result is a warning window with the message "runSofa cannot be opened because the developer cannot be verified.", preventing to open the application.

There are several solutions to run SOFA anyway:

- Build SOFA by yourself. MacOS does not add the quarantine flags on the local builds. See the instructions [here](https://www.sofa-framework.org/community/doc/getting-started/build/macos/).
- Run the following command:

```bash
xattr -dr com.apple.quarantine path/to/sofa/folder
```

with path/to/sofa/folder is the folder where the binaries of SOFA are located. This command removes the quarantine flags on the binary files.
