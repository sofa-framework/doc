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
D_{iv_{t_{i_3}}} = \frac{1}{6} (v_{t_{i_1}}-v_{t_{i_0}})\times(v_{t_{i_3}}-v_{t_{i_0}})
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
