<!-- generate_doc -->
# DisplacementMatrixEngine

Converts a vector of Rigid to a vector of displacement matrices.


## Rigid3d

Templates:

- Rigid3d

__Target__: Sofa.Component.Engine.Transform

__namespace__: sofa::component::engine::transform

__parents__:

- DisplacementTransformEngine

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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|

## Examples 

DisplacementMatrixEngine.scn

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
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", animate="1")

       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Transform")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Forward")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Shader")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('EulerExplicitSolver', name="odesolver")

       deformable_object = root.addChild('DeformableObject')

       deformable_object.addObject('MechanicalObject', template="Rigid3", name="Bones", position="0 -2 0 0 0 0 1 0 2 0 0 0 0 1", rest_position="0 -2 0 0 0 0 1 0 2 0 0 0 0 1", showObject="1", showObjectScale="0.5")
       deformable_object.addObject('LinearMovementProjectiveConstraint', template="Rigid3", name="BoneTrajectories", indices="1", keyTimes="0 1 2 3 4 5 6 7 8 9 10 11 12 20", movements=" 0 0 0 0 0 0 0 0 0 1.5708 0 0 0 0 0 0 0 0 0 0 0 0 1.5708 0 0 0 0 0 0 0 0 0 0 0 0 1.5708 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0")

       static_mesh = DeformableObject.addChild('StaticMesh')

       static_mesh.addObject('MechanicalObject', template="Vec3", name="2", position="-1 -2 0 1 -2 0 -1 0 0 1 0 0 -1 2 0 1 2 0")
       static_mesh.addObject('MeshTopology', triangles="0 1 2  2 1 3  2 3 4  4 3 5 ")

       gpu_mesh = StaticMesh.addChild('GPUMesh')

       gpu_mesh.addObject('OglModel', template="Vec3")
       gpu_mesh.addObject('IdentityMapping', template="Vec3,Vec3", mapForces="0", mapConstraints="0", mapMasses="0")
       gpu_mesh.addObject('DisplacementTransformEngine', name="BoneDisplacements", template="Rigid3,Mat4x4", x0="@../../Bones.rest_position", x="@../../Bones.position")
       gpu_mesh.addObject('OglShader', name="SkinningShader", fileFragmentShaders="['shaders/linearBlendSkinning.frag']", fileVertexShaders="['shaders/linearBlendSkinning.vert']")
       gpu_mesh.addObject('OglMatrix4VectorVariable', id="boneMatrix", value="@BoneDisplacements.displacements", transpose="1")
       gpu_mesh.addObject('OglInt4Attribute', id="indices", value="0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 1 0 0 0 1 0 0 0")
       gpu_mesh.addObject('OglFloat4Attribute', id="weights", value="1 0 0 0 1 0 0 0 0.5 0.5 0 0 0.5 0.5 0 0 1 0 0 0 1 0 0 0")
    ```

