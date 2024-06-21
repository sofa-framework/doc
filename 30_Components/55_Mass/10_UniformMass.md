---
title: UniformMass
---

UniformMass  
===========


This component belongs to the category of [Masses](https://www.sofa-framework.org/community/doc/main-principles/multi-model-representation/mass/). The UniformMass is a very **simplistic mass** component since it does not compute the volume integration of a density term. The mass is equally spread over the number of points, thus resulting in the following diagonal mass matrix:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}=\begin{bmatrix}m&0&\cdots&0\\%30&m&\cdots&0\\%20\vdots&\vdots&\ddots&\vdots\\%30&0&\cdots&m\end{bmatrix}" title="UniformMass M" />

Each diagonal term equals the nodal mass <img class="latex" src="https://latex.codecogs.com/png.latex?m=\frac{m_{\textnormal{total}}}{N}" title="Nodal mass" /> where <img class="latex" src="https://latex.codecogs.com/png.latex?m_{\textnormal{total}}" title="Total mass" /> is the total mass of the objet and <img class="latex" src="https://latex.codecogs.com/png.latex?N" title="Number of nodes" /> is the number of nodes of the object. Spreading the mass over the nodes without considering their connectivity results in this diagonal mass matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}" title="UniformMass M" />.


As all mass components, the UniformMass <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}" title="Mass matrix" /> will contribute to the main matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> in the system <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="Linear system" />. Depending on the type of [LinearSolver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/linear-solvers/) used:

- for iterative solvers, the result of the multiplication between the mass matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}" title="Mass matrix" /> and an approximated solution is computed by the function:

``` cpp
template <class DataTypes, class MassType>
void UniformMass<DataTypes, MassType>::addMDx ( const core::MechanicalParams*, DataVecDeriv& vres, const DataVecDeriv& vdx, SReal factor)
{
    helper::WriteAccessor<DataVecDeriv> res = vres;
    helper::ReadAccessor<DataVecDeriv> dx = vdx;

    WriteAccessor<Data<vector<int> > > indices = d_indices;

    MassType m = d_vertexMass.getValue();
    if ( factor != 1.0 )
        m *= ( typename DataTypes::Real ) factor;

    for ( unsigned int i=0; i<indices.size(); i++ )
        res[indices[i]] += dx[indices[i]] * m;
}
```

- for direct solvers, the mass matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{M}" title="Mass matrix" /> is built by the function:

``` cpp
/// Add Mass contribution to global Matrix assembling
template <class DataTypes, class MassType>
void UniformMass<DataTypes, MassType>::addMToMatrix (const MechanicalParams *mparams, const MultiMatrixAccessor* matrix)
{
    const MassType& m = d_vertexMass.getValue();

    const size_t N = DataTypeInfo<Deriv>::size();

    AddMToMatrixFunctor<Deriv,MassType> calc;
    MultiMatrixAccessor::MatrixRef r = matrix->getMatrix(mstate);

    Real mFactor = (Real)mparams->mFactorIncludingRayleighDamping(this->rayleighMass.getValue());

    ReadAccessor<Data<vector<int> > > indices = d_indices;
    for ( unsigned int i=0; i<indices.size(); i++ )
        calc ( r.matrix, m, r.offset + N*indices[i], mFactor);
}
```



Data
----

Since the UniformMass equally spread the total mass <img class="latex" src="https://latex.codecogs.com/png.latex?m_{\textnormal{total}}" title="Total mass" /> over all the nodes of the object, the component can be initialized using:

- either the **vertexMass** data: corresponding to the nodal mass <img class="latex" src="https://latex.codecogs.com/png.latex?m=\frac{m_{\textnormal{total}}}{N}" title="Nodal mass" />, set equally at each node
- or the **totalMass** data: corresponding to the total mass <img class="latex" src="https://latex.codecogs.com/png.latex?m_{\textnormal{total}}" title="Total mass" /> of the object


Usage
-----

The UniformMass only **requires** a MechanicalObject to store the degrees of freedom associated to the nodes. An integration scheme and a solver are also necessary to solve the linear system at each time step.

Since the UniformMass only set a constant mass at each node without considering their connectivity, no topology is needed for the UniformMass. For this reason, the UniformMass is suitable for rigid frames.

However, the UniformMass should be carefully used if accuracy is a criterion, especially when using surface or volumetric physical models. As written above, the UniformMass does not take into account the geometry and the topology of the object since no space integration is computed.


Example
-------

This component is used as follows in XML format:

``` xml
<UniformMass totalMass="10" />
```

or using SofaPython3:

``` python
node.addObject('UniformMass', totalMass='10')
```

An example scene involving a UniformMass is available in [*examples/Component/Mass/UniformMass.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/Mass/UniformMass.scn)
<!-- automatically generated doc START -->
__Target__: `Sofa.Component.Mass`

__namespace__: `#!c++ sofa::component::mass`

__parents__: 

- `#!c++ Mass`

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
Specify one single, positive, real value for the mass of each particle. 
If unspecified or wrongly set, the totalMass information is used.
</td>
		<td>1 1 1</td>
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
		<td>filename</td>
		<td>
File storing the mass parameters [rigid objects only].
</td>
		<td></td>
	</tr>
	<tr>
		<td>compute_mapping_inertia</td>
		<td>
to be used if the mass is placed under a mapping
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>localRange</td>
		<td>
optional range of local DOF indices. 
Any computation involving only indices outside of this range 
are discarded (useful for parallelization using mesh partitionning)
</td>
		<td>-1 -1</td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
optional local DOF indices. Any computation involving only indices outside of this list are discarded
</td>
		<td></td>
	</tr>
	<tr>
		<td>preserveTotalMass</td>
		<td>
Prevent totalMass from decreasing when removing particles.
</td>
		<td>0</td>
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
	<tr>
		<td>showInitialCenterOfGravity</td>
		<td>
display the initial center of gravity of the system
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showX0</td>
		<td>
display the rest positions
</td>
		<td>0</td>
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



__Templates__:

- `#!c++ Rigid3d`

__Target__: `Sofa.Component.Mass`

__namespace__: `#!c++ sofa::component::mass`

__parents__: 

- `#!c++ Mass`

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
Specify one single, positive, real value for the mass of each particle. 
If unspecified or wrongly set, the totalMass information is used.
</td>
		<td>1 1 [1 0 0,0 1 0,0 0 1]</td>
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
		<td>filename</td>
		<td>
rigid file to load the mass parameters
</td>
		<td></td>
	</tr>
	<tr>
		<td>compute_mapping_inertia</td>
		<td>
to be used if the mass is placed under a mapping
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>localRange</td>
		<td>
optional range of local DOF indices. 
Any computation involving only indices outside of this range 
are discarded (useful for parallelization using mesh partitionning)
</td>
		<td>-1 -1</td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
optional local DOF indices. Any computation involving only indices outside of this list are discarded
</td>
		<td></td>
	</tr>
	<tr>
		<td>preserveTotalMass</td>
		<td>
Prevent totalMass from decreasing when removing particles.
</td>
		<td>0</td>
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
	<tr>
		<td>showInitialCenterOfGravity</td>
		<td>
display the initial center of gravity of the system
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showX0</td>
		<td>
display the rest positions
</td>
		<td>0</td>
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



__Templates__:

- `#!c++ Vec1d`
- `#!c++ Vec2d`
- `#!c++ Vec3d`
- `#!c++ Vec6d`

__Target__: `Sofa.Component.Mass`

__namespace__: `#!c++ sofa::component::mass`

__parents__: 

- `#!c++ Mass`

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
Specify one single, positive, real value for the mass of each particle. 
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
		<td>filename</td>
		<td>
File storing the mass parameters [rigid objects only].
</td>
		<td></td>
	</tr>
	<tr>
		<td>compute_mapping_inertia</td>
		<td>
to be used if the mass is placed under a mapping
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>localRange</td>
		<td>
optional range of local DOF indices. 
Any computation involving only indices outside of this range 
are discarded (useful for parallelization using mesh partitionning)
</td>
		<td>-1 -1</td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
optional local DOF indices. Any computation involving only indices outside of this list are discarded
</td>
		<td></td>
	</tr>
	<tr>
		<td>preserveTotalMass</td>
		<td>
Prevent totalMass from decreasing when removing particles.
</td>
		<td>0</td>
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
	<tr>
		<td>showInitialCenterOfGravity</td>
		<td>
display the initial center of gravity of the system
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showX0</td>
		<td>
display the rest positions
</td>
		<td>0</td>
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

Component/Mass/UniformMass.scn

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
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
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
            <UniformMass totalMass="60"  name="uniformlyConstantMass" />
            <TetrahedralCorotationalFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.45" youngModulus="5000" />
            <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="3 39 64" />
            
            <Node name="Visu">
                <OglModel name="VisualModel" src="@../../meshLoader_0" color="yellow" />
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
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('CollisionPipeline', verbose="0", name="CollisionPipeline")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField", name="collision response")
        root.addObject('DiscreteIntersection')
        root.addObject('DefaultAnimationLoop')
        root.addObject('MeshGmshLoader', name="loader", filename="mesh/liver.msh")
        root.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/liver-smooth.obj", handleSeams="1")

        Liver = root.addChild('Liver', depend="topo dofs")
        Liver.addObject('EulerImplicitSolver', name="integration scheme")
        Liver.addObject('CGLinearSolver', name="linear solver", iterations="1000", tolerance="1e-9", threshold="1e-9")
        Liver.addObject('MechanicalObject', name="dofs", src="@../loader")
        Liver.addObject('TetrahedronSetTopologyContainer', name="TetraTopo", src="@../loader")
        Liver.addObject('TetrahedronSetGeometryAlgorithms', name="GeomAlgo")
        Liver.addObject('UniformMass', totalMass="60", name="uniformlyConstantMass")
        Liver.addObject('TetrahedralCorotationalFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.45", youngModulus="5000")
        Liver.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="3 39 64")

        Visu = Liver.addChild('Visu')
        Visu.addObject('OglModel', name="VisualModel", src="@../../meshLoader_0", color="yellow")
        Visu.addObject('BarycentricMapping', name="VisualMapping", input="@../dofs", output="@VisualModel")

        Surf = Liver.addChild('Surf')
        Surf.addObject('SphereLoader', filename="mesh/liver.sph")
        Surf.addObject('MechanicalObject', name="spheres", position="@[-1].position")
        Surf.addObject('SphereCollisionModel', name="CollisionModel", listRadius="@[-2].listRadius")
        Surf.addObject('BarycentricMapping', name="CollisionMapping", input="@../dofs", output="@spheres")
    ```


<!-- automatically generated doc END -->
