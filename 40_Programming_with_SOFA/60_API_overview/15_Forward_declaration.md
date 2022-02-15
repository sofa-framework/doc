Forward declaration
===============
To reduce the amount of file inclusion in Sofa and thus compilation time it is possible to use forward declaration. 
A forward declaration is a an incomplete type ta complete definition is not provided. 
```cpp
class AClass; ///< this is a forward declaration of a type

/// This is the full declaration + definition of a type
class AClass   
{
    public:
}
```

Forward declaration can be used in place of the complete type (declaration+definition) when the "inner" details of the type are not needed. A classical scenario is the following
```cpp
#include <sofa/core/objectmodel/BaseObject>
bool myFunction1(BaseObject* a)
{
    return doSomethingWith(a);
}
```

As we are manipulating the 'a' object via a pointer and passing it to the doSomethingWith function there is no need to know any details of the BaseObject to compile that properly. Using a forward declaration for BaseObject would save us from the inclusion of the file ```#include <sofa/core/objectmodel/BaseObject>```

Where to put forward declaration
--------------------------------

Forward declaration must be in a file called ```fwd.h```. The fwd.h can be located at the module root directory.
Eg:
```
sofa/core/fwd.h
```

If there is a lot of forward declaration it is allowed to have a per sub-module ```fwd.h``` file. 
Eg:
```
sofa/core/objectmodel/fwd.h
sofa/core/behavior/fwd.h
```

In that case it is mandatory that the module file contains them all. In our example 
```cpp
sofa/core/fwd.h
    #include<sofa/core/objectmodel/fwd.h>
    #include<sofa/core/behavior/fwd.h>
```


Opaque API 
=========
When it is not desirable to have access the full type definition it is possible to make or use what is called an opaque API. The Opaque API mimmics the methods provided by a class but relying only on forward declaration. 
Example of the "transparent" API: 
```cpp
#include <Context>
#include <BaseNode>
namespace sofa::simulation
{
class Node : public Context, public BaseNode 
{
    public:
         double getDt(); 
         ///....
};
}
```

Example of the corresponding "opaque" API: 
```cpp
namespace sofa::simulation::node
{
     double getDt(Node*);  
}
```

Opaque API for a given type can be located at the same location where the type is forward declared or if very long in their own dedicated file close to the one where the type definition is. 
```
sofa/simulation/node.h
sofa/simulation/node.cpp
sofa/simulation/node-fwd.h 
```

If the second solution is chosen, the ``node-fwd.h` file must be included by the per-module fwd.h. 