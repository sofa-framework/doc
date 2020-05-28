Sofa Mouse Manager
------------------

A Mouse Manager has been created in Sofa, allowing to easily create and
change the interactions with the different buttons of the Mouse. Note that the Shift key needs to be hold during the operation. 
This panel is available through: *Edit -&gt; Mouse Manager*
[![SofaMouseManager\_GUI](https://www.sofa-framework.org/wp-content/uploads/2014/11/SofaMouseManager_GUI1.png){.aligncenter
.size-full .wp-image-1510 width="460"
height="544"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/SofaMouseManager_GUI1.png)
The basic interactions are from now (see below parts for further
informations):

-   **Attach an object to the Mouse:** when clicked, the mouse casts a ray,
    and create a spring between a point in the ray, and a DOF
    encountered (if one has been found in the proximity of the ray)
-   **Fix picked particle:** when clicked, the particle of the collision
    model near the mouse is fixed using a stiff spring.
-   **Incise along a path:** pressing the mouse, you can proceed to an
    incision following the path of the mouse. (Only available for
    triangular mesh)
-   **Perform topological operations:** useful to make some
    topological changes. Only primitive removal available for
    the moment.
-   **Add a spring to suture two points:** allow to create a spring, with a
    null rest length, between two points, in order to join them.
-   **Add a Frame to Skinned model:** TODO
-   **Save camera's view points for navigation:** TODO
-   **Start navigation if camera's view point have been saved:** TODO

Operations available
--------------------

Further informations for specific mouse interactions.

### Attach an object to the Mouse

when clicked, the mouse casts a ray, and create a spring between a point
in the ray, and a DOF encountered (if one has been found in the
proximity of the ray) When clicking on shift, collision model will
appear (first figure), Then clicking with button mouse without releasing
shift will allow to move selected dof (second figure). Then, releasing
mouse button will let the object come back to it rest position (if the
mechanical behavior allows it). Whereas releasing shift first will
freeze the object in the current position.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![200px-Attach\_01](https://www.sofa-framework.org/wp-content/uploads/2014/11/200px-Attach_011.png)](https://www.sofa-framework.org/wp-content/uploads/2014/11/200px-Attach_011.png) Area selected   [![200px-Attach\_02](https://www.sofa-framework.org/wp-content/uploads/2014/11/200px-Attach_021.png)](https://www.sofa-framework.org/wp-content/uploads/2014/11/200px-Attach_021.png) Area attached with a spring and pulled
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Fix picked particle

when clicked, the particle of the collision model near the mouse is
fixed using a stiff spring. When shift is pushed, collision model will
appear (first figure), Then clicking with button mouse will fix the
particle of the collision model near the mouse using a stiff spring.

|Area selected                    |Area fixed by a stiff spring |                         
|:-------------------------------:|:-----------------------------:|
|[![200px-Attach\_01](https://www.sofa-framework.org/wp-content/uploads/2014/11/200px-Attach_011.png){.wp-image-1511 .size-full width="200" height="144"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/200px-Attach_011.png) | [![200px-Fixed\_01](https://www.sofa-framework.org/wp-content/uploads/2014/11/200px-Fixed_011.png){.wp-image-1513 .size-full width="200" height="131"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/200px-Fixed_011.png) |

### Incise along a path

This operation allow to simulate incision on a triangular mesh. There
are two methods available for performing incision:

-   Through segmentIn this method, first click set starting position of
    the incision and second click set ending position. Then incision
    will be performed between these points. If you don't release "shift"
    button then you can continue clicking. Incision will be performed
    between previous point and this new one. Thus you can obtain
    successive incisions. (see fig1 to fig3) \[caption
    id="attachment\_1515" align="alignright"
    width="417"\][![MouseManager GUI for
    Incision](https://www.sofa-framework.org/wp-content/uploads/2014/11/SofaMouseManager_GUI_Incision1.png){.size-full
    .wp-image-1515 width="417"
    height="238"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/SofaMouseManager_GUI_Incision1.png)
    MouseManager GUI for Incision\[/caption\] Advanced settings are
    available for this method:
    1.  Distance to snap from border: This allow to perform incision
        until or from mesh borders (see figures behind). To do this, you
        need to click near a border. Thus, this parameter define the
        area in which the position of the click will be "assimilate" as
        on the border. To go further into details, for a triangle on the
        border of the mesh. This area is defined by the border and at
        maximum it's barycentric point. Thus taking a value of 100%
        means that a click between the border and the barycentric point
        will be considered as a click on the border. In this case, two
        options appear. Either the click is near a vertex (on the
        border), and then incision will be expand to this last on. Or
        incision is perform until the orthogonal projection of point
        clicked, on the border.
    2.  Distance to snap along path: This allow to perform an incision
        without creating small triangles along the incision path. For
        example, if the incision path pass near a point of a triangle,
        instead of cutting the edges and thus create a new small
        triangle, this last point will be moved on the incision path.
        Here again the pourcentage is link to the area. Thus for a value
        of 100%, this mean that it the incision pass between a point and
        the barycentric point. This last point will be moved.

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      \[caption id="attachment\_1516" align="aligncenter" width="150"\][![Triangular Mesh (under gravity)](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-Incision_011.png){.size-full .wp-image-1516 width="150" height="150"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-Incision_011.png) Triangular Mesh (under gravity)\[/caption\]   \[caption id="attachment\_1517" align="aligncenter" width="150"\][![First incision](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-Incision_02.png){.size-full .wp-image-1517 width="150" height="150"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-Incision_02.png) First incision\[/caption\]   \[caption id="attachment\_1518" align="aligncenter" width="150"\][![Piece of sheet is being removed](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-Incision_031.png){.size-full .wp-image-1518 width="150" height="150"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-Incision_031.png) PIece of sheet is being removed\[/caption\]   \[caption id="attachment\_1519" align="aligncenter" width="150"\][![Second incision](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-Incision_041.png){.size-full .wp-image-1519 width="150" height="150"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-Incision_041.png) Second incision\[/caption\]   \[caption id="attachment\_1520" align="aligncenter" width="150"\][![Bottom part of the sheet is falling down](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-Incision_051.png){.size-full .wp-image-1520 width="150" height="150"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-Incision_051.png) Bottom part of the sheet is falling down\[/caption\]
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   ContinuallyIn this second method, first click will initialize the
    incision and then the incision will follow mouse movement (like if
    the mouse was a scalpel). Here again, "shift" release will end
    the incision. For the moment, this method doesn't handle
    snapping options.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      \[caption id="attachment\_1516" align="aligncenter" width="150"\][![Triangular Mesh (under gravity)](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-Incision_011.png){.size-full .wp-image-1516 width="150" height="150"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-Incision_011.png) Triangular Mesh (under gravity)\[/caption\]   \[caption id="attachment\_1524" align="aligncenter" width="150"\][![Start incision](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-Incision_02bis.png){.size-full .wp-image-1524 width="150" height="157"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-Incision_02bis.png) Start incision\[/caption\]   \[caption id="attachment\_1525" align="aligncenter" width="150"\][![Continuous incision](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-Incision_03bis.png){.size-full .wp-image-1525 width="150" height="157"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-Incision_03bis.png) Continuous incision\[/caption\]
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Perform topological operations

Different kind of topological operations are available:

-   Remove an element: This operation allow to remove a topological
    element (surface or volume depending on the type of collision model)
    . Notes that it is possible to remove a volume element using a
    surface collision model if the scene contains a Topological Mapping.
-   Remove a zone of elements: This operation allow to remove a zone of
    element (circle for surface, sphere for volume). Different situation
    can be encountered depending on which kind of collision model is
    used. \[caption id="attachment\_1541" align="alignright"
    width="414"\][![Topological Operations menu
    GUI](https://www.sofa-framework.org/wp-content/uploads/2014/11/SofaMouseManager_GUI_topology1.png){.size-full
    .wp-image-1541 width="414"
    height="174"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/SofaMouseManager_GUI_topology1.png)
    Topological Operations menu GUI\[/caption\]
    -   For surface collision model:
        1.  On a surface mesh it will remove a part of the mesh
            (see fig)
              --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
              \[caption id="attachment\_1533" align="aligncenter" width="150"\][![Selected Triangles](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-RemoveTri011.png){.size-full .wp-image-1533 width="150" height="182"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-RemoveTri011.png) Selected Triangles\[/caption\]   \[caption id="attachment\_1534" align="aligncenter" width="150"\][![Removed Triangles](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-RemoveTri021.png){.size-full .wp-image-1534 width="150" height="182"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-RemoveTri021.png) Removed Triangles\[/caption\]
              --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        2.  On a volume mesh using the option surface will remove
            surface element as well as volume element link to them (this
            can let sharp element at the surface see fig). Using the
            option Volume will remove a sphere volume of elements (see
            fig on right)
              ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
              \[caption id="attachment\_1536" align="aligncenter" width="150"\][![Corresponding Tetrahedra removed](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-RemoveTetra021.png){.size-full .wp-image-1536 width="150" height="182"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-RemoveTetra021.png) Corresponding Tetrahedra removed\[/caption\]   \[caption id="attachment\_1534" align="aligncenter" width="150"\][![Removed Triangles](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-RemoveTri021.png){.size-full .wp-image-1534 width="150" height="182"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-RemoveTri021.png) Removed Triangles\[/caption\]   \[caption id="attachment\_1537" align="aligncenter" width="150"\][![Visual model of the modified volume (Surface Option)](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-RemoveTetra03.png){.size-full .wp-image-1537 width="150" height="182"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-RemoveTetra03.png) Visual model of the modified volume\[/caption\]   \[caption id="attachment\_1539" align="aligncenter" width="150"\][![Visual model of the modified volume (Volume Option)](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-RemoveTri03.png){.size-full .wp-image-1539 width="150" height="182"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-RemoveTri03.png) Visual model of the modified volume (Volume Option)\[/caption\]
              ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    -   For volume collision model:
        1.  Using the Volume option will have the same results as above
            (remove a sphere volume of elements)
        2.  Using the Surface option will remove a layer of element at
            the surface of the mesh (see fig)

          ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
          \[caption id="attachment\_1543" align="aligncenter" width="150"\][![Selected Tetrahedra](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-RemoveTetra04.png){.size-full .wp-image-1543 width="150" height="182"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-RemoveTetra04.png) Selected Tetrahedra\[/caption\]   \[caption id="attachment\_1544" align="aligncenter" width="150"\][![Removed Tetrahedra (Volume Option)](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-RemoveTetra05.png){.size-full .wp-image-1544 width="150" height="182"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-RemoveTetra05.png) Removed Tetrahedra (Volume Option)\[/caption\]   \[caption id="attachment\_1545" align="aligncenter" width="150"\][![Second selection](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-RemoveTetra06.png){.size-full .wp-image-1545 width="150" height="182"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-RemoveTetra06.png) Second selection\[/caption\]   \[caption id="attachment\_1546" align="aligncenter" width="150"\][![Removed Tetrahedra (with Surface Option)](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-RemoveTetra07.png){.size-full .wp-image-1546 width="150" height="182"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/150px-RemoveTetra07.png) Removed Tetrahedra (with Surface Option)\[/caption\]
          ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Add a spring to suture two points

TODO

### Add a Frame to Skinned model

TODO
