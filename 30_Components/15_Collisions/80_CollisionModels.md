Collision Models
================

SOFA implements a series of collision primitives called CollisionModel. A CollisionModel contains a list of same-type elements. It can be part of a list of CollisionModels or a hierarchy. Here is a list of them:

- PointCollisionModel
- LineCollisionModel
- TriangleCollisionModel
- SphereCollisionModel
- CylinderCollisionModel

Data
----

All collision models define the following data:

- **active**: boolean defining if the CollisionModel should be considered in the detection
- **moving**: boolean defining if the object associated to this CollisionModel might move during the simulation
- **simulated**: boolean defining if this CollisionModel is attached to a simulation. It is false for immobile or procedurally animated objects that don't use contact forces (no Penality or InteractionConstraint created)
- **selfCollision**: boolean defining if the object can self collide
- **group**: integer ID corresponding to the groups containing this model. No collision can occur between collision models included in a common group (e.g. allowing the same object to have multiple collision models). See info about [collision group](https://www.sofa-framework.org/community/doc/simulation-principles/multi-model-representation/collision/#collision-group)

If you are using a collision response using the Penality method, the following data will be also used:

- **contactStiffness**: defining the stiffness coefficient which will be used to compute the penality force using the interpenetration distance (value) resulting from the collision detection.



Usage
-----

To use a CollisionModel, you must first make sure that the collision node in which the CollisionModel is defined does contain the associated topology (e.g. TriangleSetTopologyContainer if you want to use the TriangleCollisionModel).

Moreover, the collision model is usually mapped to a noce containing the mechanical representation of the object. The collision node should therefore include a mapping.



Example
-------

This component is used as follows in XML format:

``` xml
<TriangleCollisionModel simulated="1" contactStiffness="100" selfCollision="0" group="1"/>
```

or using SofaPython3:

``` python
node.addObject('TriangleCollisionModel', simulated='1', contactStiffness='100', selfCollision='0', group='1')
```

An example scene involving a TriangleCollisionModel is available in [*examples/Components/collision/TriangleModel.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/collision/TriangleModel.scn)
