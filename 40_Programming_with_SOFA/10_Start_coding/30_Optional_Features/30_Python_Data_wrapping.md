Wrap your own Data types for Python
----------------------------------

If you are using SofaPython to create your scenes, you are probably interested in accessing your component's data fields and reading / writing their values from python, as done in the example below:

```xml
 # Modify a scalar data field from Python
  self.myComponent.findData('integerValue').value = 1

 # Modify a complex data field from Python
  self.myMecaObject.findData('position').value=str(x)+' '+str(y)+' '+str(z)+' 0 0 0 1'
```

This is possible, because the Data `integerValue` from `myComponent` is a scalar, and SofaPython provides natively the access to those Data types. In addition to Scalars, SofaPython also provides a python wrapper for more complex types such as `defaulttype::Vec<T, real>` or `defaulttype::Matrix<T>`, but also containers classes such as `helper::vector` or `helper::SVector` for instance.

In order to get python support for your [custom Data types](https://www.sofa-framework.org/community/doc/programming-with-sofa/start-coding/components-api/components-and-datas/#data-for-custom-types), you will need to implement bindings for your custom type. This is done by:

1. Implementing data / methods accessors and bindings in CPython
2. Declaring and Registering your bindings to SOFA's Python Factory


As an example, we will consider the native Sofa type [`DataFileName`](https://www.sofa-framework.org/api/SOFA/classsofa_1_1core_1_1objectmodel_1_1_data_file_name.html), whose bindings are implemented in the SofaPython plugin.
In any case, it is very informative to look into the "native" binding implementations present in the SofaPython plugin.




Implementing data / methods accessors and bindings in CPython
------------------------------
Custom types are extended to python using the `SP_DECLARE_CLASS_TYPE` macro declared in [`PythonMacros.h`](https://www.sofa-framework.org/api/SofaPython/_python_macros_8h.html)
All python macros are prefixed with **SP_**


```
#include "PythonMacros.h"
#include <sofa/core/objectmodel/DataFileName.h>
SP_DECLARE_CLASS_TYPE(DataFileName)
```

Then a CPython getter is implemented, to retrieve the data structure's instance pointer in Python:

```
/// getting a DataFileName* from a PyObject*
static inline DataFileName* get_DataFileName(PyObject* obj) {
    return sofa::py::unwrap<DataFileName>(obj);
}
```

Getters are implemented to read attribute values from the DataFileName structure (fullPath and relativePath):

```
/// read accessor for fullPath
SP_CLASS_ATTR_GET(DataFileName, fullPath)(PyObject *self, void*)
{
    DataFileName* dataFilename = get_DataFileName( self );;
    return PyString_FromString(dataFilename->getFullPath().c_str());
}

/// read accessor for relativePath
SP_CLASS_ATTR_GET(DataFileName, relativePath)(PyObject *self, void*)
{
    DataFileName* dataFilename = get_DataFileName( self );;
    return PyString_FromString(dataFilename->getRelativePath().c_str());
}
```

These functions will make the values fullPath and relativePath accessible from python:

```python
print myComponent.myDatFileName.fullPath
print myComponent.myDatFileName.relativePath
```

Once implemented, these methods must be passed to cPython in a structure called [`PyGetSetDef`](https://docs.python.org/2/c-api/structures.html#c.PyGetSetDef) that defines the property access. This is encapsulated inside macros in Sofa, and done using the following code:

```cpp

SP_CLASS_ATTRS_BEGIN(DataFileName) // Open Attributes declaration
SP_CLASS_ATTR(DataFileName,fullPath) // declare attribute fullPath
SP_CLASS_ATTR(DataFileName,relativePath) // declare attribute relativePath
SP_CLASS_ATTRS_END // close Attributes declaration

// The same can be done for methods, if you want any to be accessed from python:
SP_CLASS_METHODS_BEGIN(DataFileName)
SP_CLASS_METHODS_END
```

Finally, the whole class type must be declared. Depending on the complexity of the binding of your class type (without any attributes, with attributes and methods, with inheritance, with constructor / destructor etc..)

For our DataFileName type, we will use the following definition macro:
```cpp
SP_CLASS_TYPE_PTR_ATTR(DataFileName, BaseData, Data);
```
All those macros are declared in [PythonMacros.h](https://www.sofa-framework.org/api/SofaPython/_python_macros_8h.html)


Declaring and Registering your bindings to SOFA's Python Factory
-----------------------

Now that you implemented your python bindings, you will need to register them to SOFA's python object factory, to make them available in your python scripts. This is done in the plugin's external modules initialization function (usually in a "initplugin.cpp" file):

```cpp
#ifdef SOFA_HAVE_SOFAPYTHON
#include <SofaPython/PythonFactory.h>
#include "Binding_DataFileName.h"
#endif

[...]

void initExternalModule()
{
  static bool first = true;
  if (first)
  {
    first = false;
#ifdef SOFA_HAVE_SOFAPYTHON
    if (PythonFactory::s_sofaPythonModule)
    {
      simulation::PythonEnvironment::gil lock(__func__);

      // adding new bindings for Data<DataFileName>
      SP_ADD_CLASS_IN_FACTORY(cvMatData, sofa::Data<DataFileName>)
    }
#endif
  }
}

```



