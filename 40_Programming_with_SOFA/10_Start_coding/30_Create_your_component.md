A **SOFA component** is a class or a class template that inherits,
directly or not, from `sofa::core::objectmodel::BaseObject`. A component
must also respect some conventions:

-   the declaration *must* begin with the `SOFA_CLASS` macro. It will
    expand to some code required by SOFA, that will enable some kind of
    reflection mechanisms;
-   a component must be registered in the `ObjectFactory`, using the
    `RegisterObject` mechanism (see example below), otherwise SOFA won't
    be aware of it.

Here is a minimal example, for a component that does nothing:

``` cpp
#include <sofa/core/objectmodel/BaseObject.h>

class MyComponent : public sofa::core::objectmodel::BaseObject
{
public:
SOFA_CLASS(MyComponent, sofa::core::objectmodel::BaseObject);

    MyComponent ();
    virtual ~MyComponent ();
};
```

``` cpp
#include "MyComponent.h"
#include <sofa/core/ObjectFactory.h>

MyComponent::MyComponent()
{
}

MyComponent::~MyComponent()
{
}

int MyComponentClass = sofa::core::RegisterObject("This component does nothing.").add<MyComponent>();
```

Once the plugin is compiled, this component can be used in an XML scene
file. You should also add a `RequiredPlugin` element in the root node in
order to load `MyPlugin` when the scene is loaded.

``` xml
<?xml version="1.0"?>
<Node name="Root">
    <RequiredPlugin pluginName="MyPlugin"/>
    <MyComponent>
</Node>
```

This is a basic example; most components don't inherit directly from
`BaseObject`, but from a subclass which represent a specific aspect of a
simulation. For example, force field components inherit from
`sofa::core::BaseForcefield`, or one of its subclasses.

Add Data to your component
--------------------------

Almost every component has parameters, inputs, or outputs: they are
referred to as *Data*; in a scene file, those are the XML attributes of
the component. Each XML attribute of a component is actually a member of
the class, declared in a special way: it is encapsulated in a
[Data](https://www.sofa-framework.org/api/SOFA/classsofa_1_1core_1_1objectmodel_1_1_data.html "Data").
For example, in order to add a float Data named `myparam` to our
component, we will add this member to `MyComponent`:

``` cpp
Data<float> m_myparam;
```

Then we must register and initialise it in **each** Constructor of
MyComponent:

``` cpp
MyComponent::MyComponent(): d_myparam(initData(&d_myparam, 0.42, "myparam", "Here should be a short description of myparam."))
{
}
```

This allows us to use this Data in scene files; it can be assigned a
value like so:

``` xml
<?xml version="1.0"?>
<Node name="Root">
    <RequiredPlugin pluginName="MyPlugin"/>
    <MyComponent myparam="3.7">
</Node>
```

Create DataEngine Components
--------------------------

Basic components such as the example above that inherits `BaseObject`, only allow for “Parameter” data fields (values that can be changed but only affects the component itself, internally).
Sometimes, you might want to create **input / output components**.
Engines can be “chained”, by giving an engine an input data that is the output of another, previously declared engine:
``` xml
<?xml version="1.0"?>
<Node name="Root">
    <RequiredPlugin pluginName="MyPlugin"/>
    <MechanicalObject name=”MO” />
    <MyEngine  name=”engine1” myinput="@MO.position" />
    <MyEngine myinput=”@engine1.myoutput” />
</Node>
```

These engine components will trigger an action when notified of a change in an input data field, and warn other engines, that take as an input the output of this engine, that the data has been modified.
In order to implement such a component, your class must inherit [`sofa::core::DataEngine` class]( https://www.sofa-framework.org/api/SOFA/classsofa_1_1core_1_1_data_engine.html "DataEngine").

More information on how to implement subclasses inheriting `DataEngine` can be found in the interface's Doxygen documentation.

