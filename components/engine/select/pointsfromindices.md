---
title: PointsFromIndices
---

PointsFromIndices
================

This component belongs to the category of [Engines](https://www.sofa-framework.org/community/doc/simulation-principles/engine/). This engine returns positions from given indices.

Input Data
----------

-   **position**: positions of the mechanical object
-   **indices**: indices we want to have corresponding positions

Output Data
----------

-   **indices\_position**: positions according to given indices  

Examples
--------

An example scene involving the PointsFromIndices engine is available in [*examples/Component/Engine/Select/PointsFromIndices.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/Engine/Select/PointsFromIndices.scn)
<!-- automatically generated doc START -->
__Target__: `Sofa.Component.Engine.Select`

__namespace__: `#!c++ sofa::component::engine::select`

__parents__: 

- `#!c++ DataEngine`

__categories__: 

- Engine

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
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Position coordinates of the degrees of freedom
</td>
		<td></td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
Indices of the points
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>indices_position</td>
		<td>
Coordinates of the points contained in indices
</td>
		<td></td>
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

Component/Engine/Select/PointsFromIndices.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -9 1" dt="0.05">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI PointsFromIndices] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangularFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [TriangularBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <VisualStyle displayFlags="showForceFields" />
        <DefaultAnimationLoop/>
    
        <Node name="SquareGravity" gravity="0 -9.81 0">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshGmshLoader name="loader" filename="mesh/square3.msh" createSubelements="true"/>
            <MechanicalObject src="@loader" template="Vec3" name="mecaObj" scale3d="10 10 10" restScale="1" />
            <TriangleSetTopologyContainer src="@loader" name="Container" />
            <TriangleSetTopologyModifier name="Modifier" />
            <TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <DiagonalMass name="default5" massDensity="0.15" />
            <BoxROI template="Vec3" name="FixedROI" box="2 9.5 -0.5 8 10.5 0.5" drawBoxes="1" position="@mecaObj.rest_position" computeTriangles="0" computeTetrahedra="0" computeEdges="0" />
            <FixedProjectiveConstraint template="Vec3" name="default6" indices="@FixedROI.indices" />
            <TriangularFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.3" youngModulus="60" />
            <TriangularBendingSprings template="Vec3" name="FEM-Bend" stiffness="300" damping="1" />
    
            <PointsFromIndices name="PFI" position="@mecaObj.position" indices="10 20 30" />
    
            <Node name="Selection" >
                <MechanicalObject template="Vec3" position="@../PFI.indices_position" name="SelectedDOFs" showIndices="1" showIndicesScale="0.2"  />
            </Node>
    
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -9 1", dt="0.05")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="showForceFields")
        root.addObject('DefaultAnimationLoop')

        SquareGravity = root.addChild('SquareGravity', gravity="0 -9.81 0")
        SquareGravity.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        SquareGravity.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        SquareGravity.addObject('MeshGmshLoader', name="loader", filename="mesh/square3.msh", createSubelements="true")
        SquareGravity.addObject('MechanicalObject', src="@loader", template="Vec3", name="mecaObj", scale3d="10 10 10", restScale="1")
        SquareGravity.addObject('TriangleSetTopologyContainer', src="@loader", name="Container")
        SquareGravity.addObject('TriangleSetTopologyModifier', name="Modifier")
        SquareGravity.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        SquareGravity.addObject('DiagonalMass', name="default5", massDensity="0.15")
        SquareGravity.addObject('BoxROI', template="Vec3", name="FixedROI", box="2 9.5 -0.5 8 10.5 0.5", drawBoxes="1", position="@mecaObj.rest_position", computeTriangles="0", computeTetrahedra="0", computeEdges="0")
        SquareGravity.addObject('FixedProjectiveConstraint', template="Vec3", name="default6", indices="@FixedROI.indices")
        SquareGravity.addObject('TriangularFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.3", youngModulus="60")
        SquareGravity.addObject('TriangularBendingSprings', template="Vec3", name="FEM-Bend", stiffness="300", damping="1")
        SquareGravity.addObject('PointsFromIndices', name="PFI", position="@mecaObj.position", indices="10 20 30")

        Selection = SquareGravity.addChild('Selection')
        Selection.addObject('MechanicalObject', template="Vec3", position="@../PFI.indices_position", name="SelectedDOFs", showIndices="1", showIndicesScale="0.2")
    ```


<!-- automatically generated doc END -->
