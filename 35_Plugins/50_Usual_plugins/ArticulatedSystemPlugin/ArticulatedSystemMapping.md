# ArticulatedSystemMapping

Mapping between a set of 6D DOF's and a set of angles (µ) using an articulated hierarchy container. 


__Templates__:

- `#!c++ Vec1d,Rigid3d,Rigid3d`

__Target__: `ArticulatedSystemPlugin`

__namespace__: `#!c++ sofa::component::mapping`

__parents__: 

- `#!c++ Multi2Mapping`

Data: 

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

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|input1|Input Object(s) (1st Data type)|
|input2|Input Object(s) (2st Data type)|
|output|Output Object(s)|
|container|Path to ArticulatedHierarchyContainer.|



## Examples

ArticulatedSystemPlugin/share/sofa/examples/ArticulatedSystemPlugin/ArticulatedSystemMapping.scn

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
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01", gravity="0 -9.81 0")
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
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse')
        root.addObject('CollisionPipeline')
        root.addObject('MinProximityIntersection', alarmDistance="1", contactDistance="0.5")
        root.addObject('DefaultAnimationLoop')
        root.addObject('DefaultVisualManagerLoop')

        root = root.addChild('root')
        root.addObject('EulerImplicitSolver', name="cg odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        root.addObject('CGLinearSolver', iterations="100", name="linear solver", threshold="1e-20", tolerance="1e-20")

        restarticulation = root.addChild('restarticulation')
        restarticulation.addObject('MechanicalObject', name="rest", template="Vec1d", position="0 0 0 0")
        restarticulation.addObject('FixedProjectiveConstraint', indices="0 1 2 3")

        articulation = root.addChild('articulation')
        articulation.addObject('MechanicalObject', name="Articulations", template="Vec1d", position="0 0 0 0")

        articulation = articulation.addChild('articulation')
        articulation.addObject('MechanicalObject', template="Rigid3d", name="DOFs", position="0 0 0  0 0 0 1  1 0 0  0 0 0 1  3 0 0  0 0 0 1  5 0 0  0 0 0 1  7 0 0  0 0 0 1")
        articulation.addObject('BeamFEMForceField', name="FEM", radius="0.1", youngModulus="1e8", poissonRatio="0.45")
        articulation.addObject('MeshTopology', name="lines", lines="0 1 1 2 2 3 3 4 ")
        articulation.addObject('UniformMass', template="Rigid3d", name="mass", vertexMass="0.1 0.1 [1 0 0,0 1 0,0 0 1]")
        articulation.addObject('FixedProjectiveConstraint', template="Rigid3d", name="fixOrigin", indices="0")
        articulation.addObject('ArticulatedSystemMapping', input1="@../Articulations", output="@DOFs")

        Collision = articulation.addChild('Collision')
        Collision.addObject('MechanicalObject', template="Vec3d", position="-1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5")
        Collision.addObject('MeshTopology', lines="0 1 1 2 2 3 3 0 1 5 5 4 4 0 5 6 6 7 7 4 2 6 7 3 8 9 9 10 10 11 11 8 9 13 13 12 12 8 13 14 14 15 15 12 10 14 15 11 16 17 17 18 18 19 19 16 17 21 21 20 20 16 21 22 22 23 23 20 18 22 23 19 24 25 25 26 26 27 27 24 25 29 29 28 28 24 29 30 30 31 31 28 26 30 31 27", triangles="3 1 0 3 2 1 3 6 2 3 7 6 7 5 6 7 4 5 4 1 5 4 0 1 5 1 2 2 6 5 4 7 3 4 3 0 11 9 8 11 10 9 11 14 10 11 15 14 15 13 14 15 12 13 12 9 13 12 8 9 13 9 10 10 14 13 12 15 11 12 11 8 19 17 16 19 18 17 19 22 18 19 23 22 23 21 22 23 20 21 20 17 21 20 16 17 21 17 18 18 22 21 20 23 19 20 19 16 27 25 24 27 26 25 27 30 26 27 31 30 31 29 30 31 28 29 28 25 29 28 24 25 29 25 26 26 30 29 28 31 27 28 27 24")
        Collision.addObject('TriangleCollisionModel')
        Collision.addObject('LineCollisionModel')
        Collision.addObject('RigidMapping', rigidIndexPerPoint="0 8 8 8 8")

        Visu = articulation.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", position="-1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5 -1 -0.5 -0.5 -1 0.5 -0.5 -1 0.5 0.5 -1 -0.5 0.5 1 -0.5 -0.5 1 0.5 -0.5 1 0.5 0.5 1 -0.5 0.5", triangles="3 1 0 3 2 1 3 6 2 3 7 6 7 5 6 7 4 5 4 1 5 4 0 1 5 1 2 2 6 5 4 7 3 4 3 0 11 9 8 11 10 9 11 14 10 11 15 14 15 13 14 15 12 13 12 9 13 12 8 9 13 9 10 10 14 13 12 15 11 12 11 8 19 17 16 19 18 17 19 22 18 19 23 22 23 21 22 23 20 21 20 17 21 20 16 17 21 17 18 18 22 21 20 23 19 20 19 16 27 25 24 27 26 25 27 30 26 27 31 30 31 29 30 31 28 29 28 25 29 28 24 25 29 25 26 26 30 29 28 31 27 28 27 24")
        Visu.addObject('RigidMapping', template="Rigid3d,Vec3d", rigidIndexPerPoint="1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4", input="@..", output="@Visual")
        articulation.addObject('ArticulatedHierarchyContainer')

        articulationCenters = articulation.addChild('articulationCenters')

        articulationCenter1 = articulationCenters.addChild('articulationCenter1')
        articulationCenter1.addObject('ArticulationCenter', parentIndex="0", childIndex="1", posOnParent="0 0 0", posOnChild="-1 0 0", articulationProcess="2")

        articulations = articulationCenter1.addChild('articulations')
        articulations.addObject('Articulation', translation="0", rotation="1", rotationAxis="0 0 1", articulationIndex="0")

        articulationCenter2 = articulationCenters.addChild('articulationCenter2')
        articulationCenter2.addObject('ArticulationCenter', parentIndex="1", childIndex="2", posOnParent="1 0 0", posOnChild="-1 0 0", articulationProcess="2")

        articulations = articulationCenter2.addChild('articulations')
        articulations.addObject('Articulation', translation="0", rotation="1", rotationAxis="0 0 1", articulationIndex="1")

        articulationCenter3 = articulationCenters.addChild('articulationCenter3')
        articulationCenter3.addObject('ArticulationCenter', parentIndex="2", childIndex="3", posOnParent="1 0 0", posOnChild="-1 0 0", articulationProcess="0")

        articulations = articulationCenter3.addChild('articulations')
        articulations.addObject('Articulation', translation="0", rotation="1", rotationAxis="0 0 1", articulationIndex="2")

        articulationCenter4 = articulationCenters.addChild('articulationCenter4')
        articulationCenter4.addObject('ArticulationCenter', parentIndex="3", childIndex="4", posOnParent="1 0 0", posOnChild="-1 0 0", articulationProcess="1")

        articulations = articulationCenter4.addChild('articulations')
        articulations.addObject('Articulation', translation="0", rotation="1", rotationAxis="0 0 1", articulationIndex="3")
        root.addObject('StiffSpringForceField', name="Spring", object1="@articulation", object2="@restarticulation", spring=" 1 1 100.0 1.0 0.0  2 2 100.0 1.0 0.0  3 3 100.0 1.0 0.0")
    ```

