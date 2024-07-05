---
title: ExtrudeSurface
---

ExtrudeSurface
==============

This component belongs to the category of [Engines](https://www.sofa-framework.org/community/doc/simulation-principles/engine/). This engine extrude a surface and returns corresponding triangles.

Input Data
----------

-   **triangles**: list of triangles of the object to extrude. It must me a vector of BaseMeshTopology::Triangle
-   **surfaceTriangles**: list of triangles of the surface to extrude. The type of triangle must be BaseMeshTopology::TriangleID, and not BaseMeshTopology::Triangle
-   **surfaceVertices**: list of positions

Output Data
----------

-   **extrusionVertices**: list of positions of the new triangles, created from extrusion
-   **extrusionTriangles**: list of triangles from extrusion (vector of BaseMeshTopology::Triangle)


Important Parameter
-------------------


-   **heightFactor**: extrusion is based on normals. So, this factor defines the final height of the extrusion.

Examples
--------

An example scene involving the ExtrudeSurface engine is available in [*examples/Component/Engine/Generate/ExtrudeSurface.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/Engine/Generate/ExtrudeSurface.scn)
<!-- automatically generated doc START -->
__Target__: `Sofa.Component.Engine.Generate`

__namespace__: `#!c++ sofa::component::engine::generate`

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
		<td>isVisible</td>
		<td>
is Visible ?
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>heightFactor</td>
		<td>
Factor for the height of the extrusion (based on normal)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
Triangle topology (list of BaseMeshTopology::Triangle)
</td>
		<td></td>
	</tr>
	<tr>
		<td>surfaceVertices</td>
		<td>
Position coordinates of the surface
</td>
		<td></td>
	</tr>
	<tr>
		<td>surfaceTriangles</td>
		<td>
Indices of the triangles of the surface to extrude
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>extrusionVertices</td>
		<td>
Position coordinates of the extrusion
</td>
		<td></td>
	</tr>
	<tr>
		<td>extrusionTriangles</td>
		<td>
Subset triangle topology used for the extrusion
</td>
		<td></td>
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

Component/Engine/Generate/ExtrudeSurface.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Engine.Generate"/> <!-- Needed to use components [ExtrudeSurface RandomPointDistributionInSurface] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [SphereROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <Node name="extrude">
            <MeshOBJLoader name="meshLoader" filename="mesh/liver.obj" />
            <MechanicalObject src="@meshLoader"/>
            <SphereROI name="surface1" centers="2 4 0" radii="0.88" drawSize="0" isVisible="0" src="@meshLoader" />
            <ExtrudeSurface template="Vec3" name="extrusion" triangles="@meshLoader.triangles" surfaceVertices="@meshLoader.position" surfaceTriangles="@surface1.triangleIndices" isVisible="0" />
            <RandomPointDistributionInSurface template="Vec3" vertices="@extrusion.extrusionVertices" triangles="@extrusion.extrusionTriangles" numberOfInPoints="100" numberOfTests="3" minDistanceBetweenPoints="0.1" />
        </Node>
        <Node name="Extrusion">
            <MeshTopology points="@../extrude/extrusion.extrusionVertices" triangles="@../extrude/extrusion.extrusionTriangles" />
            <MechanicalObject position="@../extrude/extrusion.extrusionVertices"/>
            <OglModel color="red" />
        </Node>
        <Node>
            <MeshOBJLoader name='myLoader' filename='mesh/liver.obj'/>
            <OglModel src='@myLoader'/>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Generate")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')

        extrude = root.addChild('extrude')
        extrude.addObject('MeshOBJLoader', name="meshLoader", filename="mesh/liver.obj")
        extrude.addObject('MechanicalObject', src="@meshLoader")
        extrude.addObject('SphereROI', name="surface1", centers="2 4 0", radii="0.88", drawSize="0", isVisible="0", src="@meshLoader")
        extrude.addObject('ExtrudeSurface', template="Vec3", name="extrusion", triangles="@meshLoader.triangles", surfaceVertices="@meshLoader.position", surfaceTriangles="@surface1.triangleIndices", isVisible="0")
        extrude.addObject('RandomPointDistributionInSurface', template="Vec3", vertices="@extrusion.extrusionVertices", triangles="@extrusion.extrusionTriangles", numberOfInPoints="100", numberOfTests="3", minDistanceBetweenPoints="0.1")

        Extrusion = root.addChild('Extrusion')
        Extrusion.addObject('MeshTopology', points="@../extrude/extrusion.extrusionVertices", triangles="@../extrude/extrusion.extrusionTriangles")
        Extrusion.addObject('MechanicalObject', position="@../extrude/extrusion.extrusionVertices")
        Extrusion.addObject('OglModel', color="red")

        root = root.addChild('root')
        root.addObject('MeshOBJLoader', name="myLoader", filename="mesh/liver.obj")
        root.addObject('OglModel', src="@myLoader")
    ```


<!-- automatically generated doc END -->
