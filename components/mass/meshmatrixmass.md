---
title: MeshMatrixMass
---

MeshMatrixMass  
==============

This component belongs to the category of [Masses](../../simulation-principles/multi-model-representation/mass/). In the dynamic equation (see [Physics integration](../../simulation-principles/multi-model-representation/physics-integration/) page), the mass density results from the first derivative in time of the momentum term. The MeshMatrixMass computes the integral of this mass density over the volume of the object geometry. To do so and for any given topology (triangles, quads, tetrahedra or hexahedra), the MeshMatrixMass integrates the mass density inside each elements and sums the mass matrix $$\mathbf{M}$$ in the system matrix $$\mathbf{A}$$.


### Volume integration

As detailed in the [Physics integration](../../simulation-principles/multi-model-representation/physics-integration/) page, the left hand side part of the linear momentum conservation equals $$\rho\dot{v}$$. To integrate over the domain, its weak form will result in the mass matrix:

$$\mathbf{M}\dot{v}=\int_{\Omega} \phi_j \rho \dot{v}d\Omega$$

where $$\phi_j$$ are the test functions, which are basis functions ensuring the existence of a solution. Since no exact integration can be performed on a random domain $$\Omega$$, the MeshMatrixMass relies on the Finite Element Method (FEM) and accumulates the result of the integral over each finite element (triangles, quads, tetrahedra or hexahedra):

$$\mathbf{M}\dot{v}=\sum_{e=0}^E \int_{V_e} \phi_j \rho \dot{v}dV_e$$

The FEM relies on simple geometries in which any field can be interpolated using shape functions $$\phi_i$$ (see [FEM at a glance](../../simulation-principles/multi-model-representation/physics-integration/#fem-at-a-glance)). Note that the same basis functions are chosen for both the test and the shape functions. The interpolation of the acceleration term $$\dot{v}$$ thus gives:

$$\mathbf{M}\dot{v}=\sum_{e=0}^E \rho \int_{V_e} \phi_j \sum_{i=0}^{N} \phi_i \dot{v}_i dV_e$$

By change of variables, the computation of the mass matrix results in solving the following integration of the shape functions $$\phi$$ in each element:

$$\mathbf{M}\dot{v}=\sum_{e=0}^E \rho \int_{V_e} |det(J)| \sum_{i=0}^{N}\phi_j(\boldsymbol{\xi}) \phi_i(\boldsymbol{\xi}) \dot{v}_i d \boldsymbol{\xi}$$


### Case of a linear tetrahedron
In the case of a linear tetrahedron, the shape functions are:

$$\begin{align*}&\phi_1=1-\xi -\eta -\zeta \\&\phi_2=\xi \\&\phi_3=\eta \\&\phi_4=\zeta \\ \end{align*}$$

By replacing the shape functions, we therefore obtain:

$$\mathbf{M}\dot{v}=\sum_{e=0}^E \rho \int_{V_e} |det(J)| \phi_j \phi_i \dot{v}_i d \boldsymbol{\xi}$$

$$\mathbf{M}\dot{v}=\sum_{e=0}^E \rho \int_{V_e} |det(J)| \begin{bmatrix}\phi_1^2&\phi_1\phi_2&\phi_1\phi_3&\phi_1\phi_4 \\\phi_2\phi_1&\phi_2^2&\phi_2\phi_3&\phi_2\phi_4 \\\phi_3\phi_1&\phi_3\phi_2&\phi_3^2&\phi_3\phi_4 \\\phi_4\phi_1&\phi_4\phi_2&\phi_4\phi_3&\phi_4^2 \\ \end{bmatrix} \begin{bmatrix}\dot{v}_1\\ \dot{v}_2\\ \dot{v}_3\\ \dot{v}_4\\ \end{bmatrix} d \boldsymbol{\xi}$$

$$\mathbf{M}\dot{v}=\sum_{e=0}^E \rho \int_{\xi} \int_{\eta} \int_{\zeta} |det(J)| \begin{bmatrix}(1-\xi -\eta -\zeta)^2&\xi-\xi^2 -\eta\xi -\zeta\xi&\eta-\xi\eta -\eta^2 -\zeta\eta&\zeta-\xi\zeta -\eta\zeta\zeta -\zeta^2 \\\phi_2\phi_1&\xi^2&\xi\eta&\xi\zeta \\\phi_3\phi_1&\phi_3\phi_2&\eta^2&\eta\zeta \\\phi_4\phi_1&\phi_4\phi_2&\phi_4\phi_3&\zeta^2 \\ \end{bmatrix} \begin{bmatrix}\dot{v}_1\\ \dot{v}_2\\ \dot{v}_3\\ \dot{v}_4\\ \end{bmatrix} d\xi d\eta d\zeta$$

We can note that the matrix is symmetric. The integration in the reference (or parent) space $$\boldsymbol{\xi}$$ can be numerically computed using a [Gauss quadrature](https://en.wikipedia.org/wiki/Gaussian_quadrature) (or Gauss point integration). The resulting mass matrix is:

$$\mathbf{M}\dot{v}=\sum_{e=0}^E \frac{\rho V_e}{20}\begin{bmatrix}2&1&1&1\\1&2&1&1\\1&1&2&1\\1&1&1&2\\ \end{bmatrix}\begin{bmatrix}\dot{v}_1\\ \dot{v}_2\\ \dot{v}_3\\ \dot{v}_4\\ \end{bmatrix}$$


### API

Depending on the type of [LinearSolver](../../simulation-principles/system-resolution/linear-solver/) used:

- for iterative solvers, the result of the multiplication between the mass matrix $$\mathbf{M}$$ and an approximated solution is computed by the function:

``` cpp
template <class DataTypes, class MassType>
void MeshMatrixMass<DataTypes, MassType>::addMDx(const core::MechanicalParams*, DataVecDeriv& vres, const DataVecDeriv& vdx, SReal factor)
{
    const MassVector &vertexMass= d_vertexMassInfo.getValue();
    const MassVector &edgeMass= d_edgeMassInfo.getValue();

    helper::WriteAccessor< DataVecDeriv > res = vres;
    helper::ReadAccessor< DataVecDeriv > dx = vdx;

    size_t v0,v1,nbEdges=_topology->getNbEdges();

    for (unsigned int i=0; i<dx.size(); i++)
    {
        res[i] += dx[i] * vertexMass[i] * (Real)factor;
    }

    for (unsigned int j=0; j<nbEdges; ++j)
    {
        v0=_topology->getEdge(j)[0];
        v1=_topology->getEdge(j)[1];

        res[v0] += dx[v1] * edgeMass[j] * (Real)factor;
        res[v1] += dx[v0] * edgeMass[j] * (Real)factor;
    }
}
```

- for direct solvers, the mass matrix $$\mathbf{M}$$ is built by the function:

``` cpp
template <class DataTypes, class MassType>
void MeshMatrixMass<DataTypes, MassType>::addMToMatrix(const core::MechanicalParams *mparams, const sofa::core::behavior::MultiMatrixAccessor* matrix)
{
    const MassVector &vertexMass= d_vertexMassInfo.getValue();
    const MassVector &edgeMass= d_edgeMassInfo.getValue();

    size_t v0,v1,nbEdges=_topology->getNbEdges();

    const int N = defaulttype::DataTypeInfo<Deriv>::size();
    AddMToMatrixFunctor<Deriv,MassType> calc;
    sofa::core::behavior::MultiMatrixAccessor::MatrixRef r = matrix->getMatrix(this->mstate);
    sofa::defaulttype::BaseMatrix* mat = r.matrix;
    Real mFactor = (Real)mparams->mFactorIncludingRayleighDamping(this->rayleighMass.getValue());


    for (size_t i = 0; i < vertexMass.size(); i++)
    {
        calc(r.matrix, vertexMass[i], r.offset + N*i, mFactor);
    }

    for (size_t j = 0; j < nbEdges; ++j)
    {
        v0 = _topology->getEdge(j)[0];
        v1 = _topology->getEdge(j)[1];

        calc(r.matrix, edgeMass[j], r.offset + N*v0, r.offset + N*v1, mFactor);
        calc(r.matrix, edgeMass[j], r.offset + N*v1, r.offset + N*v0, mFactor);
    }
}

```
### Case of mass lumping

Note that using the optional data **lumping**, it is possible to simply the mass matrix by making it diagonal. This is called mass lumping and it consists in summing all mass values of a line on the diagonal. The DiagonalMass is an optimized version of this mass lumping approach. In case of a linear tetrahedron, if the data **lumping** is true, the (lumped) mass matrix becomes:

$$\mathbf{M}\dot{v}=\sum_{e=0}^E \frac{\rho V_e}{4}\begin{bmatrix}1&0&0&0\\&1&0&0\\&0&1&0\\&0&0&1\\ \end{bmatrix}\begin{bmatrix}\dot{v}_1\\ \dot{v}_2\\ \dot{v}_3\\ \dot{v}_4\\ \end{bmatrix}$$

Use lumping with caution since it is a numerical approximation, thus decreasing the accuracy of the integration.



Usage
-----

The MeshMatrixMass **requires** a MechanicalObject to store the degrees of freedom associated to the nodes, as well as a Topology. An integration scheme and a solver are also necessary to solve the linear system at each time step.

Several topologies are handled by the MeshMatrixMass, namely: triangles, quads, tetrahedra or hexahedra. Only the beam model (edge topology) is not handled by this component.
<!-- automatically generated doc START -->
__Target__: `Sofa.Component.Mass`

__namespace__: `#!c++ sofa::component::mass`

__parents__: 

- `#!c++ Mass`

__categories__: 

- Mass

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
		<td>separateGravity</td>
		<td>
add separately gravity to velocity computation
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>rayleighMass</td>
		<td>
Rayleigh damping - mass matrix coefficient
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>massDensity</td>
		<td>
Specify real and strictly positive value(s) for the mass density. 
If unspecified or wrongly set, the totalMass information is used.
</td>
		<td></td>
	</tr>
	<tr>
		<td>totalMass</td>
		<td>
Specify the total mass resulting from all particles. 
If unspecified or wrongly set, the default value is used: totalMass = 1.0
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>vertexMass</td>
		<td>
internal values of the particles masses on vertices, supporting topological changes
</td>
		<td></td>
	</tr>
	<tr>
		<td>edgeMass</td>
		<td>
internal values of the particles masses on edges, supporting topological changes
</td>
		<td></td>
	</tr>
	<tr>
		<td>computeMassOnRest</td>
		<td>
If true, the mass of every element is computed based on the rest position rather than the position
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>lumping</td>
		<td>
If true, the mass matrix is lumped, meaning the mass matrix becomes diagonal (summing all mass values of a line on the diagonal)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>printMass</td>
		<td>
boolean if you want to check the mass conservation
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>graph</td>
		<td>
Graph of the controlled potential
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showGravityCenter</td>
		<td>
display the center of gravity of the system
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showAxisSizeFactor</td>
		<td>
factor length of the axis displayed (only used for rigids)
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
|geometryState|link to the MechanicalObject associated with the geometry|



## Examples

Component/Mass/MeshMatrixMass.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.005">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [SphereCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader MeshOBJLoader SphereLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [MeshMatrixMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedralCorotationalFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <DefaultAnimationLoop/>
        <CollisionPipeline verbose="0" name="CollisionPipeline" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" name="collision response" />
        <DiscreteIntersection />
    
        <MeshGmshLoader name="MeshLoader" filename="mesh/liver.msh" />
        <MeshOBJLoader name="LiverSurface" filename="mesh/liver-smooth.obj" />
    
        <Node name="Liver">
            <EulerImplicitSolver name="integration scheme" />
            <CGLinearSolver name="linear solver" iterations="1000" tolerance="1e-9" threshold="1e-9"/>
            <MechanicalObject name="dofs" src="@../MeshLoader"/>
            <!-- Container for the tetrahedra-->
            <TetrahedronSetTopologyContainer name="TetraTopo" src="@../MeshLoader"/>
            <TetrahedronSetGeometryAlgorithms name="GeomAlgo" />
            <MeshMatrixMass totalMass="60" name="SparseMass" topology="@TetraTopo" />
            <TetrahedralCorotationalFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.45" youngModulus="5000" />
            <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="3 39 64" />
    
            <Node name="Visu" >
                <OglModel  name="VisualModel" src="@../../LiverSurface" color="cyan"/>
                <BarycentricMapping name="VisualMapping" input="@../dofs" output="@VisualModel" />
            </Node>
            <Node name="Surf" >
                <SphereLoader filename="mesh/liver.sph" />
                <MechanicalObject name="spheres" position="@[-1].position" />
                <SphereCollisionModel name="CollisionModel" listRadius="@[-2].listRadius"/>
                <BarycentricMapping name="CollisionMapping" input="@../dofs" output="@spheres" />
            </Node>
    
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.005")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
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
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
        root.addObject('DefaultAnimationLoop')
        root.addObject('CollisionPipeline', verbose="0", name="CollisionPipeline")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField", name="collision response")
        root.addObject('DiscreteIntersection')
        root.addObject('MeshGmshLoader', name="MeshLoader", filename="mesh/liver.msh")
        root.addObject('MeshOBJLoader', name="LiverSurface", filename="mesh/liver-smooth.obj")

        Liver = root.addChild('Liver')
        Liver.addObject('EulerImplicitSolver', name="integration scheme")
        Liver.addObject('CGLinearSolver', name="linear solver", iterations="1000", tolerance="1e-9", threshold="1e-9")
        Liver.addObject('MechanicalObject', name="dofs", src="@../MeshLoader")
        Liver.addObject('TetrahedronSetTopologyContainer', name="TetraTopo", src="@../MeshLoader")
        Liver.addObject('TetrahedronSetGeometryAlgorithms', name="GeomAlgo")
        Liver.addObject('MeshMatrixMass', totalMass="60", name="SparseMass", topology="@TetraTopo")
        Liver.addObject('TetrahedralCorotationalFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.45", youngModulus="5000")
        Liver.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="3 39 64")

        Visu = Liver.addChild('Visu')
        Visu.addObject('OglModel', name="VisualModel", src="@../../LiverSurface", color="cyan")
        Visu.addObject('BarycentricMapping', name="VisualMapping", input="@../dofs", output="@VisualModel")

        Surf = Liver.addChild('Surf')
        Surf.addObject('SphereLoader', filename="mesh/liver.sph")
        Surf.addObject('MechanicalObject', name="spheres", position="@[-1].position")
        Surf.addObject('SphereCollisionModel', name="CollisionModel", listRadius="@[-2].listRadius")
        Surf.addObject('BarycentricMapping', name="CollisionMapping", input="@../dofs", output="@spheres")
    ```


<!-- automatically generated doc END -->
