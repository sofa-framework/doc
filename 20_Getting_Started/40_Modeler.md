What is the Modeler ?
---------------------

The Modeler is a graphic tool using Qt, designed to ease the creation of
scenes for Sofa, and also to provide information of all the contents
available, and how to use them. It allows you to dynamically
create/remove/configure components inside the Sofa scene graph, and
launch the Sofa application to see directly what behaviour you get. Once
you are satisfied, you can save your scene graph to a xml file, and use
it later within Sofa.

Scene Graph
-----------

-   Load all .scn files, display their scene graph, and allow you to
    modify each component
-   Launch the scene currently being built in Sofa, directly from the
    Modeler (using runSofa in the main menu, or CTRL+R)
-   Presets: this is one of the most useful feature, we'll go more into
    details later, but basically, it allows someone with absolutly no
    knowledge of Sofa to create a deformable/rigid body using a 3D mesh,
    in only 3 clicks!

\[caption id="attachment\_1060" align="aligncenter"
width="500"\][![ModelerSceneGraph](https://www.sofa-framework.org/wp-content/uploads/2014/11/ModelerSceneGraph1.png){.wp-image-1060
width="500"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/ModelerSceneGraph1.png)
The scene graph\[/caption\] Click to enlarge the three steps:
\[one\_third\]\[responsive\][![Modeler1](https://www.sofa-framework.org/wp-content/uploads/2014/11/Modeler11.png){.alignnone
.size-full .wp-image-1065 width="1008"
height="627"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/Modeler11.png)\[/responsive\]\[/one\_third\]\[one\_third\]\[responsive\][![Modeler2](https://www.sofa-framework.org/wp-content/uploads/2014/11/Modeler21.png){.alignnone
.size-full .wp-image-1066 width="1008"
height="627"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/Modeler21.png)\[/responsive\]\[/one\_third\]\[one\_third\_last\]\[responsive\][![Modeler3](https://www.sofa-framework.org/wp-content/uploads/2014/11/Modeler3.png){.alignnone
.size-full .wp-image-1067 width="1008"
height="627"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/Modeler3.png)\[/responsive\]\[/one\_third\_last\]

Library
-------

-   Display all the components available in SOFA: in the left part of
    the application, you can find a library of components, sorted into
    categories
-   Filter the components using a keyword: entering the text Triangle in
    the filter zone will reduce the library to the only components
    containing the word Triangle in their name.

Documentation
-------------

-   Inheritance
-   Description
-   Namespace
-   Authors
-   Licence
-   some examples scenes. They are displayed as links, by clicking on
    them, you directly open them inside the Modeler: simply press CTRL+R
    and you test the scene.

Flexibility
-----------

-   Each component of the library is a button: by drag&dropping them in
    a node of the scene graph, you actually add it to the simulation.
    -   First Click on the component,
    -   Keep the mouse button down, move your cursor at the place where
        your want to place your new component
    -   If you drop (release the mouse button) above a node, the
        component will be placed after all the current Sofa component of
        the node
    -   If you drop above a component, it will be placed above
        this component.
-   Save the scene or a node
-   Copy/Paste of a node or a component
-   Delete a component or a node from the scene graph by pressing DEL
-   Undo/Redo
-   Error detection: errors on template are automatically detected and
    displayed to the user.

The goal of the Modeler is to turn you ACTIVE in the understanding of
Sofa. Try any scene you want, modify the components, add some, delete
others, then CTRL+R, and you try it in SOFA. You don't need anymore to
know by heart the name of all the components, and their parameters, just
drag&drop them from the library to the scene graph, and edit them. This
can be done, just like inside the SOFA main application by
double-clicking on the component in the scene graph.

#### TIP \#1 : Add a link to an example scene in the Modeler

To have an example linked inside the Modeler, you have to create a .scn
file with the exact same name as your component. It must be placed in
examples/Components and a subdirectory corresponding to its base class
(forcefield, constraint, ...)

#### TIP \#2 : Graphic Documentation of a special Scene

To pop-up a small documentation of a scene, when loaded in Sofa, you
need to create a .html file, with the same name as your .scn file. An
example can be found for examples/Demos/chainHybridNoGroup.scn.
