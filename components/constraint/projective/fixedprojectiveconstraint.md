---
title: FixedProjectiveConstraint
---

FixedProjectiveConstraint
=========================

This component belongs to the category of [Projective Constraint](../../../simulation-principles/constraint/projective-constraint/).
The FixedProjectiveConstraint projects a constant velocity.  If the fixed points have a zero velocity at the simulation start, they will keep a zero velocity i.e. be fixed.

As introduced in the page about the Projective Constraint, the FixedProjectiveConstraint corresponds to a projection matrix noted $$\mathbf{P}$$ which will multiply the system matrix $$\mathbf{A}$$ so that: $$\mathbf{P}^T\mathbf{A}\mathbf{P}\Deltav=\mathbf{P}^Tb$$. This projection matrix $$\mathbf{P}$$ is the identity matrix in which the diagonal value corresponding to the indices of the fixed points equals zero. These lines and columns equals 0. As a consequence, when the integration scheme (ODESolver) will call the ```projectResponse()``` or ```projectVelocity()``` the constraint will be applied, ensuring that the desired degrees of freedom remain fixed.

Example of a system of size 6, with a fixed constraint at the index 5:

$$\mathbf{P}=\begin{bmatrix}1&0&0&0&0&0\\0&1&0&0&0&0\\0&0&1&0&0&0\\0&0&0&1&0&0\\0&0&0&0&\mathbf{0}&0\\0&0&0&0&0&1\end{bmatrix}$$

By projecting this $$\mathbf{P}$$ matrix on the right hand side vector we have $$\mathbf{P}^Tb$$. This ensures to have the projection $$b[5]=0$$, thus preventing any time evolution of the fifth degree of freedom. In such case, we function _projectResponse()_:

```cpp
template <class DataTypes>
void FixedProjectiveConstraint<DataTypes>::projectResponse(const core::MechanicalParams* mparams, DataVecDeriv& resData)
{
    SOFA_UNUSED(mparams);

    helper::WriteAccessor<DataVecDeriv> res (resData );
    const SetIndexArray & indices = d_indices.getValue();

    if( d_fixAll.getValue() )
    {
        // fix everything
        typename VecDeriv::iterator it;
        for( it = res.begin(); it != res.end(); ++it )
        {
            *it = Deriv();
        }
    }
    else
    {
        for (SetIndexArray::const_iterator it = indices.begin(); it != indices.end(); ++it)
        {
            res[*it] = Deriv();
        }
    }
}
```



Usage
-----

The FixedProjectiveConstraint **requires** a MechanicalObject to store the degrees of freedom associated to the nodes, as well as a Mass so that the system matrix is not null. An integration scheme and a solver are also necessary to solve the linear system at each time step.

Note that if only a part of the degrees of freedom must be constraint, you can use the PartialFixedProjectiveConstraint working in the same way as the FixedProjectiveConstraint.

<!-- automatically generated doc START -->
__Target__: `Sofa.Component.Constraint.Projective`

__namespace__: `#!c++ sofa::component::constraint::projective`

__parents__: 

- `#!c++ ProjectiveConstraintSet`

__categories__: 

- ProjectiveConstraintSet

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
		<td>group</td>
		<td>
ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>endTime</td>
		<td>
The constraint stops acting after the given value.
Use a negative value for infinite constraints
</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
Indices of the fixed points
</td>
		<td></td>
	</tr>
	<tr>
		<td>fixAll</td>
		<td>
filter all the DOF to implement a fixed object
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>activate_projectVelocity</td>
		<td>
if true, projects not only a constant but a zero velocity
</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showObject</td>
		<td>
draw or not the fixed constraints
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>drawSize</td>
		<td>
Size of the rendered particles (0 -&gt; point based rendering, &gt;0 -&gt; radius of spheres)
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

Component/Constraint/Projective/FixedProjectiveConstraint.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.02">
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
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels" />
        <CollisionPipeline verbose="0" name="CollisionPipeline" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" name="collision response" />
        <DiscreteIntersection />
        <Node name="Liver">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshGmshLoader name="loader" filename="mesh/liver.msh" />
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader" name="dofs" />
            <UniformMass name="mass" vertexMass="0.05" />
            <TetrahedronFEMForceField name="FEM" youngModulus="500" poissonRatio="0.3" computeGlobalMatrix="false" method="large" />
            <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="3 39 64" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/liver-smooth.obj" handleSeams="1" />
                <OglModel name="VisualModel" src="@meshLoader_0" color="red" />
                <BarycentricMapping input="@.." output="@VisualModel" name="visual mapping" />
            </Node>
            <Node name="Surf">
    	    <SphereLoader filename="mesh/liver.sph" />
                <MechanicalObject position="@[-1].position" />
                <SphereCollisionModel name="CollisionModel" listRadius="@[-2].listRadius" />
                <BarycentricMapping name="sphere mapping" />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02")
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
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')
        root.addObject('VisualStyle', displayFlags="showBehaviorModels")
        root.addObject('CollisionPipeline', verbose="0", name="CollisionPipeline")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField", name="collision response")
        root.addObject('DiscreteIntersection')

        Liver = root.addChild('Liver')
        Liver.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        Liver.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        Liver.addObject('MeshGmshLoader', name="loader", filename="mesh/liver.msh")
        Liver.addObject('MeshTopology', src="@loader")
        Liver.addObject('MechanicalObject', src="@loader", name="dofs")
        Liver.addObject('UniformMass', name="mass", vertexMass="0.05")
        Liver.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="500", poissonRatio="0.3", computeGlobalMatrix="false", method="large")
        Liver.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="3 39 64")

        Visu = Liver.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/liver-smooth.obj", handleSeams="1")
        Visu.addObject('OglModel', name="VisualModel", src="@meshLoader_0", color="red")
        Visu.addObject('BarycentricMapping', input="@..", output="@VisualModel", name="visual mapping")

        Surf = Liver.addChild('Surf')
        Surf.addObject('SphereLoader', filename="mesh/liver.sph")
        Surf.addObject('MechanicalObject', position="@[-1].position")
        Surf.addObject('SphereCollisionModel', name="CollisionModel", listRadius="@[-2].listRadius")
        Surf.addObject('BarycentricMapping', name="sphere mapping")
    ```


<!-- automatically generated doc END -->
