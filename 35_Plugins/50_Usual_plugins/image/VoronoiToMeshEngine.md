# VoronoiToMeshEngine

Generate flat faces between adjacent regions of an image


__Templates__:

- `#!c++ ImageUC`
- `#!c++ ImageUI`

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
		<td>image</td>
		<td>
Voronoi image
</td>
		<td>0 0 0 0 0</td>
	</tr>
	<tr>
		<td>background</td>
		<td>
Optional Voronoi image of the background to surface details
</td>
		<td>0 0 0 0 0</td>
	</tr>
	<tr>
		<td>transform</td>
		<td>

</td>
		<td>0 0 0 0 0 0 1 1 1 0 1 0</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
output positions
</td>
		<td></td>
	</tr>
	<tr>
		<td>edges</td>
		<td>
output edges
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
output triangles
</td>
		<td></td>
	</tr>
	<tr>
		<td>minLength</td>
		<td>
minimun edge length in pixels
</td>
		<td>2</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showMesh</td>
		<td>
show reconstructed mesh
</td>
		<td>0</td>
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

image/share/sofa/examples/image/VoronoiToMeshEngine.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node 	name="root" gravity="0 0 0" dt="1"  >
        <Node name="plugins">
            <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
            <RequiredPlugin name="Sofa.Component.Setting"/> <!-- Needed to use components [BackgroundSetting] -->
            <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
            <RequiredPlugin name="image"/> <!-- Needed to use components [ImageContainer ImageSampler MeshToImageEngine TransferFunction VoronoiToMeshEngine] -->
        </Node>
     <BackgroundSetting color="1 1 1"/>
    	
    
    <!--Simple flat outer shape (no need to sample the background)-->
    <Node name="box" >
    	 <MeshOBJLoader  filename="mesh/cube.obj"  triangulate="1"  name="mesh" scale3d="3 0.5 3" translation="10 0 0" />
    	 <MeshToImageEngine  template="ImageUC"  name="rasterizer"  position="@mesh.position"  triangles="@mesh.triangles"  value="1"  voxelSize="0.1"  padSize="2"  />
    	 <ImageContainer  template="ImageUC"  name="image"  src="@rasterizer"/>
    <!--	 <ImageViewer  template="ImageUC"  src="@image"/>-->
    
    	 <ImageSampler  name="sampler"  template="ImageUC"  src="@image"  method="1"  param="50"  showSamplesScale="10"  clearData="0"/>
    <!--	 <ImageViewer  template="ImageUI"  transform="@image.transform"  image="@sampler.voronoi"  plane="-1 10 -1"/>-->
    
    	 <VoronoiToMeshEngine  name="VoronoiToMesh"  template="ImageUI"  transform="@image.transform"  image="@sampler.voronoi"  showMesh="0" minLength="0.5" printLog="1"/>
    
    	 <OglModel position="@VoronoiToMesh.position" edges="@VoronoiToMesh.edges" color="red" lineWidth="1" lineSmooth="1"/>
    	 <OglModel position="@VoronoiToMesh.position" triangles="@VoronoiToMesh.triangles" color="5e-1 5e-1 10e-1 1e-1" lineWidth="1"/>
    
    </Node>
    
    <!--more complex outer shape -->
    <Node name="gear" >
    	 <MeshOBJLoader  filename="mesh/gear0.obj"  triangulate="1"  name="mesh"  />
    	 <MeshToImageEngine  template="ImageUC"  name="rasterizer"  position="@mesh.position"  triangles="@mesh.triangles"  value="1"  voxelSize="0.12"  padSize="2"  />
    	 <ImageContainer  template="ImageUC"  name="image"  src="@rasterizer"/>
    <!--	 <ImageViewer  template="ImageUC"  src="@image"/>-->
    
    	 <TransferFunction  template="ImageUC,ImageUC" name="tf" inputImage="@image.image" param="0 1 1 0"   />
    	 <ImageContainer  template="ImageUC"  name="background"  image="@tf.outputImage" transform="@image.transform"/>
    	<!-- <ImageViewer  template="ImageUC"  src="@background"/>-->
    
    	 <ImageSampler  name="sampler"  template="ImageUC"  src="@image"  method="1"  param="40"  showSamplesScale="10"  clearData="0"/>
    <!--	 <ImageViewer  template="ImageUI"  transform="@image.transform"  image="@sampler.voronoi"  plane="-1 10 -1"/>-->
    	 <ImageSampler  name="sampler_background"  template="ImageUC"  src="@background"  method="1"  param="150"  clearData="0"/>
    
    	 <VoronoiToMeshEngine  name="VoronoiToMesh"  template="ImageUI"  transform="@image.transform"  image="@sampler.voronoi"  background="@sampler_background.voronoi"  showMesh="0" minLength="0.5" printLog="1"/>
    
    	 <OglModel position="@VoronoiToMesh.position" edges="@VoronoiToMesh.edges" color="red" lineWidth="1" lineSmooth="1"/>
    	 <OglModel position="@VoronoiToMesh.position" triangles="@VoronoiToMesh.triangles" color="5e-1 5e-1 10e-1 1e-1" lineWidth="1"/>
    </Node>
    
    <!--	  <ClipPlane normal="0 1 0" position="0 0 0"/>-->
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 0 0", dt="1")

        plugins = root.addChild('plugins')
        plugins.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Setting")
        plugins.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        plugins.addObject('RequiredPlugin', name="image")
        root.addObject('BackgroundSetting', color="1 1 1")

        box = root.addChild('box')
        box.addObject('MeshOBJLoader', filename="mesh/cube.obj", triangulate="1", name="mesh", scale3d="3 0.5 3", translation="10 0 0")
        box.addObject('MeshToImageEngine', template="ImageUC", name="rasterizer", position="@mesh.position", triangles="@mesh.triangles", value="1", voxelSize="0.1", padSize="2")
        box.addObject('ImageContainer', template="ImageUC", name="image", src="@rasterizer")
        box.addObject('ImageSampler', name="sampler", template="ImageUC", src="@image", method="1", param="50", showSamplesScale="10", clearData="0")
        box.addObject('VoronoiToMeshEngine', name="VoronoiToMesh", template="ImageUI", transform="@image.transform", image="@sampler.voronoi", showMesh="0", minLength="0.5", printLog="1")
        box.addObject('OglModel', position="@VoronoiToMesh.position", edges="@VoronoiToMesh.edges", color="red", lineWidth="1", lineSmooth="1")
        box.addObject('OglModel', position="@VoronoiToMesh.position", triangles="@VoronoiToMesh.triangles", color="5e-1 5e-1 10e-1 1e-1", lineWidth="1")

        gear = root.addChild('gear')
        gear.addObject('MeshOBJLoader', filename="mesh/gear0.obj", triangulate="1", name="mesh")
        gear.addObject('MeshToImageEngine', template="ImageUC", name="rasterizer", position="@mesh.position", triangles="@mesh.triangles", value="1", voxelSize="0.12", padSize="2")
        gear.addObject('ImageContainer', template="ImageUC", name="image", src="@rasterizer")
        gear.addObject('TransferFunction', template="ImageUC,ImageUC", name="tf", inputImage="@image.image", param="0 1 1 0")
        gear.addObject('ImageContainer', template="ImageUC", name="background", image="@tf.outputImage", transform="@image.transform")
        gear.addObject('ImageSampler', name="sampler", template="ImageUC", src="@image", method="1", param="40", showSamplesScale="10", clearData="0")
        gear.addObject('ImageSampler', name="sampler_background", template="ImageUC", src="@background", method="1", param="150", clearData="0")
        gear.addObject('VoronoiToMeshEngine', name="VoronoiToMesh", template="ImageUI", transform="@image.transform", image="@sampler.voronoi", background="@sampler_background.voronoi", showMesh="0", minLength="0.5", printLog="1")
        gear.addObject('OglModel', position="@VoronoiToMesh.position", edges="@VoronoiToMesh.edges", color="red", lineWidth="1", lineSmooth="1")
        gear.addObject('OglModel', position="@VoronoiToMesh.position", triangles="@VoronoiToMesh.triangles", color="5e-1 5e-1 10e-1 1e-1", lineWidth="1")
    ```

