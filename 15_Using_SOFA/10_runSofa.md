### runSOFA

The default compilation of SOFA produces a binary file called **runSofa**, which can be
found in the folder *%{SOFA\_BUILD\_DIR}/bin*.
The execution of the binary - either via the terminal or by double-clicking the executable -
launches a default [XML scene](./../create-your-scene-in-xml) with the name caduceus.scn, using the Qt library.
![Execution of runSofa using the
default scene caduceus](https://www.sofa-framework.org/wp-content/uploads/2014/11/Screenshot-from-2015-01-14-1839152.png)

### Launch runSOFA

The binary **runSofa** can be launched with different options, that can
be enabled through the command line. You can display the different
options available by using the argument ‘-h’ in the command line:
`runSofa -h`
We obtain the following output:
```
This is a SOFA application. Here are the command line arguments (short name, long name, description, default value)
    -h, --help: this help 
    -a, --start: start the animation loop  (default: false ) 
    -c, --computationTimeSampling: Frequency of display of the computation time statistics, in number of animation steps. 0 means never.  (default: 0 ) 
    -g, --gui: choose the UI (batch|glut|glut-mt|qglviewer|qt)  (default:  ) 
    -l, --load: load given plugins  (default: ) 
    -n, --nb_iterations: (only batch) Number of iterations of the simulation  (default: 1000 ) 
    -p, --factory: print factory logs  (default: false ) 
    -r, --recent: load most recently opened file  (default: false ) 
    -s, --simu: select the type of simulation (bgl, dag, tree, smp)  (default: tree ) 
    -t, --temporary: the loaded scene won't appear in history of opened files  (default: false ) 
    -v, --verification: load verification data for the scene  (default:  ) others: file names`
```
When getting started with **runSofa**, the following options might be
valuable for you:

**-a:** **runSofa** starts the animation directly (no need to press on the animate button)

**-c:** Displays interesting statistics about the computation time of the simulation. It is very useful to analyse the performance of your simulation, or to benchmark a plugin developed for SOFA. The value that follows the argument determines the number of simulation steps to wait for before dumping the statistics (-c 10 will display the logs every 10 simulation steps)

**-g** allows you to choose between the existing user interfaces developed in SOFA:
- **qglviewer**: default interface using Qt and with a 3D view using QGLViewer
- **qt**: same but with an alternative viewer based on Qt only
- **batch:** command line interface (only displays statistics)

**-l** allows you to load a SOFA plugin by specifying its name

**-n** specifies the number of simulation steps to run before closing **runSofa**. Can only be used with **–g batch**.

If using the shipped binaries of SOFA (or the default CMake options when compiling), the default GUI will be based on Qt/QGLViewer (same as using **–g qglviewer**).

### Load and run a specific scene

The default scene loaded by **runSofa** is named “caduceus.scn”. This
scene file can be found in *%{SOFA\_SOURCE\_DIR}/examples/Demos*, along
with other demo scenes. Let us see now how to load one of these scenes:

-   From the **runSofa** interface, you can select a scene file through
    the “File-&gt;Open” Menu (Ctrl+O), and run it by simply pressing the
    "animate" button.
-   If you are launching **runSofa** from the command line, you can also
    specify the scene file to load as an argument.


