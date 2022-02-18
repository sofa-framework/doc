MergePoints
===========

This component belongs to the category of [Engines](https://www.sofa-framework.org/community/doc/simulation-principles/engine/). This engine returns a merged list of positions, given 2 primary lists.

Input Data
----------

-   **position1**: positions of the 1st object
-   **position2**: positions of the 2nd object

Output Data
----------

-   **points**: a new list of positions, containing the 2 previous lists
-   **indices1**: indices of the 1st position list in the new list
-   **indices2**: indices of the 2nd position list in the new list


Examples
--------

An example scene involving the MergePoints engine is available in [*examples/Components/engine/MergePoints.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/engine/MergePoints.scn)