# SquareMapping

This component is classified under the category of [Mappings](../../../simulation-principles/multi-model-representation/mapping/).

In this particular mapping, we designate the input as the parent state and the output as the child state.

## Mapping Function

The transformation function employed in this mapping is the square function.
Formally, if $f$ denotes the mapping function, then for any input $x$, the output $f(x)$ is $x^2$.

Mathematically, this can be expressed as:

$$
f(x)=x^2
$$

for all $x$ in the domain.

## Jacobian Matrix

The Jacobian matrix of this mapping, which represents the first-order partial derivatives of the output with respect to the input, is not constant, and depends on the input.

The elements of the Jacobian matrix are given by:
$$
J_{ij} = \frac{\partial f_i}{\partial x_j} = \delta_{ij} 2  x_j
$$

This can be written in matrix form as:

$$
J(x) = 2\: \text{diag} (x)
$$

Here, $\text{diag}(x)$ denotes a diagonal matrix with the elements of $x$ on the diagonal.

Since the Jacobian matrix is diagonal, its transpose is equal to itself:

$$
J(x)^T = J(x)
$$

## Hessian Tensor

The Hessian tensor represents the second-order partial derivatives of the output with respect to the input. For the `SquareMapping` component, the Hessian tensor is non-zero because the Jacobian matrix depends on the input $x$.

The elements of the Hessian tensor are given by:

$$
H_{ijk} = \frac{\partial J_{ij}(x)}{\partial x_k} = \frac{\partial (\delta_{ij} 2  x_j)}{\partial x_k} = 2 \delta_{ij} \frac{\partial x_j}{\partial x_k} = 2 \delta_{ij} \delta_{jk}
$$

Then, for any vector $v$
$$
(H \cdot v)_{ij} = \sum_k H_{ijk} v_k = 2 \delta_{ij} \sum_k \delta_{jk} v_k = 2 \delta_{ij} v_j
$$

In matrix notation, this can be written as:

$$
H \cdot v = 2 \: \text{diag}(v)
$$

## Implementation Details

Given the nature of the mapping function, the mapping is defined only if the input and output are scalar DoFs.
It means, the only available template for this mapping is `Vec1`.

