ArticulatedSystemMapping  
========================


This component belongs to the category of Multi2Mapping, which is the interface to describe many to many mapping. It allows for building an articulated system, like for robotics. From each articulation, it becomes therefore possible to compute the global motion of the system.

Each articulation is represented as one degree of freedom (translation or rotation). All articulation DOFs are contained in a MechanicalObject with a `template=Vec1d`. From these local articulation DOFs, the ArticulatedSystemMapping can build a serial chain (arborescent chain).

To compute this mapping, the ArticulatedSystemMapping needs an ArticulatedHierarchyContainer. At the initialization, this component browse the graph and detects to all articulations. The ArticulatedHierarchyContainer therefore contains a link to all pairs of:

- ArticulationCenter: defines the location of the articulation. It can either be defined relatively to the parent and child articulations (in local coordinates), or defined in the global coordinate system (and all local data are automatically computed).
- Articulation: defines the id (integer) and the nature of the articulation, e.g. a translation along the x axis ` translationAxis="1 0 0"` or rotation around the z axis `rotationAxis="0 0 1"`



Data
----

The ArticulatedSystemMapping builds the correspondence the articulations and the global motion of the system. It has therefore only two data:

- **input1** link to the MechanicalObject containing the articulation DOFs (Vec1d)
- **output** link to the MechanicalObject containing the mapped DOFs in the global coordinate system for each rigid body (Rigid3d), i.e. for each part of the articulated system

Note that the ArticulatedSystemMapping can include an *optional* second input, named **input2**. This data is a link to the MechanicalObject containing the rigid position of a moving base (Rigid3d). This is useful if the articulated system is attached on another body (which must be defined higher in the graph).



Usage
-----

This component and this structure works well for simple serial articulations. However, more advanced articulations like ball joint can not be created as is. Moreover, it can be noticed that only the position is given to the ArticulationCenter.
The ArticulatedSystemMapping works well in quasi-static cases.

_Next steps of development:_

- add option of defining a position and a rotation in the ArticulationCenter
- handle more complex articulations than only Vec1d (rotation/translation), like using quaternions
- representing the articulated system as a graph, separated from the scene graph
- load standard format (like urdf)
- validate the dynamic simulations


Example
-------

An example scene involving a ArticulatedSystemMapping is available in [*applications/plugins/ArticulatedSystemPlugin/examples/ArticulatedSystemMapping.scn*](https://github.com/sofa-framework/sofa/blob/master/applications/plugins/ArticulatedSystemPlugin/examples/ArticulatedSystemMapping.scn).


``` xml
<EulerImplicitSolver name="cg odesolver" />
<CGLinearSolver iterations="100" name="linear solver" threshold="1e-20" tolerance="1e-20" />

<Node name="restarticulation">
    <MechanicalObject name="rest" template="Vec1d" position="0 0 0 0" />
    <FixedProjectiveConstraint indices="0 1 2 3" />
</Node>


<Node name="articulation">

    <MechanicalObject name="Articulations" template="Vec1d" position="0 0 0 0" />
    
    <Node>
        <MechanicalObject template="Rigid3d" name="DOFs" position="0 0 0  0 0 0 1  1 0 0  0 0 0 1  3 0 0  0 0 0 1  5 0 0  0 0 0 1  7 0 0  0 0 0 1" />
        <BeamFEMForceField name="FEM" radius="0.1" youngModulus="1e8" poissonRatio="0.45"/>
        <MeshTopology name="lines" lines="0 1 1 2 2 3 3 4 " />
        <UniformMass template="Rigid3d" name="mass" vertexMass="0.1 0.1 [1 0 0,0 1 0,0 0 1]" />
        <FixedProjectiveConstraint template="Rigid3d" name="fixOrigin" indices="0" />
        <ArticulatedSystemMapping input1="@../Articulations" output="@DOFs" />
    </Node>


    <ArticulatedHierarchyContainer />
    

    <Node name="articulationCenters">
        <Node name="articulationCenter1">
            <ArticulationCenter parentIndex="0" childIndex="1" posOnParent="0 0 0" posOnChild="-1 0 0" articulationProcess="2" />
            <Node name="articulations">
                <Articulation translation="0" rotation="1" rotationAxis="0 0 1" articulationIndex="0" />
            </Node>
        </Node>
        <Node name="articulationCenter2">
            <ArticulationCenter parentIndex="1" childIndex="2" posOnParent="1 0 0" posOnChild="-1 0 0" articulationProcess="2" />
            <Node name="articulations">
                <Articulation translation="0" rotation="1" rotationAxis="0 0 1" articulationIndex="1" />
            </Node>
        </Node>
        <Node name="articulationCenter3">
            <ArticulationCenter parentIndex="2" childIndex="3" posOnParent="1 0 0" posOnChild="-1 0 0" articulationProcess="0" />
            <Node name="articulations">
                <Articulation translation="0" rotation="1" rotationAxis="0 0 1" articulationIndex="2" />
            </Node>
        </Node>
        <Node name="articulationCenter4">
            <ArticulationCenter parentIndex="3" childIndex="4" posOnParent="1 0 0" posOnChild="-1 0 0" articulationProcess="1" />
            <Node name="articulations">
                <Articulation translation="0" rotation="1" rotationAxis="0 0 1" articulationIndex="3" />
            </Node>
        </Node>
    </Node>
</Node>

<StiffSpringForceField name="Spring" object1="@articulation" object2="@restarticulation" spring=" 1 1 100.0 1.0 0.0  2 2 100.0 1.0 0.0  3 3 100.0 1.0 0.0" />

```

In this above example, we have five rigid frames, saved in the MechanicalObject "DOFs", connected through four articulations. All four articulations  all corresponds to a rotation around the z axis (see the component Articulation). The MechanicalObject "Articulations" contains the four rotation angles (Vec1d) of each articulation.

Note that the MechanicalObject "DOF" only contains the result of the articulated system, i.e. it contains mapped degrees of freedom (not real degrees of freedom).

The ArticulatedHierarchyContainer must be defined before the description of the articulations. Then, all articulations are made up of a pair: ArticulationCenter+Articulation.

The ArticulationCenter defines the location of the articulation. In the example, the position of one articulation is defined relatively to the position of the others. For instance, the second articulation "articulationCenter2" is located in x+=1 relatively to the first articulation, and x-=1 relatively to the third articulation.

Finally, a StiffSpringForceField is added to enforce each articulation get back to its rest configuration (saved in the MechanicalObject "rest") through elastic forces. This component is optional.
