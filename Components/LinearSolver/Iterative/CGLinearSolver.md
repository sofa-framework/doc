---
title: CGLinearSolver
---

CGLinearSolver  
==============

This component belongs to the category of [LinearSolver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/linear-solvers/). The role of the CGLinearSolver is to solve the linear system <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="Linear system" /> without any _a priori_ on this system.

In SOFA, the CGLinearSolver follows the well-known [conjugate gradient method](https://en.wikipedia.org/wiki/Conjugate_gradient_method), which consists in iteratively solving <img class="latex" src="https://latex.codecogs.com/png.latex?r=b-\mathbf{A}x^k" title="Computation of residual" /> where *r* is known as the residual. This residual will be used to compute mutually conjugate vectors *p* (see the sequence diagram below) which will be used as a basis to find a new approximated solution <img class="latex" src="https://latex.codecogs.com/png.latex?x^{k+1}" title="New approximated solution" />.

**Note**: the CGLinearSolver in SOFA assumes that the right hand side (RHS) vector *b* is already computed. The computation of *b* is usually called in the [integration scheme](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/integration-schemes/) through the function `computeForce()`.



Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/CGLinearSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/CGLinearSolver.png?raw=true" title="Flow diagram for the CGLinearSolver"/></a>



Data  
----

This LinearSolver is ruled by several breaking conditions:  

- **iterations**: specified the maximum number of iterations after which the iterative descent of the CGLinearSolver must stop
- **tolerance**: defines the desired accuracy of the Conjugate Gradient solution (ratio of current residual norm over initial residual norm)"
- **threshold**: defines the minimum value of the denominator in the conjugate Gradient solution
- **warmStart**: this option allows to use the previous solution as initial solution, which improves the initial guess if your system is evolving smoothly


Usage
-----

The CGLinearSolver **requires** the use (above in the scene graph) of an integration scheme, and (below in the scene graph) of a MechanicalObject storing the state information that the CGLinearSolver will access.

When using a CGLinearSolver, make sure you carefully chose the value of the free data field iterations, tolerance and threshold. Both tolerance and threshold data must be chosen in accordance with the dimension of the degrees of freedom (DOFs). Usually, the value of these two data is close to the square of the expected error on the DOFs.

Remember that when using an iterative linear solver like the CGLinearSolver, no exact solution can be found. The accuracy of your solution will always depend on the conditioning of your system and your input data (iterations, tolerance and threshold).



Example
-------

This component is used as follows in XML format:

``` xml
<CGLinearSolver iterations="100" tolerance="1e-5" threshold="1e-5"/>
```

or using SofaPython3:

``` python
node.addObject('CGLinearSolver', iterations='100', tolerance='1e-5', threshold='1e-5')
```

A lot of scene examples are available in SOFA involving a CGLinearSolver. One is available in [*examples/Demos/liver.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Demos/liver.scn)
<!-- automatically generated doc START -->
__Target__: `Sofa.Component.LinearSolver.Iterative`

__namespace__: `#!c++ sofa::component::linearsolver::iterative`

__parents__: 

- `#!c++ MatrixLinearSolver`

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
		<td>parallelInverseProduct</td>
		<td>
Parallelize the computation of the product J*M^{-1}*J^T where M is the matrix of the linear system and J is any matrix with compatible dimensions
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>iterations</td>
		<td>
Maximum number of iterations after which the iterative descent of the Conjugate Gradient must stop
</td>
		<td>25</td>
	</tr>
	<tr>
		<td>tolerance</td>
		<td>
Desired accuracy of the Conjugate Gradient solution evaluating: |r|²/|b|² (ratio of current residual norm over initial residual norm)
</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>threshold</td>
		<td>
Minimum value of the denominator (pT A p)^ in the conjugate Gradient solution
</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>warmStart</td>
		<td>
Use previous solution as initial solution, which may improve the initial guess if your system is evolving smoothly
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>graph</td>
		<td>
Graph of residuals at each iteration
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
|linearSystem|The linear system to solve|



## Examples

Component/LinearSolver/Iterative/CGLinearSolver.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.02" gravity="0 -10 0">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <DefaultAnimationLoop/>
        
        <Node>
            <EulerImplicitSolver name="eulerimplicit_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="100" tolerance="1e-20" threshold="1e-20" warmStart="1" />
            <MechanicalObject />
            <UniformMass vertexMass="1" />
            <RegularGridTopology nx="4" ny="4" nz="4" xmin="-9" xmax="-6" ymin="0" ymax="3" zmin="0" zmax="3" />
            <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15" />
            <HexahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" method="large" />
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02", gravity="0 -10 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
        root.addObject('DefaultAnimationLoop')

        root = root.addChild('root')
        root.addObject('EulerImplicitSolver', name="eulerimplicit_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        root.addObject('CGLinearSolver', iterations="100", tolerance="1e-20", threshold="1e-20", warmStart="1")
        root.addObject('MechanicalObject')
        root.addObject('UniformMass', vertexMass="1")
        root.addObject('RegularGridTopology', nx="4", ny="4", nz="4", xmin="-9", xmax="-6", ymin="0", ymax="3", zmin="0", zmax="3")
        root.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15")
        root.addObject('HexahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3", method="large")
    ```


<!-- automatically generated doc END -->
