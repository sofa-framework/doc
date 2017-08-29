#### Introduction

Components implement most of the simulation methods. One can rougly
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

#### Base functions

A Sofa component is a class deriving from
**sofa::core::objectmodel::BaseObject**. This way, several virtual
methods are provided, and must be known in order to configure correctly
the behavior of your component:

#### init() and bwdInit()

When SOFA loads a simulation, its creates in C++, or directly using XML
the Sofa Components (and the default constructor). At this stage, you
must initialize what we call **Data**, a component that you can find in
**sofa::core::objectmodel::Data**. The purpose of this utility class is
to store all the parameters of your component, and handle this way the
input (parametrize the component from xml files for instance), and
output (save at a time T the configuration of your component).
Everything that needs to be saved in your component must be kept into
memory inside a Data. Basically to initialize a data, you must do the
following:

``` cpp
//Previous declaration of the Data
Data<bool> isEnabled;
//In Component constructor
MyComponent():
isEnabled(initData(&isEnabled, true, "isEnabled", "Boolean indicating if the component is enable"))) //ptr to the data, default value, name used for the parameter (the same that will appear later in the XML file), description of the parameter (its purpose)
{
};
```

Once all the Sofa Components of the scenes have been created, we launch
a Visitor to initialize the components: Basically a Visitor starts from
a node (for the InitVisitor, we start from the root), execute several
specific operations going top-&gt;down, and then another set of
operations going bottom-&gt;up. This is translated for the InitVisitor
by the call, each time we initialize a scene of two methods

``` cpp
void init(); //call during Top->Down traversal
void bwdInit(); //call during Bottom->Up traversal
```

bwdInit is called once all the children of a node has been initialized,
the methods init() and bwdInit() have been called for all the component
of the children nodes.

#### reinit()

The purpose of the reinit() method is to recompute, and reconfigure your
component when you have modified one or several of its Data. Typically,
we automatically call reinit() when you edit a component in the GUI of
Sofa.

``` cpp
void reinit();
```

#### cleanup() and reset()

``` cpp
void cleanup();
void reset();
```

These methods are called each time you want to reset a scene: first
cleanup will be called, then reset. \* In cleanup, you have to remove
all the components you might have added to the scene: if in the scene,
you have some collisions, and you create contact components, or
collision response components, cleanup is a good place for you to remove
them. \* In reset, you must set back to default all the Datas and
internal values of your component.

#### draw()

``` cpp
void draw();
```

All Sofa components have a method draw(), so you don't need to derive
from a VisualModel base component to display debug information!. It is
called at the end of the simulation time, directly by the GUI. At this
moment, we only have one thread running both the simulation and the
visualization. Soon we want to separate these processes into two
different thread so that the frequency of the visualization doesn't
depend anymore on the frequency of the simulation (generally much
slower).

#### getContext()

``` cpp
sofa::core::objectmodel::BaseContext* getContext();
```

Every Sofa component has a context. By casting this context to a
simulation::Node\*, you manage to get the node containing your
component. A Node is a very useful component, as you can launch visitors
from them, or quickly get information about the content of the node.
Example of use:

``` cpp
simulation::Node* currentNode = static_cast<simulation::Node*>(myComponent->getContext());
```

#### handleEvent( Event\* )

``` cpp
void handleEvent( Event* );
```

If the Data **f\_listening** is true, then each time an Event is sent to
the node containing your component, this method will be called. This
way, you can execute specific operations when an event is triggered.

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
triggered. The most common Sofa events are:

-   AnimateBeginEvent
-   AnimateEndEvent
-   CollisionBeginEvent
-   CollisionEndEvent
-   TopologyChangeEvent
-   UpdateMappingEndEvent

#### Component properties: Data

Numerical values are stored in components using 'core::objectmodel::Data
objects. For instance, to store a Real, use a Data. Wrapping values in
this template class provides the following features:

-   automatic read/write in scene files
-   connections with other Data or to/from Engines using Links, for
    automatic updates
-   thread-safe access (work in progress)

This is how a Data called enableOptionA storing a boolean can appear in
a scene file:

```xml
<Node name="Root">
   <MyClass enableOptionA="true"/>
</Node>
```

To add this Data to a C++ class, you need to:

1.  declare a Data template with the type of your option: here, a
    boolean

    ``` cpp
    Data activeOption;
    ```

2.  in the constructor of you class MyClass, initialize the Data

    ``` cpp
    MyClass(): activeOption(initData(&activeOption, true, "enableOptionA", "Activate the option A")){};
    ```

    1.  &activeOption **\[REQUIRED\]**: the pointer to the data.
    2.  true **\[OPTIONAL\]**: a default value. When the option is not
        specified (in xml or C++), the Data will have this value.
    3.  "enableOptionA" **\[REQUIRED\]**: the name of your option, as it
        will appear in the XML file.

#### Links between Data

It is possible to create a link from a source Data to a target Data of
compatible type, to automatically duplicate the value of the source in
the target. For instance, the indices Data output of a BoxROI engine can
be linked to the indices Data of a FixedConstraint, to constrain the
particles in the box. A source can be connected to several targets. Each
time a source value changes, it sends a dirty message to all its
targets, which recursively propagate the dirty signal if they are the
sources of further links. When a target data value is accessed (see How
to Access Data below), it first checks its dirty state and if necessary,
it updates its value based on the source, recursively. In XML, links are
set using the @ symbol as in the following example:

```xml
```

In C++, links are set using method BaseData::setParent( BaseData\* ), as
in the following example:

``` cpp
myFixedConstraint->f_indices.setParent(&myBoxRoi->f_indices);
```

#### How to Access Data in the C++ API

The disadvantage of storing values in a Data container, rather than
directly, is to make the value less easily accessible. Different ways of
accessing it are presented in the following.

#### setValue/getValue

To have a read only access to the data, use the method getValue()

``` cpp
//with Data activeOption;
//and  Data > values;
void MyClass::doOperation()
{
  bool isActive=activeOption.getValue();
  const vector< int > &v=values.getValue();
  if (isActive)
  {
    for (unsigned int i=0;i
```

To write the value of the data, use the method setValue(...) A dirty
flag is propagated to the all the Data connected to this one (see Engine
and Data dependency). This is appropriate for a «one shot» value
setting. To iterate over an array, prefer one of the following methods.

``` cpp
//with Data activeOption;
//and  Data > values;
void MyClass::changeParameters(bool b)
{
  activeOption.setValue(b);
  vector< int > newVector(10);
  values.setValue(newVector);
  //...
}
```

#### beginEdit/endEdit

This method is useful when you need to change multiple values (such as
array cells) before to notify the change to other Data, and to prevent
concurrent writing in the same time.

-   beginEdit() returns a pointer to the internal data, and records that
    the Data is currently being modified. This allows to implement a
    «lock» against concurrent writing.
-   endEdit() unlocks the data and propagate the dirty flag.

The direct use of this method is deprecated, please use the
ReadAccessor/WriteAccessor presented below. This is commonly used while
manipulating vectors of data.

``` cpp
//with Data > values;
void MyClass::manipulatingParameters()
{
  vector& myValues = *values.beginEdit();
  for( int i=0; i
```

#### ReadAccessor/WriteAccessor

These objects encapsulate beginEdit and endEdit in their constructor or
destructor, respectively. These ensures that you do not forget to
endEdit, and allows to distinguish read-only and write access. This is
the preferred method for accessing arrays.

``` cpp
//with Data > values;
  helper::WriteAccessor > > myValues(values);
  for( int i=0; i
```

For read access, replace WriteAccessor with ReadAccessor. Here is
another example:

``` cpp
// Get read access to the coordinate vector associated with object1. Of course you need to know the DataTypes associated with Object1.
core::behavior::MechanicalState* mstate1 = dynamic_cast*>( object1->getContext()->getMechanicalState() );
helper::ReadAccessor > coord1( *mstate1->read(core::ConstVecCoordId::position()) );
```

#### Using State member types and methods

Class core::State has types and methods to ease the use of accessors.
For example, the second line of the previous example could be written
as:

``` cpp
typename core::behavior::MechanicalState::ReadVecCoord coord1 = mstate1->readPositions();
```

#### Using MechanicalParams

In the following example, all the state vectors are obtained from the
local MechanicalState as Data and Data using a MechanicalParam, such as
the current position and velocity of the local object. The force vector
id is passed explicitly to remind that the result should be stored in
this vector, and a alternative instruction is used, but the force vector
can also be obtained using an instruction like for positions and
velocities. The vectors are then passed to a more concrete (though
virtual) function which processes actual vectors rather than Ids.

``` cpp
template
void ForceField::addForce(const MechanicalParams* mparams, MultiVecDerivId fId )
{
    addForce(mparams, *fId[mstate.get(mparams)].write() , *mparams->readX(mstate), *mparams->readV(mstate));
}
```

#### Data for standard containers

To ease the use of Data, we already serialized some of the most common
data container: map, vector, set, list. Instead of using a std::vector,
use a helper::vector:

``` cpp
Data< helper::vector > values;
```

**WARNING**: to use a vector&lt; vector&lt; int&gt; &gt;, you must use a
SVector instead:

``` cpp
Data< helper::SVector< helper::vector< int> > > vecValues;
```

#### Data for custom types

A Data is template with the type of your option: a boolean, an integer,
... But it is not restricted to the default types, you put inside a Data
your own class, or data structure. Your class must implement the
operator &lt; &lt; and &gt;&gt; in order to be used through an input and
output stream:

``` cpp
struct MyStruct
{
    bool active;
    int  value;

    inline friend std::istream& operator >> ( std::istream& in, MyStruct& s ){
        in >> s.active >> s.value
            return in;
    }

    inline friend std::ostream& operator < < ( std::ostream& out, const MyStruct& s ){
        out << s.active << " " << s.value;
        return out;
    }
};
Data configureStruct;
```

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
```

As a rule of thumb, you should override these methods in your component
class if these conditions are met :

-   your component class depends on template parameters
-   your component class does not inherit from a class of sofa::core
    which uses the exact same template parameters.

Examples:

-   sofa::component::engine::BoxROI depends on a template paremeter, and
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
```

instead of :

```xml
```

#### Common operations

When you use a Component in Sofa, you generally make it interact with
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

The genericity of Sofa is achieved mainly by the use of Visitors. It is
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
Sofa have a data with public access to express its bounding box.

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

Contexts, also have a notion of Bouding Box. A Context bounding box is
the inclusion of:

-   the bounding boxes of all its components.
-   the bounding boxes of all its child contexts

#### accessing the bouding box value from a component

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
