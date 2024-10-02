# VolumeMapping

This component is classified under the category of [Mappings](../../../../simulation-principles/multi-model-representation/mapping/).
It maps each tetrahedron in a topology to a scalar value representing its volume.

The inputs of the component are:
- a `State`: it contains the list of coordinates of the tetrahedra vertices
- a `BaseMeshTopology`: it contains the list of tetrahedra, typically defined by indices that reference their vertices.

The output is a `State` where the `position` field is the list of scalar values representing the volume of tetrahedra. These values are output in the same order as the input tetrahedron list, ensuring a direct correlation between each tetrahedron and its corresponding volume value.

## Mapping function

Let us define 4 vertices forming a tetrahedron: $P_0$, $P_1$, $P_2$, and $P_3$.

The volume of a tetrahedron is computed as:

$$
\text{Volume}(P_0, P_1, P_2, P_3) = \frac{1}{6} | (P_1-P_0) \cdot \left( (P_2-P_0)\times(P_3-P_0) \right) |
$$

Here, the cross product $\times$ and the dot product $\cdot$ are combined in the scalar triple product to compute the volume.

Given $n$ tetrahedra in the topology and $m$ vertices, the mapping function of this mapping is $f(x) = (f_0(x), \dots, f_{n-1}(x))$. For $0 \le i < n$:

$$
f_i(x) = \text{Volume}(v_{t_{i_0}}, v_{t_{i_1}}, v_{t_{i_2}}, v_{t_{i_3}})
$$

with $t_{i_j}$ is the index of the $j$-th vertex in the $i$-th tetrahedron.
$x \in \mathbb{R}^{3m}$ is the input vector, i.e. the concatenation of all vertices positions.
$v_i$ is the $i$-th vertex position, i.e. $v_i = (x_{3i}, x_{3i+1}, x_{3i+2})$.

## Jacobian Matrix

The Jacobian matrix of this mapping, which represents the first-order partial derivatives of the output with respect to the input, is not constant, and depends on the input.

The elements of the Jacobian matrix $J \in \mathbb{R}^{n \times 3 m}$ are given by:
for $0 \leq i < n, 0 \leq j < 3m$,

$$
J_{ij} = \frac{\partial f_i}{\partial x_j}
$$

Let us compute the $3 \times 1$ sub-matrix $D_{ij}$ such that $j$ is a multiple of 3, and $D_{ij_k} = J_{i,j+k}$ for $0 \leq k < 3$.

$$
D_{iv_{t_{i_1}}} = \frac{1}{6} (v_{t_{i_2}}-v_{t_{i_0}})\times(v_{t_{i_3}}-v_{t_{i_0}})
$$

$$
D_{iv_{t_{i_2}}} = \frac{1}{6} (v_{t_{i_3}}-v_{t_{i_0}})\times(v_{t_{i_1}}-v_{t_{i_0}})
$$

$$
D_{iv_{t_{i_3}}} = \frac{1}{6} (v_{t_{i_1}}-v_{t_{i_0}})\times(v_{t_{i_2}}-v_{t_{i_0}})
$$

$$
D_{iv_{t_{i_0}}} = -\frac{1}{6} (D_{iv_{t_{i_1}}} + D_{iv_{t_{i_2}}} + D_{iv_{t_{i_3}}})
$$

The computation uses the triple product property that it remains unchanged under a circular shift.
That is why $D_{iv_{t_{i_1}}}$, $D_{iv_{t_{i_2}}}$, and $D_{iv_{t_{i_3}}}$ are very similar.
$D_{iv_{t_{i_0}}}$ is more complex because $v_{t_{i_0}}$ appears in all terms.

## Hessian Tensor

The Hessian tensor represents the second-order partial derivatives of the output with respect to the input. For the VolumeMapping component, the Hessian tensor is non-zero because the Jacobian matrix depends on the input $x$.

The elements of the Hessian tensor are given by:

$$
H_{ijk} = \frac{\partial J_{ij}(x)}{\partial x_k}
$$

It can be noticed that for $0 \le i < n$ and $0 \le j < 4$:

$$
\frac{\partial D_{iv_{t_{i_j}}}}{\partial v_{t_{i_j}}} = 0
$$


Then,

$$
\frac{\partial D_{iv_{t_{i_0}}}}{\partial v_{t_{i_1}}} = \frac{1}{6} [v_{t_{i_2}} - v_{t_{i_3}}]_\times
$$

$$
\frac{\partial D_{iv_{t_{i_0}}}}{\partial v_{t_{i_2}}} = \frac{1}{6} [v_{t_{i_3}} - v_{t_{i_1}}]_\times
$$

$$
\frac{\partial D_{iv_{t_{i_0}}}}{\partial v_{t_{i_3}}} = \frac{1}{6} [v_{t_{i_1}} - v_{t_{i_2}}]_\times
$$

$$
\frac{\partial D_{iv_{t_{i_1}}}}{\partial v_{t_{i_2}}} = \frac{1}{6} [v_{t_{i_0}} - v_{t_{i_3}}]_\times
$$

$$
\frac{\partial D_{iv_{t_{i_1}}}}{\partial v_{t_{i_3}}} = \frac{1}{6} [v_{t_{i_2}} - v_{t_{i_0}}]_\times
$$

$$
\frac{\partial D_{iv_{t_{i_2}}}}{\partial v_{t_{i_3}}} = \frac{1}{6} [v_{t_{i_0}} - v_{t_{i_1}}]_\times
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

The other elements of the matrix are obtained by symmetry of the Hessian matrix.
<!-- automatically generated doc START -->
<!-- generate_doc -->

Mapping each tetrahedron in a topology to a scalar value representing its volume


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

VolumeMapping.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -9.81 0" dt="0.02">
    
        <CollisionPipeline name="CollisionPipeline" verbose="0"/>
        <DefaultAnimationLoop/>
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="collision response" response="PenalityContactForceField"/>
        <DiscreteIntersection/>
    
        <MeshOBJLoader name="LiverSurface" filename="mesh/liver-smooth.obj"/>
    
        <Node name="Liver" gravity="0 -9.81 0">
            <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1"/>
            <EigenSimplicialLDLT template="CompressedRowSparseMatrixMat3x3d"/>
            <MeshGmshLoader name="meshLoader" filename="mesh/liver.msh"/>
            <TetrahedronSetTopologyContainer name="topo" src="@meshLoader"/>
            <MechanicalObject name="dofs" src="@meshLoader"/>
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo"/>
            <DiagonalMass name="computed using mass density" massDensity="1"/>
            <TetrahedralCorotationalFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.3"
                                                  youngModulus="3000" computeGlobalMatrix="0"/>
            <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="3 39 64"/>
            <Node name="constraintSpace">
                <MechanicalObject template="Vec1" name="volumeDoFs"/>
                <VolumeMapping name="volumeMapping" topology="@../topo" geometricStiffness="Exact" applyRestPosition="true"/>
                <RestShapeSpringsForceField template="Vec1" stiffness="15000"/>
            </Node>
            <Node name="Visu" tags="Visual" gravity="0 -9.81 0">
                <OglModel name="VisualModel" src="@../../LiverSurface"/>
                <BarycentricMapping name="visual mapping" input="@../dofs" output="@VisualModel"/>
            </Node>
            <Node name="Surf" gravity="0 -9.81 0">
                <SphereLoader filename="mesh/liver.sph"/>
                <MechanicalObject name="spheres" position="@[-1].position"/>
                <SphereCollisionModel name="CollisionModel" listRadius="@[-2].listRadius"/>
                <BarycentricMapping name="sphere mapping" input="@../dofs" output="@spheres"/>
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9.81 0", dt="0.02")

       root.addObject('CollisionPipeline', name="CollisionPipeline", verbose="0")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', name="collision response", response="PenalityContactForceField")
       root.addObject('DiscreteIntersection', )
       root.addObject('MeshOBJLoader', name="LiverSurface", filename="mesh/liver-smooth.obj")

       liver = root.addChild('Liver', gravity="0 -9.81 0")

       liver.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
       liver.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrixMat3x3d")
       liver.addObject('MeshGmshLoader', name="meshLoader", filename="mesh/liver.msh")
       liver.addObject('TetrahedronSetTopologyContainer', name="topo", src="@meshLoader")
       liver.addObject('MechanicalObject', name="dofs", src="@meshLoader")
       liver.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       liver.addObject('DiagonalMass', name="computed using mass density", massDensity="1")
       liver.addObject('TetrahedralCorotationalFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.3", youngModulus="3000", computeGlobalMatrix="0")
       liver.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="3 39 64")

       constraint_space = Liver.addChild('constraintSpace')

       constraint_space.addObject('MechanicalObject', template="Vec1", name="volumeDoFs")
       constraint_space.addObject('VolumeMapping', name="volumeMapping", topology="@../topo", geometricStiffness="Exact", applyRestPosition="true")
       constraint_space.addObject('RestShapeSpringsForceField', template="Vec1", stiffness="15000")

       visu = Liver.addChild('Visu', tags="Visual", gravity="0 -9.81 0")

       visu.addObject('OglModel', name="VisualModel", src="@../../LiverSurface")
       visu.addObject('BarycentricMapping', name="visual mapping", input="@../dofs", output="@VisualModel")

       surf = Liver.addChild('Surf', gravity="0 -9.81 0")

       surf.addObject('SphereLoader', filename="mesh/liver.sph")
       surf.addObject('MechanicalObject', name="spheres", position="@[-1].position")
       surf.addObject('SphereCollisionModel', name="CollisionModel", listRadius="@[-2].listRadius")
       surf.addObject('BarycentricMapping', name="sphere mapping", input="@../dofs", output="@spheres")
    ```


<!-- automatically generated doc END -->
