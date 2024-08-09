SOFA is a very modular framework, it therefore uses shared libraries extensively.

Differences between Windows and Linux/Mac when creating a shared library
------------------------------------------------------------------------

On Linux, every class and every function are automatically exported
in the shared library, you don't have to do anything. On Windows, the
default behaviour is to not export anything implicitly. You must use the
**\_\_declspec(dllexport)** symbol to export classes and functions you
need. And you must use **\_\_declspec(dllimport)** to import classes and
functions from a shared library. On SOFA, we use a specific macro for
each library to silently import / export. This macro is defined this way
: **SOFA\_mylib\_API** and is automatically set as
\_\_declspec(dllexport) if we are inside the library "mylib" because we
want to expose its class and function definitions. On the other side, if
we are outside the library, for instance in another lib or in an
application, the same macro is automatically defined as
\_\_declspec(dllimport) because we want to import class and function
definitions that we don't know yet but, we notify the compiler it will
find them in one of its linker dependencies. In common SOFA libraries,
the macros are all defined in the component.h file and for plugins, you
will find a initMyPlugin.h setting this macro. In each file you want to
use it you must include the corresponding file. Thus, "component.h" if
you are adding a component in the common SOFA libraries or the
"**initMyPlugin.h**" if you are implementing a new component in a
plugin.

How to use the macro to import / export definitions
---------------------------------------------------

For instance if we want to import / export definitions from our plugin
"MyPlugin" :

#### Example with a class

MyClass.h:

    #include "initMyPlugin.h" // contains the definition of SOFA_MyPlugin_API

    class SOFA_MyPlugin_API MyClass // export the class if we are currently building MyPlugin, else if we are outside MyClass will be imported
    {
        ...
    };

#### Example with a generic class

MyGenericClass.h:

    #include "initMyPlugin.h"

    template
    class MyGenericClass // we do not set the macro here since we are not defining a class but a generic class (a pattern) and definitions really exist only with a template instantiation
    {
        ...
    };

    // here we notify the compiler it will find the template instantiation elsewhere
    #if defined(SOFA_EXTERN_TEMPLATE) && !defined(SOFA_MYGENERICCLASS_CPP)
    #ifndef SOFA_FLOAT
    extern template class SOFA_MyPlugin_API MyGenericClass < MyDoubleType >;
    #endif
    #ifndef SOFA_DOUBLE
    extern template class SOFA_MyPlugin_API MyGenericClass < MyFloatType >;
    #endif
    #endif

MyGenericClass.cpp:

    #define SOFA_MYGENERICCLASS_CPP

    #include "MyGenericClass.h"

    // and here we explicitly instantiate the templated class
    #ifndef SOFA_FLOAT
    template class SOFA_MyPlugin_API MyGenericClass < MyDoubleType >;
    #endif
    #ifndef SOFA_DOUBLE
    template class SOFA_MyPlugin_API MyGenericClass < MyFloatType >;
    #endif

For generic class where we cannot predict the kind of template
instantiation the user will need, we do not use the import / export
macro because we cannot instantiate the template class. The user will
directly use the definitions from a .inl file that you have to provide.

#### Example with a function

    #include "initMyPlugin.h"

    void SOFA_MyPlugin_API MyFunc()
    {
        ...
    };

You should not use the SOFA\_MyPlugin\_API macro for member functions,
you just have to set the macro for the class owning the member functions
and, they will all be exported.

Common mistakes
---------------

If you are experiencing linking issues about dllimport the problem may
come from an omission or a bad use of the macro **SOFA\_\*\_API**. For
instance if you copied a class from a library to another without editing
its macro, its definitions will not be exported and worse the linker
will expect to find them in a dependency, although they are in the
currently compiled library.
