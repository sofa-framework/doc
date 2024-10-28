<!-- generate_doc -->
# CompareState

Compare State vectors from a reference frame to the associated Mechanical State.


__Target__: Sofa.Component.Playback

__namespace__: sofa::component::playback

__parents__:

- ReadState

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
		<td>filename</td>
		<td>
output file name
		</td>
		<td></td>
	</tr>
	<tr>
		<td>interval</td>
		<td>
time duration between inputs
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>shift</td>
		<td>
shift between times in the file and times when they will be read
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>loop</td>
		<td>
set to 'true' to re-read the file when reaching the end
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Transformation</td>
	</tr>
	<tr>
		<td>scalePos</td>
		<td>
scale the input mechanical object
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>rotation</td>
		<td>
rotate the input mechanical object
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>translation</td>
		<td>
translate the input mechanical object
		</td>
		<td>0 0 0</td>
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

CompareState.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 -9.81 0">
        <Node name="plugins">
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [SparseLDLSolver] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin name="Sofa.Component.Playback"/> <!-- Needed to use components [CompareState] -->
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
            <UniformMass totalMass="5" />
            
            <!-- CompareState: read file beamGravity exported with totalMass == 10 -->
            <CompareState name="StateComparator" filename="beamGravity.txt.gz" printLog="0"/>
    
            <FixedProjectiveConstraint indices="0-8" />
            <TetrahedronFEMForceField name="FEM" youngModulus="100" poissonRatio="0.3" method="large" />
        </Node>
        
        <Node name="BeamReplay">
            <MechanicalObject name="beamMO" showObject="1"/>
            <RegularGridTopology name="grid" nx="3" ny="3" nz="7" xmin="0" xmax="3" ymin="0" ymax="3" zmin="0" zmax="7" />
            <ReadState name="StateReader" filename="beamGravity.txt.gz" />
            
            <Node name="visu">
                <EdgeSetTopologyContainer edges="@../grid.edges"/>
                <EdgeSetTopologyModifier />
                <EdgeSetGeometryAlgorithms template="Vec3" drawEdges="1"/>
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 -9.81 0")

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Playback")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Visual")

       root.addObject('VisualStyle', displayFlags="showForceFields showBehaviorModels showVisual showInteractionForceFields")
       root.addObject('DefaultAnimationLoop', )

       beam = root.addChild('Beam')

       beam.addObject('EulerImplicitSolver', )
       beam.addObject('SparseLDLSolver', )
       beam.addObject('MechanicalObject', name="beamMO", template="Vec3")
       beam.addObject('RegularGridTopology', nx="3", ny="3", nz="7", xmin="0", xmax="3", ymin="0", ymax="3", zmin="0", zmax="7")
       beam.addObject('UniformMass', totalMass="5")
       beam.addObject('CompareState', name="StateComparator", filename="beamGravity.txt.gz", printLog="0")
       beam.addObject('FixedProjectiveConstraint', indices="0-8")
       beam.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="100", poissonRatio="0.3", method="large")

       beam_replay = root.addChild('BeamReplay')

       beam_replay.addObject('MechanicalObject', name="beamMO", showObject="1")
       beam_replay.addObject('RegularGridTopology', name="grid", nx="3", ny="3", nz="7", xmin="0", xmax="3", ymin="0", ymax="3", zmin="0", zmax="7")
       beam_replay.addObject('ReadState', name="StateReader", filename="beamGravity.txt.gz")

       visu = BeamReplay.addChild('visu')

       visu.addObject('EdgeSetTopologyContainer', edges="@../grid.edges")
       visu.addObject('EdgeSetTopologyModifier', )
       visu.addObject('EdgeSetGeometryAlgorithms', template="Vec3", drawEdges="1")
    ```

