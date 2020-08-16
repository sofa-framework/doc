The ObjectFactory
-----------------

The ObjectFactory is mostly a register which gives a correspondancy
between a component name and a function pointer to a method able to
construct that object. It is located in the sofacore library.

Registering a component
-----------------------

In SOFA a component is a class which has
sofa::core::objectmodel::BaseObject in its class inheritance hierarchy.
In order to make your component available in SOFA you have to call the
registration method of the ObjectFactory, and use two macros
SOFA\_DECL\_CLASS and SOFA\_LINK\_CLASS whose purpose is to make sure
that the code which actually registers the component in the factory is
called in the output binary. The summary of the steps to follow is here
:

-   Add a : SOFA\_DECL\_CLASS(NewComponent) in your .cpp file,
    NewComponent being the class name of your component.
-   Register the component: it is generally done in the .cpp of your new
    component class. if your component is not template:

    ``` cpp
    #include <sofa/core/ObjectFactory.h>
     int NewComponentClass = sofa::core::RegisterObject("Description of your component")
    .add< NewComponent >();
    ```

    if your component is template with Vec3dTypes and Vec3fTypes
    (for instance)

    ``` cpp
     int NewComponentClass = sofa::core::RegisterObject("Description of your component")
    .add< NewComponent <Vec3dTypes>>()
    .add< NewComponent <Vec3fTypes>>()
    ;
    ```

-   Add a : SOFA\_LINK\_CLASS(NewComponent) in the init file.
    -   If you chose to put your components directly inside SOFA modules
        directories you will find a file called
        initNameCategoryComponent.cpp with NameCategoryComponent being
        the category of your component: ForceField, Constraint,
        Mapping ... This is were you put the SOFA\_LINK\_CLASS macro
    -   If you are writing a plugin, you have to call in the
        SOFA\_LINK\_CLASS macro from your initMyPlugin.cpp.

The documentation about the methods regarding the registration component
can be found in the [doxygen documentation of the
sofa::core::RegisterObject
class](https://www.sofa-framework.org/api/SOFA/classsofa_1_1core_1_1_register_object.html "RegisterObject class").

The ObjectFactory and the XML (**MechanicalObject** example)
------------------------------------------------------------

For a given instance of SOFA we can know what are the available
components by looking at the ObjectFactory entries. An entry in the
ObjectFactory can point to multiple constructors, which happens to be
useful when you write components which depend on a template parameter.

``` cpp
int MechanicalObjectClass = core::RegisterObject("mechanical state vectors")
#ifdef SOFA_FLOAT
.add< MechanicalObject >(true) // default template
#else
.add< MechanicalObject >(true) // default template
#ifndef SOFA_DOUBLE
.add< MechanicalObject >()
#endif
#endif
#ifndef SOFA_FLOAT
.add< MechanicalObject >()
.add< MechanicalObject >()
.add< MechanicalObject >()
.add< MechanicalObject >()
.add< MechanicalObject >()
#endif
#ifndef SOFA_DOUBLE
.add< MechanicalObject >()
.add< MechanicalObject >()
.add< MechanicalObject >()
.add< MechanicalObject >()
.add< MechanicalObject >()
#endif
.add< MechanicalObject >()
;
```

We can see that the same entry "MechanicalObject" has multiple flavor
depending on the template parameter, and that the default entry points
to a

-   sofa::component::container::MechanicalObject if SOFA is compiled in
    float mode
-   sofa::component::container::MechanicalObject if SOFA is compiled in
    double mode

When you write a SOFA scene in XML this means that such a line

```xml
<MechanicalObject />
```

will be translated by the default instance of MechanicalObject
registered in the ObjectFactory. If you want a specific flavor of
MechanicalObject, you have to specify it by using the template attribute
in the XML.

```xml
<MechanicalObject template="Real"/>
```

This will produce a MechanicalObject if SOFA is compiled with double and
MechanicalObject otherwise The template attribute is resolved using the
templateName method. Ultimately for a RigidType in 3D ( ie Rigid3dTypes
Rigid3fTypes) this points to :

``` cpp
/// Note: Many scenes use Rigid as template for 3D double-precision rigid type. Changing it to Rigid3d would break backward compatibility.
#ifdef SOFA_FLOAT
        template<> inline const char* Rigid3dTypes::Name() { return "Rigid3d"; }
        template<> inline const char* Rigid3fTypes::Name() { return "Rigid"; }
#else
        template<> inline const char* Rigid3dTypes::Name() { return "Rigid"; }
        template<> inline const char* Rigid3fTypes::Name() { return "Rigid3f"; }
#endif
```

The createObject method
-----------------------

``` cpp
sofa::core::objectmodel::BaseObject::SPtr obj = ObjectFactory::createObject( /* objectmodel::BaseContext* */ context, /* objectmodel::BaseObjectDescription* */arg);
MyComponent::SPtr my_obj = sofa::core::objectmodel::SPtr_dynamic_cast(obj);
```

The method needs two parameters :

-   core::objectmodel::BaseContext , ie the graph node where your
    component will reside
-   core::objectmodel::BaseObjectDescription, which is stores specific
    parameters of the component you are trying to create.

Example of the TetrahedronFEMForceField
---------------------------------------

``` cpp
sofa::core::objectmodel::BaseObjectDescription options("myFF1","TetrahedronFEMForceField");
    options.setAttribute("youngModulus", "10000");
    BaseForceField::SPtr ff = sofa::core::objectmodel::SPtr_dynamic_cast(sofa::core::ObjectFactory::CreateObject(node, &options));
```

 
