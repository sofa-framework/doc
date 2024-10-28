<!-- generate_doc -->
# Visual3DText

Display 3D camera-oriented text.


__Target__: Sofa.Component.Visual

__namespace__: sofa::component::visual

__parents__:

- VisualModel

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
		<td>enable</td>
		<td>
Display the object or not
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>text</td>
		<td>
Test to display
		</td>
		<td></td>
	</tr>
	<tr>
		<td>position</td>
		<td>
3d position
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>scale</td>
		<td>
text scale
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>color</td>
		<td>
text color. (default=[1.0,1.0,1.0,1.0])
		</td>
		<td>1 1 1 1</td>
	</tr>
	<tr>
		<td>depthTest</td>
		<td>
perform depth test
		</td>
		<td>1</td>
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

Visual3DText.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" >
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [Visual3DText VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <DefaultAnimationLoop/>
        
    	<VisualStyle displayFlags="showVisualModels"/>
            <Visual3DText text="hello world!" position="1 1 1" color="red" scale="2" depthTest="false"/>
            
            <MeshOBJLoader name="meshLoader_0" filename="mesh/dragon.obj" handleSeams="1" />
            <OglModel src="@meshLoader_0"/>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root')

       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showVisualModels")
       root.addObject('Visual3DText', text="hello world!", position="1 1 1", color="red", scale="2", depthTest="false")
       root.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/dragon.obj", handleSeams="1")
       root.addObject('OglModel', src="@meshLoader_0")
    ```

