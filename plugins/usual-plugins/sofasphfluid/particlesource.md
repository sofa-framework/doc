<!-- generate_doc -->
# ParticleSource

Parametrable particle generator


## Vec2d

Templates:

- Vec2d

__Target__: SofaSphFluid

__namespace__: sofa::component::misc

__parents__:

- ProjectiveConstraintSet

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
		<td>translation</td>
		<td>
translation applied to center(s)
		</td>
		<td>0 0</td>
	</tr>
	<tr>
		<td>scale</td>
		<td>
scale applied to center(s)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>center</td>
		<td>
Source center(s)
		</td>
		<td></td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
Source radius
		</td>
		<td>0 0</td>
	</tr>
	<tr>
		<td>velocity</td>
		<td>
Particle initial velocity
		</td>
		<td>0 0</td>
	</tr>
	<tr>
		<td>delay</td>
		<td>
Delay between particles creation
		</td>
		<td>0.01</td>
	</tr>
	<tr>
		<td>start</td>
		<td>
Source starting time
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>stop</td>
		<td>
Source stopping time
		</td>
		<td>1e+10</td>
	</tr>
	<tr>
		<td>addNoise</td>
		<td>
Will add random value to the radius of new created particles
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>lastparticles</td>
		<td>
lastparticles indices
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
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec2d&gt;|

<!-- generate_doc -->
## Vec3d

Templates:

- Vec3d

__Target__: SofaSphFluid

__namespace__: sofa::component::misc

__parents__:

- ProjectiveConstraintSet

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
		<td>translation</td>
		<td>
translation applied to center(s)
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>scale</td>
		<td>
scale applied to center(s)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>center</td>
		<td>
Source center(s)
		</td>
		<td></td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
Source radius
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>velocity</td>
		<td>
Particle initial velocity
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>delay</td>
		<td>
Delay between particles creation
		</td>
		<td>0.01</td>
	</tr>
	<tr>
		<td>start</td>
		<td>
Source starting time
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>stop</td>
		<td>
Source stopping time
		</td>
		<td>1e+10</td>
	</tr>
	<tr>
		<td>addNoise</td>
		<td>
Will add random value to the radius of new created particles
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>lastparticles</td>
		<td>
lastparticles indices
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
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|

## Examples 

ParticleSource.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node dt="0.005" gravity="0 -10 0" bbox="-4 -4 -4 4 4 4">
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Forward"/> <!-- Needed to use components [EulerExplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="SofaSphFluid"/> <!-- Needed to use components [ParticleSource] -->
        <VisualStyle displayFlags="showBehaviorModels showForceFields showWireframe" />
    
        <DefaultAnimationLoop/>
        <Node name="Particles">
            <EulerExplicitSolver symplectic="1" />
            <MechanicalObject name="MModel" showObject="1"/>        
            <ParticleSource name="Source" translation="0 4 0" radius="0.01 0.1 0.01" velocity="0 -1 0" delay="0.1" start="-0.1" stop="10" printLog="0"
            center="-0.375 0 -0.75 
                0.0 0.0 -0.75 
                0.375 0.0 -0.75 
                -0.75  0.0 -0.375 
                -0.375 0.0 -0.375 
                0.0 0.0 -0.375 
                0.375 0.0 -0.375 
                0.75 0.0 -0.375 
                -0.75 0.0 0.0 
                -0.375 0.0 0.0 
                0.0 0.0 0.0 
                0.375 0.0 0.0 
                0.75 0.0 0.0 
                -0.75 0.0 0.375 
                -0.375 0.0 0.375 
                0.0 0.0 0.375 
                0.375 0.0 0.375 
                0.75 0.0 0.375 
                -0.375 0.0 0.75 
                0.0 0.0 0.75 
                0.375 0.0 0.75"  />
            <UniformMass name="M1" vertexMass="1.0" />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       node = root_node.addChild('node', dt="0.005", gravity="0 -10 0", bbox="-4 -4 -4 4 4 4")

       node.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       node.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Forward")
       node.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       node.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       node.addObject('RequiredPlugin', name="SofaSphFluid")
       node.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields showWireframe")
       node.addObject('DefaultAnimationLoop', )

       particles = node.addChild('Particles')

       particles.addObject('EulerExplicitSolver', symplectic="1")
       particles.addObject('MechanicalObject', name="MModel", showObject="1")
       particles.addObject('ParticleSource', name="Source", translation="0 4 0", radius="0.01 0.1 0.01", velocity="0 -1 0", delay="0.1", start="-0.1", stop="10", printLog="0", center="-0.375 0 -0.75              0.0 0.0 -0.75              0.375 0.0 -0.75              -0.75  0.0 -0.375              -0.375 0.0 -0.375              0.0 0.0 -0.375              0.375 0.0 -0.375              0.75 0.0 -0.375              -0.75 0.0 0.0              -0.375 0.0 0.0              0.0 0.0 0.0              0.375 0.0 0.0              0.75 0.0 0.0              -0.75 0.0 0.375              -0.375 0.0 0.375              0.0 0.0 0.375              0.375 0.0 0.375              0.75 0.0 0.375              -0.375 0.0 0.75              0.0 0.0 0.75              0.375 0.0 0.75")
       particles.addObject('UniformMass', name="M1", vertexMass="1.0")
    ```

