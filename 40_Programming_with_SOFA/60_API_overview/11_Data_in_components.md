Each SOFA component can define **Data**. These data correspond to properties
of the Components, i.e. member variable of the corresponding C++ class,
which are made available and visible to the rest of the simulation.
Numerical values can thus be stored in components using `core::objectmodel::Data`.

Wrapping values in this template class provides the following features:

-   automatic read/write in scene files
-   connections with other Data or to/from Engines using Links, for
    automatic updates
-   thread-safe access (work in progress)

[Naming convention](https://www.sofa-framework.org/community/doc/programming-with-sofa/guidelines/#naming)
in SOFA specifies that Data name must be preceeded from `d_`.



## Create and use a Data

1. A Data called `d_isEnabled` is usually declared as follows:

    ``` cpp
    //Previous declaration of the Data
    Data<bool> d_isEnabled;
    ```

2.  in the constructor of you class MyClass, initialize the Data

    ``` cpp
    //In Component constructor
    MyComponent():
    d_isEnabled(initData(&d_isEnabled, (bool)true, "isEnabled", "Boolean indicating if the component is enabled"))) //ptr to the data, default value, name used for the parameter (the same that will appear later in the XML/Python file), description of the parameter (its purpose)
    {
    };
    ```

3. and it eventually can be defined in an XML scene file:

    ```xml
    <Node name="Root">
       <MyClass isEnabled="true"/>
    </Node>
    ```


#### Data for standard containers

To ease the use of Data, we already serialized some of the most common
data containers: map, vector, set, list. Instead of using a `std::vector`,
use a `helper::vector`:

``` cpp
Data< helper::vector > d_values;
```

**WARNING**: to use a `vector<vector<int>>`, you must use a
`SVector` instead:

``` cpp
Data< helper::SVector< helper::vector< int> > > d_vecValues;
```

The `SVector` class is basically `helper::vector` with a different serialization: it defines brackets for the beginning and the end of the whole string, plus a comma to separate values.


#### Data for custom types

A Data is template with the type of your option: a boolean, an integer,
... But it is not restricted to the default types; you can put inside a Data
your own class/struct. Your class/struct must implement the
operator `<<` and `>>` in order to be used through an input and
output stream:

``` cpp
struct MyStruct
{
    bool active;
    int  value;

    inline friend std::istream& operator >> ( std::istream& in, MyStruct& s ){
        in >> s.active >> s.value;
        return in;
    }

    inline friend std::ostream& operator << ( std::ostream& out, const MyStruct& s ){
        out << s.active << " " << s.value;
        return out;
    }
};

Data<MyStruct> d_configureStruct;
```

While Data are passed to other components **by copy**, the stream operators are used to display a data field's content, e.g. in the console, in a GUI or simply into a file. This data serialization may also have other uses, such as sending data over the network, through the Communication plugin for instance.





## Data flags

In your C++ code, you can define several features for each Data:

-   `d_isEnabled.setRequired(bool b)` whether the Data has to be set by the user for the owner component to be valid
-   `d_isEnabled.setDisplayed(bool b)` whether this Data should be displayed in GUIs
-   `d_isEnabled.setReadOnly(bool b)` whether this Data is read-only (applicable in the GUI only, no effect in the code itself)
-   `d_isEnabled.setPersistent(bool b)` whether this Data contains persistent information (i.e. should it be exported when saving the scene)
-   `d_isEnabled.setAutoLink(bool b)` whether this data should be autolinked when using the src="" syntax


## Links between Data

It is possible to create a link from a source Data to a target Data of
compatible type, to automatically duplicate the value of the source in
the target. For instance, the indices Data output of a BoxROI engine can
be linked to the indices Data of a FixedConstraint, to constrain the
particles in the box. A source can be connected to several targets. Each
time a source value changes, it sends a dirty message to all its
targets, which recursively propagate the dirty signal if they are the
sources of further links. When a target data value is accessed (see How
to Access Data below), it first checks its dirty state and if necessary,
it updates its value based on the source, recursively.

In XML, links are set using the `@` symbol as in the following example:

```xml
<FixedProjectiveConstraint  indices="@box_roi.indices"/>
```

In C++, links are set using method `BaseData::setParent( BaseData* )`, as
in the following example:

``` cpp
myFixedConstraint->f_indices.setParent(&myBoxRoi->f_indices);
```

Note that for some of the non-simple types (mainly containers), the value of the data is *COW* (Copy-On-Write), i.e. if you link from a (potentially huge) `Data`, this will simply access the data in the same memory location as the original `Data`, and will avoid doing a (potentially costly) copy. But if the linked `Data` is modified, the underlying data will be copied, and the contents will be in two different independent locations.



## How to access Data in the C++ API

The disadvantage of storing values in a Data container, rather than
directly, is to make the value less easily accessible. Different ways of
accessing it are presented in the following.

#### setValue/getValue

To have read-only access to the data, use the method `getValue()`:

``` cpp
//with Data<bool> activeOption;
//and  Data<vector<int>> values;
void MyClass::doOperation()
{
  bool isActive = d_activeOption.getValue();
  const vector< int > &v = d_values.getValue();
  vector< int > newVector;

  if (isActive)
  {
    for( size_t i=0; i<v.size(); i++ )
    {
       newVector.push_back(v[i]);
    }
  }
}
```

To write the value of the data, use the method `setValue(...)`. Such a write access,
triggers the propagation of a dirty flag to all Data connected to this one (see Engine
and Data dependency). This is appropriate for a «one shot» value setting.

``` cpp
//with Data<bool> activeOption;
//and  Data<vector<int>> values;
void MyClass::changeParameters(bool b)
{
  d_activeOption.setValue(b);
  vector< int > newVector(10);
  d_values.setValue(newVector);
  //...
}
```


#### ReadAccessor/WriteAccessor

These objects encapsulate `beginEdit()` and `endEdit()` (described below) in their constructor or
destructor, respectively. This ensures that you do not forget to `endEdit()`
since the WriteAccessor manages it for you (through *RAII*).
This also allows to distinguish read-only and write access. This is
the **preferred** method for accessing arrays in write-access.

``` cpp
//with Data <vector<int>> values;
void MyClass::doOperation()
{
  helper::WriteAccessor<Data< vector< int > > > valuesWriteAccess(d_values);
  //or a more modern version:
  //auto valuesWriteAccess = helper::getWriteAccessor(d_values);

  for( size_t i=0; i<valuesWriteAccess.size(); i++ )
  {
    valuesWriteAccess[i] = 0.0;
  }
}
```

For read access, replace WriteAccessor with ReadAccessor. Here is another example:

``` cpp
//with Data<bool> activeOption;
//and  Data<vector<int>> values;
void MyClass::doOperation()
{
  bool isActive = d_activeOption.getValue();
  helper::ReadAccessor<Data< vector< int > > > valuesReadAccess = d_values;
  //or a more modern version:
  //auto valuesReadAccess = helper::getReadAccessor(d_values);
  vector< int > newVector;

  if (isActive)
  {
    for( size_t i=0; i<v.size(); i++ )
    {
       newVector.push_back(valuesReadAccess[i]);
    }
  }
}
```


#### beginEdit/endEdit

**NB**: _this method is not recommended to use, use ReadAccessor/WriteAccessor instead._

This method is useful when you need to change multiple values (such as
array cells) before to notify the change to other Data, and to prevent
concurrent writing in the same time.

-   `beginEdit()` returns a pointer to the internal data, and records that
    the Data is currently being modified. This allows to implement a
    «lock» against concurrent writing.
-   `endEdit()` unlocks the data and propagate the dirty flag.

The direct use of this method is deprecated, please use the
ReadAccessor/WriteAccessor presented below. This is commonly used while
manipulating vectors of data.

``` cpp
//with Data<vector<int>> values;
void MyClass::manipulatingParameters()
{
  vector<int>& myValues = *values.beginEdit();
  for( size_t i=0; i<myValues.size(); i++ )
  {
     myValues[i] = 0;
  }
  values.endEdit(); // do not forget this !
```

Needlessly to say that, as you are getting a raw pointer to the data, you should proceed with the uttermost attention, especially in a multithreaded code!



#### Using State member types and methods

Class core::State has types and methods to ease the use of accessors.
For example, the second line of the previous example could be written
as:

``` cpp
typename core::behavior::MechanicalState::ReadVecCoord coord1 = mstate1->readPositions();
//or:
//auto coord1 = mstate1->readPositions();
```

#### Using MechanicalParams

In the following example, all the state vectors are obtained from the
local MechanicalState as Data and Data using a MechanicalParam, such as
the current position and velocity of the local object. The force vector
ID is passed explicitly to remind that the result should be stored in
this vector, and an alternative instruction is used, but the force vector
can also be obtained in the same way as the positions and the
velocities. The vectors are then passed to a more concrete (though
virtual) function which processes actual vectors rather than IDs.

``` cpp
template
void ForceField::addForce(const MechanicalParams* mparams, MultiVecDerivId fId )
{
    addForce(mparams, *fId[mstate.get(mparams)].write() , *mparams->readX(mstate), *mparams->readV(mstate));
}
```


