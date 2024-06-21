# GenerateRigidMass

An engine computing the RigidMass of a mesh : mass, volume and inertia matrix.


__Templates__:

- `#!c++ Rigid3d`

__Target__: `Sofa.Component.Engine.Generate`

__namespace__: `#!c++ sofa::component::engine::generate`

__parents__: 

- `#!c++ DataEngine`

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

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|



## Examples

Component/Engine/Generate/GenerateRigidMass.scn

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
    def createScene(rootNode):

        Root = rootNode.addChild('Root', gravity="0 0 0", dt="0.02")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Generate")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Transform")
        Root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        Root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        Root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        Root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels showWireframe")
        Root.addObject('DefaultAnimationLoop')

        Livers = Root.addChild('Livers')

        Green Liver = Livers.addChild('Green Liver')
        Green Liver.addObject('MeshOBJLoader', name="loader", filename="mesh/liver-smooth.obj", trianglesGroups="Mesh1  -1 0 4384")
        Green Liver.addObject('GenerateRigidMass', template="Rigid3", name="massEngine", density="1000", position="@loader.position", triangles="@loader.triangles", quads="@loader.quads")
        Green Liver.addObject('TransformPosition', template="Vec3", name="positionEngine", input_position="@loader.position", translation="@massEngine.centerToOrigin", method="translation")
        Green Liver.addObject('MechanicalObject', template="Rigid3", name="RigidObject", translation="@massEngine.massCenter", translation2="-5 10 0")
        Green Liver.addObject('UniformMass', template="Rigid3", name="Mass", vertexMass="@massEngine.rigidMass", showAxisSizeFactor="1")

        VisualNode = Green Liver.addChild('VisualNode', tags="Visual")
        VisualNode.addObject('OglModel', template="Vec3", name="Visual", position="@../positionEngine.output_position", normal="@../loader.normals", triangles="@../loader.triangles", material="Default Diffuse 1 0 0.8 0 1 Ambient 1 0.1 0.1 0.1 1 Specular 0 0.5 0.5 0.5 1 Emissive 0 0.5 0.5 0.5 1 Shininess 0 45")
        VisualNode.addObject('RigidMapping', template="Rigid3,Vec3", name="VisualMapping", input="@..", output="@Visual")

        Red Liver = Livers.addChild('Red Liver')
        Red Liver.addObject('MeshOBJLoader', name="loader", filename="mesh/liver-smooth.obj", trianglesGroups="Mesh1  -1 0 4384")
        Red Liver.addObject('MechanicalObject', template="Rigid3", name="RigidObject", translation2="5 10 0")
        Red Liver.addObject('UniformMass', template="Rigid3", name="Mass", totalMass="1", showAxisSizeFactor="1")

        VisualNode = Red Liver.addChild('VisualNode', tags="Visual")
        VisualNode.addObject('OglModel', template="Vec3", name="Visual", position="@../loader.position", normal="@../loader.normals", triangles="@../loader.triangles", material="Default Diffuse 1 0.8 0 0 1 Ambient 1 0.1 0.1 0.1 1 Specular 0 0.5 0.5 0.5 1 Emissive 0 0.5 0.5 0.5 1 Shininess 0 45")
        VisualNode.addObject('RigidMapping', template="Rigid3,Vec3", name="VisualMapping", input="@..", output="@Visual")

        Dragons = Root.addChild('Dragons')

        Green Dragon = Dragons.addChild('Green Dragon')
        Green Dragon.addObject('MeshOBJLoader', name="loader", filename="mesh/dragon_clean.obj", trianglesGroups="Mesh  -1 0 2484")
        Green Dragon.addObject('GenerateRigidMass', template="Rigid3", name="massEngine", density="1000", position="@loader.position", triangles="@loader.triangles", quads="@loader.quads")
        Green Dragon.addObject('TransformPosition', template="Vec3", name="positionEngine", input_position="@loader.position", translation="@massEngine.centerToOrigin", method="translation")
        Green Dragon.addObject('MechanicalObject', template="Rigid3", name="RigidObject", translation="@massEngine.massCenter", translation2="-15 0 0")
        Green Dragon.addObject('UniformMass', template="Rigid3", name="Mass", vertexMass="@massEngine.rigidMass", showAxisSizeFactor="1")

        VisualNode = Green Dragon.addChild('VisualNode', tags="Visual")
        VisualNode.addObject('OglModel', template="Vec3", name="Visual", position="@../positionEngine.output_position", normal="@../loader.normals", triangles="@../loader.triangles", material="Default Diffuse 1 0 0.8 0 1 Ambient 1 0.1 0.1 0.1 1 Specular 0 0.5 0.5 0.5 1 Emissive 0 0.5 0.5 0.5 1 Shininess 0 45")
        VisualNode.addObject('RigidMapping', template="Rigid3,Vec3", name="VisualMapping", input="@..", output="@Visual")

        Red Dragon 2 = Dragons.addChild('Red Dragon 2')
        Red Dragon 2.addObject('MeshOBJLoader', name="loader", filename="mesh/dragon_clean.obj", trianglesGroups="Mesh  -1 0 2484")
        Red Dragon 2.addObject('MechanicalObject', template="Rigid3", name="RigidObject", translation2="15 0 0")
        Red Dragon 2.addObject('UniformMass', template="Rigid3", name="Mass", filename="BehaviorModels/dragon_clean.rigid", showAxisSizeFactor="1")

        VisualNode = Red Dragon 2.addChild('VisualNode', tags="Visual")
        VisualNode.addObject('OglModel', template="Vec3", name="Visual", position="@../loader.position", normal="@../loader.normals", triangles="@../loader.triangles", material="Default Diffuse 1 0.8 0 0 1 Ambient 1 0.1 0.1 0.1 1 Specular 0 0.5 0.5 0.5 1 Emissive 0 0.5 0.5 0.5 1 Shininess 0 45")
        VisualNode.addObject('RigidMapping', template="Rigid3,Vec3", name="VisualMapping", input="@..", output="@Visual")
    ```

