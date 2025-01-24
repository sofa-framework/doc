<!-- generate_doc -->
# DistanceMultiMapping

Mapping point positions from several mechanical states to distances (in distance unit).


## Rigid3d,Vec1d

Templates:

- Rigid3d,Vec1d

__Target__: Sofa.Component.Mapping.NonLinear

__namespace__: sofa::component::mapping::nonlinear

__parents__:

- MultiMapping

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
		<td>geometricStiffness</td>
		<td>
Method used to compute the geometric stiffness:
-None: geometric stiffness is not computed
-Exact: the exact geometric stiffness is computed
-Stabilized: the exact geometric stiffness is approximated in order to improve stability
		</td>
		<td>Stabilized</td>
	</tr>
	<tr>
		<td>computeDistance</td>
		<td>
if 'computeDistance = true', then rest length of each element equal 0, otherwise rest length is the initial length of each of them
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>restLengths</td>
		<td>
Rest lengths of the connections
		</td>
		<td></td>
	</tr>
	<tr>
		<td>indexPairs</td>
		<td>
list of couples (parent index + index in the parent)
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showObjectScale</td>
		<td>
Scale for object display
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showColor</td>
		<td>
Color for object display. (default=[1.0,1.0,0.0,1.0])
		</td>
		<td>1 1 0 1</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|input|Input Object(s)|State&lt;Rigid3d&gt;|
|output|Output Object(s)|State&lt;Vec1d&gt;|
|topology|link to the topology container|BaseMeshTopology|

<!-- generate_doc -->
## Vec3d,Vec1d

Templates:

- Vec3d,Vec1d

__Target__: Sofa.Component.Mapping.NonLinear

__namespace__: sofa::component::mapping::nonlinear

__parents__:

- MultiMapping

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
		<td>geometricStiffness</td>
		<td>
Method used to compute the geometric stiffness:
-None: geometric stiffness is not computed
-Exact: the exact geometric stiffness is computed
-Stabilized: the exact geometric stiffness is approximated in order to improve stability
		</td>
		<td>Stabilized</td>
	</tr>
	<tr>
		<td>computeDistance</td>
		<td>
if 'computeDistance = true', then rest length of each element equal 0, otherwise rest length is the initial length of each of them
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>restLengths</td>
		<td>
Rest lengths of the connections
		</td>
		<td></td>
	</tr>
	<tr>
		<td>indexPairs</td>
		<td>
list of couples (parent index + index in the parent)
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showObjectScale</td>
		<td>
Scale for object display
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showColor</td>
		<td>
Color for object display. (default=[1.0,1.0,0.0,1.0])
		</td>
		<td>1 1 0 1</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|input|Input Object(s)|State&lt;Vec3d&gt;|
|output|Output Object(s)|State&lt;Vec1d&gt;|
|topology|link to the topology container|BaseMeshTopology|

## Examples 

DistanceMultiMapping.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="Root" gravity="0 -10 0" time="0" animate="0"  dt="0.01">
    
        <Node name="plugins">
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin name="Sofa.Component.Engine.Transform"/> <!-- Needed to use components [TransformEngine] -->
            <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [StringMeshCreator] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
            <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [DistanceMapping DistanceMultiMapping] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
            <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [UniformVelocityDampingForceField] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [RestShapeSpringsForceField] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [EdgeSetGeometryAlgorithms EdgeSetTopologyContainer] -->
            <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        </Node>
    
        <DefaultVisualManagerLoop/>
        <VisualStyle displayFlags="showVisualModels showBehaviorModels showMappings showForceFields showMechanicalMappings" />
    
        <DefaultAnimationLoop/>
        <StringMeshCreator name="loader" resolution="20" />
    
        <EulerImplicitSolver rayleighStiffness="0.1" rayleighMass="0.1"/>
        <CGLinearSolver iterations="2500" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
        <Node  name="springs0" >
            <TransformEngine name="translate" input_position="@../loader.position" translation="0 0 0" />
    
            <EdgeSetTopologyContainer name="topology" position="@translate.output_position" edges="@../loader.edges" />
            <MechanicalObject name="defoDOF" template="Vec3" />
            <EdgeSetGeometryAlgorithms drawEdges="true" />
            <FixedProjectiveConstraint indices="0" />
            <DiagonalMass  name="mass" totalMass="1e-2"/>
            <UniformVelocityDampingForceField template="Vec3" name="uniformVelocityDampingFF0" implicit="true" dampingCoefficient="0.005"/>
            <Node name="extensionsNode" >
                <MechanicalObject template="Vec1" name="extensionsDOF" />
                <DistanceMapping name="distanceMapping" topology="@../topology" input="@../defoDOF" output="@extensionsDOF" geometricStiffness="0" applyRestPosition="true" computeDistance="true"/>
                <RestShapeSpringsForceField template="Vec1" stiffness="1000"/>
            </Node>
        </Node>
    
        <Node  name="springs1" >
            <TransformEngine name="translate" input_position="@../loader.position" translation="1.2 0 0" />
    
            <EdgeSetTopologyContainer name="topology" position="@translate.output_position" edges="@../loader.edges" />
            <MechanicalObject name="defoDOF" template="Vec3" />
            <EdgeSetGeometryAlgorithms drawEdges="true" />
            <FixedProjectiveConstraint indices="19" />
            <DiagonalMass  name="mass" totalMass="1e-2"/>
            <UniformVelocityDampingForceField template="Vec3" name="uniformVelocityDampingFF0" implicit="true" dampingCoefficient="0.005"/>
            <Node name="extensionsNode" >
                <MechanicalObject template="Vec1" name="extensionsDOF" />
                <DistanceMapping name="distanceMapping" topology="@../topology" input="@../defoDOF" output="@extensionsDOF" geometricStiffness="0" applyRestPosition="true" computeDistance="true"/>
                <RestShapeSpringsForceField template="Vec1" stiffness="1000"/>
            </Node>
        </Node>
    
        <Node name="connection">
            <MechanicalObject template="Vec1" name="connectionDOF" />
            <EdgeSetTopologyContainer name="edgeTopo" edges="0 1"/>
            <DistanceMultiMapping template="Vec3,Vec1" topology="@edgeTopo" input="@../springs0 @../springs1" output="@connectionDOF" indexPairs="0 19 1 0" restLengths="1" geometricStiffness="0" applyRestPosition="true" computeDistance="true"/>
            <RestShapeSpringsForceField template="Vec1" stiffness="1"/>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('Root', gravity="0 -10 0", time="0", animate="0", dt="0.01")

       plugins = Root.addChild('plugins')

       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Engine.Transform")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Visual")

       root.addObject('DefaultVisualManagerLoop', )
       root.addObject('VisualStyle', displayFlags="showVisualModels showBehaviorModels showMappings showForceFields showMechanicalMappings")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('StringMeshCreator', name="loader", resolution="20")
       root.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
       root.addObject('CGLinearSolver', iterations="2500", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")

       springs0 = Root.addChild('springs0')

       springs0.addObject('TransformEngine', name="translate", input_position="@../loader.position", translation="0 0 0")
       springs0.addObject('EdgeSetTopologyContainer', name="topology", position="@translate.output_position", edges="@../loader.edges")
       springs0.addObject('MechanicalObject', name="defoDOF", template="Vec3")
       springs0.addObject('EdgeSetGeometryAlgorithms', drawEdges="true")
       springs0.addObject('FixedProjectiveConstraint', indices="0")
       springs0.addObject('DiagonalMass', name="mass", totalMass="1e-2")
       springs0.addObject('UniformVelocityDampingForceField', template="Vec3", name="uniformVelocityDampingFF0", implicit="true", dampingCoefficient="0.005")

       extensions_node = springs0.addChild('extensionsNode')

       extensions_node.addObject('MechanicalObject', template="Vec1", name="extensionsDOF")
       extensions_node.addObject('DistanceMapping', name="distanceMapping", topology="@../topology", input="@../defoDOF", output="@extensionsDOF", geometricStiffness="0", applyRestPosition="true", computeDistance="true")
       extensions_node.addObject('RestShapeSpringsForceField', template="Vec1", stiffness="1000")

       springs1 = Root.addChild('springs1')

       springs1.addObject('TransformEngine', name="translate", input_position="@../loader.position", translation="1.2 0 0")
       springs1.addObject('EdgeSetTopologyContainer', name="topology", position="@translate.output_position", edges="@../loader.edges")
       springs1.addObject('MechanicalObject', name="defoDOF", template="Vec3")
       springs1.addObject('EdgeSetGeometryAlgorithms', drawEdges="true")
       springs1.addObject('FixedProjectiveConstraint', indices="19")
       springs1.addObject('DiagonalMass', name="mass", totalMass="1e-2")
       springs1.addObject('UniformVelocityDampingForceField', template="Vec3", name="uniformVelocityDampingFF0", implicit="true", dampingCoefficient="0.005")

       extensions_node = springs1.addChild('extensionsNode')

       extensions_node.addObject('MechanicalObject', template="Vec1", name="extensionsDOF")
       extensions_node.addObject('DistanceMapping', name="distanceMapping", topology="@../topology", input="@../defoDOF", output="@extensionsDOF", geometricStiffness="0", applyRestPosition="true", computeDistance="true")
       extensions_node.addObject('RestShapeSpringsForceField', template="Vec1", stiffness="1000")

       connection = Root.addChild('connection')

       connection.addObject('MechanicalObject', template="Vec1", name="connectionDOF")
       connection.addObject('EdgeSetTopologyContainer', name="edgeTopo", edges="0 1")
       connection.addObject('DistanceMultiMapping', template="Vec3,Vec1", topology="@edgeTopo", input="@../springs0 @../springs1", output="@connectionDOF", indexPairs="0 19 1 0", restLengths="1", geometricStiffness="0", applyRestPosition="true", computeDistance="true")
       connection.addObject('RestShapeSpringsForceField', template="Vec1", stiffness="1")
    ```

