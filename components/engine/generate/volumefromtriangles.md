<!-- generate_doc -->
# VolumeFromTriangles

This component computes the volume of a given closed surfacic mesh.


## Rigid3d

Templates:

- Rigid3d

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
		<td>position</td>
		<td>
If not set by user, find the context mechanical.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
If not set by user, find the context topology.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quads</td>
		<td>
If not set by user, find the context topology.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>volume</td>
		<td>
The volume is only relevant if the surface is closed.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>update</td>
		<td>
If true, will update the volume at each time step of the simulation.
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
|topology|link to the topology|BaseMeshTopology|
|mechanical|link to the mechanical|MechanicalState&lt;Rigid3d&gt;|

<!-- generate_doc -->
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
		<td>position</td>
		<td>
If not set by user, find the context mechanical.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
If not set by user, find the context topology.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quads</td>
		<td>
If not set by user, find the context topology.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>volume</td>
		<td>
The volume is only relevant if the surface is closed.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>update</td>
		<td>
If true, will update the volume at each time step of the simulation.
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
|topology|link to the topology|BaseMeshTopology|
|mechanical|link to the mechanical|MechanicalState&lt;Vec3d&gt;|

## Examples 

VolumeFromTriangles.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="0 0 0" dt="1"  >
        <RequiredPlugin name="Sofa.Component.Engine.Generate"/> <!-- Needed to use components [VolumeFromTriangles] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshVTKLoader] -->
        <RequiredPlugin name="Sofa.Component.Setting"/> <!-- Needed to use components [BackgroundSetting] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->  
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->  
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->  
    
    
        <DefaultAnimationLoop/>
        <BackgroundSetting color="1 1 1" />
        <Node name="Volume" >
            <MeshSTLLoader name="mesh" filename="mesh/Bunny.stl"/>
            <MeshTopology src="@mesh" name="topology"/>
            <MechanicalObject />
            <VolumeFromTriangles/>
            <Node name="Visual" >
                <OglModel src="@../topology" color="0.5 0.5 0.5 0.3"/>
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 0 0", dt="1")

       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Generate")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.Setting")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('BackgroundSetting', color="1 1 1")

       volume = root.addChild('Volume')

       volume.addObject('MeshSTLLoader', name="mesh", filename="mesh/Bunny.stl")
       volume.addObject('MeshTopology', src="@mesh", name="topology")
       volume.addObject('MechanicalObject', )
       volume.addObject('VolumeFromTriangles', )

       visual = Volume.addChild('Visual')

       visual.addObject('OglModel', src="@../topology", color="0.5 0.5 0.5 0.3")
    ```

