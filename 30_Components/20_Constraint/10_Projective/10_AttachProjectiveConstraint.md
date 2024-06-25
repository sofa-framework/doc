---
title: AttachProjectiveConstraint
---

AttachProjectiveConstraint
================

This component belongs to the category of [Projective Constraint](https://www.sofa-framework.org/community/doc/main-principles/constraint/projective-constraint/). The AttachProjectiveConstraint works with a pair of objects, and it projects the degrees of freedom (e.g. position) and their derivatives (e.g. velocity), so that both objects are attached. As being a projective constraint, this projective constraints ensures a geometrical connection between both objects at the end of the time step, but it does not integrate the physics of both object (contrary to Lagrange based constraints).



Data 
----

The AttachProjectiveConstraint can be initialized using three input data:

- **object1**: link to the first model (MechanicalModel)
- **object2**: link to the second model (MechanicalModel)
- **indices1**: corresponding to the indices of the source points on the first model
- **indices2**: corresponding to the indices of the fixed points on the second model
- **constraintFactor**: allows for the partial application of the constraint using this factor per pair of points constrained (0=the constraint is released. 1=the constraint is fully constrained)
- **twoWay**:
  - if true, this boolean projects the constraint vertices of both _object1_ and _object2_ towards their average degrees of freedom and derivatives: 
  ```cpp
  Deriv corr = (dx2-dx1)*0.5*responseFactor*getConstraintFactor(index);
        dx1 += corr;
        dx2 -= corr;
  ```
  - if false, the position of the _object1_ are projected onto the _object2_. Therefore, _object2_ only follows _object1_ without affecting the motion of _object1_
  ```cpp
  dx2 = Deriv();
  ```



Usage
-----

The AttachProjectiveConstraint **requires** two MechanicalObjects so that both degrees of freedom can be accessed and projected to the attached configuration. An integration scheme and a solver are also necessary to solve the linear system at each time step.


Example
-------

This component is used as follows in XML format:

``` xml
<AttachProjectiveConstraint name="AttachProjectiveConstraint" object1="@M1" object2="@M2" indices1="0 1 2" indices2="10 11 12" constraintFactor="1 1 1"/>
```

or using SofaPython3:

``` python
node.addObject('AttachProjectiveConstraint', object1="@M1", object2="@M2", indices1="0 1 2", indices2="10 11 12", constraintFactor="1 1 1")
```

An example scene involving a AttachProjectiveConstraint is available in [*examples/Component/Constraint/Projective/AttachProjectiveConstraint.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/Constraint/Projective/AttachProjectiveConstraint.scn)
<!-- automatically generated doc START -->
__Target__: `Sofa.Component.Constraint.Projective`

__namespace__: `#!c++ sofa::component::constraint::projective`

__parents__: 

- `#!c++ PairInteractionProjectiveConstraintSet`

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
		<td>indices1</td>
		<td>
Indices of the source points on the first model
</td>
		<td></td>
	</tr>
	<tr>
		<td>indices2</td>
		<td>
Indices of the fixed points on the second model
</td>
		<td></td>
	</tr>
	<tr>
		<td>twoWay</td>
		<td>
if true, projects the constraint vertices of both object1 and object2 towards their average degrees of freedom and derivatives. If false, the position of the object1 are projected onto the object2. Therefore, object2 only follows object1 without affecting the motion of object1
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>freeRotations</td>
		<td>
true to keep rotations free (only used for Rigid DOFs)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>lastFreeRotation</td>
		<td>
true to keep rotation of the last attached point free (only used for Rigid DOFs)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>restRotations</td>
		<td>
true to use rest rotations local offsets (only used for Rigid DOFs)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>lastPos</td>
		<td>
position at which the attach constraint should become inactive
</td>
		<td></td>
	</tr>
	<tr>
		<td>lastDir</td>
		<td>
direction from lastPos at which the attach coustraint should become inactive
</td>
		<td></td>
	</tr>
	<tr>
		<td>clamp</td>
		<td>
true to clamp particles at lastPos instead of freeing them.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>minDistance</td>
		<td>
the constraint become inactive if the distance between the points attached is bigger than minDistance.
</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>positionFactor</td>
		<td>
IN: Factor applied to projection of position
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>velocityFactor</td>
		<td>
IN: Factor applied to projection of velocity
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>responseFactor</td>
		<td>
IN: Factor applied to projection of force/acceleration
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>constraintFactor</td>
		<td>
Vector of factors adapting the application of the constraint per pair of points (0 -&gt; the constraint is released. 1 -&gt; the constraint is fully constrained)
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
|mechanicalStates|List of mechanical states to which this component is associated|
|object1|First object associated to this component|
|object2|Second object associated to this component|



## Examples

Component/Constraint/Projective/AttachProjectiveConstraint.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [AttachProjectiveConstraint FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <DefaultAnimationLoop/>
        <Node name="Single">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <Node name="M1">
                <MechanicalObject showObject="1"/>
                <UniformMass vertexMass="1" />
                <RegularGridTopology nx="4" ny="4" nz="28" xmin="-9" xmax="-6" ymin="0" ymax="3" zmin="0" zmax="27" />
                <BoxConstraint box="-9.1 -0.1 -0.1 -5.9 3.1 0.1" />
                <!--<BoxConstraint box="-9.1 -0.1 26.9 -5.9 3.1 27.1" />-->
                <TetrahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" />
            </Node>
        </Node>
        <Node name="AttachOneWay">
            <EulerImplicitSolver name="cg_odesolver" printLog="false" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <Node name="M1">
                <MechanicalObject />
                <UniformMass vertexMass="1" />
                <RegularGridTopology nx="4" ny="4" nz="10" xmin="-4" xmax="-1" ymin="0" ymax="3" zmin="0" zmax="9" />
                <BoxConstraint box="-4.1 -0.1 -0.1 -0.9 3.1 0.1" />
                <TetrahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" />
            </Node>
            <Node name="M2">
                <EulerImplicitSolver name="cg_odesolver" printLog="false" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MechanicalObject />
                <UniformMass vertexMass="1" />
                <RegularGridTopology nx="4" ny="4" nz="10" xmin="-4" xmax="-1" ymin="0" ymax="3" zmin="9" zmax="18" />
                <TetrahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" />
            </Node>
            <Node name="M3">
                <EulerImplicitSolver name="cg_odesolver" printLog="false" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MechanicalObject />
                <UniformMass vertexMass="1" />
                <RegularGridTopology nx="4" ny="4" nz="10" xmin="-4" xmax="-1" ymin="0" ymax="3" zmin="18" zmax="27" />
                <!--<BoxConstraint box="-4.1 -0.1 26.9 -0.9 3.1 27.1" />-->
                <TetrahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" />
            </Node>
            <AttachProjectiveConstraint object1="@M1" object2="@M2" indices1="144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159" indices2="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15" constraintFactor="1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"/>
            <AttachProjectiveConstraint object1="@M2" object2="@M3" indices1="144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159" indices2="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15" constraintFactor="1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"/>
        </Node>
        <Node name="AttachTwoWay">
            <EulerImplicitSolver name="cg_odesolver" printLog="false" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <Node name="M1">
                <MechanicalObject />
                <UniformMass vertexMass="1" />
                <RegularGridTopology nx="4" ny="4" nz="10" xmin="1" xmax="4" ymin="0" ymax="3" zmin="0" zmax="9" />
                <BoxConstraint box="0.9 -0.1 -0.1 4.1 3.1 0.1" />
                <TetrahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" />
            </Node>
            <Node name="M2">
                <EulerImplicitSolver name="cg_odesolver" printLog="false" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MechanicalObject />
                <UniformMass vertexMass="1" />
                <RegularGridTopology nx="4" ny="4" nz="10" xmin="1" xmax="4" ymin="0" ymax="3" zmin="9" zmax="18" />
                <TetrahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" />
            </Node>
            <Node name="M3">
                <EulerImplicitSolver name="cg_odesolver" printLog="false" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MechanicalObject />
                <UniformMass vertexMass="1" />
                <RegularGridTopology nx="4" ny="4" nz="10" xmin="1" xmax="4" ymin="0" ymax="3" zmin="18" zmax="27" />
                <!--<BoxConstraint box="0.9 -0.1 26.9 4.1 3.1 27.1" />-->
                <TetrahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" />
            </Node>
            <AttachProjectiveConstraint object1="@M1" object2="@M2" twoWay="true" indices1="144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159" indices2="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15" constraintFactor="1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"/>
            <AttachProjectiveConstraint object1="@M2" object2="@M3" twoWay="true" indices1="144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159" indices2="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15"/>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
        root.addObject('DefaultAnimationLoop')

        Single = root.addChild('Single')
        Single.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        Single.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")

        M1 = Single.addChild('M1')
        M1.addObject('MechanicalObject', showObject="1")
        M1.addObject('UniformMass', vertexMass="1")
        M1.addObject('RegularGridTopology', nx="4", ny="4", nz="28", xmin="-9", xmax="-6", ymin="0", ymax="3", zmin="0", zmax="27")
        M1.addObject('BoxConstraint', box="-9.1 -0.1 -0.1 -5.9 3.1 0.1")
        M1.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3")

        AttachOneWay = root.addChild('AttachOneWay')
        AttachOneWay.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        AttachOneWay.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")

        M1 = AttachOneWay.addChild('M1')
        M1.addObject('MechanicalObject')
        M1.addObject('UniformMass', vertexMass="1")
        M1.addObject('RegularGridTopology', nx="4", ny="4", nz="10", xmin="-4", xmax="-1", ymin="0", ymax="3", zmin="0", zmax="9")
        M1.addObject('BoxConstraint', box="-4.1 -0.1 -0.1 -0.9 3.1 0.1")
        M1.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3")

        M2 = AttachOneWay.addChild('M2')
        M2.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        M2.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        M2.addObject('MechanicalObject')
        M2.addObject('UniformMass', vertexMass="1")
        M2.addObject('RegularGridTopology', nx="4", ny="4", nz="10", xmin="-4", xmax="-1", ymin="0", ymax="3", zmin="9", zmax="18")
        M2.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3")

        M3 = AttachOneWay.addChild('M3')
        M3.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        M3.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        M3.addObject('MechanicalObject')
        M3.addObject('UniformMass', vertexMass="1")
        M3.addObject('RegularGridTopology', nx="4", ny="4", nz="10", xmin="-4", xmax="-1", ymin="0", ymax="3", zmin="18", zmax="27")
        M3.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3")
        AttachOneWay.addObject('AttachProjectiveConstraint', object1="@M1", object2="@M2", indices1="144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159", indices2="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15", constraintFactor="1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1")
        AttachOneWay.addObject('AttachProjectiveConstraint', object1="@M2", object2="@M3", indices1="144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159", indices2="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15", constraintFactor="1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1")

        AttachTwoWay = root.addChild('AttachTwoWay')
        AttachTwoWay.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        AttachTwoWay.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")

        M1 = AttachTwoWay.addChild('M1')
        M1.addObject('MechanicalObject')
        M1.addObject('UniformMass', vertexMass="1")
        M1.addObject('RegularGridTopology', nx="4", ny="4", nz="10", xmin="1", xmax="4", ymin="0", ymax="3", zmin="0", zmax="9")
        M1.addObject('BoxConstraint', box="0.9 -0.1 -0.1 4.1 3.1 0.1")
        M1.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3")

        M2 = AttachTwoWay.addChild('M2')
        M2.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        M2.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        M2.addObject('MechanicalObject')
        M2.addObject('UniformMass', vertexMass="1")
        M2.addObject('RegularGridTopology', nx="4", ny="4", nz="10", xmin="1", xmax="4", ymin="0", ymax="3", zmin="9", zmax="18")
        M2.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3")

        M3 = AttachTwoWay.addChild('M3')
        M3.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        M3.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        M3.addObject('MechanicalObject')
        M3.addObject('UniformMass', vertexMass="1")
        M3.addObject('RegularGridTopology', nx="4", ny="4", nz="10", xmin="1", xmax="4", ymin="0", ymax="3", zmin="18", zmax="27")
        M3.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3")
        AttachTwoWay.addObject('AttachProjectiveConstraint', object1="@M1", object2="@M2", twoWay="true", indices1="144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159", indices2="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15", constraintFactor="1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1")
        AttachTwoWay.addObject('AttachProjectiveConstraint', object1="@M2", object2="@M3", twoWay="true", indices1="144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159", indices2="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15")
    ```

Component/Constraint/Projective/AttachProjectiveConstraintMatrix.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [AttachProjectiveConstraint FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [EigenSimplicialLDLT] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <DefaultAnimationLoop/>
        <Node name="AttachOneWay">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <Node name="M1">
                <MechanicalObject showObject="1"/>
                <UniformMass vertexMass="1" />
                <RegularGridTopology nx="4" ny="4" nz="10" xmin="1" xmax="4" ymin="0" ymax="3" zmin="0" zmax="9" />
                <BoxConstraint box="0.9 -0.1 -0.1 4.1 3.1 0.1" />
                <TetrahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" />
            </Node>
            <Node name="M2">
                <MechanicalObject />
                <UniformMass vertexMass="1" />
                <RegularGridTopology nx="4" ny="4" nz="10" xmin="1" xmax="4" ymin="0" ymax="3" zmin="9" zmax="18" />
                <TetrahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" />
            </Node>
            <!--
    		<Node name="M3">
    			<EulerImplicitSolver name="cg_odesolver" printLog="false"/>
    			<CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9"/>
    			<MechanicalObject/>
    			<UniformMass mass="1"/>
    			<RegularGridTopology nx="4" ny="4" nz="10" xmin="1" xmax="4" ymin="0" ymax="3" zmin="18" zmax="27"/>
    			<TetrahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3"/>
    		</Node>
    		-->
            <AttachProjectiveConstraint object1="@M1" object2="@M2" indices1="144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159" indices2="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15"/>
            <!--	<AttachProjectiveConstraint object1="@M2" object2="@M3" radius="0.1" indices1="144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159" indices2="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15" constraintFactor="1"/>	-->
        </Node>
        <Node name="AttachOneWay2">
            <EulerImplicitSolver name="cg_odesolver" printLog="false" />
            <EigenSimplicialLDLT template="CompressedRowSparseMatrixMat3x3"/>
            <Node name="M1">
                <MechanicalObject />
                <UniformMass vertexMass="1" />
                <RegularGridTopology nx="4" ny="4" nz="10" xmin="-4" xmax="-1" ymin="0" ymax="3" zmin="0" zmax="9" />
                <BoxConstraint box="-4.1 -0.9 -0.1 4.1 3.1 0.1" />
                <TetrahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" />
            </Node>
            <Node name="M2">
                <MechanicalObject />
                <UniformMass vertexMass="1" />
                <RegularGridTopology nx="4" ny="4" nz="10" xmin="-4" xmax="-1" ymin="0" ymax="3" zmin="9" zmax="18" />
                <TetrahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" />
            </Node>
            <!--
    		<Node name="M3">
    			<EulerImplicitSolver name="cg_odesolver" printLog="false"/>
    			<CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9"/>
    			<MechanicalObject/>
    			<UniformMass mass="1"/>
    			<RegularGridTopology nx="4" ny="4" nz="10" xmin="-4" xmax="-1" ymin="0" ymax="3" zmin="18" zmax="27"/>
    			<TetrahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3"/>
    		</Node>
    		-->
            <AttachProjectiveConstraint object1="@M1" object2="@M2" indices1="144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159" indices2="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15"/>
            <!--	<AttachProjectiveConstraint object1="@M2" object2="@M3" radius="0.1" indices1="144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159" indices2="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15" constraintFactor="1"/>	-->
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
        root.addObject('DefaultAnimationLoop')

        AttachOneWay = root.addChild('AttachOneWay')
        AttachOneWay.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        AttachOneWay.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")

        M1 = AttachOneWay.addChild('M1')
        M1.addObject('MechanicalObject', showObject="1")
        M1.addObject('UniformMass', vertexMass="1")
        M1.addObject('RegularGridTopology', nx="4", ny="4", nz="10", xmin="1", xmax="4", ymin="0", ymax="3", zmin="0", zmax="9")
        M1.addObject('BoxConstraint', box="0.9 -0.1 -0.1 4.1 3.1 0.1")
        M1.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3")

        M2 = AttachOneWay.addChild('M2')
        M2.addObject('MechanicalObject')
        M2.addObject('UniformMass', vertexMass="1")
        M2.addObject('RegularGridTopology', nx="4", ny="4", nz="10", xmin="1", xmax="4", ymin="0", ymax="3", zmin="9", zmax="18")
        M2.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3")
        AttachOneWay.addObject('AttachProjectiveConstraint', object1="@M1", object2="@M2", indices1="144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159", indices2="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15")

        AttachOneWay2 = root.addChild('AttachOneWay2')
        AttachOneWay2.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        AttachOneWay2.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrixMat3x3")

        M1 = AttachOneWay2.addChild('M1')
        M1.addObject('MechanicalObject')
        M1.addObject('UniformMass', vertexMass="1")
        M1.addObject('RegularGridTopology', nx="4", ny="4", nz="10", xmin="-4", xmax="-1", ymin="0", ymax="3", zmin="0", zmax="9")
        M1.addObject('BoxConstraint', box="-4.1 -0.9 -0.1 4.1 3.1 0.1")
        M1.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3")

        M2 = AttachOneWay2.addChild('M2')
        M2.addObject('MechanicalObject')
        M2.addObject('UniformMass', vertexMass="1")
        M2.addObject('RegularGridTopology', nx="4", ny="4", nz="10", xmin="-4", xmax="-1", ymin="0", ymax="3", zmin="9", zmax="18")
        M2.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3")
        AttachOneWay2.addObject('AttachProjectiveConstraint', object1="@M1", object2="@M2", indices1="144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159", indices2="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15")
    ```


<!-- automatically generated doc END -->
