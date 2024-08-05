# AdaptiveBeamController

Adaptive beam controller


__Templates__:

- `#!c++ Rigid3d`

__Target__: `BeamAdapter`

__namespace__: `#!c++ sofa::component::controller::_adaptivebeamcontroller_`

__parents__: 

- `#!c++ MechanicalStateController`

__categories__: 

- Controller

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
		<td>handleEventTriggersUpdate</td>
		<td>
Event handling frequency controls the controller update frequency
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>index</td>
		<td>
Index of the controlled DOF
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>onlyTranslation</td>
		<td>
Controlling the DOF only in translation
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>buttonDeviceState</td>
		<td>
state of ths device button
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>mainDirection</td>
		<td>
Main direction and orientation of the controlled DOF
</td>
		<td>0 0 -1</td>
	</tr>
	<tr>
		<td>interpolation</td>
		<td>
Path to the Interpolation component on scene
</td>
		<td></td>
	</tr>
	<tr>
		<td>controlledInstrument</td>
		<td>
provide the id of the interventional radiology instrument which is under control: press contr + number to change it
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>xtip</td>
		<td>
curvilinear abscissa of the tip of each interventional radiology instrument
</td>
		<td></td>
	</tr>
	<tr>
		<td>rotationInstrument</td>
		<td>
angle of rotation for each interventional radiology instrument
</td>
		<td></td>
	</tr>
	<tr>
		<td>step</td>
		<td>
base step when changing beam length
</td>
		<td>0.1</td>
	</tr>
	<tr>
		<td>angularStep</td>
		<td>
base step when changing beam angle
</td>
		<td>0.15708</td>
	</tr>
	<tr>
		<td>speed</td>
		<td>
continuous beam length increase/decrease
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

BeamAdapter/examples/AdaptiveBeamController.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="0 -9.81 0" dt="0.01" bbox="0 0 0 10 10 10">
    	<RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
    	<RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [EigenSparseLU] -->
    	<RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
    	<RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
    	<RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
    	<RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="BeamAdapter"/> <!-- Needed to use components [AdaptiveBeamController,AdaptiveBeamForceFieldAndMass,BeamInterpolation] -->
    
    	<VisualStyle displayFlags="showBehaviorModels showCollisionModels hideBoundingCollisionModels showForceFields" />
    	<DefaultAnimationLoop />
        
    	<Node name="AdaptiveBeam1">
    		<EulerImplicitSolver rayleighStiffness="0" rayleighMass="0" printLog="false" />
    		<EigenSparseLU template="CompressedRowSparseMatrixMat3x3d"/>
    		<MechanicalObject template="Rigid3d" name="DOFs" position="0 0 0 0 0 0 1  0.5 0 0 0 0 0 1  1 0 0 0 0 0 1  1.5 0 0 0 0 0 1  2 0 0 0 0 0 1  2.5 0 0 0 0 0 1  3 0 0 0 0 0 1"/> 
    		<MeshTopology name="lines" lines="0 1 1 2 2 3 3 4 4 5 5 6" /> 
    		<FixedProjectiveConstraint name="FixedConstraint" indices="0" />
    		<BeamInterpolation name="BeamInterpolation" radius="0.1"/> 
    		<AdaptiveBeamForceFieldAndMass name="BeamForceField"   computeMass="1" massDensity="50"/> 
    <!--
    		<Node name="Collision">
    			<CubeTopology nx="13" ny="2" nz="2" min="0 -0.2 -0.2" max="3 0.2 0.2" />
    			<MechanicalObject name="collision"/>
    			<AdaptiveBeamMapping isMechanical="true" input="@../DOFs" output="@collision"/>
    			<Triangle />
    		</Node>
    -->
    	</Node>
    
    	<Node name="AdaptiveBeam2">
    		<EulerImplicitSolver rayleighStiffness="0" rayleighMass="0" printLog="false" />
    		<EigenSparseLU template="CompressedRowSparseMatrixMat3x3d"/>
    		<MeshTopology name="lines" lines="0 1 1 2 2 3" /> 
    		<MechanicalObject template="Rigid3d" name="DOFs" position="0 0 2 0 0 0 1  1 0 2 0 0 0 1  2 0 2 0 0 0 1  3 0 2 0 0 0 1"/> 
    		<BeamInterpolation name="BeamInterpolation2" radius="0.1" /> 
    		<FixedProjectiveConstraint name="FixedConstraint" indices="0" />
    		<AdaptiveBeamController template="Rigid3d" name="m_controller"/>	
    		<AdaptiveBeamForceFieldAndMass name="BeamForceField"  computeMass="1" massDensity="50"/> 
    <!--
    		<Node name="Collision">
    			<CubeTopology nx="13" ny="2" nz="2" min="0 -0.2 -0.2" max="3 0.2 0.2" />
    			<MechanicalObject name="collision"/>
    			<AdaptiveBeamMapping isMechanical="true" input="@../DOFs" output="@collision"/>
    			<Triangle />
    		</Node>
    -->
    	</Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -9.81 0", dt="0.01", bbox="0 0 0 10 10 10")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="BeamAdapter")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showCollisionModels hideBoundingCollisionModels showForceFields")
        root.addObject('DefaultAnimationLoop')

        AdaptiveBeam1 = root.addChild('AdaptiveBeam1')
        AdaptiveBeam1.addObject('EulerImplicitSolver', rayleighStiffness="0", rayleighMass="0", printLog="false")
        AdaptiveBeam1.addObject('EigenSparseLU', template="CompressedRowSparseMatrixMat3x3d")
        AdaptiveBeam1.addObject('MechanicalObject', template="Rigid3d", name="DOFs", position="0 0 0 0 0 0 1  0.5 0 0 0 0 0 1  1 0 0 0 0 0 1  1.5 0 0 0 0 0 1  2 0 0 0 0 0 1  2.5 0 0 0 0 0 1  3 0 0 0 0 0 1")
        AdaptiveBeam1.addObject('MeshTopology', name="lines", lines="0 1 1 2 2 3 3 4 4 5 5 6")
        AdaptiveBeam1.addObject('FixedProjectiveConstraint', name="FixedConstraint", indices="0")
        AdaptiveBeam1.addObject('BeamInterpolation', name="BeamInterpolation", radius="0.1")
        AdaptiveBeam1.addObject('AdaptiveBeamForceFieldAndMass', name="BeamForceField", computeMass="1", massDensity="50")

        AdaptiveBeam2 = root.addChild('AdaptiveBeam2')
        AdaptiveBeam2.addObject('EulerImplicitSolver', rayleighStiffness="0", rayleighMass="0", printLog="false")
        AdaptiveBeam2.addObject('EigenSparseLU', template="CompressedRowSparseMatrixMat3x3d")
        AdaptiveBeam2.addObject('MeshTopology', name="lines", lines="0 1 1 2 2 3")
        AdaptiveBeam2.addObject('MechanicalObject', template="Rigid3d", name="DOFs", position="0 0 2 0 0 0 1  1 0 2 0 0 0 1  2 0 2 0 0 0 1  3 0 2 0 0 0 1")
        AdaptiveBeam2.addObject('BeamInterpolation', name="BeamInterpolation2", radius="0.1")
        AdaptiveBeam2.addObject('FixedProjectiveConstraint', name="FixedConstraint", indices="0")
        AdaptiveBeam2.addObject('AdaptiveBeamController', template="Rigid3d", name="m_controller")
        AdaptiveBeam2.addObject('AdaptiveBeamForceFieldAndMass', name="BeamForceField", computeMass="1", massDensity="50")
    ```

