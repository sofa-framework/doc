TetrahedronHyperelasticityFEMForceField
=======================================

This component belongs to the category of [ForceField](../../../../../simulation-principles/multi-model-representation/forcefield/). The TetrahedronHyperelasticityFEMForceField implements - for tetrahedral topology only - several non-linear mechanical constitutive laws, also named as hyperelastic constitutive laws. The available models are:

- [Arruda-Boyce model](https://en.wikipedia.org/wiki/Arruda%E2%80%93Boyce_model)
- [Costa model](https://www.jstor.org/stable/pdf/3066567.pdf)
- [Mooney-Rivlin model](https://en.wikipedia.org/wiki/Mooney%E2%80%93Rivlin_solid)
- [Neo-Hookean model](https://en.wikipedia.org/wiki/Neo-Hookean_solid)
- [Ogden model](https://en.wikipedia.org/wiki/Ogden_hyperelastic_model) (order 1)
- [St Venant-Kirchhoff model](https://en.wikipedia.org/wiki/Hyperelastic_material#Saint_Venant%E2%80%93Kirchhoff_model)
- [Veronda-Westmann model](https://www.sciencedirect.com/science/article/pii/0021929070900552)



Note that the **ParameterSet** data changes depending on the chosen material. It corresponds to:
	- for "ArrudaBoyce", two parameters are required: $$\left[ \mu ,k_0\right]$$
	- for "Costa", eight parameters are required: $$\left[ a,k_{0},b_{ff},b_{fs},b_{ss},b_{fn},b_{sn},b_{nn}\right]$$
	- for "MooneyRivlin", three parameters are required: $$\left[ C_{01},C_{10},k_{0}\right]$$
	- for "NeoHookean", two parameters are required: $$\left[ \mu,k\right]$$
	- for "Ogden", three parameters are required: $$\left[ k,\mu_1,\alpha_1\right]$$
	- for "StVenantKirchhoff", two parameters are required: $$\left[ \mu,\lambda \right]$$
	- for "VerondaWestman", parameters are required: $$\left[ C_{1},C_{2},k_0\right]$$


Usage
-----

As a Forcefield, the TetrahedronHyperelasticityFEMForceField requires a **MechanicalObject** and the associated **solvers** (integration scheme and linear solver), as well as a **TetrahedronSetTopologyContainer**.

