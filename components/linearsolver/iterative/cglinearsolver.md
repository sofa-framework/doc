---
title: CGLinearSolver
---

CGLinearSolver  
==============

This component belongs to the category of [LinearSolver](../../../../simulation-principles/system-resolution/linear-solver/). The role of the CGLinearSolver is to solve the linear system $\mathbf{A}x=b$ without any _a priori_ on this system.

In SOFA, the CGLinearSolver follows the well-known [conjugate gradient method](https://en.wikipedia.org/wiki/Conjugate_gradient_method), which consists in iteratively solving $r=b-\mathbf{A}x^k$ where *r* is known as the residual. This residual will be used to compute mutually conjugate vectors *p* (see the sequence diagram below) which will be used as a basis to find a new approximated solution $x^{k+1}$.

**Note**: the CGLinearSolver in SOFA assumes that the right hand side (RHS) vector *b* is already computed. The computation of *b* is usually called in the [integration scheme](../../../../simulation-principles/system-resolution/integration-scheme/) through the function `computeForce()`.



Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/CGLinearSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/CGLinearSolver.png?raw=true" title="Flow diagram for the CGLinearSolver"/></a>


Usage
-----

The CGLinearSolver **requires** the use (above in the scene graph) of an integration scheme, and (below in the scene graph) of a MechanicalObject storing the state information that the CGLinearSolver will access.

When using a CGLinearSolver, make sure you carefully chose the value of the free data field iterations, tolerance and threshold. Both tolerance and threshold data must be chosen in accordance with the dimension of the degrees of freedom (DOFs). Usually, the value of these two data is close to the square of the expected error on the DOFs.

Remember that when using an iterative linear solver like the CGLinearSolver, no exact solution can be found. The accuracy of your solution will always depend on the conditioning of your system and your input data (iterations, tolerance and threshold).

