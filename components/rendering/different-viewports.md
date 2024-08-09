---
title: Different Viewports
---

Using different views in OpenGL
-------------------------------

You can get different points of view of your scene. It can be useful if
you want to watch something for example. In order to get those
viewports, you have to add :

```xml
<OglViewport screenPosition="0 0" screenSize="250 250" cameraPosition="-1 2.7 5" cameraOrientation="-0 -0 -0 1" />
```

where :

-   screenPosition = : position on the viewer
-   screenSize = : size of the viewport
-   cameraPosition = : position of the camera in eye's space
-   cameraOrientation = : camera's orientation (direction and
    up vectors)

**cameraPosition** and **cameraOrientation** can be easily retrieved,
using viewer's view file: get the view you want to add with the main
viewer, save the view, open the resulting yourscene.scn.view file and
copy-paste the 2 vectors into the corresponding fields.

#### Example

-   [example/Component/visualmodel/OglViewport.scn](https://github.com/sofa-framework/sofa/blob/master/examples/Component/Visual/OglViewport.scn)

