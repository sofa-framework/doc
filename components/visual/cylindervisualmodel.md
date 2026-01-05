<!-- generate_doc -->
# CylinderVisualModel

Visualize a set of cylinders.


__Target__: Sofa.Component.Visual

__namespace__: sofa::component::visual

__parents__:

- VisualModel
- VisualState

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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|

## Examples 

CylinderVisualModel.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [CylinderVisualModel VisualStyle] -->
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showVisual" />
        <CylinderVisualModel  position="0 0 0   10 0 0 "  edges="0 1" color="yellow" />
        
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02")

       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showVisual")
       root.addObject('CylinderVisualModel', position="0 0 0   10 0 0 ", edges="0 1", color="yellow")
    ```

