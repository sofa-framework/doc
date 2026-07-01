SOFA policy is to support only the latest MacOS version.

# Installation with Pixi

You can download and build SOFA in only three steps without any environment installation.

## Prerequisites

- [Install Git](https://git-scm.com/install/mac)
- [Install Pixi](https://pixi.prefix.dev/latest/installation/)


## Installation steps

- Clone SOFA : `git clone https://github.com/sofa-framework/sofa` :inbox_tray: 
- Trigger the build : run `pixi run -e supported-plugins build` in the sofa source folder :desktop_computer: 
- Launch SOFA : run `pixi run -e supported-plugins runSofa` :rocket: 

⚠️ A known issue under macOS has been hotfixed in the pixi build using a patch. _You don't need to do anything while using pixi, it is applied for you_. FYI, the issue appeared through the use of Python from runSofa with SofaPython3 and caused a segmentation fault due to symbol duplication (the Python package from Conda Forge statically linked with libpython, conflicting with runSofa’s own linking). The patch (proposed in PR [#394](https://github.com/sofa-framework/SofaPython3/pull/394)) is currently used in our Conda packages.


# Manual installation (for developpers)

<details>

<summary>This installation method is advised for developers. It is STRONGLY advised to read through this entire doc page before getting started.</summary>

<h2>Build tools</h2>

<h3>Compiler</h3>
SOFA requires a <a href="https://en.cppreference.com/w/cpp/compiler_support#C.2B.2B17_features">C++17 compatible compiler</a>.<br>
On MacOS, we officially support <strong>MacOS &gt;= 10.13.2 (High Sierra)</strong> and <strong>AppleClang &gt;= 9.1.0</strong>.

Check your MacOS version with <code>system_profiler SPSoftwareDataType</code><br>
Check your AppleClang version with <code>clang --version</code>

If your MacOS version is too low, update your Mac from the App Store.

If your AppleClang version is too low:
<ol>
  <li>Download and install the highest possible Xcode compatible with your MacOS.<br>
    Compatibility list (taken from <a href="https://en.wikipedia.org/wiki/Xcode#Version_comparison_table">Wikipedia</a>):
    <pre><code>MacOS &gt;= 11.3    : Xcode 13.2.1 (with AppleClang 13.0.0)
MacOS &gt;= 11.0    : Xcode 12.5.1 (with AppleClang 12.0.5)
MacOS &gt;= 10.15.4 : Xcode 12.4   (with AppleClang 12.0.0)
MacOS &gt;= 10.15.2 : Xcode 11.7   (with AppleClang 11.0.3)
MacOS &gt;= 10.14.4 : Xcode 11.3.1 (with AppleClang 11.0.0)
MacOS &gt;= 10.14.3 : Xcode 10.3   (with AppleClang 10.0.1)
MacOS &gt;= 10.13.6 : Xcode 10.1   (with AppleClang 10.0.0)
MacOS &gt;= 10.13.2 : Xcode 9.4.1  (with AppleClang  9.1.0)</code></pre>
    To download any version, go to <a href="https://developer.apple.com/download/more/">https://developer.apple.com/download/more/</a> and search for "Xcode".
  </li>
  <li>Open Xcode to automatically finalize installation</li>
  <li>In Xcode, navigate to "Xcode &gt; Preferences &gt; Locations" and set Command Line Tools to your Xcode version</li>
  <li>Verify Command Line Tools path: <code>xcode-select -p</code><br>
    If it is not pointing to your Xcode, change it: <code>xcode-select --switch /Applications/Xcode.app</code>
  </li>
  <li>Reboot</li>
</ol>


<h3>CMake: Makefile generator</h3>
SOFA requires at least <strong>CMake 3.22</strong>.
<pre><code>brew install --cask cmake</code></pre>


<h3>[optional] Ninja: build system</h3>
Ninja is an alternative to Make. It has a better handling of incremental builds.
<pre><code>brew install ninja</code></pre>


<h3>[optional] CCache: caching system</h3>
We advise you to use <a href="https://ccache.dev/">ccache</a>. It is by no means mandatory, but it will dramatically improve the compilation time if you make changes to SOFA.
<pre><code>brew install ccache</code></pre>


<h2>Dependencies</h2>

<h3>Core (required)</h3>
SOFA requires some libraries:

<ul>
  <li><strong>tinyXML2</strong>
    <pre><code>brew install tinyxml2</code></pre>
  </li>

  <li><strong>Boost</strong> (&gt;= 1.65.1)
    <pre><code>brew install boost</code></pre>
  </li>

  <li><strong>Python 3.12</strong> + pip + numpy + scipy
    <pre><code>brew install python@3.12
brew link --force python@3.12</code></pre>
    Python 3.12 now favors the use of venv. We highly recommend it too. To bootstrap it, type <code>python3.12 -m venv sofa-venv</code> in the folder you want to keep this venv. We recommend creating it either in your home directory or in the folder containing both your sources and the build directory. Once created, you can activate it by calling <code>source /path/to/sofa-venv/bin/activate</code>. Now you can install all dependencies through the following commands:
    <pre><code>python3.12 -m pip install --upgrade pip \
&& python3.12 -m pip install numpy scipy pybind11==2.12.0</code></pre>
    Now, each time you want to build or use SOFA, you first need to call <code>source /path/to/sofa-venv/bin/activate</code> to activate this virtual environment and get access to the dependencies.
  </li>

  <li><strong>Additional libraries</strong>: libPNG, libJPEG, libTIFF, Glew
    <pre><code>brew install libpng libjpeg libtiff glew</code></pre>
  </li>

  <li><strong>Eigen</strong> (&gt;= 3.2.10)
    <pre><code>brew install eigen</code></pre>
  </li>
</ul>


<h3>Plugins (optional)</h3>
SOFA <strong>plugins</strong> depend on libraries that are available in the official repositories.<br>
You probably don't need them all, but you might find it convenient to install them all and not worry about it later.<br>
This list does not cover all available SOFA plugins, only the ones that are built by our continuous integration platform.

<ul>
  <li><strong>CGALPlugin</strong>
    <pre><code>brew install cgal</code></pre>
  </li>
  <li><strong>SofaCUDA</strong>
    <pre><code>brew install homebrew/cask-drivers/nvidia-cuda</code></pre>
  </li>
</ul>


<h2>Build SOFA</h2>

<h3>Setup your source and build directories</h3>
To set up clean repositories, we recommend arranging the SOFA directories as follows:
<pre><code>sofa/
├── build/
│   ├── master/
│   └── v25.12/
└── src/
    └── &lt; SOFA sources here &gt;</code></pre>

<strong>First</strong>, checkout the sources from the Git repository:

<h4>Get the current <strong>stable</strong> version on the v25.12 branch:</h4>
<pre><code>git clone -b v25.12 https://github.com/sofa-framework/sofa.git sofa/src</code></pre>

<h4><strong>OR</strong> get the development <strong>unstable</strong> version on the master branch:</h4>
<pre><code>git clone -b master https://github.com/sofa-framework/sofa.git sofa/src</code></pre>


<h3>Generate a Makefile with CMake</h3>
<ol>
  <li>Activate your venv:
    <pre><code>source /path/to/sofa-venv/bin/activate</code></pre>
    and tell CMake to look there to find pybind11:
    <pre><code>export CMAKE_PREFIX_PATH=/path/to/sofa-venv/lib/python3.12/site-packages</code></pre>
  </li>

  <li>Create build directories respecting the arrangement above.</li>

  <li>Run CMake.app and set source folder and build folder.</li>

  <li>Run <strong>Configure</strong>. A popup will ask you to specify the generator for the project.
    <ul>
      <li>If you installed <a href="#optional-ninja-build-system">Ninja</a> (recommended), select <code>CodeBlocks - Ninja</code>.</li>
      <li>Otherwise, select <code>CodeBlocks - Unix Makefile</code>.</li>
    </ul>
  </li>

  <li>Keep <code>Use default native compilers</code> and press <code>Done</code>.</li>

  <li>Fix eventual dependency errors by following CMake messages (see Troubleshoot section below). Do not worry about warnings.</li>

  <li>Customize SOFA via CMake variables
    <ul>
      <li>choose the build type by setting <code>CMAKE_BUILD_TYPE</code> to <code>Release</code> or <code>RelWithDebInfo</code> (recommended) or <code>Debug</code></li>
      <li>if your Mac has a M1 processor: set <code>CMAKE_OSX_ARCHITECTURES</code> to <code>arm64</code></li>
      <li>activate or deactivate plugins: see <code>PLUGIN_XXX</code> variables</li>
      <li>activate or deactivate functionalities: see <code>SOFA_XXX</code> variables</li>
    </ul>
    Do not forget to <strong>Configure</strong> again to check if your changes are valid.<br>
    <em>NOTE</em>: here is an <a href="../activate-plugins/">exhaustive list of plugins</a> that can be activated for an in-tree compilation.
  </li>

  <li>When you are ready, run <strong>Generate</strong>.</li>
</ol>


<h3>Compile</h3>
To compile, open a terminal in your build directory and run <code>make</code> or <code>ninja</code> depending on the generator you chose during CMake configuration.<br>
Do not forget the <code>-j</code> option to use all your CPU cores.

Time for a coffee!

</details>



# Run SOFA

## with the SOFA GUI
To run SOFA, locate and execute the application called `runSofa`. For more detailed information on how to use the application, you can refer to the [page dedicated to runsofa](../../../using-sofa/runsofa/). This documentation will provide you with further guidance on using SOFA effectively.


## within a Python environment

To use SOFA within a Python3 environment, the section "using Python3" details how to [set up your environment on various operating systems](https://sofapython3.readthedocs.io/en/latest/content/Installation.html#using-python3).


