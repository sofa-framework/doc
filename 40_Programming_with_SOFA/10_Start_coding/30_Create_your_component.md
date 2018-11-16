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

The interface of the DataEngine class inherits BaseObject's, and adds an additional `doUpdate()` method. Input and output fields must be added to the engine in the init() method by respectively calling `addInput(myInputData)` and `addOutput(myOutputData)`:

```cpp
virtual void init() override
{
	addInput(d_input1)
	addInput(d_input2)
    ...
	addOutput(d_output1)
	addOutput(d_output2)
	...
}
```
The `doUpdate()` is a pure virtual method of DataEngine. This method will be automatically called when another component in the scene graph tries to access a data field (`getValue() / beginEdit() / ReadAccessor / WriteAccessor ...`) that is linked to one of your Engine's output field.

In `doUpdate()` your input fields are always "ready", i.e already updated from their parent value, thus holding up-to-date data.
Each engine holds an internal `DataTracker`, called `m_dataTracker`. DataTrackers can tell you which input field has been changed, during a call to doUpdate(). DataTrackers need to be told which data it should track. this is done by calling:
```cpp
m_dataTracker.trackData(d_myData)
```
Every call to `addInput` automatically adds the given input to the dataTracker.

If you have multiple input fields, and want to perform specific functions depending on which input has been modified, you can use this DataTracker to check which input has changed:
```cpp
virtual void doUpdate()
{
	if (m_dataTracker.hasChanged(d_input1))
	{
		// Do Stuff With d_input1
		...
	}
	if (m_dataTracker.hasChanged(d_input2))
	{
		// Do stuff with d_input2
		...
	}
	...
}
```

#### Remarks ####

- Note that you should not modify your inputs in an engine. I do not know of any use cases where this would be a good idea. If you do, it will set the engine's dirty flag, hence forcing a re-call to update().
If for some reason you would need to do so, you will need to call `DDGNode::cleanDirty()` on your engine to prevent the call loop.
- `doUpdate` is actually a **delegate function** called by the `update()` method. This method is `final`, which means that you cannot override it. Here's its implementation:

```cpp
void DataEngine::update()
{
    updateAllInputs(); ///< Updates all input fields to retrieve their parent values if changed
    DDGNode::cleanDirty(); ///< Cleans the engine's "dirty value".
	                       ///  This dirty value is used to know whether or not the call to update is necessary
    doUpdate(); ///< Your engine's implementation is called here.
    m_dataTracker.clean(); ///< The dataTracker is cleaned, i.e its internal counters are synced with the input's counters
}
```
- Some engines might require performing an action when an event is triggered, not just when an input is dirty. This is still possible by calling BaseObject's handleEvent() method. If you do so though, make sure that you stay consistent with the Data dependency graph
- Except in some specific / rare cases, every data field in your engine should either be inputs or outputs of the engine, and there should be no "standard" data field.
- before the 18.12, a call to setDirtyValue had to be made once all the inputs and outputs were set. It is now obsolete
- DataEngines are part of the Data Dependency Graph of Sofa. This mechanism is inherited from DDGNode, and can be quite challenging to understand by simply digging in the code. If you are curious about how it works, a [presentation is available on Google Drive](https://docs.google.com/presentation/d/1p0a3PVYhfZS9Vqkvn2DIYUo10SDnJolb2QYKZIy5W3s/edit) 
