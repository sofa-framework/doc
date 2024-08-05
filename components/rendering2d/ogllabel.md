# OglLabel

Display 2D text in the viewport.


__Target__: `Sofa.GL.Component.Rendering2D`

__namespace__: `#!c++ sofa::gl::component::rendering2d`

__parents__: 

- `#!c++ VisualModel`

__categories__: 

- VisualModel

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
		<td>prefix</td>
		<td>
The prefix of the text to display
</td>
		<td></td>
	</tr>
	<tr>
		<td>label</td>
		<td>
The text to display
</td>
		<td></td>
	</tr>
	<tr>
		<td>suffix</td>
		<td>
The suffix of the text to display
</td>
		<td></td>
	</tr>
	<tr>
		<td>x</td>
		<td>
The x position of the text on the screen
</td>
		<td>10</td>
	</tr>
	<tr>
		<td>y</td>
		<td>
The y position of the text on the screen
</td>
		<td>10</td>
	</tr>
	<tr>
		<td>fontsize</td>
		<td>
The size of the font used to display the text on the screen
</td>
		<td>14</td>
	</tr>
	<tr>
		<td>color</td>
		<td>
The color of the text to display. (default='gray')
</td>
		<td>0.5 0.5 0.5 1</td>
	</tr>
	<tr>
		<td>selectContrastingColor</td>
		<td>
Overide the color value but one that contrast with the background color
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>updateLabelEveryNbSteps</td>
		<td>
Update the display of the label every nb of time steps
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

Component/Visual/OglLabel.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    
    <Node name="root" dt="0.01" gravity="0 0 -9.81">
        <RequiredPlugin name="Sofa.Component.Engine.Analyze"/> <!-- Needed to use components [AverageCoord] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [PlaneForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.Setting"/> <!-- Needed to use components [BackgroundSetting] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [MeshSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualGrid VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering2D"/> <!-- Needed to use components [OglLabel] -->
        <DefaultAnimationLoop/>
        
    	<VisualStyle displayFlags="showForceFields"/>
    	<BackgroundSetting color="0.8 0.4 0.6"/>
    
    	<VisualGrid size="16" plane="y"/>
    
    	<EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
    	<CGLinearSolver name="CG Solver" iterations="100" tolerance="1e-5" threshold="1e-5" />
    
    	<MechanicalObject name="Particles" template="Vec3"
    		    position="0 0 1  1 0 1  0 1 1  1 1 1  0 0 2  1 0 2  0 1 2  1 1 2" />
    
    	<MeshTopology name="Topology" hexas="0 4 6 2 1 5 7 3" />
    
    	<UniformMass name="Mass" totalMass="1" />
    	<MeshSpringForceField name="Springs" stiffness="100" damping="1" />
    
    	<PlaneForceField name="Floor" normal="-0.2 0 1" stiffness="100" damping="1"/>
    	<!-- <PlaneForceField name="Wall" normal="0 -1 0" d="-4" stiffness="100" damping="1" draw="1" color="0.4 0.4 0.4" /> -->
    
    	<AverageCoord name="center" template="Vec3" listening="true"/>
    
    	<OglLabel label="Sofa framework" fontsize="30"/>
    	<OglLabel label="Falling cube on an inclined plane" fontsize="20" y="50"/>
    	<OglLabel label="@center.average" fontsize="20" selectContrastingColor='true' prefix="Cube position: " updateLabelEveryNbSteps="30" y="75"/>
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01", gravity="0 0 -9.81")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Analyze")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.Setting")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering2D")
        root.addObject('DefaultAnimationLoop')
        root.addObject('VisualStyle', displayFlags="showForceFields")
        root.addObject('BackgroundSetting', color="0.8 0.4 0.6")
        root.addObject('VisualGrid', size="16", plane="y")
        root.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        root.addObject('CGLinearSolver', name="CG Solver", iterations="100", tolerance="1e-5", threshold="1e-5")
        root.addObject('MechanicalObject', name="Particles", template="Vec3", position="0 0 1  1 0 1  0 1 1  1 1 1  0 0 2  1 0 2  0 1 2  1 1 2")
        root.addObject('MeshTopology', name="Topology", hexas="0 4 6 2 1 5 7 3")
        root.addObject('UniformMass', name="Mass", totalMass="1")
        root.addObject('MeshSpringForceField', name="Springs", stiffness="100", damping="1")
        root.addObject('PlaneForceField', name="Floor", normal="-0.2 0 1", stiffness="100", damping="1")
        root.addObject('AverageCoord', name="center", template="Vec3", listening="true")
        root.addObject('OglLabel', label="Sofa framework", fontsize="30")
        root.addObject('OglLabel', label="Falling cube on an inclined plane", fontsize="20", y="50")
        root.addObject('OglLabel', label="@center.average", fontsize="20", selectContrastingColor="true", prefix="Cube position: ", updateLabelEveryNbSteps="30", y="75")
    ```

