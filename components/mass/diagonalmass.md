---
title: DiagonalMass
---

DiagonalMass  
============

This component belongs to the category of [Masses](../../../simulation-principles/multi-model-representation/mass/). In the dynamic equation (see [Physics integration](../../../simulation-principles/multi-model-representation/physics-integration/) page), the mass density results from the first derivative in time of the momentum term. Like the MeshMatrixMass, the DiagonalMass computes the integral of this mass density over the volume of the object geometry. To do so and for any given topology (edges, triangles, quads, tetrahedra or hexahedra), the DiagonalMass integrates the mass density inside each elements and sums the mass matrix $\mathbf{M}$ in the system matrix $\mathbf{A}$.

However, the DiagonalMass makes a strong simplification: it considers the mass matrix $\mathbf{M}$ as being diagonal. To build this diagonal mass matrix, the DiagonalMass relies on a numerical method called the mass lumping. It consists in summing all mass values of a line on the diagonal. This approach is already implemented in the MeshMatrixMass but the DiagonalMass proposes an optimized version of the mass lumping and extend it to edge topology.

For details on the volume integration, please report to the [MeshMatrixMass](./../meshmatrixmass/) page. As demonstrated in the [MeshMatrixMass](./../meshmatrixmass/#case-of-a-linear-tetrahedron) page, in case of a topology using linear tetrahedra, the diagonal mass matrix corresponds to:


$$
\mathbf{M}\dot{v}=\sum_{e=0}^E \frac{\rho V_e}{4}\begin{bmatrix}1&0&0&0\\&1&0&0\\&0&1&0\\&0&0&1\\ \end{bmatrix}\begin{bmatrix}\dot{v}_1\\ \dot{v}_2\\ \dot{v}_3\\ \dot{v}_4\\ \end{bmatrix}
$$


By making the matrix diagonal (i.e. removing extra-diagonal terms), the lumping method removes the connectivity (neighborhood) information from the matrix. Due to this numerical approximation, the accuracy of the integration is decreased compared to the MeshMatrixMass integration. It is therefore advised to use the DiagonalMass carefully.




### API

Depending on the type of [LinearSolver](../../../simulation-principles/system-resolution/linear-solver/) used:

- for iterative solvers, the result of the multiplication between the mass matrix $\mathbf{M}$ and an approximated solution is computed by the function:

``` cpp
template <class DataTypes, class MassType>
void DiagonalMass<DataTypes, MassType>::addMDx(const core::MechanicalParams* /*mparams*/, DataVecDeriv& res, const DataVecDeriv& dx, SReal factor)
{
    const MassVector &masses= d_vertexMass.getValue();
    helper::WriteAccessor< DataVecDeriv > _res = res;
    helper::ReadAccessor< DataVecDeriv > _dx = dx;

    size_t n = masses.size();

    for (size_t i=0; i<n; i++)
    {
        _res[i] += (_dx[i] * masses[i]) * (Real)factor;
    }
}
```

- for direct solvers, the mass matrix $\mathbf{M}$ is built by the function:

``` cpp
template <class DataTypes, class MassType>
void DiagonalMass<DataTypes, MassType>::addMToMatrix(const core::MechanicalParams *mparams, const sofa::core::behavior::MultiMatrixAccessor* matrix)
{
    const MassVector &masses= d_vertexMass.getValue();
    const int N = defaulttype::DataTypeInfo<Deriv>::size();
    AddMToMatrixFunctor<Deriv,MassType> calc;
    sofa::core::behavior::MultiMatrixAccessor::MatrixRef r = matrix->getMatrix(this->mstate);
    Real mFactor = (Real)mparams->mFactorIncludingRayleighDamping(this->rayleighMass.getValue());
    for (unsigned int i=0; i<masses.size(); i++)
        calc(r.matrix, masses[i], r.offset + N*i, mFactor);
}
```


Usage
-----

The DiagonalMass **requires** a MechanicalObject to store the degrees of freedom associated to the nodes, as well as a Topology. An integration scheme and a solver are also necessary to solve the linear system at each time step.

All topologies are handled by the DiagonalMass, namely: edges, triangles, quads, tetrahedra or hexahedra.
<!-- automatically generated doc START -->
<!-- generate_doc -->

Define a specific mass for each particle


## Rigid2d,Rigid2d

Templates:

- Rigid2d,Rigid2d

__Target__: Sofa.Component.Mass

__namespace__: sofa::component::mass

__parents__:

- Mass

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
		<td>vertexMass</td>
		<td>
Specify a vector giving the mass of each vertex. 
If unspecified or wrongly set, the massDensity or totalMass information is used.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>massDensity</td>
		<td>
Specify one single real and positive value for the mass density. 
If unspecified or wrongly set, the totalMass information is used.
		</td>
		<td>1</td>
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
		<td>computeMassOnRest</td>
		<td>
If true, the mass of every element is computed based on the rest position rather than the position
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>filename</td>
		<td>
Xsp3.0 file to specify the mass parameters
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showGravityCenter</td>
		<td>
Display the center of gravity of the system
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showAxisSizeFactor</td>
		<td>
Factor length of the axis displayed (only used for rigids)
		</td>
		<td>1</td>
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Rigid2d&gt;|
|topology|link to the topology container|BaseMeshTopology|
|geometryState|link to the MechanicalObject associated with the geometry|MechanicalState&lt;Rigid2d&gt;|

<!-- generate_doc -->
## Rigid2d,Rigid3d

Templates:

- Rigid2d,Rigid3d

__Target__: Sofa.Component.Mass

__namespace__: sofa::component::mass

__parents__:

- Mass

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
		<td>vertexMass</td>
		<td>
Specify a vector giving the mass of each vertex. 
If unspecified or wrongly set, the massDensity or totalMass information is used.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>massDensity</td>
		<td>
Specify one single real and positive value for the mass density. 
If unspecified or wrongly set, the totalMass information is used.
		</td>
		<td>1</td>
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
		<td>computeMassOnRest</td>
		<td>
If true, the mass of every element is computed based on the rest position rather than the position
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>filename</td>
		<td>
Xsp3.0 file to specify the mass parameters
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showGravityCenter</td>
		<td>
Display the center of gravity of the system
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showAxisSizeFactor</td>
		<td>
Factor length of the axis displayed (only used for rigids)
		</td>
		<td>1</td>
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Rigid2d&gt;|
|topology|link to the topology container|BaseMeshTopology|
|geometryState|link to the MechanicalObject associated with the geometry|MechanicalState&lt;Rigid3d&gt;|

<!-- generate_doc -->
## Rigid3d,Rigid3d

Templates:

- Rigid3d,Rigid3d

__Target__: Sofa.Component.Mass

__namespace__: sofa::component::mass

__parents__:

- Mass

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
		<td>vertexMass</td>
		<td>
Specify a vector giving the mass of each vertex. 
If unspecified or wrongly set, the massDensity or totalMass information is used.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>massDensity</td>
		<td>
Specify one single real and positive value for the mass density. 
If unspecified or wrongly set, the totalMass information is used.
		</td>
		<td>1</td>
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
		<td>computeMassOnRest</td>
		<td>
If true, the mass of every element is computed based on the rest position rather than the position
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>filename</td>
		<td>
Xsp3.0 file to specify the mass parameters
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showGravityCenter</td>
		<td>
Display the center of gravity of the system
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showAxisSizeFactor</td>
		<td>
Factor length of the axis displayed (only used for rigids)
		</td>
		<td>1</td>
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Rigid3d&gt;|
|topology|link to the topology container|BaseMeshTopology|
|geometryState|link to the MechanicalObject associated with the geometry|MechanicalState&lt;Rigid3d&gt;|

<!-- generate_doc -->
## Vec1d,Vec1d

Templates:

- Vec1d,Vec1d

__Target__: Sofa.Component.Mass

__namespace__: sofa::component::mass

__parents__:

- Mass

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
		<td>vertexMass</td>
		<td>
Specify a vector giving the mass of each vertex. 
If unspecified or wrongly set, the massDensity or totalMass information is used.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>massDensity</td>
		<td>
Specify one single real and positive value for the mass density. 
If unspecified or wrongly set, the totalMass information is used.
		</td>
		<td>1</td>
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
		<td>computeMassOnRest</td>
		<td>
If true, the mass of every element is computed based on the rest position rather than the position
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>filename</td>
		<td>
Xsp3.0 file to specify the mass parameters
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showGravityCenter</td>
		<td>
Display the center of gravity of the system
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showAxisSizeFactor</td>
		<td>
Factor length of the axis displayed (only used for rigids)
		</td>
		<td>1</td>
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec1d&gt;|
|topology|link to the topology container|BaseMeshTopology|
|geometryState|link to the MechanicalObject associated with the geometry|MechanicalState&lt;Vec1d&gt;|

<!-- generate_doc -->
## Vec1d,Vec2d

Templates:

- Vec1d,Vec2d

__Target__: Sofa.Component.Mass

__namespace__: sofa::component::mass

__parents__:

- Mass

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
		<td>vertexMass</td>
		<td>
Specify a vector giving the mass of each vertex. 
If unspecified or wrongly set, the massDensity or totalMass information is used.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>massDensity</td>
		<td>
Specify one single real and positive value for the mass density. 
If unspecified or wrongly set, the totalMass information is used.
		</td>
		<td>1</td>
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
		<td>computeMassOnRest</td>
		<td>
If true, the mass of every element is computed based on the rest position rather than the position
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>filename</td>
		<td>
Xsp3.0 file to specify the mass parameters
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showGravityCenter</td>
		<td>
Display the center of gravity of the system
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showAxisSizeFactor</td>
		<td>
Factor length of the axis displayed (only used for rigids)
		</td>
		<td>1</td>
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec1d&gt;|
|topology|link to the topology container|BaseMeshTopology|
|geometryState|link to the MechanicalObject associated with the geometry|MechanicalState&lt;Vec2d&gt;|

<!-- generate_doc -->
## Vec1d,Vec3d

Templates:

- Vec1d,Vec3d

__Target__: Sofa.Component.Mass

__namespace__: sofa::component::mass

__parents__:

- Mass

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
		<td>vertexMass</td>
		<td>
Specify a vector giving the mass of each vertex. 
If unspecified or wrongly set, the massDensity or totalMass information is used.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>massDensity</td>
		<td>
Specify one single real and positive value for the mass density. 
If unspecified or wrongly set, the totalMass information is used.
		</td>
		<td>1</td>
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
		<td>computeMassOnRest</td>
		<td>
If true, the mass of every element is computed based on the rest position rather than the position
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>filename</td>
		<td>
Xsp3.0 file to specify the mass parameters
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showGravityCenter</td>
		<td>
Display the center of gravity of the system
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showAxisSizeFactor</td>
		<td>
Factor length of the axis displayed (only used for rigids)
		</td>
		<td>1</td>
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec1d&gt;|
|topology|link to the topology container|BaseMeshTopology|
|geometryState|link to the MechanicalObject associated with the geometry|MechanicalState&lt;Vec3d&gt;|

<!-- generate_doc -->
## Vec2d,Vec3d

Templates:

- Vec2d,Vec3d

__Target__: Sofa.Component.Mass

__namespace__: sofa::component::mass

__parents__:

- Mass

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
		<td>vertexMass</td>
		<td>
Specify a vector giving the mass of each vertex. 
If unspecified or wrongly set, the massDensity or totalMass information is used.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>massDensity</td>
		<td>
Specify one single real and positive value for the mass density. 
If unspecified or wrongly set, the totalMass information is used.
		</td>
		<td>1</td>
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
		<td>computeMassOnRest</td>
		<td>
If true, the mass of every element is computed based on the rest position rather than the position
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>filename</td>
		<td>
Xsp3.0 file to specify the mass parameters
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showGravityCenter</td>
		<td>
Display the center of gravity of the system
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showAxisSizeFactor</td>
		<td>
Factor length of the axis displayed (only used for rigids)
		</td>
		<td>1</td>
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec2d&gt;|
|topology|link to the topology container|BaseMeshTopology|
|geometryState|link to the MechanicalObject associated with the geometry|MechanicalState&lt;Vec3d&gt;|

<!-- generate_doc -->
## Vec3d,Vec3d

Templates:

- Vec3d,Vec3d

__Target__: Sofa.Component.Mass

__namespace__: sofa::component::mass

__parents__:

- Mass

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
		<td>vertexMass</td>
		<td>
Specify a vector giving the mass of each vertex. 
If unspecified or wrongly set, the massDensity or totalMass information is used.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>massDensity</td>
		<td>
Specify one single real and positive value for the mass density. 
If unspecified or wrongly set, the totalMass information is used.
		</td>
		<td>1</td>
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
		<td>computeMassOnRest</td>
		<td>
If true, the mass of every element is computed based on the rest position rather than the position
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>filename</td>
		<td>
Xsp3.0 file to specify the mass parameters
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showGravityCenter</td>
		<td>
Display the center of gravity of the system
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showAxisSizeFactor</td>
		<td>
Factor length of the axis displayed (only used for rigids)
		</td>
		<td>1</td>
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
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|
|topology|link to the topology container|BaseMeshTopology|
|geometryState|link to the MechanicalObject associated with the geometry|MechanicalState&lt;Vec3d&gt;|

## Examples 

DiagonalMass.scn

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
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedralCorotationalFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <CollisionPipeline verbose="0" name="CollisionPipeline" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" name="collision response" />
        <DiscreteIntersection />
        <DefaultAnimationLoop/>
    
        <MeshGmshLoader name="loader" filename="mesh/liver.msh" />
        <MeshOBJLoader name="meshLoader_0" filename="mesh/liver-smooth.obj" handleSeams="1" />
    
        <Node name="Liver" depend="topo dofs">
            <EulerImplicitSolver name="integration scheme" />
            <CGLinearSolver name="linear solver" iterations="1000" tolerance="1e-9" threshold="1e-9"/>
            <MechanicalObject name="dofs" src="@../loader" />
            <!-- Container for the tetrahedra-->
            <TetrahedronSetTopologyContainer name="TetraTopo" src="@../loader" />
            <TetrahedronSetGeometryAlgorithms name="GeomAlgo" />
            <DiagonalMass totalMass="60" name="diagonalMass" />
            <TetrahedralCorotationalFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.45" youngModulus="5000" />
            <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="3 39 64" />
            
            <Node name="Visu">
                <OglModel name="VisualModel" src="@../../meshLoader_0" color="red" />
                <BarycentricMapping name="VisualMapping" input="@../dofs" output="@VisualModel" />
            </Node>
            <Node name="Surf">
        	    <SphereLoader filename="mesh/liver.sph" />
                <MechanicalObject name="spheres" position="@[-1].position" />
                <SphereCollisionModel name="CollisionModel" listRadius="@[-2].listRadius" />
                <BarycentricMapping name="CollisionMapping" input="@../dofs" output="@spheres" />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.005")

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
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('CollisionPipeline', verbose="0", name="CollisionPipeline")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', response="PenalityContactForceField", name="collision response")
       root.addObject('DiscreteIntersection', )
       root.addObject('DefaultAnimationLoop', )
       root.addObject('MeshGmshLoader', name="loader", filename="mesh/liver.msh")
       root.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/liver-smooth.obj", handleSeams="1")

       liver = root.addChild('Liver', depend="topo dofs")

       liver.addObject('EulerImplicitSolver', name="integration scheme")
       liver.addObject('CGLinearSolver', name="linear solver", iterations="1000", tolerance="1e-9", threshold="1e-9")
       liver.addObject('MechanicalObject', name="dofs", src="@../loader")
       liver.addObject('TetrahedronSetTopologyContainer', name="TetraTopo", src="@../loader")
       liver.addObject('TetrahedronSetGeometryAlgorithms', name="GeomAlgo")
       liver.addObject('DiagonalMass', totalMass="60", name="diagonalMass")
       liver.addObject('TetrahedralCorotationalFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.45", youngModulus="5000")
       liver.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="3 39 64")

       visu = Liver.addChild('Visu')

       visu.addObject('OglModel', name="VisualModel", src="@../../meshLoader_0", color="red")
       visu.addObject('BarycentricMapping', name="VisualMapping", input="@../dofs", output="@VisualModel")

       surf = Liver.addChild('Surf')

       surf.addObject('SphereLoader', filename="mesh/liver.sph")
       surf.addObject('MechanicalObject', name="spheres", position="@[-1].position")
       surf.addObject('SphereCollisionModel', name="CollisionModel", listRadius="@[-2].listRadius")
       surf.addObject('BarycentricMapping', name="CollisionMapping", input="@../dofs", output="@spheres")
    ```


<!-- automatically generated doc END -->