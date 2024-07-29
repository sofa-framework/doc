Since SOFA is working a lot on solid mechanics, this introduction to physics integration using the FEM is applied on continuum mechanics.

Conservation of linear momentum
===============================

The Newton's second law gives:

$$\frac{d\boldsymbol{p}}{dt}=f$$
$$\frac{d\boldsymbol{p}}{dt}=f_{\text{vol}}+f_{\text{surf}}$$

the force $$f_{\text{surf}}$$ corresponds to the integration of traction forces and the force $$f_{\text{vol}}$$ corresponds to the body forces. With the Cauchy's law and Gauss's theorem, the conservation of linear momentum in the strong (or generalized) form is written:

$$\frac{d\boldsymbol{p}}{dt}=f_{\text{vol}}+f_{\text{surf}}$$
$$\frac{D}{Dt}\int_{\Omega}\rho \boldsymbol{v}d\Omega =\int_{\Omega} \rho \boldsymbol{b}d\Omega +\int_{\Gamma}\boldsymbol{t}d\Gamma$$
$$\int_{\Omega} \rho \frac{D\boldsymbol{v}}{Dt}d\Omega =\int_{\Omega} \rho \boldsymbol{b}d\Omega +\int_{\Gamma}n\cdot \boldsymbol{\sigma}d\Gamma$$
$$\int_{\Omega}\rho \frac{D\boldsymbol{v}}{Dt}d\Omega =\int_{\Omega}\rho \boldsymbol{b}d\Omega +\int_{\Omega}\frac{\partial \sigma_{ij}}{\partial x{i}}d\Omega$$
$$\rho \dot{v}=\rho \boldsymbol{b}+\nabla \cdot \boldsymbol{\sigma}$$



where $$\boldsymbol{\sigma}$$ is the Cauchy's stress tensor (as a reminder $$\nabla \cdot \boldsymbol{\sigma}=\text{div}(\boldsymbol{\sigma})$$), $$\boldsymbol{b}$$ is the density of external forces (force per mass unit), $$\rho$$ is the mass density and $$\dot{v}$$ is the acceleration of the body. The conservation of linear momentum equation relates the change of momentum (LHS inertia term) and the equilibrium equation (RHS with the internal and external forces), which must be solved at each time step.



In order to find a solution over the domain of simulation, we need to integrate this momentum equation. However, in much cases, no exact solution can directly be found. To ensure the existence of a solution, this strong form must be converted into a discrete problem, known as the weak or variational formulation. This is done by taking the product of a test function with the momentum equation and integrating over the current configuration. It is equivalent to formulating the problem to require a solution in the sense of a distribution. The test function is also known as weight function or basis functions, noted $$\psi_j$$. Let $$\Omega$$ denote the volume of our domain and $\Gamma$ denote the surface of the domain, the weak form of the momentum equation becomes:

$$\int_{\Omega} \psi_j \rho \dot{v}d\Omega =\int_{\Omega} \psi_j \rho \boldsymbol{b}d\Omega+\int_{\Omega} \psi_j \nabla \cdot \boldsymbol{\sigma}d\Omega$$

The divergence term can be split as follows:

$$\int_{\Omega} \psi_j \nabla \cdot \boldsymbol{\sigma}d\Omega =\int_\Gamma \psi_j \cdot ( \boldsymbol{\sigma} \cdot n)d\Gamma -\int_\Omega \nabla (\psi_j):\boldsymbol{\sigma}d\Omega$$
$$\int_{\Omega} \psi_j \nabla \cdot \boldsymbol{\sigma}d\Omega =\int_\Gamma \psi_j \cdot \boldsymbol{t}d\Gamma -\int_\Omega \nabla (\psi_j): \boldsymbol{\sigma}d\Omega$$


where appear both a traction boundary condition and an interior traction condition, so that the equation is:

$$\int_{\Omega} \psi_j \rho \dot{v}d\Omega =\int_{\Omega} \psi_j \rho \boldsymbol{b}d\Omega -\int_\Omega \nabla (\psi_j):\boldsymbol{\sigma}d\Omega +\int_\Gamma \psi_j \cdot \boldsymbol{t}d\Gamma$$




FEM at a glance
===============

Since no exact integration can be performed on a random domain $\Omega$, the Finite Element Method (FEM) relies on the subdivision of the domain into subdomains: the finite elements. Many different elements can be considered: quads, triangles, tetrahedra, hexahedra etc. The integration of any function *f* over the domain $$\Omega$$ will therefore result in the sum of the integrals over each finite element (*E* being the total number of finite elements) so that:

$$\int_{\Omega}f(x)d\Omega =\sum_{e=0}^E \int_{V_e}f(x)dV_e$$


The FEM will take advantage of the simple shape of these finite elements to compute these integrals. Within an element, any field like the displacement field *u* can be evaluated in any point *P(x)* as a linear combination of interpolation functions $$\phi_i$$ (called shape functions) and the values of this field $$u(x_i)=u_i$$ at each vertex *i* of the element (*N* being the total number of vertices in one element):

$$u(x)=\sum_{i=0}^{N}u_i\phi_i$$

The shape functions $$\phi_i$$ ensures the continuity of any field over the element. Each element type therefore has specific shape functions. In SOFA, linear interpolation functions are used in the open-source core. Note that higher order (non-linear) elements are available in a SOFA plugin: [SofaHighOrder](https://github.com/sofa-framework/plugin.HighOrder).


**Note**: the Galerkin-Ritz method, the test function $$\psi$$ corresponds to the shape function, noted $$\phi$$. In SOFA, we rely here on this method.


The shape functions $$\phi$$ can be expressed with regard to local coordinates $$(\xi ,\eta ,\zeta )$$, corresponding to a reference configuration of the element. Even if the elements get distorted during the simulation, each element can always be mapped back to one common reference configuration with local coordinates $$(\xi ,\eta ,\zeta )$$, as shown in the figure below. In other words, for any point in space $$\textbf{x}=(x,y,z)$$ inside the element $$K$$ a corresponding point $$\boldsymbol{\xi}=(\xi ,\eta ,\zeta )$$ can be found in the reference space of the element $$\hat{K}$$.


<a href="https://github.com/sofa-framework/doc/blob/master/images/FEM/Tetra-ParentConfig.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/FEM/Tetra-ParentConfig.png?raw=true" title="Transformation T^K from reference configuration to 3D space of a linear tetrahedron"/></a>



Therefore, it always exists a transformation $$T^$$ which can be defined as:

$$T^K:\hat{K} \longrightarrow K$$
$$\boldsymbol{\xi}=(\xi ,\eta ,\zeta )\longrightarrow \textbf{x}=T^K(\boldsymbol{\xi})=\sum_{i=0}^{N}x_i \phi_i(\boldsymbol{\xi})$$

This transformation $$T^K$$ is bijective if the determinant of the Jacobian of the transformation is non-null $$det(J)\neq0$$. Moreover, the transformation $$T^K$$ will allow for the integration of the weak form by change of variables: instead of integrating over $$d\Omega=dxdydz$$, the integration will be reported on the reference element $$d\xi d\eta d\zeta$$. 


#### Example
Let's consider an example. A density of force $$\boldsymbol{b}$$ that depends linearly on the coordinates $$\textbf{x}=(x,y,z)$$: $$\boldsymbol{b}=\alpha \textbf{x}$$. The integration of this term can be done as follows:



$$\int_{\Omega} \phi_j \rho \boldsymbol{b}d\Omega =\sum_{e=0}^E \rho \int_{V_e} \phi_j \alpha \textbf{x}dV_e$$
$$\int_{\Omega} \phi_j \rho \boldsymbol{b}d\Omega =\sum_{e=0}^E \rho \alpha \int_{V_e} \phi_j \sum_{i=0}^{N} \phi_i x_i dV_e$$
$$\int_{\Omega} \phi_j \rho \boldsymbol{b}d\Omega =\sum_{e=0}^E \rho \alpha \int_{V_e} |det(J)| \sum_{i=0}^{N}\phi_j(\boldsymbol{\xi}) \phi_i(\boldsymbol{\xi}) x_i d \boldsymbol{\xi}$$




For each finite element, the shape function $$\phi_i$$ is defined regarding the local coordinates $$\boldsymbol{\xi}$$. The expression of  $$\phi_j(\boldsymbol{\xi}) \phi_i(\boldsymbol{\xi})$$ results from it. Finally, using a [Gauss quadrature](https://en.wikipedia.org/wiki/Gaussian_quadrature) (or Gauss point integration), it is possible to find a numerical solution to this integral over the reference element.



Integration of physics
======================

In SOFA, the physics will be mainly implemented in Mass components and ForceField. You can have a look at the integration of:

- the mass in [MeshMatrixMass](../../components/mass/meshmatrixmass/)
- the integration of linear elasticity in [TetrahedronFEMForceField](../../components/solidmechanics/fem/elastic/tetrahedronfemforcefield/)
