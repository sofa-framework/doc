# Fluid3D

Eulerian 3D fluid


__Target__: `SofaEulerianFluid`

__namespace__: `#!c++ sofa::component::behaviormodel::eulerianfluid`

__parents__: 

- `#!c++ BehaviorModel`

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
		<td>nx</td>
		<td>
grid size along x axis
</td>
		<td>16</td>
	</tr>
	<tr>
		<td>ny</td>
		<td>
grid size along y axis
</td>
		<td>16</td>
	</tr>
	<tr>
		<td>nz</td>
		<td>
grid size along z axis
</td>
		<td>16</td>
	</tr>
	<tr>
		<td>cellwidth</td>
		<td>
width of each cell
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>center</td>
		<td>
position of grid center
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>height</td>
		<td>
initial fluid height
</td>
		<td>5</td>
	</tr>
	<tr>
		<td>dir</td>
		<td>
initial fluid surface normal
</td>
		<td>0 1 0</td>
	</tr>
	<tr>
		<td>tstart</td>
		<td>
starting time for fluid source
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>tstop</td>
		<td>
stopping time for fluid source
</td>
		<td>60</td>
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

SofaEulerianFluid/share/sofa/examples/SofaEulerianFluid/Fluid3D.scn

=== "XML"

    ```xml
    <Node dt="0.04" gravity="0 -10 0">
        <VisualStyle displayFlags="showForceFields showCollisionModels showMappings" />
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="SofaEulerianFluid"/> <!-- Needed to use components [Fluid3D] -->
    
        <Fluid3D nx="32" ny="32" nz="32" tstart="0" tstop="0" height="20.5" dir="0.5 0 1" />
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        rootNode = rootNode.addChild('rootNode', dt="0.04", gravity="0 -10 0")
        rootNode.addObject('VisualStyle', displayFlags="showForceFields showCollisionModels showMappings")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        rootNode.addObject('RequiredPlugin', name="SofaEulerianFluid")
        rootNode.addObject('Fluid3D', nx="32", ny="32", nz="32", tstart="0", tstop="0", height="20.5", dir="0.5 0 1")
    ```

