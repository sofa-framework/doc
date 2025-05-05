<!-- generate_doc -->
# ArticulatedHierarchyBVHController

Implements a handler that controls the values of the articulations of an articulated hierarchy container using a .bvh file.


__Target__: ArticulatedSystemPlugin

__namespace__: articulatedsystemplugin

__parents__:

- ArticulatedHierarchyController

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
list of the subsets the object belongs to
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
		<td>handleEventTriggersUpdate</td>
		<td>
Event handling frequency controls the controller update frequency
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>articulationsIndices</td>
		<td>
Indices of articulations controlled by the keyboard
		</td>
		<td></td>
	</tr>
	<tr>
		<td>bindingKeys</td>
		<td>
Keys to press to control the articulations
		</td>
		<td></td>
	</tr>
	<tr>
		<td>angleDelta</td>
		<td>
Angle incrementation due to each user interaction
		</td>
		<td>0.01</td>
	</tr>
	<tr>
		<td>propagateUserInteraction</td>
		<td>
Says wether or not the user interaction is local on the articulations, or must be propagated to children recursively
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>useExternalTime</td>
		<td>
use the external time line
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>externalTime</td>
		<td>
 value of the External Time
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

## Examples 

ArticulatedHierarchyBVHController.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -.98 0" dt="0.5">
        <VisualStyle displayFlags="showVisual showBehaviorModels" />
        <RequiredPlugin name="ArticulatedSystemPlugin"/> <!-- Needed to use components [ArticulatedHierarchyBVHController ArticulatedHierarchyContainer ArticulatedSystemMapping] -->
        <RequiredPlugin name="Sofa.Component.AnimationLoop"/> <!-- Needed to use components [FreeMotionAnimationLoop] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Solver"/> <!-- Needed to use components [LCPConstraintSolver] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultVisualManagerLoop />
        <FreeMotionAnimationLoop />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
    
        <MinProximityIntersection name="Proximity" alarmDistance="1.0" contactDistance="0.5" />
        <CollisionResponse name="Response" response="FrictionContactConstraint" />
        <LCPConstraintSolver maxIt="1000" tolerance="0.001" />
        <Node name="articulatedObject1">
            <MechanicalObject name="ArticulatedObject" template="Vec1d" />
            <Node name="6D_DOFs1">
                <MechanicalObject name="6D_Dof" template="Rigid3d" />
                <UniformMass totalMass="0.5" />
                <ArticulatedSystemMapping input1="@../ArticulatedObject" input2="" output="@6D_Dof" />
            </Node>
            <ArticulatedHierarchyContainer filename="bvh/manWalking.bvh" />
            <ArticulatedHierarchyBVHController />
        </Node>
        <Node name="Floor">
            <MeshOBJLoader name="loader" filename="mesh/floor.obj" />
            <OglModel name="FloorV" src="@loader" texturename="textures/floor.bmp" scale="2" dy="-40.0" />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -.98 0", dt="0.5")

       root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels")
       root.addObject('RequiredPlugin', name="ArticulatedSystemPlugin")
       root.addObject('RequiredPlugin', name="Sofa.Component.AnimationLoop")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Solver")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('DefaultVisualManagerLoop', )
       root.addObject('FreeMotionAnimationLoop', )
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="1.0", contactDistance="0.5")
       root.addObject('CollisionResponse', name="Response", response="FrictionContactConstraint")
       root.addObject('LCPConstraintSolver', maxIt="1000", tolerance="0.001")

       articulated_object1 = root.addChild('articulatedObject1')

       articulated_object1.addObject('MechanicalObject', name="ArticulatedObject", template="Vec1d")

       6_d__do_fs1 = articulatedObject1.addChild('6D_DOFs1')

       6_d__do_fs1.addObject('MechanicalObject', name="6D_Dof", template="Rigid3d")
       6_d__do_fs1.addObject('UniformMass', totalMass="0.5")
       6_d__do_fs1.addObject('ArticulatedSystemMapping', input1="@../ArticulatedObject", input2="", output="@6D_Dof")

       articulated_object1.addObject('ArticulatedHierarchyContainer', filename="bvh/manWalking.bvh")
       articulated_object1.addObject('ArticulatedHierarchyBVHController', )

       floor = root.addChild('Floor')

       floor.addObject('MeshOBJLoader', name="loader", filename="mesh/floor.obj")
       floor.addObject('OglModel', name="FloorV", src="@loader", texturename="textures/floor.bmp", scale="2", dy="-40.0")
    ```

