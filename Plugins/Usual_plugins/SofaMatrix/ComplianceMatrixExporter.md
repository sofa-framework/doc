# ComplianceMatrixExporter

Export the compliance matrix from a constraint solver.


__Target__: `SofaMatrix`

__namespace__: `#!c++ sofa::component::constraintset`

__parents__: 

- `#!c++ BaseSimulationExporter`

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
Path or filename where to export the data.  If missing the name of the component is used.
</td>
		<td></td>
	</tr>
	<tr>
		<td>exportEveryNumberOfSteps</td>
		<td>
export file only at specified number of steps (0=disable, default=0)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>exportAtBegin</td>
		<td>
export file before the simulation starts, once the simulation is initialized (default=false)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>exportAtEnd</td>
		<td>
export file when the simulation is over and cleanup is called, i.e. just before deleting the simulation (default=false)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>enable</td>
		<td>
Enable or disable the component. (default=true)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>format</td>
		<td>
File format
</td>
		<td>txt</td>
	</tr>
	<tr>
		<td>precision</td>
		<td>
Number of digits used to write an entry of the matrix, default is 6
</td>
		<td>6</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|constraintSolver|Constraint solver used to export its compliance matrix|



## Examples

SofaMatrix/share/sofa/examples/SofaMatrix/ComplianceMatrixExporter.scn

=== "XML"

    ```xml
    <Node   name="Root" gravity="0 -10 0" time="0" animate="0"  dt="0.01" >
        <RequiredPlugin name="Sofa.Component.AnimationLoop"/> <!-- Needed to use components [FreeMotionAnimationLoop] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [GenericConstraintCorrection] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Model"/> <!-- Needed to use components [UniformLagrangianConstraint] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Solver"/> <!-- Needed to use components [GenericConstraintSolver] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Transform"/> <!-- Needed to use components [TransformEngine] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [StringMeshCreator] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [EigenSimplicialLLT] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [DistanceMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [EdgeSetGeometryAlgorithms EdgeSetTopologyContainer] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="SofaMatrix"/> <!-- Needed to use components [ComplianceMatrixExporter] -->
    
        <VisualStyle displayFlags="hideVisualModels showBehaviorModels showMappings showForceFields" />
        <FreeMotionAnimationLoop solveVelocityConstraintFirst="true" />
        <GenericConstraintSolver tolerance="1e-9" maxIterations="1000"/>
        <ComplianceMatrixExporter exportEveryNumberOfSteps="1" filename="compliance" printLog="true" format="csv" precision="12"/>
    
        <StringMeshCreator name="loader" resolution="20" scale3d="1 1 1" />
    
        <TransformEngine name="translate" input_position="@loader.position" translation="0 0 0" />
        <EulerImplicitSolver />
        <EigenSimplicialLLT />
        <GenericConstraintCorrection />
    
        <EdgeSetTopologyContainer position="@translate.output_position" edges="@loader.edges" />
        <MechanicalObject name="defoDOF" template="Vec3d" showObject="1" />
        <EdgeSetGeometryAlgorithms drawEdges="true" />
        <FixedProjectiveConstraint indices="0" />
        <DiagonalMass  name="mass" totalMass="1e-3"/>
        <Node name="extensionsNode" >
            <MechanicalObject template="Vec1d"  name="extensionsDOF" />
            <DistanceMapping  name="distanceMapping" />
            <UniformLagrangianConstraint template="Vec1d" iterative="false" />
        </Node>
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        Root = rootNode.addChild('Root', gravity="0 -10 0", time="0", animate="0", dt="0.01")
        Root.addObject('RequiredPlugin', name="Sofa.Component.AnimationLoop")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Model")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Solver")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Transform")
        Root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        Root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        Root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        Root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        Root.addObject('RequiredPlugin', name="SofaMatrix")
        Root.addObject('VisualStyle', displayFlags="hideVisualModels showBehaviorModels showMappings showForceFields")
        Root.addObject('FreeMotionAnimationLoop', solveVelocityConstraintFirst="true")
        Root.addObject('GenericConstraintSolver', tolerance="1e-9", maxIterations="1000")
        Root.addObject('ComplianceMatrixExporter', exportEveryNumberOfSteps="1", filename="compliance", printLog="true", format="csv", precision="12")
        Root.addObject('StringMeshCreator', name="loader", resolution="20", scale3d="1 1 1")
        Root.addObject('TransformEngine', name="translate", input_position="@loader.position", translation="0 0 0")
        Root.addObject('EulerImplicitSolver')
        Root.addObject('EigenSimplicialLLT')
        Root.addObject('GenericConstraintCorrection')
        Root.addObject('EdgeSetTopologyContainer', position="@translate.output_position", edges="@loader.edges")
        Root.addObject('MechanicalObject', name="defoDOF", template="Vec3d", showObject="1")
        Root.addObject('EdgeSetGeometryAlgorithms', drawEdges="true")
        Root.addObject('FixedProjectiveConstraint', indices="0")
        Root.addObject('DiagonalMass', name="mass", totalMass="1e-3")

        extensionsNode = Root.addChild('extensionsNode')
        extensionsNode.addObject('MechanicalObject', template="Vec1d", name="extensionsDOF")
        extensionsNode.addObject('DistanceMapping', name="distanceMapping")
        extensionsNode.addObject('UniformLagrangianConstraint', template="Vec1d", iterative="false")
    ```

