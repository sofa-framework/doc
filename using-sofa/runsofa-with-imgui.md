---
title: runSofa with ImGui
---

## SofaGLFW

[![Gitter](https://img.shields.io/badge/chat-on_Gitter-ff69b4.svg)](https://app.gitter.im/#/room/#sofa-framework_sofa:gitter.im)
[![Support](https://img.shields.io/badge/support-on_GitHub_Discussions-blue.svg)](https://github.com/sofa-framework/sofa/discussions/categories/sofaglfw-imgui)

![download](https://img.shields.io/github/downloads/sofa-framework/SofaGLFW/total.svg)
![forks](https://img.shields.io/github/forks/sofa-framework/SofaGLFW.svg)
![stars](https://img.shields.io/github/stars/sofa-framework/SofaGLFW.svg)

This SOFA plugin brings a simple GUI based on GLFW (a spiritual successor of Glut).

It only needs Sofa.Simulation.Graph, Sofa.Component.Visual, Sofa.GUI.Common and Sofa.GL as dependencies.
Integration of GLFW is automatic (automatic fetching and integration with CMake), and linked statically (does not need a glfw.dll to be shipped with)

This GUI is launchable with the standard runSofa (with the parameter "-g glfw"), or can be used with a (provided) stand-alone executable `runSofaGLFW` (which needs much less dependencies than runSofa)

Lastly, this GUI was designed to support multiple windows in the same time and multiple simulations. 

### Dependencies

#### Linux

Unix-like systems such as Linux need a few extra packages for GLFW. Read the documentation on the [GLFW website (section `Installing dependencies`)](https://www.glfw.org/docs/latest/compile_guide.html).
**For example**, if you are on Ubuntu running X11, you need to do:

```
sudo apt install xorg-dev
```

In case you want the video recording feature, make sure to also have installed the following dependencies:

```
sudo apt install libavcodec-dev libavformat-dev libavutil-dev libswresample-dev libswscale-dev
```

#### Others

No dependencies


### Compilation

As any plugin, to compile SofaGLFW, follow the instructions on the [SOFA documentation website](https://www.sofa-framework.org/community/doc/plugins/build-a-plugin-from-sources/).

### Keyboard Shortcuts

Several shortcuts are related to the window:
* F11: switch to fullscreen
* Escape: close the app
* Space: play/pause the simulation
* Any letter on your keyboard would result in a search in the scene graph

Using the control (CTRL) key, you activate GUI shortcuts such as:
* Ctrl+A: show the scene axis
* Ctrl+B: switch the background
* Ctrl+R: reload the current scene
* Ctrl+O: open a scene file

Using the SHIFT key, you activate the scene interactions such as the mouse interaction.

### Command Line Options

`runSofaGLFW` accepts the following command line options:
* `-f` or `--file` to specify the scene file to load. If not defined, the default scene file `Demos/caduceus.scn` is loaded.
* `-a` or `--start`: if true, starts the simulation just after opening. True by default.
* `-s` or `--fullscreen`: set full screen at startup. False by default.
* `-l` or `--load`: load given plugins as a comma-separated list. Example: -l SofaPython3

## Dear ImGui

By default, SofaGLFW does not show any user interface.
Only the keyboard allows limited interactions with the simulation.
That is why a user interface based on [Dear ImGui](https://github.com/ocornut/imgui) is provided, in the form of a SOFA plugin.

By default, this interface is not compiled.
The CMake variable `PLUGIN_SOFAIMGUI` must be set to `ON`.

Integration of Dear ImGui is automatic (automatic fetching and integration with CMake), and linked statically.

### Dependencies

SofaImGui depends on SofaGLFW, so it must also be activated.

The GUI relies on the [NFD-extended library](https://github.com/btzy/nativefiledialog-extended).
Therefore, it comes with its dependencies. See the list on [GitHub](https://github.com/btzy/nativefiledialog-extended#dependencies).

### Compilation

As any plugin, to compile SofaImGui, follow the instructions on the [SOFA documentation website](https://www.sofa-framework.org/community/doc/plugins/build-a-plugin-from-sources/).

### Usage

To run SOFA with the GUI from SofaImGui, execute the following command:

```bash
runSofa -l SofaImGui -g imgui
```

- `-l SofaImGui`: loads the plugin in order to be able to use the GUI (see the [documentation](https://www.sofa-framework.org/community/doc/plugins/what-is-a-plugin/))
- `-g imgui`: selects the `runSofa` GUI to be the one from SofaImGui

It is possible to run the Dear ImGui-based GUI by default when running the command `./runSofa` (without the `-l` and `-g` arguments). To do so, add the SofaImGui plugin into the list of loaded plugin in the `plugin_list.conf` file (see the [documentation](https://www.sofa-framework.org/community/doc/plugins/what-is-a-plugin/)). Then, run `runSofa -g imgui` at least once so that `runSofa` save the last used GUI. After that, `./runSofa` will load the imgui GUI.

### Windows

The GUI is based on dockable windows.
Each window gathers related features.
Here are all the available windows:

| Window            | Description                                                                      |
|-------------------|----------------------------------------------------------------------------------|
| __Performances__  | display simple metrics related to application performances: ms/frame, FPS, graph |
| __Profiler__      | display detailed metrics related to the physics loop performances                |
| __Scene Graph__   | show the scene graph and the Data associated to each components                  |
| __Display Flags__ | filter which components are rendered in the 3D view                              |
| __Plugin__        | show a list of plugins currently loaded                                          |
| __Components__    | show a detailed list of components currently loaded                              |
| __Log__           | all the messages sent by SOFA                                                    |

### Screenshots

![MainGUI](doc/screenshot.png)

### Custom GUI

The software allows for flexible extension of its GUI through custom windows.
Users can develop and integrate their own GUI components tailored to the needs of a specific simulation scene.
This makes it possible to build highly specialized controls, panels, or visualization tools that enhance or modify the user experience.

To help users get started, the built-in `SofaImGui.Camera` extension serves as a reference implementation.
It demonstrates how a custom window can be structured and integrated into the GUI framework.
Developers can use it as a foundation to build their own extensions, adapting it to different simulation contexts and requirements.

As any SOFA plugin, the custom GUI is available only if loaded (https://sofa-framework.github.io/doc/plugins/what-is-a-plugin/#plugin_loading).
