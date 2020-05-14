Since SOFA is working a lot on solid mechanics, this introduction to physics integration using the FEM is applied on continuum mechanics.

Conservation of linear momentum
===============================

The Newton's second law gives:

<img class="latex" src="https://latex.codecogs.com/png.latex?\frac{d\boldsymbol{p}}{dt}=f" title="Newton's second law" />

<img class="latex" src="https://latex.codecogs.com/png.latex?\frac{d\boldsymbol{p}}{dt}=f_{\text{vol}}+f_{\text{surf}}" title="Newton's second law" />

the force <img class="latex" src="https://latex.codecogs.com/png.latex?f_{\text{surf}}" title="Traction forces" /> corresponds to the integration of traction forces and the force <img class="latex" src="https://latex.codecogs.com/png.latex?f_{\text{vol}}" title="Body forces" /> corresponds to the body forces. With the Cauchy's law and Gauss's theorem, the conservation of linear momentum in the strong (or generalized) form is written:

<img class="latex" src="https://latex.codecogs.com/png.latex?\frac{d\boldsymbol{p}}{dt}=f_{\text{vol}}+f_{\text{surf}}" title="Newton's second law" />

<img class="latex" src="https://latex.codecogs.com/png.latex?\frac{D}{Dt}\int_{\Omega}\rho%20\boldsymbol{v}d\Omega%20=\int_{\Omega}%20\rho%20\boldsymbol{b}d\Omega%20+\int_{\Gamma}\boldsymbol{t}d\Gamma" title="Integral form" />

<img class="latex" src="https://latex.codecogs.com/png.latex?\int_{\Omega}%20\rho%20\frac{D\boldsymbol{v}}{Dt}d\Omega%20=\int_{\Omega}%20\rho%20\boldsymbol{b}d\Omega%20+\int_{\Gamma}n\cdot%20\boldsymbol{\sigma}d\Gamma" title="Cauchy's law" />

<img class="latex" src="https://latex.codecogs.com/png.latex?\int_{\Omega}\rho%20\frac{D\boldsymbol{v}}{Dt}d\Omega%20=\int_{\Omega}\rho%20\boldsymbol{b}d\Omega%20+\int_{\Omega}\frac{\partial%20\sigma_{ij}}{\partial%20x{i}}d\Omega" title="Gauss's theorem" />

<img class="latex" src="https://latex.codecogs.com/png.latex?\rho%20\dot{v}=\rho%20\boldsymbol{b}+\nabla%20\cdot%20\boldsymbol{\sigma}" title="Strong form" />



where <img class="latex" src="https://latex.codecogs.com/png.latex?\boldsymbol{\sigma}" title="Cauchy's stress tensor" /> is the Cauchy's stress tensor (as a reminder <img class="latex" src="https://latex.codecogs.com/png.latex?\nabla%20\cdot%20\boldsymbol{\sigma}=\text{div}(\boldsymbol{\sigma})" title="Divergence" />), <img class="latex" src="https://latex.codecogs.com/png.latex?\boldsymbol{b}" title="Density of external forces" /> is the density of external forces (force per mass unit), <img class="latex" src="https://latex.codecogs.com/png.latex?\rho" title="Mass density" /> is the mass density and <img class="latex" src="https://latex.codecogs.com/png.latex?\dot{v}" title="Acceleration of the body" /> is the acceleration of the body. The conservation of linear momentum equation relates the change of momentum (LHS inertia term) and the equilibrium equation (RHS with the internal and external forces), which must be solved at each time step.



In order to find a solution over the domain of simulation, we need to integrate this momentum equation. However, in much cases, no exact solution can directly be found. To ensure the existence of a solution, this strong form must be converted into a discrete problem, known as the weak or variational formulation. This is done by taking the product of a test function with the momentum equation and integrating over the current configuration. It is equivalent to formulating the problem to require a solution in the sense of a distribution. The test function is also known as weight function or basis functions, noted <img class="latex" src="https://latex.codecogs.com/png.latex?\psi_j" title="Test function" />. Let <img class="latex" src="https://latex.codecogs.com/png.latex?\Omega" title="Domain volume" /> denote the volume of our domain and $\Gamma$ denote the surface of the domain, the weak form of the momentum equation becomes:

<img class="latex" src="https://latex.codecogs.com/png.latex?\int_{\Omega}%20\psi_j%20\rho%20\dot{v}d\Omega%20=\int_{\Omega}%20\psi_j%20\rho%20\boldsymbol{b}d\Omega+\int_{\Omega}%20\psi_j%20\nabla%20\cdot%20\boldsymbol{\sigma}d\Omega" title="Weak form of the momentum equation" />

The divergence term can be split as follows:

<img class="latex" src="https://latex.codecogs.com/png.latex?\int_{\Omega}%20\psi_j%20\nabla%20\cdot%20\boldsymbol{\sigma}d\Omega%20=\int_\Gamma%20\psi_j%20\cdot%20(%20\boldsymbol{\sigma}%20\cdot%20n)d\Gamma%20-\int_\Omega%20\nabla%20(\psi_j):\boldsymbol{\sigma}d\Omega" title="Divergence splitting" />

<img class="latex" src="https://latex.codecogs.com/png.latex?\int_{\Omega}%20\psi_j%20\nabla%20\cdot%20\boldsymbol{\sigma}d\Omega%20=\int_\Gamma%20\psi_j%20\cdot%20\boldsymbol{t}d\Gamma%20-\int_\Omega%20\nabla%20(\psi_j):%20\boldsymbol{\sigma}d\Omega" title="Divergence splitting" />


where appear both a traction boundary condition and an interior traction condition, so that the equation is:

<img class="latex" src="https://latex.codecogs.com/png.latex?\int_{\Omega}%20\psi_j%20\rho \dot{v}d\Omega%20=\int_{\Omega}%20\psi_j%20\rho%20\boldsymbol{b}d\Omega%20-\int_\Omega%20\nabla%20(\psi_j):\boldsymbol{\sigma}d\Omega%20+\int_\Gamma%20\psi_j%20\cdot%20\boldsymbol{t}d\Gamma" title="Weak form of the dynamic equation" />




FEM at a glance
===============

Since no exact integration can be performed on a random domain $\Omega$, the Finite Element Method (FEM) relies on the subdivision of the domain into sub-domains: the finite elements. Many different elements can be considered: quads, triangles, tetrahedra, hexahedra etc. The integration of any function *f* over the domain <img class="latex" src="https://latex.codecogs.com/png.latex?\Omega" title="Domain volume" /> will therefore result in the sum of the integrals over each finite element (*E* being the total number of finite elements) so that:

<img class="latex" src="https://latex.codecogs.com/png.latex?\int_{\Omega}f(x)d\Omega%20=\sum_{e=0}^E%20\int_{V_e}f(x)dV_e" title="Integration on sub-elements" />


The FEM will take advantage of the simple shape of these finite elements to compute these integrals. Within an element, any field like the displacement field *u* can be evaluated in any point *P(x)* as a linear combination of interpolation functions <img class="latex" src="https://latex.codecogs.com/png.latex?\phi_i" title="Shape functions" /> (called shape functions) and the values of this field <img class="latex" src="https://latex.codecogs.com/png.latex?u(x_i)=u_i" title="Field at element vertices" /> at each vertex *i* of the element (*N* being the total number of vertices in one element):

<img class="latex" src="https://latex.codecogs.com/png.latex?u(x)=\sum_{i=0}^{N}u_i\phi_i" title="Interpolation within a FE" />


The shape functions <img class="latex" src="https://latex.codecogs.com/png.latex?\phi_i" title="Shape functions" /> ensures the continuity of any field over the element. Each element type therefore has specific shape functions. In SOFA, linear interpolation functions are used in the open-source core. Note that higher order (non-linear) elements are available in a SOFA plugin: [SofaHighOrder](https://github.com/sofa-framework/plugin.HighOrder).


**Note**: the Galerkin-Ritz method, the test function <img class="latex" src="https://latex.codecogs.com/png.latex?\psi" title="Test functions" /> corresponds to the shape function, noted <img class="latex" src="https://latex.codecogs.com/png.latex?\phi" title="Shape functions" />. In SOFA, we rely here on this method.


The shape functions <img class="latex" src="https://latex.codecogs.com/png.latex?\phi" title="Shape functions" /> can be expressed with regards to local coordinates <img class="latex" src="https://latex.codecogs.com/png.latex?(\xi%20,\eta%20,\zeta%20)" title="Local coordinates" />, corresponding to a reference configuration of the element. Even if the elements get distorted during the simulation, each element can always be mapped back to one common reference configuration with local coordinates <img class="latex" src="https://latex.codecogs.com/png.latex?(\xi%20,\eta%20,\zeta%20)" title="Local coordinates" />, as shown in the figure below. In other words, for any point in space <img class="latex" src="https://latex.codecogs.com/png.latex?\textbf{x}=(x,y,z)" title="Global coordinates" /> inside the element <img class="latex" src="https://latex.codecogs.com/png.latex?K" title="Element K" /> a corresponding point <img class="latex" src="https://latex.codecogs.com/png.latex?\boldsymbol{\xi}=(\xi%20,\eta%20,\zeta%20)" title="Local coordinates" /> can be found in the reference space of the element <img class="latex" src="https://latex.codecogs.com/png.latex?\hat{K}" title="Reference of element K" />.


<a href="https://github.com/sofa-framework/doc/blob/master/images/FEM/Tetra-ParentConfig.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/FEM/Tetra-ParentConfig.png?raw=true" title="Transformation T^K from reference configuration to 3D space of a linear tetrahedron"/></a>



Therefore, it always exists a transformation <img class="latex" src="https://latex.codecogs.com/png.latex?T^K" title="Transformation T^K from reference configuration to global space" /> which can be defined as:

<img class="latex" src="https://latex.codecogs.com/png.latex?T^K:\hat{K}%20\longrightarrow%20K" title="Transformation T^K" />

<img class="latex" src="https://latex.codecogs.com/png.latex?\boldsymbol{\xi}=(\xi%20,\eta%20,\zeta%20)\longrightarrow%20\textbf{x}=T^K(\boldsymbol{\xi})=\sum_{i=0}^{N}x_i%20\phi_i(\boldsymbol{\xi})" title="Transformation T^K" />


This transformation <img class="latex" src="https://latex.codecogs.com/png.latex?T^K" title="Transformation T^K from reference configuration to global space" /> is bijective if the determinant of the Jacobian of the transmation is non-null <img class="latex" src="https://latex.codecogs.com/png.latex?det(J)\neq0" title="Non-zero Jacobian" />. Moreover, the transformation <img class="latex" src="https://latex.codecogs.com/png.latex?T^K" title="Transformation T^K from reference configuration to global space" /> will allow for the integration of the weak form by change of variables: instead of integrating over <img class="latex" src="https://latex.codecogs.com/png.latex?d\Omega=dxdydz" title="Derivative of global coordinates" />, the integration will be reported on the reference element <img class="latex" src="https://latex.codecogs.com/png.latex?d\xi%20d\eta%20d\zeta" title="Derivative of local coordinates" />. 


#### Example
Let's consider an example. A density of force <img class="latex" src="https://latex.codecogs.com/png.latex?\boldsymbol{b}" title="Density of force" /> that depends linearly on the coordinates <img class="latex" src="https://latex.codecogs.com/png.latex?\textbf{x}=(x,y,z)" title="Global coordinates" />: <img class="latex" src="https://latex.codecogs.com/png.latex?\boldsymbol{b}=\alpha%20\textbf{x}" title="Density of force" />. The integration of this term can be done as follows:



<img class="latex" src="https://latex.codecogs.com/png.latex?\int_{\Omega}%20\phi_j%20\rho%20\boldsymbol{b}d\Omega%20=\sum_{e=0}^E%20\rho%20\int_{V_e}%20\phi_j%20\alpha%20\textbf{x}dV_e" title="Integration of the force" />

<img class="latex" src="https://latex.codecogs.com/png.latex?\int_{\Omega}%20\phi_j%20\rho%20\boldsymbol{b}d\Omega%20=\sum_{e=0}^E%20\rho%20\alpha%20\int_{V_e}%20\phi_j%20\sum_{i=0}^{N}%20\phi_i%20x_i%20dV_e" title="Integraton of the force" />

<img class="latex" src="https://latex.codecogs.com/png.latex?\int_{\Omega}%20\phi_j%20\rho%20\boldsymbol{b}d\Omega%20=\sum_{e=0}^E%20\rho%20\alpha%20\int_{V_e}%20|det(J)|%20\sum_{i=0}^{N}\phi_j(\boldsymbol{\xi})%20\phi_i(\boldsymbol{\xi})%20x_i%20d%20\boldsymbol{\xi}
" title="Integraton of the force" />




For each finite element, the shape function <img class="latex" src="https://latex.codecogs.com/png.latex?\phi_i" title="Shape functions" /> is defined regarding the local coordinates <img class="latex" src="https://latex.codecogs.com/png.latex?\boldsymbol{\xi}" title="Local coordinates" />. The expression of  <img class="latex" src="https://latex.codecogs.com/png.latex?\phi_j(\boldsymbol{\xi})%20\phi_i(\boldsymbol{\xi})" title="Shape function integration" /> results from it. Finally, using a [Gauss quadrature](https://en.wikipedia.org/wiki/Gaussian_quadrature) (or Gauss point integration), it is possible to find a numerical solution to this integral over the reference element.



Integration of physics
======================

In SOFA, the physics will be mainly implemented in Mass components and ForceField. You can have a look at the integration of:

- the mass in [MeshMatrixMass](https://www.sofa-framework.org/community/doc/using-sofa/components/mass/meshmatrixmass/)
- the integration of linear elasticity in [TetrahedronFEMForceField](https://www.sofa-framework.org/community/doc/using-sofa/components/forcefield/tetrahedronfemforcefield/)
