CGLinearSolver  
==============

This component belongs to the category of [LinearSolver](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/linear-solvers/). The role of the CGLinearSolver is to solve the linear system <img class="latex" src="https://latex.codecogs.com/png.latex?\mathbf{A}x=b" title="Linear system" /> without any _a priori_ on this system.

In SOFA, the CGLinearSolver follows the well-known [conjugate gardient method](https://en.wikipedia.org/wiki/Conjugate_gradient_method), which consists in iteratively solving <img class="latex" src="https://latex.codecogs.com/png.latex?r=b-\mathbf{A}x^k" title="Computation of residual" /> where *r* is known as the residual. This residual will be used to compute mutually conjugate vectors *p* (see the sequence diagram below) which will be used as a basis to find a new approximated solution <img class="latex" src="https://latex.codecogs.com/png.latex?x^{k+1}" title="New approximated solution" />.

**Note**: the CGLinearSolver in SOFA assumes that the right hand side (RHS) vector *b* is already computed. The computation of *b* is usually called in the [integration scheme](https://www.sofa-framework.org/community/doc/main-principles/system-resolution/integration-schemes/) through the function `computeForce()`.



Sequence diagram
----------------

<a href="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/CGLinearSolver.png?raw=true"><img src="https://github.com/sofa-framework/doc/blob/master/images/linearsolver/CGLinearSolver.png?raw=true" title="Flow diagram for the CGLinearSolver"/></a>



Data  
----

This LinearSolver is ruled by several breaking conditions:  

- **iterations**: specified the maximum number of iterations after which the iterative descent of the CGLinearSolver must stop
- **tolerance**: defines the desired accuracy of the Conjugate Gradient solution (ratio of current residual norm over initial residual norm)"
- **threshold**: defines the minimum value of the denominator in the conjugate Gradient solution
- **warmStart**: this option allows to use the previous solution as initial solution, which improves the initial guess if your system is evolving smoothly


Usage
-----

The CGLinearSolver **requires** the use (above in the scene graph) of an integration scheme, and (below in the scene graph) of a MechanicalObject storing the state information that the CGLinearSolver will access.

When using a CGLinearSolver, make sure you carefully chose the value of the free data field iterations, tolerance and threshold. Both tolerance and threshold data must be chosen in accordance with the dimension of the degrees of freedom (DOFs). Usually, the value of these two data is close to the square of the expected error on the DOFs.

Remember that using an iterative linear solver like the CGLinearSolver, no exact solution can be found. The accuracy of your solution will always depend on the conditioning of your system and your input data (iterations, tolerance and threshold).



Example
-------

This component is used as follows in XML format:

``` xml
<CGLinearSolver iterations="100" tolerance="1e-5" threshold="1e-5"/>
```

or using SofaPython3:

``` python
node.addObject('CGLinearSolver', iterations='100' tolerance='1e-5' threshold='1e-5')
```

A lot of scene examples are available in SOFA involving a CGLinearSolver. One is available in [*examples/Demos/liver.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Demos/liver.scn)