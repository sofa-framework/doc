Wrap your own Data types for Python
----------------------------------

If you are using SofaPython to create your scenes, you are probably interested in accessing your component's data fields and reading / writing their values from python, as done in the example below:

```python
 # Modify a scalar data field from Python
  self.myComponent.findData('integerValue').value = 1

 # Modify a complex data field from Python
  self.myMecaObject.findData('position').value=str(x)+' '+str(y)+' '+str(z)+' 0 0 0 1'
```

This is possible, because the Data `integerValue` from `myComponent` is a scalar, and SofaPython provides natively the access to those Data types. In addition to Scalars, SofaPython also provides a python wrapper for more complex types such as `defaulttype::Vec<T, real>` or `defaulttype::Matrix<T>`, but also containers classes such as `helper::vector` or `helper::SVector` for instance.

In order to get python support for your [custom Data types](../../programming-with-sofa/api-overview/data-in-components/#data-for-custom-types), you will need to implement bindings for your custom type. This is done by:

1. Implementing data / methods accessors and bindings in CPython
2. Declaring and Registering your bindings to SOFA's Python Factory


As an example, we will consider the native SOFA type [`DataFileName`](https://www.sofa-framework.org/api/SOFA/classsofa_1_1core_1_1objectmodel_1_1_data_file_name.html), whose bindings are implemented in the SofaPython plugin.
In any case, it is very informative to look into the "native" binding implementations present in the SofaPython plugin.

An overview of the complete code for this example can be found at the end of this page.



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

Getters / Setters are implemented to read attribute values from the DataFileName structure (fullPath and relativePath):

```
/// read accessor for fullPath
SP_CLASS_ATTR_GET(DataFileName, fullPath)(PyObject *self, void*)
{
    DataFileName* dataFilename = get_DataFileName( self );;
    return PyString_FromString(dataFilename->getFullPath().c_str());
}

SP_CLASS_ATTR_SET(DataFileName, fullPath)(PyObject */*self*/, PyObject * /*args*/, void*)
{
    SP_MESSAGE_ERROR("fullPath attribute is read only")
        PyErr_BadArgument();
    return -1;
}

/// read accessor for relativePath
SP_CLASS_ATTR_GET(DataFileName, relativePath)(PyObject *self, void*)
{
    DataFileName* dataFilename = get_DataFileName( self );;
    return PyString_FromString(dataFilename->getRelativePath().c_str());
}

SP_CLASS_ATTR_SET(DataFileName, relativePath)(PyObject */*self*/, PyObject * /*args*/, void*)
{
    SP_MESSAGE_ERROR("relativePath attribute is read only")
        PyErr_BadArgument();
    return -1;
}

```

These functions will make the values fullPath and relativePath accessible from python as such:

```python
print myComponent.myDatFileName.fullPath
print myComponent.myDatFileName.relativePath
```

Once implemented, these methods must be passed to cPython in a structure called [`PyGetSetDef`](https://docs.python.org/2/c-api/structures.html#c.PyGetSetDef) that defines the property access. This is encapsulated inside macros in Sofa, and done using the following code:

```cpp

SP_CLASS_ATTRS_BEGIN(DataFileName) // Open Attributes declaration
SP_CLASS_ATTR(DataFileName,fullPath) // declare attribute fullPath and references both the getter and setter method for this attribute
SP_CLASS_ATTR(DataFileName,relativePath) // declare attribute relativePath and references both the getter and setter method for this attribute
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
      SP_ADD_CLASS_IN_FACTORY(DataFileName, sofa::Data<DataFileName>)
    }
#endif
  }
}

```


Here's the complete code for this example:

_Binding_DataFileName.h_

```
#ifndef BINDING_DataFileName_H
#define BINDING_DataFileName_H

#include "PythonMacros.h"
#include <sofa/core/objectmodel/DataFileName.h>

SP_DECLARE_CLASS_TYPE(DataFileName)

#endif
```

_Binding_DataFileName.cpp_

```
#include "Binding_DataFileName.h"
#include "Binding_Data.h"
#include "PythonToSofa.inl"


using namespace sofa::core::objectmodel;

/// getting a DataFileName* from a PyObject*
static inline DataFileName* get_DataFileName(PyObject* obj) {
    return sofa::py::unwrap<DataFileName>(obj);
}


SP_CLASS_ATTR_GET(DataFileName, fullPath)(PyObject *self, void*)
{
    DataFileName* dataFilename = get_DataFileName( self );;
    return PyString_FromString(dataFilename->getFullPath().c_str());
}


SP_CLASS_ATTR_SET(DataFileName, fullPath)(PyObject */*self*/, PyObject * /*args*/, void*)
{
    SP_MESSAGE_ERROR("fullPath attribute is read only")
        PyErr_BadArgument();
    return -1;
}


SP_CLASS_ATTR_GET(DataFileName, relativePath)(PyObject *self, void*)
{
    DataFileName* dataFilename = get_DataFileName( self );;
    return PyString_FromString(dataFilename->getRelativePath().c_str());
}


SP_CLASS_ATTR_SET(DataFileName, relativePath)(PyObject */*self*/, PyObject * /*args*/, void*)
{
    SP_MESSAGE_ERROR("relativePath attribute is read only")
        PyErr_BadArgument();
    return -1;
}


SP_CLASS_ATTRS_BEGIN(DataFileName)
SP_CLASS_ATTR(DataFileName,fullPath)
SP_CLASS_ATTR(DataFileName,relativePath)
SP_CLASS_ATTRS_END


SP_CLASS_METHODS_BEGIN(DataFileName)
SP_CLASS_METHODS_END

SP_CLASS_TYPE_PTR_ATTR(DataFileName, BaseData, Data);

```

_initplugin.cpp_

```
/// initplugin.cpp
#include <SofaPython/PythonFactory.h>
#include "Binding_DataFileName.h"

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
      SP_ADD_CLASS_IN_FACTORY(DataFileName, sofa::Data<DataFileName>)
    }
#endif
  }
}
```
