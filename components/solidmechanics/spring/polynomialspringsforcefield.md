---
title: PolynomialSpringsForceField
---

PolynomialSpringsForceField
===========================

This component belongs to the category of [ForceField](../../../../simulation-principles/multi-model-representation/forcefield/). This component allows to simulate springs with Polynomial stress strain behavior. If we note:

- $F$ the spring force
- $S$ the cross section (always 1.0)
- $\sigma$ the stress-strain non-linear function
- $l_0$ the original length and $l$ the current length of the spring
- $\Delta u %3D \left\{\begin{matrix} \Delta x\\ \Delta y\\ \Delta z\\ \end{matrix}\right.$ the point displacement

the generic non-linear force can thus be written:

$$
F=S%7E\sigma \left( \frac{l-l_0}{l_0} \right%29 \frac{\Delta u}{l}
$$ 

where $\sigma$ is polynom as follows:

$$
\sigma \left( \frac{l-l_0}{l_0} \right) =\sigma(L)=a_1L+a_2L^2+\cdots+a_nL^n
$$

and

$$
\frac{\partial \sigma}{\partial L}=a_1+a_2L+\cdots+a_nL^{n-1}
$$

The dedication of Jacobian matrix for PolynomialSpringForceField is given below:

$$
J_F(u)=\left(S\frac{\partial&space;\sigma}{\partial&space;L}\cdot\frac{1}{l_0}-S\sigma\cdot\frac{1}{|l|}&space;\right)\begin{bmatrix}\frac{\Delta&space;x^2}{l^2}&\frac{\Delta&space;x\Delta&space;y}{l^2}&\frac{\Delta&space;x\Delta&space;z}{l^2}\\\frac{\Delta&space;y\Delta&space;x}{l^2}&\frac{\Delta&space;y^2}{l^2}&\frac{\Delta&space;y\Delta&space;z}{l^2}\\\frac{\Delta&space;z\Delta&space;x}{l^2}&\frac{\Delta&space;z\Delta&space;y}{l^2}&&space;\frac{\Delta&space;z^2}{l^2}\end{bmatrix}&plus;S\sigma\cdot\frac{1}{|l|}\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}
$$


Note that a **RestShape**PolynomialSpringsForceField does exist. It will compute the same non-linear force with regards to the rest shape of one single object. To avoid Nan problems when a spring has a zero length, an exponential addition to the denominator has been added. As a result, the stress simulation is shifted compared with polynomial values, but it keeps its nonlinearity:

$$
J_F(u)=\left(S\frac{\partial&space;\sigma}{\partial&space;L}\cdot\frac{(1-sc\cdot&space;e^{sh-sc(\Delta&space;x^2&plus;\Delta&space;y^2&plus;\Delta&space;z^2)})}{l_0}-S\sigma\cdot\frac{(1-sc\cdot&space;e^{sh-sc(\Delta&space;x^2&plus;\Delta&space;y^2&plus;\Delta&space;z^2)})}{\sqrt{\Delta&space;x^2&plus;\Delta&space;y^2&plus;\Delta&space;z^2&plus;e^{sh-sc(\Delta&space;x^2&plus;\Delta&space;y^2&plus;\Delta&space;z^2)}}}&space;\right)\cdot\frac{1}{\sqrt{\Delta&space;x^2&plus;\Delta&space;y^2&plus;\Delta&space;z^2&plus;e^{sh-sc(\Delta&space;x^2&plus;\Delta&space;y^2&plus;\Delta&space;z^2)}}}\cdot\begin{bmatrix}\Delta&space;x^2&\Delta&space;x\Delta&space;y&\Delta&space;x\Delta&space;z\\\Delta&space;y\Delta&space;x&\Delta&space;y^2&\Delta&space;y\Delta&space;z\\\Delta&space;z\Delta&space;x&\Delta&space;z\Delta&space;y&\Delta&space;z^2\end{bmatrix}&plus;S\sigma\cdot\frac{1}{\sqrt{\Delta&space;x^2&plus;\Delta&space;y^2&plus;\Delta&space;z^2&plus;e^{sh-sc(\Delta&space;x^2&plus;\Delta&space;y^2&plus;\Delta&space;z^2)}}}\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}
$$

More details were given in the pull-request [#1342](https://github.com/sofa-framework/sofa/pull/1342).


Usage
-----

The PolynomialSpringsForceField **requires** two different objects to link, which means two MechanicalObjects on which the non-linear spring will act.
On the other hand, RestShapePolynomialSpringsForceField will act on one single body, i.e. one MechanicalObject.
<!-- automatically generated doc START -->
<!-- generate_doc -->

Simple elastic springs applied to given degrees of freedom between their current and rest shape position


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.SolidMechanics.Spring

__namespace__: sofa::component::solidmechanics::spring

__parents__:

- PairInteractionForceField

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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|object1|First object associated to this component|MechanicalState&lt;Vec3d&gt;|
|object2|Second object associated to this component|MechanicalState&lt;Vec3d&gt;|

## Examples 

PolynomialSpringsForceField.scn

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
    def createScene(root_node):

       lroot = root_node.addChild('lroot', gravity="0 0 0", dt="0.02")

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
       lroot.addObject('DefaultAnimationLoop', )
       lroot.addObject('MeshOBJLoader', name="LiverSurface", filename="mesh/liver-smooth.obj")

       liver = lroot.addChild('Liver')

       liver.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
       liver.addObject('CGLinearSolver', name="linear solver", iterations="25", tolerance="1e-09", threshold="1e-09")
       liver.addObject('MeshGmshLoader', name="meshLoader", filename="mesh/liver.msh")
       liver.addObject('TetrahedronSetTopologyContainer', name="topo", src="@meshLoader")
       liver.addObject('MechanicalObject', name="dofs", src="@meshLoader")
       liver.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       liver.addObject('DiagonalMass', name="computed using mass density", massDensity="1")
       liver.addObject('TetrahedralCorotationalFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.3", youngModulus="3000", computeGlobalMatrix="0")
       liver.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="3 39 64")

       visu = Liver.addChild('Visu', tags="Visual", gravity="0 -9.81 0")

       visu.addObject('OglModel', name="VisualModel", src="@../../LiverSurface")
       visu.addObject('BarycentricMapping', name="visual mapping", input="@../dofs", output="@VisualModel")

       weight = Liver.addChild('Weight')

       weight.addObject('MechanicalObject', template="Vec3", name="myParticle", rest_position="0 0 0", position="0 0 0")
       weight.addObject('UniformMass', totalMass="30")
       weight.addObject('PolynomialSpringsForceField', polynomialDegree="3", polynomialStiffness="20 10 50", object1="@.", firstObjectPoints="0", object2="@../dofs", secondObjectPoints="15", drawMode="0", showIndicesScale="1")
    ```


<!-- automatically generated doc END -->
