<!-- generate_doc -->
# TrailRenderer

Render a trail behind particles.


Templates:

- Rigid3d
- Vec3d

__Target__: Sofa.Component.Visual

__namespace__: sofa::component::visual

__parents__:

- VisualModel

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
		<td>position</td>
		<td>
Position of the particles behind which a trail is rendered
		</td>
		<td></td>
	</tr>
	<tr>
		<td>nbSteps</td>
		<td>
Number of time steps to use to render the trail
		</td>
		<td>100</td>
	</tr>
	<tr>
		<td>color</td>
		<td>
Color of the trail
		</td>
		<td>0 1 0 1</td>
	</tr>
	<tr>
		<td>thickness</td>
		<td>
Thickness of the trail
		</td>
		<td>1</td>
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

TrailRenderer.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    
    <Node name="root" gravity="0 -9.81 0" dt="0.01">
        <DefaultAnimationLoop/>
        <Node name="plugins">
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Forward"/> <!-- Needed to use components [EulerExplicitSolver] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [TrailRenderer VisualGrid] -->
        </Node>
    
        <VisualGrid size="20"/>
    
        <DefaultAnimationLoop/>
    
        <EulerExplicitSolver/>
        <MechanicalObject template="Vec3" name="particle"
                          position="0 0 0  0 0 0  0 0 0  0 0 0"
                          velocity="5 5 0  -5 5 0  7 7 0  -7 7 0" showObject="true" showObjectScale="10"/>
        <UniformMass totalMass="1.0"/>
        <TrailRenderer template="Vec3" position="@particle.position" nbSteps="200"/>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9.81 0", dt="0.01")

       root.addObject('DefaultAnimationLoop', )

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Forward")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Visual")

       root.addObject('VisualGrid', size="20")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('EulerExplicitSolver', )
       root.addObject('MechanicalObject', template="Vec3", name="particle", position="0 0 0  0 0 0  0 0 0  0 0 0", velocity="5 5 0  -5 5 0  7 7 0  -7 7 0", showObject="true", showObjectScale="10")
       root.addObject('UniformMass', totalMass="1.0")
       root.addObject('TrailRenderer', template="Vec3", position="@particle.position", nbSteps="200")
    ```

