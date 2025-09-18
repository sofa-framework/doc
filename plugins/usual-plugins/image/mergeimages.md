<!-- generate_doc -->
# MergeImages

Merge images


Templates:

- ImageB
- ImageD
- ImageUC

__Target__: image

__namespace__: sofa::component::engine

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
		<td>overlap</td>
		<td>
method for handling overlapping regions
		</td>
		<td></td>
	</tr>
	<tr>
		<td>interpolation</td>
		<td>
Interpolation method.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>nbImages</td>
		<td>
number of images to merge
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>image</td>
		<td>
Image
		</td>
		<td>0 0 0 0 0</td>
	</tr>
	<tr>
		<td>transform</td>
		<td>
Transform
		</td>
		<td>0 0 0 0 0 0 1 1 1 0 1 0</td>
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

MergeImages.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="0 0 0" dt=".1"  >
        <Node name="plugins">
            <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
            <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [LineAxis VisualGrid VisualStyle] -->
            <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglSceneFrame] -->
            <RequiredPlugin name="image"/> <!-- Needed to use components [ImageContainer ImageViewer MergeImages MeshToImageEngine] -->
        </Node>
    
        <VisualStyle displayFlags="showVisual showBehaviorModels" />
        <VisualGrid size="50"/>
        <LineAxis size="50"/>
        <OglSceneFrame/>
        
        <Node name="Average">
          <MeshOBJLoader name="mesh1" filename="mesh/sphere.obj" triangulate="1" scale="2 2 2"/>
          <MeshOBJLoader name="mesh2" filename="mesh/sphere.obj" triangulate="1"/>
    
          <MeshToImageEngine template="ImageUC" value="1" insideValue="1" name="rasterizer1" src="@mesh1" voxelSize="0.1" padSize="2" rotateImage="false" printLog="true"/>
          <MeshToImageEngine template="ImageUC" value="2" insideValue="2" name="rasterizer2" src="@mesh2" voxelSize="0.1" padSize="2" rotateImage="false" printLog="true"/>
    
          <MergeImages  template="ImageUC" name="merge" nbImages="2" overlap="0" interpolation="0"
                                         image1="@rasterizer1.image" transform1="@rasterizer1.transform"
                                         image2="@rasterizer2.image" transform2="@rasterizer2.transform"/>
    
          <ImageContainer template="ImageUC" name="image" image="@merge.image" transform="@merge.transform" drawBB="true"/>
          <ImageViewer template="ImageUC" name="viewer" src="@image" />
    
        </Node>
    
        <Node name="Order">
          <MeshOBJLoader name="mesh1" filename="mesh/sphere.obj" triangulate="1" scale="2 2 2" translation="5 0 0"/>
          <MeshOBJLoader name="mesh2" filename="mesh/sphere.obj" triangulate="1" translation="5 0 0"/>
    
          <MeshToImageEngine template="ImageUC" value="1" insideValue="1" name="rasterizer1" src="@mesh1" voxelSize="0.1" padSize="2" rotateImage="false" printLog="true"/>
          <MeshToImageEngine template="ImageUC" value="2" insideValue="2" name="rasterizer2" src="@mesh2" voxelSize="0.1" padSize="2" rotateImage="false" printLog="true"/>
    
          <MergeImages  template="ImageUC" name="merge" nbImages="2" overlap="1" interpolation="0"
                                         image1="@rasterizer1.image" transform1="@rasterizer1.transform"
                                         image2="@rasterizer2.image" transform2="@rasterizer2.transform"/>
    
          <ImageContainer template="ImageUC" name="image" image="@merge.image" transform="@merge.transform" drawBB="true"/>
          <ImageViewer template="ImageUC" name="viewer" src="@image" />
    
        </Node>
    
        <Node name="AlphaBlend">
          <MeshOBJLoader name="mesh1" filename="mesh/sphere.obj" triangulate="1" scale="2 2 2" translation="10 0 0"/>
          <MeshOBJLoader name="mesh2" filename="mesh/sphere.obj" triangulate="1" translation="10 0 0"/>
    
          <MeshToImageEngine template="ImageUC" value="1" insideValue="1" name="rasterizer1" src="@mesh1" voxelSize="0.1" padSize="2" rotateImage="false" printLog="true"/>
          <MeshToImageEngine template="ImageUC" value="2" insideValue="2" name="rasterizer2" src="@mesh2" voxelSize="0.1" padSize="2" rotateImage="false" printLog="true"/>
    
          <MergeImages  template="ImageUC" name="merge" nbImages="2" overlap="2" interpolation="0"
                                         image1="@rasterizer1.image" transform1="@rasterizer1.transform"
                                         image2="@rasterizer2.image" transform2="@rasterizer2.transform"/>
    
          <ImageContainer template="ImageUC" name="image" image="@merge.image" transform="@merge.transform" drawBB="true"/>
          <ImageViewer template="ImageUC" name="viewer" src="@image" />
    
        </Node>
    
        <Node name="Separate">
          <MeshOBJLoader name="mesh1" filename="mesh/sphere.obj" triangulate="1" scale="2 2 2" translation="15 0 0"/>
          <MeshOBJLoader name="mesh2" filename="mesh/sphere.obj" triangulate="1" translation="15 0 0"/>
    
          <MeshToImageEngine template="ImageUC" value="1" insideValue="1" name="rasterizer1" src="@mesh1" voxelSize="0.1" padSize="2" rotateImage="false" printLog="true"/>
          <MeshToImageEngine template="ImageUC" value="2" insideValue="2" name="rasterizer2" src="@mesh2" voxelSize="0.1" padSize="2" rotateImage="false" printLog="true"/>
    
          <MergeImages  template="ImageUC" name="merge" nbImages="2" overlap="3" interpolation="0"
                                         image1="@rasterizer1.image" transform1="@rasterizer1.transform"
                                         image2="@rasterizer2.image" transform2="@rasterizer2.transform"/>
    
          <ImageContainer template="ImageUC" name="image" image="@merge.image" transform="@merge.transform" drawBB="true"/>
          <ImageViewer template="ImageUC" name="viewer" src="@image" />
    
        </Node>
    
        <Node name="Additive">
          <MeshOBJLoader name="mesh1" filename="mesh/sphere.obj" triangulate="1" scale="2 2 2" translation="20 0 0"/>
          <MeshOBJLoader name="mesh2" filename="mesh/sphere.obj" triangulate="1" translation="20 0 0"/>
    
          <MeshToImageEngine template="ImageUC" value="1" insideValue="1" name="rasterizer1" src="@mesh1" voxelSize="0.1" padSize="2" rotateImage="false" printLog="true"/>
          <MeshToImageEngine template="ImageUC" value="2" insideValue="2" name="rasterizer2" src="@mesh2" voxelSize="0.1" padSize="2" rotateImage="false" printLog="true"/>
    
          <MergeImages  template="ImageUC" name="merge" nbImages="2" overlap="4" interpolation="0"
                                         image1="@rasterizer1.image" transform1="@rasterizer1.transform"
                                         image2="@rasterizer2.image" transform2="@rasterizer2.transform"/>
    
          <ImageContainer template="ImageUC" name="image" image="@merge.image" transform="@merge.transform" drawBB="true"/>
          <ImageViewer template="ImageUC" name="viewer" src="@image" />
    
        </Node>
    
        <Node name="Intersect">
          <MeshOBJLoader name="mesh1" filename="mesh/sphere.obj" triangulate="1" scale="2 2 2" translation="25 0 0" />
          <MeshOBJLoader name="mesh2" filename="mesh/sphere.obj" triangulate="1" translation="25 0 0"/>
    
          <MeshToImageEngine template="ImageUC" value="1" insideValue="1" name="rasterizer1" src="@mesh1" voxelSize="0.1" padSize="2" rotateImage="false" printLog="true"/>
          <MeshToImageEngine template="ImageUC" value="2" insideValue="2" name="rasterizer2" src="@mesh2" voxelSize="0.1" padSize="2" rotateImage="false" printLog="true"/>
    
          <MergeImages  template="ImageUC" name="merge" nbImages="2" overlap="5" interpolation="0"
                                         image1="@rasterizer1.image" transform1="@rasterizer1.transform"
                                         image2="@rasterizer2.image" transform2="@rasterizer2.transform"/>
    
          <ImageContainer template="ImageUC" name="image" image="@merge.image" transform="@merge.transform" drawBB="true"/>
          <ImageViewer template="ImageUC" name="viewer" src="@image" />
    
        </Node>
    
    
    </Node>
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 0 0", dt=".1")

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       plugins.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       plugins.addObject('RequiredPlugin', name="image")

       root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels")
       root.addObject('VisualGrid', size="50")
       root.addObject('LineAxis', size="50")
       root.addObject('OglSceneFrame', )

       average = root.addChild('Average')

       average.addObject('MeshOBJLoader', name="mesh1", filename="mesh/sphere.obj", triangulate="1", scale="2 2 2")
       average.addObject('MeshOBJLoader', name="mesh2", filename="mesh/sphere.obj", triangulate="1")
       average.addObject('MeshToImageEngine', template="ImageUC", value="1", insideValue="1", name="rasterizer1", src="@mesh1", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
       average.addObject('MeshToImageEngine', template="ImageUC", value="2", insideValue="2", name="rasterizer2", src="@mesh2", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
       average.addObject('MergeImages', template="ImageUC", name="merge", nbImages="2", overlap="0", interpolation="0", image1="@rasterizer1.image", transform1="@rasterizer1.transform", image2="@rasterizer2.image", transform2="@rasterizer2.transform")
       average.addObject('ImageContainer', template="ImageUC", name="image", image="@merge.image", transform="@merge.transform", drawBB="true")
       average.addObject('ImageViewer', template="ImageUC", name="viewer", src="@image")

       order = root.addChild('Order')

       order.addObject('MeshOBJLoader', name="mesh1", filename="mesh/sphere.obj", triangulate="1", scale="2 2 2", translation="5 0 0")
       order.addObject('MeshOBJLoader', name="mesh2", filename="mesh/sphere.obj", triangulate="1", translation="5 0 0")
       order.addObject('MeshToImageEngine', template="ImageUC", value="1", insideValue="1", name="rasterizer1", src="@mesh1", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
       order.addObject('MeshToImageEngine', template="ImageUC", value="2", insideValue="2", name="rasterizer2", src="@mesh2", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
       order.addObject('MergeImages', template="ImageUC", name="merge", nbImages="2", overlap="1", interpolation="0", image1="@rasterizer1.image", transform1="@rasterizer1.transform", image2="@rasterizer2.image", transform2="@rasterizer2.transform")
       order.addObject('ImageContainer', template="ImageUC", name="image", image="@merge.image", transform="@merge.transform", drawBB="true")
       order.addObject('ImageViewer', template="ImageUC", name="viewer", src="@image")

       alpha_blend = root.addChild('AlphaBlend')

       alpha_blend.addObject('MeshOBJLoader', name="mesh1", filename="mesh/sphere.obj", triangulate="1", scale="2 2 2", translation="10 0 0")
       alpha_blend.addObject('MeshOBJLoader', name="mesh2", filename="mesh/sphere.obj", triangulate="1", translation="10 0 0")
       alpha_blend.addObject('MeshToImageEngine', template="ImageUC", value="1", insideValue="1", name="rasterizer1", src="@mesh1", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
       alpha_blend.addObject('MeshToImageEngine', template="ImageUC", value="2", insideValue="2", name="rasterizer2", src="@mesh2", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
       alpha_blend.addObject('MergeImages', template="ImageUC", name="merge", nbImages="2", overlap="2", interpolation="0", image1="@rasterizer1.image", transform1="@rasterizer1.transform", image2="@rasterizer2.image", transform2="@rasterizer2.transform")
       alpha_blend.addObject('ImageContainer', template="ImageUC", name="image", image="@merge.image", transform="@merge.transform", drawBB="true")
       alpha_blend.addObject('ImageViewer', template="ImageUC", name="viewer", src="@image")

       separate = root.addChild('Separate')

       separate.addObject('MeshOBJLoader', name="mesh1", filename="mesh/sphere.obj", triangulate="1", scale="2 2 2", translation="15 0 0")
       separate.addObject('MeshOBJLoader', name="mesh2", filename="mesh/sphere.obj", triangulate="1", translation="15 0 0")
       separate.addObject('MeshToImageEngine', template="ImageUC", value="1", insideValue="1", name="rasterizer1", src="@mesh1", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
       separate.addObject('MeshToImageEngine', template="ImageUC", value="2", insideValue="2", name="rasterizer2", src="@mesh2", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
       separate.addObject('MergeImages', template="ImageUC", name="merge", nbImages="2", overlap="3", interpolation="0", image1="@rasterizer1.image", transform1="@rasterizer1.transform", image2="@rasterizer2.image", transform2="@rasterizer2.transform")
       separate.addObject('ImageContainer', template="ImageUC", name="image", image="@merge.image", transform="@merge.transform", drawBB="true")
       separate.addObject('ImageViewer', template="ImageUC", name="viewer", src="@image")

       additive = root.addChild('Additive')

       additive.addObject('MeshOBJLoader', name="mesh1", filename="mesh/sphere.obj", triangulate="1", scale="2 2 2", translation="20 0 0")
       additive.addObject('MeshOBJLoader', name="mesh2", filename="mesh/sphere.obj", triangulate="1", translation="20 0 0")
       additive.addObject('MeshToImageEngine', template="ImageUC", value="1", insideValue="1", name="rasterizer1", src="@mesh1", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
       additive.addObject('MeshToImageEngine', template="ImageUC", value="2", insideValue="2", name="rasterizer2", src="@mesh2", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
       additive.addObject('MergeImages', template="ImageUC", name="merge", nbImages="2", overlap="4", interpolation="0", image1="@rasterizer1.image", transform1="@rasterizer1.transform", image2="@rasterizer2.image", transform2="@rasterizer2.transform")
       additive.addObject('ImageContainer', template="ImageUC", name="image", image="@merge.image", transform="@merge.transform", drawBB="true")
       additive.addObject('ImageViewer', template="ImageUC", name="viewer", src="@image")

       intersect = root.addChild('Intersect')

       intersect.addObject('MeshOBJLoader', name="mesh1", filename="mesh/sphere.obj", triangulate="1", scale="2 2 2", translation="25 0 0")
       intersect.addObject('MeshOBJLoader', name="mesh2", filename="mesh/sphere.obj", triangulate="1", translation="25 0 0")
       intersect.addObject('MeshToImageEngine', template="ImageUC", value="1", insideValue="1", name="rasterizer1", src="@mesh1", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
       intersect.addObject('MeshToImageEngine', template="ImageUC", value="2", insideValue="2", name="rasterizer2", src="@mesh2", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
       intersect.addObject('MergeImages', template="ImageUC", name="merge", nbImages="2", overlap="5", interpolation="0", image1="@rasterizer1.image", transform1="@rasterizer1.transform", image2="@rasterizer2.image", transform2="@rasterizer2.transform")
       intersect.addObject('ImageContainer', template="ImageUC", name="image", image="@merge.image", transform="@merge.transform", drawBB="true")
       intersect.addObject('ImageViewer', template="ImageUC", name="viewer", src="@image")
    ```

