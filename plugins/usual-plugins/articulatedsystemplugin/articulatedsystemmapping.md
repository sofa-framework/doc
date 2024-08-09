---
title: ArticulatedSystemMapping
---

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
<!-- automatically generated doc START -->
<!-- generate_doc -->

Mapping between a set of 6D DOF's and a set of angles (µ) using an articulated hierarchy container. 


## Vec1d,Rigid3d,Rigid3d

Templates:

- Vec1d,Rigid3d,Rigid3d

__Target__: ArticulatedSystemPlugin

__namespace__: sofa::component::mapping

__parents__:

- Multi2Mapping

### Data

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Default value</th>
        </tr>
    </thead>
    <tbody>
	<tr>
		<td>name</td>
		<td>
object name
		</td>
		<td>unnamed</td>
	</tr>
	<tr>
		<td>printLog</td>
		<td>
if true, emits extra messages at runtime.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>tags</td>
		<td>
list of the subsets the objet belongs to
		</td>
		<td></td>
	</tr>
	<tr>
		<td>bbox</td>
		<td>
this object bounding box
		</td>
		<td></td>
	</tr>
	<tr>
		<td>componentState</td>
		<td>
The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
		</td>
		<td>Undefined</td>
	</tr>
	<tr>
		<td>listening</td>
		<td>
if true, handle the events, otherwise ignore the events
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>mapForces</td>
		<td>
Are forces mapped ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapConstraints</td>
		<td>
Are constraints mapped ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapMasses</td>
		<td>
Are masses mapped ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapMatrices</td>
		<td>
Are matrix explicit mapped?
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>applyRestPosition</td>
		<td>
set to true to apply this mapping to restPosition at init
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>indexInput2</td>
		<td>
Corresponding index if the base of the articulated system is attached to input2. Default is last index.
		</td>
		<td>0</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|input1|Input Object(s) (1st Data type)|State&lt;Vec1d&gt;|
|input2|Input Object(s) (2st Data type)|State&lt;Rigid3d&gt;|
|output|Output Object(s)|State&lt;Rigid3d&gt;|
|container|Path to ArticulatedHierarchyContainer.|ArticulatedHierarchyContainer|

## Examples 

ArticulatedSystemMapping.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node dt="0.01" gravity="0 -9.81 0" name="root">
        <RequiredPlugin name="ArticulatedSystemPlugin"/> <!-- Needed to use components [ArticulatedHierarchyContainer ArticulatedSystemMapping Articulation ArticulationCenter] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [BeamFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [StiffSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse />
        <CollisionPipeline />
        <MinProximityIntersection alarmDistance="1" contactDistance="0.5"/>
        <DefaultAnimationLoop />
        <DefaultVisualManagerLoop />
        <Node>
            <EulerImplicitSolver name="cg odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
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
                    <Node name="Collision">
                        <MechanicalObject template="Vec3d" position="-1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5" />
                        <MeshTopology lines="0 1 1 2 2 3 3 0 1 5 5 4 4 0 5 6 6 7 7 4 2 6 7 3 8 9 9 10 10 11 11 8 9 13 13 12 12 8 13 14 14 15 15 12 10 14 15 11 16 17 17 18 18 19 19 16 17 21 21 20 20 16 21 22 22 23 23 20 18 22 23 19 24 25 25 26 26 27 27 24 25 29 29 28 28 24 29 30 30 31 31 28 26 30 31 27" triangles="3 1 0 3 2 1 3 6 2 3 7 6 7 5 6 7 4 5 4 1 5 4 0 1 5 1 2 2 6 5 4 7 3 4 3 0 11 9 8 11 10 9 11 14 10 11 15 14 15 13 14 15 12 13 12 9 13 12 8 9 13 9 10 10 14 13 12 15 11 12 11 8 19 17 16 19 18 17 19 22 18 19 23 22 23 21 22 23 20 21 20 17 21 20 16 17 21 17 18 18 22 21 20 23 19 20 19 16 27 25 24 27 26 25 27 30 26 27 31 30 31 29 30 31 28 29 28 25 29 28 24 25 29 25 26 26 30 29 28 31 27 28 27 24" />
                        <TriangleCollisionModel />
                        <LineCollisionModel />
                        <RigidMapping rigidIndexPerPoint="0 8 8 8 8" />
                    </Node>
                    <Node name="Visu">
                        <OglModel name="Visual" position="-1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5" triangles="3 1 0 3 2 1 3 6 2 3 7 6 7 5 6 7 4 5 4 1 5 4 0 1 5 1 2 2 6 5 4 7 3 4 3 0 11 9 8 11 10 9 11 14 10 11 15 14 15 13 14 15 12 13 12 9 13 12 8 9 13 9 10 10 14 13 12 15 11 12 11 8 19 17 16 19 18 17 19 22 18 19 23 22 23 21 22 23 20 21 20 17 21 20 16 17 21 17 18 18 22 21 20 23 19 20 19 16 27 25 24 27 26 25 27 30 26 27 31 30 31 29 30 31 28 29 28 25 29 28 24 25 29 25 26 26 30 29 28 31 27 28 27 24" />
                        <RigidMapping template="Rigid3d,Vec3d" rigidIndexPerPoint="1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4" input="@.." output="@Visual" />
                    </Node>
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
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 -9.81 0")

       root.addObject('RequiredPlugin', name="ArticulatedSystemPlugin")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', )
       root.addObject('CollisionPipeline', )
       root.addObject('MinProximityIntersection', alarmDistance="1", contactDistance="0.5")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('DefaultVisualManagerLoop', )

       node = root.addChild('node')

       node.addObject('EulerImplicitSolver', name="cg odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       node.addObject('CGLinearSolver', iterations="100", name="linear solver", threshold="1e-20", tolerance="1e-20")

       restarticulation = node.addChild('restarticulation')

       restarticulation.addObject('MechanicalObject', name="rest", template="Vec1d", position="0 0 0 0")
       restarticulation.addObject('FixedProjectiveConstraint', indices="0 1 2 3")

       articulation = node.addChild('articulation')

       articulation.addObject('MechanicalObject', name="Articulations", template="Vec1d", position="0 0 0 0")

       node = articulation.addChild('node')

       node.addObject('MechanicalObject', template="Rigid3d", name="DOFs", position="0 0 0  0 0 0 1  1 0 0  0 0 0 1  3 0 0  0 0 0 1  5 0 0  0 0 0 1  7 0 0  0 0 0 1")
       node.addObject('BeamFEMForceField', name="FEM", radius="0.1", youngModulus="1e8", poissonRatio="0.45")
       node.addObject('MeshTopology', name="lines", lines="0 1 1 2 2 3 3 4 ")
       node.addObject('UniformMass', template="Rigid3d", name="mass", vertexMass="0.1 0.1 [1 0 0,0 1 0,0 0 1]")
       node.addObject('FixedProjectiveConstraint', template="Rigid3d", name="fixOrigin", indices="0")
       node.addObject('ArticulatedSystemMapping', input1="@../Articulations", output="@DOFs")

       collision = node.addChild('Collision')

       collision.addObject('MechanicalObject', template="Vec3d", position="-1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5")
       collision.addObject('MeshTopology', lines="0 1 1 2 2 3 3 0 1 5 5 4 4 0 5 6 6 7 7 4 2 6 7 3 8 9 9 10 10 11 11 8 9 13 13 12 12 8 13 14 14 15 15 12 10 14 15 11 16 17 17 18 18 19 19 16 17 21 21 20 20 16 21 22 22 23 23 20 18 22 23 19 24 25 25 26 26 27 27 24 25 29 29 28 28 24 29 30 30 31 31 28 26 30 31 27", triangles="3 1 0 3 2 1 3 6 2 3 7 6 7 5 6 7 4 5 4 1 5 4 0 1 5 1 2 2 6 5 4 7 3 4 3 0 11 9 8 11 10 9 11 14 10 11 15 14 15 13 14 15 12 13 12 9 13 12 8 9 13 9 10 10 14 13 12 15 11 12 11 8 19 17 16 19 18 17 19 22 18 19 23 22 23 21 22 23 20 21 20 17 21 20 16 17 21 17 18 18 22 21 20 23 19 20 19 16 27 25 24 27 26 25 27 30 26 27 31 30 31 29 30 31 28 29 28 25 29 28 24 25 29 25 26 26 30 29 28 31 27 28 27 24")
       collision.addObject('TriangleCollisionModel', )
       collision.addObject('LineCollisionModel', )
       collision.addObject('RigidMapping', rigidIndexPerPoint="0 8 8 8 8")

       visu = node.addChild('Visu')

       visu.addObject('OglModel', name="Visual", position="-1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5", triangles="3 1 0 3 2 1 3 6 2 3 7 6 7 5 6 7 4 5 4 1 5 4 0 1 5 1 2 2 6 5 4 7 3 4 3 0 11 9 8 11 10 9 11 14 10 11 15 14 15 13 14 15 12 13 12 9 13 12 8 9 13 9 10 10 14 13 12 15 11 12 11 8 19 17 16 19 18 17 19 22 18 19 23 22 23 21 22 23 20 21 20 17 21 20 16 17 21 17 18 18 22 21 20 23 19 20 19 16 27 25 24 27 26 25 27 30 26 27 31 30 31 29 30 31 28 29 28 25 29 28 24 25 29 25 26 26 30 29 28 31 27 28 27 24")
       visu.addObject('RigidMapping', template="Rigid3d,Vec3d", rigidIndexPerPoint="1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4", input="@..", output="@Visual")

       articulation.addObject('ArticulatedHierarchyContainer', )

       articulation_centers = articulation.addChild('articulationCenters')

       articulation_center1 = articulationCenters.addChild('articulationCenter1')

       articulation_center1.addObject('ArticulationCenter', parentIndex="0", childIndex="1", posOnParent="0 0 0", posOnChild="-1 0 0", articulationProcess="2")

       articulations = articulationCenter1.addChild('articulations')

       articulations.addObject('Articulation', translation="0", rotation="1", rotationAxis="0 0 1", articulationIndex="0")

       articulation_center2 = articulationCenters.addChild('articulationCenter2')

       articulation_center2.addObject('ArticulationCenter', parentIndex="1", childIndex="2", posOnParent="1 0 0", posOnChild="-1 0 0", articulationProcess="2")

       articulations = articulationCenter2.addChild('articulations')

       articulations.addObject('Articulation', translation="0", rotation="1", rotationAxis="0 0 1", articulationIndex="1")

       articulation_center3 = articulationCenters.addChild('articulationCenter3')

       articulation_center3.addObject('ArticulationCenter', parentIndex="2", childIndex="3", posOnParent="1 0 0", posOnChild="-1 0 0", articulationProcess="0")

       articulations = articulationCenter3.addChild('articulations')

       articulations.addObject('Articulation', translation="0", rotation="1", rotationAxis="0 0 1", articulationIndex="2")

       articulation_center4 = articulationCenters.addChild('articulationCenter4')

       articulation_center4.addObject('ArticulationCenter', parentIndex="3", childIndex="4", posOnParent="1 0 0", posOnChild="-1 0 0", articulationProcess="1")

       articulations = articulationCenter4.addChild('articulations')

       articulations.addObject('Articulation', translation="0", rotation="1", rotationAxis="0 0 1", articulationIndex="3")

       node.addObject('StiffSpringForceField', name="Spring", object1="@articulation", object2="@restarticulation", spring=" 1 1 100.0 1.0 0.0  2 2 100.0 1.0 0.0  3 3 100.0 1.0 0.0")
    ```


<!-- automatically generated doc END -->
