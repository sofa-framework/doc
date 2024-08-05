# MergeVectors

Apply a merge operation to combine several inputs


__Templates__:

- `#!c++ vector<RigidCoord2d>`
- `#!c++ vector<RigidCoord3d>`
- `#!c++ vector<RigidDeriv2d>`
- `#!c++ vector<RigidDeriv3d>`
- `#!c++ vector<Vec2I>`
- `#!c++ vector<Vec2d>`
- `#!c++ vector<Vec3d>`
- `#!c++ vector<Vec4d>`
- `#!c++ vector<bool>`
- `#!c++ vector<d>`
- `#!c++ vector<i>`

__Target__: `Sofa.Component.Engine.Generate`

__namespace__: `#!c++ sofa::component::engine::generate`

__parents__: 

- `#!c++ DataEngine`

__categories__: 

- Engine

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
		<td>nbInputs</td>
		<td>
Number of input vectors
</td>
		<td>2</td>
	</tr>
	<tr>
		<td>output</td>
		<td>
Output vector
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

Component/Engine/Generate/MergeVectors.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.05" showBoundingTree="0" gravity="0 -9 1">
        
        <RequiredPlugin name="Sofa.Component.Engine.Generate"/> <!-- Needed to use components [MergeVectors] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <VisualStyle displayFlags="showVisual showBehaviorModels" />
        <DefaultAnimationLoop/>
        
        <Node name="mesh">
            
    		<MeshOBJLoader name="mesh1" filename="mesh/raptor_35kp.obj"/>  
                    <MeshOBJLoader name="mesh2" filename="mesh/snake_body.obj"/>  
                    
                    <MergeVectors template="Data<double>" name="mergedPositions"  nbInputs="2" input1="@mesh1.position" input2="@mesh2.position" />
                    <MechanicalObject  template="Vec3"  position="@mergedPositions.output" showObject="True" />
                                    
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.05", showBoundingTree="0", gravity="0 -9 1")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Generate")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels")
        root.addObject('DefaultAnimationLoop')

        mesh = root.addChild('mesh')
        mesh.addObject('MeshOBJLoader', name="mesh1", filename="mesh/raptor_35kp.obj")
        mesh.addObject('MeshOBJLoader', name="mesh2", filename="mesh/snake_body.obj")
        mesh.addObject('MergeVectors', template="Data<double>", name="mergedPositions", nbInputs="2", input1="@mesh1.position", input2="@mesh2.position")
        mesh.addObject('MechanicalObject', template="Vec3", position="@mergedPositions.output", showObject="True")
    ```

