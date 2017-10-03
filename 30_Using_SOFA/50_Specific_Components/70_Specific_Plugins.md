Specific Plugins
=======================

Over the time, many components have been implemented in SOFA. 
Some of these components are specific and allows for a particular functionnality.
They have been repackaged into plugins that can be activated / desactivated in the compilation of SOFA.

In this documentation, you will find a brief description of these plugins

### Specific Boudnary Conditions

This plugin gathers components that inherit from Forcefields and Projective Constraints.
Here is the list of the components and their function:
- **OscillatingTorsionPressureForceField** was developped for creating an oscillating torsion (used in the [paper](http://www-sop.inria.fr/asclepios/Publications/Stephanie.Marchesseau/PBMB-Marchesseau-2010.pdf) )
- **AffineMovementConstraint** imposes a motion to all the boundary points of a mesh. The motion of the 4 corners are given in the data m_cornerMovements and the movements of the edge points are computed by linear interpolation.
