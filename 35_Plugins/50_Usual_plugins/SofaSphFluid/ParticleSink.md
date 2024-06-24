# ParticleSink

Parametrable particle generator


__Templates__:

- `#!c++ Vec2d`
- `#!c++ Vec3d`

__Target__: `SofaSphFluid`

__namespace__: `#!c++ sofa::component::misc`

__parents__: 

- `#!c++ ProjectiveConstraintSet`

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
		<td>group</td>
		<td>
ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>endTime</td>
		<td>
The constraint stops acting after the given value.
Use a negative value for infinite constraints
</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>normal</td>
		<td>
plane normal
</td>
		<td></td>
	</tr>
	<tr>
		<td>d0</td>
		<td>
plane d coef at which particles acceleration is constrained to 0
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>d1</td>
		<td>
plane d coef at which particles are removed
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>fixed</td>
		<td>
indices of fixed particles
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showPlane</td>
		<td>
enable/disable drawing of plane
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
|mechanicalStates|List of mechanical states to which this component is associated|
|mstate|MechanicalState used by this component|
|topology|link to the topology container|



## Examples

SofaSphFluid/share/sofa/examples/SofaSphFluid/ParticleSink.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node dt="0.005" gravity="0 -10 0" bbox="-6 -6 -6  6 6 6">
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Forward"/> <!-- Needed to use components [EulerExplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="SofaSphFluid"/> <!-- Needed to use components [ParticleSink ParticleSource] -->
        <VisualStyle displayFlags="showBehaviorModels showForceFields hideWireframe" />
        <DefaultAnimationLoop/>
        <Node name="Fluid">
            <EulerExplicitSolver symplectic="1" />
            <MechanicalObject name="MModel" showObject="1"/>
            <ParticleSource name="Source" 
                center="-0.375 0 -0.75    
                0 0 -0.75    
                0.375 0 -0.75    
                -0.75  0 -0.375    
                -0.375 0 -0.375    
                0 0 -0.375    
                0.375 0 -0.375    
                0.75  0 -0.375    
                -0.75  0  0.0    
                -0.375 0  0.0    
                0 0  0    
                0.375 0  0.0    
                0.75  0  0.0    
                -0.75  0  0.375    
                -0.375 0  0.375    
                0.0   0  0.375    
                0.375 0  0.375    
                0.75  0  0.375    
                -0.375 0  0.75    
                0 0  0.75    
                0.375 0  0.75" 
                translation="0 3 0" radius="0.01 0.1 0.01" velocity="0 -20 0" delay="0.01875" start="-0.1" stop="2" />
            <ParticleSink normal="0 1 0" d0="-10" d1="-11" showPlane="true" printLog="false" />
            <UniformMass name="M1" vertexMass="1.0" />
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        rootNode = rootNode.addChild('rootNode', dt="0.005", gravity="0 -10 0", bbox="-6 -6 -6  6 6 6")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Forward")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        rootNode.addObject('RequiredPlugin', name="SofaSphFluid")
        rootNode.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields hideWireframe")
        rootNode.addObject('DefaultAnimationLoop')

        Fluid = rootNode.addChild('Fluid')
        Fluid.addObject('EulerExplicitSolver', symplectic="1")
        Fluid.addObject('MechanicalObject', name="MModel", showObject="1")
        Fluid.addObject('ParticleSource', name="Source", center="-0.375 0 -0.75    
            0 0 -0.75    
            0.375 0 -0.75    
            -0.75  0 -0.375    
            -0.375 0 -0.375    
            0 0 -0.375    
            0.375 0 -0.375    
            0.75  0 -0.375    
            -0.75  0  0.0    
            -0.375 0  0.0    
            0 0  0    
            0.375 0  0.0    
            0.75  0  0.0    
            -0.75  0  0.375    
            -0.375 0  0.375    
            0.0   0  0.375    
            0.375 0  0.375    
            0.75  0  0.375    
            -0.375 0  0.75    
            0 0  0.75    
            0.375 0  0.75", translation="0 3 0", radius="0.01 0.1 0.01", velocity="0 -20 0", delay="0.01875", start="-0.1", stop="2")
        Fluid.addObject('ParticleSink', normal="0 1 0", d0="-10", d1="-11", showPlane="true", printLog="false")
        Fluid.addObject('UniformMass', name="M1", vertexMass="1.0")
    ```

