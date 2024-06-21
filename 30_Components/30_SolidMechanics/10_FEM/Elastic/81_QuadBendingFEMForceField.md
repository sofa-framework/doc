---
title: QuadBendingFEMForceField
---

QuadBendingFEMForceField
========================

This component belongs to the category of [ForceField](https://www.sofa-framework.org/community/doc/simulation-principles/multi-model-representation/forcefield/). The page is still incomplete, but give us a bit of time to work on it!

Description of the component ...

What it is made for, what it does



Sequence diagram
----------------


Data  
----



Usage
-----

How to use it, what **required** component, case

In which case it works, in which case it doesn't

Limitations

Example
-------

This component is used as follows in XML format:

``` xml
<QuadBendingFEMForceField data_field="X" />
```
or using SofaPython3:

``` python
node.addObject('QuadBendingFEMForceField', data_field='X')
```

With a description of each data

An example scene involving a QuadBendingFEMForceField is available in [*examples/Component/SolidMechanics/FEM/QuadBendingFEMForceField.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/SolidMechanics/FEM/QuadBendingFEMForceField.scn)
<!-- automatically generated doc START -->
__Target__: `Sofa.Component.SolidMechanics.FEM.Elastic`

__namespace__: `#!c++ sofa::component::solidmechanics::fem::elastic`

__parents__: 

- `#!c++ ForceField`

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
		<td>isCompliance</td>
		<td>
Consider the component as a compliance, else as a stiffness
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping - stiffness matrix coefficient
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>quadInfo</td>
		<td>
Internal quad data
</td>
		<td></td>
	</tr>
	<tr>
		<td>vertexInfo</td>
		<td>
Internal point data
</td>
		<td></td>
	</tr>
	<tr>
		<td>edgeInfo</td>
		<td>
Internal edge data
</td>
		<td></td>
	</tr>
	<tr>
		<td>method</td>
		<td>
large: large displacements, small: small displacements
</td>
		<td>small</td>
	</tr>
	<tr>
		<td>poissonRatio</td>
		<td>
Poisson ratio in Hooke's law (vector)
</td>
		<td>0.45</td>
	</tr>
	<tr>
		<td>youngModulus</td>
		<td>
Young modulus in Hooke's law (vector)
</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>thickness</td>
		<td>
Thickness of the elements
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
|mechanicalStates|List of mechanical states to which this component is associated|
|mstate|MechanicalState used by this component|
|topology|link to the topology container|



## Examples

Component/SolidMechanics/FEM/QuadBendingFEMForceField.scn

=== "XML"

    ```xml
    <!-- Mechanical QuadbendingFEMForceField Example -->
    <Node name="root" gravity="-1 0 0" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshVTKLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [QuadBendingFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [QuadSetGeometryAlgorithms QuadSetTopologyContainer QuadSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showVisual showForceFields showBehaviorModels" />
        <CollisionPipeline name="CollisionPipeline" verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="collision response" response="PenalityContactForceField" />
        <MinProximityIntersection name="proximity" alarmDistance="0.5" contactDistance="0.33"/>
    
        <Node name="skin" gravity="0 0 -9.81">
            <EulerImplicitSolver name="cg_odesolver" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshVTKLoader filename="mesh/test_quad.vtk" name="loader" />
            <MechanicalObject template="Vec3" src="@loader" name="DOFs" />
            <QuadSetTopologyContainer src="@loader" name="topology" />
            <QuadSetTopologyModifier name="Modifier" />
            <QuadSetGeometryAlgorithms name="GeomAlgo" template="Vec3" />
            <DiagonalMass massDensity="0.5" name="mass" />
    
            <QuadBendingFEMForceField name="FEM" youngModulus="2000" poissonRatio="0.49" thickness="0.5" method="small" />
    
            <FixedProjectiveConstraint indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58" />
    
            <Node name="Visual">
                <OglModel name="Visual" color="yellow" />
                <IdentityMapping template="Vec3,Vec3" name="visualMapping" input="@../DOFs" output="@Visual" />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="-1 0 0", dt="0.02")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')
        root.addObject('VisualStyle', displayFlags="showVisual showForceFields showBehaviorModels")
        root.addObject('CollisionPipeline', name="CollisionPipeline", verbose="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', name="collision response", response="PenalityContactForceField")
        root.addObject('MinProximityIntersection', name="proximity", alarmDistance="0.5", contactDistance="0.33")

        skin = root.addChild('skin', gravity="0 0 -9.81")
        skin.addObject('EulerImplicitSolver', name="cg_odesolver")
        skin.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        skin.addObject('MeshVTKLoader', filename="mesh/test_quad.vtk", name="loader")
        skin.addObject('MechanicalObject', template="Vec3", src="@loader", name="DOFs")
        skin.addObject('QuadSetTopologyContainer', src="@loader", name="topology")
        skin.addObject('QuadSetTopologyModifier', name="Modifier")
        skin.addObject('QuadSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
        skin.addObject('DiagonalMass', massDensity="0.5", name="mass")
        skin.addObject('QuadBendingFEMForceField', name="FEM", youngModulus="2000", poissonRatio="0.49", thickness="0.5", method="small")
        skin.addObject('FixedProjectiveConstraint', indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58")

        Visual = skin.addChild('Visual')
        Visual.addObject('OglModel', name="Visual", color="yellow")
        Visual.addObject('IdentityMapping', template="Vec3,Vec3", name="visualMapping", input="@../DOFs", output="@Visual")
    ```


<!-- automatically generated doc END -->
