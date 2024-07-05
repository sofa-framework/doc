---
title: Shadowing
---

Shadows
-------

Shadow Mapping has been implemented in SOFA, in order to have a better
depth feeling (and an overall nicer scene...) Two versions has been
coded :

-   hard shadows : quick and not so bad visually,
-   soft shadows : requires more GPU processing, but nicer than
    hard shadows.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[caption id="attachment\_1419" align="alignnone" width="400"\][![Hard shadows](https://www.sofa-framework.org/wp-content/uploads/2015/01/Hard_shadows.jpg){.wp-image-1419 width="400" height="300"}](https://www.sofa-framework.org/wp-content/uploads/2015/01/Hard_shadows.jpg) Hard shadows\[/caption\]   \[caption id="attachment\_1420" align="alignnone" width="400"\][![Soft shadows](https://www.sofa-framework.org/wp-content/uploads/2015/01/Soft_shadows1.jpg){.wp-image-1420 width="400" height="300"}](https://www.sofa-framework.org/wp-content/uploads/2015/01/Soft_shadows1.jpg) Soft shadows\[/caption\]
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

(example in [*examples/Component/Visual/OglShadowShader.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/Visual/OglShadowShader.scn))

#### Enabling Shadows

First, you have a light in your scene in order to have shadows
(obviously). And you will need two more objects :

```xml
 
```

As you may guess, the important parameter here is **softShadows** which
if true, enable soft shadows, else enable only hard shadows. Put these
at the root of your scene file, if you want to cast shadows for all the
visual objects in your scene. Finally, press **CONTROL + L** to draw
shadows when simulating. If you don't want to activate it manually,
simply add the parameter shadows to true, which will automatically draws
shadows.

#### Customize Shadows

Default parameters may be not sufficient for your needs (speed,
rendering quality). One important parameter located in Light\* object is
the texture size, which is used in shadow mapping algorithm.

```xml
```

For hard shadows, greater the number is, **more precise** the shadow
will be, but slower the scene will be ... But for soft shadows, greater
the number is, **fuzzier** the shadow will be. So try to have a good
balance between speed and rendering quality.

\[caption id="attachment\_1430" align="alignnone"
width="401"\][![Hard\_shadows\_128](https://www.sofa-framework.org/wp-content/uploads/2015/01/Hard_shadows_1281.jpg){.wp-image-1430
width="401"
height="300"}](https://www.sofa-framework.org/wp-content/uploads/2015/01/Hard_shadows_1281.jpg)
Hard shadows with 128x128 texture size\[/caption\]

\[caption id="attachment\_1431" align="alignnone"
width="401"\][![Hard\_shadows\_2048](https://www.sofa-framework.org/wp-content/uploads/2015/01/Hard_shadows_20481.jpg){.wp-image-1431
width="401"
height="300"}](https://www.sofa-framework.org/wp-content/uploads/2015/01/Hard_shadows_20481.jpg)
Hard shadows with 2048x2048 texture size\[/caption\]

\[caption id="attachment\_1432" align="alignnone"
width="401"\][![Soft\_shadows\_128](https://www.sofa-framework.org/wp-content/uploads/2015/01/Soft_shadows_1281.jpg){.wp-image-1432
width="401"
height="300"}](https://www.sofa-framework.org/wp-content/uploads/2015/01/Soft_shadows_1281.jpg)
Soft shadows with 128x128 texture size\[/caption\]

\[caption id="attachment\_1433" align="alignnone"
width="401"\][![Soft\_shadows\_512](https://www.sofa-framework.org/wp-content/uploads/2015/01/Soft_shadows_5121.jpg){.wp-image-1433
width="401"
height="300"}](https://www.sofa-framework.org/wp-content/uploads/2015/01/Soft_shadows_5121.jpg)
Soft shadows with 512x512 texture size\[/caption\]

\[caption id="attachment\_1434" align="alignnone"
width="401"\][![Soft\_shadows\_2048](https://www.sofa-framework.org/wp-content/uploads/2015/01/Soft_shadows_2048.jpg){.wp-image-1434
width="401"
height="300"}](https://www.sofa-framework.org/wp-content/uploads/2015/01/Soft_shadows_2048.jpg)
Soft shadows with 2048x2048 texture size\[/caption\]
