About Eigen
-----------

[Eigen](http://eigen.tuxfamily.org/index.php?title=Main_Page "http://eigen.tuxfamily.org/index.php?title=Main_Page"){.external
.text} is a linear algebra library written in C++. It is shipped with
the SOFA distribution in extlibs/ []()

Which components in SOFA use Eigen
----------------------------------

Eigen is used by ODE and DAE solvers in the Compliant plugin. The
associated matrix classes, derived from BaseMatrix, are
EigenSparseMatrix and EigenBaseSparseMatrix. Moreover, some older
specific components related to constraint resolution use Eigen. Note
that it is not mandatory to use Eigen to have access to constraint
resolution ! The following components become available when compiling
with Eigen :

-   LMConstraintSolver
-   DistanceLMConstraint
-   DOFBlockerLMConstraint
-   FixedLMConstraint

