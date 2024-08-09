Engine
======

As explained the documentation page on Data, SOFA allows to connect Data instances (Data link) to keep their value synchronized. An Engine (or DataEngine) is a component which relies on this concept to compute one or several output Data based on one or several input Data.

The specifity of the Engines resides in their update mechanism: output Data are updated based on the input Data through a mechanism of lazy evaluation. Data values which are not up-to-date are recursively flagged as "dirty", but they are recomputed only when necessary. The update (recomputation) only occurs when the Data itself or a Data depending on this Data is accessed.
    
For instance:

- the TransformEngine computes a geometric transformation (rotation, translation,scaling) on input positions (e.g. coming from a MeshLoader) and outputs the transformed position
- based on a bounding box and a vector of coordinates, a BoxROI engine computes the list of indices of the coordinates inside the box. These indices can then be used as input of a FixedConstraint to define a fixed boundary condition. With this design, the simulation can transparently be setup either from data stored in static files, or generated automatically with engines.

Engines are meant to perform relatively simple computations, but can easily be created in a series. The network of interconnected Data objects defines a Data dependency graph, superimposed on the scene graph. This Data dependency graph is not visible within the runSofa GUI.


API of Engines
--------------

The API of engines is pretty simple since only one function is to be implemented (on top of the `init()` function common to all SOFA components):

``` cpp

// Update function in Engines computing the new values of outputs from inputs
void doUpdate()

```

This function is in charge of the computation of the ouput Data based on the input Data. It is the delegate function from the `update()` function implemented in DataEngine which updates all inputs before calling the `doUpdate()` function.



Example of use
--------------

Here is an example with the [TransformEngine](../../components/engine/transform/transformengine/) with an input data ("input_position") and an output data ("output_position") resulting from a transformation defined by the user (here translation):

``` xml
<TransformEngine name="translationEngine" template="Vec3d" translation="10 0 0" input_position="@meshLoader.position" />
<MechanicalObject name="transform" template="Vec3d" position="@translationEngine.output_position" />
```

or in python:

``` python
node.addObject("TransformEngine", name="translationEngine", template="Vec3d", translation="10 0 0", input_position="@meshLoader.position")
node.addObject("MechanicalObject", name="transform", template="Vec3d", position="@translationEngine.output_position")
```
