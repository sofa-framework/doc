---
title: TetrahedronHyperelasticityFEMForceField
---

TetrahedronHyperelasticityFEMForceField
=======================================

This component belongs to the category of [ForceField](https://www.sofa-framework.org/community/doc/simulation-principles/multi-model-representation/forcefield/). The TetrahedronHyperelasticityFEMForceField implements - for tetrahedral topology only - several non-linear mechanical constitutive laws, also named as hyperelastic constitutive laws. The available models are:

- [Arruda-Boyce model](https://en.wikipedia.org/wiki/Arruda%E2%80%93Boyce_model)
- [Costa model](https://www.jstor.org/stable/pdf/3066567.pdf)
- [Mooney-Rivlin model](https://en.wikipedia.org/wiki/Mooney%E2%80%93Rivlin_solid)
- [Neo-Hookean model](https://en.wikipedia.org/wiki/Neo-Hookean_solid)
- [Ogden model](https://en.wikipedia.org/wiki/Ogden_hyperelastic_model) (order 1)
- [St Venant-Kirchhoff model](https://en.wikipedia.org/wiki/Hyperelastic_material#Saint_Venant%E2%80%93Kirchhoff_model)
- [Veronda-Westmann model](https://www.sciencedirect.com/science/article/pii/0021929070900552)



Data  
----

- **materialName**: name of the material to be used, the possible options are:
	- "ArrudaBoyce"
	- "Costa"
	- "MooneyRivlin"
	- "NeoHookean"
	- "Ogden"
	- "StVenantKirchhoff"
	- "VerondaWestman"
- **ParameterSet**: global parameters specifying the material, the number of data depends on the materialName given:
	- for "ArrudaBoyce", two parameters are required: <img class="latex" src="https://latex.codecogs.com/png.latex?\left[%20\mu%20,k_0\right]" title="ArrudaBoyce ParameterSet" />
	- for "Costa", eight parameters are required: <img class="latex" src="https://latex.codecogs.com/png.latex?\left[%20a,k_{0},b_{ff},b_{fs},b_{ss},b_{fn},b_{sn},b_{nn}\right]" title="Costa ParameterSet" />
	- for "MooneyRivlin", three parameters are required: <img class="latex" src="https://latex.codecogs.com/png.latex?\left[%20C_{01},C_{10},k_{0}\right]" title="MooneyRivlin ParameterSet" />
	- for "NeoHookean", two parameters are required: <img class="latex" src="https://latex.codecogs.com/png.latex?\left[%20\mu,k\right]" title="NeoHookean ParameterSet" />
	- for "Ogden", three parameters are required: <img class="latex" src="https://latex.codecogs.com/png.latex?\left[%20k,\mu_1,\alpha_1\right]" title="Ogden ParameterSet" />
	- for "StVenantKirchhoff", two parameters are required: <img class="latex" src="https://latex.codecogs.com/png.latex?\left[%20\mu,\lambda%20\right]" title="StVenantKirchhoff ParameterSet" />
	- for "VerondaWestman", parameters are required: <img class="latex" src="https://latex.codecogs.com/png.latex?\left[%20C_{1},C_{2},k_0\right]" title="VerondaWestman ParameterSet" />
- **AnisotropyDirections**: global directions of anisotropy of the material, it is a `vector<Coord>` i.e. a vector containing at each entry a vector which size is the dimension of your degrees of freedom (e.g. 3 if Vec3d). The size of the array is 0 if the material is isotropic, 1 if it is transversely isotropic and 2 for orthotropic materials.
- **topology**: link towards the TetrahedronSetTopologyContainer associated to your degrees of freedom in the node or in the graph


Usage
-----

As a Forcefield, the TetrahedronHyperelasticityFEMForceField requires a **MechanicalObject** and the associated **solvers** (integration scheme and linear solver), as well as a **TetrahedronSetTopologyContainer**.


Example
-------

This component is used as follows in XML format:

``` xml
<TetrahedronHyperelasticityFEMForceField name="HyperElasticMaterial" materialName="StVenantKirchhoff" ParameterSet="3448.2 31034.4"/>
```

with a St Venant-Kirchhoff model using the parameters: <img class="latex" src="https://latex.codecogs.com/png.latex?\mu= 3448.2,~\lambda=31034.4\right]" title="StVenantKirchhoff example" />
Using SofaPython3:

``` python
node.addObject('TetrahedronHyperelasticityFEMForceField', name="HyperElasticMaterial", materialName="StVenantKirchhoff", ParameterSet="3448.2 31034.4")
```

An example scene involving a TetrahedronHyperelasticityFEMForceField is available in [*examples/Component/SolidMechanics/FEM/TetrahedronHyperelasticityFEMForceField.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/SolidMechanics/FEM/TetrahedronHyperelasticityFEMForceField.scn)
<!-- automatically generated doc START -->
__Target__: `Sofa.Component.SolidMechanics.FEM.HyperElastic`

__namespace__: `#!c++ sofa::component::solidmechanics::fem::hyperelastic`

__parents__: 

- `#!c++ ForceField`

__categories__: 

- ForceField

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
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping - stiffness matrix coefficient
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>matrixRegularization</td>
		<td>
Regularization of the Stiffness Matrix (between true or false)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>materialName</td>
		<td>
the name of the material to be used. Possible options are: 'ArrudaBoyce', 'Costa', 'MooneyRivlin', 'NeoHookean', 'Ogden', 'StVenantKirchhoff', 'VerondaWestman', 'StableNeoHookean'
</td>
		<td>ArrudaBoyce</td>
	</tr>
	<tr>
		<td>ParameterSet</td>
		<td>
The global parameters specifying the material
</td>
		<td></td>
	</tr>
	<tr>
		<td>AnisotropyDirections</td>
		<td>
The global directions of anisotropy of the material: vector containing anisotropic directions. The vector size is 0 if the material is isotropic, 1 if it is transversely isotropic and 2 for orthotropic materials
</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedronInfo</td>
		<td>
Internal tetrahedron data
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

Component/SolidMechanics/FEM/TetrahedronHyperelasticityFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.005" showBoundingTree="0" gravity="0 -9 0">
    	<RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
    	<RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
    	<RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
    	<RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
    	<RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
    	<RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
    	<RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [MeshMatrixMass] -->
    	<RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
    	<RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
    	<RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.HyperElastic"/> <!-- Needed to use components [TetrahedronHyperelasticityFEMForceField] -->
    	<RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
    	<RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier] -->
    	<RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
    	<RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping] -->
    	<RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [Visual3DText VisualStyle] -->
    
    	<VisualStyle displayFlags="showForceFields showBehaviorModels" />
    	<CollisionPipeline verbose="0" />
    	<BruteForceBroadPhase/>
        <BVHNarrowPhase/>
    	<CollisionResponse response="PenalityContactForceField" />
    	<MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
    	<DefaultAnimationLoop/>
    	
    	<Node name="Corrotational">
    		<EulerImplicitSolver name="cg_odesolver" printLog="false" />
    		<CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    		
    		<RegularGridTopology name="hexaGrid" min="0 0 0" max="1 1 2.7" n="3 3 8" p0="0 0 0"/>
    		
    		<MechanicalObject name="mechObj"/>
    		<MeshMatrixMass totalMass="1.0"/>
    		<TetrahedronFEMForceField name="FEM" youngModulus="10000" poissonRatio="0.45" method="large" />
    		
    		<BoxROI drawBoxes="0" box="0 0 0 1 1 0.05" name="box"/>
    		<FixedProjectiveConstraint indices="@box.indices"/>
    		<Visual3DText text="Corrotational" position="1 0 -0.5" scale="0.2" />
    	</Node>
    	
    	<Node name="ArrudaBoyce">		
    		<EulerImplicitSolver name="cg_odesolver" printLog="false" />
    		<CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    			
    		<RegularGridTopology name="hexaGrid" min="0 0 0" max="1 1 2.7" n="3 3 8" p0="2 0 0"/>
    		
    		<MechanicalObject name="mechObj"/>
    		<MeshMatrixMass totalMass="1.0"/>
    		
    		<Node name="tetras">
    			<TetrahedronSetTopologyContainer name="Container"/>
    			<TetrahedronSetTopologyModifier name="Modifier" />
    			<TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
    			<Hexa2TetraTopologicalMapping name="default28" input="@../" output="@Container" printLog="0" />
    			
    			<TetrahedronHyperelasticityFEMForceField name="FEM" ParameterSet="3448.2759 31034.483"/>
    		</Node>
    		
    		<BoxROI drawBoxes="1" box="2 0 0 3 1 0.05" name="box"/>
    		<FixedProjectiveConstraint indices="@box.indices"/>
    		<Visual3DText text="ArrudaBoyce" position="3 0 -0.5" scale="0.2" />
    	</Node>
    	
    	<Node name="StVenantKirchhoff">		
    		<EulerImplicitSolver name="cg_odesolver" printLog="false" />
    		<CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    			
    		<RegularGridTopology name="hexaGrid" min="0 0 0" max="1 1 2.7" n="3 3 8" p0="4 0 0"/>
    		
    		<MechanicalObject name="mechObj"/>
    		<MeshMatrixMass totalMass="1.0"/>
    		
    		<Node name="tetras">
    			<TetrahedronSetTopologyContainer name="Container"/>
    			<TetrahedronSetTopologyModifier name="Modifier" />
    			<TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
    			<Hexa2TetraTopologicalMapping name="default28" input="@../" output="@Container" printLog="0" />
    			
    			<TetrahedronHyperelasticityFEMForceField name="FEM" ParameterSet="3448.2759 31034.483" materialName="StVenantKirchhoff"/>
    		</Node>
    		
    		<BoxROI drawBoxes="1" box="4 0 0 5 1 0.05" name="box"/>
    		<FixedProjectiveConstraint indices="@box.indices"/>
    		<Visual3DText text="StVenantKirchhoff" position="5 0 -0.5" scale="0.2" />
    	</Node>
    	
    	
    	<Node name="NeoHookean">		
    		<EulerImplicitSolver name="cg_odesolver" printLog="false" />
    		<CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    			
    		<RegularGridTopology name="hexaGrid" min="0 0 0" max="1 1 2.7" n="3 3 8" p0="6 0 0"/>
    		
    		<MechanicalObject name="mechObj"/>
    		<MeshMatrixMass totalMass="1.0"/>
    		
    		<Node name="tetras">
    			<TetrahedronSetTopologyContainer name="Container"/>
    			<TetrahedronSetTopologyModifier name="Modifier" />
    			<TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
    			<Hexa2TetraTopologicalMapping name="default28" input="@../" output="@Container" printLog="0" />
    			
    			<TetrahedronHyperelasticityFEMForceField name="FEM" ParameterSet="3448.2759 31034.483" materialName="NeoHookean"/>
    		</Node>
    		
    		<BoxROI drawBoxes="1" box="6 0 0 7 1 0.05" name="box"/>
    		<FixedProjectiveConstraint indices="@box.indices"/>
    		<Visual3DText text="NeoHookean" position="7 0 -0.5" scale="0.2" />
    	</Node>
    	
    	
    	<Node name="MooneyRivlin">		
    		<EulerImplicitSolver name="cg_odesolver" printLog="false" />
    		<CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    			
    		<RegularGridTopology name="hexaGrid" min="0 0 0" max="1 1 2.7" n="3 3 8" p0="8 0 0"/>
    		
    		<MechanicalObject name="mechObj"/>
    		<MeshMatrixMass totalMass="1.0"/>
    		
    		<Node name="tetras">
    			<TetrahedronSetTopologyContainer name="Container"/>
    			<TetrahedronSetTopologyModifier name="Modifier" />
    			<TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
    			<Hexa2TetraTopologicalMapping name="default28" input="@../" output="@Container" printLog="0" />
    			
    			<TetrahedronHyperelasticityFEMForceField name="FEM" ParameterSet="5000 7000 10" materialName="MooneyRivlin"/>
    		</Node>
    		
    		<BoxROI drawBoxes="1" box="8 0 0 9 1 0.05" name="box"/>
    		<FixedProjectiveConstraint indices="@box.indices"/>
    		<Visual3DText text="MooneyRivlin" position="9 0 -0.5" scale="0.2" />
    	</Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.005", showBoundingTree="0", gravity="0 -9 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.HyperElastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="showForceFields showBehaviorModels")
        root.addObject('CollisionPipeline', verbose="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField")
        root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")
        root.addObject('DefaultAnimationLoop')

        Corrotational = root.addChild('Corrotational')
        Corrotational.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        Corrotational.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        Corrotational.addObject('RegularGridTopology', name="hexaGrid", min="0 0 0", max="1 1 2.7", n="3 3 8", p0="0 0 0")
        Corrotational.addObject('MechanicalObject', name="mechObj")
        Corrotational.addObject('MeshMatrixMass', totalMass="1.0")
        Corrotational.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="10000", poissonRatio="0.45", method="large")
        Corrotational.addObject('BoxROI', drawBoxes="0", box="0 0 0 1 1 0.05", name="box")
        Corrotational.addObject('FixedProjectiveConstraint', indices="@box.indices")
        Corrotational.addObject('Visual3DText', text="Corrotational", position="1 0 -0.5", scale="0.2")

        ArrudaBoyce = root.addChild('ArrudaBoyce')
        ArrudaBoyce.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        ArrudaBoyce.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        ArrudaBoyce.addObject('RegularGridTopology', name="hexaGrid", min="0 0 0", max="1 1 2.7", n="3 3 8", p0="2 0 0")
        ArrudaBoyce.addObject('MechanicalObject', name="mechObj")
        ArrudaBoyce.addObject('MeshMatrixMass', totalMass="1.0")

        tetras = ArrudaBoyce.addChild('tetras')
        tetras.addObject('TetrahedronSetTopologyContainer', name="Container")
        tetras.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        tetras.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        tetras.addObject('Hexa2TetraTopologicalMapping', name="default28", input="@../", output="@Container", printLog="0")
        tetras.addObject('TetrahedronHyperelasticityFEMForceField', name="FEM", ParameterSet="3448.2759 31034.483")
        ArrudaBoyce.addObject('BoxROI', drawBoxes="1", box="2 0 0 3 1 0.05", name="box")
        ArrudaBoyce.addObject('FixedProjectiveConstraint', indices="@box.indices")
        ArrudaBoyce.addObject('Visual3DText', text="ArrudaBoyce", position="3 0 -0.5", scale="0.2")

        StVenantKirchhoff = root.addChild('StVenantKirchhoff')
        StVenantKirchhoff.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        StVenantKirchhoff.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        StVenantKirchhoff.addObject('RegularGridTopology', name="hexaGrid", min="0 0 0", max="1 1 2.7", n="3 3 8", p0="4 0 0")
        StVenantKirchhoff.addObject('MechanicalObject', name="mechObj")
        StVenantKirchhoff.addObject('MeshMatrixMass', totalMass="1.0")

        tetras = StVenantKirchhoff.addChild('tetras')
        tetras.addObject('TetrahedronSetTopologyContainer', name="Container")
        tetras.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        tetras.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        tetras.addObject('Hexa2TetraTopologicalMapping', name="default28", input="@../", output="@Container", printLog="0")
        tetras.addObject('TetrahedronHyperelasticityFEMForceField', name="FEM", ParameterSet="3448.2759 31034.483", materialName="StVenantKirchhoff")
        StVenantKirchhoff.addObject('BoxROI', drawBoxes="1", box="4 0 0 5 1 0.05", name="box")
        StVenantKirchhoff.addObject('FixedProjectiveConstraint', indices="@box.indices")
        StVenantKirchhoff.addObject('Visual3DText', text="StVenantKirchhoff", position="5 0 -0.5", scale="0.2")

        NeoHookean = root.addChild('NeoHookean')
        NeoHookean.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        NeoHookean.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        NeoHookean.addObject('RegularGridTopology', name="hexaGrid", min="0 0 0", max="1 1 2.7", n="3 3 8", p0="6 0 0")
        NeoHookean.addObject('MechanicalObject', name="mechObj")
        NeoHookean.addObject('MeshMatrixMass', totalMass="1.0")

        tetras = NeoHookean.addChild('tetras')
        tetras.addObject('TetrahedronSetTopologyContainer', name="Container")
        tetras.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        tetras.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        tetras.addObject('Hexa2TetraTopologicalMapping', name="default28", input="@../", output="@Container", printLog="0")
        tetras.addObject('TetrahedronHyperelasticityFEMForceField', name="FEM", ParameterSet="3448.2759 31034.483", materialName="NeoHookean")
        NeoHookean.addObject('BoxROI', drawBoxes="1", box="6 0 0 7 1 0.05", name="box")
        NeoHookean.addObject('FixedProjectiveConstraint', indices="@box.indices")
        NeoHookean.addObject('Visual3DText', text="NeoHookean", position="7 0 -0.5", scale="0.2")

        MooneyRivlin = root.addChild('MooneyRivlin')
        MooneyRivlin.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        MooneyRivlin.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        MooneyRivlin.addObject('RegularGridTopology', name="hexaGrid", min="0 0 0", max="1 1 2.7", n="3 3 8", p0="8 0 0")
        MooneyRivlin.addObject('MechanicalObject', name="mechObj")
        MooneyRivlin.addObject('MeshMatrixMass', totalMass="1.0")

        tetras = MooneyRivlin.addChild('tetras')
        tetras.addObject('TetrahedronSetTopologyContainer', name="Container")
        tetras.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        tetras.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        tetras.addObject('Hexa2TetraTopologicalMapping', name="default28", input="@../", output="@Container", printLog="0")
        tetras.addObject('TetrahedronHyperelasticityFEMForceField', name="FEM", ParameterSet="5000 7000 10", materialName="MooneyRivlin")
        MooneyRivlin.addObject('BoxROI', drawBoxes="1", box="8 0 0 9 1 0.05", name="box")
        MooneyRivlin.addObject('FixedProjectiveConstraint', indices="@box.indices")
        MooneyRivlin.addObject('Visual3DText', text="MooneyRivlin", position="9 0 -0.5", scale="0.2")
    ```

Component/SolidMechanics/FEM/TetrahedronHyperelasticityFEMForceField_invertedTets.scn

=== "XML"

    ```xml
    ﻿<?xml version="1.0" ?>
    <Node name="root" dt="0.00005" showBoundingTree="0" gravity="0 0 0">
        <Node name="plugins">
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [SparseLDLSolver] -->
            <RequiredPlugin name="Sofa.Component.LinearSystem"/> <!-- Needed to use components [ConstantSparsityPatternSystem] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [MeshMatrixMass] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.HyperElastic"/> <!-- Needed to use components [TetrahedronHyperelasticityFEMForceField] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
            <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping] -->
            <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        </Node>
    
        <VisualStyle displayFlags="showForceFields showBehaviorModels" />
    
        <DefaultAnimationLoop/>
    
        <Node name="StableNeoHookean">
            <EulerImplicitSolver name="odesolver"/>
            <ConstantSparsityPatternSystem template="CompressedRowSparseMatrixd" name="A"/>
            <SparseLDLSolver template="CompressedRowSparseMatrixd"/>
    
            <RegularGridTopology name="hexaGrid"     min="0 0 0" max="1 1 2.7" n="6 6 16" p0="0 0 0"/>
            <RegularGridTopology name="hexaGridRest" min="0 0 0" max="1 1 -2.7"   n="6 6 16" p0="0 0 0"/>
    
            <MechanicalObject name="mechObj" rest_position="@hexaGrid.position" position="@hexaGridRest.position"/>
            <MeshMatrixMass totalMass="1.0"/>
    
            <Node name="tetras">
                <TetrahedronSetTopologyContainer name="Container"/>
                <TetrahedronSetTopologyModifier name="Modifier" />
                <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                <Hexa2TetraTopologicalMapping name="default28" input="@../hexaGrid" output="@Container" printLog="0" />
    
                <TetrahedronHyperelasticityFEMForceField name="FEM" ParameterSet="1644295.30201342 33557.0469798658" materialName="StableNeoHookean"/>
            </Node>
    
            <BoxROI drawBoxes="1" box="0 0 0 1 1 0.05" name="box"/>
            <FixedProjectiveConstraint indices="@box.indices"/>
        </Node>
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.00005", showBoundingTree="0", gravity="0 0 0")

        plugins = root.addChild('plugins')
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSystem")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.HyperElastic")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="showForceFields showBehaviorModels")
        root.addObject('DefaultAnimationLoop')

        StableNeoHookean = root.addChild('StableNeoHookean')
        StableNeoHookean.addObject('EulerImplicitSolver', name="odesolver")
        StableNeoHookean.addObject('ConstantSparsityPatternSystem', template="CompressedRowSparseMatrixd", name="A")
        StableNeoHookean.addObject('SparseLDLSolver', template="CompressedRowSparseMatrixd")
        StableNeoHookean.addObject('RegularGridTopology', name="hexaGrid", min="0 0 0", max="1 1 2.7", n="6 6 16", p0="0 0 0")
        StableNeoHookean.addObject('RegularGridTopology', name="hexaGridRest", min="0 0 0", max="1 1 -2.7", n="6 6 16", p0="0 0 0")
        StableNeoHookean.addObject('MechanicalObject', name="mechObj", rest_position="@hexaGrid.position", position="@hexaGridRest.position")
        StableNeoHookean.addObject('MeshMatrixMass', totalMass="1.0")

        tetras = StableNeoHookean.addChild('tetras')
        tetras.addObject('TetrahedronSetTopologyContainer', name="Container")
        tetras.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        tetras.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        tetras.addObject('Hexa2TetraTopologicalMapping', name="default28", input="@../hexaGrid", output="@Container", printLog="0")
        tetras.addObject('TetrahedronHyperelasticityFEMForceField', name="FEM", ParameterSet="1644295.30201342 33557.0469798658", materialName="StableNeoHookean")
        StableNeoHookean.addObject('BoxROI', drawBoxes="1", box="0 0 0 1 1 0.05", name="box")
        StableNeoHookean.addObject('FixedProjectiveConstraint', indices="@box.indices")
    ```


<!-- automatically generated doc END -->
