# OglCylinderModel

A simple visualization for set of cylinder.


__Target__: `Sofa.GL.Component.Rendering3D`

__namespace__: `#!c++ sofa::gl::component::rendering3d`

__parents__: 

- `#!c++ VisualModel`
- `#!c++ VisualState`

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
		<td>enable</td>
		<td>
Display the object or not
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
Radius of the cylinder.
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>color</td>
		<td>
Color of the cylinders.
</td>
		<td>1 1 1 1</td>
	</tr>
	<tr>
		<td>edges</td>
		<td>
List of edge indices
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Vector</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Vertices coordinates
</td>
		<td></td>
	</tr>
	<tr>
		<td>restPosition</td>
		<td>
Vertices rest coordinates
</td>
		<td></td>
	</tr>
	<tr>
		<td>normal</td>
		<td>
Normals of the model
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

Component/Visual/OglCylinderModel.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglCylinderModel] -->
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showVisual" />
        <OglCylinderModel  position="0 0 0   10 0 0 "  edges="0 1" />
        
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')
        root.addObject('VisualStyle', displayFlags="showVisual")
        root.addObject('OglCylinderModel', position="0 0 0   10 0 0 ", edges="0 1")
    ```

