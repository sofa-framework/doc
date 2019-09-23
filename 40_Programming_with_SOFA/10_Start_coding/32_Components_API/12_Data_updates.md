This section defines the two main update mechanisms of Data in SOFA:
- updates within the Data-dependency graph
- updates of internal Data within components


Data-dependency graph
---------------------

In SOFA, the class DDGNode is the base class which makes possible to define "input" and "output" Data in a component. The declaration of an input Data is done using the `addInput()` function, an output Data using the `addOutput()` function. An ouput Data is a Data resulting from a computation involving one or several input Data. Engines (and graph nodes) inherit from this class DDGNode.

Whenever an output Data of a class is accessed (e.g. using the function `getValue()`), while an associated input Data is dirty (dirty = the Data or one of its parents has been modified), it triggers an update mechanism. This automatic update first updates all dirty parents and Data before updating the component. Every engine implements this 'doUpdate()' function.

When Data are linked from a component to another, this builds a data-dependency graph.


### API functions


/// Indicate the value needs to be updated
setDirtyValue()

/// Indicate the outputs needs to be updated
setDirtyOutputs

/// Set dirty flag to false
cleanDirty()

### Example



Internal data
-------------


