How to manage the recorded camera
---------------------------------

In this page, we explain how to manage the recorded camera. The recorded
camera is available on componentSofaBaseVisual. You have three modes to
manipulate the camera: rotation mode, translation mode and navigation
mode.

#### The rotation mode

The camera can rotate, if you define the rotation center, the rotation
axis and the rotation start point. The rotation path is visible if you
check the option "if true, draw the rotation path".

#### The translation mode

This mode enables to move the camera between intermediate camera
positions. The camera path is then defined with a linear spline linking
these intermediate positions.You can select the intermediate positions
on the orthogonal views of the plugin image by double-clicking on the
point. Each time you double-click on a point you have to update the
ImageViewer component. Image:Example.jpg The camera can navigate along
the path with a default view up, if you check the option "if true,
translation will be performed". To draw the translation path check the
option "if true, translation path will be performed". An example
navigationInVolume.scn is available in the plugin image.

-   How is camera orientation defined ? To define the camera
    orientation, you have to determine the look-at vector and the
    view-up vector. The camera looks at the next point of the
    linear spline. To define the up vector, we initialize it with a
    default value. Then in order to guarantee a stability during the
    navigation, the up vector is oriented almost in the
    same orientation. Indeed for each step n, the right vector is
    defined as the cross product between the previous up vector and the
    current focal vector. \[caption id="attachment\_1558"
    align="aligncenter" width="302"\][![Axes of the
    Camera](https://www.sofa-framework.org/wp-content/uploads/2014/11/AxesCamera.jpg){.size-full
    .wp-image-1558 width="302"
    height="214"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/AxesCamera.jpg)
    Axes of the Camera\[/caption\]

#### The navigation mode

The navigation mode enables to move between selected intermediate camera
view points. A view point corresponds to a camera position and a camera
orientation. Therefore, the main difference between navigation mode and
translation mode is that the camera orientation is defined in the
navigation mode by interpolation between intermediate orientations. To
save an intermediate camera view point select in the mouse manager
(*edit-&gt;Mouse manager*) the operation "**Save camera's view point for
navigation**". To navigate select the operation "**Start navigation if
camera's view points have been saved**", which works if at least 2 view
points have been saved. An example navigationRecordedCamera.scn is
available in *examplesComponentsvisualmodel*.
