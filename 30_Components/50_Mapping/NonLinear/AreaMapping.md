# AreaMapping

This component is classified under the category of [Mappings](../../../../simulation-principles/multi-model-representation/mapping/).
It maps each triangle in a topology to a scalar value representing its area.

The inputs of the component are:
- A `State`: it contains the list of coordinates of the triangles vertices
- A `BaseMeshTopology`: it contains the list of triangles, typically defined by indices that reference their vertices.

The output is a
- A `State` where the `position` field is the list of scalar values representing the area of the triangles. These values are output in the same order as the input triangle list, ensuring a direct correlation between each triangle and its corresponding area value.

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
f_i(x) = \text{Area}(v_{t_{i_0}}, v_{t_{i_1}}, v_{t_{i_1}})
$$

with $t_{i_j}$ is the index of the $j$-th vertex in the $i$-th triangle.
$x \in \mathbb{R}^{3m}$ is the input vector, i.e. the concatenation of all vertices positions.
$v_i$ is the $i$-th vertex position, i.e $v_i = (x_{3i}, x_{3i+1}, x_{3i+2})$.

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
