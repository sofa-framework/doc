---
title: runSofa with Qt
---



### How to use the SOFA GUI (Qt)

To start the simulation, press **Animate** - the simulation speed in
frames per second (fps) and the advancement of the simulation time in
seconds (s) will show up in the left bottom corner. If there is a need
for a simulation with a lower or higher detail of the time, then adapt
the parameter **dt.** A stepwise advancing of the simulation with the
stepsize **dt** can be achieved by clicking on "Step". In order to restart
the scene use "Reset Scene". The camera of the visualization on the
right hand side of the executable is controlled by the mouse movement
and the:

-   **left mouse button** to change the rotation of the camera
-   **right mouse button** to translate the camera
-   **middle mouse button** to zoom in and out.

The camera position and orientation can be saved and recovered using the
**Save View** and **Reset View** buttons respectively. A running simulation
can be manipulated with the mouse movement, when clicking on the **left
mouse button** and pressing the **shift** key. Further uses of the keyboard can be found in
the tab "Viewer":

-   **B:** TO CHANGE THE BACKGROUND
-   **C:** TO SWITCH INTERACTION MODE: press the KEY C. Allow or not the
    navigation with the mouse.
-   **O:** TO EXPORT TO .OBJ The generated files scene-time.obj and
    scene-time.mtl are saved in the running project directory
-   **P:** TO SAVE A SEQUENCE OF OBJ Each time the frame is updated an
    obj is exported
-   **R:** TO DRAW THE SCENE AXIS
-   **S:** TO SAVE A SCREENSHOT The captured images are saved in the
    running project directory under the name format capturexxxx.bmp
-   **T:** TO CHANGE BETWEEN A PERSPECTIVE OR AN ORTHOGRAPHIC CAMERA
-   **(Shift+) V:** TO SAVE A VIDEO. See the part on *Video Recording*
   
-   **Esc:** TO QUIT ::sofa::

### Video recording
#### Frames
By default, Video recording consists in dumping each frame of rendering (so even if the simulation is paused, it will record if you are moving the camera) in PNG (lossless). All frames are recorded in *%{SOFA\_DIR}/share/screenshots*. If the folder does not exist, it needs to be created. If you wish to make a video with those images, you can use your favorite encoder (ffmpeg, libavi...).
After pressing the **"V"** key in your interface, you should see something like that:
```shell
[INFO]    [QtViewer] Saved 782x598 screen image to C:/Work/sofa/build/sandbox/screenshots/caduceus_00000001.png
[INFO]    [QtViewer] Saved 782x598 screen image to C:/Work/sofa/build/sandbox/screenshots/caduceus_00000002.png
....
```
And the dumped PNG files will be located in the designated folder.
Dumping will be stopped either if you quit the process, or press **"V"** again.

#### Video

You can choose instead to directly record a video using an external ffmpeg executable. This is not really recommended as you will not have a total control on the input, contrary to the previous way, i.e. dump frames + using your own tool with your options.

If it is still okay for you, you will need first to download **ffmpeg** on your system and tell SOFA its location by different means:
1. you set your system PATH with ffmpeg inside (it will the best choice for the Linux users)
2. you put ffmpeg(.exe) directly alongside runSofa (easiest solution)
3. you set the directory where ffmpeg is. Edit *%{SOFA\_DIR}/plugins/SofaGuiQt/etc/SofaGuiQt.ini* and set the value of **FFMPEG_EXEC_PATH**

Then in the interlace, you need to select the choice of writing directly a video file (***Menu->Edit->Video Recorder Manager***)
![](https://raw.githubusercontent.com/sofa-framework/doc/master/images/usingSOFA/videorecordmenu.png)
If everything is OK, you should see that in your console, when pressing the **"V"** key:
```shell
Start recording to C:/Work/sofa/build/sandbox/screenshots/caduceus__r60_0001.mp4 ( yuv420p, 60 FPS, 5120000 b/s) using ffmpeg.exe
ffmpeg version 4.4-full_build-www.gyan.dev Copyright (c) 2000-2021 the FFmpeg developers
  built with gcc 10.2.0 (Rev6, Built by MSYS2 project)
  ...
  frame=  132 fps= 25 q=-1.0 Lsize=     727kB time=00:00:02.15 bitrate=2771.1kbits/s speed=0.412x
```
When you wish the finish, press **"V"** again and ffmpeg should close the file.
```shell
...
[libx264 @ 000001fc48715700] ref B L1: 97.7%  2.3%
[libx264 @ 000001fc48715700] kb/s:2697.25
C:/Work/sofa/build/sandbox/screenshots/caduceus__r60_0001.mp4 written
```
and can obtain your video in the *%{SOFA\_DIR}/share/screenshots*.


