Adding Lights
-------------

One white global light illuminates the scene by default. This can be
changed through a light manager object and a certain number of lights
(limited by OpenGL). The first step is to add the object called
LightManager, preferably at the top of the scene file.

``` {.lang:xhtml .decode:true}
```

After that, we can add 3 different kinds of lights :

-   a positional light (parameters : color, position) ;

    ``` {.lang:xhtml .decode:true}
    ```

-   a directional light (parameters : color, direction) ;

    ``` {.lang:xhtml .decode:true}
    ```

-   a spotlight (parameters : color, position, direction, cut off,
    exponent, attenuation)

    ``` {.lang:xhtml .decode:true}
    ```

<!-- -->


