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
d_isEnabled(initData(&d_isEnabled, (bool)true, "isEnabled", "Boolean indicating if the component is enable"))) //ptr to the data, default value, name used for the parameter (the same that will appear later in the XML/Python file), description of the parameter (its purpose)
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
operator &lt;&lt; and &gt;&gt; in order to be used through an input and
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

While Data are passed to other components **by copy**, the stream operators are used to display a data field's content in the GUI. This data serialization method could also have other uses, such as sending data over the network, through the **Communication plugin** for instance.





## Data flags

In your C++ code, you can define several features for each Data:

-   `d_isEnabled.setRequired(bool b)` whether the Data has to be set by the user for the owner component to be valid
-   `d_isEnabled.setDisplayed(bool b)` whether this Data should be displayed in GUIs
-   `d_isEnabled.setReadOnly(bool b)` whether this Data is read-only
-   `d_isEnabled.setPersistent(bool b)` whether this %Data contains persistent information
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
<FixedConstraint  indices="@box_roi.indices"/>
```

In C++, links are set using method `BaseData::setParent( BaseData* )`, as
in the following example:

``` cpp
myFixedConstraint->f_indices.setParent(&myBoxRoi->f_indices);
```




## How to access Data in the C++ API

The disadvantage of storing values in a Data container, rather than
directly, is to make the value less easily accessible. Different ways of
accessing it are presented in the following.

#### setValue/getValue

To have a read only access to the data, use the method `getValue()`:

``` cpp
//with Data activeOption;
//and  Data > values;
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
To iterate over an array, prefer one of the following methods.

``` cpp
//with Data activeOption;
//and  Data > values;
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
destructor, respectively. These ensures that you do not forget to `endEdit()`
since the WriteAccessor manages it for you.
This also allows to distinguish read-only and write access. This is
the **preferred** method for accessing arrays in write-access.

``` cpp
//with Data > values;
void MyClass::doOperation()
{
  helper::WriteAccessor<Data< vector< int > > > valuesWriteAccess(d_values);
  for( size_t i=0; i<valuesWriteAccess.size(); i++ )
  {
    valuesWriteAccess[i] = 0.0;
  }
}
```

For read access, replace WriteAccessor with ReadAccessor. Here is another example:

``` cpp
//with Data activeOption;
//and  Data > values;
void MyClass::doOperation()
{
  bool isActive = d_activeOption.getValue();
  helper::ReadAccessor<Data< vector< int > > > valuesReadAccess = d_values;
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

**NB**: _this methods are now deprecated, use ReadAccessor/WriteAccessor instead._

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
//with Data > values;
void MyClass::manipulatingParameters()
{
  vector& myValues = *values.beginEdit();
  for( int i=0; i<max; i++ )
  {
     myValues[i] = 0.0;
  }
  values.endEdit();
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


