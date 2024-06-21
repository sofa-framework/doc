# SubsetMultiMapping

Compute a subset of the input MechanicalObjects according to a dof index list
Compute a subset of the input MechanicalObjects according to a dof index list


__Templates__:

- `#!c++ CudaRigid3d,CudaRigid3d`
- `#!c++ CudaRigid3d,CudaVec3d`
- `#!c++ CudaRigid3f,CudaRigid3f`
- `#!c++ CudaRigid3f,CudaVec3f`
- `#!c++ CudaVec1d,CudaVec1d`
- `#!c++ CudaVec1f,CudaVec1f`
- `#!c++ CudaVec3d,CudaVec3d`
- `#!c++ CudaVec3f,CudaVec3f`

__Target__: `SofaCUDA`

__namespace__: `#!c++ sofa::component::mapping::linear`

__parents__: 

- `#!c++ CRTPLinearMapping`

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
		<td>indexPairs</td>
		<td>
list of couples (parent index + index in the parent)
</td>
		<td></td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|input|Input Object(s)|
|output|Output Object(s)|



## Examples

Component/Mapping/Linear/SubsetMultiMapping.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.02" gravity="0 0 0">
    
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [SphereCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [GridMeshCreator] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [SubsetMultiMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [ConstantForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <VisualStyle displayFlags="showBehaviorModels showCollisionModels showForceFields" />
        
        <CollisionPipeline/>
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <DiscreteIntersection/>
        <DefaultAnimationLoop/>
        
        
        <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
        <CGLinearSolver iterations="25" tolerance="1e-5" threshold="1e-5"/>
        
        
        <Node name="object1">        
            <GridMeshCreator name="loader" filename="nofile" resolution="2 2" />
            <MeshTopology src="@loader" />
            <MechanicalObject template="Vec3" src="@loader" name="dof1" />
    
            <Node name="object2">        
                <GridMeshCreator name="loader" filename="nofile" resolution="2 2" translation="2 0 0" />
                <MeshTopology src="@loader" />
                <MechanicalObject template="Vec3" src="@loader"  name="dof2"/>
                
                <Node name="concatenation">
                    <MechanicalObject template="Vec3" name="dofall" showObject="1"/>
                    <SubsetMultiMapping template="Vec3,Vec3" input="@../../dof1 @../dof2" output="@./dofall" indexPairs="0 0 0 1 1 0 1 1"/>
                    <SphereCollisionModel radius="0.3" selfCollision="1"/>
                    <UniformMass vertexMass="1" />
                    <ConstantForceField indices="0" forces="1 0 0"/>
                </Node>
                
            </Node>
        
        </Node>
    
        <!--    converting  Rigid -> Vec in SubsetMultiMapping  -->
        <Node name="rigid1" activated="1">
            <GridMeshCreator name="loader" filename="nofile" resolution="2 2"  translation="0 2 0"/>
            <MeshTopology src="@loader" />
            <MechanicalObject template="Rigid3" src="@loader" name="dof1" />
    
            <Node name="origid2">
                <GridMeshCreator name="loader" filename="nofile" resolution="2 2" translation="2 2 0" />
                <MeshTopology src="@loader" />
                <MechanicalObject template="Rigid3" src="@loader"  name="dof2"/>
    
                <Node name="concatenation">
                    <MechanicalObject template="Vec3" name="dofall" showObject="1"/>
                    <SubsetMultiMapping template="Rigid3,Vec3" input="@../../dof1 @../dof2" output="@./dofall" indexPairs="0 0 0 1 1 0 1 1"/>
                    <SphereCollisionModel radius="0.3" selfCollision="1"/>
                    <UniformMass vertexMass="1" />
                    <ConstantForceField indices="0" forces="1 0 0"/>
                </Node>
    
            </Node>
    
        </Node>
            
        
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02", gravity="0 0 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showCollisionModels showForceFields")
        root.addObject('CollisionPipeline')
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField")
        root.addObject('DiscreteIntersection')
        root.addObject('DefaultAnimationLoop')
        root.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
        root.addObject('CGLinearSolver', iterations="25", tolerance="1e-5", threshold="1e-5")

        object1 = root.addChild('object1')
        object1.addObject('GridMeshCreator', name="loader", filename="nofile", resolution="2 2")
        object1.addObject('MeshTopology', src="@loader")
        object1.addObject('MechanicalObject', template="Vec3", src="@loader", name="dof1")

        object2 = object1.addChild('object2')
        object2.addObject('GridMeshCreator', name="loader", filename="nofile", resolution="2 2", translation="2 0 0")
        object2.addObject('MeshTopology', src="@loader")
        object2.addObject('MechanicalObject', template="Vec3", src="@loader", name="dof2")

        concatenation = object2.addChild('concatenation')
        concatenation.addObject('MechanicalObject', template="Vec3", name="dofall", showObject="1")
        concatenation.addObject('SubsetMultiMapping', template="Vec3,Vec3", input="@../../dof1 @../dof2", output="@./dofall", indexPairs="0 0 0 1 1 0 1 1")
        concatenation.addObject('SphereCollisionModel', radius="0.3", selfCollision="1")
        concatenation.addObject('UniformMass', vertexMass="1")
        concatenation.addObject('ConstantForceField', indices="0", forces="1 0 0")

        rigid1 = root.addChild('rigid1', activated="1")
        rigid1.addObject('GridMeshCreator', name="loader", filename="nofile", resolution="2 2", translation="0 2 0")
        rigid1.addObject('MeshTopology', src="@loader")
        rigid1.addObject('MechanicalObject', template="Rigid3", src="@loader", name="dof1")

        origid2 = rigid1.addChild('origid2')
        origid2.addObject('GridMeshCreator', name="loader", filename="nofile", resolution="2 2", translation="2 2 0")
        origid2.addObject('MeshTopology', src="@loader")
        origid2.addObject('MechanicalObject', template="Rigid3", src="@loader", name="dof2")

        concatenation = origid2.addChild('concatenation')
        concatenation.addObject('MechanicalObject', template="Vec3", name="dofall", showObject="1")
        concatenation.addObject('SubsetMultiMapping', template="Rigid3,Vec3", input="@../../dof1 @../dof2", output="@./dofall", indexPairs="0 0 0 1 1 0 1 1")
        concatenation.addObject('SphereCollisionModel', radius="0.3", selfCollision="1")
        concatenation.addObject('UniformMass', vertexMass="1")
        concatenation.addObject('ConstantForceField', indices="0", forces="1 0 0")
    ```

