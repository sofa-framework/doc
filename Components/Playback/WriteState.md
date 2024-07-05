# WriteState

Write State vectors to file at each timestep


__Target__: `Sofa.Component.Playback`

__namespace__: `#!c++ sofa::component::playback`

__parents__: 

- `#!c++ BaseObject`

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
		<td>filename</td>
		<td>
output file name
</td>
		<td></td>
	</tr>
	<tr>
		<td>writeX</td>
		<td>
flag enabling output of X vector
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>writeX0</td>
		<td>
flag enabling output of X0 vector
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>writeV</td>
		<td>
flag enabling output of V vector
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>writeF</td>
		<td>
flag enabling output of F vector
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>time</td>
		<td>
set time to write outputs (by default export at t=0)
</td>
		<td></td>
	</tr>
	<tr>
		<td>period</td>
		<td>
period between outputs
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>DOFsX</td>
		<td>
set the position DOFs to write
</td>
		<td></td>
	</tr>
	<tr>
		<td>DOFsV</td>
		<td>
set the velocity DOFs to write
</td>
		<td></td>
	</tr>
	<tr>
		<td>stopAt</td>
		<td>
stop the simulation when the given threshold is reached
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>keperiod</td>
		<td>
set the period to measure the kinetic energy increase
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

Component/Playback/WriteState.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 -9.81 0">
        <Node name="plugins">
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [SparseLDLSolver] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin name="Sofa.Component.Playback"/> <!-- Needed to use components [WriteState] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
            <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        </Node>
           
        <VisualStyle displayFlags="showForceFields showBehaviorModels showVisual showInteractionForceFields" />
        <DefaultAnimationLoop/>
    
        <!-- Beam under gravity -->
        <Node name="Beam">
            <EulerImplicitSolver/>                
            <SparseLDLSolver />
            
            <MechanicalObject name="beamMO" template="Vec3" />
            <RegularGridTopology nx="3" ny="3" nz="7" xmin="0" xmax="3" ymin="0" ymax="3" zmin="0" zmax="7" />
            <UniformMass totalMass="10" />
            
            <!-- WriteState: finds automatically the Mechanical within its node/context -->
            <!-- Export positions (X) every 0.01 (each time step) -->
            <WriteState name="StateWriter" filename="beamGravity.txt.gz" period="0.01" writeX="1" writeV="0" writeF="0" time="0"/>
    
            <FixedProjectiveConstraint indices="0-8" />
            <TetrahedronFEMForceField name="FEM" youngModulus="100" poissonRatio="0.3" method="large" />
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01", gravity="0 -9.81 0")

        plugins = root.addChild('plugins')
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Playback")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="showForceFields showBehaviorModels showVisual showInteractionForceFields")
        root.addObject('DefaultAnimationLoop')

        Beam = root.addChild('Beam')
        Beam.addObject('EulerImplicitSolver')
        Beam.addObject('SparseLDLSolver')
        Beam.addObject('MechanicalObject', name="beamMO", template="Vec3")
        Beam.addObject('RegularGridTopology', nx="3", ny="3", nz="7", xmin="0", xmax="3", ymin="0", ymax="3", zmin="0", zmax="7")
        Beam.addObject('UniformMass', totalMass="10")
        Beam.addObject('WriteState', name="StateWriter", filename="beamGravity.txt.gz", period="0.01", writeX="1", writeV="0", writeF="0", time="0")
        Beam.addObject('FixedProjectiveConstraint', indices="0-8")
        Beam.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="100", poissonRatio="0.3", method="large")
    ```

