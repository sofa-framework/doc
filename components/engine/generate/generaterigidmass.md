<!-- generate_doc -->
# GenerateRigidMass

An engine computing the RigidMass of a mesh : mass, volume and inertia matrix.


## Rigid3d

Templates:

- Rigid3d

__Target__: Sofa.Component.Engine.Generate

__namespace__: sofa::component::engine::generate

__parents__:

- DataEngine

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
		<td>density</td>
		<td>
input: Density of the object
		</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
input: positions of the vertices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
input: triangles of the mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quads</td>
		<td>
input: quads of the mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td>polygons</td>
		<td>
input: polygons of the mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>rigidMass</td>
		<td>
output: rigid mass computed
		</td>
		<td></td>
	</tr>
	<tr>
		<td>mass</td>
		<td>
output: mass of the mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td>volume</td>
		<td>
output: volume of the mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td>inertiaMatrix</td>
		<td>
output: the inertia matrix of the mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td>massCenter</td>
		<td>
output: the gravity center of the mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td>centerToOrigin</td>
		<td>
output: vector going from the mass center to the space origin
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

GenerateRigidMass.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="Root" gravity="0 0 0" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Engine.Generate"/> <!-- Needed to use components [GenerateRigidMass] -->
        <RequiredPlugin name="Sofa.Component.Engine.Transform"/> <!-- Needed to use components [TransformPosition] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <VisualStyle displayFlags="showVisual showBehaviorModels showWireframe" />
        <DefaultAnimationLoop/>
        <Node name="Livers">
            <Node name="Green Liver">
                <MeshOBJLoader name="loader" filename="mesh/liver-smooth.obj" trianglesGroups="Mesh1  -1 0 4384" />
                <GenerateRigidMass template="Rigid3" name="massEngine" density="1000" position="@loader.position" triangles="@loader.triangles" quads="@loader.quads" />
                <TransformPosition template="Vec3" name="positionEngine" input_position="@loader.position" translation="@massEngine.centerToOrigin" method="translation" />
                <MechanicalObject template="Rigid3" name="RigidObject" translation="@massEngine.massCenter" translation2="-5 10 0" />
                <UniformMass template="Rigid3" name="Mass" vertexMass="@massEngine.rigidMass" showAxisSizeFactor="1" />
                <Node name="VisualNode" tags="Visual">
                    <OglModel template="Vec3" name="Visual" position="@../positionEngine.output_position" normal="@../loader.normals" triangles="@../loader.triangles" material="Default Diffuse 1 0 0.8 0 1 Ambient 1 0.1 0.1 0.1 1 Specular 0 0.5 0.5 0.5 1 Emissive 0 0.5 0.5 0.5 1 Shininess 0 45" />
                    <RigidMapping template="Rigid3,Vec3" name="VisualMapping" input="@.." output="@Visual" />
                </Node>
            </Node>
            <Node name="Red Liver">
                <MeshOBJLoader name="loader" filename="mesh/liver-smooth.obj" trianglesGroups="Mesh1  -1 0 4384" />
                <MechanicalObject template="Rigid3" name="RigidObject" translation2="5 10 0" />
                <UniformMass template="Rigid3" name="Mass" totalMass="1" showAxisSizeFactor="1" />
                <Node name="VisualNode" tags="Visual">
                    <OglModel template="Vec3" name="Visual" position="@../loader.position" normal="@../loader.normals" triangles="@../loader.triangles" material="Default Diffuse 1 0.8 0 0 1 Ambient 1 0.1 0.1 0.1 1 Specular 0 0.5 0.5 0.5 1 Emissive 0 0.5 0.5 0.5 1 Shininess 0 45" />
                    <RigidMapping template="Rigid3,Vec3" name="VisualMapping" input="@.." output="@Visual" />
                </Node>
            </Node>
        </Node>
        <Node name="Dragons">
            <Node name="Green Dragon">
                <MeshOBJLoader name="loader" filename="mesh/dragon_clean.obj" trianglesGroups="Mesh  -1 0 2484" />
                <GenerateRigidMass template="Rigid3" name="massEngine" density="1000" position="@loader.position" triangles="@loader.triangles" quads="@loader.quads" />
                <TransformPosition template="Vec3" name="positionEngine" input_position="@loader.position" translation="@massEngine.centerToOrigin" method="translation" />
                <MechanicalObject template="Rigid3" name="RigidObject" translation="@massEngine.massCenter" translation2="-15 0 0" />
                <UniformMass template="Rigid3" name="Mass" vertexMass="@massEngine.rigidMass" showAxisSizeFactor="1" />
                <Node name="VisualNode" tags="Visual">
                    <OglModel template="Vec3" name="Visual" position="@../positionEngine.output_position" normal="@../loader.normals" triangles="@../loader.triangles" material="Default Diffuse 1 0 0.8 0 1 Ambient 1 0.1 0.1 0.1 1 Specular 0 0.5 0.5 0.5 1 Emissive 0 0.5 0.5 0.5 1 Shininess 0 45" />
                    <RigidMapping template="Rigid3,Vec3" name="VisualMapping" input="@.." output="@Visual" />
                </Node>
            </Node>
            <Node name="Red Dragon 2">
                <MeshOBJLoader name="loader" filename="mesh/dragon_clean.obj" trianglesGroups="Mesh  -1 0 2484" />
                <MechanicalObject template="Rigid3" name="RigidObject" translation2="15 0 0" />
                <UniformMass template="Rigid3" name="Mass" filename="BehaviorModels/dragon_clean.rigid" showAxisSizeFactor="1" />
                <Node name="VisualNode" tags="Visual">
                    <OglModel template="Vec3" name="Visual" position="@../loader.position" normal="@../loader.normals" triangles="@../loader.triangles" material="Default Diffuse 1 0.8 0 0 1 Ambient 1 0.1 0.1 0.1 1 Specular 0 0.5 0.5 0.5 1 Emissive 0 0.5 0.5 0.5 1 Shininess 0 45" />
                    <RigidMapping template="Rigid3,Vec3" name="VisualMapping" input="@.." output="@Visual" />
                </Node>
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('Root', gravity="0 0 0", dt="0.02")

       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Generate")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Transform")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels showWireframe")
       root.addObject('DefaultAnimationLoop', )

       livers = Root.addChild('Livers')

       green__liver = Livers.addChild('Green Liver')

       green__liver.addObject('MeshOBJLoader', name="loader", filename="mesh/liver-smooth.obj", trianglesGroups="Mesh1  -1 0 4384")
       green__liver.addObject('GenerateRigidMass', template="Rigid3", name="massEngine", density="1000", position="@loader.position", triangles="@loader.triangles", quads="@loader.quads")
       green__liver.addObject('TransformPosition', template="Vec3", name="positionEngine", input_position="@loader.position", translation="@massEngine.centerToOrigin", method="translation")
       green__liver.addObject('MechanicalObject', template="Rigid3", name="RigidObject", translation="@massEngine.massCenter", translation2="-5 10 0")
       green__liver.addObject('UniformMass', template="Rigid3", name="Mass", vertexMass="@massEngine.rigidMass", showAxisSizeFactor="1")

       visual_node = Green Liver.addChild('VisualNode', tags="Visual")

       visual_node.addObject('OglModel', template="Vec3", name="Visual", position="@../positionEngine.output_position", normal="@../loader.normals", triangles="@../loader.triangles", material="Default Diffuse 1 0 0.8 0 1 Ambient 1 0.1 0.1 0.1 1 Specular 0 0.5 0.5 0.5 1 Emissive 0 0.5 0.5 0.5 1 Shininess 0 45")
       visual_node.addObject('RigidMapping', template="Rigid3,Vec3", name="VisualMapping", input="@..", output="@Visual")

       red__liver = Livers.addChild('Red Liver')

       red__liver.addObject('MeshOBJLoader', name="loader", filename="mesh/liver-smooth.obj", trianglesGroups="Mesh1  -1 0 4384")
       red__liver.addObject('MechanicalObject', template="Rigid3", name="RigidObject", translation2="5 10 0")
       red__liver.addObject('UniformMass', template="Rigid3", name="Mass", totalMass="1", showAxisSizeFactor="1")

       visual_node = Red Liver.addChild('VisualNode', tags="Visual")

       visual_node.addObject('OglModel', template="Vec3", name="Visual", position="@../loader.position", normal="@../loader.normals", triangles="@../loader.triangles", material="Default Diffuse 1 0.8 0 0 1 Ambient 1 0.1 0.1 0.1 1 Specular 0 0.5 0.5 0.5 1 Emissive 0 0.5 0.5 0.5 1 Shininess 0 45")
       visual_node.addObject('RigidMapping', template="Rigid3,Vec3", name="VisualMapping", input="@..", output="@Visual")

       dragons = Root.addChild('Dragons')

       green__dragon = Dragons.addChild('Green Dragon')

       green__dragon.addObject('MeshOBJLoader', name="loader", filename="mesh/dragon_clean.obj", trianglesGroups="Mesh  -1 0 2484")
       green__dragon.addObject('GenerateRigidMass', template="Rigid3", name="massEngine", density="1000", position="@loader.position", triangles="@loader.triangles", quads="@loader.quads")
       green__dragon.addObject('TransformPosition', template="Vec3", name="positionEngine", input_position="@loader.position", translation="@massEngine.centerToOrigin", method="translation")
       green__dragon.addObject('MechanicalObject', template="Rigid3", name="RigidObject", translation="@massEngine.massCenter", translation2="-15 0 0")
       green__dragon.addObject('UniformMass', template="Rigid3", name="Mass", vertexMass="@massEngine.rigidMass", showAxisSizeFactor="1")

       visual_node = Green Dragon.addChild('VisualNode', tags="Visual")

       visual_node.addObject('OglModel', template="Vec3", name="Visual", position="@../positionEngine.output_position", normal="@../loader.normals", triangles="@../loader.triangles", material="Default Diffuse 1 0 0.8 0 1 Ambient 1 0.1 0.1 0.1 1 Specular 0 0.5 0.5 0.5 1 Emissive 0 0.5 0.5 0.5 1 Shininess 0 45")
       visual_node.addObject('RigidMapping', template="Rigid3,Vec3", name="VisualMapping", input="@..", output="@Visual")

       red__dragon_2 = Dragons.addChild('Red Dragon 2')

       red__dragon_2.addObject('MeshOBJLoader', name="loader", filename="mesh/dragon_clean.obj", trianglesGroups="Mesh  -1 0 2484")
       red__dragon_2.addObject('MechanicalObject', template="Rigid3", name="RigidObject", translation2="15 0 0")
       red__dragon_2.addObject('UniformMass', template="Rigid3", name="Mass", filename="BehaviorModels/dragon_clean.rigid", showAxisSizeFactor="1")

       visual_node = Red Dragon 2.addChild('VisualNode', tags="Visual")

       visual_node.addObject('OglModel', template="Vec3", name="Visual", position="@../loader.position", normal="@../loader.normals", triangles="@../loader.triangles", material="Default Diffuse 1 0.8 0 0 1 Ambient 1 0.1 0.1 0.1 1 Specular 0 0.5 0.5 0.5 1 Emissive 0 0.5 0.5 0.5 1 Shininess 0 45")
       visual_node.addObject('RigidMapping', template="Rigid3,Vec3", name="VisualMapping", input="@..", output="@Visual")
    ```

