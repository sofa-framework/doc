<!-- generate_doc -->
# MergeMeshes

Merge several meshes


Templates:

- Rigid2d
- Rigid3d
- Vec1d
- Vec2d
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
		<td>nbMeshes</td>
		<td>
number of meshes to merge
		</td>
		<td>2</td>
	</tr>
	<tr>
		<td>npoints</td>
		<td>
Number Of out points
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Output Vertices of the merged mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td>edges</td>
		<td>
Output Edges of the merged mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
Output Triangles of the merged mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quads</td>
		<td>
Output Quads of the merged mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td>polygons</td>
		<td>
Output Polygons of the merged mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedra</td>
		<td>
Output Tetrahedra of the merged mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedra</td>
		<td>
Output Hexahedra of the merged mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>position1</td>
		<td>
input positions for mesh 1
		</td>
		<td></td>
	</tr>
	<tr>
		<td>position2</td>
		<td>
input positions for mesh 2
		</td>
		<td></td>
	</tr>
	<tr>
		<td>edges1</td>
		<td>
input edges for mesh 1
		</td>
		<td></td>
	</tr>
	<tr>
		<td>edges2</td>
		<td>
input edges for mesh 2
		</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles1</td>
		<td>
input triangles for mesh 1
		</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles2</td>
		<td>
input triangles for mesh 2
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quads1</td>
		<td>
input quads for mesh 1
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quads2</td>
		<td>
input quads for mesh 2
		</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedra1</td>
		<td>
input tetrahedra for mesh 1
		</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedra2</td>
		<td>
input tetrahedra for mesh 2
		</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedra1</td>
		<td>
input hexahedra for mesh 1
		</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedra2</td>
		<td>
input hexahedra for mesh 2
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

MergeMeshes.scn

=== "XML"

    ```xml
    <Node name="Scene" gravity="0 0 0" dt="0.1" >
        <RequiredPlugin name="Sofa.Component.Engine.Generate"/> <!-- Needed to use components [MergeMeshes] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <DefaultAnimationLoop/>
    	<VisualStyle displayFlags="showBehavior" />
        <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
        <CGLinearSolver iterations="25" tolerance="1e-05" threshold="1e-05"/>
        <Node>
            <MeshOBJLoader name="frog" filename="mesh/frog.obj" />
            <MeshOBJLoader name="dragon" filename="mesh/dragon.obj" />
    
            <MergeMeshes name="basis" nbMeshes="2" 
                         position1="@frog.position" 
                         triangles1="@frog.triangles"
                         position2="@dragon.position"
                         triangles2="@dragon.triangles"
                         />
        	  
            <MeshTopology src="@basis" drawTriangles="1"/>
            <MechanicalObject showObject="1"/>
            <UniformMass />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       scene = root_node.addChild('Scene', gravity="0 0 0", dt="0.1")

       scene.addObject('RequiredPlugin', name="Sofa.Component.Engine.Generate")
       scene.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       scene.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       scene.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       scene.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       scene.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       scene.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       scene.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       scene.addObject('DefaultAnimationLoop', )
       scene.addObject('VisualStyle', displayFlags="showBehavior")
       scene.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
       scene.addObject('CGLinearSolver', iterations="25", tolerance="1e-05", threshold="1e-05")

       node = Scene.addChild('node')

       node.addObject('MeshOBJLoader', name="frog", filename="mesh/frog.obj")
       node.addObject('MeshOBJLoader', name="dragon", filename="mesh/dragon.obj")
       node.addObject('MergeMeshes', name="basis", nbMeshes="2", position1="@frog.position", triangles1="@frog.triangles", position2="@dragon.position", triangles2="@dragon.triangles")
       node.addObject('MeshTopology', src="@basis", drawTriangles="1")
       node.addObject('MechanicalObject', showObject="1")
       node.addObject('UniformMass', )
    ```

