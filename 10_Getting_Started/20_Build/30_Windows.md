SOFA policy is to support only the latest Windows version.

# Installation with Pixi

You can download and build SOFA in only three steps without any environment installation.

## Prerequisites

- [Install Git](https://git-scm.com/install/windows)
- [Install Pixi](https://pixi.prefix.dev/latest/installation/)


## Installation steps

- Clone SOFA : `git clone https://github.com/sofa-framework/sofa` :inbox_tray: 
- Trigger the build : run `pixi run -e supported-plugins build` in the sofa source folder :desktop_computer: 
- Launch SOFA : run `pixi run -e supported-plugins runSofa` :rocket: 




# Manual installation (for developpers)

<details>

<summary>This installation method is advised for developers. It is STRONGLY advised to read through this entire doc page before getting started.</summary>

<h2>Build tools</h2>

<h3>Compiler</h3>

SOFA requires a <a href="https://en.cppreference.com/w/cpp/compiler_support#C.2B.2B17_features">C++17 compatible compiler</a>.<br>On Windows, we officially support <strong>Microsoft Visual Studio &gt;= 2017</strong> (version 15.7).<br>If you want to use <strong>Visual Studio IDE</strong>, install the complete Visual Studio solution.<br>If you want to use <strong>another IDE</strong> (like QtCreator), install the Build Tools only.

<table>
<thead>
<tr>
<th></th>
<th style="text-align:center"><strong>Visual Studio 2017</strong></th>
<th style="text-align:center"><strong>Visual Studio 2019</strong></th>
<th style="text-align:center"><strong>Visual Studio 2022</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Build Tools only</strong></td>
<td style="text-align:center"><a href="https://visualstudio.microsoft.com/fr/thank-you-downloading-visual-studio/?sku=BuildTools&amp;rel=15">download</a></td>
<td style="text-align:center"><a href="https://visualstudio.microsoft.com/fr/thank-you-downloading-visual-studio/?sku=BuildTools&amp;rel=16">download</a></td>
<td style="text-align:center"><a href="https://visualstudio.microsoft.com/fr/thank-you-downloading-visual-studio/?sku=BuildTools&amp;rel=17">download</a></td>
</tr>
<tr>
<td><strong>IDE + Build Tools</strong></td>
<td style="text-align:center"><a href="https://visualstudio.microsoft.com/fr/thank-you-downloading-visual-studio/?sku=Community&amp;rel=15">download</a></td>
<td style="text-align:center"><a href="https://visualstudio.microsoft.com/fr/thank-you-downloading-visual-studio/?sku=Community&amp;rel=16">download</a></td>
<td style="text-align:center"><a href="https://visualstudio.microsoft.com/fr/thank-you-downloading-visual-studio/?sku=Community&amp;rel=17">download</a></td>
</tr>
</tbody>
</table>


In the installer, you must enable:

<ol>
<li>In the main panel: the <strong>C++ development toolkit</strong>, called &quot;C++ Build Tools&quot; or &quot;Desktop C++&quot;.</li>
<li>In the side panel: the <strong>C++ ATL</strong> and <strong>C++ MFC</strong> components.</li>
</ol>

<img src="https://www.sofa-framework.org/wp-content/uploads/2020/03/install_vs_ide.png" alt="">


<h3>CMake: Makefile generator</h3>

SOFA requires at least <strong>CMake 3.22.1</strong>.
Install CMake with <a href="https://github.com/Kitware/CMake/releases/latest">the latest official installer</a>.
<strong>IMPORTANT</strong>: check the option <strong>&quot;Add CMake to the system PATH for all users&quot;</strong> during the install process.

<img src="https://www.sofa-framework.org/wp-content/uploads/2019/03/install-cmake.png" alt="">


<h3>[optional] Ninja: build system</h3>

We strongly advise you to use Ninja if you chose to install the Build Tools only (no IDE).

Ninja is an alternative to NMake. It has a better handling of incremental builds.  
You can download the latest release from <a href="https://github.com/ninja-build/ninja/releases">their GitHub repository</a>.
<strong>IMPORTANT</strong>: do not forget to <strong>add ninja to your system PATH</strong>.

<h2>Dependencies</h2>

<h3>Core (required)</h3>

SOFA requires some libraries:
<ul>
<li><strong>Boost</strong> (&gt;= 1.65.1)<br>Download and install the latest version compatible with your Visual Studio from <a href="https://sourceforge.net/projects/boost/files/boost-binaries/">https://sourceforge.net/projects/boost/files/boost-binaries/</a>.
<ul>
<li><strong>For Visual Studio 2022</strong>: choose boost_X_X_X-msvc-14.3-64.exe</li>
<li><strong>For Visual Studio 2019</strong>: choose boost_X_X_X-msvc-14.2-64.exe</li>
<li><strong>For Visual Studio 2017</strong>: choose boost_X_X_X-msvc-14.1-64.exe</li>
</ul>
</li>
<li><strong>Python</strong> (= 3.12.x)<br>Download and install the latest <a href="https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe"><strong>Python 3.12 (amd64)</strong></a>.
Python 3.12 now favor the use of venv. We highly recommend it too. To bootstrap it type <code>C:\path\to\python3.12 -m venv sofa-venv</code> in the folder you want to keep this venv. We recommend creating it either in your home directory, in the folder containing both your sources and the build directory. Once created, you can activate it by calling <code>C:\path\to\sofa-venv\bin\Scripts\activate.bat</code>. Now you can install all dependency through the following commands.
Then, install the Python dependencies. Run the following commands in cmd by replacing <code>path\to\Python312\</code> by the path to you venv bin directory.
    ```
    path\to\Python312\python.exe -m pip install --upgrade pip
    path\to\Python312\python.exe -m pip install numpy scipy pybind11==2.12.0
    ```
    Now, each time you want to build or use SOFA, you first need to call `C:\path\to\sofa-venv\bin\Scripts\activate.bat` to activate this virtual environment and get access to the dependencies. 
</li>
<li><strong>Additional libraries</strong>: libPNG, libJPEG, libTIFF, Glew, Zlib, TinyXML2
It will be fetch automatically from <a href="https://github.com/sofa-framework/WinDepPack.git">https://github.com/sofa-framework/WinDepPack.git</a> directly by SOFA CMake generation. For advanced dev, you can provide you own by modfying the CMake variables WINDEPPACK_GIT_REPOSITORY and WINDEPPACK_GIT_TAG.
</li>
<li><strong>Eigen</strong> (&gt;= 3.2.10)<br>Download and extract the <a href="https://gitlab.com/libeigen/eigen/-/releases">latest Eigen sources</a>.
</li>
</ul>


<h4>[optional] PATH modification</h4>

You can add Boost to your PATH to ease their detection by CMake.<br><strong>Boost</strong>: add <code>your/Boost/path</code> and <code>your/Boost/path/libXX-msvc-XX</code>  


<h2>Build SOFA</h2>


<h3>Setup your source and build directories</h3>

To set up clean repositories, we recommend to arrange the SOFA directories
as follows:

```
sofa/
├── build/
│   ├── master/
│   └── v26.06/
└── src/
    └── < SOFA sources here >
```

<strong>First</strong>, checkout the sources from Git repository:

Get the current <strong>stable</strong> version on the v26.06 branch:

``` {.bash .stable}
git clone -b v26.06 https://github.com/sofa-framework/sofa.git sofa/src
```

<strong>OR</strong> get the development <strong>unstable</strong> version on the master branch:

``` {.bash .unstable}
git clone -b master https://github.com/sofa-framework/sofa.git sofa/src
```

<h3>Generate a VS project (.sln) or a Makefile with CMake</h3>

<ol>
  <li>Create build directories respecting the arrangement above.</li>

  <li>In Windows Start menu, search for <code>Native Tools Command Prompt</code> and run the one corresponding to your Windows architecture (x64 for 64-bit, x86 for 32-bit).<br>
  <img src="https://www.sofa-framework.org/wp-content/uploads/2020/04/SearchCommandPrompt2.png" alt="Search Command Prompt"></li>

  <li>Call
    <pre><code>C:\path\to\sofa-venv\bin\Scripts\activate.bat</code></pre>
    to activate the virtual environment.
  </li>

  <li>In the command prompt, type <code>cmake-gui</code> and press Enter.<br>
    If you get the error <code>'cmake-gui' is not recognized as an internal or external command</code>, it means that your system PATH does not correctly include the path to cmake-gui. In this case, you need to provide the full path to your cmake-gui.</li>

  <li>In CMake-GUI, set source folder and build folder.</li>

  <li>Run <strong>Configure</strong>.</li>

  <li>A pop-up will ask you to specify the generator for the project.
    <ul>
      <li>If you want to use <strong>Visual Studio IDE</strong>, select <code>Visual Studio 15 2017 Win64</code> or <code>Visual Studio 16 2019 Win64</code> (or without the <code>Win64</code> if you are on Windows 32-bit).</li>
      <li>If you want to use <strong>another IDE like QtCreator</strong>, select <code>CodeBlocks - Ninja</code> (recommended, needs <a href="#optional-ninja-build-system">Ninja</a>) or <code>CodeBlocks - NMake</code>.</li>
    </ul>
    Keep <code>Use default native compilers</code> and press <code>Finish</code>.
  </li>

  <li>Fix eventual dependency errors by following CMake messages (see Troubleshoot section below). You may ignore warnings.
    <ul>
      <li>e.g. define the <code>Eigen3_DIR</code> with the path where you installed Eigen</li>
      <li>Add the path to your venv site-packages to CMake by setting a path variable called <code>CMAKE_PREFIX_PATH=C:\path\to\sofa-venv\Lib\site-packages</code></li>
    </ul>
  </li>

  <li>(optional) Customize SOFA via CMake variables
    <ul>
      <li>choose the build type by setting <code>CMAKE_BUILD_TYPE</code> to <code>Release</code> or <code>RelWithDebInfo</code> (recommended) or <code>Debug</code></li>
      <li>activate or deactivate plugins: see <code>PLUGIN_XXX</code> variables</li>
      <li>activate or deactivate features: see <code>SOFA_XXX</code> variables</li>
    </ul>
    Do not forget to <strong>Configure</strong> again to check if your changes are valid.<br>
    <em>NOTE</em>: here is an <a href="../activate-plugins/">exhaustive list of plugins</a> that can be activated for an in-tree compilation.
  </li>

  <li>When you are ready, run <strong>Generate</strong>. In the build directory, this will create a Visual Studio project (<code>.sln</code>) or a Makefile depending on the generator you chose at step 4.</li>
</ol>

<h3>Compile</h3>
To build SOFA in Visual Studio, simply <strong>open the generated Sofa.sln</strong>. Finally, <strong>build the solution</strong> using the Visual Studio interface as shown in the image below:<br>
<img src="https://www.sofa-framework.org/wp-content/uploads/2019/03/build-visual.png" alt="Build Visual">

If you chose another generator you will have to run the generator from the build directory.

<h4>Example with Ninja:</h4>
<ul>
  <li>In Windows Start menu, search for <code>Native Tools Command Prompt</code> and run the one corresponding to your Windows architecture (x64 for 64-bit, x86 for 32-bit).</li>
  <li>Go to the build directory with <code>cd</code></li>
  <li>Run <code>ninja</code></li>
</ul>
Time for a coffee!

<h3>Setup script</h3>
To simplify the configuration of our continuous integration machines, we created a complete set of setup scripts.<br>

These scripts install a lot of software directly in <code>C:\</code> without any preliminary check.
It is meant to be used on a <strong>fresh Windows</strong>. We use it on disposable virtual machines only.<br>

Setup script: <a href="https://github.com/sofa-framework/ci/blob/master/setup/">I am aware of the disclaimer above</a>.
<strong>WARNING: USE AT YOUR OWN RISKS</strong>

The two scripts <code>setup-windows_1.bat</code> and <code>setup-windows_2.bat</code> install the minimum set of requirements.

<h3>Compilation tutorial</h3>
See our page presenting <a href="../../video-tutorials/how-to-compile-sofa/#windows">video tutorial for compilation on Windows</a>.

</details>


# Run SOFA

## with the SOFA GUI
To run SOFA, locate and execute the application called `runSofa`. For more detailed information on how to use the application, you can refer to the [page dedicated to runsofa](../../../using-sofa/runsofa/). This documentation will provide you with further guidance on using SOFA effectively.


## within a Python environment

To use SOFA within a Python3 environment, the section "using Python3" details how to [set up your environment on various operating systems](https://sofapython3.readthedocs.io/en/latest/content/Installation.html#using-python3).


