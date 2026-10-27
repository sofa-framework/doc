# CorotationalFEMForceField

The corotational finite element formulation is used to model geometrically nonlinear mechanical problems in which bodies undergo large translations and/or rotations while experiencing relatively small strains.
In each element, the rigid-body motion is estimated from the nodal positions and separated from its deformational motion. The internal forces are computed per element, using a small-strain formulation, and are expressed in an element frame that translates and rotates with the element. These forces are then transformed back into the global coordinate frame. The formulation is detailed in [1].

## Internal forces

The internal forces follow from the small-strain tensor of linear elasticity

$$
\boldsymbol{\varepsilon} = \tfrac{1}{2}\left(\mathbf{F} + \mathbf{F}^T\right) - \mathbf{I}
$$

where $\mathbf{F} = \frac{\partial\mathbf{x}}{\partial\mathbf{X}}$ is the deformation gradient, and $\mathbf{X}$ and $\mathbf{x}$ are the positions of a material point on the reference and current configuration, respectively. The linear law sees a nonzero strain under a rigid rotation, $\mathbf{F} = \mathbf{R}$, since it treats the rotation as a stretch, and the element incorrectly reports internal forces. The rotation must therefore be extracted from the deformation gradient. Quantities expressed in the element frame are denoted with a bar, those without a bar are expressed in the global frame, with which the element frame coincides at rest. The polar decomposition of $\mathbf{F}$ separates the rotation from the stretch,

$$
\mathbf{F} = \mathbf{R} \bar{\mathbf{S}}
$$

with $\mathbf{R}$ a rotation and $\bar{\mathbf{S}}$ a symmetric stretch, and the corotational formulation measures the strain after removing the rotation:

$$
\bar{\boldsymbol{\varepsilon}} = \tfrac{1}{2}\left(\mathbf{R}^T\mathbf{F} + \mathbf{F}^T\mathbf{R}\right) - \mathbf{I} = \bar{\mathbf{S}} - \mathbf{I}
$$

- Vanishes for pure rigid-body motion $\mathbf{F} = \mathbf{R}$ and $\bar{\mathbf{S}} = \mathbf{I}$.
- Reduces to the usual small strain when $\mathbf{F} = \bar{\mathbf{S}}$ and $\mathbf{R} = \mathbf{I}$.

How $\mathbf{R}$ is estimated from the nodal positions is presented at the end.

On the element, the strain is measured through the local displacement of each node, i.e. its displacement in the element frame once the rigid-body motion is removed. The translation is removed by measuring the nodal positions from their average over the element, $\mathbf{t}$ on the current and $\mathbf{t} _0$ on the reference configuration:

$$
\mathbf{p} _n = \mathbf{x} _n - \mathbf{t}, \qquad \mathbf{q} _n = \mathbf{X} _n - \mathbf{t} _0
$$

The rotation is removed by bringing the current offset $\mathbf{p} _n$ back into the element frame, so the local displacement of node $n$ is

$$
\bar{\mathbf{u}} _n = \mathbf{R}^T\mathbf{p} _n - \mathbf{q} _n
$$

The element stiffness matrix $\bar{\mathbf{K}}$, applied to the local displacements, yields the local force of node $n$

$$
\bar{\mathbf{f}} _n = \sum _m \bar{\mathbf{K}} _{nm} \bar{\mathbf{u}} _m = \sum _m \bar{\mathbf{K}} _{nm}\left(\mathbf{R}^T\mathbf{p} _m - \mathbf{q} _m\right)
$$

where $\bar{\mathbf{K}} _{nm}$ is the block of $\bar{\mathbf{K}}$ coupling nodes $n$ and $m$. The local force is then rotated back into the global frame:

$$
\mathbf{f} _n = \mathbf{R} \bar{\mathbf{f}} _n
$$

## Tangent stiffness

The consistent tangent stiffness $\mathbf{K}^{(T)} _{nk} = \frac{\partial\mathbf{f} _n}{\partial\mathbf{x} _k}$ satisfies $d\mathbf{f} _n = \sum _k \mathbf{K}^{(T)} _{nk} d\mathbf{x} _k$. The variation of $\mathbf{x} _k$ is propagated to the force through the rotation $\mathbf{R}$, which the force field estimates from the current nodal positions, and through the local displacements $\bar{\mathbf{u}} _m$:

$$
d\mathbf{f} _n = d\mathbf{R} \bar{\mathbf{f}} _n + \mathbf{R}\sum _m \bar{\mathbf{K}} _{nm} d\bar{\mathbf{u}} _m
$$

Since $\mathbf{R}^T\mathbf{R} = \mathbf{I}$, its variation gives $\mathbf{R}^T d\mathbf{R} + d\mathbf{R}^T\mathbf{R} = \mathbf{0}$, so $\mathbf{R}^T d\mathbf{R}$ is skew-symmetric. It is described by a few independent components, one in 2D and three in 3D, gathered in the rotation vector $d\bar{\boldsymbol{\theta}}$, an angle about an axis expressed in the element frame. The variation of the rotation is written [1]

$$
d\mathbf{R} = \mathbf{R} [d\bar{\boldsymbol{\theta}}] _\times, \qquad d\mathbf{R}^T = -[d\bar{\boldsymbol{\theta}}] _\times\mathbf{R}^T
$$

so that $\mathbf{R} + d\mathbf{R} = \mathbf{R}\left(\mathbf{I} + [d\bar{\boldsymbol{\theta}}] _\times\right)$ applies the small rotation in the element frame before $\mathbf{R}$. Here $[d\bar{\boldsymbol{\theta}}] _\times$ is the cross-product matrix of $d\bar{\boldsymbol{\theta}}$, $[d\bar{\boldsymbol{\theta}}] _\times\mathbf{b} = d\bar{\boldsymbol{\theta}}\times\mathbf{b} = [\mathbf{b}] _\times^T d\bar{\boldsymbol{\theta}}$ for any vector $\mathbf{b}$. In 2D, $d\bar{\boldsymbol{\theta}}$ is a scalar and

$$
[d\bar{\boldsymbol{\theta}}] _\times = d\bar{\boldsymbol{\theta}}\begin{bmatrix}0 & -1 \cr 1 & 0\end{bmatrix}, \qquad [\mathbf{b}] _\times = \begin{bmatrix}-b _2 & b _1\end{bmatrix}
$$

The rotation thus enters the tangent through $d\bar{\boldsymbol{\theta}}$ only.

The first term becomes

$$
d\mathbf{R} \bar{\mathbf{f}} _n = \mathbf{R} [d\bar{\boldsymbol{\theta}}] _\times\bar{\mathbf{f}} _n = \mathbf{R} [\bar{\mathbf{f}} _n] _\times^T d\bar{\boldsymbol{\theta}}
$$

In the second term, with $\mathbf{R}^T\mathbf{p} _m = \mathbf{q} _m + \bar{\mathbf{u}} _m$ and $d\mathbf{p} _m = d\mathbf{x} _m - d\mathbf{t}$,

$$
d\bar{\mathbf{u}} _m = d\mathbf{R}^T\mathbf{p} _m + \mathbf{R}^T d\mathbf{p} _m = -[d\bar{\boldsymbol{\theta}}] _\times\left(\mathbf{q} _m + \bar{\mathbf{u}} _m\right) + \mathbf{R}^T \left(d\mathbf{x} _m - d\mathbf{t}\right)
$$

so that the second term splits into four sums, of which the first and fourth vanish because a rigid rotation of the element and a rigid translation produce no force:

$$
\mathbf{R}\sum _m \bar{\mathbf{K}} _{nm} d\bar{\mathbf{u}} _m = -\mathbf{R}\sum _m \bar{\mathbf{K}} _{nm}[d\bar{\boldsymbol{\theta}}] _\times\mathbf{q} _m - \mathbf{R}\sum _m \bar{\mathbf{K}} _{nm}[d\bar{\boldsymbol{\theta}}] _\times\bar{\mathbf{u}} _m + \mathbf{R}\sum _m \bar{\mathbf{K}} _{nm}\mathbf{R}^T d\mathbf{x} _m - \mathbf{R}\sum _m \bar{\mathbf{K}} _{nm}\mathbf{R}^T d\mathbf{t} = \mathbf{R}\sum _m \bar{\mathbf{K}} _{nm}\left(-[\bar{\mathbf{u}} _m] _\times^T d\bar{\boldsymbol{\theta}} + \mathbf{R}^T d\mathbf{x} _m\right)
$$

Collecting all terms,

$$
d\mathbf{f} _n = \mathbf{R}\left(\sum _m \bar{\mathbf{K}} _{nm}\mathbf{R}^T d\mathbf{x} _m + \bar{\mathbf{W}} _n d\bar{\boldsymbol{\theta}}\right), \qquad \bar{\mathbf{W}} _n = [\bar{\mathbf{f}} _n] _\times^T - \sum _m \bar{\mathbf{K}} _{nm}[\bar{\mathbf{u}} _m] _\times^T
$$

The force variation now depends on the node motions, but also on the small rotation $d\bar{\boldsymbol{\theta}}$ of the element frame. To obtain the tangent, $d\bar{\boldsymbol{\theta}}$ must also be written in terms of the node motions. Each node motion turns the element frame slightly, and $d\bar{\boldsymbol{\theta}}$ collects these contributions:

$$
d\bar{\boldsymbol{\theta}} = \sum _k \bar{\mathbf{G}} _k d\bar{\mathbf{x}} _k
$$

where $d\bar{\mathbf{x}} _k = \mathbf{R}^T d\mathbf{x} _k$ is the motion of node $k$ expressed in the element frame, and the Jacobian $\bar{\mathbf{G}} _k$ [1] links the motion of node $k$ to the rotation of the element frame. Substituting it yields

$$
d\mathbf{f} _n = \mathbf{R}\sum _k \left(\bar{\mathbf{K}} _{nk} + \bar{\mathbf{W}} _n\bar{\mathbf{G}} _k\right)\mathbf{R}^T d\mathbf{x} _k
$$

and, finally, the tangent stiffness

$$
\mathbf{K}^{(T)} _{nk} = \mathbf{R} \bar{\mathbf{K}}^{(T)} _{nk}\mathbf{R}^T, \qquad \bar{\mathbf{K}}^{(T)} _{nk} = \bar{\mathbf{K}} _{nk} + \bar{\mathbf{W}} _n\bar{\mathbf{G}} _k
$$

The matrices $\bar{\mathbf{K}}$ and $\bar{\mathbf{W}} _n$ are inherent to the force field, while $\bar{\mathbf{G}} _k$ is provided by the method used to estimate $\mathbf{R}$. With $\bar{\mathbf{G}} _k = \mathbf{0}$, the tangent reduces to $\mathbf{R} \bar{\mathbf{K}} _{nk}\mathbf{R}^T$, which treats the rotation as constant.

## Estimating the element rotation and its Jacobian

The rotation $\mathbf{R}$ is computed once per element and is shared by all its nodes. It is not known in advance: it is estimated from a linear map that takes vectors of the element from the reference configuration to the current one. In a typical problem, an element deforms as well as rotates, so no rotation maps its reference shape exactly onto its current shape, and $\mathbf{R}$ is only the best guess of the rotation that the map allows. In SOFA, there are two different strategies that can be employed to define the map and their rules differ in accuracy. Each strategy also provides the Jacobian $\bar{\mathbf{G}} _k$ used in the tangent stiffness.

### Element frames

An orthonormal frame is built from two vectors $\mathbf{a}$ and $\mathbf{b}$ along the edges of the element, once on the reference configuration and once on the current one. The linear map is the rotation from the reference frame to the current frame. The vectors $\mathbf{a}$ and $\mathbf{b}$ are combinations of the node positions $\mathbf{x}$:

$$
\mathbf{a} = \sum _k \alpha _k \mathbf{x} _k, \qquad \mathbf{b} = \sum _k \beta _k \mathbf{x} _k
$$

where $k = 0, 1, \dots$ following the numbering of the element connectivity. The coefficients $\alpha _k$ and $\beta _k$ depend on the element type:

- Triangle or tetrahedron:

  $$\mathbf{a} = \mathbf{x} _1 - \mathbf{x} _0, \qquad \mathbf{b} = \mathbf{x} _2 - \mathbf{x} _0$$

- Hexahedron:

  $$\mathbf{a} = \tfrac{1}{4}\left(\mathbf{x} _1 - \mathbf{x} _0 + \mathbf{x} _2 - \mathbf{x} _3 + \mathbf{x} _5 - \mathbf{x} _4 + \mathbf{x} _6 - \mathbf{x} _7\right)$$

  $$\mathbf{b} = \tfrac{1}{4}\left(\mathbf{x} _3 - \mathbf{x} _0 + \mathbf{x} _2 - \mathbf{x} _1 + \mathbf{x} _7 - \mathbf{x} _4 + \mathbf{x} _6 - \mathbf{x} _5\right)$$

Under a rigid motion, $\mathbf{R}$ is exact for any choice of $\mathbf{a}$ and $\mathbf{b}$. Otherwise, it depends on the node numbering of the element. The frame is then built from $\mathbf{a}$ and $\mathbf{b}$:

$$
\mathbf{e} _1 = \frac{\mathbf{a}}{\lVert \mathbf{a}\rVert}, \qquad \mathbf{e} _3 = \frac{\mathbf{a}\times\mathbf{b}}{\lVert \mathbf{a}\times\mathbf{b}\rVert}, \qquad \mathbf{e} _2 = \mathbf{e} _3\times\mathbf{e} _1
$$

Its axes are the rows of the matrix $\mathbf{E}$ which is formed at every step. The frame $\mathbf{E} _0$ of the reference configuration is computed once and stored. The rotation is then taken as:

$$
\mathbf{R} = \mathbf{E}^T\mathbf{E} _0
$$

A variation of the nodes turns the current frame by a small rotation $d\boldsymbol{\omega}$ [1]:

$$
d\mathbf{e} _i = d\boldsymbol{\omega}\times\mathbf{e} _i
$$

Since $\mathbf{E} _0$ is fixed, the rotation varies as

$$
d\mathbf{R} = d\mathbf{E}^T\mathbf{E} _0 = [d\boldsymbol{\omega}] _\times\mathbf{R}
$$

and comparing with $d\mathbf{R} = \mathbf{R} [d\bar{\boldsymbol{\theta}}] _\times$ gives

$$
d\bar{\boldsymbol{\theta}} = \mathbf{R}^T d\boldsymbol{\omega}
$$

The rotation $d\boldsymbol{\omega}$ follows from the variations of $\mathbf{a}$ and $\mathbf{b}$. With $\mathbf{b} _\perp = \mathbf{b} - (\mathbf{b}\cdot\mathbf{e} _1) \mathbf{e} _1$, the part of $\mathbf{b}$ orthogonal to $\mathbf{a}$, differentiating $\mathbf{e} _1 = \mathbf{a}/\lVert \mathbf{a}\rVert$, $\mathbf{e} _3\cdot\mathbf{a} = 0$ and $\mathbf{e} _3\cdot\mathbf{b} = 0$ gives

$$
d\boldsymbol{\omega} = \frac{\mathbf{e} _1\times d\mathbf{a}}{\lVert \mathbf{a}\rVert} + \mathbf{e} _1 \frac{\mathbf{e} _3\cdot d\mathbf{b} _\perp}{\lVert \mathbf{b} _\perp\rVert}
$$

or, in matrix form, with $b _1 = \mathbf{b}\cdot\mathbf{e} _1$ and $b _2 = \lVert \mathbf{b} _\perp\rVert$,

$$
d\boldsymbol{\omega} = \mathbf{G} _a d\mathbf{a} + \mathbf{G} _b d\mathbf{b}, \qquad \mathbf{G} _a = \frac{[\mathbf{e} _1] _\times}{\lVert \mathbf{a}\rVert} - \frac{b _1}{\lVert \mathbf{a}\rVert  b _2} \mathbf{e} _1\mathbf{e} _3^T, \qquad \mathbf{G} _b = \frac{\mathbf{e} _1\mathbf{e} _3^T}{b _2}
$$

Finally, $\mathbf{a}$ and $\mathbf{b}$ vary with the nodes as

$$
d\mathbf{a} = \sum _k \alpha _k d\mathbf{x} _k, \qquad d\mathbf{b} = \sum _k \beta _k d\mathbf{x} _k
$$

Substituting them into $d\bar{\boldsymbol{\theta}}$, with $d\mathbf{x} _k = \mathbf{R} d\bar{\mathbf{x}} _k$, yields the Jacobian

$$
\bar{\mathbf{G}} _k = \mathbf{R}^T\left(\alpha _k \mathbf{G} _a + \beta _k \mathbf{G} _b\right)\mathbf{R}
$$

### Polar decomposition

This strategy extracts the rotation through the polar decomposition of a matrix $\hat{\mathbf{F}}$ built from the node offsets. Ideally, $\hat{\mathbf{F}}$ would be the deformation gradient, but the element has a single rotation, whereas $\mathbf{F}$ generally varies within the element and cannot be computed as one matrix. The rotation is instead obtained by a best fit [2] that takes the reference offsets $\mathbf{q} _k$ as close as possible to the current offsets $\mathbf{p} _k$. Both fits employed decompose a matrix of the form

$$
\hat{\mathbf{F}} = \sum _k \mathbf{p} _k \mathbf{w} _k^T = \mathbf{R} \bar{\mathbf{S}}
$$

where the weights $\mathbf{w} _k$ depend only on the reference offsets $\mathbf{q}$:

- Rigid Fit: seeks the rotation $\mathbf{R}$ that minimizes $\sum _k \lVert\mathbf{p} _k - \mathbf{R} \mathbf{q} _k\rVert^2$. This rotation is the one of the polar decomposition with $\mathbf{w} _k = \mathbf{q} _k$, that is of

  $$\hat{\mathbf{F}} = \mathbf{H} = \sum _k \mathbf{p} _k \mathbf{q} _k^T$$

- Affine Fit: seeks the matrix $\hat{\mathbf{F}}$ that minimizes $\sum _k \lVert\mathbf{p} _k - \hat{\mathbf{F}} \mathbf{q} _k\rVert^2$, the least-squares estimate of $\mathbf{F}$. It is given by $\mathbf{w} _k = \mathbf{M}^{-1}\mathbf{q} _k$, that is

  $$\hat{\mathbf{F}} = \mathbf{H} \mathbf{M}^{-1}, \qquad \mathbf{M} = \sum _k \mathbf{q} _k \mathbf{q} _k^T$$

Under a uniform deformation, the affine fit estimates $\mathbf{F}$ and $\mathbf{R}$ exactly. The rigid fit amounts to the affine fit with $\mathbf{M}$ taken as $\mathbf{I}$. It is exact under rigid motions, but under a uniform deformation only if $\mathbf{M}$ is a multiple of $\mathbf{I}$, as for a cube or a square element. For irregular shapes, this assumption breaks.

On embedded elements, such as triangles and quadrilaterals in 3D or an edge in 2D, the offsets have no component along the element normal. $\mathbf{H}$ and $\mathbf{M}$ are then singular: the polar decomposition cannot be computed reliably from $\mathbf{H}$, and $\mathbf{M}$ cannot be inverted. To avoid this, the reference normal $\mathbf{n} _0$ is mapped onto the current normal $\mathbf{n}$ as well, by completing the matrices with

$$
\hat{\mathbf{F}} \leftarrow \hat{\mathbf{F}} + \mathbf{n} \mathbf{n} _0^T, \qquad \mathbf{M} \leftarrow \mathbf{M} + \mathbf{n} _0 \mathbf{n} _0^T
$$

the latter for the affine fit only. The completion serves only to find $\mathbf{R}$; the Jacobian below uses $\hat{\mathbf{F}}$ and $\bar{\mathbf{S}}$ without it.

The Jacobian follows from varying the decomposition, then subtracting the transpose to remove the symmetric $d\bar{\mathbf{S}}$ [3]:

$$
\mathbf{R}^T d\hat{\mathbf{F}} - d\hat{\mathbf{F}}^T\mathbf{R} = [d\bar{\boldsymbol{\theta}}] _\times\bar{\mathbf{S}} + \bar{\mathbf{S}} [d\bar{\boldsymbol{\theta}}] _\times
$$

The right-hand side equals:

$$
[d\bar{\boldsymbol{\theta}}] _\times\bar{\mathbf{S}} + \bar{\mathbf{S}} [d\bar{\boldsymbol{\theta}}] _\times = [\bar{\mathbf{A}} d\bar{\boldsymbol{\theta}}] _\times, \qquad \bar{\mathbf{A}} = \mathrm{tr}(\bar{\mathbf{S}}) \mathbf{I} - \bar{\mathbf{S}}
$$

with $\bar{\mathbf{A}} = \mathrm{tr}(\bar{\mathbf{S}})$ in 2D. On the left-hand side, since $\sum _k \mathbf{w} _k = \mathbf{0}$,

$$
d\hat{\mathbf{F}} = \sum _k \left(d\mathbf{x} _k - d\mathbf{t}\right)\mathbf{w} _k^T = \sum _k d\mathbf{x} _k \mathbf{w} _k^T
$$

and, with $d\bar{\mathbf{x}} _k = \mathbf{R}^T d\mathbf{x} _k$,

$$
\mathbf{R}^T d\hat{\mathbf{F}} - d\hat{\mathbf{F}}^T\mathbf{R} = \sum _k \left(d\bar{\mathbf{x}} _k \mathbf{w} _k^T - \mathbf{w} _k d\bar{\mathbf{x}} _k^T\right) = \left[\sum _k [\mathbf{w} _k] _\times d\bar{\mathbf{x}} _k\right] _\times
$$

Equating both sides yields the Jacobian

$$
\bar{\mathbf{G}} _k = \bar{\mathbf{A}}^{-1}[\mathbf{w} _k] _\times
$$

## References

1. C. A. Felippa, B. Haugen. A unified formulation of small-strain corotational finite elements: I. Theory. *Computer Methods in Applied Mechanics and Engineering*, 194:2285–2335, 2005.
2. M. Müller, B. Heidelberger, M. Teschner, M. Gross. Meshless deformations based on shape matching. *ACM Transactions on Graphics*, 24(3):471–478, 2005.
3. L. Rosati. Derivatives and rates of the stretch and rotation tensors. *Journal of Elasticity*, 56:213–230, 1999.
