# PolynomialRestShapeSpringsForceField

Simple elastic springs applied to given degrees of freedom between their current and rest shape position


__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.Component.SolidMechanics.Spring`

__namespace__: `#!c++ sofa::component::solidmechanics::spring`

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
		<td>points</td>
		<td>
points controlled by the rest shape springs
</td>
		<td></td>
	</tr>
	<tr>
		<td>external_points</td>
		<td>
points from the external Mechancial State that define the rest shape springs
</td>
		<td></td>
	</tr>
	<tr>
		<td>polynomialStiffness</td>
		<td>
coefficients for all spring polynomials
</td>
		<td></td>
	</tr>
	<tr>
		<td>polynomialDegree</td>
		<td>
vector of values that show polynomials degrees
</td>
		<td></td>
	</tr>
	<tr>
		<td>recompute_indices</td>
		<td>
Recompute indices (should be false for BBOX)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>springColor</td>
		<td>
spring color
</td>
		<td>0 1 0 1</td>
	</tr>
	<tr>
		<td>initialLength</td>
		<td>
initial virtual length of the spring
</td>
		<td></td>
	</tr>
	<tr>
		<td>smoothShift</td>
		<td>
denominator correction adding shift value
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>smoothScale</td>
		<td>
denominator correction adding scale
</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawSpring</td>
		<td>
draw Spring
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showIndicesScale</td>
		<td>
Scale for indices display. (default=0.02)
</td>
		<td>0.02</td>
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
|external_rest_shape|rest_shape can be defined by the position of an external Mechanical State|



## Examples

Component/SolidMechanics/Spring/PolynomialRestShapeSpringsForceField.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.01" gravity="0 0 0">
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [PolynomialRestShapeSpringsForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <VisualStyle displayFlags="showForceFields"/>
        <DefaultAnimationLoop/>
    
        <Node name="Particle" bbox="-10 -10 -10 20 20 20" >
            <EulerImplicitSolver />
            <CGLinearSolver iterations="200" tolerance="1e-09" threshold="1e-09"/>
            <MechanicalObject template="Vec3" name="myParticle" rest_position="0 0 0" position="1.1 0 0" showObject="1" showObjectScale="10" />
            <UniformMass totalMass="1" />
            <PolynomialRestShapeSpringsForceField polynomialStiffness="10 10" polynomialDegree="2" points='0' smoothShift="0.0001" smoothScale='10000000' drawSpring='1' />
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01", gravity="0 0 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="showForceFields")
        root.addObject('DefaultAnimationLoop')

        Particle = root.addChild('Particle', bbox="-10 -10 -10 20 20 20")
        Particle.addObject('EulerImplicitSolver')
        Particle.addObject('CGLinearSolver', iterations="200", tolerance="1e-09", threshold="1e-09")
        Particle.addObject('MechanicalObject', template="Vec3", name="myParticle", rest_position="0 0 0", position="1.1 0 0", showObject="1", showObjectScale="10")
        Particle.addObject('UniformMass', totalMass="1")
        Particle.addObject('PolynomialRestShapeSpringsForceField', polynomialStiffness="10 10", polynomialDegree="2", points="0", smoothShift="0.0001", smoothScale="10000000", drawSpring="1")
    ```

