Write an XML scene
==================

Now let's take a look at the scene file. Scene files are XML files that
describes the scene graph for the simulation. By convention, scene files
have extension ".scn". You can find example scenes in the
%{SOFA\_DIR}/examples/Demo/ folder. This is where you will find the
"caduceus.scn".

As you can see, the content of a scene file is written in XML.

To create the simulation tree, you need to create a scene graph using
the XML format. XML is a very simple language that allows the
hierarchical description of a graph. Each element contained between
chevrons are called "Tags". There are 2 types of tags: Nodes, and
Leaves.

In terms of simulation, the **Node** tag is used to create a
hierarchical level of modeling (e.g. behavior model, collision model,
visual model etc.). A scene file **always** contains a root node, that
encapsulates your whole graph, and defines some overall specificities
for your simulation (e.g. gravity, dt, ...):

```xml
<Node name="root" gravity="0 -1000 0" dt="0.04">
    <Node name="Snake">
        <!-- some XML code -->
    </Node>
    <Node name="Collis">
        <!-- some collision-specific code -->
    </Node>
    <Node name="VisuBody" tags="Visual" >
        <!-- some rendering-specific code -->
    </Node>
    <!-- some more code... -->
    <Node name="Base">
        <!-- some more code... -->
    </Node>
</Node>
```

Nodes can be **nested**, as it is the case with every nodes inside the
root node, allowing you to separate the different parts of your scenes.
Nodes by themselves though, are useless, unless you combine them with
some of the large collection of components available in SOFA. Those
components are "leaves", meaning that they cannot be nested. Leaves,
**must** be contained inside the root node, or any other nodes in the
scene graph.

XML properties: SOFA's data and links
-------------------------------------

As you can see in the scene file, nodes and components can have
properties. In SOFA, xml properties are called Data, and allows you to
access, and change some properties of the component it belongs to. This
way for instance, a node can be activated or deactivated by setting its
boolean data field **activated** to "true" or "false". Those data are
the same parameters that you can find and modify in the "property" sheet
of runSofa's interface.

```xml
<Node name="Snake" activated="true" >
    <!-- some code -->
</Node>
```

[![Node Property
Sheet](https://www.sofa-framework.org/wp-content/uploads/2014/11/Screenshot-from-2014-11-26-1716591.png){.wp-image-1035
width="277"
height="366"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/Screenshot-from-2014-11-26-1716591.png)

Moreover, dependency between Data containers of same nature can be
speciﬁed in the XML scene ﬁles, indicating that the content of one
container should be copied from the other, making the scene description
fairly simple and above all efﬁcient. To create this dependency, the
flag "@" follow by the name of the source component should be used, as
in following example:

```xml
<Node name="myNode">
    <MeshOBJLoader name="myLoader" filename="mesh.obj"/>
    <MeshTopology name="myMesh" src="@myLoader"/>
</Node>
```

The example above links the whole component "myLoader" to the property
"src" of the component "myMesh". But it is also possible to link more
specifically the data of a component to the data of another one, again,
as long as those data are of the same type:

```xml
<Node name="root" gravity="0 -1000 0" dt="0.04">
    <Node name="Loader">
        <MeshVTKLoader name="vtkLoader" filename="liver"/>
    </Node>
    <Node name="MechanicalModel">
        <MechanicalObject name="liverMO" scale="1" position="@../Loader/vtkLoader.position"/>
    </Node>
</Node>
```

The example above also shows the possibility to link to a component
located in another node. Here, the component vtkLoader is not located
in the same node as the mechanical object component. by using
"../Loader/" before component's name we want to link with, we are going
up from one node, search for the "Loader" node, look for the component
"vtkLoader" in it, and finally link with its data labeled "position"

Important note: It is not possible to link to a component that has not
been yet declared in the scenegraph. In other words, a component in the
XML file only knows about the components declared earlier in the file.

Split your scene graph into multiple files
------------------------------------------

It is possible to include other xml files inside your scn file. This
allows you to fragment your code to get a clearer and cleaner view of
your scene. This can be achieved using the tag. For instance, the
"caduceus.scn" could look like this:

```xml
<Node name="root" gravity="0 -1000 0" dt="0.04">
    <VisualStyle displayFlags="showVisual  "/> <!--showBehaviorModels showCollisionModels-->
    <LCPConstraintSolver tolerance="1e-3" initial_guess="false" build_lcp="false"  printLog="0" mu="0.2"/>
    <FreeMotionAnimationLoop/>
    <CollisionPipeline depth="15" verbose="0" draw="0"/>
    <BruteForceBroadPhase name="N2"/>
    <BVHNarrowPhase />
    <MinProximityIntersection name="Proximity" alarmDistance="1.5" contactDistance="1"/>
    <LightManager/>
    <SpotLight name="light1" color="1 1 1" position="0 80 25" direction="0 -1 -0.8" cutoff="30" exponent="1"/>
    <SpotLight name="light2" color="1 1 1" position="0 40 100" direction="0 0 -1" cutoff="30" exponent="1"/>
    <CollisionResponse name="Response" response="FrictionContactConstraint"/>

    <Node name="Snake">
        <include href="snake.scn"/>
    </Node>

    <Node name="Base" >
        <include href="base.scn"/>
    </Node>
</Node>
```

You would have the rest of the scene graph declared in two other files:

-   snake.scn, containing the snake's graph
-   base.scn, containing the pod's graph

