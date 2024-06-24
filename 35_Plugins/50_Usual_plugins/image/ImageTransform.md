# ImageTransform

Read data from ImageContainer


__Templates__:

- `#!c++ ImageB`
- `#!c++ ImageD`
- `#!c++ ImageUC`

__Target__: `image`

__namespace__: `#!c++ sofa::component::engine`

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
		<td>update</td>
		<td>
Type of update
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Transformation</td>
	</tr>
	<tr>
		<td>translation</td>
		<td>
Translation
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>euler</td>
		<td>
Euler angles
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>scale</td>
		<td>
Voxel size
</td>
		<td>1 1 1</td>
	</tr>
	<tr>
		<td>isPerspective</td>
		<td>
Is perspective?
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>timeOffset</td>
		<td>
Time offset
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>timeScale</td>
		<td>
Time scale
</td>
		<td>1</td>
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

image/share/sofa/examples/image/ImageTransform.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <!-- example of how to give translation parameter to an image and update it every time step-->
    <Node 	name="root" gravity="0 -10 0" dt="0.01"  >
        <Node name="plugins">
            <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
            <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
            <RequiredPlugin name="image"/> <!-- Needed to use components [ImageContainer ImageTransform ImageViewer] -->
        </Node>
      	
      	<EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
       	<CGLinearSolver template="GraphScattered" iterations="200" threshold="1e-12" tolerance="1e-5"/>
    	
    	<MechanicalObject name="meca" template="Rigid3d" translation="7 7 0" />
    	<UniformMass template="Rigid3d" totalMass="10"/>
    
    	<Node name="Visu">
            <OglModel name="Visual" filename="mesh/cube.obj" translation="7 7 0"/>
            <RigidMapping input="@../meca" output="@Visual" />
        </Node>	
    	
    	<Node name="image">
    		<ImageContainer  name="image" filename="textures/cubemap_bk.bmp" drawBB="false"/>
    	  	<ImageTransform name="transform" translation="@../meca.position" isPerspective="true" scale="0.1 0.1 15" update="1"/>
    
    	  	<ImageViewer  name="viewer" src="@image" />
      	</Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -10 0", dt="0.01")

        plugins = root.addChild('plugins')
        plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        plugins.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        plugins.addObject('RequiredPlugin', name="image")
        root.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
        root.addObject('CGLinearSolver', template="GraphScattered", iterations="200", threshold="1e-12", tolerance="1e-5")
        root.addObject('MechanicalObject', name="meca", template="Rigid3d", translation="7 7 0")
        root.addObject('UniformMass', template="Rigid3d", totalMass="10")

        Visu = root.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", filename="mesh/cube.obj", translation="7 7 0")
        Visu.addObject('RigidMapping', input="@../meca", output="@Visual")

        image = root.addChild('image')
        image.addObject('ImageContainer', name="image", filename="textures/cubemap_bk.bmp", drawBB="false")
        image.addObject('ImageTransform', name="transform", translation="@../meca.position", isPerspective="true", scale="0.1 0.1 15", update="1")
        image.addObject('ImageViewer', name="viewer", src="@image")
    ```

