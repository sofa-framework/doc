# AdaptiveBeamMapping

Set the positions and velocities of points attached to a beam using linear interpolation between DOFs


__Templates__:

- `#!c++ Rigid3d,Rigid3d`
- `#!c++ Rigid3d,Vec3d`

__Target__: `BeamAdapter`

__namespace__: `#!c++ sofa::component::mapping::_adaptivebeammapping_`

__parents__: 

- `#!c++ Mapping`

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
		<td>mapForces</td>
		<td>
Are forces mapped ?
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapConstraints</td>
		<td>
Are constraints mapped ?
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapMasses</td>
		<td>
Are masses mapped ?
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapMatrices</td>
		<td>
Are matrix explicit mapped?
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>applyRestPosition</td>
		<td>
set to true to apply this mapping to restPosition at init
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>useCurvAbs</td>
		<td>
true if the curvilinear abscissa of the points remains the same during the simulation if not the curvilinear abscissa moves with adaptivity and the num of segment per beam is always the same
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>points</td>
		<td>
defines the mapped points along the beam axis (in beam frame local coordinates)
</td>
		<td></td>
	</tr>
	<tr>
		<td>proximity</td>
		<td>
if positive, the mapping is modified for the constraints to take into account the lever created by the proximity
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>contactDuplicate</td>
		<td>
if true, this mapping is a copy of an input mapping and is used to gather contact points (ContinuousFrictionContact Response)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>nameOfInputMap</td>
		<td>
if contactDuplicate==true, it provides the name of the input mapping
</td>
		<td></td>
	</tr>
	<tr>
		<td>nbPointsPerBeam</td>
		<td>
if non zero, we will adapt the points depending on the discretization, with this num of points per beam (compatible with useCurvAbs)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>segmentsCurvAbs</td>
		<td>
the abscissa of each point on the collision model
</td>
		<td></td>
	</tr>
	<tr>
		<td>parallelMapping</td>
		<td>
flag to enable parallel internal computation
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
|input|Input object to map|
|output|Output object to map|
|interpolation|Path to the Interpolation component on scene|



## Examples

BeamAdapter/examples/AdaptiveBeamMapping.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="0 -9.81 0" dt="0.01" >
     	<RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
     	<RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedConstraint] -->
     	<RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [BTDLinearSolver] -->
     	<RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
     	<RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
     	<RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [CubeTopology MeshTopology] -->
     	<RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    	<VisualStyle displayFlags="showBehaviorModels showCollisionModels hideBoundingCollisionModels showForceFields" />
    
    	<DefaultAnimationLoop />
    	<DefaultVisualManagerLoop />
    
    	<Node name="AdaptiveBeam2">
    		<EulerImplicitSolver rayleighStiffness="0" rayleighMass="0" printLog="false" />
    		<BTDLinearSolver verbose="0"/>
    		<MechanicalObject template="Rigid3d" name="DOFs" position="0 0 2 0 0 0 1  1 0 2 0 0 0 1  2 0 2 0 0 0 1  3 0 2 0 0 0 1"/> 
    		<MeshTopology name="lines" lines="0 1 1 2 2 3" /> 
    		<FixedConstraint name="FixedConstraint" indices="0" />
    		<BeamInterpolation name="BeamInterpolation" radius="0.1" /> 
    		<AdaptiveBeamForceFieldAndMass name="BeamForceField"  computeMass="1" massDensity="10"/>
    		<Node name="Collision">
    			<CubeTopology nx="20" ny="2" nz="2" min="0 -0.1 -0.1" max="3 0.1 0.1" />
    			<MechanicalObject template="Vec3d" name="collision"/>
    			<TriangleCollisionModel color="0.5 1 0.5 1" />
    			<AdaptiveBeamMapping isMechanical="true" input="@../DOFs"  output="@collision" mapForces="0" mapMasses="0"/>		
    		</Node>
    	</Node>  
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -9.81 0", dt="0.01")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showCollisionModels hideBoundingCollisionModels showForceFields")
        root.addObject('DefaultAnimationLoop')
        root.addObject('DefaultVisualManagerLoop')

        AdaptiveBeam2 = root.addChild('AdaptiveBeam2')
        AdaptiveBeam2.addObject('EulerImplicitSolver', rayleighStiffness="0", rayleighMass="0", printLog="false")
        AdaptiveBeam2.addObject('BTDLinearSolver', verbose="0")
        AdaptiveBeam2.addObject('MechanicalObject', template="Rigid3d", name="DOFs", position="0 0 2 0 0 0 1  1 0 2 0 0 0 1  2 0 2 0 0 0 1  3 0 2 0 0 0 1")
        AdaptiveBeam2.addObject('MeshTopology', name="lines", lines="0 1 1 2 2 3")
        AdaptiveBeam2.addObject('FixedConstraint', name="FixedConstraint", indices="0")
        AdaptiveBeam2.addObject('BeamInterpolation', name="BeamInterpolation", radius="0.1")
        AdaptiveBeam2.addObject('AdaptiveBeamForceFieldAndMass', name="BeamForceField", computeMass="1", massDensity="10")

        Collision = AdaptiveBeam2.addChild('Collision')
        Collision.addObject('CubeTopology', nx="20", ny="2", nz="2", min="0 -0.1 -0.1", max="3 0.1 0.1")
        Collision.addObject('MechanicalObject', template="Vec3d", name="collision")
        Collision.addObject('TriangleCollisionModel', color="0.5 1 0.5 1")
        Collision.addObject('AdaptiveBeamMapping', isMechanical="true", input="@../DOFs", output="@collision", mapForces="0", mapMasses="0")
    ```

