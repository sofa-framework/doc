Components implement most of the simulation methods. One can roughly
distinguish two categories of components: **Property** components
implement a facet of one object's physical properties, such as its mass,
stiffness, attachments. They are associated with a given simulated
object, and the C++ class is often templatized on the type of Degrees of
Freedom (DOF) of the object. The most important component of an object
is its MechanicalState, which contains the state vectors: positions,
velocities, and auxiliary vectors. **Control** components implement
high-level algorithms such as time integration and collision detection.
Most of them are not attached to a given object. They control all the
objects within their scope (their subgraph in the scenegraph) using
visitors which traverse the scenegraph to apply virtual functions.

## Base functions

A SOFA component is a class deriving from
**sofa::core::objectmodel::BaseObject**. This way, several virtual
methods are provided, and must be known in order to configure correctly
the behavior of your component:

#### init() and bwdInit()

When SOFA loads a simulation, its creates in C++, or directly using XML/Python
the SOFA Components (and the default constructor). At this stage, you
must initialize what we call **Data**, a component that you can find in
**sofa::core::objectmodel::Data**. The purpose of this utility class is
to store all the parameters of your component, and handle this way the
input (parametrize the component from XML/Python files for instance), and
output (save at a time T the configuration of your component).
Everything that needs to be saved in your component must be kept into
memory inside a Data (find out more about the [Data here](https://www.sofa-framework.org/community/doc/programming-with-sofa/api-overview/data-in-components/)).
Basically to initialize a data, you must do the following:

``` cpp
//Previous declaration of the Data
Data<bool> d_isEnabled;
//In Component constructor
MyComponent():
d_isEnabled(initData(&d_isEnabled, true, "isEnabled", "Boolean indicating if the component is enable"))) //ptr to the data, default value, name used for the parameter (the same that will appear later in the XML/Python file), description of the parameter (its purpose)
{
};
```

Once all the SOFA components of the scenes have been created, we launch
a Visitor to initialize the components. Basically a Visitor starts from
a node (for the InitVisitor, we start from the root), execute several
specific operations going top&#8594;down, and then another set of
operations going bottom&#8594;up. This is translated for the InitVisitor
by the call, each time we initialize a scene of two methods:

``` cpp
void init(); //call during Top->Down traversal
void bwdInit(); //call during Bottom->Up traversal
```

init() is called in each component of the graph (top&#8594;down) for initialization,
bwdInit() is called once all the children of a node has been initialized (bottom&#8594;up).
The methods init() and bwdInit() have been called for all the component
of the children nodes. Both method are virtual function from BaseObject
which can be overriden in any component.

#### reinit()

The reinit() method is automatically call reinit() when you
edit a component in the GUI of SOFA:

``` cpp
void reinit();
```

#### cleanup() and reset()

These methods are called each time you want to reset a scene: first
cleanup will be called, then reset.

- In cleanup, you have to remove
all the components you might have added to the scene: if in the scene,
you have some collisions, and you create contact components, or
collision response components, cleanup is a good place for you to remove
them.
- In reset, you must set back to default all the Datas and
internal values of your component.

``` cpp
void cleanup();
void reset();
```

#### draw()

All SOFA components have a method draw(), so you don't need to derive
from a VisualModel base component to display debug information. It is
called at the end of the simulation time, directly by the GUI. At this
moment, we only have one thread running both the simulation and the
visualization. Soon, we want to separate these processes into two
different threads so that the frequency of the visualization doesn't
depend anymore on the frequency of the simulation (generally much
slower).

``` cpp
void draw();
```

#### getContext()

Every SOFA component has a context. By casting this context to a
`simulation::Node*`, you manage to get the node containing your
component. A Node is a very useful component, as you can launch visitors
from them, or quickly get information about the content of the node. However,
we insist on the fact that accessing other components through the context
is not recommended: instead create [Link](https://www.sofa-framework.org/community/doc/programming-with-sofa/api-overview/create-links/)/DataLink. 

``` cpp
sofa::core::objectmodel::BaseContext* getContext();
```

Example:

``` cpp
simulation::Node* currentNode = static_cast<simulation::Node*>(myComponent->getContext());
```

#### handleEvent( Event\* )


Every SOFA component inherits a [Data](https://www.sofa-framework.org/community/doc/programming-with-sofa/api-overview/data-in-components/) **f\_listening** from BaseObject.
If **f\_listening** is true, then each time an [Event](https://www.sofa-framework.org/community/doc/programming-with-sofa/api-overview/events-in-sofa/) is sent to
the node containing your component, this method will be called. This
way, you can execute specific operations when an event is triggered.


``` cpp
void handleEvent( Event* );
```

Example:

``` cpp
void handleEvent ( core::objectmodel::Event* ev )
{
  if ( dynamic_cast ( ev ) )
  {
    // Do some operation when the collision detection ends.
  }
}
```

You can use the Trace of Visitor to know when and where the Events are
triggered. The most common SOFA events are:

-   AnimateBeginEvent
-   AnimateEndEvent
-   CollisionBeginEvent
-   CollisionEndEvent
-   TopologyChangeEvent
-   UpdateMappingEndEvent

Find out more about the [Events here](https://www.sofa-framework.org/community/doc/programming-with-sofa/api-overview/events-in-sofa/).


## Member variables

#### Component state

The [Data](https://www.sofa-framework.org/community/doc/programming-with-sofa/api-overview/data-in-components/) attribute `d_componentState` defined in Base.h corresponds to
the state of every component. This enum defines the following states:

- Undefined: for a component that does not make use of this field have this one
- Loading: the component is loading but never passed successfully its init() function
- Valid: the component has passed successfully its init function and is operational
- Dirty: the component is ready to be used but requires a call to reinit
- Busy:  the component is doing "something", don't trust its values for doing your computation
- Invalid: the component reached an error and is thus unable to behave normally.


#### Print log

The [Data](https://www.sofa-framework.org/community/doc/programming-with-sofa/api-overview/data-in-components/) attribute `f_printLog` defined in Base.h is a boolean triggering
the emission of log messages at runtime. If true, all messages as follows will be emitted:

```cpp
msg_info() << "My log message";
```



## Update mechanism

All components (i.e. class inheriting from BaseObject) inherits from a callback mechanism to update its internal attributes and Data.
In SOFA, callback functions can be added so that outputs can be updated upon changes on their input data.
The callback function returns a component state (see above: Valid / Invalid / etc.) which guarantees that the component state is properly maintained.
Here is the callback used in Loaders:

```cpp
/// name filename => component state update + change of all data field...but not visible ?
    addUpdateCallback("UpdateOnFilename", {&m_filename}, [this](const core::DataTracker& t)
    {
        SOFA_UNUSED(t);
        if(load()){
            clearLoggedMessages();
            return sofa::core::objectmodel::ComponentState::Valid;
        }
        return sofa::core::objectmodel::ComponentState::Invalid;
    }, {&d_positions, &d_normals, &d_edges, &d_triangles, &d_quads, &d_tetrahedra, &d_hexahedra, &d_pentahedra, &d_pyramids,
        &d_polylines, &d_polygons, &d_highOrderEdgePositions, &d_highOrderTrianglePositions, &d_highOrderQuadPositions, &d_highOrderHexahedronPositions, &d_highOrderTetrahedronPositions,
        &d_edgesGroups, &d_quadsGroups, &d_polygonsGroups, &d_pyramidsGroups, &d_hexahedraGroups, &d_trianglesGroups, &d_pentahedraGroups, &d_tetrahedraGroups}
    );
```

it is triggered whenever the Data `d_filename` has been modified (i.e. it is dirty) in order to recompute the Data `d_positions`, `d_normals`, `d_edges` etc.



## Other information about components



#### ObjectFactory methods

To support the creation of a scene from a xml description, we rely on an
ObjectFactory. Optionally a SOFA Component can define several static
methods to customize its creation and its XML syntax.

#### canCreate

``` cpp
 template
    static bool canCreate(T*& obj, core::objectmodel::BaseContext* context, core::objectmodel::BaseObjectDescription* arg);
```

This method is called before the effective creation of the object
specified in the xml: this way, you have access to the current context
(object that have already been created), and you can process to some
basic verifications; for instance, if your component needs a specific
template, or another component to work, you can test this here.

#### create

``` cpp
template
    static void create(T*& obj, BaseContext* context, BaseObjectDescription* arg);
```

If, and if only, the method canCreate answered true, the component is
created: By default, the implementation made in
sofa::core::objectmodel::BaseObject does:

``` cpp
template
    static void create(T*& obj, BaseContext* context, BaseObjectDescription* arg)
{
obj = new T;
if (context) context->addObject(obj);
if (arg) obj->parse(arg);
}
```

Three steps:

-   Creation of the object passed by template (look at how works the
    design pattern of an abstract factory)
-   Add the object inside the current context: the side effect of this
    instruction is that the new object will appear in the scene graph
    inside the node corresponding to the context
-   Parse method to initialize the parameters described in XML. All the
    parameters stored as Data will be automatically set, YOU DON'T HAVE
    TO IMPLEMENT YOUR OWN PARSE METHOD!

#### templateName

The templateName() and getTemplateName() methods purpose is to give
convenient names to the attribute template of your component when
reading/writing from the XML. These methods are defined in
sofa::core::objectmodel::Base which is the base class for all SOFA
objects that can belong to the scene graph, ie Nodes and Components.

``` cpp
std::string getTemplateName() const

static std::string templateName(const MyTemplateClass* = NULL)
```

The two methods inherently do the same thing but

-   the static method is used in the parts of the code where compile
    time generecity over SOFA objects is used ( meaning when we treat
    SOFA objects through some template parameter)
-   the class method is more convenient in the parts of the where we
    treat SOFA objects through a base class pointer.
    (runtime polymorphism)

**The important thing to remember is that if you want to give a special
behavior for the template attribute, you need to override both these
method otherwise there will be some mismatches about what is expected.**
The template attribute is used at the component creation to select the
appropriate constructor registered in the ObjectFactory.

```xml
<MechanicalObject template="Rigid"/>
```

As a rule of thumb, you should override these methods in your component
class if these conditions are met :

-   your component class depends on template parameters
-   your component class does not inherit from a class of sofa::core
    which uses the exact same template parameters.

Examples:

-   sofa::component::engine::BoxROI depends on a template parameter, and
    derives from sofa::core::DataEngine which does not, so the
    templateName methods are overriden.
-   sofa::component::mapping::IdentityMapping depends on template
    parameters, and derives from sofa::core::Mapping which uses the
    exact same template parameters, so the templateName methods need not
    to be overriden.

For most common template parameters like VecTypes and RigidTypes, we
provide convenient aliases using the compile time expected method Name()
of the template parameter. For example by providing

``` cpp
template<> inline const char* Vec3dTypes::Name() { return "Vec3d"; }
```

As a result we can write

```xml
<MechanicalObject template="Vec3d"/>
```

instead of :

```xml
<MechanicalObject template="StdVectorTypes<Vec<3,double>,Vec<3,double>,double> >" />
```

#### Common operations

When you use a Component in SOFA, you generally make it interact with
the rest of the scene, and more specifically the node containing your
component and the hierarchy above and below it.

#### Search components in the graph

One basic need you will have will be to get pointers to some components:
Get the Mechanical State, or the Mapping... In the following examples,
methods of class BaseObject are used to get smart pointers to the
components:

``` cpp
// Search one component of a given type; return when the first is found.
Mapping::SPtr m;                      // using smart pointers is safer than plain pointers
m = searchLocal();           // search in the same node as this
m = BaseObject::searchLocal();           // from a template class, you may have to help the compiler
m = searchUp();              // search in the same node as this, then upward in the node hierarchy
m = searchDown();            // search in the same node as this, then downward in the node hierarchy
m = searchFromRoot();        // search starting from the root
m = searchInParents();       // search in the parents of the local node

// Search all the component of a given type
vector v;
v = searchAllLocal();
v = searchAllUp();
v = searchAllDown();
v = searchAllFromRoot();
v = searchAllInParents();

// Search all the component of a given type with a given Tag
core::objectmodel::Tag t("Fluid");
v = searchAllLocal( t );
v = searchAllUp( t );
v = searchAllDown( t );
v = searchAllFromRoot( t );
v = searchAllInParents( t );

// Search all the component of a given type with a given TagSet
core::objectmodel::TagSet ts= this->getTags();
v = searchAllLocal( ts );
v = searchAllUp( ts );
v = searchAllDown( ts );
v = searchAllFromRoot( ts );
v = searchAllInParents( ts );
```

In the following examples, the same is done using the lower-level method
BaseObject::get

``` cpp
core::componentmodel::behavior::BaseMapping* mapping;
this->getContext()->get(mapping);
if (mapping)
{  //Mapping found
}
else
{  //Mapping NOT found
}

//Same call as this->getContext()->get(mapping);
this->getContext()->get(mapping, sofa::core::objectmodel::BaseContext::SearchUp);
//Starts from local node, then if nothing is found, goes down in the hierarchy of node
this->getContext()->get(mapping, sofa::core::objectmodel::BaseContext::SearchDown);
//Search only inside the local node
this->getContext()->get(mapping, sofa::core::objectmodel::BaseContext::Local);
//Search from the Root node, then goes down to all the nodes
this->getContext()->get(mapping, sofa::core::objectmodel::BaseContext::SearchRoot);


sofa::helper::vector< sofa::core::CollisionModel* > list_collisionModels; //container for the component you want to find
//Default call: search from current node, then goes up
static_cast(this->getContext())->get< sofa::core::CollisionModel >( &list_collisionModels );
//Same behavior as previous call, only it explicits the method called
static_cast(this->getContext())->get< sofa::core::CollisionModel >( &list_collisionModels, BaseContext::SearchUp);
//Starts from the current node, and goes down
static_cast(this->getContext())->get< sofa::core::CollisionModel >( &list_collisionModels, BaseContext::SearchDown);
//Search only in the current node
static_cast(this->getContext())->get< sofa::core::CollisionModel >( &list_collisionModels, BaseContext::Local);
//Search from the root
static_cast(this->getContext())->get< sofa::core::CollisionModel >( &list_collisionModels, BaseContext::SearchRoot);


//Find a mapping (previously declared), containing the same set of tags as your component
this->getContext()->get(mapping, this->getTags(), sofa::core::objectmodel::BaseContext::SearchDown);

//Find a mapping (previously declared), containing the set of tags "Fluid" and "Mecha"
sofa::core::objectmodel::TagSet tagsToFind;
tagsToFind.insert(sofa::core::objectmodel::Tag("Fluid"));
tagsToFind.insert(sofa::core::objectmodel::Tag("Mecha"));
this->getContext()->get(mapping, tagsToFind, sofa::core::objectmodel::BaseContext::SearchDown);
```

#### Launch Visitor

The genericity of SOFA is achieved mainly by the use of Visitors. It is
good to know how to launch them.

``` cpp
simulation::Node *currentNode=static_cast(this->getContext());
currentNode->execute(); //Launch the visitor VisualUpdateVisitor from the currentNode

//If you need to configure your Visitor before launching it
sofa::simulation::MechanicalWriteLMConstraint  LMConstraintVisitor;
LMConstraintVisitor.setOrder(orderState); //configuring the Visitor
//...
//Launch the Visitor
LMConstraintVisitor.execute(this->getContext());
```

As mentioned previously, you can use Tags in order to execute your
Visitor only on the components containing a set of Tags

``` cpp
LMConstraintVisitor.setTags(this->getTags()).execute(this->getContext());
```

#### Bounding Box

There is a BoundingBox class declared in sofa/defaulttype/BoundingBox.h
This class defines most common operations regarding bounding boxes, such
as intersection and inclusion. All the components and contexts/nodes in
SOFA have a data with public access to express its bounding box.

``` cpp
// in sofa/core/Base.h
Data< sofa::defaulttype::BoundingBox > f_bbox;
```

#### components

The default value for the bounding box is a the neutral element for the
inclusion operation. A component can describe how its bounding box is
computed by redefining the virtual method.

``` cpp
// in sofa/core/BaseObject.h
virtual void computeBBox(sofa::core::ExecParams* params);
```

There is an example of such an override in the sofa::core::State class.

#### contexts and nodes

Contexts, also have a notion of Bounding Box. A Context bounding box is
the inclusion of:

-   the bounding boxes of all its components.
-   the bounding boxes of all its child contexts

#### accessing the bounding box value from a component

You can access the value of your component bounding box using :

``` cpp
//somewhere in yourcomponent.cpp
const sofa::defaulttype::BoundingBox& bbox = this->f_bbox.getValue();
```

If your component does not define any bounding box, you can still access
its context bounding box

``` cpp
//somewhere in yourcomponent.cpp
const sofa::defaulttype::BoundingBox& bbox = this->getContext()->f_bbox.getValue();
```

#### update of the bounding boxes

Bounding boxes values are set the first time during the InitVisitor
traversal. There are kept up to date using the UpdateBoundingBoxVisitor.