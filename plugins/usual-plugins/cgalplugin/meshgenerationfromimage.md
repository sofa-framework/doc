<!-- generate_doc -->
# MeshGenerationFromImage

Generate tetrahedral mesh from image


## Vec3d,ImageUC

Templates:

- Vec3d,ImageUC

__Target__: CGALPlugin

__namespace__: cgal

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
		<td>filename</td>
		<td>
Image file
		</td>
		<td></td>
	</tr>
	<tr>
		<td>image</td>
		<td>
image input
		</td>
		<td>0 0 0 0 0</td>
	</tr>
	<tr>
		<td>transform</td>
		<td>
12-param vector for trans, rot, scale, ...
		</td>
		<td></td>
	</tr>
	<tr>
		<td>features</td>
		<td>
features (1D) that will be preserved in the mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td>outputPoints</td>
		<td>
New Rest position coordinates from the tetrahedral generation
		</td>
		<td></td>
	</tr>
	<tr>
		<td>outputTetras</td>
		<td>
List of tetrahedra
		</td>
		<td></td>
	</tr>
	<tr>
		<td>outputTetrasDomains</td>
		<td>
domain of each tetrahedron
		</td>
		<td></td>
	</tr>
	<tr>
		<td>outputCellData</td>
		<td>
Output cell data
		</td>
		<td></td>
	</tr>
	<tr>
		<td>frozen</td>
		<td>
true to prohibit recomputations of the mesh
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>edgeSize</td>
		<td>
Edge size criterium (needed for polyline features
		</td>
		<td>2</td>
	</tr>
	<tr>
		<td>facetAngle</td>
		<td>
Lower bound for the angle in degrees of the surface mesh facets
		</td>
		<td>25</td>
	</tr>
	<tr>
		<td>facetSize</td>
		<td>
Uniform upper bound for the radius of the surface Delaunay balls
		</td>
		<td>0.15</td>
	</tr>
	<tr>
		<td>facetApproximation</td>
		<td>
Upper bound for the center-center distances of the surface mesh facets
		</td>
		<td>0.008</td>
	</tr>
	<tr>
		<td>cellRatio</td>
		<td>
Upper bound for the radius-edge ratio of the tetrahedra
		</td>
		<td>4</td>
	</tr>
	<tr>
		<td>cellSize</td>
		<td>
Uniform upper bound for the circumradii of the tetrahedra in the mesh
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>label</td>
		<td>
label to be resized to a specific cellSize
		</td>
		<td></td>
	</tr>
	<tr>
		<td>labelCellSize</td>
		<td>
Uniform upper bound for the circumradii of the tetrahedra in the mesh by label
		</td>
		<td></td>
	</tr>
	<tr>
		<td>labelCellData</td>
		<td>
1D cell data by label
		</td>
		<td></td>
	</tr>
	<tr>
		<td>odt</td>
		<td>
activate odt optimization
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>lloyd</td>
		<td>
activate lloyd optimization
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>perturb</td>
		<td>
activate perturb optimization
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>exude</td>
		<td>
activate exude optimization
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>odt_max_it</td>
		<td>
odt max iteration number
		</td>
		<td>200</td>
	</tr>
	<tr>
		<td>lloyd_max_it</td>
		<td>
lloyd max iteration number
		</td>
		<td>200</td>
	</tr>
	<tr>
		<td>perturb_max_time</td>
		<td>
perturb maxtime
		</td>
		<td>20</td>
	</tr>
	<tr>
		<td>exude_max_time</td>
		<td>
exude max time
		</td>
		<td>20</td>
	</tr>
	<tr>
		<td>ordering</td>
		<td>
Output points and elements ordering (0 = none, 1 = longest bbox axis)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawTetras</td>
		<td>
display generated tetra mesh
		</td>
		<td>0</td>
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

MeshGenerationFromImage.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="0 0 0" dt="1"  >
    	<RequiredPlugin pluginName="CGALPlugin"/>
    	<RequiredPlugin pluginName="image"/>
        <RequiredPlugin pluginName='SofaOpenglVisual'/>
        
    	<BackgroundSetting color="0 0.16862745098 0.21176470588"/>
    	<VisualStyle displayFlags="showVisual" />
    	<VisualGrid/>
    	<OglSceneFrame/>
    	<LineAxis/>
    
    	<ImageContainer name="image" template="ImageUC" filename="data/image/image-cube.inr"/>
    	<!-- <ImageViewer template="ImageUC" src="@image"/> -->
    		
    	<MeshGenerationFromImage template="Vec3d,ImageUC" name="generator" printLog="0" drawTetras="true"
    	image="@image.image" transform="@image.transform"
    	cellSize="0.5" facetAngle="30" facetSize="1" cellRatio="3" facetApproximation="1" ordering="0"
    	label="1 2 3" labelCellSize="0.2 0.5 0.1" labelCellData="100 200 300"/>
    		
    	<MeshTopology name="volume" points="@generator.outputPoints" 	tetras="@generator.outputTetras"/> 
    	<!--<VTKExporter name="exporter" filename="data/output.vtu"  XMLformat="1" edges="0" tetras="1"  listening="true" exportAtBegin="true" cellsDataFields="generator.outputCellData" overwrite="true"/>-->
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 0 0", dt="1")

       root.addObject('RequiredPlugin', pluginName="CGALPlugin")
       root.addObject('RequiredPlugin', pluginName="image")
       root.addObject('RequiredPlugin', pluginName="SofaOpenglVisual")
       root.addObject('BackgroundSetting', color="0 0.16862745098 0.21176470588")
       root.addObject('VisualStyle', displayFlags="showVisual")
       root.addObject('VisualGrid', )
       root.addObject('OglSceneFrame', )
       root.addObject('LineAxis', )
       root.addObject('ImageContainer', name="image", template="ImageUC", filename="data/image/image-cube.inr")
       root.addObject('MeshGenerationFromImage', template="Vec3d,ImageUC", name="generator", printLog="0", drawTetras="true", image="@image.image", transform="@image.transform", cellSize="0.5", facetAngle="30", facetSize="1", cellRatio="3", facetApproximation="1", ordering="0", label="1 2 3", labelCellSize="0.2 0.5 0.1", labelCellData="100 200 300")
       root.addObject('MeshTopology', name="volume", points="@generator.outputPoints", tetras="@generator.outputTetras")
    ```

MeshGenerationFromImageWithFeatures.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="0 0 0" dt="1"  >
    	<RequiredPlugin pluginName="CGALPlugin"/>
    	<RequiredPlugin pluginName="image"/>
    	
    	<MeshVTKLoader name="loader" filename="data/edgePoints.vtk" scale3d="1.0 1.0 1.0"/>
    	<ImageContainer name="image" template="ImageUC" filename="data/image/image-cube.inr"/>
    	<ImageViewer template="ImageUC" src="@image" plane="0 0 0"/>
    	
       	<MeshGenerationFromImage template="Vec3d,ImageUC" name="generator" printLog="0" drawTetras="true"
                image="@image.image" transform="@image.transform"  features="@loader.position"
                cellSize="5" edgeSize="5"  facetSize="5" facetApproximation="0.1"  facetAngle="30" cellRatio="3"  ordering="0"
    			label="1 2 3" labelCellSize="0.15 0.15 0.15" labelCellData="100 200 300"/>/> 
    	
    	<MeshTopology name="generatedMesh" points="@generator.outputPoints" 	tetras="@generator.outputTetras"/> 	
    	<!--<VTKExporter name="exporter" filename="cubeWithFeatures.vtk"  XMLformat="0" edges="0" tetras="1" exportAtBegin="1" cellsDataFields="generator.outputCellData"/>-->
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 0 0", dt="1")

       root.addObject('RequiredPlugin', pluginName="CGALPlugin")
       root.addObject('RequiredPlugin', pluginName="image")
       root.addObject('MeshVTKLoader', name="loader", filename="data/edgePoints.vtk", scale3d="1.0 1.0 1.0")
       root.addObject('ImageContainer', name="image", template="ImageUC", filename="data/image/image-cube.inr")
       root.addObject('ImageViewer', template="ImageUC", src="@image", plane="0 0 0")
       root.addObject('MeshGenerationFromImage', template="Vec3d,ImageUC", name="generator", printLog="0", drawTetras="true", image="@image.image", transform="@image.transform", features="@loader.position", cellSize="5", edgeSize="5", facetSize="5", facetApproximation="0.1", facetAngle="30", cellRatio="3", ordering="0", label="1 2 3", labelCellSize="0.15 0.15 0.15", labelCellData="100 200 300")
       root.addObject('MeshTopology', name="generatedMesh", points="@generator.outputPoints", tetras="@generator.outputTetras")
    ```

