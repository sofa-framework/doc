# SquareMapping

This component is classified under the category of [Mappings](../../../../simulation-principles/multi-model-representation/mapping/).

In this particular mapping, we designate the input as the parent state and the output as the child state.

## Mapping Function

The transformation function employed in this mapping is the square function.
Formally, if $f$ denotes the mapping function, then for any input $x$, the output $f(x)$ is $x^2$.

Mathematically, this can be expressed as:

$$
f(x)=x^2
$$

for all $x$ in the domain.

## Jacobian Matrix

The Jacobian matrix of this mapping, which represents the first-order partial derivatives of the output with respect to the input, is not constant, and depends on the input.

The elements of the Jacobian matrix are given by:
$$
J_{ij} = \frac{\partial f_i}{\partial x_j} = \delta_{ij} 2  x_j
$$

This can be written in matrix form as:

$$
J(x) = 2\: \text{diag} (x)
$$

Here, $\text{diag}(x)$ denotes a diagonal matrix with the elements of $x$ on the diagonal.

Since the Jacobian matrix is diagonal, its transpose is equal to itself:

$$
J(x)^T = J(x)
$$

## Hessian Tensor

The Hessian tensor represents the second-order partial derivatives of the output with respect to the input. For the `SquareMapping` component, the Hessian tensor is non-zero because the Jacobian matrix depends on the input $x$.

The elements of the Hessian tensor are given by:

$$
H_{ijk} = \frac{\partial J_{ij}(x)}{\partial x_k} = \frac{\partial (\delta_{ij} 2  x_j)}{\partial x_k} = 2 \delta_{ij} \frac{\partial x_j}{\partial x_k} = 2 \delta_{ij} \delta_{jk}
$$

Then, for any vector $v$

$$
(H \cdot v)_{ij} = \sum_k H_{ijk} v_k = 2 \delta_{ij} \sum_k \delta_{jk} v_k = 2 \delta_{ij} v_j
$$

In matrix notation, this can be written as:

$$
H \cdot v = 2 \: \text{diag}(v)
$$

## Implementation Details

Given the nature of the mapping function, the mapping is defined only if the input and output are scalar DoFs.
It means, the only available template for this mapping is `Vec1`.

<!-- automatically generated doc START -->
<!-- generate_doc -->

Compute the square value from the inputs.


## Vec1d,Vec1d

Templates:

- Vec1d,Vec1d

__Target__: Sofa.Component.Mapping.NonLinear

__namespace__: sofa::component::mapping::nonlinear

__parents__:

- BaseNonLinearMapping

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
		</td>
		<td>Exact</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|input|Input object to map|State&lt;Vec1d&gt;|
|output|Output object to map|State&lt;Vec1d&gt;|

## Examples 

SquareMapping.scn

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
    def createScene(root_node):

       root = root_node.addChild('Root', gravity="0 -10 0", time="0", animate="0", dt="0.01")

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

       root.addObject('DefaultVisualManagerLoop', )
       root.addObject('VisualStyle', displayFlags="showVisualModels showBehaviorModels showMappings showForceFields showMechanicalMappings")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('StringMeshCreator', name="loader", resolution="3")

       two_mappings = Root.addChild('twoMappings')

       two_mappings.addObject('EulerImplicitSolver', name="solverTwoMappings", rayleighStiffness="0.1", rayleighMass="0.1")
       two_mappings.addObject('CGLinearSolver', iterations="1e4", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       two_mappings.addObject('EdgeSetTopologyContainer', name="topology", position="@../loader.position", edges="@../loader.edges")
       two_mappings.addObject('MechanicalObject', name="defoDOF", template="Vec3")
       two_mappings.addObject('EdgeSetGeometryAlgorithms', drawEdges="true")
       two_mappings.addObject('FixedProjectiveConstraint', indices="0")
       two_mappings.addObject('DiagonalMass', name="mass", totalMass="1e-2")

       extensions_node = twoMappings.addChild('extensionsNode')

       extensions_node.addObject('MechanicalObject', template="Vec1", name="extensionsDOF")
       extensions_node.addObject('DistanceMapping', name="distanceMapping", topology="@../topology", input="@../defoDOF", output="@extensionsDOF", geometricStiffness="1", applyRestPosition="true", computeDistance="true")

       square = extensionsNode.addChild('square')

       square.addObject('MechanicalObject', template="Vec1", name="squaredDOF")
       square.addObject('SquareMapping', input="@../extensionsDOF", output="@squaredDOF", geometricStiffness="1", applyRestPosition="true")
       square.addObject('RestShapeSpringsForceField', template="Vec1", stiffness="10000")

       one_mapping = Root.addChild('oneMapping')

       one_mapping.addObject('TransformEngine', name="transform", template="Vec3", translation="0 0 0", input_position="@../loader.position")
       one_mapping.addObject('EulerImplicitSolver', name="solverOneMapping", rayleighStiffness="0.1", rayleighMass="0.1")
       one_mapping.addObject('CGLinearSolver', iterations="1e4", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       one_mapping.addObject('EdgeSetTopologyContainer', name="topology", position="@transform.output_position", edges="@../loader.edges")
       one_mapping.addObject('MechanicalObject', name="defoDOF", template="Vec3")
       one_mapping.addObject('EdgeSetGeometryAlgorithms', drawEdges="true")
       one_mapping.addObject('FixedProjectiveConstraint', indices="0")
       one_mapping.addObject('DiagonalMass', name="mass", totalMass="1e-2")

       extensions_node = oneMapping.addChild('extensionsNode')

       extensions_node.addObject('MechanicalObject', template="Vec1", name="extensionsDOF")
       extensions_node.addObject('SquareDistanceMapping', name="distanceMapping", topology="@../topology", input="@../defoDOF", output="@extensionsDOF", geometricStiffness="1", applyRestPosition="true")
       extensions_node.addObject('RestShapeSpringsForceField', template="Vec1", stiffness="10000")
    ```


<!-- automatically generated doc END -->
