# MergeImages

Merge images


__Templates__:

- `#!c++ ImageB`
- `#!c++ ImageD`
- `#!c++ ImageUC`

__Target__: `image`

__namespace__: `#!c++ sofa::component::engine`

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

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|



## Examples

image/share/sofa/examples/image/MergeImages.scn

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
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 0 0", dt=".1")

        plugins = root.addChild('plugins')
        plugins.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        plugins.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        plugins.addObject('RequiredPlugin', name="image")
        root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels")
        root.addObject('VisualGrid', size="50")
        root.addObject('LineAxis', size="50")
        root.addObject('OglSceneFrame')

        Average = root.addChild('Average')
        Average.addObject('MeshOBJLoader', name="mesh1", filename="mesh/sphere.obj", triangulate="1", scale="2 2 2")
        Average.addObject('MeshOBJLoader', name="mesh2", filename="mesh/sphere.obj", triangulate="1")
        Average.addObject('MeshToImageEngine', template="ImageUC", value="1", insideValue="1", name="rasterizer1", src="@mesh1", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
        Average.addObject('MeshToImageEngine', template="ImageUC", value="2", insideValue="2", name="rasterizer2", src="@mesh2", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
        Average.addObject('MergeImages', template="ImageUC", name="merge", nbImages="2", overlap="0", interpolation="0", image1="@rasterizer1.image", transform1="@rasterizer1.transform", image2="@rasterizer2.image", transform2="@rasterizer2.transform")
        Average.addObject('ImageContainer', template="ImageUC", name="image", image="@merge.image", transform="@merge.transform", drawBB="true")
        Average.addObject('ImageViewer', template="ImageUC", name="viewer", src="@image")

        Order = root.addChild('Order')
        Order.addObject('MeshOBJLoader', name="mesh1", filename="mesh/sphere.obj", triangulate="1", scale="2 2 2", translation="5 0 0")
        Order.addObject('MeshOBJLoader', name="mesh2", filename="mesh/sphere.obj", triangulate="1", translation="5 0 0")
        Order.addObject('MeshToImageEngine', template="ImageUC", value="1", insideValue="1", name="rasterizer1", src="@mesh1", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
        Order.addObject('MeshToImageEngine', template="ImageUC", value="2", insideValue="2", name="rasterizer2", src="@mesh2", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
        Order.addObject('MergeImages', template="ImageUC", name="merge", nbImages="2", overlap="1", interpolation="0", image1="@rasterizer1.image", transform1="@rasterizer1.transform", image2="@rasterizer2.image", transform2="@rasterizer2.transform")
        Order.addObject('ImageContainer', template="ImageUC", name="image", image="@merge.image", transform="@merge.transform", drawBB="true")
        Order.addObject('ImageViewer', template="ImageUC", name="viewer", src="@image")

        AlphaBlend = root.addChild('AlphaBlend')
        AlphaBlend.addObject('MeshOBJLoader', name="mesh1", filename="mesh/sphere.obj", triangulate="1", scale="2 2 2", translation="10 0 0")
        AlphaBlend.addObject('MeshOBJLoader', name="mesh2", filename="mesh/sphere.obj", triangulate="1", translation="10 0 0")
        AlphaBlend.addObject('MeshToImageEngine', template="ImageUC", value="1", insideValue="1", name="rasterizer1", src="@mesh1", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
        AlphaBlend.addObject('MeshToImageEngine', template="ImageUC", value="2", insideValue="2", name="rasterizer2", src="@mesh2", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
        AlphaBlend.addObject('MergeImages', template="ImageUC", name="merge", nbImages="2", overlap="2", interpolation="0", image1="@rasterizer1.image", transform1="@rasterizer1.transform", image2="@rasterizer2.image", transform2="@rasterizer2.transform")
        AlphaBlend.addObject('ImageContainer', template="ImageUC", name="image", image="@merge.image", transform="@merge.transform", drawBB="true")
        AlphaBlend.addObject('ImageViewer', template="ImageUC", name="viewer", src="@image")

        Separate = root.addChild('Separate')
        Separate.addObject('MeshOBJLoader', name="mesh1", filename="mesh/sphere.obj", triangulate="1", scale="2 2 2", translation="15 0 0")
        Separate.addObject('MeshOBJLoader', name="mesh2", filename="mesh/sphere.obj", triangulate="1", translation="15 0 0")
        Separate.addObject('MeshToImageEngine', template="ImageUC", value="1", insideValue="1", name="rasterizer1", src="@mesh1", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
        Separate.addObject('MeshToImageEngine', template="ImageUC", value="2", insideValue="2", name="rasterizer2", src="@mesh2", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
        Separate.addObject('MergeImages', template="ImageUC", name="merge", nbImages="2", overlap="3", interpolation="0", image1="@rasterizer1.image", transform1="@rasterizer1.transform", image2="@rasterizer2.image", transform2="@rasterizer2.transform")
        Separate.addObject('ImageContainer', template="ImageUC", name="image", image="@merge.image", transform="@merge.transform", drawBB="true")
        Separate.addObject('ImageViewer', template="ImageUC", name="viewer", src="@image")

        Additive = root.addChild('Additive')
        Additive.addObject('MeshOBJLoader', name="mesh1", filename="mesh/sphere.obj", triangulate="1", scale="2 2 2", translation="20 0 0")
        Additive.addObject('MeshOBJLoader', name="mesh2", filename="mesh/sphere.obj", triangulate="1", translation="20 0 0")
        Additive.addObject('MeshToImageEngine', template="ImageUC", value="1", insideValue="1", name="rasterizer1", src="@mesh1", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
        Additive.addObject('MeshToImageEngine', template="ImageUC", value="2", insideValue="2", name="rasterizer2", src="@mesh2", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
        Additive.addObject('MergeImages', template="ImageUC", name="merge", nbImages="2", overlap="4", interpolation="0", image1="@rasterizer1.image", transform1="@rasterizer1.transform", image2="@rasterizer2.image", transform2="@rasterizer2.transform")
        Additive.addObject('ImageContainer', template="ImageUC", name="image", image="@merge.image", transform="@merge.transform", drawBB="true")
        Additive.addObject('ImageViewer', template="ImageUC", name="viewer", src="@image")

        Intersect = root.addChild('Intersect')
        Intersect.addObject('MeshOBJLoader', name="mesh1", filename="mesh/sphere.obj", triangulate="1", scale="2 2 2", translation="25 0 0")
        Intersect.addObject('MeshOBJLoader', name="mesh2", filename="mesh/sphere.obj", triangulate="1", translation="25 0 0")
        Intersect.addObject('MeshToImageEngine', template="ImageUC", value="1", insideValue="1", name="rasterizer1", src="@mesh1", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
        Intersect.addObject('MeshToImageEngine', template="ImageUC", value="2", insideValue="2", name="rasterizer2", src="@mesh2", voxelSize="0.1", padSize="2", rotateImage="false", printLog="true")
        Intersect.addObject('MergeImages', template="ImageUC", name="merge", nbImages="2", overlap="5", interpolation="0", image1="@rasterizer1.image", transform1="@rasterizer1.transform", image2="@rasterizer2.image", transform2="@rasterizer2.transform")
        Intersect.addObject('ImageContainer', template="ImageUC", name="image", image="@merge.image", transform="@merge.transform", drawBB="true")
        Intersect.addObject('ImageViewer', template="ImageUC", name="viewer", src="@image")
    ```

