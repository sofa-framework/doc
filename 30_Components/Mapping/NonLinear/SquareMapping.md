# SquareMapping

Compute the square


__Templates__:

- `#!c++ Vec1d,Vec1d`

__Target__: `Sofa.Component.Mapping.NonLinear`

__namespace__: `#!c++ sofa::component::mapping::nonlinear`

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
		<td>geometricStiffness</td>
		<td>
Method used to compute the geometric stiffness:
-None: geometric stiffness is not computed
-Exact: the exact geometric stiffness is computed
</td>
		<td>Exact</td>
	</tr>
	<tr>
		<td>useGeometricStiffnessMatrix</td>
		<td>
If available (cached), the geometric stiffness matrix is used in order to compute the product with the parent displacement. Otherwise, the product is computed directly using the available vectors (matrix-free method).
</td>
		<td>1</td>
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



## Examples

Component/Mapping/NonLinear/SquareMapping.scn

=== "XML"

    ```xml
    ﻿<?xml version="1.0"?>
    <Node name="Root" gravity="0 -10 0" time="0" animate="0"  dt="0.01">
    
        <Node name="plugins">
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin name="Sofa.Component.Engine.Transform"/> <!-- Needed to use components [TransformEngine] -->
            <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [StringMeshCreator] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
            <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [DistanceMapping SquareDistanceMapping SquareMapping] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [RestShapeSpringsForceField] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [EdgeSetGeometryAlgorithms EdgeSetTopologyContainer] -->
            <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        </Node>
    
        <DefaultVisualManagerLoop/>
        <VisualStyle displayFlags="showVisualModels showBehaviorModels showMappings showForceFields showMechanicalMappings" />
    
        <DefaultAnimationLoop/>
        <StringMeshCreator name="loader" resolution="3" />
    
        <Node name="twoMappings">
    
            <EulerImplicitSolver name="solverTwoMappings" rayleighStiffness="0.1" rayleighMass="0.1"/>
            <CGLinearSolver iterations="1e4" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
            <EdgeSetTopologyContainer name="topology" position="@../loader.position" edges="@../loader.edges" />
            <MechanicalObject name="defoDOF" template="Vec3" />
            <EdgeSetGeometryAlgorithms drawEdges="true" />
            <FixedProjectiveConstraint indices="0" />
            <DiagonalMass  name="mass" totalMass="1e-2"/>
            <Node name="extensionsNode" >
                <MechanicalObject template="Vec1" name="extensionsDOF" />
                <DistanceMapping name="distanceMapping" topology="@../topology" input="@../defoDOF" output="@extensionsDOF" geometricStiffness="1" applyRestPosition="true" computeDistance="true"/>
                <Node name="square">
                    <MechanicalObject template="Vec1" name="squaredDOF" />
                    <SquareMapping input="@../extensionsDOF" output="@squaredDOF" geometricStiffness="1" applyRestPosition="true"/>
                    <RestShapeSpringsForceField template="Vec1" stiffness="10000"/>
                </Node>
            </Node>
        </Node>
    
        <Node name="oneMapping">
            <TransformEngine name="transform" template="Vec3" translation="0 0 0" input_position="@../loader.position" />
    
            <EulerImplicitSolver name="solverOneMapping" rayleighStiffness="0.1" rayleighMass="0.1"/>
            <CGLinearSolver iterations="1e4" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
            <EdgeSetTopologyContainer name="topology" position="@transform.output_position" edges="@../loader.edges" />
            <MechanicalObject name="defoDOF" template="Vec3" />
            <EdgeSetGeometryAlgorithms drawEdges="true" />
            <FixedProjectiveConstraint indices="0" />
            <DiagonalMass  name="mass" totalMass="1e-2"/>
            <Node name="extensionsNode" >
                <MechanicalObject template="Vec1" name="extensionsDOF" />
                <SquareDistanceMapping name="distanceMapping" topology="@../topology" input="@../defoDOF" output="@extensionsDOF" geometricStiffness="1" applyRestPosition="true"/>
                <RestShapeSpringsForceField template="Vec1" stiffness="10000"/>
            </Node>
        </Node>
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        Root = rootNode.addChild('Root', gravity="0 -10 0", time="0", animate="0", dt="0.01")

        plugins = Root.addChild('plugins')
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Engine.Transform")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        Root.addObject('DefaultVisualManagerLoop')
        Root.addObject('VisualStyle', displayFlags="showVisualModels showBehaviorModels showMappings showForceFields showMechanicalMappings")
        Root.addObject('DefaultAnimationLoop')
        Root.addObject('StringMeshCreator', name="loader", resolution="3")

        twoMappings = Root.addChild('twoMappings')
        twoMappings.addObject('EulerImplicitSolver', name="solverTwoMappings", rayleighStiffness="0.1", rayleighMass="0.1")
        twoMappings.addObject('CGLinearSolver', iterations="1e4", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        twoMappings.addObject('EdgeSetTopologyContainer', name="topology", position="@../loader.position", edges="@../loader.edges")
        twoMappings.addObject('MechanicalObject', name="defoDOF", template="Vec3")
        twoMappings.addObject('EdgeSetGeometryAlgorithms', drawEdges="true")
        twoMappings.addObject('FixedProjectiveConstraint', indices="0")
        twoMappings.addObject('DiagonalMass', name="mass", totalMass="1e-2")

        extensionsNode = twoMappings.addChild('extensionsNode')
        extensionsNode.addObject('MechanicalObject', template="Vec1", name="extensionsDOF")
        extensionsNode.addObject('DistanceMapping', name="distanceMapping", topology="@../topology", input="@../defoDOF", output="@extensionsDOF", geometricStiffness="1", applyRestPosition="true", computeDistance="true")

        square = extensionsNode.addChild('square')
        square.addObject('MechanicalObject', template="Vec1", name="squaredDOF")
        square.addObject('SquareMapping', input="@../extensionsDOF", output="@squaredDOF", geometricStiffness="1", applyRestPosition="true")
        square.addObject('RestShapeSpringsForceField', template="Vec1", stiffness="10000")

        oneMapping = Root.addChild('oneMapping')
        oneMapping.addObject('TransformEngine', name="transform", template="Vec3", translation="0 0 0", input_position="@../loader.position")
        oneMapping.addObject('EulerImplicitSolver', name="solverOneMapping", rayleighStiffness="0.1", rayleighMass="0.1")
        oneMapping.addObject('CGLinearSolver', iterations="1e4", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        oneMapping.addObject('EdgeSetTopologyContainer', name="topology", position="@transform.output_position", edges="@../loader.edges")
        oneMapping.addObject('MechanicalObject', name="defoDOF", template="Vec3")
        oneMapping.addObject('EdgeSetGeometryAlgorithms', drawEdges="true")
        oneMapping.addObject('FixedProjectiveConstraint', indices="0")
        oneMapping.addObject('DiagonalMass', name="mass", totalMass="1e-2")

        extensionsNode = oneMapping.addChild('extensionsNode')
        extensionsNode.addObject('MechanicalObject', template="Vec1", name="extensionsDOF")
        extensionsNode.addObject('SquareDistanceMapping', name="distanceMapping", topology="@../topology", input="@../defoDOF", output="@extensionsDOF", geometricStiffness="1", applyRestPosition="true")
        extensionsNode.addObject('RestShapeSpringsForceField', template="Vec1", stiffness="10000")
    ```

