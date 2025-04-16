NewtonRaphsonSolver
===================

NewtonRaphsonSolver is a component able to solve nonlinear equations using [Newton-Raphson method](https://en.wikipedia.org/wiki/Newton%27s_method).
From an initial guess, the algorithm successively computes better approximations of the root of the nonlinear function.
At every iteration, multiple criteria are evaluated to decide to stop the algorithm (because it converged or the maximum number of iterations has been reached), or to continue.

The algorithm relies on the derivative of the function and a linear system to solve.
For a function $F : \mathbb{R}^k \rightarrow \mathbb{R}^k$, the new approximation of the root $x_{n+1}$ is computed as:

$$
\nabla_F(x_n) (x_{n+1} - x_n) = -F(x_n)
$$

where:

- $x_i$ is the $i$-th approximation of the root
- $x_0$ is the initial guess
- $\nabla_F$ is the Jacobian matrix of the function

If $dx$ is the solution of the previous linear system, then

$$
x_{n+1} = dx + x_n
$$

Example
-------

To solve a static equilibrium (see [StaticSolver](StaticSolver.md)), the nonlinear equation to solve is the sum of forces must be equal to zero ($\sum F = 0$). At each iteration, the linear system $K dx = -\sum F$ must be solved to compute the next approximation of the root. Here K is the derivative of the forces, also called the stiffness matrix.

Usage
-----

This component must be linked by another component requiring to solve a nonlinear equation, such as an implicit ODE solver or a static solver.

In XML format, the link may look like:

```xml
<NewtonRaphsonSolver name="newton"
                     maxNbIterationsNewton="10" absoluteResidualStoppingThreshold="1e-5"
                     maxNbIterationsLineSearch="5" lineSearchCoefficient="0.5"
                     relativeInitialStoppingThreshold="1e-3"
                     absoluteEstimateDifferenceThreshold="1e-5"
                     relativeEstimateDifferenceThreshold="1e-5"/>
<BDFOdeSolver newtonSolver="@newton" order="2" rayleighMass="0.01" rayleighStiffness="0.01" />
```
<!-- automatically generated doc START -->
<!-- generate_doc -->

Generic Newton-Raphson algorithm solving nonlinear equations.


__Target__: Sofa.Component.ODESolver.Backward

__namespace__: sofa::component::odesolver::backward

__parents__:

- BaseObject

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
		<td>updateStateWhenDiverged</td>
		<td>
Update the states within the last iteration even if the iterative process is considered diverged.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>warnWhenLineSearchFails</td>
		<td>
Trigger a warning if line search fails
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>warnWhenDiverge</td>
		<td>
Trigger a warning if Newton-Raphson diverges
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Stopping criteria</td>
	</tr>
	<tr>
		<td>maxNbIterationsNewton</td>
		<td>
Maximum number of iterations of the Newton's method if it has not converged.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>relativeSuccessiveStoppingThreshold</td>
		<td>
Threshold for the relative successive progress criterion. The Newton iterations will stop when the ratio between the norm of the residual at iteration k over the norm of the residual at iteration k-1 is lower than this threshold.
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>relativeInitialStoppingThreshold</td>
		<td>
Threshold for the relative initial progress criterion. The Newton iterations will stop when the ratio between the norm of the residual at iteration k over the norm of the residual at iteration 0 is lower than this threshold. This criterion tracks the overall progress made since the beginning of the iteration process. If the ratio is significantly smaller than 1, it indicates that the iterative process is making substantial progress, and the method is converging toward the root.
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>absoluteResidualStoppingThreshold</td>
		<td>
Threshold for the absolute function value stopping criterion. The Newton iterations will stop when the norm of the residual at iteration k is lower than this threshold. This criterion indicates the current iteration found an estimate close to the root.
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>relativeEstimateDifferenceThreshold</td>
		<td>
Threshold for the relative change in root estimate criterion. The Newton iterations will stop when the difference between two successive estimates divided by the previous estimate is smaller than this threshold
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>absoluteEstimateDifferenceThreshold</td>
		<td>
Threshold for the absolute change in root estimate criterion. The Newton iterations will stop when the difference between two successive estimates is smaller than this threshold.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Line Search</td>
	</tr>
	<tr>
		<td>maxNbIterationsLineSearch</td>
		<td>
Maximum number of iterations of the line search method if it has not converged.
		</td>
		<td>5</td>
	</tr>
	<tr>
		<td>lineSearchCoefficient</td>
		<td>
Line search coefficient
		</td>
		<td>0.5</td>
	</tr>
	<tr>
		<td colspan="3">Analysis</td>
	</tr>
	<tr>
		<td>status</td>
		<td>
status
- Undefined: The solver has not been called yet
- Running: The solver is still running and/or did not finish
- ConvergedEquilibrium: Converged: the iterations did not start because the system is already at equilibrium
- DivergedLineSearch: Diverged: line search failed
- DivergedMaxIterations: Diverged: Reached the maximum number of iterations
- ConvergedResidualSuccessiveRatio: Converged: Residual successive ratio is smaller than the threshold
- ConvergedResidualInitialRatio: Converged: Residual initial ratio is smaller than the threshold
- ConvergedAbsoluteResidual: Converged: Absolute residual is smaller than the threshold
- ConvergedRelativeEstimateDifference: Converged: Relative estimate difference is smaller than the threshold
- ConvergedAbsoluteEstimateDifference: Converged: Absolute estimate difference is smaller than the threshold
		</td>
		<td>Undefined</td>
	</tr>
	<tr>
		<td>residualGraph</td>
		<td>
Graph of the residual over the iterations
		</td>
		<td></td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|


<!-- automatically generated doc END -->
