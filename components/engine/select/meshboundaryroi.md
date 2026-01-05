<!-- generate_doc -->
# MeshBoundaryROI

Outputs indices of boundary vertices of a triangle/quad mesh


__Target__: Sofa.Component.Engine.Select

__namespace__: sofa::component::engine::select

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
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
input triangles
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quads</td>
		<td>
input quads
		</td>
		<td></td>
	</tr>
	<tr>
		<td>inputROI</td>
		<td>
optional subset of the input mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
Index lists of the closing vertices
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

MeshBoundaryROI.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node 	name="root" gravity="0 0 0" dt="1"  >
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Generate"/> <!-- Needed to use components [MergeMeshes] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [MeshBoundaryROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.Setting"/> <!-- Needed to use components [BackgroundSetting] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <BackgroundSetting color="1 1 1" />
        <VisualStyle displayFlags="showVisual showBehaviorModels" />
        <DefaultAnimationLoop/>
    
        <MeshOBJLoader name="mesh1" filename="mesh/c_open.obj" triangulate="0"/>
        <!-- computeTriangleList or computeQuadList must be set to false. Otherwise, both are considered, and boundary detection cannot rely on a unique element -->
        <RegularGridTopology name="mesh2" nx="5" ny="5" nz="1" xmin="-10" xmax="10" ymin="-10" ymax="10" zmin="-5" zmax="-5" computeTriangleList="false"/>
        <MergeMeshes name="mesh" nbMeshes="2" position1="@mesh1.position" position2="@mesh2.position" triangles1="@mesh1.triangles" triangles2="@mesh2.triangles" quads1="@mesh1.quads" quads2="@mesh2.quads"/>
    
        <MechanicalObject template="Vec3" position="@mesh.position" />
        <MeshBoundaryROI name="roi"/>
        <FixedProjectiveConstraint template="Vec3" indices="@roi.indices" />
    
        <Node name="visu">
            <OglModel name="visual"  src="@../mesh" color="0.5 0.5 1 1" />
        </Node>
    </Node>
    

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 0 0", dt="1")

       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Generate")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.Setting")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('BackgroundSetting', color="1 1 1")
       root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('MeshOBJLoader', name="mesh1", filename="mesh/c_open.obj", triangulate="0")
       root.addObject('RegularGridTopology', name="mesh2", nx="5", ny="5", nz="1", xmin="-10", xmax="10", ymin="-10", ymax="10", zmin="-5", zmax="-5", computeTriangleList="false")
       root.addObject('MergeMeshes', name="mesh", nbMeshes="2", position1="@mesh1.position", position2="@mesh2.position", triangles1="@mesh1.triangles", triangles2="@mesh2.triangles", quads1="@mesh1.quads", quads2="@mesh2.quads")
       root.addObject('MechanicalObject', template="Vec3", position="@mesh.position")
       root.addObject('MeshBoundaryROI', name="roi")
       root.addObject('FixedProjectiveConstraint', template="Vec3", indices="@roi.indices")

       visu = root.addChild('visu')

       visu.addObject('OglModel', name="visual", src="@../mesh", color="0.5 0.5 1 1")
    ```

