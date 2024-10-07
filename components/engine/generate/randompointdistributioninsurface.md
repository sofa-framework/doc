<!-- generate_doc -->
# RandomPointDistributionInSurface

Engine distributing points over a surface randomly.


## Vec3d

Templates:

- Vec3d

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
		<td>randomSeed</td>
		<td>
Set a specified seed for random generation (0 for "true pseudo-randomness" 
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>isVisible</td>
		<td>
is Visible ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>minDistanceBetweenPoints</td>
		<td>
Min Distance between 2 points (-1 for true randomness)
		</td>
		<td>0.1</td>
	</tr>
	<tr>
		<td>numberOfInPoints</td>
		<td>
Number of points inside
		</td>
		<td>10</td>
	</tr>
	<tr>
		<td>numberOfTests</td>
		<td>
Number of tests to find if the point is inside or not (odd number)
		</td>
		<td>5</td>
	</tr>
	<tr>
		<td>outPoints</td>
		<td>
Points outside the surface
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawOutputPoints</td>
		<td>
Output points visible ?
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>vertices</td>
		<td>
Vertices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
Triangles indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>inPoints</td>
		<td>
Points inside the surface
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

RandomPointDistributionInSurface.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Engine.Generate"/> <!-- Needed to use components [RandomPointDistributionInSurface] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <VisualStyle displayFlags="showBehaviorModels" />
        <DefaultAnimationLoop/>
        
        <Node name="Random">
            <MeshOBJLoader name="meshLoader" filename="mesh/liver.obj" />
            <MechanicalObject src="@meshLoader"/>
            <RandomPointDistributionInSurface template="Vec3" drawOutputPoints="true"
                vertices="@meshLoader.position" triangles="@meshLoader.triangles" numberOfInPoints="100" numberOfTests="3" minDistanceBetweenPoints="0.1" 
            />
        </Node>
        <Node name="Visu">
            <VisualStyle displayFlags="showWireframe" />
            <MeshOBJLoader name='myLoader' filename='mesh/liver.obj'/>  
            <OglModel src='@myLoader'/>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02")

       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Generate")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="showBehaviorModels")
       root.addObject('DefaultAnimationLoop', )

       random = root.addChild('Random')

       random.addObject('MeshOBJLoader', name="meshLoader", filename="mesh/liver.obj")
       random.addObject('MechanicalObject', src="@meshLoader")
       random.addObject('RandomPointDistributionInSurface', template="Vec3", drawOutputPoints="true", vertices="@meshLoader.position", triangles="@meshLoader.triangles", numberOfInPoints="100", numberOfTests="3", minDistanceBetweenPoints="0.1")

       visu = root.addChild('Visu')

       visu.addObject('VisualStyle', displayFlags="showWireframe")
       visu.addObject('MeshOBJLoader', name="myLoader", filename="mesh/liver.obj")
       visu.addObject('OglModel', src="@myLoader")
    ```

