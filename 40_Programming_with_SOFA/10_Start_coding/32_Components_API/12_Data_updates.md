This section defines the different update mechanisms present in SOFA:
- updates within the Data-dependency graph
- updates of Engines
- updates of internal Data within components


Data-dependency graph
---------------------

As you know from the [Data documentation](https://www.sofa-framework.org/community/doc/programming-with-sofa/start-coding/components-api/components-and-datas/), it is possible to link Data. These connections create a so-called Data-Dependency Graph (DDG). Each element of this data-dependency graph is a DDGNode. It must be clear that **DDGNode has nothing to do with graph Nodes**. Graph Nodes belong to the scene graph (visible in the SOFA GUI) while DDGNodes belong to the Data-dependency graph due to Data linked together and hidden to the user.


DDGNode is the base class which makes possible to define "input" and "output". The declaration of an input is done using the `addInput()` function, an output using the `addOutput()` function. Data and Engines inherit from this class DDGNode. A DDGNode also integrates a "dirty" state flag, helper methods to handle it (see following subsection) and a virtual pure `update()` method.

Whenever an output DDGNode of a class is accessed (e.g. using the function `getValue()`), while the associated input DDGNode is dirty (dirty = the DDGNode or one of its DDG-parents has been modified), it triggers an update mechanism. First, it recursively checks if the parent DDGNode is dirty. Once the last dirty parent is found, the function update() is called in this DDGNode. Then, the child are updated one after another. This automatic update therefore makes sure that all dirty parents are updated before updating the current DDGNode.



### API functions for the update mechanism

``` cpp
/// Indicate the value needs to be updated
void setDirtyValue()

/// Indicate the outputs needs to be updated
void setDirtyOutputs()

/// Returns the flag dirty
bool setDirtyOutputs()

/// Utility method to call update() if necessary. This method should be called before reading of writing the value of this node.
void updateIfDirty()

/// Function implementing the update computation and then calling cleanDirty()
void update()

/// Set dirty flag to false
void cleanDirty()
```


### Example

Let's take an example to illustrate the update mechanism. Each circle in the following diagrams corresponds to a DDGNode. Each arrow binding two circles depicts a link between two DDGNodes (output of A → input of B). The red colors corresponds to the flag `dirty=true` while green corresponds to  `dirty=false`.

<a href="https://github.com/sofa-framework/doc/blob/master/Images/dataupdate/DDGNodes-1.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/Images/dataupdate/DDGNodes-1.png?raw=true" title="A is modified, then set to dirty"/></a>

Let's consider that **B** has been modified. Therefore, a `setDirtyValue()` is automatically called, thus triggering the `setDirtyOutputs()` on its outputs **C** and **D** and calling `setDirtyValue()`. Recursively, the dirty state spreads to **E**.

<a href="https://github.com/sofa-framework/doc/blob/master/Images/dataupdate/DDGNodes-2.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/Images/dataupdate/DDGNodes-2.png?raw=true" title="Recursive propagation to C and D"/></a>
<a href="https://github.com/sofa-framework/doc/blob/master/Images/dataupdate/DDGNodes-3.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/Images/dataupdate/DDGNodes-3.png?raw=true" title="Dirty state is properly propagated to E"/></a>

Now, if **E** is accessed (call to `getValue()`), the function `updateIfDirty()` is called on inputs of **E**, i.e. to **C** and **D**. Recursively, the function `updateIfDirty()` will look for the last dirty parent: here **B**.

<a href="https://github.com/sofa-framework/doc/blob/master/Images/dataupdate/DDGNodes-4.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/Images/dataupdate/DDGNodes-4.png?raw=true" title="Recursive propagation to C and D"/></a>
<a href="https://github.com/sofa-framework/doc/blob/master/Images/dataupdate/DDGNodes-5.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/Images/dataupdate/DDGNodes-5.png?raw=true" title="Dirty state is properly propagated to E"/></a>

Once the highest parent in the dependency hierarchy is found, the DDGNode is updated and its dirty flag is cleaned (set back to false). This repeats recursively down into the hierarchy.

<a href="https://github.com/sofa-framework/doc/blob/master/Images/dataupdate/DDGNodes-6.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/Images/dataupdate/DDGNodes-6.png?raw=true" title="Recursive propagation to C and D"/></a>
<a href="https://github.com/sofa-framework/doc/blob/master/Images/dataupdate/DDGNodes-7.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/Images/dataupdate/DDGNodes-7.png?raw=true" title="Dirty state is properly propagated to E"/></a>
<a href="https://github.com/sofa-framework/doc/blob/master/Images/dataupdate/DDGNodes-8.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/Images/dataupdate/DDGNodes-8.png?raw=true" title="Recursive propagation to C and D"/></a>
<a href="https://github.com/sofa-framework/doc/blob/master/Images/dataupdate/DDGNodes-9.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/Images/dataupdate/DDGNodes-9.png?raw=true" title="Dirty state is properly propagated to E"/></a>

The information recovered by the `getValue()` therefore returns a fresh up-to-date value and the Data-dependency graph is cleaned.


Update in engines
-----------------

Engines are components aiming at computing a set of Data outputs from a set of Data inputs. Engines inherit from the base class DDGNode but their input/output are nested in the Data fields. As a DDGNode, Engines implement an update mechanism to recompute the output Data when an input Data is dirty or modified. Let's see how this works.

First, the Engine class must specify which Data is an input or an output, respectively using the functions `addInput()` and `addOutput()`. These Data are therefore added to a 'DataTracker'. This DataTracker registers all changes using a counter for each tracked Data. It also implements a callback when one of the tracked data has changed. As for the DDGNode, if an output Data is accessed while an input is dirty, the whole update mechanism takes place.

To make the implementation of the update easier and less error-prone, the `update()` function of an Engine is not left to the developer. The final implementation of the `update()` function is done in the DataEngine class so that:
- it manages the process of update and clean of dirty parents
- it calls a delegate function `doUpdate()`
- it cleans the DataTracker

```cpp
void DataEngine::update() final
{
    updateAllInputs();
    DDGNode::cleanDirty();
    doUpdate(); // Implemented in all engines
    m_dataTracker.clean();
}
```

Only the delegate function `doUpdate()` is therefore left to the user. The user is therefore free to implement the desired update mechanism depending on which tracked Data has been changed. You can find examples of implementation in any Engine, e.g. [TransformEngine](https://www.sofa-framework.org/community/doc/using-sofa/components/engine/roi-engines/).




Update of internal data in other components
-------------------------------------------

In SOFA, components others than Engines do not share the same automatic update of their Data fields. Yet, it is important for several components to be able to recompute internal information when a Data is modified. For example, when the _massDensity_ Data is modified, we want the MeshMatrixMass component to recompute the _totalMass_ and the _vertexMass_ vector defining the mass spread on each vertex.

This update mechanism of internal information is done by the call of the **UpdateInternalDataVisitor** at each begin of step (within any AnimationLoop). This visitor triggers a function `updateInternal()` which manages this internal update. The final implementation of the `updateInternal()` function is done in the BaseObject class so that:
- it checks if at least one the tracked Data of the component has changed
- it calls a delegate function `doUpdateInternal()`
- it cleans the DataTracker

``` cpp
void BaseObject::updateInternal()
{
    const auto& mapTrackedData = m_internalDataTracker.getMapTrackedData();
    for( auto const& it : mapTrackedData )
    {
        it.first->updateIfDirty();
    }

    if(m_internalDataTracker.hasChanged())
    {
        doUpdateInternal();                // left to be implemented in components
        m_internalDataTracker.clean();
    }
}
```

Only the delegate function `doUpdateInternal()` is therefore available in any component to handle internal update. You can find examples of implementation in any Engine, e.g. [MeshMatrixMass](https://www.sofa-framework.org/community/doc/using-sofa/components/masses/meshmatrixmass/).