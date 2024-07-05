# DisplacementMatrixEngine

Converts a vector of Rigid to a vector of displacement matrices.


__Templates__:

- `#!c++ Rigid3d`

__Target__: `Sofa.Component.Engine.Transform`

__namespace__: `#!c++ sofa::component::engine::transform`

__parents__: 

- `#!c++ DisplacementTransformEngine`

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
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>x0</td>
		<td>
Rest position
</td>
		<td></td>
	</tr>
	<tr>
		<td>x</td>
		<td>
Current position
</td>
		<td></td>
	</tr>
	<tr>
		<td>scales</td>
		<td>
Scale transformation added to the rigid transformation
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>displaceMats</td>
		<td>
Displacement transforms with respect to original rigid positions
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



## Examples

Component/Engine/Transform/DisplacementMatrixEngine.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node 	 name="root"  dt="0.01" animate="1" >
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [LinearMovementProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Transform"/> <!-- Needed to use components [DisplacementTransformEngine] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Forward"/> <!-- Needed to use components [EulerExplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="Sofa.GL.Component.Shader"/> <!-- Needed to use components [OglFloat4Attribute OglInt4Attribute OglMatrix4VectorVariable OglShader] -->
    
        <DefaultAnimationLoop/>
        <EulerExplicitSolver name="odesolver"  />
        <Node 	 name="DeformableObject"   >
            <MechanicalObject template="Rigid3" name="Bones"  position="0 -2 0 0 0 0 1 0 2 0 0 0 0 1" rest_position="0 -2 0 0 0 0 1 0 2 0 0 0 0 1"  showObject="1"  showObjectScale="0.5" />
            <LinearMovementProjectiveConstraint template="Rigid3" name="BoneTrajectories"  indices="1"  keyTimes="0 1 2 3 4 5 6 7 8 9 10 11 12 20"  movements=" 0 0 0 0 0 0 0 0 0 1.5708 0 0 0 0 0 0 0 0 0 0 0 0 1.5708 0 0 0 0 0 0 0 0 0 0 0 0 1.5708 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0" />
            <Node 	 name="StaticMesh" >
                <MechanicalObject template="Vec3" name="2"  position="-1 -2 0 1 -2 0 -1 0 0 1 0 0 -1 2 0 1 2 0"    />
                <MeshTopology   triangles="0 1 2  2 1 3  2 3 4  4 3 5 " />
                <Node 	 name="GPUMesh"  >
                   <OglModel template="Vec3"  />
                    <IdentityMapping template="Vec3,Vec3" mapForces="0"  mapConstraints="0"  mapMasses="0"   />
                    <DisplacementTransformEngine name="BoneDisplacements" template="Rigid3,Mat4x4"  x0="@../../Bones.rest_position"  x="@../../Bones.position"   />
                    <OglShader name="SkinningShader" fileFragmentShaders="['shaders/linearBlendSkinning.frag']" fileVertexShaders="['shaders/linearBlendSkinning.vert']"/>
                    <OglMatrix4VectorVariable  id="boneMatrix"  value="@BoneDisplacements.displacements"  transpose="1" />
                    <OglInt4Attribute   id="indices"  value="0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 1 0 0 0 1 0 0 0" />
                    <OglFloat4Attribute id="weights"  value="1 0 0 0 1 0 0 0 0.5 0.5 0 0 0.5 0.5 0 0 1 0 0 0 1 0 0 0" />
                </Node>
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01", animate="1")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Transform")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Forward")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Shader")
        root.addObject('DefaultAnimationLoop')
        root.addObject('EulerExplicitSolver', name="odesolver")

        DeformableObject = root.addChild('DeformableObject')
        DeformableObject.addObject('MechanicalObject', template="Rigid3", name="Bones", position="0 -2 0 0 0 0 1 0 2 0 0 0 0 1", rest_position="0 -2 0 0 0 0 1 0 2 0 0 0 0 1", showObject="1", showObjectScale="0.5")
        DeformableObject.addObject('LinearMovementProjectiveConstraint', template="Rigid3", name="BoneTrajectories", indices="1", keyTimes="0 1 2 3 4 5 6 7 8 9 10 11 12 20", movements=" 0 0 0 0 0 0 0 0 0 1.5708 0 0 0 0 0 0 0 0 0 0 0 0 1.5708 0 0 0 0 0 0 0 0 0 0 0 0 1.5708 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0")

        StaticMesh = DeformableObject.addChild('StaticMesh')
        StaticMesh.addObject('MechanicalObject', template="Vec3", name="2", position="-1 -2 0 1 -2 0 -1 0 0 1 0 0 -1 2 0 1 2 0")
        StaticMesh.addObject('MeshTopology', triangles="0 1 2  2 1 3  2 3 4  4 3 5 ")

        GPUMesh = StaticMesh.addChild('GPUMesh')
        GPUMesh.addObject('OglModel', template="Vec3")
        GPUMesh.addObject('IdentityMapping', template="Vec3,Vec3", mapForces="0", mapConstraints="0", mapMasses="0")
        GPUMesh.addObject('DisplacementTransformEngine', name="BoneDisplacements", template="Rigid3,Mat4x4", x0="@../../Bones.rest_position", x="@../../Bones.position")
        GPUMesh.addObject('OglShader', name="SkinningShader", fileFragmentShaders="['shaders/linearBlendSkinning.frag']", fileVertexShaders="['shaders/linearBlendSkinning.vert']")
        GPUMesh.addObject('OglMatrix4VectorVariable', id="boneMatrix", value="@BoneDisplacements.displacements", transpose="1")
        GPUMesh.addObject('OglInt4Attribute', id="indices", value="0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 1 0 0 0 1 0 0 0")
        GPUMesh.addObject('OglFloat4Attribute', id="weights", value="1 0 0 0 1 0 0 0 0.5 0.5 0 0 0.5 0.5 0 0 1 0 0 0 1 0 0 0")
    ```

