<!-- generate_doc -->
# HausdorffDistance

Compute the Hausdorff distance of two point clouds


Templates:

- Rigid2d
- Rigid3d
- Vec1d
- Vec2d
- Vec3d

__Target__: Sofa.Component.Engine.Analyze

__namespace__: sofa::component::engine::analyze

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
		<td>update</td>
		<td>
Recompute every time step
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Input</td>
	</tr>
	<tr>
		<td>points1</td>
		<td>
Points belonging to the first point cloud
		</td>
		<td></td>
	</tr>
	<tr>
		<td>points2</td>
		<td>
Points belonging to the second point cloud
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Output</td>
	</tr>
	<tr>
		<td>d12</td>
		<td>
Distance from point cloud 1 to 2
		</td>
		<td></td>
	</tr>
	<tr>
		<td>d21</td>
		<td>
Distance from point cloud 2 to 1
		</td>
		<td></td>
	</tr>
	<tr>
		<td>max</td>
		<td>
Symmetrical Hausdorff distance
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

HausdorffDistance.scn

=== "XML"

    ```xml
    <Node name="Scene" gravity="0 0 0" dt="0.1" >
        <RequiredPlugin name="Sofa.Component.Engine.Analyze"/> <!-- Needed to use components [HausdorffDistance] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.Setting"/> <!-- Needed to use components [BackgroundSetting] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <VisualStyle displayFlags="showBehavior" />
        <BackgroundSetting color="1 1 1"/>
        <DefaultAnimationLoop/>
    
        <Node name="case1">
            <Node name="mesh1">
                <MeshOBJLoader name="meshloader1" filename="mesh/cube.obj"/>          
                <OglModel name="visu1" src="@meshloader1" color="0.8 0.2 0.2 0.5"/>
    
            </Node>
    
            <Node name="mesh2">
                <MeshOBJLoader name="meshloader2" filename="mesh/cube.obj" />
                <OglModel name="visu1" src="@meshloader2" color="0.2 0.2 0.8 0.5"/>
            </Node>
    
            <HausdorffDistance points1="@mesh1/meshloader1.position" points2="@mesh2/meshloader2.position"/>
        </Node>
    
        <Node name="case2">
            <Node name="mesh1">
                <MeshOBJLoader name="meshloader1" filename="mesh/cube.obj" translation="5 0 0"/>          
                <OglModel name="visu1" src="@meshloader1" color="0.8 0.2 0.2 0.5"/>
    
            </Node>
    
            <Node name="mesh2">
                <MeshOBJLoader name="meshloader2" filename="mesh/cube.obj" translation="6 0 0"/>
                <OglModel name="visu1" src="@meshloader2" color="0.2 0.2 0.8 0.5"/>
            </Node>
    
            <HausdorffDistance points1="@mesh1/meshloader1.position" points2="@mesh2/meshloader2.position"/>
        </Node>
    
        <Node name="case3">
            <Node name="mesh1">
                <MeshOBJLoader name="meshloader1" filename="mesh/cube.obj" translation="10 0 0"/>          
                <OglModel name="visu1" src="@meshloader1" color="0.8 0.2 0.2 0.5"/>
    
            </Node>
    
            <Node name="mesh2">
                <MeshOBJLoader name="meshloader2" filename="mesh/sphere.obj" translation="10 0 0"/>
                <OglModel name="visu1" src="@meshloader2" color="0.2 0.2 0.8 0.5"/>
            </Node>
    
            <HausdorffDistance points1="@mesh1/meshloader1.position" points2="@mesh2/meshloader2.position"/>
        </Node>
    
        <Node name="case4">
            <MeshOBJLoader name="meshloader1" filename="mesh/sphere.obj" translation="10 0 0"/>
            <HausdorffDistance points1="@meshloader1.position" points2="0 0 0"/>
        </Node>
    
        <Node name="case5">
            <HausdorffDistance points1="10 0 0" points2="0 0 0"/>
        </Node>
    
        <Node name="case6">
            <HausdorffDistance template="Vec2" points1="10 0" points2="0 0"/>
        </Node>
    
        <Node name="case7">
            <HausdorffDistance template="Vec1" points1="10" points2="0"/>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       scene = root_node.addChild('Scene', gravity="0 0 0", dt="0.1")

       scene.addObject('RequiredPlugin', name="Sofa.Component.Engine.Analyze")
       scene.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       scene.addObject('RequiredPlugin', name="Sofa.Component.Setting")
       scene.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       scene.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       scene.addObject('VisualStyle', displayFlags="showBehavior")
       scene.addObject('BackgroundSetting', color="1 1 1")
       scene.addObject('DefaultAnimationLoop', )

       case1 = Scene.addChild('case1')

       mesh1 = case1.addChild('mesh1')

       mesh1.addObject('MeshOBJLoader', name="meshloader1", filename="mesh/cube.obj")
       mesh1.addObject('OglModel', name="visu1", src="@meshloader1", color="0.8 0.2 0.2 0.5")

       mesh2 = case1.addChild('mesh2')

       mesh2.addObject('MeshOBJLoader', name="meshloader2", filename="mesh/cube.obj")
       mesh2.addObject('OglModel', name="visu1", src="@meshloader2", color="0.2 0.2 0.8 0.5")

       case1.addObject('HausdorffDistance', points1="@mesh1/meshloader1.position", points2="@mesh2/meshloader2.position")

       case2 = Scene.addChild('case2')

       mesh1 = case2.addChild('mesh1')

       mesh1.addObject('MeshOBJLoader', name="meshloader1", filename="mesh/cube.obj", translation="5 0 0")
       mesh1.addObject('OglModel', name="visu1", src="@meshloader1", color="0.8 0.2 0.2 0.5")

       mesh2 = case2.addChild('mesh2')

       mesh2.addObject('MeshOBJLoader', name="meshloader2", filename="mesh/cube.obj", translation="6 0 0")
       mesh2.addObject('OglModel', name="visu1", src="@meshloader2", color="0.2 0.2 0.8 0.5")

       case2.addObject('HausdorffDistance', points1="@mesh1/meshloader1.position", points2="@mesh2/meshloader2.position")

       case3 = Scene.addChild('case3')

       mesh1 = case3.addChild('mesh1')

       mesh1.addObject('MeshOBJLoader', name="meshloader1", filename="mesh/cube.obj", translation="10 0 0")
       mesh1.addObject('OglModel', name="visu1", src="@meshloader1", color="0.8 0.2 0.2 0.5")

       mesh2 = case3.addChild('mesh2')

       mesh2.addObject('MeshOBJLoader', name="meshloader2", filename="mesh/sphere.obj", translation="10 0 0")
       mesh2.addObject('OglModel', name="visu1", src="@meshloader2", color="0.2 0.2 0.8 0.5")

       case3.addObject('HausdorffDistance', points1="@mesh1/meshloader1.position", points2="@mesh2/meshloader2.position")

       case4 = Scene.addChild('case4')

       case4.addObject('MeshOBJLoader', name="meshloader1", filename="mesh/sphere.obj", translation="10 0 0")
       case4.addObject('HausdorffDistance', points1="@meshloader1.position", points2="0 0 0")

       case5 = Scene.addChild('case5')

       case5.addObject('HausdorffDistance', points1="10 0 0", points2="0 0 0")

       case6 = Scene.addChild('case6')

       case6.addObject('HausdorffDistance', template="Vec2", points1="10 0", points2="0 0")

       case7 = Scene.addChild('case7')

       case7.addObject('HausdorffDistance', template="Vec1", points1="10", points2="0")
    ```

