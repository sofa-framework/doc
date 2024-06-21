---
title: PolynomialSpringsForceField
---

PolynomialSpringsForceField
===========================

This component belongs to the category of [ForceField](https://www.sofa-framework.org/community/doc/simulation-principles/multi-model-representation/forcefield/). This component allows to simulate springs with Polynomial stress strain behavior. If we note:

- <img class="latex" src="https://latex.codecogs.com/png.latex?F" title="Spring force" /> the spring force
- <img class="latex" src="https://latex.codecogs.com/png.latex?S" title="Cross section" /> the cross section (always 1.0)
- <img class="latex" src="https://latex.codecogs.com/png.latex?\sigma" title="Stress-strain non-linear function" /> the stress-strain non-linear function
- <img class="latex" src="https://latex.codecogs.com/png.latex?l_0" title="Original length of the spring" /> the original length and <img class="latex" src="https://latex.codecogs.com/png.latex?l" title="Current length of the spring" /> the current length of the spring
- <img class="latex" src="https://latex.codecogs.com/png.latex?\Delta%20u%20%3D%20\left\{\begin{matrix}%20\Delta%20x\\%20\Delta%20y\\%20\Delta%20z\\%20\end{matrix}\right." title="Point displacement" /> the point displacement

the generic non-linear force can thus be written:
<img class="latex" src="https://latex.codecogs.com/png.latex?F=S%7E\sigma%20\left(%20\frac{l-l_0}{l_0}%20\right%29%20\frac{\Delta%20u}{l}" title="Generic non-linear spring force" /> 
where <img class="latex" src="https://latex.codecogs.com/png.latex?\sigma" title="Stress-strain non-linear function" /> is polynom as follows:
<img class="latex" src="https://latex.codecogs.com/png.latex?\sigma%20\left(%20\frac{l-l_0}{l_0}%20\right)%20=\sigma(L)=a_1L+a_2L^2+\cdots+a_nL^n" title="Stress-strain non-linear function" />
and
<img class="latex" src="https://latex.codecogs.com/png.latex?\frac{\partial%20\sigma}{\partial%20L}=a_1+a_2L+\cdots+a_nL^{n-1}" title="Derivative of the stress-strain non-linear function" />

The dedication of jacobian matrix for PolynomialSpringForceField is given below:

<img class="latex" src="https://latex.codecogs.com/png.latex?J_F(u)=\left(S\frac{\partial&space;\sigma}{\partial&space;L}\cdot\frac{1}{l_0}-S\sigma\cdot\frac{1}{|l|}&space;\right)\begin{bmatrix}\frac{\Delta&space;x^2}{l^2}&\frac{\Delta&space;x\Delta&space;y}{l^2}&\frac{\Delta&space;x\Delta&space;z}{l^2}\\\frac{\Delta&space;y\Delta&space;x}{l^2}&\frac{\Delta&space;y^2}{l^2}&\frac{\Delta&space;y\Delta&space;z}{l^2}\\\frac{\Delta&space;z\Delta&space;x}{l^2}&\frac{\Delta&space;z\Delta&space;y}{l^2}&&space;\frac{\Delta&space;z^2}{l^2}\end{bmatrix}&plus;S\sigma\cdot\frac{1}{|l|}\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}" title="Jacobian of the spring" />


Note that a **RestShape**PolynomialSpringsForceField does exist. It will compute the same non-linear force with regards to the rest shape of one single object. To avoid Nan problems when a spring has a zero length, an exponential addition to the denominator has been added. As a result, the stress simulation is shifted compared with polynomial values, but it keeps its nonlinearity:

<img class="latex" src="https://latex.codecogs.com/png.latex?J_F(u)=\left(S\frac{\partial&space;\sigma}{\partial&space;L}\cdot\frac{(1-sc\cdot&space;e^{sh-sc(\Delta&space;x^2&plus;\Delta&space;y^2&plus;\Delta&space;z^2)})}{l_0}-S\sigma\cdot\frac{(1-sc\cdot&space;e^{sh-sc(\Delta&space;x^2&plus;\Delta&space;y^2&plus;\Delta&space;z^2)})}{\sqrt{\Delta&space;x^2&plus;\Delta&space;y^2&plus;\Delta&space;z^2&plus;e^{sh-sc(\Delta&space;x^2&plus;\Delta&space;y^2&plus;\Delta&space;z^2)}}}&space;\right)\cdot\frac{1}{\sqrt{\Delta&space;x^2&plus;\Delta&space;y^2&plus;\Delta&space;z^2&plus;e^{sh-sc(\Delta&space;x^2&plus;\Delta&space;y^2&plus;\Delta&space;z^2)}}}\cdot\begin{bmatrix}\Delta&space;x^2&\Delta&space;x\Delta&space;y&\Delta&space;x\Delta&space;z\\\Delta&space;y\Delta&space;x&\Delta&space;y^2&\Delta&space;y\Delta&space;z\\\Delta&space;z\Delta&space;x&\Delta&space;z\Delta&space;y&\Delta&space;z^2\end{bmatrix}&plus;S\sigma\cdot\frac{1}{\sqrt{\Delta&space;x^2&plus;\Delta&space;y^2&plus;\Delta&space;z^2&plus;e^{sh-sc(\Delta&space;x^2&plus;\Delta&space;y^2&plus;\Delta&space;z^2)}}}\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}" title="Modified Jacobian of the RestShapePolynomialSpringsForceField" />


More details were given in the pull-request [#1342](https://github.com/sofa-framework/sofa/pull/1342).


Data  
----

The polynomial parameters are set as two arrays:

- **polynomialDegree**: describing the set of polynomial degrees for every spring
- **polynomialStiffness**: describing the set of polynomial coefficients sequentially combined in one vector.

The coefficients are put from smaller degree to bigger one, and the free coefficient is always zero (since for no strain we have no stress).
For examples the coefficients for polynomials [3,2,4] will be put as [a1,a2,a3,b1,b2,c1,c2,c3,c4].

- **firstObjectPoints** corresponding to the indices of the points related to the first object
- **secondObjectPoints** corresponding to the indices of the points related to the second object
- **compressible**: indicating if object compresses without reaction force


Usage
-----

The PolynomialSpringsForceField **requires** two different objects to link, which means two MechanicalObjects on which the non-linear spring will act.
On the other hand, RestShapePolynomialSpringsForceField will act on one single body, i.e. one MechanicalObject.

Example
-------

This component is used as follows in XML format:

``` xml
<DiagonalMass massDensity="1000" />
```

or using Python:

``` python
node.createObject('DiagonalMass', massDensity='1000')
```

An example scene involving a PolynomialSpringsForceField is available in [*examples/Component/SolidMechanics/Spring/PolynomialSpringsForceField.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/SolidMechanics/Spring/PolynomialSpringsForceField.scn)
<!-- automatically generated doc START -->
__Target__: `Sofa.Component.SolidMechanics.Spring`

__namespace__: `#!c++ sofa::component::solidmechanics::spring`

__parents__: 

- `#!c++ PairInteractionForceField`

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
		<td>firstObjectPoints</td>
		<td>
points related to the first object
</td>
		<td></td>
	</tr>
	<tr>
		<td>secondObjectPoints</td>
		<td>
points related to the second object
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
		<td>computeZeroLength</td>
		<td>
flag to compute initial length for springs
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>zeroLength</td>
		<td>
initial length for springs
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
		<td>compressible</td>
		<td>
Indicates if object compresses without any reaction force
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
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawMode</td>
		<td>
The way springs will be drawn:
- 0: Line
- 1:Cylinder
- 2: Arrow
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showArrowSize</td>
		<td>
size of the axis
</td>
		<td>0.01</td>
	</tr>
	<tr>
		<td>showIndicesScale</td>
		<td>
Scale for indices display (default=0.02)
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
|object1|First object associated to this component|
|object2|Second object associated to this component|



## Examples

Component/SolidMechanics/Spring/PolynomialSpringsForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="lroot" gravity="0 0 0" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedralCorotationalFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [PolynomialSpringsForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <VisualStyle displayFlags="showInteractionForceFields"/>
        <DefaultAnimationLoop/>
        <MeshOBJLoader name="LiverSurface" filename="mesh/liver-smooth.obj" />
    
        <Node name="Liver" >
            <EulerImplicitSolver name="cg_odesolver"   rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver name="linear solver" iterations="25" tolerance="1e-09" threshold="1e-09" />
            <MeshGmshLoader name="meshLoader" filename="mesh/liver.msh" />
            <TetrahedronSetTopologyContainer name="topo" src="@meshLoader" />
            <MechanicalObject name="dofs" src="@meshLoader" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <DiagonalMass  name="computed using mass density" massDensity="1" />
            <TetrahedralCorotationalFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.3" youngModulus="3000" computeGlobalMatrix="0" />
            <FixedProjectiveConstraint  name="FixedProjectiveConstraint" indices="3 39 64" />
            <Node name="Visu" tags="Visual" gravity="0 -9.81 0">
                <OglModel  name="VisualModel" src="@../../LiverSurface" />
                <BarycentricMapping name="visual mapping" input="@../dofs" output="@VisualModel" />
            </Node>
    
            <Node name="Weight" >
                <MechanicalObject template="Vec3" name="myParticle" rest_position="0 0 0" position="0 0 0" />
                <UniformMass totalMass="30" />
                <PolynomialSpringsForceField polynomialDegree="3" polynomialStiffness="20 10 50" object1='@.' firstObjectPoints='0' object2='@../dofs' secondObjectPoints='15' drawMode='0' showIndicesScale="1"/>
            </Node>
        </Node>
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        lroot = rootNode.addChild('lroot', gravity="0 0 0", dt="0.02")
        lroot.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        lroot.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        lroot.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        lroot.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        lroot.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        lroot.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        lroot.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        lroot.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        lroot.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        lroot.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        lroot.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        lroot.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        lroot.addObject('VisualStyle', displayFlags="showInteractionForceFields")
        lroot.addObject('DefaultAnimationLoop')
        lroot.addObject('MeshOBJLoader', name="LiverSurface", filename="mesh/liver-smooth.obj")

        Liver = lroot.addChild('Liver')
        Liver.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        Liver.addObject('CGLinearSolver', name="linear solver", iterations="25", tolerance="1e-09", threshold="1e-09")
        Liver.addObject('MeshGmshLoader', name="meshLoader", filename="mesh/liver.msh")
        Liver.addObject('TetrahedronSetTopologyContainer', name="topo", src="@meshLoader")
        Liver.addObject('MechanicalObject', name="dofs", src="@meshLoader")
        Liver.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        Liver.addObject('DiagonalMass', name="computed using mass density", massDensity="1")
        Liver.addObject('TetrahedralCorotationalFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.3", youngModulus="3000", computeGlobalMatrix="0")
        Liver.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="3 39 64")

        Visu = Liver.addChild('Visu', tags="Visual", gravity="0 -9.81 0")
        Visu.addObject('OglModel', name="VisualModel", src="@../../LiverSurface")
        Visu.addObject('BarycentricMapping', name="visual mapping", input="@../dofs", output="@VisualModel")

        Weight = Liver.addChild('Weight')
        Weight.addObject('MechanicalObject', template="Vec3", name="myParticle", rest_position="0 0 0", position="0 0 0")
        Weight.addObject('UniformMass', totalMass="30")
        Weight.addObject('PolynomialSpringsForceField', polynomialDegree="3", polynomialStiffness="20 10 50", object1="@.", firstObjectPoints="0", object2="@../dofs", secondObjectPoints="15", drawMode="0", showIndicesScale="1")
    ```


<!-- automatically generated doc END -->
