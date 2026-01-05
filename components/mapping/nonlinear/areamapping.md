# AreaMapping

This component is classified under the category of [Mappings](../../../../simulation-principles/multi-model-representation/mapping/).
It maps each triangle in a topology to a scalar value representing its area.

The inputs of the component are:
- a `State`: it contains the list of coordinates of the triangles vertices
- a `BaseMeshTopology`: it contains the list of triangles, typically defined by indices that reference their vertices.

The output is a `State` where the `position` field is the list of scalar values representing the area of the triangles. These values are output in the same order as the input triangle list, ensuring a direct correlation between each triangle and its corresponding area value.

## Mapping function


Let us define 3 vertices forming a triangle: $P_0$, $P_1$, and $P_2$.

Let us define the vector function $N(x, y, z) = (y - x) \times (z - x)$, where $\times$ is the cross product.

The area of the triangle is computed as:

$$
\text{Area}(P_0, P_1, P_2) = \frac{1}{2} \| N (P_0, P_1, P_2) \|
$$

where $\| \cdot \|$ is the magnitude of a vector.

$n$ is the number of triangles in the topology and $m$ is the number of vertices.

The mapping function of this mapping is $f(x) = (f_0(x), \dots, f_{n-1}(x))$. For $0 \le i < n$:

$$
f_i(x) = \text{Area}(v_{t_{i_0}}, v_{t_{i_1}}, v_{t_{i_2}})
$$

with $t_{i_j}$ is the index of the $j$-th vertex in the $i$-th triangle.
$x \in \mathbb{R}^{3m}$ is the input vector, i.e. the concatenation of all vertices positions.
$v_i$ is the $i$-th vertex position, i.e. $v_i = (x_{3i}, x_{3i+1}, x_{3i+2})$.

## Jacobian Matrix

The Jacobian matrix of this mapping, which represents the first-order partial derivatives of the output with respect to the input, is not constant, and depends on the input.

The elements of the Jacobian matrix $J \in \mathbb{R}^{n \times 3 m}$ are given by:
for $0 \leq i < n, 0 \leq j < 3m$,

$$
J_{ij} = \frac{\partial f_i}{\partial x_j}
$$

Let us compute the $3 \times 1$ sub-matrix $D_{ij}$ such that $j$ is a multiple of 3, and $D_{ij_k} = J_{i,j+k}$ for $0 \leq k < 3$:

$$
D_{ij} =
\begin{cases}
\frac{1}{2  \| N_i \|} l_j \times N_i, & \text{if}\ j \ \text{is a vertex in the triangle}\ i \\
0, & \text{otherwise}
\end{cases}
$$

where $N_i = N(v_{t_{i_0}}, v_{t_{i_1}}, v_{t_{i_1}})$ and $l_i$ is the opposite segment to the vertex $j$ in the triangle $i$.

## Hessian Tensor

The Hessian tensor represents the second-order partial derivatives of the output with respect to the input. For the AreaMapping component, the Hessian tensor is non-zero because the Jacobian matrix depends on the input $x$.

The elements of the Hessian tensor are given by:

$$
H_{ijk} = \frac{\partial J_{ij}(x)}{\partial x_k} 
$$

Let us focus on the triangle $i$, and call U the matrix such that $U_{jk} = H_{ijk}$

$$
U_{jk} =
\begin{cases}
\frac{1}{2  \| N_i \|^3}\left(-(N_i \times l_j) \otimes (N_i \times l_k) + \| N_i \|^2 (l_j \cdot l_k \ I - l_k \otimes l_j + s_{kj} [N]_\times) \right) , & \text{if}\ j \ \text{and}\ k \ \text{are vertices in the triangle}\ i \\
0, & \text{otherwise}
\end{cases}
$$

where $[a]_\times$ refers to the skew-symmetric matrix such that

$$
[a]_\times = 
\begin{bmatrix}
\,\,0&\!-a_3&\,\,\,a_2\\
\,\,\,a_3&0&\!-a_1\\
\!-a_2&\,\,a_1&\,\,0
\end{bmatrix}
$$

$\otimes$ is the outer product, and $s = [(1,1,1)]_\times$
<!-- automatically generated doc START -->
<!-- generate_doc -->

Mapping each triangle in a topology to a scalar value representing its area.


## Vec3d,Vec1d

Templates:

- Vec3d,Vec1d

__Target__: Sofa.Component.Mapping.NonLinear

__namespace__: sofa::component::mapping::nonlinear

__parents__:

- BaseNonLinearMapping

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
list of the subsets the object belongs to
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
		<td>mapForces</td>
		<td>
Are forces mapped ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapConstraints</td>
		<td>
Are constraints mapped ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapMasses</td>
		<td>
Are masses mapped ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapMatrices</td>
		<td>
Are matrix explicit mapped?
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>applyRestPosition</td>
		<td>
set to true to apply this mapping to restPosition at init
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>geometricStiffness</td>
		<td>
Method used to compute the geometric stiffness:
-None: geometric stiffness is not computed
-Exact: the exact geometric stiffness is computed
-Stabilized: the exact geometric stiffness is approximated in order to improve stability
		</td>
		<td>Stabilized</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|input|Input object to map|State&lt;Vec3d&gt;|
|output|Output object to map|State&lt;Vec1d&gt;|
|topology|link to the topology container|BaseMeshTopology|

## Examples 

AreaMapping.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -9.81 0" dt="0.05">
    
        <Node name="plugins">
            <RequiredPlugin name="Sofa.Component.AnimationLoop"/> <!-- Needed to use components [FreeMotionAnimationLoop] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [GenericConstraintCorrection] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Solver"/> <!-- Needed to use components [GenericConstraintSolver] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [EigenSimplicialLDLT] -->
            <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
            <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [AreaMapping] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [MeshMatrixMass] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangleFEMForceField] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [RestShapeSpringsForceField] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetTopologyContainer] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
            <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
            <RequiredPlugin name="Sofa.GL.Component.Rendering2D"/> <!-- Needed to use components [OglColorMap] -->
            <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [DataDisplay OglModel] -->
        </Node>
    
        <FreeMotionAnimationLoop solveVelocityConstraintFirst="true" computeBoundingBox="false" parallelODESolving="true"/>
        <BlockGaussSeidelConstraintSolver tolerance="1e-9" maxIterations="1000"/>
        <VisualStyle displayFlags="showWireframe showBehaviorModels"/>
    
        <RegularGridTopology name="grid" nx="10" ny="10" nz="1" xmin="0" xmax="10" ymin="0" ymax="10" zmin="0" zmax="0" />
        
        <Node name="withAreaConstraints">
            <EulerImplicitSolver name="odeSolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <EigenSimplicialLDLT name="linearSolver" template="CompressedRowSparseMatrixMat3x3d"/>
    
            <TriangleSetTopologyContainer src="@../grid" name="topology"/>
            <MechanicalObject template="Vec3" name="DoFs"/>
            <GenericConstraintCorrection />
    
            <MeshMatrixMass totalMass="1000" />
    
            <BoxROI box="-1 9.9 -1 11 10.1 1" name="roi"/>
            <FixedProjectiveConstraint indices="@roi.indices" />
            <TriangleFEMForceField name="FEM1" youngModulus="5000" poissonRatio="0.3" method="large" topology="@topology"/>
    
            <Node name="constraintSpace">
                <MechanicalObject template="Vec1" name="areaDoFs"/>
                <AreaMapping name="areaMapping" topology="@../topology" geometricStiffness="Exact" applyRestPosition="true"/>
                <RestShapeSpringsForceField template="Vec1" stiffness="15000"/>
            </Node>
    
            <Node name="Visu">
                <VisualStyle displayFlags="hideWireframe"/>
                <DataDisplay name="Visual" triangleData="@../constraintSpace/areaDoFs.position"/>
                <OglColorMap colorScheme="HSV" showLegend="true" legendTitle="Triangle area" min="@Visual.currentMin" max="@Visual.currentMax"/>
                <IdentityMapping input="@.." output="@Visual" />
            </Node>
        </Node>
    
        <Node name="noConstraints">
            <EulerImplicitSolver name="odeSolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <EigenSimplicialLDLT name="linearSolver" template="CompressedRowSparseMatrixMat3x3d"/>
    
            <TriangleSetTopologyContainer src="@../grid" name="topology"/>
            <MechanicalObject template="Vec3" name="DoFs"/>
            <GenericConstraintCorrection />
    
            <MeshMatrixMass totalMass="1000" />
    
            <BoxROI box="-1 9.9 -1 11 10.1 1" name="roi"/>
            <FixedProjectiveConstraint indices="@roi.indices" />
            <TriangleFEMForceField name="FEM1" youngModulus="5000" poissonRatio="0.3" method="large" topology="@topology"/>
    
            <Node name="constraintSpace">
                <MechanicalObject template="Vec1" name="areaDoFs"/>
                <AreaMapping name="areaMapping" topology="@../topology"/>
            </Node>
    
            <Node name="Visu">
                <OglModel name="Visual" color="darkgray" />
                <IdentityMapping input="@.." output="@Visual" />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9.81 0", dt="0.05")

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', name="Sofa.Component.AnimationLoop")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Solver")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       plugins.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering2D")
       plugins.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")

       root.addObject('FreeMotionAnimationLoop', solveVelocityConstraintFirst="true", computeBoundingBox="false", parallelODESolving="true")
       root.addObject('BlockGaussSeidelConstraintSolver', tolerance="1e-9", maxIterations="1000")
       root.addObject('VisualStyle', displayFlags="showWireframe showBehaviorModels")
       root.addObject('RegularGridTopology', name="grid", nx="10", ny="10", nz="1", xmin="0", xmax="10", ymin="0", ymax="10", zmin="0", zmax="0")

       with_area_constraints = root.addChild('withAreaConstraints')

       with_area_constraints.addObject('EulerImplicitSolver', name="odeSolver", rayleighStiffness="0.1", rayleighMass="0.1")
       with_area_constraints.addObject('EigenSimplicialLDLT', name="linearSolver", template="CompressedRowSparseMatrixMat3x3d")
       with_area_constraints.addObject('TriangleSetTopologyContainer', src="@../grid", name="topology")
       with_area_constraints.addObject('MechanicalObject', template="Vec3", name="DoFs")
       with_area_constraints.addObject('GenericConstraintCorrection', )
       with_area_constraints.addObject('MeshMatrixMass', totalMass="1000")
       with_area_constraints.addObject('BoxROI', box="-1 9.9 -1 11 10.1 1", name="roi")
       with_area_constraints.addObject('FixedProjectiveConstraint', indices="@roi.indices")
       with_area_constraints.addObject('TriangleFEMForceField', name="FEM1", youngModulus="5000", poissonRatio="0.3", method="large", topology="@topology")

       constraint_space = withAreaConstraints.addChild('constraintSpace')

       constraint_space.addObject('MechanicalObject', template="Vec1", name="areaDoFs")
       constraint_space.addObject('AreaMapping', name="areaMapping", topology="@../topology", geometricStiffness="Exact", applyRestPosition="true")
       constraint_space.addObject('RestShapeSpringsForceField', template="Vec1", stiffness="15000")

       visu = withAreaConstraints.addChild('Visu')

       visu.addObject('VisualStyle', displayFlags="hideWireframe")
       visu.addObject('DataDisplay', name="Visual", triangleData="@../constraintSpace/areaDoFs.position")
       visu.addObject('OglColorMap', colorScheme="HSV", showLegend="true", legendTitle="Triangle area", min="@Visual.currentMin", max="@Visual.currentMax")
       visu.addObject('IdentityMapping', input="@..", output="@Visual")

       no_constraints = root.addChild('noConstraints')

       no_constraints.addObject('EulerImplicitSolver', name="odeSolver", rayleighStiffness="0.1", rayleighMass="0.1")
       no_constraints.addObject('EigenSimplicialLDLT', name="linearSolver", template="CompressedRowSparseMatrixMat3x3d")
       no_constraints.addObject('TriangleSetTopologyContainer', src="@../grid", name="topology")
       no_constraints.addObject('MechanicalObject', template="Vec3", name="DoFs")
       no_constraints.addObject('GenericConstraintCorrection', )
       no_constraints.addObject('MeshMatrixMass', totalMass="1000")
       no_constraints.addObject('BoxROI', box="-1 9.9 -1 11 10.1 1", name="roi")
       no_constraints.addObject('FixedProjectiveConstraint', indices="@roi.indices")
       no_constraints.addObject('TriangleFEMForceField', name="FEM1", youngModulus="5000", poissonRatio="0.3", method="large", topology="@topology")

       constraint_space = noConstraints.addChild('constraintSpace')

       constraint_space.addObject('MechanicalObject', template="Vec1", name="areaDoFs")
       constraint_space.addObject('AreaMapping', name="areaMapping", topology="@../topology")

       visu = noConstraints.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="darkgray")
       visu.addObject('IdentityMapping', input="@..", output="@Visual")
    ```


<!-- automatically generated doc END -->
