Installation the SofaPython plugin
----------------------------------

First, you need to have the python-2.7 library installed. After
installing and compiling SOFA, you have to:

-   re-run the cmake-gui
-   and activate the **SOFA-PLUGIN\_SOFAPYTHON** option, and configure,
-   Finally, recompile SOFA.

 

Test the plugin using examples
------------------------------

Once you activated the SofaPython plugin, you can test the compilation
using the examples available in the folder of *SofaPython/examples/*.
For example, start the fontain.scn scene:

    runSofa applications/plugins/SofaPython/examples/fontain.scn

This scene creates particles from the associated Python script
(fontain.py). Here is a preview of the working scene. \[caption
id="attachment\_1688" align="aligncenter" width="600"\][![Screenshot of
the scene
fontain.scn](https://www.sofa-framework.org/wp-content/uploads/2014/11/Screenshot-from-2015-01-20-183338.png){.wp-image-1688
width="600"
height="425"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/Screenshot-from-2015-01-20-183338.png)
Screenshot of the scene fontain.scn\[/caption\]  

Write your own python !
-----------------------

#### From scratch

**<span style="text-decoration: underline;">In your scene</span>**, if
you want to use Python in one of your scene (fontain.scn), you need:

-   in the first place add the plugin in the scene using the
    **RequiredPlugin**,
-   and define a **PythonScriptController** in the scene graph.

Most of the time, this PythonScriptController is placed inside the root
node as illustrated in the example "fontain.scn" below:


        ...

The core of this plugin is the Sofa Python module available to python
scripts from within the SofaPython components (they are not available
outside Sofa environment, in the command-line python binary for
example). **<span style="text-decoration: underline;">Any python
script</span>** (fontain.py) embedded in SOFA should include the
following line if it wants to interact with the SOFA framework:

    import sofa

SofaPython provides several module methods, for general purpose (not
linked to a particular node or component). For example:

-   *createGraph()*: allows to access the time at which the graph is
    created,
-   *reset()*: when the scene is reset
-   *onKeyPressed()*: allows to recover any user interaction, for
    example with the keyboard,
-   and many other functions.

The following small example gives an idea on the various possibilities
of the sofa python plugin. In any of the module methods (presented
above), you can:

-   have access to a node (here in the function initGraph):

        def initGraph(self,node):
                print 'the name of the node is'+node.name
                self.root = node

-   interactively create new components with specific parameters in the
    node:

        def initGraph(self,node):
                print 'the name of the node is'+node.name
                self.root = node
                myLoader = self.root.createObject('CGLinearSolver',iterations=25,tolerance=1.0e-9,threshold=1.0e-9)

-   even access an existing component (named 'MecaObject') in the node:

        def initGraph(self,node):
                print 'the name of the node is'+node.name
                self.root = node
                self.myMecaObject = node.getObject('MecaObject')

-   and access/modify its properties:

        def initGraph(self,node):
                print 'the name of the node is'+node.name
                self.root = node
                self.myMecaObject = node.getObject('MecaObject')
                # Access data
                print 'my positions are : '+self.myMecaObject.findData('position').value
                # Modify data
                self.myMecaObject.findData('position').value=str(x)+' '+str(y)+' '+str(z)+' 0 0 0 1'

You see ! Python is unlimited !!  

#### Translate an existing scene in a python script

In the Python plugin in SOFA, you will find an executable
**./createPythonScene.py** which allows to translate an existing scene
(e.g. myExample.scn) into a new SOFA scene (e.g. myExamplePython.scn)
calling a python script (e.g. myExamplePython.py). This is very useful
since it generates a script with ALL possible functions that you can use
in SOFA such as *init()*, *handleEvent()*, *onKeyPressed()* an so on.
Optional arguments:

      -h, --help      show this help message and exit
      -n [N]          node to replace by python script, if N the complete scene is
                      replaced by a python script (default: None)
      -o [O [O ...]]  filename(s) of the transformed scene(s) (default: None)
      --py            output only a .py file (default: 0)

The created scene (e.g. myExamplePython.scn) is actually empty and only
includes a PythonScriptController in the scene. This controller then
uses the information of the created script (e.g. myExamplePython.py) to
define the scene, its components, etc. **More informations** about the
plugin itself can be found in
*sofa/applications/plugins/SofaPython/doc/SofaPython.pdf*.
