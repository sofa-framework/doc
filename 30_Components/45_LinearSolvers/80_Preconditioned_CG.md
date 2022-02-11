ShewchukPCGLinearSolver  
=======================

This component belongs to the category of [LinearSolver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/linear-solvers/), it therefore aims at solving the linear system <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="Linear system" />. The ShewchukPCGLinearSolver is an iterative solver using the [conjugate gradient method](https://en.wikipedia.org/wiki/Conjugate_gradient_method) as implemented in the [CGLinearSolver](https://www.sofa-framework.org/community/doc/components/linearsolver/cglinearsolver/) in SOFA but it adds the possibility to define a [preconditioner](https://en.wikipedia.org/wiki/Preconditioner). It must be reminded that the ShewchukPCGLinearSolver relies on the conjugate gradient method, meaning that as all iterative approaches, no exact solution can be found. The accuracy of your solution will always depend on the conditioning of your system and your input data (iterations, tolerance and threshold).


Preconditioners are used in cases where the convergence of the system is slow, which is usually due to a ill-conditioned system (high [condition number](https://en.wikipedia.org/wiki/Condition_number)). In order to preserve accuracy, while improving performance, preconditioning methods aims at projecting a matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{P}" title="Precondioner matrix" /> (preconditioner) on the linear system <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="Linear system" />, in order to get closer to the solution. The efficiency of the preconditioner will depend on the choice of the preconditioner <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{P}" title="Precondioner matrix" />.

The ShewchukPCGLinearSolver allows to choose the preconditioner of our choice based on an external direct linear solver: LULinearSolver, [SparseLDLSolver](https://www.sofa-framework.org/community/doc/components/linearsolvers/sparseldlsolver/), etc. These solvers will allow to compute <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{P}%20\approx%20\mathbf{A}" title="Precondioning method" /> and use it to compute at each iteration _k_ of the conjugate gradient:

<img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{P}^{-1}(\mathbf{A}x_k-b)=0" title="Preconditioning of the CG Linear Solver" />

Using an appropriate preconditioner <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{P}" title="Precondioner matrix" /> of a matrix <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" /> means that <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{P}^{-1}\mathbf{A}" title="Apply the transformation" /> has a smaller condition number than <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}" title="System matrix" />.


Data  
----

This LinearSolver is ruled by several breaking conditions:  

- **iterations**: specified the maximum number of iterations after which the iterative descent of the conjugate gradient must stop
- **tolerance**: defines the desired accuracy of the Conjugate Gradient solution (ratio of current residual norm over initial residual norm)"
- **preconditioners**: name of the linear solvers to be used as preconditioner
- **update_step**: number of steps before the next refresh of precondtioners
- **build_precond**: if false build the preconditioner only at the initial step, else building the preconditioner every *update_step*


Usage
-----

The ShewchukPCGLinearSolver **requires**:

- the use (above in the scene graph) of an integration scheme
- (below in the scene graph) of a MechanicalObject storing the state information that the ShewchukPCGLinearSolver will access
- and, if a preconditioning is desired, a linear solver to compute the <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{P}^{-1}" title="Inverse of the precondioner matrix" />

As for the CGLinearSolver, when using a ShewchukPCGLinearSolver, make sure you carefully chose the value of the free data field iterations, tolerance and threshold. Both tolerance and threshold data must be chosen in accordance with the dimension of the degrees of freedom (DOFs). Usually, the value of these two data is close to the square of the expected error on the DOFs.



Example
-------

This component is used as follows in XML format:

``` xml
<ShewchukPCGLinearSolver iterations="1000" tolerance="1e-9" preconditioners="LUSolver" build_precond="1" update_step="1000"/>
```

or using SofaPython3:

``` python
node.addObject('ShewchukPCGLinearSolver', iterations='1000', tolerance='1e-9', preconditioners='LUSolver'. build_precond='1', update_step='1000')
```

An example scene involving a ShewchukPCGLinearSolver is available in [*examples/Components/solver/ShewchukPCGLinearSolver.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/solver/ShewchukPCGLinearSolver.scn)
