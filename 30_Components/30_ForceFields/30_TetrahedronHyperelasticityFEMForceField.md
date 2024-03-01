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
