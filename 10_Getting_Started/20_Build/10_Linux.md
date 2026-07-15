SOFA policy is to support only the latest Ubuntu LTS.

# Installation with Pixi

You can download and build SOFA in only three steps without any environment installation.

## Prerequisites

- [Install Git](https://git-scm.com/install/linux)
- [Install Pixi](https://pixi.prefix.dev/latest/installation/)


## Installation steps

- Clone SOFA : `git clone https://github.com/sofa-framework/sofa` :inbox_tray: 
- Trigger the build : run `pixi run -e supported-plugins build` in the sofa source folder :desktop_computer: 
- Launch SOFA : run `pixi run -e supported-plugins runSofa` :rocket: 




# Alternative build methods


## Manual installation (for developpers)

<details>

<summary>This installation method is advised for developers. It is STRONGLY advised to read through this entire doc page before getting started.</summary>


<h3>Build tools</h3>

<h4>Compiler</h4>
SOFA requires a <a href="https://en.cppreference.com/w/cpp/compiler_support#C.2B.2B17_features">C++17 compatible compiler</a>.<br>
On Linux, we officially support <strong>GCC &gt;= 7</strong> and <strong>Clang &gt;= 5</strong>.

<h5>First, install the standard compilation toolkit:</h5>
<pre><code>sudo apt install build-essential software-properties-common</code></pre>

<h5>GCC</h5>
To know which GCC versions are available for your distribution, run this command:
<pre><code>apt-cache search '^gcc-[0-9.]+$'</code></pre>

Then, install the latest one with the usual command (example with gcc-11):
<pre><code>sudo apt install gcc-11</code></pre>

<h5>Clang</h5>
Clang is an <strong>alternative to GCC</strong>. It compiles approximately two times faster!<br>
We recommend to install <strong>Clang 5 or newer</strong>.

To know which Clang versions are available for your distribution, run this command:
<pre><code>apt-cache search '^clang-[0-9.]+$'</code></pre>

Then, install the latest one with the usual command (example with clang-12):
<pre><code>sudo apt install clang-12</code></pre>

<h4>CMake: Makefile generator</h4>
CMake will be required to configure the SOFA project before compiling it. Note that SOFA requires at least <strong>CMake 3.22</strong>.
<pre><code>sudo apt install cmake cmake-gui</code></pre>

<h4>[optional] Ninja: build system</h4>
Ninja is an alternative to Make. It has a better handling of incremental builds.
<pre><code>sudo apt install ninja-build</code></pre>

<h4>[optional] CCache: caching system</h4>
We advise you to use <a href="https://ccache.dev/">ccache</a>. It is by no means mandatory, but it will dramatically improve the compilation time if you make changes to SOFA.
<pre><code>sudo apt install ccache</code></pre>


<h3>Dependencies</h3>

<h4>Core (required)</h4>
SOFA requires some libraries:

<ul>
  <li><strong>tinyXML2</strong>
    <pre><code>sudo apt install libtinyxml2-dev</code></pre>
  </li>

  <li><strong>OpenGL</strong>
    <pre><code>sudo apt install libopengl0</code></pre>
  </li>

  <li><strong>Boost</strong> (&gt;= 1.65.1)
    <pre><code>sudo apt install libboost-all-dev</code></pre>
  </li>

  <li><strong>Python 3.12</strong> + pip + numpy + scipy
    <pre><code>sudo apt install python3.12-dev python3.12-venv</code></pre>
    Python 3.12 now favors the use of venv. We highly recommend it too. To bootstrap it, type <code>python3.12 -m venv sofa-venv</code> in the folder you want to keep this venv. We recommend creating it either in your home directory or in the folder containing both your sources and the build directory. Once created, you can activate it by calling <code>source /path/to/sofa-venv/bin/activate</code>. Now you can install all dependencies through the following commands:
    <pre><code>python3.12 -m pip install --upgrade pip \
&& python3.12 -m pip install numpy scipy pybind11==2.12.0</code></pre>
    Now, each time you want to build or use SOFA, you first need to call <code>source /path/to/sofa-venv/bin/activate</code> to activate this virtual environment and get access to the dependencies.
  </li>

  <li><strong>Additional libraries</strong>: libPNG, libJPEG, libTIFF, Glew, Zlib
    <pre><code>sudo apt install libpng-dev libjpeg-dev libtiff-dev libglew-dev zlib1g-dev</code></pre>
  </li>

  <li><strong>Eigen</strong> (&gt;= 3.2.10)
    <pre><code>sudo apt install libeigen3-dev</code></pre>
  </li>
</ul>

<h4>Graphical User Interface</h4>
The <a href="https://github.com/sofa-framework/SofaGLFW">SOFAGLFW</a> project is based on both <strong>GLFW</strong> and <strong>ImGui</strong> libraries. It requires the following dependencies to be installed:
<pre><code>sudo apt install xorg-dev libgtk-3-dev</code></pre>

<h4>Plugins (optional)</h4>
SOFA <strong>plugins</strong> depend on libraries that are available in the official repositories.<br>
You probably don't need them all, but you might find it convenient to install them all and not worry about it later.<br>
This list does not cover all available SOFA plugins, only the ones that are built by our continuous integration platform.

<ul>
  <li><strong>CGALPlugin</strong>
    <pre><code>sudo apt install libcgal-dev</code></pre>
  </li>
  <li><strong>SofaCUDA</strong><br>
    The currently supported CUDA version is 12.2
    <pre><code>sudo apt install nvidia-cuda-toolkit</code></pre>
  </li>
</ul>


<h3>Build SOFA</h3>

<h4>Setup your source and build directories</h4>
To set up clean repositories, we recommend arranging the SOFA directories as follows:
<pre><code>sofa/
├── build/
│   ├── master/
│   └── v26.06/
└── src/
    └── &lt; SOFA sources here &gt;</code></pre>

<strong>First</strong>, checkout the sources from the Git repository:

<h5>Get the current <strong>stable</strong> version on the v26.06 branch:</h5>
<pre><code>git clone -b v26.06 https://github.com/sofa-framework/sofa.git sofa/src</code></pre>

<h5><strong>OR</strong> get the development <strong>unstable</strong> version on the master branch:</h5>
<pre><code>git clone -b master https://github.com/sofa-framework/sofa.git sofa/src</code></pre>


<h4>Generate a Makefile with CMake</h4>
<ol>
  <li>Activate your venv:
    <pre><code>source /path/to/sofa-venv/bin/activate</code></pre>
    and tell CMake to look there to find pybind11:
    <pre><code>export CMAKE_PREFIX_PATH=/path/to/sofa-venv/lib/python3.12/site-packages</code></pre>
  </li>

  <li>Create build directories respecting the arrangement above.</li>

  <li>Run CMake-GUI and set source folder and build folder.</li>

  <li>Run <strong>Configure</strong>. A popup will ask you to specify the generator for the project.
    <ul>
      <li>If you installed <a href="#optional-ninja-build-system">Ninja</a>, select <code>Ninja</code>.</li>
      <li>Otherwise, select <code>Unix Makefile</code>.</li>
    </ul>
  </li>

  <li>Choose <code>Specify native compilers</code> and press <code>Next</code></li>

  <li>Set the C compiler to <code>/usr/bin/gcc</code> <strong>or</strong> <code>/usr/bin/clang</code><br>
      Set the C++ compiler to <code>/usr/bin/g++</code> <strong>or</strong> <code>/usr/bin/clang++</code>
  </li>

  <li>Run <strong>Configure</strong>.</li>

  <li>Fix eventual dependency errors by following CMake messages (see Troubleshoot section below). Do not worry about warnings.</li>

  <li>(optional) Customize SOFA via CMake variables
    <ul>
      <li>choose the build type by setting <code>CMAKE_BUILD_TYPE</code> to <code>Release</code> or <code>RelWithDebInfo</code> (recommended) or <code>Debug</code></li>
      <li>activate or deactivate plugins: see <code>PLUGIN_XXX</code> variables</li>
      <li>activate or deactivate functionalities: see <code>SOFA_XXX</code> variables</li>
    </ul>
    Do not forget to <strong>Configure</strong> again to check if your changes are valid.<br>
    <em>NOTE</em>: here is an <a href="../activate-plugins/">exhaustive list of plugins</a> that can be activated for an in-tree compilation.
  </li>

  <li>When you are ready, run <strong>Generate</strong>.</li>
</ol>


<h4>Compile</h4>
To compile, open a terminal in your build directory and run <code>make</code> or <code>ninja</code> depending on the generator you chose during CMake configuration.<br>
If you chose <code>Unix Makefile</code> as generator, you can enable parallel compilation by specifying the number of parallel builds you want by adding the <code>-j n</code> option with <code>n</code> being the number of desired parallel jobs.<br>
This is set automatically to the highest possible by <code>ninja</code>, but this can be modified in the same way as for <code>make</code>.

Time for a coffee!<br><br>
To get assistance, see our page presenting <a href="../../video-tutorials/how-to-compile-sofa/#linux">video tutorial for compilation on Linux</a> or use our <a href="https://github.com/sofa-framework/sofa/discussions/categories/build-config-environment">GitHub Discussion forum</a>.


</details>


## Preconfigured Docker image

We provide preconfigured Docker images based on Ubuntu or Fedora.  
These images contain all the tools and dependencies needed to build SOFA.  
Feel free to use them and to propose your own versions on Docker Hub!

Ubuntu image: [https://hub.docker.com/r/sofaframework/sofabuilder_ubuntu](https://hub.docker.com/r/sofaframework/sofabuilder_ubuntu)

Fedora image: [https://hub.docker.com/r/sofaframework/sofabuilder_fedora](https://hub.docker.com/r/sofaframework/sofabuilder_fedora)


## Nix package

[Nix](https://nix.dev/) is a package manager which stores all packages into a common place called the Nix store, usually located at /nix/store. Each package is stored in a unique subdirectory in the store, and each package has its own tree structure.

A Nix package for SOFA is available and can be used as follows:

- Install [Nix](https://nix.dev/install-nix), you can run `sh <(curl -L https://nixos.org/nix/install) --daemon`, restart your terminal or check the installation using `nix --version`
- From the SOFA sources, build using the command `nix build --extra-experimental-features nix-command --extra-experimental-features flakes` (for master). Note that you can point towards any commit hash: `nix build github:sofa-framework/sofa/COMMIT_HASH_HERE`
- Command `nix develop` provides a shell with an environment containing all required dependencies to build the project in the usual CMake way
- Finally, starts SOFA `nix run --impure .#nixgl --extra-experimental-features nix-command --extra-experimental-features flakes`


# Run SOFA

## with the SOFA GUI
To run SOFA, locate and execute the application called `runSofa`. For more detailed information on how to use the application, you can refer to the [page dedicated to runsofa](../../../using-sofa/runsofa/). This documentation will provide you with further guidance on using SOFA effectively.


## within a Python environment

To use SOFA within a Python3 environment, the section "using Python3" details how to [set up your environment on various operating systems](https://sofapython3.readthedocs.io/en/latest/content/Installation.html#using-python3).

